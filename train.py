import torch
import torch.nn.functional as F
from torch.optim import AdamW
from model import MiniGPT
from tokenizer import CharTokenizer

# Hyperparameters
batch_size = 1
block_size = 400
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.0
learning_rate = 1e-3        
max_iters = 15000
eval_interval = 1000

with open('train.txt', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = text.strip().split('\n\n')
pairs = []
for block in blocks:
    lines = block.strip().split('\n')
    if len(lines) >= 2 and lines[0].startswith('Q:') and lines[1].startswith('A:'):
        question = lines[0][3:]
        answer = lines[1][3:]
        pairs.append((question, answer))

print(f"Found {len(pairs)} Q:A pairs")

# Build tokenizer
tokenizer = CharTokenizer(text)
tokenizer.save('tokenizer.json')
vocab_size = tokenizer.vocab_size

# Convert pairs to tensor sequences
data = []
for q, a in pairs:
    prompt = f"Q: {q}\nA:"
    completion = a + "Q:\n"
    full_seq = prompt + completion
    encoded = tokenizer.encode(full_seq)
    data.append(torch.tensor(encoded, dtype=torch.long))

model = MiniGPT(vocab_size, n_embd, n_head, n_layer, block_size, dropout)
optimizer = AdamW(model.parameters(), lr=learning_rate)

# Learning rate scheduler: after 12000 steps, reduce by factor of 10
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=12000, gamma=0.1)

def get_sample(model, tokenizer, question):
    prompt = f"Q: {question}\nA:"
    input_ids = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long)
    out_ids = model.generate(input_ids, max_new_tokens=400)
    full_gen = tokenizer.decode(out_ids[0].tolist())
    if "A:" in full_gen:
        ans = full_gen.split("A:", 1)[1]
        if "Q:" in ans:
            ans = ans.split("Q:")[0]
        return ans.strip()
    return full_gen.strip()

# Training loop
for iter in range(max_iters):
    # Sample a random pair
    idx = torch.randint(len(data), (1,)).item()
    seq = data[idx]
    if len(seq) > block_size:
        start = torch.randint(len(seq) - block_size + 1, (1,)).item()
        seq = seq[start:start + block_size]
    x = seq[:-1].unsqueeze(0)   # (1, seq_len-1)
    y = seq[1:].unsqueeze(0)

    logits, loss = model(x, y)

    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    scheduler.step()

    if iter % eval_interval == 0:
        model.eval()
        with torch.no_grad():
            # Test multiple questions
            test_qs = [
                "What is the mission of TMC?",
                "Who created this AI?",
                "Unsa ang misyon sa TMC?"
            ]
            print(f"step {iter}: loss {loss.item():.4f}, lr {scheduler.get_last_lr()[0]:.2e}")
            for q in test_qs:
                ans = get_sample(model, tokenizer, q)
                print(f"  Q: {q}\n  A: {ans[:100]}...")
            print()
        model.train()

# Final loss
model.eval()
with torch.no_grad():
    idx = 0
    seq = data[idx]
    if len(seq) > block_size:
        seq = seq[:block_size]
    x = seq[:-1].unsqueeze(0)
    y = seq[1:].unsqueeze(0)
    _, final_loss = model(x, y)
print(f"Final loss: {final_loss.item():.6f}")
torch.save(model.state_dict(), 'tmc_model.pt')
print("Model saved.")