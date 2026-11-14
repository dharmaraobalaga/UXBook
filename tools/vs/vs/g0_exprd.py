# Group 0 · 0.8 – Practical PRD exercise: reviewing a PM's PRD as a Senior Product Designer (Classic Rummy – First-Time Player Onboarding).
# Source: Example_PRD.pdf (Telugu-first, short). Telugu answer = PDF text (assembled by hand); English answer = PDF English text + Claude's
# translation of the Telugu lines. Diagram = Claude's own drawing (figs_g0.py: vs-prd-review). The model answer to Question 1 was written by Claude.

def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'
FIG = ('vs-prd-review', 'Eight coloured cards: Problem, Research, Users, Requirements, UX, Edge cases, Metrics, Scope – each with the question to check')

PRD_DOC = """PRODUCT REQUIREMENTS DOCUMENT – Draft
First-Time Player Onboarding
Product – Classic Rummy · Feature ID: CR-ONB-001 · Version 1.0

1 · Feature Overview:
We want to improve the first-time player experience by introducing a simple onboarding experience that helps new users understand the basic Rummy gameplay before joining their first table.

2 · Problem Statement:
New users may find it difficult to understand the game rules, card arrangement and basic gameplay actions. This may create confusion and prevent them from confidently starting their first game.

3 · Business Goal:
- Improve new-player activation.
- Increase first-game participation.
- Reduce early user drop-offs.
- Improve the first-time player experience.

4 · Target Users:
- First-time Rummy players.
- Users unfamiliar with Rummy rules.
- Users who need guidance before joining a game.

5 · Proposed Solution – introduce an interactive onboarding experience covering:
- Basic Rummy rules.
- Card arrangement.
- Sequences and sets.
- Game actions.
- How to start playing.

6 · Functional Requirements:

ID\tRequirement
FR-01\tDisplay onboarding to eligible first-time users.
FR-02\tExplain basic Rummy rules.
FR-03\tDemonstrate card arrangement.
FR-04\tExplain sequences and sets.
FR-05\tProvide a way to skip onboarding.
FR-06\tAllow users to access help later.
FR-07\tProvide an option to start playing after onboarding.

7 · Success Metrics:
- Onboarding completion rate.
- First-game start rate.
- Time to first game.
- First-game abandonment rate.

8 · Out of Scope:
- Complete redesign of the Rummy gameplay interface.
- Changes to the game scoring engine.
- Changes to tournament functionality.

9 · Expected Outcome:
New users should understand the basic gameplay and feel confident enough to start their first Rummy game.

End of PM's PRD draft."""

Q_EN = "Practical PRD exercise: as a Senior Product Designer, how do you review a PM's PRD before starting design? (Classic Rummy – First-Time Player Onboarding)"
Q_TE = 'Practical PRD Exercise: Senior Product Designer‌గా PM ఇచ్చిన PRD‌ను Design ప్రారంభించే ముందు ఎలా Review చేయాలి? (Classic Rummy – First-Time Player Onboarding)'

TE = f"""ఇప్పుడు మనం ఒక నిజమైన Product Teamలో పనిచేస్తున్నట్లుగా Practical PRD Exercise చేద్దాం.
ఈసారి నువ్వు Senior Product Designer పాత్రలో ఉంటావు. Product Manager PRD ఇస్తారు. నువ్వు ఆ PRD‌ను విశ్లేషించి, అవసరమైన ప్రశ్నలు అడిగి, UX/UI Design Process‌ను ప్రారంభించాలి.

Practical Exercise: Classic Rummy – First-Time User Experience
- Project: Classic Rummy
- Feature: First-Time Player Onboarding
- Your Role: Senior Product Designer
- PRD ఇచ్చేవారు: Product Manager

గమనిక: ఇది నీ Classic Rummy అనుభవం ఆధారంగా రూపొందించిన hypothetical practice scenario. ఇందులోని Requirements, Metrics నిజమైన ప్రాజెక్ట్ డేటా అని భావించకూడదు.

### Part 1 · Product Manager's PRD
PM రాసిన PRD Draft (English లోనే – నిజమైన PRD లాగా)

{PRD_DOC}

### Part 2 · Senior Product Designer‌గా నీ పని
PRD ను Review చేయడం

ఒక ముఖ్యమైన విషయం: PM ఇచ్చిన PRD‌ను వెంటనే Figmaలోకి తీసుకెళ్లకూడదు. ముందుగా దానిని Review చేయాలి.

{fig(FIG[0], FIG[1], 'Figma తెరిచే ముందు PRD ను ఈ 8 అంశాల్లో Review చేయాలి.', 'Review the PRD in these 8 areas before opening Figma.')}

నీ Reviewలో ఈ అంశాలు పరిశీలించాలి:

Review Area\tనువ్వు పరిశీలించాల్సిన విషయం
Problem\tఅసలు సమస్య స్పష్టంగా ఉందా?
Research\tఈ సమస్యకు ఆధారాలు ఉన్నాయా?
Users\tTarget Users సరిగ్గా నిర్వచించారా?
Requirements\tప్రతి Requirement స్పష్టంగా ఉందా?
UX\tUser Journey, User Flow అవసరాలు ఉన్నాయా?
Edge Cases\tSkip, Exit, Return వంటి సందర్భాలు ఉన్నాయా?
Metrics\tSuccess ఎలా కొలుస్తారు?
Scope\tఏమి చేయాలి, ఏమి చేయకూడదు?

### Part 3 · Interactive Interview – Question 1
Question 1 of 5

As a Senior Product Designer, what questions would you ask the Product Manager before starting the design?

PM ఇచ్చిన PRDను పరిశీలించినప్పుడు కొన్ని విషయాలు ఇంకా స్పష్టంగా లేవు. ఉదాహరణకు:
- కొత్త యూజర్లు నిజంగా ఏ విషయంలో ఇబ్బంది పడుతున్నారు?
- Onboarding తప్పనిసరిగా చూపించాలా?
- యూజర్‌కు ఇప్పటికే Rummy తెలిసి ఉంటే?
- Tutorial మధ్యలో Exit చేస్తే ఏమవుతుంది?
- Onboarding పూర్తి చేయకుండానే Game Start చేయవచ్చా?
- Success Metrics‌కు Baseline Data ఉందా?

నీ Task: Product Manager‌ను అడగాల్సిన కనీసం 5 ముఖ్యమైన ప్రశ్నలు రాయాలి – English లో ప్రయత్నించు; Grammar mistakes వచ్చినా పరవాలేదు.
ఉదా: 1. What research data supports this problem? 2. Who are the target users? 3. ...

నీ సమాధానాన్ని ఇలా పరిశీలించుకో:
1. నీ ప్రశ్నల నాణ్యత.
2. Product Thinking.
3. UX Thinking.
4. English grammar.
5. తెలుగులో వివరణ.
6. మరింత మెరుగైన Model Answer తో పోల్చడం – ఒక Model Answer Group 0 review page లో ఉంది."""

EN = f"""Let's do a practical PRD exercise as if we were working in a real product team.
This time you are in the Senior Product Designer role. The Product Manager gives you a PRD. You analyse it, ask the necessary questions and start the UX/UI design process.

Practical Exercise: Classic Rummy – First-Time User Experience
- Project: Classic Rummy
- Feature: First-Time Player Onboarding
- Your Role: Senior Product Designer
- PRD from: Product Manager

Note: this is a hypothetical practice scenario based on your Classic Rummy experience. Don't treat its requirements and metrics as real project data.

### Part 1 · Product Manager's PRD
The PM's PRD draft

{PRD_DOC}

### Part 2 · Your job as Senior Product Designer
Reviewing the PRD

An important point: don't take the PM's PRD straight into Figma. Review it first.

{fig(FIG[0], 'PRD review areas', '', 'Review the PRD in these 8 areas before opening Figma.')}

Check these areas in your review:

Review Area\tWhat you should check
Problem\tIs the real problem clear?
Research\tIs there evidence for this problem?
Users\tAre the target users defined correctly?
Requirements\tIs every requirement clear?
UX\tAre user journey and user flow needs included?
Edge Cases\tAre cases like skip, exit and return covered?
Metrics\tHow will success be measured?
Scope\tWhat should be done – and what not?

### Part 3 · Interactive Interview – Question 1
Question 1 of 5

As a Senior Product Designer, what questions would you ask the Product Manager before starting the design?

Looking at the PM's PRD, some things are still unclear. For example:
- What exactly are new users struggling with?
- Must the onboarding be shown to everyone?
- What if the user already knows Rummy?
- What happens if they exit the tutorial midway?
- Can they start a game without completing onboarding?
- Is there baseline data for the success metrics?

Your task: write at least 5 important questions to ask the Product Manager – try in English; grammar mistakes are fine.
e.g. 1. What research data supports this problem? 2. Who are the target users? 3. ...

Check your answer against:
1. The quality of your questions.
2. Product thinking.
3. UX thinking.
4. English grammar.
5. A Telugu explanation.
6. A stronger model answer – one is on the Group 0 review page."""

EX_TE = """PRD వచ్చిన వెంటనే Figma కాదు – ముందుగా Review:
- Problem: "may find it difficult" – ఆధారం ఏమిటి? Analytics లేదా research ఉందా?
- Users: Rummy తెలిసిన కొత్త users కూ onboarding చూపించాలా?
- Edge cases: Skip, మధ్యలో exit, తిరిగి వచ్చినప్పుడు ఏమవుతుంది?
- Metrics: Onboarding completion, first-game start rate – baseline ఎంత?
- Scope: Gameplay UI redesign out of scope – onboarding అందులో ఎలా fit అవుతుంది?"""
EX_EN = """Not straight into Figma – review the PRD first:
- Problem: "may find it difficult" – what's the evidence? Is there analytics or research?
- Users: should new users who already know Rummy see onboarding too?
- Edge cases: what happens on skip, exit midway, or return later?
- Metrics: onboarding completion, first-game start rate – what's the baseline?
- Scope: the gameplay UI redesign is out of scope – how does onboarding fit into the existing UI?"""

REVISION = [['Reviewing a PRD', 'Before Figma: check problem, research, users, requirements, UX, edge cases, metrics, scope']]

MODEL = ('PRD exercise · 0.8 – model answer for Question 1', """Question: As a Senior Product Designer, what questions would you ask the Product Manager before starting the design?

ముందుగా మీ సొంత ప్రశ్నలు రాసి, తర్వాత ఈ నమూనాతో పోల్చండి. (Model answer written by Claude – one strong way to answer, not the only one.)

1. Evidence: What data or research shows that new users struggle – for example, where do first-time users drop off today, and what do support tickets or session recordings say?
2. Users: How do we define an "eligible first-time user"? Should players who already know Rummy (from other apps or offline) see the same onboarding, or can they skip it or take a quick version?
3. Flow & control: Is onboarding mandatory or optional? What happens if a user skips it, exits midway or comes back later – do they resume where they left off?
4. Format: Should onboarding be a separate tutorial, or guidance inside a practice game, so users learn by playing rather than reading?
5. Success: What are the current baselines for first-game start rate and time to first game, and what targets would count as success?
6. Constraints: Since the gameplay UI is out of scope, which existing screens and components can onboarding use, and are there any technical or legal limits (for example, real-money game rules) we must follow?
7. Help later (FR-06): Where should help live after onboarding – in the game table, in settings, or both?

Why this works: it covers evidence, users, flow and edge cases, format, metrics, constraints and the requirements that are still vague, which shows product thinking as well as UX thinking.

తెలుగు సారాంశం: సమస్యకు ఆధారం, ఎవరికి onboarding, skip/exit/resume, tutorial vs practice game, baseline metrics, scope పరిమితులు, తర్వాత help ఎక్కడ – ఈ ప్రశ్నలతో design ప్రారంభానికి ముందే PRD లోని ఖాళీలను పూరించవచ్చు.""")
