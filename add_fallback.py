fallback_pairs = []

english_fallbacks = [
    "What is the capital of France?",
    "Who is the president of the Philippines?",
    "What time is it?",
    "How are you?",
    "Can you dance?",
    "What's the weather like?",
    "Tell me a joke.",
    "Do you love me?",
    "What is your favorite color?",
    "Are you a robot?",
    "Can you help me with my homework?",
    "What is the meaning of life?",
    "How to cook adobo?",
    "What is Python?",
    "Where is the nearest hospital?",
    "How old are you?",
    "What is your name?",
    "Do you know Siri?",
]

cebuano_fallbacks = [
    "Unsa ang oras?",
    "Kumusta ka?",
    "Asa ang pinakaduol nga ospital?",
    "Unsa imong ngalan?",
    "Pwede ka mosayaw?",
    "Unsa ang imong paborito nga kolor?",
    "Tagai kog joke.",
    "Unsa ang panahon karon?",
    "Mahimo ba nimo akong tabangan sa akong homework?",
    "Kinsa ang presidente sa Pilipinas?",
    "Unsa ang kapital sa France?",
]

tagalog_fallbacks = [
    "Anong oras na?",
    "Kumusta ka?",
    "Saan ang pinakamalapit na ospital?",
    "Ano ang pangalan mo?",
    "Marunong ka bang sumayaw?",
    "Ano ang paborito mong kulay?",
    "Magbigay ka ng joke.",
    "Ano ang panahon ngayon?",
    "Pwede mo ba akong tulungan sa homework ko?",
    "Sino ang presidente ng Pilipinas?",
    "Ano ang kabisera ng France?",
]

# The fixed fallback answer (you can use a single consistent answer)
fallback_answer_en = "I'm sorry, I can only answer questions about TMC's vision, mission, slogan, philosophy, goal, and creator."
fallback_answer_ceb = "Pasayloa ko, makatubag ra ko og mga pangutana bahin sa panan-awon, misyon, slogan, pilosopiya, tumong, ug tiglalang sa TMC."
fallback_answer_tag = "Paumanhin, ang kaya ko lang sagutin ay mga tanong tungkol sa pananaw, misyon, slogan, pilosopiya, layunin, at tagalikha ng TMC."

# Combine
all_fallbacks = []
for q in english_fallbacks:
    all_fallbacks.append(f"Q: {q}\nA: {fallback_answer_en}\n")
for q in cebuano_fallbacks:
    all_fallbacks.append(f"Q: {q}\nA: {fallback_answer_ceb}\n")
for q in tagalog_fallbacks:
    all_fallbacks.append(f"Q: {q}\nA: {fallback_answer_tag}\n")

# Append to existing train.txt (don't overwrite)
with open('train.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join(all_fallbacks))

print(f"Added {len(all_fallbacks)} fallback examples to train.txt")