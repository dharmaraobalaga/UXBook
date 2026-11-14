"""Phase 1 – Discovery & Research, steps 1.6–1.10"""
S = []

S.append(dict(
 id='st-1-6', label='Step 1.6',
 en="User interviews and contextual inquiry",
 te="User Interviews మరియు Contextual Inquiry",
 body_te="""ఎందుకు? (WHY):
Analytics "ఎక్కడ" సమస్య ఉందో చెబుతుంది; users తో మాట్లాడితే "ఎందుకు" తెలుస్తుంది – వారి లక్ష్యాలు, భయాలు, అలవాట్లు, workarounds, context. Contextual inquiry లో users వాస్తవంగా పని చేసే చోట గమనిస్తాం, ఎందుకంటే users చెప్పేది మరియు చేసేది తరచూ వేరుగా ఉంటాయి.

ఏమిటి? (WHAT):
- User interview: ఒక user తో 30–60 నిమిషాల one-on-one సంభాషణ – గత అనుభవాలు, behaviour, motivations గురించి.
- Contextual inquiry: User వారి నిజమైన environment లో (ఇంటి వద్ద, office desk వద్ద) పని చేస్తుండగా గమనించి, మధ్యలో ప్రశ్నలు అడగడం – "master–apprentice" model.

ఎప్పుడు? (WHEN):
Research plan మరియు analytics review తర్వాత. కొత్త domain, సంక్లిష్ట workflows (ఉదా: ResolveAI agents) ఉన్నప్పుడు contextual inquiry తప్పనిసరి.

ఎలా? (HOW):
1. Recruiting: Screener తో సరైన participants ఎంచుకోండి (segment, usage, device, language). Incentive నిర్ణయించండి.
2. Discussion guide రాయండి: Intro & consent → Warm-up → గత అనుభవం ("చివరిసారి … చెప్పండి") → Tasks/observation → Deep-dive → Wrap-up.
3. Consent తీసుకోండి – recording, data ఉపయోగం, ఎప్పుడైనా ఆపవచ్చని స్పష్టంగా చెప్పండి. Real-money gaming లో వయస్సు 18+ నిర్ధారించండి.
4. ఒకరు interview చేస్తారు, మరొకరు notes తీసుకుంటారు.
5. Open, non-leading ప్రశ్నలు అడగండి; మౌనాన్ని అనుమతించండి; "ఇంకా చెప్పండి", "ఎందుకు?" అని లోతుగా వెళ్లండి.
6. ప్రతి session తర్వాత 15 నిమిషాల debrief – top observations, quotes, surprises.
7. 5–6 interviews తర్వాత కొత్త విషయాలు రావడం తగ్గితే (saturation) ఆపవచ్చు.

మంచి vs చెడు ప్రశ్నలు:
చెడు (leading)\tమంచి (open)
Tutorial ఉపయోగపడుతుందా?\tమీరు మొదటిసారి ఆడినప్పుడు ఏమి జరిగిందో చెప్పండి.
Deposit process కష్టంగా ఉందా?\tచివరిసారి డబ్బు add చేసినప్పుడు step by step ఏమి చేశారు?
AI suggestion మంచిదే కదా?\tAI suggestion వచ్చినప్పుడు మీరు ఏమి చేస్తారు? చూపించండి.

Deliverable: User interview notes / recordings:
- ప్రయోజనం: Users యొక్క నిజమైన behaviour, needs, pain points మరియు quotes ను evidence గా భద్రపరచడం.
- నిర్మాణం: Participant profile (పేరు లేకుండా code: P1, P2) · Context · Observations · Quotes · Pain points · Workarounds · Goals · Surprises.
- తయారీ: Guide → sessions → debrief → notes ను ఒకే template లో → recordings సురక్షితంగా, consent నియమాల ప్రకారం.

తదుపరి step కు కనెక్షన్:
Observations → CSD Matrix లో Suppositions ను confirm/reject చేస్తాయి (Step 1.7). Quotes మరియు behaviours → Empathy Map (Step 1.9). Notes అన్నీ → Phase 2 Affinity Diagram కు sticky notes అవుతాయి.

Senior / Principal Designer నిర్ణయం:
- Users చెప్పే solutions ("ఒక button పెట్టండి") కాదు, వెనుక ఉన్న need వింటారు.
- చెప్పేది vs చేసేది తేడా గమనిస్తారు.
- Stakeholders (PM, developers) ను sessions చూడమని ఆహ్వానిస్తారు – empathy మరియు buy-in రెండూ పెరుగుతాయి.
- Participant వివరాలను anonymise చేసి, privacy కాపాడతారు.

Agile ఉదాహరణ:
Sprint 1 రెండవ వారంలో 3 రోజుల్లో 8 remote interviews (Google Meet), PM మరియు ఒక developer observer గా. ప్రతి సాయంత్రం 20 నిమిషాల debrief; sprint చివర "Top 5 observations" share.""",
 body_en="""WHY:
Analytics tells you where the problem is; talking to users tells you why – their goals, fears, habits, workarounds and context. Contextual inquiry observes users where they actually work, because what users say and what they do are often different.

WHAT:
- User interview: a 30–60 minute one-on-one conversation about past experiences, behaviour and motivations.
- Contextual inquiry: observing users in their real environment (at home, at their office desk) while they work, asking questions along the way – the "master–apprentice" model.

WHEN:
After the research plan and analytics review. Contextual inquiry is essential for a new domain or complex workflows (e.g. ResolveAI agents).

HOW:
1. Recruiting: choose the right participants with a screener (segment, usage, device, language). Decide the incentive.
2. Write a discussion guide: intro & consent → warm-up → past experience ("Tell me about the last time…") → tasks/observation → deep-dive → wrap-up.
3. Get consent – explain recording, data use and that they can stop at any time. For real-money gaming, confirm the participant is 18+.
4. One person interviews, another takes notes.
5. Ask open, non-leading questions; allow silence; probe with "tell me more" and "why?"
6. Hold a 15-minute debrief after each session – top observations, quotes, surprises.
7. Stop when new interviews stop revealing new things (saturation), often after 5–6 per segment.

Bad vs good questions:
Bad (leading)\tGood (open)
Would a tutorial help?\tTell me what happened the first time you played.
Is the deposit process difficult?\tWalk me through, step by step, the last time you added money.
The AI suggestion is good, right?\tWhat do you do when an AI suggestion appears? Show me.

Deliverable: user interview notes / recordings:
- Purpose: preserve users' real behaviour, needs, pain points and quotes as evidence.
- Structure: participant profile (coded P1, P2, no names) · context · observations · quotes · pain points · workarounds · goals · surprises.
- Creation: guide → sessions → debrief → notes in one template → recordings stored securely under the consent rules.

Connection to the next step:
Observations confirm or reject suppositions in the CSD Matrix (Step 1.7). Quotes and behaviours feed the empathy map (Step 1.9). All notes become the sticky notes for the affinity diagram in Phase 2.

Senior / Principal Designer decision:
- They listen for the need behind user-proposed solutions ("add a button").
- They notice the gap between what users say and what they do.
- They invite stakeholders (PM, developers) to observe – it builds empathy and buy-in.
- They anonymise participant details and protect privacy.

Agile example:
In week two of Sprint 1: 8 remote interviews over 3 days (Google Meet), with the PM and a developer observing. A 20-minute debrief each evening; "Top 5 observations" shared at sprint end.""",
 ex_te="""Classic Rummy – గమనించినవి (illustrative):
- P3 (కొత్త player, Telugu): "Real money game లో తప్పు చేస్తే డబ్బు పోతుందని భయం. ముందు free గా ఆడి చూడాలనుకున్నా."
- P5: KYC photo upload రెండుసార్లు fail అయింది; ఎందుకో message లో లేదు → app వదిలేశారు.
- P1: Rules screen చదవకుండా YouTube లో video చూశారు (workaround).

ResolveAI – contextual inquiry (illustrative):
- Agent desk పై 2 monitors: ResolveAI, CRM, knowledge base, Slack.
- AI suggestion వచ్చినా agent knowledge base లో మళ్లీ వెతికి verify చేస్తున్నారు: "ఇది ఎక్కడ నుంచి వచ్చిందో తెలియదు, customer కు తప్పు చెబితే నా పేరు పోతుంది."
- Team lead: refund policy తరచూ మారుతుంది; AI పాత policy చెబుతుందేమో భయం.""",
 ex_en="""Classic Rummy – observations (illustrative):
- P3 (new player, Telugu): "I was afraid of losing money if I made a mistake in a real-money game. I wanted to try it free first."
- P5: the KYC photo upload failed twice with no reason given → left the app.
- P1: skipped the rules screen and watched a YouTube video instead (workaround).

ResolveAI – contextual inquiry (illustrative):
- The agent's two monitors show ResolveAI, the CRM, the knowledge base and Slack.
- Even with an AI suggestion, the agent searches the knowledge base again to verify: "I don't know where this came from; if I tell the customer something wrong, it's on me."
- Team lead: the refund policy changes often; they fear the AI quotes an old policy.""",
 markers=[('tip', 'Interview line', 'I combined interviews with contextual inquiry, because what users say and what they do are often different. I invited the PM and engineers to observe so the team built shared empathy.'),
          ('mistake', 'సాధారణ తప్పు', 'Leading questions అడగడం, users కు product ను "sell" చేయడం, లేదా ఒక్క user మాటను అందరికీ వర్తింపజేయడం.')],
))

S.append(dict(
 id='st-1-7', label='Step 1.7',
 en="CSD Matrix: certainties, suppositions and doubts",
 te="CSD Matrix: నిశ్చితాలు, ఊహలు మరియు సందేహాలు",
 figure='ux-4',
 body_te="""ఎందుకు? (WHY):
ప్రతి team లో "మనకు తెలుసు" అనుకునే విషయాలు చాలా ఉంటాయి, వాటిలో చాలావరకు ఊహలే. CSD Matrix facts ను assumptions నుంచి వేరు చేసి, ఏది test చేయాలో స్పష్టంగా చూపిస్తుంది. దీంతో opinion ఆధారిత వాదనలు తగ్గి, evidence ఆధారిత చర్చ మొదలవుతుంది.

ఏమిటి? (WHAT):
మూడు columns ఉన్న ఒక సాధారణ matrix:
- C – Certainties (నిశ్చితాలు): Evidence తో నిరూపితమైనవి.
- S – Suppositions (ఊహలు): మనం నమ్ముతున్నవి కానీ ఇంకా నిరూపించనివి.
- D – Doubts (సందేహాలు): మనకు తెలియనివి, తెలుసుకోవాల్సిన ప్రశ్నలు.

ఎప్పుడు? (WHEN):
Discovery ప్రారంభంలో (stakeholder interviews తర్వాత) ఒకసారి, research జరుగుతున్న కొద్దీ update చేస్తూ. Workshop format లో team తో కలిసి చేయడం ఉత్తమం.

ఎలా? (HOW):
1. Team (PM, design, engineering, support, data) ను 60–90 నిమిషాల workshop కు పిలవండి.
2. ప్రతి ఒక్కరూ sticky notes పై project గురించి తెలిసినవి / నమ్మేవి రాయాలి.
3. ప్రతి note ను అడగండి: "దీనికి evidence ఏమిటి?" Evidence ఉంటే C, లేకపోతే S, ప్రశ్న అయితే D.
4. ప్రతి Certainty కు source రాయండి (analytics, interview, policy).
5. Suppositions ను risk (తప్పయితే ఎంత నష్టం) ఆధారంగా ranking చేయండి.
6. High-risk suppositions మరియు doubts ను research questions లేదా experiments గా మార్చండి.
7. Research తర్వాత: S → C (నిరూపితమైతే) లేదా తొలగించండి (తప్పయితే).

Deliverable: CSD Matrix:
- ప్రయోజనం: Assumptions ను కనిపించేలా చేసి, research మరియు experiments కు ప్రాధాన్యత ఇవ్వడం.
- నిర్మాణం: మూడు columns (C / S / D) · ప్రతి item కు source లేదా owner · Risk level · తదుపరి action (research / experiment / ignore).
- తయారీ: Workshop → sticky notes → classify → evidence check → risk rank → actions → research తర్వాత update.

తదుపరి step కు కనెక్షన్:
Doubts మరియు high-risk suppositions → interview deep-dives మరియు Phase 3 లో experiment hypotheses. Certainties → Phase 2 Problem Statement లో evidence. Updated matrix → Research Findings (Step 1.10).

Senior / Principal Designer నిర్ణయం:
- Senior stakeholder చెప్పినంత మాత్రాన ఏదీ Certainty కాదు – evidence అడుగుతారు, గౌరవంగా.
- అన్ని suppositions ను test చేయరు; "తప్పయితే ఎక్కువ నష్టం + తక్కువ evidence" ఉన్నవాటినే ముందు test చేస్తారు.
- Matrix ను living document గా ఉంచి, ప్రతి sprint review లో update చేస్తారు.

Agile ఉదాహరణ:
Sprint 1 మొదటి వారంలో Miro board పై remote workshop. High-risk suppositions ను Jira లో "Hypothesis" tickets గా వేస్తారు: "We believe … We will know when …".""",
 body_en="""WHY:
Every team has many things it "knows" that are really assumptions. A CSD Matrix separates facts from assumptions and makes clear what needs testing. It shifts discussions from opinion to evidence.

WHAT:
A simple three-column matrix:
- C – Certainties: proven by evidence.
- S – Suppositions: what we believe but haven't proven.
- D – Doubts: what we don't know – questions to answer.

WHEN:
Once at the start of discovery (after stakeholder interviews), then updated as research progresses. It works best as a team workshop.

HOW:
1. Invite the team (PM, design, engineering, support, data) to a 60–90 minute workshop.
2. Everyone writes what they know or believe about the project on sticky notes.
3. Ask of each note: "What is the evidence?" Evidence → C; no evidence → S; a question → D.
4. Write a source for each certainty (analytics, interview, policy).
5. Rank suppositions by risk (how much damage if they're wrong).
6. Turn high-risk suppositions and doubts into research questions or experiments.
7. After research: move S → C if proven, or remove it if disproven.

Deliverable: CSD Matrix:
- Purpose: make assumptions visible and prioritise research and experiments.
- Structure: three columns (C / S / D) · source or owner for each item · risk level · next action (research / experiment / ignore).
- Creation: workshop → sticky notes → classify → evidence check → risk ranking → actions → update after research.

Connection to the next step:
Doubts and high-risk suppositions → interview deep-dives and experiment hypotheses in Phase 3. Certainties → evidence for the Phase 2 problem statement. The updated matrix → research findings (Step 1.10).

Senior / Principal Designer decision:
- Nothing becomes a certainty just because a senior stakeholder said it – they ask for evidence, respectfully.
- They don't test every supposition; they test first those with high cost-if-wrong and low evidence.
- They keep the matrix as a living document and update it at every sprint review.

Agile example:
A remote workshop on a Miro board in week one of Sprint 1. High-risk suppositions become Jira "hypothesis" tickets: "We believe … We will know when …".""",
 ex_te="""Classic Rummy CSD (illustrative):
C – Certainties: 62% మాత్రమే registration పూర్తి చేస్తున్నారు (analytics). KYC 18+ తప్పనిసరి (compliance). 31% tickets deposit pending (support).
S – Suppositions: పెద్ద bonus చూపిస్తే activation పెరుగుతుంది. కొత్త players కు rules తెలుసు. Telugu users కు English screens సమస్య కాదు.
D – Doubts: Verification దగ్గర ఎందుకు ఆగుతున్నారు? Practice game వల్ల real-money conversion తగ్గుతుందా?

ResolveAI CSD (illustrative):
C: AI suggestions 18% మాత్రమే వాడుతున్నారు. Refund tickets AHT అత్యధికం.
S: Agents కు AI పై నమ్మకం లేకపోవడానికి కారణం accuracy. Summary ఇస్తే AHT తగ్గుతుంది.
D: Agents ఏ evidence చూస్తే AI ను నమ్ముతారు? Team leads quality ను ఎలా review చేస్తారు?""",
 ex_en="""Classic Rummy CSD (illustrative):
C – Certainties: only 62% complete registration (analytics). KYC 18+ is mandatory (compliance). 31% of tickets are "deposit pending" (support).
S – Suppositions: showing a bigger bonus will increase activation. New players already know the rules. English screens are not a problem for Telugu users.
D – Doubts: why do people stop at verification? Will a practice game reduce real-money conversion?

ResolveAI CSD (illustrative):
C: AI suggestions are used on only 18% of tickets. Refund tickets have the highest AHT.
S: agents distrust AI because of accuracy. A summary will reduce AHT.
D: what evidence makes agents trust the AI? How do team leads review quality?""",
 markers=[('tip', 'Interview line', 'I ran a CSD workshop to separate certainties from suppositions, then focused research on the highest-risk assumptions.')],
))

S.append(dict(
 id='st-1-8', label='Step 1.8',
 en="Ecosystem map",
 te="Ecosystem Map (పర్యావరణ వ్యవస్థ పటం)",
 figure='ux-6',
 body_te="""ఎందుకు? (WHY):
User అనుభవం మన screens లోనే జరగదు. Payment gateway, SMS OTP, bank, support agent, CRM, knowledge base, friends – ఇవన్నీ అనుభవాన్ని ప్రభావితం చేస్తాయి. ఏ ఒక్క భాగం fail అయినా user కు అది "మన product తప్పు" గానే అనిపిస్తుంది. Ecosystem map వల్ల dependencies, handoffs మరియు risk points కనిపిస్తాయి.

ఏమిటి? (WHAT):
User ను మధ్యలో పెట్టి, చుట్టూ ఉన్న people (actors), products, services, systems, channels మరియు వాటి మధ్య సంబంధాలు (data, money, information flow) చూపించే diagram.

ఎప్పుడు? (WHEN):
Discovery లో, ముఖ్యంగా అనేక systems, partners లేదా roles ఉన్న products లో (payments, B2B SaaS, marketplaces). Service Blueprint (Phase 4/7) కు ముందు.

ఎలా? (HOW):
1. మధ్యలో primary user ను పెట్టండి.
2. Interviews, stakeholder notes నుంచి అన్ని actors జాబితా చేయండి (internal + external).
3. Products, systems, channels జోడించండి.
4. Rings గా అమర్చండి – దగ్గర = నేరుగా, తరచుగా ప్రభావం; దూరం = పరోక్షం.
5. సంబంధాలను బాణాలతో కలపండి – ఏమి ప్రవహిస్తుంది (డబ్బు, data, సమాచారం).
6. Pain points మరియు failure points ను ఎరుపు రంగులో గుర్తించండి.
7. Team తో review చేసి missing actors జోడించండి.

Deliverable: Ecosystem Map:
- ప్రయోజనం: User చుట్టూ ఉన్న మొత్తం system ను, dependencies మరియు risk points ను చూపించడం.
- నిర్మాణం: Center (user) · Rings (people / products / services & channels) · Connections (labelled arrows) · Pain/failure markers · Legend.
- తయారీ: Actors list → rings → connections → pain points → validate.

తదుపరి step కు కనెక్షన్:
Failure points → Research findings లో opportunity areas. Actors → Phase 2 లో Personas (ఎవరికి design చేస్తున్నాం). Systems మరియు handoffs → Phase 4/7 లో Service Blueprint మరియు error states.

Senior / Principal Designer నిర్ణయం:
- మన control లో లేని parts (bank delay) ను కూడా design చేయగల అనుభవంగా చూస్తారు – ఉదా: clear status, expected time.
- B2B లో buyer (manager) మరియు user (agent) వేరని గుర్తిస్తారు.
- Map ను engineering మరియు partnerships teams తో share చేసి, ownership స్పష్టం చేస్తారు.

Agile ఉదాహరణ:
Discovery sprint లో ఒక 45 నిమిషాల session లో Miro లో draft; తర్వాత architecture diagram తో పోల్చి engineering lead తో validate.""",
 body_en="""WHY:
The user experience doesn't happen only on our screens. The payment gateway, SMS OTP, bank, support agent, CRM, knowledge base and friends all shape it. If any part fails, the user feels it as "our product's fault". An ecosystem map makes dependencies, handoffs and risk points visible.

WHAT:
A diagram with the user at the centre, showing the surrounding people (actors), products, services, systems and channels, and the relationships between them (flows of data, money and information).

WHEN:
During discovery, especially for products with many systems, partners or roles (payments, B2B SaaS, marketplaces). Before a service blueprint (Phases 4/7).

HOW:
1. Place the primary user at the centre.
2. List all actors from interviews and stakeholder notes (internal + external).
3. Add products, systems and channels.
4. Arrange them in rings – close = direct, frequent influence; far = indirect.
5. Connect relationships with arrows – what flows (money, data, information).
6. Mark pain points and failure points in red.
7. Review with the team and add missing actors.

Deliverable: ecosystem map:
- Purpose: show the whole system around the user, with dependencies and risk points.
- Structure: centre (user) · rings (people / products / services & channels) · connections (labelled arrows) · pain/failure markers · legend.
- Creation: list actors → rings → connections → pain points → validate.

Connection to the next step:
Failure points → opportunity areas in the research findings. Actors → personas in Phase 2 (who we design for). Systems and handoffs → service blueprint and error states in Phases 4/7.

Senior / Principal Designer decision:
- They treat parts outside our control (bank delays) as experiences we can still design – e.g. clear status and expected time.
- In B2B they recognise that the buyer (manager) and the user (agent) are different.
- They share the map with engineering and partnerships to clarify ownership.

Agile example:
A 45-minute session in the discovery sprint produces a Miro draft, then the engineering lead validates it against the architecture diagram.""",
 ex_te="""Classic Rummy ecosystem:
Player ↔ Friends (referral), Other players (tables), Support agent · Rummy app, Play Store, Phone · UPI/Bank, Payment gateway, OTP SMS, KYC service, Push/Email, Social media.
Failure points: OTP delay, KYC service reject, bank "pending" – player కు అన్నీ "app సమస్య" లా అనిపిస్తాయి.

ResolveAI ecosystem:
Agent ↔ Customer, Team lead, Admin · ResolveAI, CRM, Knowledge base, Email/Chat channels · AI model, Policy owners, Security/Audit.
Failure points: Knowledge base పాతది → AI పాత policy చెబుతుంది; CRM data sync ఆలస్యం.""",
 ex_en="""Classic Rummy ecosystem:
Player ↔ friends (referral), other players (tables), support agent · Rummy app, Play Store, phone · UPI/bank, payment gateway, OTP SMS, KYC service, push/email, social media.
Failure points: OTP delay, KYC rejection, bank "pending" – to the player, all feel like "app problems".

ResolveAI ecosystem:
Agent ↔ customer, team lead, admin · ResolveAI, CRM, knowledge base, email/chat channels · AI model, policy owners, security/audit.
Failure points: an outdated knowledge base → AI quotes an old policy; slow CRM data sync.""",
 markers=[],
))

S.append(dict(
 id='st-1-9', label='Step 1.9',
 en="Empathy map",
 te="Empathy Map (సానుభూతి పటం)",
 figure='ux-7',
 body_te="""ఎందుకు? (WHY):
Research notes చాలా ఉంటాయి; team అంతా user ను ఒకేలా అర్థం చేసుకోవడానికి ఒక సరళమైన, ఒక పేజీ రూపం కావాలి. Empathy map user యొక్క బయటి ప్రవర్తన (says, does) మరియు లోపలి స్థితి (thinks, feels) రెండింటినీ చూపిస్తుంది – దీంతో features కాకుండా మనుషుల గురించి ఆలోచిస్తాం.

ఏమిటి? (WHAT):
ఒక user segment గురించి నాలుగు భాగాల map:
- Says (చెబుతారు): Interviews లోని నిజమైన quotes.
- Thinks (ఆలోచిస్తారు): మనసులో ఉన్నవి, బయటకు చెప్పకపోవచ్చు.
- Does (చేస్తారు): గమనించిన actions, workarounds.
- Feels (అనుభూతి): భావోద్వేగాలు – భయం, ఆందోళన, ఉత్సాహం.
తరచుగా Pains (ఇబ్బందులు) మరియు Gains (కావాల్సినవి) అనే రెండు భాగాలు కూడా కలుపుతారు.

ఎప్పుడు? (WHEN):
User interviews తర్వాత, synthesis మొదలయ్యే ముందు. Persona కు ముందు ఒక తేలికపాటి అడుగు. Research లేకుండా తయారు చేస్తే అది "assumption map" మాత్రమే – అలా అని స్పష్టంగా label చేయాలి.

ఎలా? (HOW):
1. ఒక user segment ఎంచుకోండి (ఉదా: "కొత్త real-money player").
2. ఆ segment interview notes అన్నీ ముందు పెట్టుకోండి.
3. Says: నిజమైన quotes మాత్రమే, participant code తో.
4. Does: గమనించిన behaviour.
5. Thinks మరియు Feels: Observations ఆధారంగా జాగ్రత్తగా inference – evidence లేని దాన్ని రాయకండి.
6. Pains మరియు Gains సారాంశం.
7. Team తో review: "ఇది నిజమైన user లా అనిపిస్తోందా? Evidence ఉందా?"

Deliverable: Empathy Map:
- ప్రయోజనం: User ను మనిషిగా అర్థం చేసుకోవడానికి team కు ఒకే దృష్టి ఇవ్వడం.
- నిర్మాణం: మధ్యలో user segment · Says / Thinks / Does / Feels quadrants · Pains / Gains · Evidence sources.
- తయారీ: Segment → notes → quadrants → pains/gains → validate. ఒక్కో segment కు ఒక్కో map.

తదుపరి step కు కనెక్షన్:
Empathy map → Phase 2 లో Persona (goals, needs, behaviours) మరియు Journey Map లోని thoughts & emotions layer. Pains → Problem statements. Gains → HMW questions.

Senior / Principal Designer నిర్ణయం:
- Says మరియు Does మధ్య తేడాలను ప్రత్యేకంగా హైలైట్ చేస్తారు – అక్కడే లోతైన insights ఉంటాయి.
- అందరు users ఒకేలా ఉంటారని భావించరు; segments వారీగా వేర్వేరు maps.
- Emotion (ముఖ్యంగా డబ్బు, నమ్మకం సంబంధిత భయం) ను design requirement గా చూస్తారు.

Agile ఉదాహరణ:
Interviews ముగిసిన రోజు 1 గంట team session లో Miro template నింపుతారు; developers కూడా పాల్గొంటారు. Map ను sprint wiki లో pin చేస్తారు.""",
 body_en="""WHY:
Research produces lots of notes; the team needs a simple one-page view so everyone understands the user the same way. An empathy map shows both external behaviour (says, does) and internal state (thinks, feels), so we think about people, not just features.

WHAT:
A four-part map about one user segment:
- Says: real quotes from interviews.
- Thinks: what is on their mind, possibly unspoken.
- Does: observed actions and workarounds.
- Feels: emotions – fear, anxiety, excitement.
Two more sections are often added: pains and gains.

WHEN:
After user interviews, before synthesis starts. A lightweight step before personas. If made without research it is only an "assumption map" and should be labelled as such.

HOW:
1. Choose one user segment (e.g. "new real-money player").
2. Lay out all the interview notes for that segment.
3. Says: real quotes only, with participant codes.
4. Does: observed behaviour.
5. Thinks and Feels: careful inference based on observations – don't write anything without evidence.
6. Summarise pains and gains.
7. Review with the team: "Does this feel like a real user? Is there evidence?"

Deliverable: empathy map:
- Purpose: give the team one shared view of the user as a person.
- Structure: user segment at the centre · Says / Thinks / Does / Feels quadrants · pains / gains · evidence sources.
- Creation: segment → notes → quadrants → pains/gains → validate. One map per segment.

Connection to the next step:
The empathy map → persona (goals, needs, behaviours) and the thoughts-and-emotions layer of the journey map in Phase 2. Pains → problem statements. Gains → HMW questions.

Senior / Principal Designer decision:
- They highlight gaps between Says and Does – that is where deep insights live.
- They don't assume all users are the same; separate maps per segment.
- They treat emotion (especially fear around money and trust) as a design requirement.

Agile example:
On the day interviews finish, a one-hour team session fills a Miro template, developers included. The map is pinned to the sprint wiki.""",
 ex_te="""Classic Rummy – కొత్త real-money player:
- Says: "నేను సరిగ్గా ఆడుతున్నానో లేదో తెలియదు."
- Thinks: "Rules తెలియక డబ్బు పోగొట్టుకుంటానా?"
- Does: ఇతరుల game చూస్తారు, cash tables avoid చేస్తారు, YouTube లో rules వెతుకుతారు.
- Feels: ఆసక్తి కానీ భయం; తప్పులపై ఆందోళన.
Pains: Rules అర్థం కాకపోవడం, KYC fail. Gains: Risk లేకుండా practice, నమ్మకం.

ResolveAI – support agent:
- Says: "AI సమాధానం ఎక్కడ నుంచి వచ్చిందో తెలియాలి."
- Thinks: "తప్పు చెబితే నా quality score పడిపోతుంది."
- Does: AI reply ను copy చేసి knowledge base లో మళ్లీ verify చేస్తారు.
- Feels: Time pressure, AI పై అనుమానం.""",
 ex_en="""Classic Rummy – new real-money player:
- Says: "I don't know if I'm playing correctly."
- Thinks: "Will I lose money because I don't know the rules?"
- Does: watches others play, avoids cash tables, searches YouTube for rules.
- Feels: curious but nervous; worried about mistakes.
Pains: unclear rules, KYC failure. Gains: risk-free practice, confidence.

ResolveAI – support agent:
- Says: "I need to know where the AI answer came from."
- Thinks: "If I say something wrong, my quality score drops."
- Does: copies the AI reply and verifies it again in the knowledge base.
- Feels: time pressure and doubt about the AI.""",
 markers=[('mistake', 'సాధారణ తప్పు', 'Research లేకుండా office లో కూర్చుని empathy map తయారు చేసి దాన్ని "user truth" గా చూపించడం.')],
))

S.append(dict(
 id='st-1-10', label='Step 1.10',
 en="Research findings and opportunity areas",
 te="Research Findings మరియు Opportunity Areas",
 body_te="""ఎందుకు? (WHY):
Research ఎంత బాగా చేసినా, findings ను స్పష్టంగా share చేయకపోతే నిర్ణయాలు మారవు. Findings document team ను ఒకే అవగాహనపై తెచ్చి, Phase 2 (Define) కు నమ్మదగిన పునాది వేస్తుంది. ఇది Phase 1 యొక్క తుది output.

ఏమిటి? (WHAT):
- Finding: Evidence ఆధారంగా గమనించిన విషయం ("8 లో 6 మంది కొత్త players KYC upload fail తర్వాత app వదిలేశారు").
- Insight: Finding వెనుక ఉన్న "ఎందుకు" ("Players కు ఏమి తప్పు జరిగిందో, ఏమి చేయాలో తెలియనప్పుడు నమ్మకం కోల్పోతారు").
- Opportunity area: Design ద్వారా మెరుగుపరచగల ప్రాంతం ("Verification లో స్పష్టమైన guidance మరియు recovery").
Finding ≠ Solution. ఇక్కడ ఇంకా solutions నిర్ణయించం.

ఎప్పుడు? (WHEN):
Research activities పూర్తయ్యాక, Phase 2 synthesis కు ముందు లేదా దానితో కలిపి. Agile లో ప్రతి discovery cycle చివర.

ఎలా? (HOW):
1. అన్ని sources ఒకచోట చేర్చండి: stakeholder notes, analytics summary, competitive analysis, interview notes, CSD, ecosystem, empathy maps.
2. Triangulate: ఒకే విషయం 2+ sources లో కనిపిస్తే అది బలమైన finding.
3. ప్రతి finding కు evidence రాయండి (ఎంత మంది, ఏ data, quote).
4. Severity (user పై ప్రభావం) మరియు frequency (ఎంత మందికి) ఇవ్వండి.
5. Findings నుంచి 3–5 key insights రాయండి.
6. Opportunity areas ను business goal తో కలపండి.
7. Short readout (20–30 నిమిషాలు) లో stakeholders కు present చేసి, Phase 2 priorities పై అంగీకారం తీసుకోండి.

Deliverable: Research findings / opportunity areas:
- ప్రయోజనం: Evidence ను నిర్ణయాలకు ఉపయోగపడే రూపంలో share చేయడం.
- నిర్మాణం: Executive summary (5 lines) · Research questions → answers · Key findings (evidence, severity, frequency) · Insights · Opportunity areas · Updated CSD · Open questions · Next steps.
- తయారీ: Gather → triangulate → evidence → rate → insights → opportunities → readout.

తదుపరి step కు కనెక్షన్:
ఇదే Phase 2 కు handoff. Findings మరియు notes → Affinity Diagram. Segments → Personas. Stage-wise pain points → Journey Map. Insights → Problem Statements మరియు HMW questions.

Senior / Principal Designer నిర్ణయం:
- Readout ను "మనం ఏమి చేశాం" కాదు, "మనం ఏమి నేర్చుకున్నాం, దాని అర్థం ఏమిటి, ఏ నిర్ణయం తీసుకోవాలి" గా చెబుతారు.
- Business language లో చెబుతారు: ప్రతి opportunity ను ఒక metric తో కలుపుతారు.
- Uncomfortable findings (ఉదా: "bonus offers నమ్మకం తగ్గిస్తున్నాయి") ను కూడా evidence తో గౌరవంగా చెబుతారు.
- Confidence level చెబుతారు – ఏది బలంగా నిరూపితం, ఏది ఇంకా test చేయాలి.

Agile ఉదాహరణ:
Discovery sprint చివర sprint review లో 25 నిమిషాల readout. PM తో కలిసి opportunities ను product backlog లో epics గా మారుస్తారు; Phase 2 synthesis workshop తదుపరి sprint మొదట్లో.""",
 body_en="""WHY:
However well research is done, decisions won't change unless the findings are shared clearly. A findings document brings the team to one shared understanding and lays a reliable foundation for Phase 2 (Define). It is the final output of Phase 1.

WHAT:
- Finding: an evidence-based observation ("6 of 8 new players left the app after a failed KYC upload").
- Insight: the "why" behind it ("players lose trust when they don't know what went wrong or what to do next").
- Opportunity area: an area design can improve ("clear guidance and recovery during verification").
A finding is not a solution. We don't decide solutions yet.

WHEN:
After the research activities and before (or together with) Phase 2 synthesis. In Agile, at the end of every discovery cycle.

HOW:
1. Bring all sources together: stakeholder notes, analytics summary, competitive analysis, interview notes, CSD, ecosystem and empathy maps.
2. Triangulate: something seen in two or more sources is a strong finding.
3. Write the evidence for each finding (how many people, which data, which quote).
4. Rate severity (impact on users) and frequency (how many users).
5. Write 3–5 key insights from the findings.
6. Link the opportunity areas to the business goal.
7. Present a short readout (20–30 minutes) to stakeholders and agree Phase 2 priorities.

Deliverable: research findings / opportunity areas:
- Purpose: share evidence in a form that supports decisions.
- Structure: executive summary (5 lines) · research questions → answers · key findings (evidence, severity, frequency) · insights · opportunity areas · updated CSD · open questions · next steps.
- Creation: gather → triangulate → evidence → rate → insights → opportunities → readout.

Connection to the next step:
This is the handoff to Phase 2. Findings and notes → affinity diagram. Segments → personas. Stage-wise pain points → journey map. Insights → problem statements and HMW questions.

Senior / Principal Designer decision:
- The readout is not "what we did" but "what we learned, what it means and which decision to take".
- They speak business language: every opportunity is linked to a metric.
- They share uncomfortable findings (e.g. "bonus offers reduce trust") respectfully, with evidence.
- They state confidence levels – what is strongly proven and what still needs testing.

Agile example:
A 25-minute readout in the discovery sprint review. With the PM, opportunities become epics in the product backlog; the Phase 2 synthesis workshop happens at the start of the next sprint.""",
 ex_te="""Classic Rummy – key insights (illustrative):
1. కొత్త players కు real money లో తప్పు చేస్తామనే భయం first game ను ఆపుతోంది (6/8 interviews + 22% rules tickets).
2. KYC fail అయినప్పుడు కారణం, తదుపరి step తెలియక వదిలేస్తున్నారు (5/8 + 18% tickets).
3. Deposit "pending" status నమ్మకాన్ని దెబ్బతీస్తుంది (31% tickets).
Opportunity areas: Risk-free learning · Verification guidance & recovery · Transparent payment status. Metric: first-game activation 21% → 30%.

ResolveAI – key insights (illustrative):
1. Source తెలియని AI answer ను agents నమ్మరు; verify చేయడానికి అదనపు సమయం (7/8 agents).
2. Refund policy మార్పులు knowledge base లో ఆలస్యంగా వస్తాయి.
Opportunity areas: Cited, verifiable AI answers · Knowledge freshness · Faster refund workflow. Metric: AHT 9 → 6 నిమిషాలు, AI adoption 18% → 50%.""",
 ex_en="""Classic Rummy – key insights (illustrative):
1. New players' fear of making mistakes with real money stops their first game (6/8 interviews + 22% rules tickets).
2. When KYC fails, players leave because they don't know the reason or the next step (5/8 + 18% of tickets).
3. A "pending" deposit status damages trust (31% of tickets).
Opportunity areas: risk-free learning · verification guidance & recovery · transparent payment status. Metric: first-game activation 21% → 30%.

ResolveAI – key insights (illustrative):
1. Agents don't trust AI answers without a source; verification adds time (7/8 agents).
2. Refund policy changes reach the knowledge base late.
Opportunity areas: cited, verifiable AI answers · knowledge freshness · faster refund workflow. Metric: AHT 9 → 6 minutes, AI adoption 18% → 50%.""",
 markers=[('tip', 'Interview line', 'I triangulated analytics, support tickets and interviews into a few evidence-backed insights, linked each opportunity to a business metric, and aligned stakeholders before moving into definition.')],
))
