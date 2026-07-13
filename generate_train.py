import random

facts = {
    "vision": {
        "en": "A model institution with fully developed academic, technical-vocational education and skill of manpower with positive work attitudes anchored in the core values of leadership and professionalism essential in the creation of self-reliant citizens.",
        "ceb": "Usa ka modelo nga institusyon nga adunay hingpit nga pagpalambo sa akademiko, teknikal-bokasyonal nga edukasyon ug kahanas sa mga tawo nga adunay positibo nga pamatasan sa trabaho nga nakasalalay sa mga kinauyokang bili sa liderato ug propesyonalismo nga hinungdanon sa paghimo og kaugalingong masaligang lungsuranon.",
        "tag": "Isang modelong institusyon na may ganap na akademiko, teknikal-bokasyonal na edukasyon at kasanayan ng mga tao na may positibong pag-uugali sa trabaho na nakasalig sa mga pangunahing halaga ng pamumuno at propesyonalismo na mahalaga sa paglikha ng mga mamamayang may sariling kakayahan."
    },
    "mission": {
        "en": "To build well-trained, competent and employable professionals, who will meet the demands of the world market.",
        "ceb": "Ang pagtukod og maayong pagkabansay, takos ug andam nga mga propesyonal nga makatubag sa panginahanglan sa tibuok kalibutan nga merkado.",
        "tag": "Bumuo ng mga bihasa, may kakayahan, at handang propesyonal na tutugon sa pangangailangan ng pandaigdigang pamilihan."
    },
    "slogan": {
        "en": "TMC is committed to public educational services second to none.",
        "ceb": "Ang TMC komitado sa publikong serbisyo sa edukasyon nga way sama.",
        "tag": "Ang TMC ay nakatuon sa pampublikong serbisyong pang-edukasyon na walang katulad."
    },
    "philosophy": {
        "en": "TMC adheres to the philosophy that education is life and growth guided by faith in God and love of fellowmen in an environment of competitiveness, professionalism and excellence.",
        "ceb": "Ang TMC nagasunod sa pilosopiya nga ang edukasyon mao ang kinabuhi ug pagtubo nga gigiyahan sa pagtuo sa Diyos ug gugma sa isigkatawo sa palibot nga kompetitibo, propesyonalismo ug kahusay.",
        "tag": "Ang TMC ay sumusunod sa pilosopiya na ang edukasyon ay buhay at pag-unlad na ginagabayan ng pananampalataya sa Diyos at pagmamahal sa kapwa sa isang kapaligiran ng kompetisyon, propesyonalismo at kahusayan."
    },
    "goal": {
        "en": "TMC aims at evolving a whole individual as a child of God and a member of a democratic society who is professionally competent that can provide leadership and advance knowledge, well-trained in a certain vocation not only to help himself but to help others, and practical yet responsible and obedient to the laws of God and to the laws of the government.",
        "ceb": "Tinguha sa TMC nga mahimo ang tibuok nga pagkatawo isip anak sa Diyos ug miyembro sa demokratikong katilingban nga may propesyonal nga katakos, makahatag og liderato ug makapauswag sa kahibalo, hanas sa usa ka bokasyon dili lamang alang sa kaugalingon kundili alang sa uban, ug praktikal apan responsable ug masinugtanon sa mga balaod sa Diyos ug sa gobyerno.",
        "tag": "Layunin ng TMC na hubugin ang isang buong indibidwal bilang anak ng Diyos at kasapi ng demokratikong lipunan na propesyonal na may kakayahan, makapagbibigay ng pamumuno at makapagsulong ng kaalaman, bihasa sa isang bokasyon hindi lamang para sa sarili kundi para sa iba, at praktikal ngunit responsable at masunurin sa mga batas ng Diyos at ng pamahalaan."
    },
    "creator": {
        "en": "CajesJM created this AI assistant for TMC.",
        "ceb": "Si CajesJM ang naghimo niining AI assistant para sa TMC.",
        "tag": "Si CajesJM ang gumawa ng AI assistant na ito para sa TMC."
    },
    "about": {
    "en": "TMC stands for Trinidad Municipal College, a public educational institution located in Trinidad, Bohol, Philippines.",
    "ceb": "Ang TMC nagpasabot og Trinidad Municipal College, usa ka publikong institusyon sa edukasyon nga nahimutang sa Trinidad, Bohol, Pilipinas.",
    "tag": "Ang TMC ay para sa Trinidad Municipal College, isang pampublikong institusyong pang-edukasyon na matatagpuan sa Trinidad, Bohol, Pilipinas."
    },
    "identity": {
    "en": "I am Cypher, the AI assistant of Trinidad Municipal College (TMC). I can answer questions about TMC's vision, mission, slogan, philosophy, goal, and creator.",
    "ceb": "Ako si Cypher, ang AI assistant sa Trinidad Municipal College (TMC). Makatubag ko sa mga pangutana bahin sa vision, mission, slogan, philosophy, goal, ug creator sa TMC.",
    "tag": "Ako si Cypher, ang AI assistant ng Trinidad Municipal College (TMC). Kaya kong sagutin ang mga tanong tungkol sa vision, mission, slogan, philosophy, goal, at creator ng TMC."
    }
}

english_templates = {
    "vision": [
        "What is the vision of TMC?",
        "Tell me about TMC's vision.",
        "Describe the TMC vision statement.",
        "What does TMC envision?",
        "Can you state the vision of TMC?",
        "What's TMC's vision?",
        "I want to know the vision of TMC.",
        "Share the TMC vision.",
        "Give me the TMC vision statement.",
        "What is meant by the vision of TMC?",
        "Explain the vision of TMC.",
        "Could you outline TMC's vision?",
        "What is TMC hoping to achieve according to its vision?",
        "Please repeat the TMC vision.",
        "Vision of TMC?",
        "TMC vision: what is it?",
        "What does TMC aim to become based on its vision?",
        "What's the institutional vision of TMC?",
        "Tell me the vision.",
        "Vision statement of TMC?"
    ],
    "mission": [
        "What is the mission of TMC?",
        "Tell me about TMC's mission.",
        "Describe the TMC mission statement.",
        "What does TMC do according to its mission?",
        "Can you state the mission of TMC?",
        "What's TMC's mission?",
        "I want to know the mission of TMC.",
        "Share the TMC mission.",
        "Give me the TMC mission statement.",
        "What is meant by the mission of TMC?",
        "Explain the mission of TMC.",
        "Could you outline TMC's mission?",
        "What is TMC's purpose?",
        "Please repeat the TMC mission.",
        "Mission of TMC?",
        "TMC mission: what is it?",
        "What does TMC strive to do?",
        "What's the institutional mission of TMC?",
        "Tell me the mission.",
        "Mission statement of TMC?"
    ],
    "slogan": [
        "What is the slogan of TMC?",
        "Tell me TMC's slogan.",
        "What's TMC's motto?",
        "Do you know the TMC slogan?",
        "Can you say the slogan of TMC?",
        "What does TMC's slogan say?",
        "Give me the TMC slogan.",
        "Share the TMC slogan.",
        "What is the official slogan of TMC?",
        "I want to hear the TMC slogan.",
        "Slogan of TMC?",
        "TMC slogan please.",
        "What's the catchphrase of TMC?",
        "What line does TMC use for its slogan?",
        "Tell me the motto of TMC.",
        "What is TMC's tagline?",
        "What does TMC advertise as its slogan?",
        "Do you recall the TMC slogan?",
        "How does TMC present itself in a few words?",
        "TMC's slogan statement?"
    ],
    "philosophy": [
        "What is the philosophy of TMC?",
        "Tell me about TMC's philosophy.",
        "Describe the TMC philosophy.",
        "What is TMC's guiding principle?",
        "Can you state the philosophy of TMC?",
        "What's TMC's philosophy?",
        "I want to know the philosophy of TMC.",
        "Share the TMC philosophy.",
        "Give me the TMC philosophy statement.",
        "What does TMC believe in?",
        "Explain the philosophy of TMC.",
        "Could you outline TMC's philosophy?",
        "What is the educational philosophy of TMC?",
        "Please repeat the TMC philosophy.",
        "Philosophy of TMC?",
        "TMC philosophy: what is it?",
        "What values guide TMC according to its philosophy?",
        "What's the foundational belief of TMC?",
        "Tell me the philosophy.",
        "Philosophy statement of TMC?"
    ],
    "goal": [
        "What is the goal of TMC?",
        "Tell me about TMC's goal.",
        "Describe the TMC goal.",
        "What does TMC aim for?",
        "Can you state the goal of TMC?",
        "What's TMC's goal?",
        "I want to know the goal of TMC.",
        "Share the TMC goal.",
        "Give me the TMC goal statement.",
        "What is the objective of TMC?",
        "Explain the goal of TMC.",
        "Could you outline TMC's goal?",
        "What does TMC strive to achieve?",
        "Please repeat the TMC goal.",
        "Goal of TMC?",
        "TMC goal: what is it?",
        "What is the end target of TMC?",
        "What's the institutional goal of TMC?",
        "Tell me the goal.",
        "Goal statement of TMC?"
    ],
    "creator": [
        "Who created this AI?",
        "Who made you?",
        "Who is your creator?",
        "Who developed this assistant?",
        "Tell me who built this AI.",
        "Who programmed you?",
        "Who is responsible for your creation?",
        "Who designed this chatbot?",
        "What is the name of your creator?",
        "Who brought you into existence?",
        "Who's your maker?",
        "Who built this TMC assistant?",
        "Who wrote the code for this AI?",
        "Who is CajesJM?",
        "Who created the TMC AI?",
        "Who's behind this AI?",
        "By whom were you created?",
        "What person made this AI?",
        "Who is your developer?",
        "Who made this TMC bot?"
    ],
    "about": [
        "What is TMC?",
        "TMC stands for?",
        "What does TMC stand for?",
        "What does TMC mean?",
        "Tell me about TMC.",
        "What is TMC as a school?",
        "Where is TMC located?",
        "What kind of institution is TMC?",
        "TMC full name?",
        "What is the full name of TMC?"
    ],
    "identity": [
        "Who are you?",
        "What are you?",
        "Are you an AI?",
        "Are you a chatbot?",
        "What can you do?",
        "What do you do?",
        "Introduce yourself.",
        "Tell me about yourself.",
        "What is your purpose?",
        "What can you answer?"
    ]
}

cebuano_templates = {
    "vision": [
        "Unsa ang vision sa TMC?",
        "Sultihi ko sa vision sa TMC.",
        "Ihulagway ang vision sa TMC.",
        "Unsa ang gidamgo sa TMC?",
        "Mahimo ba nimong isaysay ang vision sa TMC?",
        "Unsay vision sa TMC?",
        "Gusto kong mahibalo sa vision sa TMC.",
        "Ipakigbahin ang vision sa TMC.",
        "Ihatag ang vision sa TMC.",
        "Unsa ang gipasabot sa vision sa TMC?",
        "Ipasabot ang vision sa TMC.",
        "Mahimo bang i-outline ang vision sa TMC?",
        "Unsa ang tinguha sa TMC sumala sa vision?",
        "Palihug sublion ang vision sa TMC.",
        "Vision sa TMC?",
        "TMC vision: unsa kini?",
        "Unsa ang gipangandoy sa TMC base sa vision?",
        "Unsa ang institusyonal nga vision sa TMC?",
        "Sultihi ko sa vision.",
        "Pahayag sa vision sa TMC?"
    ],
    "mission": [
        "Unsa ang mission sa TMC?",
        "Sultihi ko sa mission sa TMC.",
        "Ihulagway ang mission sa TMC.",
        "Unsa ang gibuhat sa TMC sumala sa mission?",
        "Mahimo ba nimong isaysay ang mission sa TMC?",
        "Unsay mission sa TMC?",
        "Gusto kong mahibalo sa mission sa TMC.",
        "Ipakigbahin ang mission sa TMC.",
        "Ihatag ang mission sa TMC.",
        "Unsa ang gipasabot sa mission sa TMC?",
        "Ipasabot ang mission sa TMC.",
        "Mahimo bang i-outline ang mission sa TMC?",
        "Unsa ang katuyoan sa TMC?",
        "Palihug sublion ang mission sa TMC.",
        "Mission sa TMC?",
        "TMC mission: unsa kini?",
        "Unsa ang gitinguha sa TMC nga buhaton?",
        "Unsa ang institusyonal nga mission sa TMC?",
        "Sultihi ko sa mission.",
        "Pahayag sa mission sa TMC?"
    ],
    "slogan": [
        "Unsa ang slogan sa TMC?",
        "Sultihi ko sa slogan sa TMC.",
        "Unsay slogan sa TMC?",
        "Nahibal-an ba nimo ang slogan sa TMC?",
        "Mahimo ba nimong isulti ang slogan sa TMC?",
        "Unsa ang giingon sa slogan sa TMC?",
        "Ihatag ang slogan sa TMC.",
        "Ipakigbahin ang slogan sa TMC.",
        "Unsa ang opisyal nga slogan sa TMC?",
        "Gusto kong makadungog sa slogan sa TMC.",
        "Slogan sa TMC?",
        "Palihug ihatag ang slogan sa TMC.",
        "Unsa ang catchphrase sa TMC?",
        "Unsang linya ang gigamit sa TMC isip slogan?",
        "Sultihi ko sa motto sa TMC.",
        "Unsa ang tagline sa TMC?",
        "Unsa ang gipang-anunsyo sa TMC isip slogan?",
        "Nahinumduman ba nimo ang slogan sa TMC?",
        "Giunsa pagpresentar sa TMC ang kaugalingon sa pipila ka pulong?",
        "Pahayag sa slogan sa TMC?"
    ],
    "philosophy": [
        "Unsa ang philosophy sa TMC?",
        "Sultihi ko sa philosophy sa TMC.",
        "Ihulagway ang philosophy sa TMC.",
        "Unsa ang giya nga prinsipyo sa TMC?",
        "Mahimo ba nimong isaysay ang philosophy sa TMC?",
        "Unsay philosophy sa TMC?",
        "Gusto kong mahibalo sa philosophy sa TMC.",
        "Ipakigbahin ang philosophy sa TMC.",
        "Ihatag ang philosophy sa TMC.",
        "Unsa ang gituohan sa TMC?",
        "Ipasabot ang philosophy sa TMC.",
        "Mahimo bang i-outline ang philosophy sa TMC?",
        "Unsa ang edukasyonal nga philosophy sa TMC?",
        "Palihug sublion ang philosophy sa TMC.",
        "Pilosopiya sa TMC?",
        "TMC pilosopiya: unsa kini?",
        "Unsa nga mga bili ang naggiya sa TMC sumala sa philosophy?",
        "Unsa ang pundasyon nga pagtuo sa TMC?",
        "Sultihi ko sa philosophy.",
        "Pahayag sa philosophy sa TMC?"
    ],
    "goal": [
        "Unsa ang goal sa TMC?",
        "Sultihi ko sa goal sa TMC.",
        "Ihulagway ang goal sa TMC.",
        "Unsa ang gitinguha sa TMC?",
        "Mahimo ba nimong isaysay ang goal sa TMC?",
        "Unsay goal sa TMC?",
        "Gusto kong mahibalo sa goal sa TMC.",
        "Ipakigbahin ang goal sa TMC.",
        "Ihatag ang goal sa TMC.",
        "Unsa ang katuyoan sa TMC?",
        "Ipasabot ang goal sa TMC.",
        "Mahimo bang i-outline ang goal sa TMC?",
        "Unsa ang gitinguha nga makab-ot sa TMC?",
        "Palihug sublion ang goal sa TMC.",
        "Goal sa TMC?",
        "TMC goal: unsa kini?",
        "Unsa ang katapusang target sa TMC?",
        "Unsa ang institusyonal nga goal sa TMC?",
        "Sultihi ko sa goal.",
        "Pahayag sa goal sa TMC?"
    ],
    "creator": [
        "Kinsa ang naghimo niining AI?",
        "Kinsa ang nagbuhat kanimo?",
        "Kinsa ang imong magbubuhat?",
        "Kinsa ang nag-develop niining assistant?",
        "Sultihi ko kung kinsa ang nagtukod niining AI.",
        "Kinsa ang nagprograma kanimo?",
        "Kinsa ang responsable sa imong pagkahimo?",
        "Kinsa ang nagdisenyo niining chatbot?",
        "Unsa ang ngalan sa imong magbubuhat?",
        "Kinsa ang naghatag kanimo og kinabuhi?",
        "Kinsa ang imong tighimo?",
        "Kinsa ang nagtukod niining TMC assistant?",
        "Kinsa ang nagsulat sa code para niining AI?",
        "Kinsa si CajesJM?",
        "Kinsa ang naghimo sa TMC AI?",
        "Kinsa ang naa sa luyo niining AI?",
        "Kang kinsa ka gibuhat?",
        "Unsang tawhana ang naghimo niining AI?",
        "Kinsa ang imong developer?",
        "Kinsa ang naghimo niining TMC bot?"
    ],
    "about": [
        "Unsa ang TMC?",
        "Unsa ang gipasabot sa TMC?",
        "Asa nahimutang ang TMC?",
        "Sultihi ko bahin sa TMC."
    ],
    "identity": [
        "Kinsa ka?",
        "Unsa ka?",
        "AI ka ba?",
        "Unsa ang imong mahimo?",
        "Ipaila ang imong kaugalingon."
]
}

tagalog_templates = {
    "vision": [
        "Ano ang vision ng TMC?",
        "Sabihin mo sa akin ang vision ng TMC.",
        "Ilarawan ang vision ng TMC.",
        "Ano ang inaasam ng TMC?",
        "Maaari mo bang sabihin ang vision ng TMC?",
        "Anong vision ng TMC?",
        "Gusto kong malaman ang vision ng TMC.",
        "Ibahagi ang vision ng TMC.",
        "Ibigay ang vision ng TMC.",
        "Ano ang ibig sabihin ng vision ng TMC?",
        "Ipaliwanag ang vision ng TMC.",
        "Maaari mo bang i-outline ang vision ng TMC?",
        "Ano ang nilalayon ng TMC ayon sa vision?",
        "Pakiulit ang vision ng TMC.",
        "Vision ng TMC?",
        "TMC vision: ano ito?",
        "Ano ang pangarap ng TMC base sa vision?",
        "Ano ang institusyonal na vision ng TMC?",
        "Sabihin mo ang vision.",
        "Pahayag ng vision ng TMC?"
    ],
    "mission": [
        "Ano ang mission ng TMC?",
        "Sabihin mo sa akin ang mission ng TMC.",
        "Ilarawan ang mission ng TMC.",
        "Ano ang ginagawa ng TMC ayon sa mission?",
        "Maaari mo bang sabihin ang mission ng TMC?",
        "Anong mission ng TMC?",
        "Gusto kong malaman ang mission ng TMC.",
        "Ibahagi ang mission ng TMC.",
        "Ibigay ang mission ng TMC.",
        "Ano ang ibig sabihin ng mission ng TMC?",
        "Ipaliwanag ang mission ng TMC.",
        "Maaari mo bang i-outline ang mission ng TMC?",
        "Ano ang layunin ng TMC?",
        "Pakiulit ang mission ng TMC.",
        "Mission ng TMC?",
        "TMC mission: ano ito?",
        "Ano ang pinagsisikapang gawin ng TMC?",
        "Ano ang institusyonal na mission ng TMC?",
        "Sabihin mo ang mission.",
        "Pahayag ng mission ng TMC?"
    ],
    "slogan": [
        "Ano ang slogan ng TMC?",
        "Sabihin mo ang slogan ng TMC.",
        "Anong slogan ng TMC?",
        "Alam mo ba ang slogan ng TMC?",
        "Maaari mo bang sabihin ang slogan ng TMC?",
        "Ano ang sinasabi ng slogan ng TMC?",
        "Ibigay ang slogan ng TMC.",
        "Ibahagi ang slogan ng TMC.",
        "Ano ang opisyal na slogan ng TMC?",
        "Gusto kong marinig ang slogan ng TMC.",
        "Slogan ng TMC?",
        "Pakiibigay ang slogan ng TMC.",
        "Ano ang catchphrase ng TMC?",
        "Anong linya ang ginagamit ng TMC bilang slogan?",
        "Sabihin mo ang motto ng TMC.",
        "Ano ang tagline ng TMC?",
        "Ano ang inaanunsyo ng TMC bilang slogan?",
        "Naaalala mo ba ang slogan ng TMC?",
        "Paano ipinapakilala ng TMC ang sarili sa ilang salita?",
        "Pahayag ng slogan ng TMC?"
    ],
    "philosophy": [
        "Ano ang philosophy ng TMC?",
        "Sabihin mo sa akin ang philosophy ng TMC.",
        "Ilarawan ang philosophy ng TMC.",
        "Ano ang gabay na prinsipyo ng TMC?",
        "Maaari mo bang sabihin ang philosophy ng TMC?",
        "Anong philosophy ng TMC?",
        "Gusto kong malaman ang philosophy ng TMC.",
        "Ibahagi ang philosophy ng TMC.",
        "Ibigay ang philosophy ng TMC.",
        "Ano ang pinaniniwalaan ng TMC?",
        "Ipaliwanag ang philosophy ng TMC.",
        "Maaari mo bang i-outline ang philosophy ng TMC?",
        "Ano ang edukasyonal na philosophy ng TMC?",
        "Pakiulit ang philosophy ng TMC.",
        "Philosophy ng TMC?",
        "TMC philosophy: ano ito?",
        "Anong mga halaga ang gumagabay sa TMC ayon sa philosophy?",
        "Ano ang pundasyon na paniniwala ng TMC?",
        "Sabihin mo ang philosophy.",
        "Pahayag ng philosophy ng TMC?"
    ],
    "goal": [
        "Ano ang goal ng TMC?",
        "Sabihin mo sa akin ang goal ng TMC.",
        "Ilarawan ang goal ng TMC.",
        "Ano ang pinupuntirya ng TMC?",
        "Maaari mo bang sabihin ang goal ng TMC?",
        "Anong goal ng TMC?",
        "Gusto kong malaman ang goal ng TMC.",
        "Ibahagi ang goal ng TMC.",
        "Ibigay ang goal ng TMC.",
        "Ano ang adhikain ng TMC?",
        "Ipaliwanag ang goal ng TMC.",
        "Maaari mo bang i-outline ang goal ng TMC?",
        "Ano ang pinagsisikapang makamit ng TMC?",
        "Pakiulit ang goal ng TMC.",
        "Goal ng TMC?",
        "TMC goal: ano ito?",
        "Ano ang huling target ng TMC?",
        "Ano ang institusyonal na goal ng TMC?",
        "Sabihin mo ang goal.",
        "Pahayag ng goal ng TMC?"
    ],
    "creator": [
        "Sino ang lumikha ng AI na ito?",
        "Sino ang gumawa sa iyo?",
        "Sino ang iyong creator?",
        "Sino ang nag-develop ng assistant na ito?",
        "Sabihin mo kung sino ang nagtayo ng AI na ito.",
        "Sino ang nag-program sa iyo?",
        "Sino ang responsable sa iyong pagkakalikha?",
        "Sino ang nagdisenyo ng chatbot na ito?",
        "Ano ang pangalan ng iyong lumikha?",
        "Sino ang nagbigay sa iyo ng buhay?",
        "Sino ang iyong gumawa?",
        "Sino ang nagtayo ng TMC assistant na ito?",
        "Sino ang sumulat ng code para sa AI na ito?",
        "Sino si CajesJM?",
        "Sino ang gumawa ng TMC AI?",
        "Sino ang nasa likod ng AI na ito?",
        "Kanino ka ginawa?",
        "Sinong tao ang gumawa ng AI na ito?",
        "Sino ang iyong developer?",
        "Sino ang gumawa ng TMC bot na ito?"
    ],
    "about": [
        "Ano ang TMC?",
        "Ano ang ibig sabihin ng TMC?",
        "Saan matatagpuan ang TMC?",
        "Sabihin mo sa akin ang tungkol sa TMC."
    ],
    "identity": [
        "Sino ka?",
        "Ano ka?",
        "AI ka ba?",
        "Ano ang kaya mong gawin?",
        "Ipakilala mo ang sarili mo."
    ]
}

keyword_variants = {
    "vision":     ["vision", "Vision", "VISION"],
    "mission":    ["mission", "Mission", "MISSION"],
    "slogan":     ["slogan", "Slogan", "motto", "tagline"],
    "philosophy": ["philosophy", "Philosophy", "pilosopiya"],
    "goal":       ["goal", "Goal", "goals", "GOALS"],
    "creator":    ["creator", "who made you", "developer", "CajesJM"],
    "about":    ["TMC", "about TMC"],
    "identity": ["who are you", "what are you"]
}

for topic, keywords in keyword_variants.items():
    for kw in keywords:
        english_templates[topic].append(kw)

# ---- GENERATE ALL PAIRS ----
all_pairs = []

for topic in ["vision", "mission", "slogan", "philosophy", "goal", "creator", "about", "identity"]:
    # English
    for q in english_templates[topic]:
        all_pairs.append((q, facts[topic]["en"]))
    # Cebuano
    for q in cebuano_templates[topic]:
        all_pairs.append((q, facts[topic]["ceb"]))
    # Tagalog
    for q in tagalog_templates[topic]:
        all_pairs.append((q, facts[topic]["tag"]))

    for kw in keyword_variants[topic]:
        for _ in range(5):
            all_pairs.append((kw, facts[topic]["en"]))

# Shuffle to mix topics
random.shuffle(all_pairs)

# Write to train.txt
with open('train.txt', 'w', encoding='utf-8') as f:
    for q, a in all_pairs:
        f.write(f"Q: {q}\nA: {a}\n\n")

print(f"Generated {len(all_pairs)} Q&A pairs in train.txt")