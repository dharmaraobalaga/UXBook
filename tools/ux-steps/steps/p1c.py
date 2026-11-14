"""Phase 1 – steps 1.11–1.14"""
S = []

S.append(dict(
 id='st-1-11', label='Step 1.11',
 en="How a Senior or Principal Designer makes discovery decisions",
 te="Senior / Principal Designer Discovery నిర్ణయాలు ఎలా తీసుకుంటారు?",
 body_te="""ఎందుకు ఇది ముఖ్యం? (WHY):
Junior designer "ఏ method చేయాలి?" అని అడుగుతారు. Senior designer "ఏ నిర్ణయం తీసుకోవాలి, దానికి ఎంత evidence సరిపోతుంది?" అని అడుగుతారు. Interviews లో Senior, Lead, Principal roles కు ఈ judgment నే పరీక్షిస్తారు.

1. Right-sizing (సరైన పరిమాణం):
ప్రతి project కు పూర్తి research అవసరం లేదు. రెండు ప్రశ్నలతో నిర్ణయిస్తారు:
- తప్పు నిర్ణయం తీసుకుంటే నష్టం ఎంత? (Risk)
- ఇప్పటికే మనకు ఎంత evidence ఉంది? (Confidence)
Risk\tEvidence\tనిర్ణయం
ఎక్కువ\tతక్కువ\tలోతైన research (interviews + data + contextual inquiry)
ఎక్కువ\tఎక్కువ\tLean validation (5 interviews లేదా quick test)
తక్కువ\tతక్కువ\tచిన్న experiment గా ship చేసి కొలవడం
తక్కువ\tఎక్కువ\tనేరుగా design చేయడం

2. Problem framing:
Stakeholder "Tutorial కావాలి" అంటే, Senior designer అడుగుతారు: "Tutorial ఏ సమస్యను పరిష్కరిస్తుంది? అది నిజమైన సమస్య అని ఎలా తెలుసు?" Solution ను problem గా reframe చేయడం senior skill.

3. Evidence quality:
- Triangulation – ఒకే విషయం data, interviews, support లో కనిపిస్తుందా?
- Sample bias – ఎవరితో మాట్లాడాం, ఎవరిని వదిలేశాం (ఉదా: app వదిలేసిన users)?
- Confidence level చెప్పడం – "ఇది బలంగా నిరూపితం" vs "ఇది signal మాత్రమే".

4. Business alignment:
ప్రతి research question ను business goal తో కలుపుతారు. Discovery ఫలితాన్ని metrics language లో చెబుతారు (activation, AHT, retention, cost).

5. Ethics, privacy మరియు responsibility:
- Consent, data minimisation, anonymisation.
- Real-money gaming లో responsible gaming – vulnerable users కు హాని చేసే "growth" ideas ను ప్రశ్నిస్తారు.
- AI products లో trust, transparency, human control.

6. Stakeholder management:
- Stakeholders ను research sessions లో పాల్గొనమని ఆహ్వానించడం.
- Uncomfortable findings ను evidence తో, blame లేకుండా చెప్పడం.
- Disagreement ఉన్నప్పుడు "ఈ assumption ను ఎలా test చేద్దాం?" అని proposal ఇవ్వడం.

7. Time-boxing:
"Analysis paralysis" ను నివారిస్తారు. Discovery కు స్పష్టమైన time-box (ఉదా: 2 వారాలు) మరియు exit criteria పెడతారు; మిగిలిన doubts ను experiments గా తర్వాతి phases లో test చేస్తారు.

Principal Designer అదనంగా:
- ఒక project కు మించి – company లో research practice (research repository, templates, continuous discovery rhythm) ఏర్పాటు చేస్తారు.
- Product strategy మరియు roadmap పై discovery insights తో ప్రభావం చూపిస్తారు.
- Juniors కు research skills mentor చేస్తారు.""",
 body_en="""Why this matters:
A junior designer asks "which method should I use?" A senior designer asks "which decision do we need to make, and how much evidence is enough?" Interviews for Senior, Lead and Principal roles test exactly this judgment.

1. Right-sizing:
Not every project needs full research. Two questions decide it:
- How costly is a wrong decision? (risk)
- How much evidence do we already have? (confidence)
Risk\tEvidence\tDecision
High\tLow\tDeep research (interviews + data + contextual inquiry)
High\tHigh\tLean validation (5 interviews or a quick test)
Low\tLow\tShip a small experiment and measure
Low\tHigh\tDesign directly

2. Problem framing:
When a stakeholder says "we need a tutorial", the senior designer asks: "Which problem does the tutorial solve, and how do we know it is the real problem?" Reframing a solution into a problem is a senior skill.

3. Evidence quality:
- Triangulation – does the same thing appear in data, interviews and support?
- Sample bias – whom did we talk to, and whom did we miss (e.g. users who abandoned the app)?
- Stating confidence – "this is strongly proven" vs "this is only a signal".

4. Business alignment:
Every research question is tied to a business goal. Discovery results are expressed in metrics language (activation, AHT, retention, cost).

5. Ethics, privacy and responsibility:
- Consent, data minimisation, anonymisation.
- In real-money gaming, responsible gaming – they challenge "growth" ideas that could harm vulnerable users.
- In AI products, trust, transparency and human control.

6. Stakeholder management:
- Invite stakeholders to take part in research sessions.
- Share uncomfortable findings with evidence and without blame.
- When there is disagreement, propose "how shall we test this assumption?"

7. Time-boxing:
They avoid analysis paralysis. Discovery gets a clear time-box (e.g. two weeks) and exit criteria; remaining doubts are tested as experiments in later phases.

A Principal Designer additionally:
- Builds the research practice beyond one project – a research repository, templates, a continuous-discovery rhythm.
- Influences product strategy and the roadmap with discovery insights.
- Mentors juniors in research skills.""",
 ex_te="""Classic Rummy – నిర్ణయం:
Marketing "bonus ఎక్కువ చూపించండి" అన్నారు. Senior designer: "ఇది ఒక supposition. Interviews లో players bonus కంటే 'డబ్బు పోతుందనే భయం' గురించి ఎక్కువగా మాట్లాడారు. Bonus banner పై చిన్న A/B test చేద్దాం, కానీ main investment risk-free practice పై పెడదాం." – evidence, risk, experiment, responsible gaming అన్నీ కలిపిన నిర్ణయం.

ResolveAI – నిర్ణయం:
ML team "accuracy పెంచితే adoption పెరుగుతుంది" అన్నారు. Research లో agents కు sources కనిపించకపోవడమే సమస్య అని తేలింది. నిర్ణయం: Accuracy పనితో పాటు, citations + confidence చూపించే design ను prototype చేసి test చేయడం.""",
 ex_en="""Classic Rummy – decision:
Marketing said "show a bigger bonus". The senior designer: "That's a supposition. In interviews players talked more about the fear of losing money than about bonuses. Let's run a small A/B test on the bonus banner, but put the main investment into risk-free practice." – a decision that combines evidence, risk, experimentation and responsible gaming.

ResolveAI – decision:
The ML team said "higher accuracy will increase adoption". Research showed the real problem was that agents couldn't see sources. Decision: continue the accuracy work, but also prototype and test a design that shows citations and confidence.""",
 markers=[('tip', 'Interview line', 'I right-size research by risk and existing evidence, frame problems before solutions, triangulate evidence, and express results in business metrics.')],
))

S.append(dict(
 id='st-1-12', label='Step 1.12',
 en="Discovery in real Agile product development",
 te="నిజమైన Agile Product Development లో Discovery",
 body_te="""ఎందుకు? (WHY):
చాలా companies లో "మూడు నెలల research phase" ఉండదు. Teams 2-వారాల sprints లో పనిచేస్తాయి. కాబట్టి discovery ను Agile rhythm లో ఎలా చేర్చాలో తెలియడం senior designer కు అవసరం.

Dual-track Agile (రెండు దారులు):
- Discovery track: Designer, PM, tech lead – "ఏమి నిర్మించాలి?" (research, prototypes, experiments).
- Delivery track: Engineering – "సరిగ్గా నిర్మించడం" (validated items build చేయడం).
Discovery track సాధారణంగా delivery కంటే 1–2 sprints ముందు నడుస్తుంది.

Continuous discovery:
- ప్రతి వారం కనీసం కొంత user contact (ఉదా: వారానికి 2–3 short interviews).
- Product trio (PM + Designer + Tech lead) కలిసి research లో పాల్గొనడం.
- Opportunity backlog నిర్వహించడం.

Agile ceremonies లో discovery:
Ceremony\tDiscovery పాత్ర
Sprint planning\tDiscovery tickets (research, interviews, analysis) plan చేయడం
Daily stand-up\tResearch progress, blockers (recruiting ఆలస్యం)
Backlog refinement\tFindings ఆధారంగా stories ను మార్చడం / కొత్తవి జోడించడం
Sprint review\tResearch readout, insights demo
Retrospective\tResearch process ను మెరుగుపరచడం

ఒక realistic timeline (Classic Rummy – illustrative):
- Sprint 0 (1 వారం): Kickoff, stakeholder interviews, research plan, CSD workshop.
- Sprint 1 (2 వారాలు): Analytics deep-dive, competitive review, 8 user interviews, empathy & ecosystem maps, findings readout.
- Sprint 2: Phase 2 synthesis + Phase 3 ideation మొదలు; అదే సమయంలో engineering ఇప్పటికే తెలిసిన bugs (KYC error message) fix చేస్తుంది.
- Quick win: Research లో దొరికిన "KYC error లో కారణం చూపకపోవడం" వెంటనే చిన్న story గా delivery track లోకి.

ResolveAI (B2B) ప్రత్యేకతలు:
- Customer Success team ద్వారా customers ను recruit చేయడం.
- Enterprise customers తో NDA, data agreements.
- "Design partner" customers – ప్రతి 2 వారాలకు feedback calls.

Senior Designer Agile లో ఎలా పనిచేస్తారు?:
- Research ను చిన్న, తరచూ cycles గా విభజిస్తారు.
- Findings ను వెంటనే backlog items గా మారుస్తారు – పెద్ద report కోసం ఎదురుచూడరు.
- Engineering ను discovery లో ముందుగానే చేర్చి feasibility early గా తెలుసుకుంటారు.
- "Good enough evidence" తో ముందుకు వెళ్లి, experiments తో risk తగ్గిస్తారు.""",
 body_en="""WHY:
Most companies don't have a "three-month research phase". Teams work in two-week sprints, so a senior designer needs to know how to fit discovery into the Agile rhythm.

Dual-track Agile:
- Discovery track: designer, PM, tech lead – "what should we build?" (research, prototypes, experiments).
- Delivery track: engineering – "build it right" (building validated items).
The discovery track usually runs 1–2 sprints ahead of delivery.

Continuous discovery:
- Some user contact every week (e.g. 2–3 short interviews a week).
- The product trio (PM + designer + tech lead) takes part in research together.
- An opportunity backlog is maintained.

Discovery in Agile ceremonies:
Ceremony\tRole of discovery
Sprint planning\tPlan discovery tickets (research, interviews, analysis)
Daily stand-up\tResearch progress and blockers (recruiting delays)
Backlog refinement\tChange stories or add new ones based on findings
Sprint review\tResearch readout, insight demo
Retrospective\tImprove the research process

A realistic timeline (Classic Rummy – illustrative):
- Sprint 0 (1 week): kickoff, stakeholder interviews, research plan, CSD workshop.
- Sprint 1 (2 weeks): analytics deep-dive, competitive review, 8 user interviews, empathy & ecosystem maps, findings readout.
- Sprint 2: Phase 2 synthesis and Phase 3 ideation begin; meanwhile engineering fixes already-known bugs (the KYC error message).
- Quick win: "the KYC error doesn't show a reason", found in research, goes straight into the delivery track as a small story.

ResolveAI (B2B) specifics:
- Recruit customers through the Customer Success team.
- NDAs and data agreements with enterprise customers.
- "Design partner" customers – feedback calls every two weeks.

How a senior designer works in Agile:
- Splits research into small, frequent cycles.
- Turns findings into backlog items immediately instead of waiting for a big report.
- Involves engineering early in discovery to learn feasibility early.
- Moves forward with "good enough evidence" and reduces risk through experiments.""",
 ex_te="""Jira లో discovery tickets (ఉదాహరణ):
- DISC-1: Stakeholder interviews (5) – Designer
- DISC-2: Funnel analysis install → first game – Data Analyst + Designer
- DISC-3: Recruit 8 new players (Telugu + English) – Researcher/Support
- DISC-4: Interview guide + consent form – Designer
- DISC-5: Competitive review (4 apps) – Designer
- DISC-6: Findings readout – Designer + PM
- BUG-212 (quick win): KYC failure లో కారణం మరియు next step చూపించడం – Engineering

ResolveAI design-partner rhythm:
ప్రతి 2 వారాలకు 3 customer companies తో 30 నిమిషాల call; ప్రతి sprint review లో "What we learned" slide.""",
 ex_en="""Discovery tickets in Jira (example):
- DISC-1: Stakeholder interviews (5) – Designer
- DISC-2: Funnel analysis, install → first game – Data Analyst + Designer
- DISC-3: Recruit 8 new players (Telugu + English) – Researcher/Support
- DISC-4: Interview guide + consent form – Designer
- DISC-5: Competitive review (4 apps) – Designer
- DISC-6: Findings readout – Designer + PM
- BUG-212 (quick win): show the reason and next step on KYC failure – Engineering

ResolveAI design-partner rhythm:
A 30-minute call with 3 customer companies every two weeks; a "What we learned" slide in every sprint review.""",
 markers=[('tip', 'Interview line', 'In Agile I run discovery one or two sprints ahead of delivery with the PM and tech lead, and I turn findings into backlog items quickly rather than waiting for a big report.')],
))

S.append(dict(
 id='st-1-13', label='Step 1.13',
 en="Project scenarios and interview questions for Phase 1",
 te="Phase 1 – ప్రాజెక్ట్ Scenarios మరియు Interview Questions",
 body_te="""Practical Scenarios (మీరైతే ఏమి చేస్తారు?):

Scenario 1 – సమయం లేదు:
PM: "Research కు సమయం లేదు, వచ్చే sprint లో tutorial build చేయాలి."
Senior approach: పూర్తిగా వద్దనకుండా lean గా – 2 రోజుల్లో funnel data + 5 quick interviews + support tickets review. అదే సమయంలో tutorial ను "hypothesis" గా రాసి, success metric నిర్ణయించి, చిన్న version తో experiment.

Scenario 2 – Stakeholder vs data:
CEO: "Users కు మా app చాలా ఇష్టం." Data: D7 retention 12%.
Senior approach: వాదించకుండా data మరియు user quotes చూపించి, "ఏ users కు ఇష్టం, ఏ users వదిలేస్తున్నారు?" అని segment వారీగా చూపించడం.

Scenario 3 – Users ను చేరుకోలేము (B2B):
ResolveAI customers agents తో మాట్లాడనివ్వడం లేదు.
Senior approach: Customer Success ద్వారా design-partner program, product usage data, support tickets, internal support team ను proxy గా ఉపయోగించడం – కానీ proxy limitation ను స్పష్టంగా చెప్పడం.

Scenario 4 – Data మరియు interviews విరుద్ధంగా ఉన్నాయి:
Interviews లో "rules సులభం" అన్నారు; data లో rules screen తర్వాత 40% drop.
Senior approach: చెప్పేది vs చేసేది తేడా – usability observation లేదా session recordings తో లోతుగా పరిశీలించడం.

Interview Questions (practise చేయండి):
1. How do you start a project when the requirements are unclear?
2. Walk me through how you plan user research.
3. How do you decide which research method to use?
4. How many users do you interview, and how do you know it's enough?
5. How do you handle a stakeholder who insists on a solution before research?
6. How do you combine qualitative and quantitative data?
7. Tell me about a time research changed the direction of a project.
8. How do you avoid bias in user interviews?
9. What is a CSD Matrix and when do you use it?
10. How do you do research when you cannot access users directly?
11. How do you fit discovery into an Agile sprint?
12. How do you present research findings to leadership?

Model answer – Q7 (Classic Rummy, STAR):
- Situation: First-game activation తక్కువగా ఉంది; team bonus offers పెంచాలనుకుంది.
- Task: Drop-off కారణం తెలుసుకుని సరైన direction ఇవ్వడం.
- Action: Funnel analysis, support tickets, 8 interviews; CSD workshop లో bonus assumption ను test చేశాం.
- Result: అసలు సమస్య "real money లో తప్పు చేస్తామనే భయం" అని తేలింది; team practice game మరియు KYC guidance వైపు direction మార్చింది.""",
 body_en="""Practical scenarios (what would you do?):

Scenario 1 – no time:
PM: "There's no time for research; we need to build a tutorial next sprint."
Senior approach: don't refuse – go lean: in two days, review funnel data, run 5 quick interviews and review support tickets. At the same time, write the tutorial up as a hypothesis, define a success metric and run a small experiment.

Scenario 2 – stakeholder vs data:
CEO: "Users love our app." Data: D7 retention is 12%.
Senior approach: don't argue; show the data and user quotes, segmented: "which users love it, and which users leave?"

Scenario 3 – users can't be reached (B2B):
ResolveAI customers won't let us talk to their agents.
Senior approach: a design-partner programme through Customer Success, product usage data, support tickets and the internal support team as a proxy – while clearly stating the limits of a proxy.

Scenario 4 – data and interviews contradict:
In interviews people said "the rules are easy"; the data shows a 40% drop after the rules screen.
Senior approach: say vs do gap – investigate further with usability observation or session recordings.

Interview questions (practise these):
1. How do you start a project when the requirements are unclear?
2. Walk me through how you plan user research.
3. How do you decide which research method to use?
4. How many users do you interview, and how do you know it's enough?
5. How do you handle a stakeholder who insists on a solution before research?
6. How do you combine qualitative and quantitative data?
7. Tell me about a time research changed the direction of a project.
8. How do you avoid bias in user interviews?
9. What is a CSD Matrix and when do you use it?
10. How do you do research when you cannot access users directly?
11. How do you fit discovery into an Agile sprint?
12. How do you present research findings to leadership?

Model answer – Q7 (Classic Rummy, STAR):
- Situation: first-game activation was low; the team wanted to increase bonus offers.
- Task: find the cause of the drop-off and set the right direction.
- Action: funnel analysis, support tickets and 8 interviews; we tested the bonus assumption in a CSD workshop.
- Result: the real problem was the fear of making mistakes with real money; the team shifted direction to a practice game and KYC guidance.""",
 ex_te="""Practice చిట్కా:
ప్రతి interview question కు 60–90 సెకన్ల సమాధానం English లో చెప్పండి. నిర్మాణం:
1. నా approach (ఒక line)
2. Steps (3–4)
3. Classic Rummy లేదా ResolveAI ఉదాహరణ
4. ఫలితం / నేర్చుకున్నది

Illustrative సంఖ్యలు చెబితే "for example" అని చెప్పండి.""",
 ex_en="""Practice tip:
Answer each interview question in English in 60–90 seconds. Structure:
1. My approach (one line)
2. Steps (3–4)
3. A Classic Rummy or ResolveAI example
4. Result / learning

When you use illustrative numbers, say "for example".""",
 markers=[],
))

S.append(dict(
 id='st-1-14', label='Step 1.14',
 en="Phase 1 knowledge check",
 te="Phase 1 జ్ఞాన పరీక్ష (Knowledge Check)",
 body_te="""ముందు సమాధానాలు చూడకుండా ప్రయత్నించండి. తర్వాత క్రింద ఉన్న జవాబులతో పోల్చండి.

భాగం A – బహుళ ఎంపిక (Multiple choice):
1. Discovery phase యొక్క ప్రధాన లక్ష్యం ఏమిటి?
(a) త్వరగా screens design చేయడం (b) సరైన సమస్యను evidence తో గుర్తించడం (c) Design system తయారు చేయడం (d) Developers కు specs ఇవ్వడం
2. "Users first game ఎందుకు మొదలుపెట్టడం లేదు?" – ఇది ఏ రకమైన ప్రశ్న?
(a) Interview question (b) Research question (c) Survey question (d) Usability task
3. CSD Matrix లో "పెద్ద bonus చూపిస్తే activation పెరుగుతుంది" ఏ column లో వస్తుంది (evidence లేకపోతే)?
(a) Certainty (b) Supposition (c) Doubt (d) ఏదీ కాదు
4. Analytics మనకు ప్రధానంగా ఏమి చెబుతుంది?
(a) ఎందుకు (b) ఏమి / ఎక్కడ / ఎంత మంది (c) User భావాలు (d) Solution
5. Empathy map లోని నాలుగు quadrants ఏవి?
(a) Plan, Do, Check, Act (b) Says, Thinks, Does, Feels (c) Must, Should, Could, Won't (d) Reach, Impact, Confidence, Effort

భాగం B – చిన్న సమాధానాలు (Short answer):
6. Research question మరియు interview question మధ్య తేడా ఒక ఉదాహరణతో చెప్పండి.
7. Triangulation అంటే ఏమిటి? ఎందుకు ముఖ్యం?
8. Contextual inquiry ఎప్పుడు అవసరం? ResolveAI ఉదాహరణ ఇవ్వండి.
9. Finding, Insight, Opportunity area – తేడా ఏమిటి?
10. Phase 1 deliverables Phase 2 కు ఎలా కనెక్ట్ అవుతాయి? రెండు ఉదాహరణలు.

భాగం C – Scenario:
11. PM research లేకుండా వెంటనే tutorial build చేయాలంటున్నారు. Senior designer గా మీరు ఏమి చేస్తారు? (3–4 lines)
12. Leading question ను open question గా మార్చండి: "మా కొత్త wallet design సులభంగా ఉంది కదా?"

### Answer key
జవాబులు (Answers)

1. (b) – సరైన సమస్యను evidence తో గుర్తించడం.
2. (b) – Research question; team తెలుసుకోవాల్సినది. Users ను నేరుగా ఇలా అడగము.
3. (b) – Supposition; evidence లేని నమ్మకం. Test చేయాలి.
4. (b) – ఏమి, ఎక్కడ, ఎంత మంది. "ఎందుకు" కు qualitative research.
5. (b) – Says, Thinks, Does, Feels (+ Pains, Gains).
6. Research question = team కోసం ("Verification దగ్గర ఎందుకు ఆగుతున్నారు?"). Interview question = user ను అడిగేది ("చివరిసారి మీ documents upload చేసినప్పుడు ఏమి జరిగిందో చెప్పండి").
7. ఒకే finding ను 2+ sources (data, interviews, support) తో నిర్ధారించడం; ఒక source లోని bias లేదా తప్పు నుంచి రక్షిస్తుంది, confidence పెంచుతుంది.
8. సంక్లిష్ట workflows, అనేక tools ఉన్నప్పుడు, users చెప్పేది మరియు చేసేది వేరుగా ఉన్నప్పుడు. ResolveAI: agent desk వద్ద గమనిస్తే AI answer ను knowledge base లో మళ్లీ verify చేస్తున్నారని తెలిసింది.
9. Finding = evidence తో గమనించినది; Insight = దాని వెనుక ఉన్న "ఎందుకు"; Opportunity = design మెరుగుపరచగల ప్రాంతం (solution కాదు).
10. Interview notes → Affinity Diagram; Empathy map → Persona; Stage-wise pain points → Journey Map; Insights → Problem statements & HMW.
11. Lean research (2 రోజులు: funnel data, 5 quick interviews, support tickets), tutorial ను hypothesis గా రాసి success metric నిర్ణయించడం, చిన్న version తో experiment, results తో next step.
12. "చివరిసారి wallet లో డబ్బు add చేసినప్పుడు ఏమి జరిగిందో step by step చూపించండి." """,
 body_en="""Try first without looking at the answers, then compare with the answer key below.

Part A – multiple choice:
1. What is the main goal of the discovery phase?
(a) Design screens quickly (b) Identify the right problem with evidence (c) Build a design system (d) Give specs to developers
2. "Why don't users start their first game?" – what type of question is this?
(a) Interview question (b) Research question (c) Survey question (d) Usability task
3. In a CSD Matrix, where does "a bigger bonus will increase activation" go (if there is no evidence)?
(a) Certainty (b) Supposition (c) Doubt (d) None
4. What does analytics mainly tell us?
(a) Why (b) What / where / how many (c) User feelings (d) The solution
5. What are the four quadrants of an empathy map?
(a) Plan, Do, Check, Act (b) Says, Thinks, Does, Feels (c) Must, Should, Could, Won't (d) Reach, Impact, Confidence, Effort

Part B – short answer:
6. Explain the difference between a research question and an interview question, with an example.
7. What is triangulation, and why does it matter?
8. When is contextual inquiry needed? Give a ResolveAI example.
9. What is the difference between a finding, an insight and an opportunity area?
10. How do Phase 1 deliverables connect to Phase 2? Give two examples.

Part C – scenario:
11. The PM wants to build a tutorial immediately without research. As a senior designer, what do you do? (3–4 lines)
12. Turn this leading question into an open one: "Our new wallet design is easy, isn't it?"

### Answer key
Answers to Parts A, B and C

1. (b) – identify the right problem with evidence.
2. (b) – a research question; what the team needs to learn. We don't ask users this directly.
3. (b) – a supposition; a belief without evidence. It must be tested.
4. (b) – what, where and how many. "Why" needs qualitative research.
5. (b) – Says, Thinks, Does, Feels (+ pains, gains).
6. Research question = for the team ("Why do people stop at verification?"). Interview question = asked to the user ("Tell me what happened the last time you uploaded your documents").
7. Confirming one finding with two or more sources (data, interviews, support); it protects against the bias or error of a single source and increases confidence.
8. For complex workflows, many tools, or when what users say differs from what they do. ResolveAI: observing at the agent's desk revealed they re-verify AI answers in the knowledge base.
9. Finding = an evidence-based observation; insight = the "why" behind it; opportunity = an area design can improve (not a solution).
10. Interview notes → affinity diagram; empathy map → persona; stage-wise pain points → journey map; insights → problem statements & HMW.
11. Lean research (two days: funnel data, 5 quick interviews, support tickets), write the tutorial up as a hypothesis with a success metric, test a small version, then decide the next step from the results.
12. "Show me, step by step, what happened the last time you added money to your wallet." """,
 ex_te="""స్కోర్ ఎలా చూసుకోవాలి:
- 10–12 సరైనవి: Phase 2 కు సిద్ధం.
- 7–9: Steps 1.3, 1.7, 1.10 మళ్లీ చదవండి.
- 6 కంటే తక్కువ: Phase 1 మొత్తం మళ్లీ చదివి, ఉదాహరణలను మీ మాటల్లో చెప్పి practice చేయండి.

Phase 2 (Define & Synthesize) కు వెళ్లే ముందు ఈ పరీక్ష పూర్తి చేయండి.""",
 ex_en="""How to score yourself:
- 10–12 correct: ready for Phase 2.
- 7–9: re-read Steps 1.3, 1.7 and 1.10.
- Fewer than 6: re-read all of Phase 1 and practise explaining the examples in your own words.

Complete this check before moving to Phase 2 (Define & Synthesize).""",
 markers=[],
))
