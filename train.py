import torch
from torch.optim import AdamW
from model import MiniGPT
from tokenizer import CharTokenizer

# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------
n_embd = 128
n_head = 4
n_layer = 4
block_size = 512
dropout = 0.1

pretrain_iters = 4000     # Phase A: learn language + facts from raw corpus.txt
pretrain_lr = 3e-3

finetune_iters = 2000      # Phase B: learn the Question/Answer reply format
finetune_lr = 3e-4
rehearsal_ratio = 0.4       # fraction of Phase B steps that replay corpus.txt
                             # instead of finetune.txt -- this is what stops
                             # the model from "forgetting" fluent language
                             # while it overfits to only 12 Q&A examples

eval_interval = 500
grad_clip = 1.0

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
with open('corpus.txt', 'r', encoding='utf-8') as f:
    corpus_text = f.read()

with open('finetune.txt', 'r', encoding='utf-8') as f:
    finetune_text = f.read()

tokenizer = CharTokenizer(corpus_text + finetune_text)
tokenizer.save('tokenizer.json')
vocab_size = tokenizer.vocab_size
print(f"Vocab size: {vocab_size}")

corpus_ids = torch.tensor(tokenizer.encode(corpus_text), dtype=torch.long)
print(f"Corpus length: {len(corpus_ids)} tokens")

finetune_blocks = [b for b in finetune_text.strip().split('\n\n') if b.strip()]
finetune_seqs = [torch.tensor(tokenizer.encode(b + "\n"), dtype=torch.long) for b in finetune_blocks]
print(f"Finetune examples: {len(finetune_seqs)}")

model = MiniGPT(vocab_size, n_embd, n_head, n_layer, block_size, dropout)


def get_batch_from_corpus():
    """Random contiguous crop of the raw corpus -- pure next-token prediction,
    no Q/A framing. This is what makes the model actually read the document."""
    max_start = len(corpus_ids) - block_size - 1
    start = torch.randint(0, max(max_start, 1), (1,)).item()
    chunk = corpus_ids[start:start + block_size + 1]
    if len(chunk) < 2:
        chunk = corpus_ids[:block_size + 1]
    x = chunk[:-1].unsqueeze(0)
    y = chunk[1:].unsqueeze(0)
    return x, y


def get_batch_from_finetune():
    idx = torch.randint(len(finetune_seqs), (1,)).item()
    seq = finetune_seqs[idx]
    if len(seq) > block_size + 1:
        seq = seq[:block_size + 1]
    if len(seq) < 2:
        return get_batch_from_finetune()
    x = seq[:-1].unsqueeze(0)
    y = seq[1:].unsqueeze(0)
    return x, y


def sample(question):
    model.eval()
    with torch.no_grad():
        prompt = f"Question: {question}\nAnswer:"
        input_ids = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long)
        out_ids = model.generate(input_ids, max_new_tokens=250, tokenizer=tokenizer, stop_str="Q:")
        text = tokenizer.decode(out_ids[0].tolist())
        ans = text.split("Answer:", 1)[1] if "Answer:" in text else text
        ans = ans.split("Q:")[0].strip()
    model.train()
    return ans


test_questions = ["What is the mission of TMC?", "Who created you?"]

# ---------------------------------------------------------------------------
# Phase A: pretrain on the raw document (the actual fix for "let it read the data")
# ---------------------------------------------------------------------------
print("\n=== Phase A: pretraining on raw corpus.txt ===")
optimizer = AdamW(model.parameters(), lr=pretrain_lr)
for it in range(pretrain_iters):
    x, y = get_batch_from_corpus()
    _, loss = model(x, y)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
    optimizer.step()
    if it % eval_interval == 0:
        print(f"  [pretrain] step {it}: loss {loss.item():.4f}")

# ---------------------------------------------------------------------------
# Phase B: fine-tune on Question/Answer format, WITH rehearsal so the model
# doesn't forget the fluent language it just learned in Phase A.
# ---------------------------------------------------------------------------
print("\n=== Phase B: fine-tuning on Question/Answer format (with rehearsal) ===")
optimizer = AdamW(model.parameters(), lr=finetune_lr)
for it in range(finetune_iters):
    if torch.rand(1).item() < rehearsal_ratio:
        x, y = get_batch_from_corpus()
    else:
        x, y = get_batch_from_finetune()
    _, loss = model(x, y)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), grad_clip)
    optimizer.step()
    if it % eval_interval == 0:
        print(f"  [finetune] step {it}: loss {loss.item():.4f}")
        for q in test_questions:
            print(f"    Q: {q}\n    A: {sample(q)[:150]}")

torch.save(model.state_dict(), 'tmc_model.pt')
print("\nModel saved to tmc_model.pt")