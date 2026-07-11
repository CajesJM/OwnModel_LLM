import torch
from model import MiniGPT
from tokenizer import CharTokenizer


n_embd = 128
n_head = 4
n_layer = 4
block_size = 400
dropout = 0.0

tokenizer = CharTokenizer.load('tokenizer.json')
model = MiniGPT(tokenizer.vocab_size, n_embd, n_head, n_layer, block_size, dropout)
model.load_state_dict(torch.load('tmc_model.pt', map_location='cpu'))
model.eval()

def answer_question(question):
    prompt = f"Q: {question}\nA:"
    input_ids = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long)
    out_ids = model.generate(input_ids, max_new_tokens=500)
    full_text = tokenizer.decode(out_ids[0].tolist())

    if "A:" in full_text:
        answer = full_text.split("A:", 1)[1]
        if "Q:" in answer:
            answer = answer.split("Q:")[0]
        answer = answer.strip()
    else:
        answer = full_text.strip()
    return answer

print("=========================================")
print("🤖 TMC AI Assistant (by Jm)")
print("Ask me about TMC's vision, mission, goal, etc. Type 'exit' to quit.\n")
print("=========================================")

while True:
    question = input("You: ")
    if question.lower() in ("exit", "quit"):
        break
    ans = answer_question(question)
    print(f"Arisu.exe: {ans}\n")