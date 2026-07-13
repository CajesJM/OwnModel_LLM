import re
import difflib
import torch
import time
import sys

def type_out(text, delay=0.015):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()
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

def load_pairs(path='train.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = content.strip().split('\n\n')
    pairs = []
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 2 and lines[0].startswith('Q:') and lines[1].startswith('A:'):
            q = lines[0][3:].strip()
            a = lines[1][3:].strip()
            pairs.append((q, a))
    return pairs

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\s+', ' ', text)       
    return text

_pairs = load_pairs()
_norm_to_answer = {}
for q, a in _pairs:
    _norm_to_answer[normalize(q)] = a
_all_norm_questions = list(_norm_to_answer.keys())

def find_answer(question, cutoff=0.6):
    
    norm = normalize(question)
    if norm in _norm_to_answer:
        return _norm_to_answer[norm]
    matches = difflib.get_close_matches(norm, _all_norm_questions, n=1, cutoff=cutoff)
    if matches:
        return _norm_to_answer[matches[0]]
    return None

TOPIC_KEYWORDS = [
    "vision", "envision", "panan-awon", "pananaw",
    "mission", "misyon", "purpose", "katuyoan", "layunin",
    "slogan", "motto", "tagline", "catchphrase",
    "philosophy", "pilosopiya", "principle", "prinsipyo", "believe", "gituohan", "paniniwalaan",
    "goal", "goals", "objective", "tinguha", "adhikain", "target",
    "creator", "created", "made you", "developer", "cajesjm", "naghimo", "gumawa", "lumikha", "programmed",
    "stands for", "what is tmc", "about tmc",
    "who are you", "what are you", "are you an ai", "introduce yourself",
]

FALLBACK_ANSWER = "I'm sorry, I can only answer questions about TMC's vision, mission, slogan, philosophy, goal, and creator."
CLARIFY_ANSWER = "Please specify what about TMC you'd like to know: vision, mission, slogan, philosophy, goal, or creator."

def is_in_scope(question):
    q = question.lower()
    return any(kw in q for kw in TOPIC_KEYWORDS)

def generate_answer(question):
    prompt = f"Q: {question}\nA:"
    input_ids = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long)
    out_ids = model.generate(input_ids, max_new_tokens=500, tokenizer=tokenizer)
    full_text = tokenizer.decode(out_ids[0].tolist())
    if "A:" in full_text:
        answer = full_text.split("A:", 1)[1]
        if "Q:" in answer:
            answer = answer.split("Q:")[0]
        return answer.strip()
    return full_text.strip()

def answer_question(question):
    norm = normalize(question)

    if norm == "tmc":
        return CLARIFY_ANSWER

    matched = find_answer(question)
    if matched:
        return matched

    if is_in_scope(question):
        return generate_answer(question)

    return FALLBACK_ANSWER

print("=========================================")
print("🤖 TMC AI Assistant (by Jm)")
print("Ask me about TMC's vision, mission, goal, etc. Type 'exit' to quit.\n")
print("=========================================")

while True:
    question = input("You: ")
    if question.lower() in ("exit", "quit" , "bye"):
        break
    ans = answer_question(question)
    sys.stdout.write("Cypher: ")
    type_out(ans)
    print()