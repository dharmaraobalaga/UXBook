"""Phase 0 – project setup for the UX-Step by step book."""
S = []

S.append(dict(
 id='st-0-1', label='Step 0.1',
 en="How to use this step-by-step UX journey",
 te="ఈ దశలవారీ UX journey ను ఎలా ఉపయోగించాలి?",
 figure='ux-intro-2',
 body_te="""ఈ ట్యాబ్ ఏమిటి? (What is this tab?):
ఇది ప్రశ్న–జవాబుల పుస్తకం కాదు. ఒక పూర్తి UX ప్రాజెక్ట్‌ను మొదటి రోజు నుంచి launch తర్వాత మెరుగుదల వరకు దశలవారీగా (step by step) నడిపించే ప్రయాణం. మనం రెండు ప్రాజెక్ట్‌లను – Classic Rummy (Gaming Product) మరియు ResolveAI (AI-powered Customer Support SaaS) – మొదటి నుంచి చివరి వరకు ఒకే కథగా అనుసరిస్తాం.

8 దశలు (8 Phases):
Phase\tఈ దశ సమాధానం చెప్పే ప్రశ్న\tప్రధాన output
1. Discovery & Research\tమనకు నిజంగా ఏం తెలుసు?\tResearch evidence
2. Define & Synthesize\tఅసలు సమస్య ఏమిటి?\tInsights, problem statements
3. Ideation & Strategy\tఏ పరిష్కారాలు సాధ్యం?\tPrioritised concepts
4. IA & Interaction Design\tUser task ఎలా పూర్తవుతుంది?\tSitemap, flows
5. Wireframing & Prototyping\tఇది user కు అర్థమవుతుందా?\tTested prototype
6. Visual Design & Design System\tఇది ఎలా కనిపించాలి, consistent గా ఉండాలి?\tUI, design system
7. Development Handoff\tఇది సరిగ్గా ఎలా build అవుతుంది?\tSpecs, collaboration
8. Testing & Measurement\tఇది నిజంగా పనిచేస్తుందా?\tMetrics, roadmap

ప్రతి Step పేజీలో ఏముంటాయి?:
- ఎందుకు? (WHY) – ఈ పని చేయకపోతే ఏమవుతుంది, దీని విలువ ఏమిటి.
- ఏమిటి? (WHAT) – activity లేదా deliverable యొక్క నిర్వచనం.
- ఎప్పుడు? (WHEN) – ప్రాజెక్ట్‌లో ఏ సమయంలో, ఏ పరిస్థితిలో చేయాలి.
- ఎలా? (HOW) – అడుగుల వారీగా చేసే విధానం.
- Deliverable – ప్రయోజనం (purpose), నిర్మాణం (structure), తయారీ విధానం (creation process).
- తదుపరి step కు కనెక్షన్ – ఈ output తర్వాతి పనికి ఎలా input అవుతుంది.
- Senior / Principal Designer నిర్ణయం – అనుభవజ్ఞులు ఎలా ఆలోచించి నిర్ణయిస్తారు.
- Agile ఉదాహరణ – నిజమైన sprint లో ఇది ఎలా జరుగుతుంది.
ఎడమ పేజీలోని ఉదాహరణ పెట్టెలో Classic Rummy మరియు ResolveAI ఉదాహరణలు ఉంటాయి. ప్రతి Phase చివర Knowledge Check ఉంటుంది.

నాలుగు పదాల తేడా (Process, Method, Deliverable, Artifact):
పదం\tతెలుగు అర్థం\tEnglish meaning
UX Process\tపని జరిగే మొత్తం క్రమం / దశలు\tThe overall sequence of UX activities
UX Method\tపని చేయడానికి ఉపయోగించే పద్ధతి\tA technique used to carry out an activity
UX Deliverable\tఇతరులకు తెలియజేయడానికి తయారు చేసే output\tA tangible output that communicates findings or decisions
UX Artifact\tపని లేదా ఆలోచనను చూపించే రూపం\tA representation or work product created during design

ముఖ్యమైన గమనిక (Important):
ఈ 8 phases ఒక learning framework మాత్రమే; కచ్చితంగా వరుసగా పూర్తయ్యే waterfall process కాదు. Agile teams లో research, design, testing, development ఒకదానితో ఒకటి overlap అవుతాయి. కొత్త సమాచారం వచ్చినప్పుడు ముందరి దశకు తిరిగి వెళ్లడం సహజం. ప్రతి deliverable లోతు project risk, complexity, timeline మరియు team అవసరాలకు తగ్గట్టుగా ఉండాలి.

ఎలా చదవాలి? (How to study):
1. ముందుగా తెలుగు వివరణ చదివి concept అర్థం చేసుకోండి.
2. "View English" నొక్కి English terminology మరియు వివరణ చదవండి.
3. ఉదాహరణను మీ సొంత project (Classic Rummy) తో పోల్చండి.
4. Interview line ను English లో గట్టిగా (aloud) చెప్పి practice చేయండి.
5. Phase చివర Knowledge Check పూర్తి చేసి, తర్వాతే తదుపరి Phase కు వెళ్లండి.""",
 body_en="""What is this tab?:
This is not a question-and-answer book. It is a step-by-step journey that walks one complete UX project from day one to post-launch improvement. We follow two projects – Classic Rummy (a gaming product) and ResolveAI (an AI-powered customer support SaaS) – as one continuous story.

The 8 phases:
Phase\tQuestion this phase answers\tMain output
1. Discovery & Research\tWhat do we actually know?\tResearch evidence
2. Define & Synthesize\tWhat is the real problem?\tInsights, problem statements
3. Ideation & Strategy\tWhich solutions are possible?\tPrioritised concepts
4. IA & Interaction Design\tHow will the user complete the task?\tSitemap, flows
5. Wireframing & Prototyping\tDoes the user understand it?\tTested prototype
6. Visual Design & Design System\tHow should it look and stay consistent?\tUI, design system
7. Development Handoff\tHow will it be built correctly?\tSpecs, collaboration
8. Testing & Measurement\tDoes it really work?\tMetrics, roadmap

What every step page contains:
- WHY – what goes wrong without it, and the value it creates.
- WHAT – the definition of the activity or deliverable.
- WHEN – at what point and in which situations to do it.
- HOW – the step-by-step method.
- Deliverable – its purpose, structure and creation process.
- Connection to the next step – how this output becomes the input to the next activity.
- Senior / Principal Designer decision – how experienced designers think and decide.
- Agile example – how it happens inside a real sprint.
The example box on the left page holds the Classic Rummy and ResolveAI examples. Each phase ends with a knowledge check.

Process, method, deliverable and artifact:
Term\tTelugu meaning\tEnglish meaning
UX Process\tపని జరిగే మొత్తం క్రమం\tThe overall sequence of UX activities
UX Method\tపని చేసే పద్ధతి\tA technique used to carry out an activity
UX Deliverable\tఇతరులకు తెలియజేసే output\tA tangible output that communicates findings or decisions
UX Artifact\tఆలోచనను చూపించే రూపం\tA representation or work product created during design

Important:
The 8 phases are a learning framework, not a strict waterfall. In Agile teams research, design, testing and development overlap, and teams revisit earlier decisions as new evidence emerges. The depth of each deliverable should match project risk, complexity, timeline and team needs.

How to study:
1. Read the Telugu explanation first and understand the concept.
2. Open "View English" for the English terminology and explanation.
3. Compare the example with your own project (Classic Rummy).
4. Practise the interview line aloud in English.
5. Complete the knowledge check at the end of each phase before moving on.""",
 ex_te="""ఒకే ప్రాజెక్ట్ కథ:
మనం ప్రతి దశలో అదే రెండు ప్రాజెక్ట్‌లను ముందుకు తీసుకెళ్తాం. Phase 1 లో సేకరించిన evidence → Phase 2 లో problem statement అవుతుంది → Phase 3 లో solution ideas అవుతాయి … Phase 8 లో కొలిచి మళ్లీ Phase 1 కు తిరిగి వస్తాం.

పై చిత్రం 8 దశల loop ను చూపిస్తుంది.""",
 ex_en="""One project story:
We carry the same two projects through every phase. Evidence collected in Phase 1 becomes the problem statement in Phase 2, solution ideas in Phase 3 … and in Phase 8 we measure the result and loop back to Phase 1.""",
 markers=[('tip', 'గుర్తుంచుకోండి', 'మంచి UX Designer ప్రతి deliverable ను తయారు చేయడు; సరైన సమస్యను పరిష్కరించడానికి అవసరమైన deliverable ను సరైన సమయంలో తయారు చేస్తాడు.')],
))

S.append(dict(
 id='st-0-2', label='Step 0.2',
 en="Meet the two projects: Classic Rummy and ResolveAI",
 te="రెండు ప్రాజెక్ట్‌ల పరిచయం: Classic Rummy మరియు ResolveAI",
 body_te="""ఈ రెండు ప్రాజెక్ట్‌లే మొత్తం 8 దశల్లో మన ఉదాహరణలు. సంఖ్యలు అన్నీ నేర్చుకోవడానికి ఇచ్చిన ఉదాహరణ సంఖ్యలు (illustrative), నిజమైన company data కాదు.

ప్రాజెక్ట్ A – Classic Rummy (Gaming Product):
- Product: Mobile లో ఆడే real-money skill card game (Points, Pool, Deals Rummy).
- పరిస్థితి (Situation): Installs ఎక్కువగా ఉన్నాయి, కానీ కొత్త users registration లేదా first game ముందే వెళ్లిపోతున్నారు.
- Business goal: First-game activation మరియు early retention (D1/D7) పెంచడం – responsible gaming మరియు compliance నియమాలను పాటిస్తూ.
- Users: కొత్త players, returning players, regular / high-value players, support team.
- Team: Product Manager, UX/UI Designer, Android/iOS/Server developers, QA, Data Analyst, Customer Support, Compliance/Legal.
- Constraints: 18+ వయస్సు మరియు KYC, కొన్ని రాష్ట్రాల్లో నిషేధం, payment gateway నియమాలు, తక్కువ ధర phones, బలహీనమైన network, అనేక భాషలు.

ప్రాజెక్ట్ B – ResolveAI (AI-powered Customer Support SaaS):
- Product: Companies యొక్క support teams కోసం web platform. Tickets (email, chat) ఒకే చోట వస్తాయి; AI ticket summary, cited knowledge answers, suggested replies ఇస్తుంది.
- పరిస్థితి: Pilot customers ఉన్నారు, కానీ agents AI suggestions ను తక్కువగా ఉపయోగిస్తున్నారు; Average Handling Time (AHT) ఎక్కువగా ఉంది.
- Business goal: AHT తగ్గించడం, First-Contact Resolution (FCR) పెంచడం, AI adoption పెంచడం – quality మరియు trust తగ్గకుండా.
- Users: Support agents, team leads, support managers / admins, end-customers.
- Team: PM, Product Designer, Frontend/Backend engineers, ML/AI engineers, QA, Customer Success, Security.
- Constraints: Data privacy, AI hallucination risk, role permissions, audit trail, CRM / email / chat integrations.

ఎందుకు రెండు ప్రాజెక్ట్‌లు?:
Classic Rummy – consumer, mobile, emotion, trust, money, regulation. ResolveAI – B2B, desktop, productivity, data-dense screens, AI trust. Interview లో మీ గత అనుభవం (Gaming) మరియు ఆధునిక SaaS/AI సామర్థ్యం రెండూ చూపించవచ్చు.

ప్రాజెక్ట్ Brief (Project brief) లో ఏమి ఉండాలి?:
- Problem / opportunity – ఏ సమస్యను పరిష్కరిస్తున్నాం.
- Business goal మరియు success metric.
- Target users.
- Scope – ఏది లోపల, ఏది బయట.
- Constraints మరియు risks.
- Team మరియు timeline.
ఈ brief Phase 1 Step 1.2 (Kickoff & Stakeholder Interviews) కు ప్రారంభ బిందువు.""",
 body_en="""These two projects are our examples across all 8 phases. All numbers are illustrative learning figures, not real company data.

Project A – Classic Rummy (Gaming Product):
- Product: a mobile real-money skill card game (Points, Pool and Deals Rummy).
- Situation: installs are high, but many new users leave before registration or before their first game.
- Business goal: increase first-game activation and early retention (D1/D7) while following responsible-gaming and compliance rules.
- Users: new players, returning players, regular / high-value players, the support team.
- Team: Product Manager, UX/UI Designer, Android/iOS/server developers, QA, Data Analyst, Customer Support, Compliance/Legal.
- Constraints: 18+ age and KYC, restrictions in some states, payment-gateway rules, low-cost phones, weak networks, multiple languages.

Project B – ResolveAI (AI-powered Customer Support SaaS):
- Product: a web platform for company support teams. Tickets (email, chat) arrive in one place; AI provides ticket summaries, cited knowledge answers and suggested replies.
- Situation: there are pilot customers, but agents rarely use AI suggestions and Average Handling Time (AHT) is high.
- Business goal: reduce AHT, increase First-Contact Resolution (FCR) and AI adoption – without lowering quality or trust.
- Users: support agents, team leads, support managers / admins, end-customers.
- Team: PM, Product Designer, frontend/backend engineers, ML/AI engineers, QA, Customer Success, Security.
- Constraints: data privacy, AI hallucination risk, role permissions, audit trail, CRM / email / chat integrations.

Why two projects?:
Classic Rummy covers consumer, mobile, emotion, trust, money and regulation. ResolveAI covers B2B, desktop, productivity, data-dense screens and AI trust. In interviews you can show both your past experience (gaming) and your ability with modern SaaS and AI.

What goes into a project brief?:
- Problem / opportunity – what we are solving.
- Business goal and success metric.
- Target users.
- Scope – what is in and what is out.
- Constraints and risks.
- Team and timeline.
This brief is the starting point for Phase 1, Step 1.2 (Kickoff & Stakeholder Interviews).""",
 ex_te="""ఒక్క లైన్‌లో రెండు ప్రాజెక్ట్‌లు:
- Classic Rummy: "కొత్త ఆటగాళ్లు మొదటి game ను నమ్మకంగా ఆడేలా చేయాలి."
- ResolveAI: "Agents AI సహాయంతో వేగంగా, సరైన సమాధానం పంపేలా చేయాలి."

Illustrative funnel (Classic Rummy): 100 installs → 62 registrations → 38 KYC/verification → 21 first games.
Illustrative baseline (ResolveAI): AHT 9 నిమిషాలు, AI suggestion వినియోగం 18%.""",
 ex_en="""The two projects in one line:
- Classic Rummy: "Help new players start their first game with confidence."
- ResolveAI: "Help agents send the right answer faster with AI assistance."

Illustrative funnel (Classic Rummy): 100 installs → 62 registrations → 38 verified → 21 first games.
Illustrative baseline (ResolveAI): AHT 9 minutes, AI suggestion usage 18%.""",
 markers=[('mistake', 'జాగ్రత్త', 'Interview లో illustrative సంఖ్యలను నిజమైన company data గా చెప్పకండి. "For example" లేదా "approximately" అని స్పష్టంగా చెప్పండి, confidential data పంచుకోకండి.')],
))
