T = {}
T[25] = dict(q="What is a Service Blueprint?", tq="Service Blueprint అంటే ఏమిటి?",
 ex="""సేవ: గెలిచిన డబ్బును withdraw చేయడం.

పొర (Layer)\tఏమి జరుగుతుంది
Customer journey\tPlayer withdrawal అభ్యర్థించి డబ్బు కోసం ఎదురుచూస్తారు
Evidence\tWithdrawal screen, confirmation message, SMS, బ్యాంక్ credit
Frontstage\tApp status updates చూపిస్తుంది; support agent ప్రశ్నలకు సమాధానం ఇస్తారు
Backstage\tKYC తనిఖీ, fraud review, finance ఆమోదం
Support resources\tPayment gateway, banking partner, verification system
Player కు withdrawal ఎందుకు నెమ్మదిగా అనిపిస్తుందో, మెరుగైన status సమాచారం లేదా వేగవంతమైన processes ఎక్కడ సహాయపడతాయో ఇది చూపిస్తుంది.""",
 how="""1. Map చేయాల్సిన service journey ఎంచుకోండి.
2. Customer చర్యలను step by step map చేయండి.
3. ప్రతి step లో customer చూసే evidence జోడించండి.
4. Frontstage కార్యకలాపాలు (customer కు కనిపించేవి) జోడించండి.
5. Backstage కార్యకలాపాలు మరియు support systems జోడించండి.
6. విఫలమయ్యే చోట్లు, ఆలస్యాలు, handoffs గుర్తించండి.""",
 iv="Customer అనుభవాన్ని దాని వెనుక ఉన్న internal processes మరియు systems తో అనుసంధానించడానికి నేను service blueprints ఉపయోగిస్తాను; దీంతో కనిపించే screens మాత్రమే కాకుండా మూలకారణాలను సరిచేస్తాం.")
T[26] = dict(q="What is a Site Map?", tq="Site Map అంటే ఏమిటి?",
 ex="""Classic Rummy (ఉదాహరణ):
- Home / Lobby → Game types → Tables
- Wallet → Add money, Withdraw, Transaction history
- Account → Profile, KYC, Settings
- Rewards → Offers, Bonuses
- Support → Help centre, FAQs, Contact us""",
 how="""1. అన్ని content మరియు features ను జాబితా చేయండి.
2. సంబంధిత content ను గ్రూప్ చేయండి (card sorting సహాయపడుతుంది).
3. ప్రధాన sections నిర్ణయించండి.
4. Pages ను hierarchy లో అమర్చండి.
5. సులభంగా కనుగొనగలరో users తో validate చేయండి (ఉదా. tree testing).
6. Navigation మరియు screens ప్లాన్ చేయడానికి site map ఉపయోగించండి.""",
 iv="స్పష్టమైన content hierarchy మరియు navigation నిర్వచించడానికి నేను site maps తయారు చేస్తాను, screens design చేసే ముందు వాటిని users తో validate చేస్తాను.")
T[27] = dict(q="What is a Skill Map?", tq="Skill Map అంటే ఏమిటి?",
 ex="""ఒక Classic Rummy design team (ఉదాహరణ):

నైపుణ్యం\tDesigner A\tDesigner B\tDesigner C
User research\tబలమైనది\tప్రాథమికం\tప్రాథమికం
Visual design\tప్రాథమికం\tబలమైనది\tబలమైనది
Motion design\tప్రాథమికం\tప్రాథమికం\tబలమైనది
Prototyping\tబలమైనది\tబలమైనది\tప్రాథమికం
Data మరియు analytics\tప్రాథమికం\tప్రాథమికం\tప్రాథమికం
Analytics లో ఖాళీ ఉన్నందున, metrics ఆధారిత redesign ముందు training లేదా కొత్త నియామకం అవసరమని ఇది సూచిస్తుంది.""",
 how="""1. టీమ్‌కు అవసరమైన నైపుణ్యాలను జాబితా చేయండి.
2. ప్రతి ఒక్కరూ తమను తాము rate చేసుకునేలా చేయండి (manager తో చర్చించండి).
3. ఫలితాలను matrix లేదా chart లో చూపించండి.
4. బలాలు, ఖాళీలు, overlaps గుర్తించండి.
5. Training, mentoring, నియామకం లేదా staffing ప్లాన్ చేయండి.
6. ఎదుగుదలను గమనించడానికి క్రమం తప్పకుండా పునరావృతం చేయండి.""",
 iv="Design lead గా, టీమ్ బలాలు మరియు ఖాళీలను అర్థం చేసుకోవడానికి నేను skill maps ఉపయోగిస్తాను; ఇది mentoring, నియామకం మరియు projects కు ఎవరిని కేటాయించాలో నిర్ణయించడంలో సహాయపడుతుంది.")
T[28] = dict(q="What is a Storyboard?", tq="Storyboard అంటే ఏమిటి?",
 ex="""Storyboard: 'ఇంటికి వెళ్తూ Rummy నేర్చుకోవడం' (ఉదాహరణ)
1. స్నేహితుడు సిఫార్సు చేయడంతో రవి app install చేస్తారు.
2. Bus లో తెరుస్తారు కానీ rules గురించి సందేహంగా ఉంటారు.
3. ఒక interactive tutorial ఒక practice hand ద్వారా మార్గనిర్దేశం చేస్తుంది.
4. ఆడుతున్నప్పుడు సరైన card groups హైలైట్ అవుతాయి.
5. Practice game పూర్తి చేసి నమ్మకం పొందుతారు.
6. తక్కువ stake table లో చేరతారు.""",
 how="""1. User మరియు scenario ఎంచుకోండి.
2. కథను కొన్ని ముఖ్యమైన క్షణాలుగా రాయండి.
3. ప్రతి క్షణానికి ఒక panel గీయండి (సాధారణ బొమ్మలు చాలు).
4. సందర్భం, భావాలు, ప్రొడక్ట్ పాత్రను చూపించండి.
5. చిన్న captions జోడించండి.
6. Stakeholders తో ideas చర్చించడానికి, test చేయడానికి ఉపయోగించండి.""",
 iv="ఒక design concept ను సందర్భంతో కూడిన user కథగా చూపించడానికి నేను storyboards ఉపయోగిస్తాను; నిర్మించకముందే ఒక idea విలువను stakeholders అర్థం చేసుకోవడానికి ఇది సహాయపడుతుంది.")
T[29] = dict(q="What is a Style Guide?", tq="Style Guide అంటే ఏమిటి?",
 ex="""- Primary మరియు secondary రంగులు.
- Card typography.
- Button రూపం.
- Icon styles.
- Background patterns.
- Text hierarchy.""",
 how="""1. Brand identity నిర్వచించండి.
2. Visual principles ఏర్పాటు చేయండి.
3. Typography మరియు రంగులు నిర్వచించండి.
4. UI styling నియమాలను document చేయండి.
5. సరైన ఉపయోగానికి ఉదాహరణలు ఇవ్వండి.
6. Documentation ను నిర్వహించండి.""",
 iv="Visual ప్రమాణాలను document చేసి, design మరియు engineering teams అంతటా consistency ఉండేలా చూడటానికి నేను style guides తయారు చేస్తాను.",
 extra=("Style Guide vs Design System","""Interview లో తరచుగా అడిగే తేడా:

Style Guide\tDesign System
Visual guidelines మరియు ప్రమాణాలపై దృష్టి\tపూర్తి design మరియు implementation ecosystem ను కవర్ చేస్తుంది
రంగులు మరియు typography నిర్వచిస్తుంది\tTokens, components, patterns మరియు guidelines నిర్వచిస్తుంది
ప్రధానంగా styling ను document చేస్తుంది\tమళ్లీ ఉపయోగించగల, విస్తరించగల product development కు సహాయపడుతుంది"""))
T[30] = dict(q="What is a Usability Report?", tq="Usability Report అంటే ఏమిటి?",
 ex="""Onboarding అనుభవాన్ని 10 మంది participants తో test చేశారు.
ఉదాహరణ ఫలితాలు:

పరిశీలన\tతీవ్రత\tసిఫార్సు
OTP errors users కు అర్థం కావడం లేదు\tఎక్కువ\tError messages మెరుగుపరచడం
Help option users కు కనిపించడం లేదు\tమధ్యస్థం\tHelp కనిపించేలా చేయడం
కార్డులు అమర్చడంలో users ఇబ్బంది పడుతున్నారు\tఎక్కువ\tGuided instructions జోడించడం""",
 how="""1. Usability లక్ష్యాలను నిర్ణయించండి.
2. ప్రతినిధ్య participants ను ఎంపిక చేయండి.
3. Test scenarios తయారు చేయండి.
4. User ప్రవర్తనను గమనించండి.
5. సమస్యలు మరియు ఆధారాలను నమోదు చేయండి.
6. తీవ్రతను (severity) అంచనా వేయండి.
7. సిఫార్సులు ఇవ్వండి.
8. మెరుగుదలలను మళ్లీ test చేయండి.""",
 iv="గమనించిన user ప్రవర్తనను ఆధారాలతో కూడిన findings, severity అంచనాలు మరియు అమలు చేయగల design సిఫార్సులుగా మార్చి నేను usability reports తయారు చేస్తాను.")
T[31] = dict(q="What is a User-Story Map?", tq="User-Story Map అంటే ఏమిటి?",
 ex="""కార్యకలాపం: ఒక గేమ్ ఆడటం.

Activity\tSteps\tవివరాలు
Game access\tApp తెరవడం\tLogin, verification
Discover\tLobby లోకి వెళ్లడం\tTables చూడటం
Game లో చేరడం\tTable ఎంచుకోవడం\tRules మరియు entry వివరాలు చూడటం
Play\tActions చేయడం\tకార్డులు అమర్చడం, moves చేయడం
Complete\tగేమ్ పూర్తి చేయడం\tఫలితం మరియు history చూడటం""",
 how="""1. User లక్ష్యాలను నిర్వచించండి.
2. ప్రధాన కార్యకలాపాలను గుర్తించండి.
3. కార్యకలాపాలను steps గా విభజించండి.
4. వివరమైన user stories జోడించండి.
5. తప్పనిసరి functionality కు ప్రాధాన్యత ఇవ్వండి.
6. Release slices నిర్ణయించండి.
7. Stories ను development tasks గా మార్చండి.""",
 iv="Product functionality ని user లక్ష్యాలతో అనుసంధానించడానికి, అర్థవంతమైన release increments కు ప్రాధాన్యత ఇవ్వడంలో Agile teams కు సహాయపడటానికి నేను user-story mapping ఉపయోగిస్తాను.")
T[32] = dict(q="What is a UX Roadmap?", tq="UX Roadmap అంటే ఏమిటి?",
 ex="""ఇప్పుడు (Now)\tతదుపరి (Next)\tభవిష్యత్తు (Future)
Onboarding మెరుగుపరచడం\tAccessibility మెరుగుపరచడం\tవ్యక్తిగత learning
Usability సమస్యలు సరిచేయడం\tWallet redesign\tAdvanced player insights
Gameplay స్పష్టత పెంచడం\tDesign system విస్తరణ\tIntelligent assistance""",
 how="""1. Product experience లక్ష్యాలను గుర్తించండి.
2. User మరియు business సమస్యలను సేకరించండి.
3. Initiatives కు ప్రాధాన్యత ఇవ్వండి.
4. Now, Next మరియు Future ను నిర్ణయించండి.
5. Product మరియు engineering తో ఏకాభిప్రాయం సాధించండి.
6. ఆధారాల ఆధారంగా నిరంతరం అప్‌డేట్ చేయండి.""",
 iv="అనుభవ మెరుగుదలలను product strategy, user needs మరియు business priorities తో అనుసంధానించడానికి నేను UX roadmap ను నిర్వహిస్తాను.")
T[33] = dict(q="What is a Wireflow?", tq="Wireflow అంటే ఏమిటి?",
 ex="""Registration wireflow:
Welcome Screen → Mobile Number Screen → OTP Screen → Profile Screen → Lobby.
ఇది వీటిని కూడా చూపించగలదు:
- OTP తప్పయితే ఏమి జరుగుతుంది?
- User Resend ఎంచుకుంటే ఏమి జరుగుతుంది?
- Registration విఫలమైతే ఏమి జరుగుతుంది?""",
 how="""1. Workflow ను గుర్తించండి.
2. ప్రతి screen కు ప్రాథమిక wireframes తయారు చేయండి.
3. బాణాలతో screens ను కలపండి.
4. నిర్ణయ బిందువులను (decision points) జోడించండి.
5. విజయం మరియు error మార్గాలను నిర్ణయించండి.
6. Developers మరియు product managers తో review చేయండి.""",
 iv="Interface నిర్మాణం మరియు navigation logic రెండింటినీ – ముఖ్యంగా అనేక states ఉన్న సంక్లిష్ట workflows కు – తెలియజేయడానికి నేను wireflows ఉపయోగిస్తాను.")
T[34] = dict(q="What is a Wireframe?", tq="Wireframe అంటే ఏమిటి?",
 ex="""ఒక gameplay wireframe లో ఇవి ఉండవచ్చు:
- Top navigation.
- Player సమాచారం.
- Game table.
- Card area.
- Action buttons.
- Timer.
- Bottom navigation.
ఈ దశలో అలంకరణ రంగులు లేదా visual effects పై దృష్టి పెట్టరు.""",
 how="""1. Requirements అర్థం చేసుకోండి.
2. Information hierarchy నిర్వచించండి.
3. Screen layout ఏర్పాటు చేయండి.
4. ముఖ్యమైన components ను ఉంచండి.
5. Content ప్రాధాన్యతను నిర్ణయించండి.
6. Interactions మరియు usability ను పరిశీలించండి.
7. High-fidelity design కు ముందు validate చేయండి.""",
 iv="Visual design పై పెట్టుబడి పెట్టే ముందు layout, information hierarchy మరియు interaction ప్రాధాన్యతలను ఏర్పాటు చేయడానికి నేను wireframes తో మొదలుపెడతాను.")
T[35] = dict(q="What is a User Flow?", tq="User Flow అంటే ఏమిటి?",
 ex="""లక్ష్యం: ఒక game table లో చేరడం.
START → Classic Rummy తెరవడం → Login / Register → Lobby లోకి ప్రవేశం → Game Type ఎంచుకోవడం → Table ఎంచుకోవడం → Eligibility మరియు table requirements తనిఖీ → Table లో చేరడం → END – గేమ్ మొదలైంది""",
 how="""1. ఒక user లక్ష్యాన్ని నిర్ణయించండి.
2. ప్రారంభ బిందువును గుర్తించండి.
3. అవసరమైన screens ను map చేయండి.
4. నిర్ణయ బిందువులను గుర్తించండి.
5. ప్రత్యామ్నాయ మరియు error మార్గాలను చేర్చండి.
6. విజయవంతమైన ముగింపు స్థితిని నిర్ణయించండి.
7. Stakeholders మరియు users తో flow ను validate చేయండి.""",
 iv="ముఖ్యమైన product tasks పూర్తి చేయడానికి users తీసుకునే steps, నిర్ణయాలు మరియు ప్రత్యామ్నాయ మార్గాలను చూపించడానికి నేను user flows తయారు చేస్తాను.")

OVT = {
"ux-intro-1": dict(q="How should you use the NN/g UX Deliverables Glossary to prepare for UX interviews?", tq="UX interviews కు సిద్ధం కావడానికి NN/g UX Deliverables Glossary ను ఎలా ఉపయోగించాలి?",
 te="""Senior UX Designer, Lead Product Designer, Principal Designer మరియు UX Manager interviews కు సిద్ధం కావడానికి ఇది అద్భుతమైన వనరు.
దీన్ని కేవలం UX పదాల glossary గా కాకుండా, పూర్తి UX project అమలు framework గా చదవాలని నా సూచన.
Classic Rummy, digital products, product design మరియు creative direction లో మీ అనుభవంతో, ఈ కార్యకలాపాల్లో చాలావాటిపై మీకు ఇప్పటికే ఆచరణాత్మక పరిచయం ఉంది. ఇప్పుడు ముఖ్యంగా అర్థం చేసుకోవాల్సినవి:

1. ప్రతి UX deliverable అర్థం ఏమిటి.
2. దాన్ని ఎందుకు తయారు చేస్తాం.
3. ప్రాజెక్ట్‌లో దాన్ని ఎప్పుడు ఉపయోగించాలి.
4. దాన్ని ఎలా తయారు చేయాలి.
5. అది ఏ business మరియు user సమస్యలను పరిష్కరిస్తుంది.
6. Interview లో దాన్ని నమ్మకంగా ఎలా వివరించాలి.
7. వేర్వేరు deliverables ఒకదానితో ఒకటి ఎలా అనుసంధానమవుతాయి.

ఈ గైడ్ అంతటా రెండు ఆచరణాత్మక ఉదాహరణలు ఉపయోగిస్తాం:
- ఉదాహరణ A – Classic Rummy: Onboarding, registration, gameplay, wallet, payments మరియు retention ఉన్న నిజమైన gaming ప్రొడక్ట్.
- ఉదాహరణ B – ResolveAI: Dashboards, ticket management, AI assistance మరియు analytics ఉన్న AI ఆధారిత customer support SaaS platform.
Classic Rummy ఉదాహరణ మీ గత అనుభవాన్ని వివరించడానికి, ResolveAI ఆధునిక SaaS మరియు AI ఆధారిత ప్రొడక్ట్స్ design చేయగల మీ సామర్థ్యాన్ని చూపించడానికి సహాయపడతాయి."""),
"ux-intro-2": dict(q="What is the complete end-to-end UX design process?", tq="పూర్తి end-to-end UX design ప్రక్రియ ఏమిటి?",
 te="""ఒక్కో deliverable చదివే ముందు, మొత్తం UX lifecycle ను అర్థం చేసుకోండి.

1. దశ 1 – Discovery & Research: Business, users, market మరియు ఇప్పుడున్న సమస్యలను అర్థం చేసుకోవడం. Research · Interviews · CSD Matrix · Ecosystem Map · Empathy Map
2. దశ 2 – Define & Synthesize: Research ఫలితాలను స్పష్టమైన సమస్యలు మరియు అవకాశాలుగా మార్చడం. Affinity Diagram · Personas · Journey Map · Experience Map · Problem Statements
3. దశ 3 – Ideation & Strategy: సాధ్యమైన పరిష్కారాలను అన్వేషించి, ముందుగా ఏమి నిర్మించాలో నిర్ణయించడం. Mind Map · Scenario Map · Storyboard · Kano · MoSCoW · RICE
4. దశ 4 – Information Architecture & Interaction Design: Content, navigation మరియు user interactions ను క్రమబద్ధం చేయడం. Sitemap · User Flow · HTA · User Story Map · Wireflow
5. దశ 5 – Wireframing & Prototyping: నిర్మాణం మరియు interactions ను తయారు చేసి validate చేయడం. Wireframes · Prototypes · Usability Testing
6. దశ 6 – Visual Design & Design System: Visual భాష మరియు మళ్లీ ఉపయోగించగల UI components ను అభివృద్ధి చేయడం. Mood Board · Style Guide · Mockups · Design System
7. దశ 7 – Development Handoff & Collaboration: Engineering, product, QA మరియు ఇతర stakeholders తో కలిసి పనిచేయడం. Specifications · RACI · Asset Map · Relationship Map
8. దశ 8 – Testing, Measurement & Improvement: అమలైన ప్రొడక్ట్‌ను validate చేసి నిరంతరం మెరుగుపరచడం. Usability Report · Analytics · UX Roadmap · Iteration""",
 imp="ఇది నేర్చుకోవడానికి ఒక framework మాత్రమే, కఠినమైన waterfall ప్రక్రియ కాదు. నిజమైన Agile product teams లో ఈ దశలు ఒకదానితో ఒకటి కలిసి, పునరావృతమవుతాయి. ఒకే sprint లో research, prototype, test మరియు redesign చేయవచ్చు."),
"ux-intro-3": dict(q="What is a UX deliverable?", tq="UX Deliverable అంటే ఏమిటి?",
 extra_te="""ఈ తేడాను గుర్తుంచుకోండి:
- UX process = మనం చేసే కార్యకలాపాలు.
- UX deliverable = మనం తయారు చేసే ఫలితం.
- UX method = ఒక కార్యకలాపాన్ని ఎలా చేస్తాం.
- UX artifact = తయారైన రూపం లేదా పని ఫలితం.

గమనిక: NN/g document లోని ప్రతి deliverable ప్రతి ప్రాజెక్ట్‌కు అవసరం లేదు. మంచి designer ప్రాజెక్ట్ సంక్లిష్టత, risk, అందుబాటులో ఉన్న సమయం మరియు stakeholder అవసరాల ఆధారంగా deliverables ను ఎంచుకుంటారు.

మీ PDF లో pages 2–9 లో 35 UX deliverables ఉన్నాయి. అసలు పదజాలాన్ని పాటిస్తూ, ఆచరణాత్మక వివరణలు, తెలుగు అర్థాలు, ఉదాహరణలు మరియు interview ప్రాముఖ్యతను జోడించాను."""),
}

PART_TE = {
 2: "ఈ deliverables యూజర్లను, వారి పరిసరాలను, ఇప్పటికే ఉన్న జ్ఞానాన్ని మరియు research ఫలితాలను అర్థం చేసుకోవడానికి సహాయపడతాయి.",
 3: "ఈ deliverables యూజర్ చుట్టూ ఉన్న ప్రపంచం, వారు ఎలా ఆలోచిస్తారు, భావిస్తారు, ఒక లక్ష్యాన్ని పనులుగా ఎలా విభజిస్తారు అనేది చూపిస్తాయి – దానితో పాటు ఒక prioritisation పద్ధతి కూడా.",
 4: "ఈ deliverables నిర్దిష్ట journeys ను map చేయడానికి, ideas ను క్రమబద్ధం చేయడానికి, ఏది ముఖ్యమో నిర్ణయించడానికి సహాయపడతాయి.",
 5: "ఈ deliverables అవగాహనను visual దిశగా, user models గా మరియు test చేయగల designs గా మారుస్తాయి.",
 6: "ఈ deliverables టీమ్‌లు కలిసి పనిచేయడానికి, సంఖ్యలతో ప్రాధాన్యత ఇవ్వడానికి, screens వెనుక ఉన్న పూర్తి సేవను design చేయడానికి సహాయపడతాయి.",
 7: "ఈ deliverables content ను క్రమబద్ధం చేస్తాయి, టీమ్ నైపుణ్యాలను map చేస్తాయి, user కథలను చిత్రాలతో చెబుతాయి, styles ను document చేస్తాయి మరియు test ఫలితాలను report చేస్తాయి.",
 8: "ఈ deliverables UX పనిని Agile delivery తో అనుసంధానిస్తాయి, screens, flows మరియు navigation ను వివరంగా నిర్దేశిస్తాయి.",
}
