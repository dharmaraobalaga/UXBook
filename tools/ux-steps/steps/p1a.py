"""Phase 1 – Discovery & Research, steps 1.1–1.5"""
S = []

S.append(dict(
 id='st-1-1', label='Step 1.1',
 en="Phase 1 at a glance: Discovery & Research",
 te="Phase 1 ఒక్క చూపులో: కనుగొనడం మరియు పరిశోధన",
 figure='st-p1-map',
 body_te="""ఎందుకు? (WHY):
వ్యాపారం, వినియోగదారులు, మార్కెట్, ప్రస్తుత అనుభవం మరియు సమస్యలను ఆధారాలతో (evidence) అర్థం చేసుకోవడం. పరిష్కారానికి వెంటనే వెళ్లకుండా, సరైన సమస్యను గుర్తించడం ఈ దశ లక్ష్యం. తప్పు సమస్యకు అందమైన పరిష్కారం తయారు చేస్తే సమయం, డబ్బు రెండూ వృథా అవుతాయి.

ఏమిటి? (WHAT):
Discovery అంటే "మనకు నిజంగా ఏం తెలుసు, ఏం తెలియదు?" అని స్పష్టం చేసుకునే దశ. Research అంటే ఆ ప్రశ్నలకు users, data, stakeholders మరియు market నుంచి సమాధానాలు సేకరించడం.

ఎప్పుడు? (WHEN):
- కొత్త product లేదా పెద్ద feature ప్రారంభించే ముందు.
- Metrics పడిపోయినప్పుడు (ఉదా: registration drop-off పెరిగినప్పుడు).
- కొత్త user segment లేదా market కు వెళ్లేటప్పుడు.
- Team లో అభిప్రాయ భేదాలు ఉన్నప్పుడు – evidence తో నిర్ణయించడానికి.
Agile లో discovery ఒకేసారి జరిగి ముగిసేది కాదు; ప్రతి sprint లో కొంత continuous discovery జరుగుతుంది.

ఎలా? (HOW) – Phase 1 యొక్క 9 steps:
1. Kickoff & Stakeholder Interviews – business goals, constraints, success తెలుసుకోవడం (Step 1.2).
2. Research Plan & Research Questions – ఏమి తెలుసుకోవాలి, ఎలా (Step 1.3).
3. Analytics & Support-ticket Review – ప్రవర్తనా ఆధారాలు (Step 1.4).
4. Competitive Review – market conventions, gaps (Step 1.5).
5. User Interviews & Contextual Inquiry – users నిజంగా ఎలా పని చేస్తారు (Step 1.6).
6. CSD Matrix – facts ను assumptions నుంచి వేరు చేయడం (Step 1.7).
7. Ecosystem Map – user చుట్టూ ఉన్న actors, systems (Step 1.8).
8. Empathy Map – user ఏమి చెబుతారు, ఆలోచిస్తారు, చేస్తారు, అనుభూతి చెందుతారు (Step 1.9).
9. Research Findings & Opportunity Areas – Phase 2 కు handoff (Step 1.10).

Inputs → Outputs:
Inputs\tOutputs (Deliverables)
Project brief, business goals\tResearch plan మరియు research questions
Analytics, support tickets\tStakeholder interview notes
Stakeholders, users\tUser interview notes / recordings (consent తో)
Competitor products\tCompetitive analysis
Existing research\tCSD Matrix, Ecosystem Map, Empathy Map
\tResearch findings / opportunity areas

Phase 1 ఎప్పుడు పూర్తయినట్టు? (Exit criteria):
- ప్రధాన research questions కు evidence తో సమాధానాలు ఉన్నాయి.
- Facts, assumptions, doubts స్పష్టంగా వేరు చేయబడ్డాయి.
- Top pain points మరియు opportunity areas పై team అంగీకరించింది.
- ఏ assumptions ఇంకా test చేయాలో తెలుసు.

తదుపరి దశకు కనెక్షన్:
Phase 1 raw evidence ఇస్తుంది. Phase 2 (Define & Synthesize) లో ఆ evidence ను Affinity Diagram, Personas, Journey Maps మరియు Problem Statements గా మారుస్తాం.

విజయాన్ని ఎలా కొలవాలి?:
Research పూర్తి చేయడం కంటే insight quality ముఖ్యం. Baseline metrics నమోదు చేయండి: registration completion, first-game activation, support contact reasons, task frequency, current task time, customer satisfaction baseline.""",
 body_en="""WHY:
To understand the business, users, market, current experience and problems through evidence before committing to a solution. The goal is to find the right problem. A beautiful solution to the wrong problem wastes both time and money.

WHAT:
Discovery clarifies "what do we really know, and what don't we know?" Research collects answers to those questions from users, data, stakeholders and the market.

WHEN:
- Before starting a new product or a major feature.
- When metrics drop (for example, registration drop-off rises).
- When entering a new user segment or market.
- When the team disagrees – to decide with evidence.
In Agile, discovery is not a one-time stage; some continuous discovery happens every sprint.

HOW – the 9 steps of Phase 1:
1. Kickoff & stakeholder interviews – business goals, constraints, success (Step 1.2).
2. Research plan & research questions – what to learn and how (Step 1.3).
3. Analytics & support-ticket review – behavioural evidence (Step 1.4).
4. Competitive review – market conventions and gaps (Step 1.5).
5. User interviews & contextual inquiry – how users really work (Step 1.6).
6. CSD Matrix – separate facts from assumptions (Step 1.7).
7. Ecosystem map – actors and systems around the user (Step 1.8).
8. Empathy map – what users say, think, do and feel (Step 1.9).
9. Research findings & opportunity areas – handoff to Phase 2 (Step 1.10).

Inputs → Outputs:
Inputs\tOutputs (deliverables)
Project brief, business goals\tResearch plan and research questions
Analytics, support tickets\tStakeholder interview notes
Stakeholders, users\tUser interview notes / recordings (with consent)
Competitor products\tCompetitive analysis
Existing research\tCSD Matrix, ecosystem map, empathy map
\tResearch findings / opportunity areas

When is Phase 1 done? (Exit criteria):
- The key research questions have evidence-based answers.
- Facts, assumptions and doubts are clearly separated.
- The team agrees on the top pain points and opportunity areas.
- We know which assumptions still need testing.

Connection to the next phase:
Phase 1 produces raw evidence. In Phase 2 (Define & Synthesize) we turn it into an affinity diagram, personas, journey maps and problem statements.

How to measure success:
Insight quality matters more than research completion. Record baseline metrics: registration completion, first-game activation, support contact reasons, task frequency, current task time and a customer-satisfaction baseline.""",
 ex_te="""Classic Rummy:
కొత్త ఆటగాళ్లు registration లేదా first game దగ్గర ఎందుకు ఆగిపోతున్నారు? కొత్త users, returning users, support team తో మాట్లాడాలి. Funnel లో install → registration → first game drop-off చూడాలి. KYC, payment trust, language, rules clarity assumptions ను CSD Matrix లో పెట్టాలి.

ResolveAI:
Support agents, team leads, customers తో interviews. Ticket data లో repeated issues, resolution time, escalation reasons. "Agents ఏ tools మధ్య మారుతున్నారు? AI suggestions పై నమ్మకం ఉందా? Customer కు status అర్థమవుతోందా?" వంటి ప్రశ్నలతో research.""",
 ex_en="""Classic Rummy:
Why do new players stop at registration or before their first game? Talk to new users, returning users and the support team. Review the install → registration → first-game funnel. Put assumptions about KYC, payment trust, language and rules clarity into a CSD Matrix.

ResolveAI:
Interview support agents, team leads and customers. In ticket data, look at repeated issues, resolution time and escalation reasons. Research questions: Which tools do agents switch between? Do they trust AI suggestions? Do customers understand the ticket status?""",
 markers=[('tip', 'Interview line', 'I did not start with a solution. I first gathered business goals, user needs, existing data and stakeholder perspectives, validated the main pain points and separated assumptions from facts.'),
          ('mistake', 'సాధారణ తప్పులు', 'Stakeholder opinion ను user truth గా భావించడం; చిన్న sample నుంచి అందరికీ వర్తించే నిర్ణయం; leading questions; research లేకుండా solution నిర్ణయించడం; consent/privacy విస్మరించడం.')],
))

S.append(dict(
 id='st-1-2', label='Step 1.2',
 en="Kickoff and stakeholder interviews",
 te="Kickoff మరియు Stakeholder Interviews",
 body_te="""ఎందుకు? (WHY):
Design చేసే ముందు business ఏమి సాధించాలనుకుంటోంది, ఏ పరిమితులు (constraints) ఉన్నాయి, success ను ఎలా కొలుస్తారు అనేది తెలియాలి. Stakeholders కు ఉన్న జ్ఞానం, అంచనాలు మరియు రాజకీయ వాస్తవాలు (who decides what) తెలియకపోతే design తర్వాత reject అవుతుంది.

ఏమిటి? (WHAT):
- Kickoff meeting: Team అంతా కలిసి problem, goals, scope, timeline, roles పై అంగీకారానికి వచ్చే మొదటి meeting.
- Stakeholder interview: Product, business, engineering, support, compliance, marketing వంటి వారితో ఒక్కొక్కరితో 30–45 నిమిషాల structured సంభాషణ.

ఎప్పుడు? (WHEN):
ప్రాజెక్ట్ మొదటి వారంలో, user research కు ముందు. కొత్త stakeholder చేరినప్పుడు లేదా goals మారినప్పుడు మళ్లీ.

ఎలా? (HOW):
1. Stakeholder list తయారు చేయండి – ఎవరు నిర్ణయిస్తారు, ఎవరు ప్రభావితం అవుతారు, ఎవరికి జ్ఞానం ఉంది.
2. Interview guide సిద్ధం చేయండి (క్రింద ప్రశ్నలు).
3. ఒక్కొక్కరితో విడిగా మాట్లాడండి – group లో అందరూ నిజం చెప్పరు.
4. "ఎందుకు?" అని లోతుగా అడగండి; solution చెబితే దాని వెనుక ఉన్న problem కనుగొనండి.
5. Notes ను ఒకే template లో రాయండి; 24 గంటల్లో సారాంశం పంపి నిర్ధారించుకోండి.
6. అందరి goals ను పోల్చి conflicts గుర్తించండి.

Stakeholder interview ప్రశ్నలు:
- ఈ project విజయవంతమైతే 6 నెలల్లో ఏమి మారుతుంది?
- మీరు ఏ metric ను చూసి success అని చెబుతారు?
- ఇప్పటి వరకు ఏమి ప్రయత్నించారు? ఎందుకు పనిచేయలేదు?
- ఏ constraints ఉన్నాయి – technical, legal, budget, timeline?
- Users గురించి మీకు ఏమి తెలుసు? ఆ విషయం ఎలా తెలిసింది?
- అతిపెద్ద risk ఏమిటి?

Deliverable: Stakeholder interview notes:
- ప్రయోజనం (Purpose): Business goals, success metrics, constraints, risks మరియు stakeholder assumptions ను ఒకే చోట నమోదు చేయడం.
- నిర్మాణం (Structure): Stakeholder పేరు/పాత్ర · Goals · Success metric · Constraints · Known user problems · Assumptions · Risks · Quotes.
- తయారీ (Creation): ప్రతి interview తర్వాత template నింపండి → ఒక summary table లో కలపండి → conflicts హైలైట్ చేయండి → stakeholders తో validate చేయండి.

తదుపరి step కు కనెక్షన్:
Stakeholder assumptions → Research Plan లో research questions (Step 1.3) మరియు CSD Matrix లో Suppositions (Step 1.7) అవుతాయి. Success metrics → Analytics review (Step 1.4) లో baseline గా ఉపయోగపడతాయి.

Senior / Principal Designer నిర్ణయం:
- Solution request ("మాకు tutorial కావాలి") ను problem ("first game drop-off") గా reframe చేస్తారు.
- Conflicting goals (growth vs compliance) ను దాచకుండా బయటపెట్టి, decision-maker ఎవరో ముందే స్పష్టం చేస్తారు.
- Success metric మరియు guardrail metric రెండింటినీ kickoff లోనే అంగీకరింపజేస్తారు.

Agile ఉదాహరణ:
Sprint 0 లో kickoff (1 గంట) మరియు 5–6 stakeholder interviews (2–3 రోజులు). ఫలితం: ఒక పేజీ "Project brief + success metrics" Confluence లో, PM తో కలిసి discovery backlog తయారు.""",
 body_en="""WHY:
Before designing, you need to know what the business wants to achieve, what constraints exist and how success will be measured. If you miss stakeholders' knowledge, expectations and organisational reality (who decides what), the design will be rejected later.

WHAT:
- Kickoff meeting: the first meeting where the whole team agrees on the problem, goals, scope, timeline and roles.
- Stakeholder interview: a structured 30–45 minute conversation, one person at a time, with product, business, engineering, support, compliance, marketing and others.

WHEN:
In the first week of the project, before user research. Repeat when a new stakeholder joins or goals change.

HOW:
1. Build a stakeholder list – who decides, who is affected, who has knowledge.
2. Prepare an interview guide (questions below).
3. Interview people individually – not everyone is honest in a group.
4. Ask "why?" deeply; when someone proposes a solution, uncover the problem behind it.
5. Record notes in one template; send a summary within 24 hours to confirm.
6. Compare everyone's goals and identify conflicts.

Stakeholder interview questions:
- If this project succeeds, what changes in six months?
- Which metric tells you it worked?
- What has been tried before, and why didn't it work?
- What constraints exist – technical, legal, budget, timeline?
- What do you know about users, and how do you know it?
- What is the biggest risk?

Deliverable: stakeholder interview notes:
- Purpose: capture business goals, success metrics, constraints, risks and stakeholder assumptions in one place.
- Structure: stakeholder name/role · goals · success metric · constraints · known user problems · assumptions · risks · quotes.
- Creation: fill the template after each interview → combine into one summary table → highlight conflicts → validate with stakeholders.

Connection to the next step:
Stakeholder assumptions become research questions in the research plan (Step 1.3) and suppositions in the CSD Matrix (Step 1.7). Success metrics become the baseline for the analytics review (Step 1.4).

Senior / Principal Designer decision:
- Reframe a solution request ("we need a tutorial") into a problem ("first-game drop-off").
- Surface conflicting goals (growth vs compliance) openly and clarify early who the decision-maker is.
- Get agreement on both the success metric and the guardrail metrics during kickoff.

Agile example:
In Sprint 0: a one-hour kickoff and 5–6 stakeholder interviews over 2–3 days. Output: a one-page "project brief + success metrics" in Confluence, and a discovery backlog created with the PM.""",
 ex_te="""Classic Rummy – stakeholders:
- PM: "First-game activation 21% నుంచి 30% కు పెంచాలి."
- Compliance: "KYC మరియు 18+ check తప్పనిసరి; skip చేయలేం."
- Support: "ఎక్కువ calls 'deposit pending' మరియు 'rules అర్థం కాలేదు' గురించి."
- Marketing: "Bonus offer ఎక్కువ చూపిస్తే activation పెరుగుతుంది" ← ఇది assumption, CSD లో పెట్టాలి.

ResolveAI – stakeholders:
- Head of Support (customer): "AHT 9 నుంచి 6 నిమిషాలకు తగ్గాలి."
- ML lead: "Suggestions 80% సరైనవి, కానీ agents వాడటం లేదు."
- Security: "Customer data AI training కు వెళ్లకూడదు."
- Team lead: "కొత్త agents కు knowledge base లో వెతకడం కష్టం.\"""",
 ex_en="""Classic Rummy – stakeholders:
- PM: "Increase first-game activation from 21% to 30%."
- Compliance: "KYC and the 18+ check are mandatory; they cannot be skipped."
- Support: "Most calls are about 'deposit pending' and 'I didn't understand the rules'."
- Marketing: "Showing bigger bonus offers will increase activation" ← an assumption for the CSD Matrix.

ResolveAI – stakeholders:
- Head of Support (customer): "AHT must drop from 9 to 6 minutes."
- ML lead: "Suggestions are 80% correct, but agents don't use them."
- Security: "Customer data must not go into AI training."
- Team lead: "New agents struggle to search the knowledge base.\"""",
 markers=[('tip', 'Interview line', 'In kickoff I aligned stakeholders on the problem, success metric and guardrails, and I reframed solution requests into problems we could research.')],
))

S.append(dict(
 id='st-1-3', label='Step 1.3',
 en="Research plan and research questions",
 te="Research Plan మరియు Research Questions",
 body_te="""ఎందుకు? (WHY):
ప్రణాళిక లేని research లో అనవసర data ఎక్కువ, ఉపయోగకరమైన insight తక్కువ వస్తుంది. Research plan వల్ల team అంతా "మనం ఏమి నేర్చుకోవాలి, ఏ నిర్ణయం కోసం" అనే దానిపై align అవుతుంది, సమయం మరియు బడ్జెట్ నియంత్రణలో ఉంటాయి.

ఏమిటి? (WHAT):
Research plan అనేది ఒక చిన్న document (1–2 పేజీలు): ఏ ప్రశ్నలకు సమాధానం కావాలి, ఎవరితో, ఏ method తో, ఎప్పుడు, ఏ నిర్ణయానికి ఉపయోగపడుతుంది.
Research question ≠ Interview question. Research question = team తెలుసుకోవాల్సినది ("కొత్త players first game ఎందుకు మొదలుపెట్టడం లేదు?"). Interview question = user ను అడిగేది ("మీరు app మొదటిసారి తెరిచినప్పుడు ఏమి జరిగిందో చెప్పండి").

ఎప్పుడు? (WHEN):
Stakeholder interviews తర్వాత, users తో మాట్లాడే ముందు.

ఎలా? (HOW):
1. Stakeholder notes నుంచి assumptions మరియు unknowns జాబితా చేయండి.
2. వాటిని 3–6 research questions గా రాయండి.
3. ప్రతి ప్రశ్నకు సరైన method ఎంచుకోండి: "ఏమి జరుగుతోంది / ఎంత మంది?" → analytics, survey (quantitative). "ఎందుకు / ఎలా?" → interviews, observation (qualitative).
4. Participants నిర్ణయించండి – ఏ segment, ఎంత మంది (qualitative interviews కు సాధారణంగా ప్రతి segment కు 5–8).
5. Timeline, బాధ్యతలు, consent మరియు privacy నియమాలు రాయండి.
6. PM మరియు key stakeholders తో review చేసి sign-off తీసుకోండి.

Deliverable: Research plan:
- ప్రయోజనం: ఏమి, ఎందుకు, ఎలా research చేస్తున్నామో అందరికీ స్పష్టం చేయడం.
- నిర్మాణం: Background · Goals / decisions · Research questions · Methods · Participants & recruiting · Timeline · Roles · Consent & privacy · Deliverables · Risks.
- తయారీ: Stakeholder notes → questions → methods → participants → timeline → review → sign-off.

తదుపరి step కు కనెక్షన్:
Research questions ఆధారంగా analytics లో ఏ data చూడాలో (Step 1.4), ఏ competitors ను పరిశీలించాలో (Step 1.5), interview discussion guide ఎలా రాయాలో (Step 1.6) నిర్ణయమవుతుంది.

Senior / Principal Designer నిర్ణయం:
- "ఈ research ఏ నిర్ణయాన్ని మారుస్తుంది?" అని అడుగుతారు; నిర్ణయాన్ని మార్చని ప్రశ్నను తొలగిస్తారు.
- Risk ఎక్కువ ఉన్న చోట ఎక్కువ research, తక్కువ risk ఉన్న చోట lean research (right-sizing).
- Quantitative (ఏమి) మరియు qualitative (ఎందుకు) రెండింటినీ కలుపుతారు (triangulation).

Agile ఉదాహరణ:
Sprint 1 మొదటి రోజున research plan, PM తో 30 నిమిషాల review. Interviews 2వ వారంలో. Plan ను Jira లో discovery tickets గా విభజిస్తారు: "Analytics deep-dive", "Recruit 8 new players", "Interview guide".""",
 body_en="""WHY:
Unplanned research produces lots of data and few useful insights. A research plan aligns the team on what we need to learn and for which decision, and keeps time and budget under control.

WHAT:
A research plan is a short document (1–2 pages): which questions need answers, with whom, using which method, when, and for which decision.
A research question is not an interview question. Research question = what the team needs to learn ("Why don't new players start their first game?"). Interview question = what you ask the user ("Tell me what happened the first time you opened the app").

WHEN:
After stakeholder interviews and before talking to users.

HOW:
1. List assumptions and unknowns from the stakeholder notes.
2. Turn them into 3–6 research questions.
3. Pick the right method for each: "what is happening / how many?" → analytics, surveys (quantitative). "Why / how?" → interviews, observation (qualitative).
4. Decide participants – which segment and how many (typically 5–8 per segment for qualitative interviews).
5. Write the timeline, responsibilities, consent and privacy rules.
6. Review with the PM and key stakeholders and get sign-off.

Deliverable: research plan:
- Purpose: make clear to everyone what we are researching, why and how.
- Structure: background · goals / decisions · research questions · methods · participants & recruiting · timeline · roles · consent & privacy · deliverables · risks.
- Creation: stakeholder notes → questions → methods → participants → timeline → review → sign-off.

Connection to the next step:
The research questions decide which analytics to examine (Step 1.4), which competitors to review (Step 1.5) and how to write the interview discussion guide (Step 1.6).

Senior / Principal Designer decision:
- They ask "which decision will this research change?" and remove questions that change nothing.
- More research where risk is high, lean research where risk is low (right-sizing).
- They combine quantitative (what) and qualitative (why) evidence (triangulation).

Agile example:
Research plan on day one of Sprint 1, with a 30-minute PM review. Interviews in week two. The plan is split into Jira discovery tickets: "Analytics deep-dive", "Recruit 8 new players", "Interview guide".""",
 ex_te="""Classic Rummy – research questions:
1. కొత్త players ఏ step లో ఎక్కువగా ఆగిపోతున్నారు? (Analytics)
2. First game ముందు వారికి ఏ సందేహాలు, భయాలు ఉంటాయి? (Interviews)
3. KYC మరియు payment పై నమ్మకం activation ను ఎలా ప్రభావితం చేస్తుంది? (Interviews + support tickets)
4. Competitors కొత్త players కు rules ఎలా నేర్పుతున్నారు? (Competitive review)
Participants: 8 కొత్త players (7 రోజుల్లో install), 5 returning players, 2 support agents.

ResolveAI – research questions:
1. ఒక ticket పరిష్కరించడానికి agent ఏ steps, ఏ tools ఉపయోగిస్తారు?
2. AI suggestion ను ఎప్పుడు నమ్ముతారు, ఎప్పుడు ignore చేస్తారు, ఎందుకు?
3. ఏ ticket categories ఎక్కువ సమయం తీసుకుంటాయి?
Participants: 3 customer companies నుంచి 8 agents, 3 team leads.""",
 ex_en="""Classic Rummy – research questions:
1. At which step do most new players drop? (Analytics)
2. What doubts and fears do they have before their first game? (Interviews)
3. How does trust in KYC and payments affect activation? (Interviews + support tickets)
4. How do competitors teach rules to new players? (Competitive review)
Participants: 8 new players (installed within 7 days), 5 returning players, 2 support agents.

ResolveAI – research questions:
1. Which steps and tools does an agent use to resolve a ticket?
2. When do agents trust an AI suggestion, when do they ignore it, and why?
3. Which ticket categories take the most time?
Participants: 8 agents and 3 team leads from 3 customer companies.""",
 markers=[('tip', 'Interview line', 'I wrote a lean research plan that tied each research question to a product decision, and combined analytics (what) with interviews (why).')],
))

S.append(dict(
 id='st-1-4', label='Step 1.4',
 en="Analytics and support-ticket review",
 te="Analytics మరియు Support-ticket Review",
 figure='st-funnel',
 body_te="""ఎందుకు? (WHY):
Users ఏమి చెబుతారో కాదు, నిజంగా ఏమి చేస్తారో data చూపిస్తుంది. ఎక్కడ drop-off, ఎక్కడ errors, ఏ complaints మళ్లీ మళ్లీ వస్తున్నాయి అనేది తెలుసుకుంటే research ను సరైన చోటుపై కేంద్రీకరించవచ్చు. ఇది baseline కూడా ఇస్తుంది – తర్వాత Phase 8 లో improvement ను దీనితోనే పోలుస్తాం.

ఏమిటి? (WHAT):
- Product analytics: Events, funnels, drop-off, cohorts, retention, feature usage (ఉదా: Mixpanel, Amplitude, GA4, Firebase).
- Support-ticket / feedback review: Tickets, chat logs, app-store reviews, call reasons ను categories గా విభజించడం.
- Session recordings / heatmaps (అందుబాటులో ఉంటే, privacy నియమాలతో).

ఎప్పుడు? (WHEN):
User interviews కు ముందు – interviews లో ఏ విషయాలు లోతుగా అడగాలో తెలుస్తుంది. Interviews తర్వాత కూడా – qualitative findings ఎంత మందికి వర్తిస్తాయో చూడడానికి.

ఎలా? (HOW):
1. Data analyst తో కలిసి key funnel నిర్వచించండి (ప్రతి step కు event).
2. Step-wise conversion మరియు drop-off లెక్కించండి.
3. Segments వారీగా విభజించండి – device, language, source, new vs returning.
4. Support tickets నుంచి 100–300 sample తీసుకుని categories గా tag చేయండి (ఉదా: payment, rules, KYC, bugs).
5. Top categories ను frequency మరియు severity తో ranking చేయండి.
6. ప్రతి finding ను "ఏమి జరుగుతోంది" గా రాయండి – "ఎందుకు" అని ఇక్కడ ఊహించకండి; అది interviews లో తెలుసుకోవాలి.

Deliverable: Data / support insights summary:
- ప్రయోజనం: Behavioural evidence మరియు baseline metrics అందించడం.
- నిర్మాణం: Funnel chart · Biggest drop-offs · Segment differences · Top support categories (count, %) · Baseline metrics table · Open "why" questions.
- తయారీ: Funnel define → data pull → segment → tickets tag → rank → summary → interviews కు questions.

తదుపరి step కు కనెక్షన్:
"ఏమి" తెలుస్తుంది → User interviews (Step 1.6) లో "ఎందుకు" అడుగుతాం. Data facts → CSD Matrix లో Certainties (Step 1.7). Baseline → Phase 8 measurement.

Senior / Principal Designer నిర్ణయం:
- Correlation ను causation గా భావించరు.
- Average మాత్రమే కాదు, segments చూస్తారు (ఉదా: Telugu users లో drop-off ఎక్కువా?).
- Data లేదా tracking తప్పుగా ఉండవచ్చని తనిఖీ చేస్తారు (event సరిగ్గా fire అవుతోందా?).
- Data తక్కువ ఉన్నప్పుడు support team ను ఒక "data source" గా ఉపయోగిస్తారు.

Agile ఉదాహరణ:
Sprint 1 లో Data Analyst తో 2 sessions; ఒక dashboard తయారు చేసి sprint review లో చూపిస్తారు. Tracking లోపం దొరికితే engineering backlog లో "add event: tutorial_started" ticket వేస్తారు.""",
 body_en="""WHY:
Data shows what users actually do, not what they say. Knowing where drop-offs, errors and repeated complaints happen lets you focus research in the right place. It also gives a baseline – in Phase 8 we compare improvements against it.

WHAT:
- Product analytics: events, funnels, drop-off, cohorts, retention, feature usage (e.g. Mixpanel, Amplitude, GA4, Firebase).
- Support-ticket / feedback review: grouping tickets, chat logs, app-store reviews and call reasons into categories.
- Session recordings / heatmaps (if available, within privacy rules).

WHEN:
Before user interviews – it tells you what to probe deeply. Also after interviews – to check how many users a qualitative finding applies to.

HOW:
1. Define the key funnel with the data analyst (one event per step).
2. Calculate step-wise conversion and drop-off.
3. Segment the data – device, language, source, new vs returning.
4. Sample 100–300 support tickets and tag them into categories (e.g. payment, rules, KYC, bugs).
5. Rank the top categories by frequency and severity.
6. Write each finding as "what is happening" – don't guess "why" here; that comes from interviews.

Deliverable: data / support insights summary:
- Purpose: provide behavioural evidence and baseline metrics.
- Structure: funnel chart · biggest drop-offs · segment differences · top support categories (count, %) · baseline metrics table · open "why" questions.
- Creation: define funnel → pull data → segment → tag tickets → rank → summarise → questions for interviews.

Connection to the next step:
You learn the "what" → user interviews (Step 1.6) ask "why". Data facts → certainties in the CSD Matrix (Step 1.7). The baseline → Phase 8 measurement.

Senior / Principal Designer decision:
- They don't treat correlation as causation.
- They look at segments, not just averages (e.g. is drop-off higher for Telugu-language users?).
- They check whether the data or tracking could be wrong (is the event firing correctly?).
- When data is thin, they use the support team as a data source.

Agile example:
Two sessions with the data analyst in Sprint 1; a dashboard is shown in the sprint review. If a tracking gap is found, an engineering ticket such as "add event: tutorial_started" is added to the backlog.""",
 ex_te="""Classic Rummy (illustrative):
Install 100% → Registration 62% → Verification 38% → First game 21%.
- అతిపెద్ద drop: Registration → Verification (−24 points).
- Telugu language users లో first-game rate 15% మాత్రమే.
- Support tickets top 3: Deposit pending 31%, Rules confusion 22%, KYC rejected 18%.
ప్రశ్న interviews కోసం: Verification దగ్గర ఎందుకు వదిలేస్తున్నారు?

ResolveAI (illustrative):
- AHT 9 నిమిషాలు; "Refund" tickets AHT 14 నిమిషాలు.
- AI suggestion ఉపయోగం 18%; ఉపయోగించినప్పుడు 60% లో agent భారీగా edit చేస్తారు.
- Agents ప్రతి ticket లో సగటున 4 tools/tabs మారుతున్నారు.
ప్రశ్న: Suggestions ను ఎందుకు నమ్మడం లేదు?""",
 ex_en="""Classic Rummy (illustrative):
Install 100% → registration 62% → verification 38% → first game 21%.
- Biggest drop: registration → verification (−24 points).
- Telugu-language users have only a 15% first-game rate.
- Top 3 support tickets: deposit pending 31%, rules confusion 22%, KYC rejected 18%.
Question for interviews: why do people give up at verification?

ResolveAI (illustrative):
- AHT 9 minutes; "refund" tickets 14 minutes.
- AI suggestions used on 18% of tickets; when used, agents heavily edit 60% of them.
- Agents switch between 4 tools/tabs per ticket on average.
Question: why don't they trust the suggestions?""",
 markers=[('mistake', 'సాధారణ తప్పు', 'Data లో drop-off చూసి వెంటనే "ఇది UI సమస్య" అని నిర్ణయించడం. Data "ఎక్కడ" అని చెబుతుంది; "ఎందుకు" అని users చెప్పాలి.')],
))

S.append(dict(
 id='st-1-5', label='Step 1.5',
 en="Competitive review",
 te="Competitive Review (పోటీ ఉత్పత్తుల విశ్లేషణ)",
 figure='ux-14',
 body_te="""ఎందుకు? (WHY):
Users మన product ను ఒంటరిగా ఉపయోగించరు; ఇతర apps నుంచి అలవాట్లు (conventions) తెచ్చుకుంటారు. Competitors ఏమి బాగా చేస్తున్నారు, ఎక్కడ gaps ఉన్నాయి, market లో ఏది standard (users ఆశించేది) అనేది తెలిస్తే, అనవసరంగా కొత్తది కనిపెట్టకుండా, నిజమైన differentiation ఎక్కడ ఇవ్వాలో తెలుస్తుంది.

ఏమిటి? (WHAT):
- Direct competitors: అదే సమస్యను అదే users కు పరిష్కరించేవారు.
- Indirect competitors: అదే user need ను వేరే విధంగా తీర్చేవారు.
- Analogous / inspiration products: వేరే industry అయినా అదే pattern బాగా చేసే వారు.
Competitive review = వారి user flows, features, content, strengths, weaknesses ను structured గా పోల్చడం. ఇది copy చేయడం కాదు.

ఎప్పుడు? (WHEN):
Discovery లో, research questions తర్వాత. Ideation (Phase 3) లో patterns కోసం మళ్లీ చూడవచ్చు.

ఎలా? (HOW):
1. 3–5 competitors మరియు 1–2 analogous products ఎంచుకోండి.
2. పోల్చాల్సిన tasks నిర్ణయించండి (ఉదా: "కొత్త user మొదటి game వరకు").
3. ప్రతి product లో ఆ task ను మీరే పూర్తి చేసి screenshots తీసుకోండి.
4. ఒక comparison matrix లో నింపండి: steps సంఖ్య, సమయం, help/tutorial, trust signals, తేడాలు.
5. Strengths, weaknesses, conventions, opportunities గుర్తించండి.
6. "మనకు ఏమి నేర్చుకోవాలి" అని 3–5 lines గా సారాంశం రాయండి.

Deliverable: Competitive analysis:
- ప్రయోజనం: Market conventions, best practices, gaps మరియు differentiation అవకాశాలు చూపించడం.
- నిర్మాణం: Competitor list · Comparison matrix (criteria × products) · Annotated screenshots · Strengths/weaknesses · Patterns to adopt / avoid · Opportunities.
- తయారీ: Select → define tasks → walkthrough → capture → compare → summarise → team తో share.

తదుపరి step కు కనెక్షన్:
Patterns → Phase 3 Ideation లో ideas. Users ఆశించే conventions → Phase 4 IA మరియు navigation నిర్ణయాలు. Competitor తో పోల్చిన అనుభవాలు → user interviews లో "మీరు ఇంతకు ముందు ఏ app వాడారు?" అనే ప్రశ్నలు.

Senior / Principal Designer నిర్ణయం:
- Features సంఖ్య కాదు, user outcome పోలుస్తారు.
- "Industry standard" ను అనుసరించడం vs differentiation ఎక్కడ – రెండింటినీ స్పష్టంగా వేరు చేస్తారు.
- Regulation లేదా business model తేడాల వల్ల competitor pattern మనకు సరిపోకపోవచ్చని గుర్తిస్తారు.

Agile ఉదాహరణ:
ఒక designer 2–3 రోజుల్లో review చేసి, Figma/Miro board లో annotated screenshots పెడతారు. Sprint review లో 10 నిమిషాల "competitor walkthrough" చూపిస్తారు.""",
 body_en="""WHY:
Users don't use our product in isolation; they bring habits (conventions) from other apps. Knowing what competitors do well, where the gaps are and what is standard in the market (what users expect) helps you avoid reinventing the wheel and shows where real differentiation is possible.

WHAT:
- Direct competitors: solve the same problem for the same users.
- Indirect competitors: meet the same user need in a different way.
- Analogous / inspiration products: different industry, but do the same pattern well.
A competitive review is a structured comparison of their user flows, features, content, strengths and weaknesses. It is not copying.

WHEN:
During discovery, after the research questions are set. Revisit it during ideation (Phase 3) for patterns.

HOW:
1. Choose 3–5 competitors and 1–2 analogous products.
2. Decide the tasks to compare (e.g. "new user up to their first game").
3. Complete the task yourself in each product and capture screenshots.
4. Fill a comparison matrix: number of steps, time, help/tutorial, trust signals, differences.
5. Identify strengths, weaknesses, conventions and opportunities.
6. Summarise "what we should learn" in 3–5 lines.

Deliverable: competitive analysis:
- Purpose: show market conventions, best practices, gaps and differentiation opportunities.
- Structure: competitor list · comparison matrix (criteria × products) · annotated screenshots · strengths/weaknesses · patterns to adopt / avoid · opportunities.
- Creation: select → define tasks → walk through → capture → compare → summarise → share with the team.

Connection to the next step:
Patterns → ideas in Phase 3. Conventions users expect → IA and navigation decisions in Phase 4. Competitor experiences → interview questions such as "Which app did you use before?"

Senior / Principal Designer decision:
- They compare user outcomes, not feature counts.
- They clearly separate where to follow the "industry standard" and where to differentiate.
- They recognise that a competitor pattern may not fit because of regulation or business-model differences.

Agile example:
One designer reviews competitors in 2–3 days and posts annotated screenshots on a Figma/Miro board, then gives a 10-minute "competitor walkthrough" in the sprint review.""",
 ex_te="""Classic Rummy – "Install నుంచి first game వరకు" పోలిక (illustrative):
Criteria\tCompetitor A\tCompetitor B\tClassic Rummy
Steps\t6\t9\t11
Practice game\tఉంది\tలేదు\tలేదు
Rules help\tVideo\tText\tText (పొడవు)
Trust signals\tCertifications, withdrawals proof\tకొన్ని\tతక్కువ
Learning: Practice game మరియు చిన్న rules video convention గా మారుతున్నాయి.

ResolveAI – పోలిక:
- Competitor X: AI reply ఉంది కానీ source చూపదు.
- Competitor Y: Knowledge citations చూపిస్తుంది, ticket summary లేదు.
- Analogous (code assistant): Suggestion ను "accept / edit / reject" తో inline గా చూపిస్తుంది.
Opportunity: Cited answer + confidence + inline edit.""",
 ex_en="""Classic Rummy – "install to first game" comparison (illustrative):
Criteria\tCompetitor A\tCompetitor B\tClassic Rummy
Steps\t6\t9\t11
Practice game\tYes\tNo\tNo
Rules help\tVideo\tText\tText (long)
Trust signals\tCertifications, withdrawal proof\tSome\tFew
Learning: a practice game and a short rules video are becoming conventions.

ResolveAI – comparison:
- Competitor X: has AI replies but shows no sources.
- Competitor Y: shows knowledge citations but no ticket summary.
- Analogous (code assistant): shows suggestions inline with accept / edit / reject.
Opportunity: cited answer + confidence + inline editing.""",
 markers=[('mistake', 'సాధారణ తప్పు', 'Competitor feature list ను నేరుగా roadmap గా మార్చడం. ముందు మన users కు ఆ సమస్య ఉందో లేదో evidence తో తనిఖీ చేయండి.')],
))
