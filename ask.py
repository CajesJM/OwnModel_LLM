import re
import sys
import time
import torch
from model import MiniGPT
from tokenizer import CharTokenizer

n_embd = 128
n_head = 4
n_layer = 4
block_size = 512
dropout = 0.0

tokenizer = CharTokenizer.load('tokenizer.json')
model = MiniGPT(tokenizer.vocab_size, n_embd, n_head, n_layer, block_size, dropout)
model.load_state_dict(torch.load('tmc_model.pt', map_location='cpu'))
model.eval()


def type_out(text, delay=0.015):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ---------------------------------------------------------------------------
# Scope check: is this question about something actually in our data?
# Built dynamically from corpus.txt, so it automatically covers whatever
# documents you drop into data/raw/ -- no hardcoded content keyword list.
#
# Separately, a small CHIT-CHAT allowlist handles greetings / "who are you"
# style questions -- these are pure conversation routing, not answer content,
# so they're fine to special-case (the actual answer still comes from the
# model, not from this list).
# ---------------------------------------------------------------------------
STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "of", "in", "on", "to",
    "and", "or", "for", "what", "who", "when", "where", "why", "how",
    "does", "do", "did", "can", "you", "your", "me", "tell", "about",
    "please", "i", "want", "know", "this", "that", "it", "its", "with",
    "as", "be", "by", "at", "from", "has", "have", "will", "which",
}

CHITCHAT_TRIGGERS = (
    "hi", "hello", "hey", "yo", "good morning", "good afternoon", "good evening",
    "who are you", "what are you", "introduce yourself", "your name",
    "are you an ai", "are you a bot", "are you human", "who made you",
    "who created you", "who is your developer", "who built you",
)

with open('corpus.txt', 'r', encoding='utf-8') as f:
    _corpus_text = f.read()

_corpus_words = set(re.findall(r"[a-zA-Z']+", _corpus_text.lower())) - STOPWORDS

FALLBACK_ANSWER = "I don't know that. I can only answer based on the data I was trained on (TMC's history, vision, mission, slogan, philosophy, and goal)."


def is_in_scope(question):
    norm = question.lower().strip()

    if any(norm == t or norm.startswith(t) for t in CHITCHAT_TRIGGERS):
        return True

    words = set(re.findall(r"[a-zA-Z']+", norm)) - STOPWORDS
    if not words:
        return False
    return len(words & _corpus_words) > 0


def generate_answer(question):
    prompt = f"Question: {question}\nAnswer:"
    input_ids = torch.tensor([tokenizer.encode(prompt)], dtype=torch.long)
    out_ids = model.generate(
        input_ids, max_new_tokens=250, tokenizer=tokenizer, stop_str="Q:",
        temperature=0.7, top_k=10, repetition_penalty=1.3,
    )
    full_text = tokenizer.decode(out_ids[0].tolist())
    if "Answer:" in full_text:
        answer = full_text.split("Answer:", 1)[1]
        if "Q:" in answer:
            answer = answer.split("Q:")[0]
        return answer.strip()
    return full_text.strip()


def answer_question(question):
    if not is_in_scope(question):
        return FALLBACK_ANSWER
    answer = generate_answer(question)
    if not answer:
        return FALLBACK_ANSWER
    return answer


if __name__ == "__main__":
    print("=========================================")
    print("Cypher - TMC AI Assistant (by CajesJM)")
    print("Ask me about TMC. Type 'exit' to quit.")
    print("=========================================")

    while True:
        question = input("You: ")
        if question.lower() in ("exit", "quit", "bye"):
            break
        ans = answer_question(question)
        sys.stdout.write("Cypher: ")
        type_out(ans)
        print()