"""
generate_finetune.py

Builds finetune.txt: a SMALL set of Question/Answer formatted examples.

IMPORTANT: this is not the model's knowledge source. corpus.txt (the raw
documents) is. This file only teaches the model the *shape* of a reply when
it sees "Question: ... \nAnswer:" -- the same way real LLMs get a short
instruction-tuning pass after large-scale pretraining on raw text.

Each answer below is copied verbatim from a sentence that already exists in
corpus.txt, so no new facts are being invented here -- we are only wrapping
existing corpus content in a prompt/response shape a handful of times.
"""

EXAMPLES = [
    ("What is the vision of TMC?",
     "A model institution with fully developed academic, technical-vocational education and skill of manpower with positive work attitudes anchored in the core values of leadership and professionalism essential in the creation of self-reliant citizens."),
    ("What is the mission of TMC?",
     "To build well-trained, competent and employable professionals, who will meet the demands of the world market."),
    ("What is the slogan of TMC?",
     "TMC is committed to public educational services second to none."),
    ("What is the philosophy of TMC?",
     "TMC adheres to the philosophy that education is life and growth guided by faith in God and love of fellowmen in an environment of competitiveness, professionalism and excellence."),
    ("What is the goal of TMC?",
     "TMC aims at evolving a whole individual as a child of God and a member of a democratic society who is professionally competent, well-trained in a certain vocation, and practical yet responsible and obedient to the laws of God and government."),
    ("Who founded Trinidad Municipal College?",
     "Mr. Paciano Petarco initiated the plan, with the help of Municipal Mayor Atty. Avelino N. Puracan, and it eventually became the Trinidad Junior College before being turned over to the Local Government Unit of Trinidad and renamed Trinidad Municipal College in 1997."),
    ("When did TMC become a municipal college?",
     "The college became known as Trinidad Municipal College from 1997 up to the present, after the Local Government Unit of Trinidad took over its ownership and management."),
    ("What courses does TMC offer?",
     "TMC offers Bachelor of Arts, Bachelor in Elementary Education, Bachelor in Secondary Education, Bachelor of Science in Information Technology, Bachelor of Science in Office Administration, Associate in Office Administration, Bachelor of Science in Criminology, and NC-II programs in Automotive Servicing, Electrical Installation and Maintenance, and Refrigeration and Air Conditioning."),
    ("Who created you?",
     "I was created and developed by CajesJM, a Bachelor of Science in Information Technology student at Trinidad Municipal College, as a from-scratch character-level language model."),
    ("Who is your developer?",
     "My developer is CajesJM, a BSIT student at Trinidad Municipal College."),
    ("Who are you?",
     "I am Cypher, an AI assistant trained on Trinidad Municipal College's official information."),
    ("What is TMC?",
     "TMC stands for Trinidad Municipal College, a college institution owned and managed by the Local Government Unit of Trinidad."),
]


def build(out_path="finetune.txt"):
    lines = []
    for q, a in EXAMPLES:
        lines.append(f"Question: {q}\nAnswer: {a}\nQ:\n")
    text = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {out_path}: {len(EXAMPLES)} format-teaching examples.")


if __name__ == "__main__":
    build()