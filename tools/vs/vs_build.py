import json, pathlib
ROOT = pathlib.Path('/home/claude/interview-mastery')
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

Q1_TE = f"""User Flow (యూజర్ ఫ్లో) మరియు User Journey (యూజర్ జర్నీ) రెండూ UX Designలో చాలా ముఖ్యమైనవి. కానీ వీటి ఉద్దేశాలు వేర్వేరు.
సింపుల్‌గా చెప్పాలంటే:
- User Flow: యూజర్ ఒక పనిని పూర్తి చేయడానికి ఏయే స్టెప్స్ ద్వారా వెళ్తాడు?
- User Journey: ఒక ప్రోడక్ట్‌ను ఉపయోగిస్తున్నప్పుడు యూజర్‌కు మొదటి నుంచి చివరి వరకు ఎలాంటి అనుభవం ఎదురవుతుంది?

### 1 · User Flow
User Flow అంటే ఏమిటి?

User Flow అంటే ఒక నిర్దిష్టమైన పనిని (Task) పూర్తి చేయడానికి యూజర్ అనుసరించే దశల క్రమం.
యూజర్ ఎక్కడ ప్రారంభిస్తాడు? ఏ బటన్ క్లిక్ చేస్తాడు? తర్వాత ఏ స్క్రీన్‌కు వెళ్తాడు? చివరకు తన పని ఎలా పూర్తి చేస్తాడు? అనే విషయాలను చూపిస్తుంది.

{fig('vs-login-flow', 'Login user flow: Open App, Login Screen, Enter Mobile Number, OTP Verification, Home Screen', 'ఉదాహరణ: Classic Rummy Appలో యూజర్ Login అవ్వడం – యాప్ ఓపెన్ చేయడం → లాగిన్ స్క్రీన్ → మొబైల్ నంబర్ నమోదు → OTP ధృవీకరణ → లాగిన్ విజయవంతం.', 'Example: user login in the Classic Rummy app.')}

ఇక్కడ యూజర్ ఒక నిర్దిష్టమైన పని అయిన Login పూర్తి చేయడానికి అనుసరించే స్టెప్స్‌ను చూపించాం.

User Flow ప్రధానంగా దేనిపై దృష్టి పెడుతుంది?:
- Screen-to-screen navigation
- User actions
- Decision points
- Task completion
- Error and alternative paths

### 2 · User Journey
User Journey అంటే ఏమిటి?

User Journey అంటే ఒక ప్రోడక్ట్ లేదా సర్వీస్‌ను ఉపయోగించే క్రమంలో యూజర్‌కు ఎదురయ్యే మొత్తం అనుభవం.
యూజర్‌కు ప్రోడక్ట్ గురించి ఎలా తెలుస్తుంది? ఎందుకు ఉపయోగించాలనుకుంటాడు? ఎక్కడ ఇబ్బంది పడతాడు? అతనికి ఎలాంటి భావనలు కలుగుతాయి? చివరకు సంతృప్తి చెందుతాడా? అనే అంశాలను వివరిస్తుంది.

{fig('vs-journey', 'User journey with five stages: Awareness, Consideration, Registration, First Game, Retention', 'ఉదాహరణ: Classic Rummy Appలో కొత్త యూజర్ అనుభవం – 5 దశలు; ప్రతి దశ తెలుగు వివరణ క్రింద ఉంది.', 'Example: a new user’s experience in the Classic Rummy app.')}

ఉదాహరణ: Classic Rummy Appలో కొత్త యూజర్ అనుభవం:
1. Awareness – పరిచయం: యూజర్ ఒక ప్రకటన ద్వారా Classic Rummy App గురించి తెలుసుకుంటాడు. (Positive) “ఈ యాప్ బాగుంది, ఒకసారి ప్రయత్నించాలి.”
2. Consideration – ఆలోచన: యాప్‌ను డౌన్‌లోడ్ చేయాలా వద్దా అని ఆలోచిస్తాడు. రేటింగ్స్, ఫీచర్లు చూస్తాడు. (Uncertain) “ఇది నమ్మదగిన యాప్‌నా?”
3. Registration – నమోదు: యాప్ ఓపెన్ చేసి మొబైల్ నంబర్, OTP ద్వారా రిజిస్టర్ అవుతాడు. (Possible Friction) “రిజిస్ట్రేషన్ సులభంగా ఉందా?”
4. First Game – మొదటి గేమ్: గేమ్ ఎలా ఆడాలో తెలుసుకుని మొదటి గేమ్ ఆడతాడు. (Engaged) “గేమ్ ఆడటం ఆసక్తికరంగా ఉంది.”
5. Retention – మళ్లీ ఉపయోగించడం: మంచి అనుభవం ఉంటే యూజర్ తిరిగి యాప్ ఓపెన్ చేసి ఆడతాడు. (Satisfied) “ఈ యాప్ మళ్లీ ఉపయోగించాలి.”

User Journey ప్రధానంగా దేనిపై దృష్టి పెడుతుంది?:
- User Goals and Expectations
- User Emotions
- Pain Points
- Touchpoints
- Overall Experience
- Opportunities for Improvement

### 3 · User Flow vs User Journey
తేడా ఏమిటి?

అంశం\tUser Flow\tUser Journey
అర్థం\tపని పూర్తి చేసే దశలు\tమొత్తం యూజర్ అనుభవం
ప్రధాన దృష్టి\tActions & Navigation\tExperience & Emotions
పరిధి\tఒక నిర్దిష్టమైన Task\tమొత్తం అనుభవం
చూపించేది\tScreens, Steps, Decisions\tStages, Goals, Pain Points
ఉపయోగం\tTask సులభతరం చేయడానికి\tమొత్తం అనుభవాన్ని మెరుగుపరచడానికి
ఉదాహరణ\tLogin ఎలా చేయాలి?\tయాప్ గురించి తెలుసుకున్నప్పటి నుంచి మళ్లీ ఉపయోగించే వరకు అనుభవం

### 4 · ఎప్పుడు ఉపయోగించాలి?
రెండింటినీ ఎప్పుడు ఉపయోగించాలి?

User Flow: ఒక Taskను యూజర్ సులభంగా పూర్తి చేయగలడా అని తెలుసుకోవడానికి.

{fig('vs-wireflow', 'User flow of screens for a first app launch, with a first-launch decision, onboarding, sign-up and home', 'User Flow – screens, actions, decision point (First launch?) మరియు alternative path.', 'User Flow: screens, actions, a decision point and an alternative path.')}

User Journey: యూజర్‌కు మొత్తం ప్రోడక్ట్ అనుభవం ఎలా ఉందో తెలుసుకోవడానికి.

{fig('vs-journey-map', 'Journey map grid with five stages and five layers: actions, goals, feelings, pain points, opportunities', 'User Journey Map – దశలు (Awareness → Loyalty) × actions, goals, feelings, pain points, opportunities.', 'Journey map: stages × actions, goals, feelings, pain points and opportunities.')}

### 5 · ఇంటర్వ్యూలో ఎలా చెప్పాలి?
Question: What is the difference between User Flow and User Journey?

మీరు ఇలా సింపుల్‌గా చెప్పవచ్చు:
“User Flow focuses on the steps a user takes to complete a specific task in a product. For example, logging into an app or making a payment.
User Journey focuses on the complete user experience, including their goals, expectations, emotions, and pain points across different stages.
In simple words, User Flow explains how users complete a task, while User Journey explains what users experience throughout their interaction with the product.”

Remember this:
- User Flow = How the user completes a task.
- User Journey = What the user experiences throughout the process.

ఈ రెండింటినీ కలిపి ఉపయోగించినప్పుడు యూజర్‌కు ఎదురయ్యే సమస్యలను గుర్తించి, మెరుగైన UX Design రూపొందించగలుగుతాము."""

Q1_EN = f"""User Flow and User Journey are both very important in UX design, but their purposes are different.
Put simply:
- User Flow: which steps does a user go through to complete a task?
- User Journey: what experience does the user have from start to finish while using a product?

### 1 · User Flow
What is a User Flow?

A User Flow is the sequence of steps a user follows to complete a specific task.
It shows where the user starts, which button they click, which screen they go to next and how they finally complete the task.

{fig('vs-login-flow', 'Login user flow', '', 'Example: user login in the Classic Rummy app – Open App → Login Screen → Enter Mobile Number → OTP Verification → Home Screen.')}

Here we show the steps a user follows to complete one specific task: login.

What does a User Flow mainly focus on?:
- Screen-to-screen navigation
- User actions
- Decision points
- Task completion
- Error and alternative paths

### 2 · User Journey
What is a User Journey?

A User Journey is the complete experience a user has while using a product or service.
It explains how the user learns about the product, why they want to use it, where they struggle, what they feel and whether they are finally satisfied.

{fig('vs-journey', 'User journey with five stages', '', 'Example: a new user’s experience in the Classic Rummy app.')}

Example – a new user’s experience in the Classic Rummy app:
1. Awareness: the user learns about the Classic Rummy app through an advertisement. (Positive) “This app looks good, I should try it once.”
2. Consideration: thinks about whether to download it; checks ratings and features. (Uncertain) “Is this a trustworthy app?”
3. Registration: opens the app and registers with a mobile number and OTP. (Possible friction) “Is registration easy?”
4. First Game: learns how to play and plays the first game. (Engaged) “Playing the game is interesting.”
5. Retention: with a good experience, the user opens the app again and plays. (Satisfied) “I should use this app again.”

What does a User Journey mainly focus on?:
- User goals and expectations
- User emotions
- Pain points
- Touchpoints
- Overall experience
- Opportunities for improvement

### 3 · User Flow vs User Journey
What is the difference?

Aspect\tUser Flow\tUser Journey
Meaning\tSteps to complete a task\tThe complete user experience
Main focus\tActions & navigation\tExperience & emotions
Scope\tOne specific task\tThe whole experience
Shows\tScreens, steps, decisions\tStages, goals, pain points
Used to\tMake a task easier\tImprove the overall experience
Example\tHow do I log in?\tThe experience from first hearing about the app to using it again

### 4 · When to use each
When should you use each?

User Flow: to check whether a user can complete a task easily.

{fig('vs-wireflow', 'User flow of screens for a first app launch', '', 'User Flow: screens, actions, a decision point (first launch?) and an alternative path.')}

User Journey: to understand how the user experiences the whole product.

{fig('vs-journey-map', 'Journey map grid', '', 'Journey map: stages (Awareness → Loyalty) × actions, goals, feelings, pain points and opportunities.')}

### 5 · How to answer in an interview
Question: What is the difference between User Flow and User Journey?

You can say it simply:
“User Flow focuses on the steps a user takes to complete a specific task in a product. For example, logging into an app or making a payment.
User Journey focuses on the complete user experience, including their goals, expectations, emotions, and pain points across different stages.
In simple words, User Flow explains how users complete a task, while User Journey explains what users experience throughout their interaction with the product.”

Remember this:
- User Flow = How the user completes a task.
- User Journey = What the user experiences throughout the process.

Using both together helps us find the problems users face and create a better UX design."""

Q2_TE = f"""కాదు, User Flow మరియు Task Flow రెండూ పూర్తిగా ఒకటే కావు. కానీ UX Designలో చాలా సందర్భాల్లో ఒకే అర్థంలో ఉపయోగిస్తారు. రెండింటి మధ్య చిన్న తేడా ఉంది.

### 1 · Task Flow
Task Flow అంటే ఏమిటి?

Task Flow అంటే యూజర్ ఒక నిర్దిష్టమైన పనిని పూర్తి చేయడానికి అనుసరించే దశలు.
ఇందులో సాధారణంగా ఒకే మార్గం (Single Path) ఉంటుంది. యూజర్‌కు ఎలాంటి ప్రత్యామ్నాయాలు లేదా నిర్ణయాలు అవసరం లేని సింపుల్ ప్రాసెస్‌ను చూపిస్తుంది.

{fig('vs-task-flow', 'Task flow: Open App, Enter Mobile Number, Enter OTP, Login Successful', 'ఉదాహరణ: Classic Rummy Appలో Login – ఇది ఒక Taskను పూర్తి చేసే సింపుల్ స్టెప్-బై-స్టెప్ ప్రాసెస్.', 'Example: login in the Classic Rummy app – a simple step-by-step process.')}

### 2 · User Flow
User Flow అంటే ఏమిటి?

User Flow అంటే యూజర్ ఒక Taskను పూర్తి చేసే సమయంలో వివిధ స్క్రీన్‌లు, Actions, Decision Points మరియు Alternative Paths ద్వారా ఎలా ప్రయాణిస్తాడో చూపిస్తుంది.
ఇందులో ఒకటి కంటే ఎక్కువ మార్గాలు ఉండవచ్చు.

{fig('vs-user-flow-branch', 'User flow with OTP decision: correct OTP leads to login success, wrong OTP shows an error and retry', 'ఉదాహరణ: Classic Rummy Appలో Login Flow – సరైన OTP ఇస్తే Login అవుతాడు; తప్పు OTP ఇస్తే Error Message చూపించి మళ్లీ ప్రయత్నించే అవకాశం ఇస్తుంది.', 'Example: login flow in the Classic Rummy app, with correct and wrong OTP paths.')}

ఇక్కడ యూజర్ సరైన OTP ఇస్తే Login అవుతాడు. తప్పు OTP ఇస్తే Error Message చూపించి మళ్లీ ప్రయత్నించే అవకాశం ఇస్తుంది.

### 3 · Task Flow vs User Flow
తేడా

అంశం\tTask Flow\tUser Flow
ఉద్దేశం\tఒక పనిని పూర్తి చేయడం\tయూజర్ చేసే మొత్తం ఇంటరాక్షన్‌ను చూపించడం
మార్గాలు\tసాధారణంగా ఒకే మార్గం\tMultiple Paths ఉండవచ్చు
Decision Points\tసాధారణంగా తక్కువ\tస్పష్టంగా చూపిస్తారు
Error Handling\tసాధారణంగా వివరించరు\tError & Alternative Paths చూపించవచ్చు
Complexity\tSimple\tSimple లేదా Complex

### 4 · ఒక సింపుల్ ఉదాహరణతో గుర్తుంచుకోండి
ATM ఉదాహరణ

ఒక ATMలో డబ్బులు విత్‌డ్రా చేయడం అనుకుందాం.
- Task Flow: ATM Card → PIN → Amount → Cash.
- User Flow: ATM Card → PIN Verification → PIN Correct or Incorrect → Select Withdrawal → Check Balance → Cash Available or Insufficient Balance → Cash Dispensed.

అంటే Task Flowలో ప్రధాన పని ఎలా పూర్తవుతుందో చూస్తాం. User Flowలో యూజర్ తీసుకునే నిర్ణయాలు, ఎదురయ్యే పరిస్థితులు, ప్రత్యామ్నాయ మార్గాలను కూడా చూస్తాం.

### 5 · ఇంటర్వ్యూలో ఎలా చెప్పాలి?
Question: What is the difference between Task Flow and User Flow?

“Task Flow represents the simple steps a user follows to complete a specific task, usually through a single path.
User Flow shows how users interact with the product, including different screens, actions, decision points, and alternative paths.
For example, a Task Flow shows the basic login steps, while a User Flow also covers scenarios like incorrect OTP, error messages, and retry options.”

ముఖ్యమైన విషయం: UX Designలో ఈ పదాల వినియోగం కంపెనీని బట్టి మారవచ్చు. కొన్ని టీమ్‌లు Task Flowను User Flowలోని ఒక సరళమైన రూపంగా పరిగణిస్తాయి. కాబట్టి ఇంటర్వ్యూలో ఈ తేడాను ఉదాహరణతో వివరించడం మంచిది."""

Q2_EN = f"""No, User Flow and Task Flow are not exactly the same, although in UX design they are often used with the same meaning. There is a small difference between them.

### 1 · Task Flow
What is a Task Flow?

A Task Flow is the set of steps a user follows to complete a specific task.
It usually has a single path. It shows a simple process in which the user needs no alternatives or decisions.

{fig('vs-task-flow', 'Task flow for login', '', 'Example: login in the Classic Rummy app – a simple step-by-step process to complete one task.')}

### 2 · User Flow
What is a User Flow?

A User Flow shows how a user moves through different screens, actions, decision points and alternative paths while completing a task.
It can have more than one path.

{fig('vs-user-flow-branch', 'User flow with OTP decision', '', 'Example: login flow in the Classic Rummy app.')}

Here, if the user enters the correct OTP they are logged in. If they enter a wrong OTP, an error message is shown with the option to try again.

### 3 · Task Flow vs User Flow
The difference

Aspect\tTask Flow\tUser Flow
Purpose\tComplete one task\tShow the user’s whole interaction
Paths\tUsually a single path\tCan have multiple paths
Decision points\tUsually few\tShown clearly
Error handling\tUsually not described\tCan show error & alternative paths
Complexity\tSimple\tSimple or complex

### 4 · Remember it with a simple example
ATM example

Imagine withdrawing money from an ATM.
- Task Flow: ATM Card → PIN → Amount → Cash.
- User Flow: ATM Card → PIN Verification → PIN Correct or Incorrect → Select Withdrawal → Check Balance → Cash Available or Insufficient Balance → Cash Dispensed.

So in a Task Flow we see how the main task gets done. In a User Flow we also see the decisions the user makes, the situations they face and the alternative paths.

### 5 · How to answer in an interview
Question: What is the difference between Task Flow and User Flow?

“Task Flow represents the simple steps a user follows to complete a specific task, usually through a single path.
User Flow shows how users interact with the product, including different screens, actions, decision points, and alternative paths.
For example, a Task Flow shows the basic login steps, while a User Flow also covers scenarios like incorrect OTP, error messages, and retry options.”

Important: how these terms are used can vary between companies. Some teams treat a Task Flow as a simpler form of a User Flow, so in an interview it’s good to explain the difference with an example."""

EX1_TE = """Classic Rummy ఉదాహరణలు:
- User Flow: Open App → Login Screen → Enter Mobile Number → OTP Verification → Home Screen (ఒక Task – Login).
- User Journey: Awareness → Consideration → Registration → First Game → Retention (మొత్తం అనుభవం – భావనలతో).

Remember this:
User Flow = How the user completes a task.
User Journey = What the user experiences throughout the process."""
EX1_EN = """Classic Rummy examples:
- User Flow: Open App → Login Screen → Enter Mobile Number → OTP Verification → Home Screen (one task – login).
- User Journey: Awareness → Consideration → Registration → First Game → Retention (the whole experience, with emotions).

Remember this:
User Flow = How the user completes a task.
User Journey = What the user experiences throughout the process."""
EX2_TE = """Classic Rummy Login:
- Task Flow: Open App → Enter Mobile Number → Enter OTP → Login Successful.
- User Flow: Open App → Login Screen → Enter Mobile Number → OTP Verification → Correct OTP (Login Success) / Wrong OTP (Show Error / Retry).

ATM:
- Task Flow: ATM Card → PIN → Amount → Cash.
- User Flow: PIN Correct or Incorrect, Cash Available or Insufficient Balance వంటి నిర్ణయాలతో."""
EX2_EN = """Classic Rummy login:
- Task Flow: Open App → Enter Mobile Number → Enter OTP → Login Successful.
- User Flow: Open App → Login Screen → Enter Mobile Number → OTP Verification → Correct OTP (Login Success) / Wrong OTP (Show Error / Retry).

ATM:
- Task Flow: ATM Card → PIN → Amount → Cash.
- User Flow: adds decisions such as PIN correct or incorrect, cash available or insufficient balance."""

import sys as _s; _s.path.insert(0, str(pathlib.Path(__file__).parent / 'vs')); import g0_roles as g0r
import g0_detail as g0d
import g0_hmw as g0h
import g0_loops as g0l
import g0_prd as g0p
import g0_exprd as g0x
import g0_uxas as g0u
def q(n, en, te, ate, aen, exte, exen):
    return {'questionId': f'vs-{n}', 'questionNumber': n, 'label': f'0.{n}', 'questionEnglish': en, 'questionTelugu': te,
            'answerTelugu': ate.strip(), 'answerEnglish': aen.strip(), 'exampleTelugu': exte, 'exampleEnglish': exen, 'importantMarkers': []}
parts = [{'partId': 'vs-0', 'partNumber': 0, 'title': 'Flows, journeys & roles', 'subtitle': 'Task Flow · User Flow · User Journey · PM vs PD vs UX vs UI · HMW · Funnels & Loops · PRD · PRD review · UX assumptions',
  'description': 'తరచుగా గందరగోళం చేసే UX పదాలు మరియు product team roles మధ్య తేడాలు – ఉదాహరణలతో. మూలం: Task Flow Vs User Journey PDF (0.1–0.2), PM vs PD vs UX vs UI Designer PDF (0.3), PM PD UX UI in-detail PDF (0.4), How Might We PDF (0.5), Loops PDF (0.6), PRD PDF (0.7), Example PRD PDF (0.8), UX Assumptions PDF (0.9).\n\nDifferences between often-confused UX terms and product-team roles, with examples. Sources: the Task Flow Vs User Journey PDF (0.1–0.2), the PM vs PD vs UX vs UI Designer PDF (0.3), the PM/PD/UX/UI in-detail PDF (0.4), the How Might We PDF (0.5), the Loops PDF (0.6), the PRD PDF (0.7), the Example PRD PDF (0.8) and the UX Assumptions PDF (0.9).',
  'questions': [
    q(1, 'What is the difference between User Flow and User Journey?', 'User Flow మరియు User Journey మధ్య తేడా ఏమిటి?', Q1_TE, Q1_EN, EX1_TE, EX1_EN),
    q(2, 'What is the difference between Task Flow and User Flow?', 'Task Flow మరియు User Flow ఒకటేనా? తేడా ఏమిటి?', Q2_TE, Q2_EN, EX2_TE, EX2_EN),
    q(3, g0r.Q_EN, g0r.Q_TE, g0r.TE, g0r.EN, g0r.EX_TE, g0r.EX_EN),
    q(4, g0d.Q_EN, g0d.Q_TE, g0d.TE, g0d.EN, g0d.EX_TE, g0d.EX_EN),
    q(5, g0h.Q_EN, g0h.Q_TE, g0h.TE, g0h.EN, g0h.EX_TE, g0h.EX_EN),
    q(6, g0l.Q_EN, g0l.Q_TE, g0l.TE, g0l.EN, g0l.EX_TE, g0l.EX_EN),
    q(7, g0p.Q_EN, g0p.Q_TE, g0p.TE, g0p.EN, g0p.EX_TE, g0p.EX_EN),
    q(8, g0x.Q_EN, g0x.Q_TE, g0x.TE, g0x.EN, g0x.EX_TE, g0x.EX_EN),
    q(9, g0u.Q_EN, g0u.Q_TE, g0u.TE, g0u.EN, g0u.EX_TE, g0u.EX_EN)],
  'revisionHeaders': ['Concept', 'Remember'],
  'revision': [{'cells': c} for c in [['User Flow', 'How the user completes a task – screens, actions, decisions, errors'], ['User Journey', 'What the user experiences – stages, goals, emotions, pain points'], ['Task Flow', 'Simple steps for one task – usually a single path']] + g0r.REVISION + g0d.REVISION + g0h.REVISION + g0l.REVISION + g0p.REVISION + g0x.REVISION + g0u.REVISION],
  'vocabulary': [], 'extras': [{'heading': g0r.QUIZ[0], 'body': g0r.QUIZ[1], 'full': True}, {'heading': g0d.QUIZ[0], 'body': g0d.QUIZ[1], 'full': True}, {'heading': g0h.EXERCISE[0], 'body': g0h.EXERCISE[1], 'full': True}, {'heading': g0x.MODEL[0], 'body': g0x.MODEL[1], 'full': True}, {'heading': g0u.MODEL[0], 'body': g0u.MODEL[1], 'full': True}]}]
import sys, re
sys.path.insert(0, str(pathlib.Path(__file__).parent / 'vs'))
import parse_pdf
GROUPS = [
 dict(n=1, title='UX Research & Discovery', sub='UX పరిశోధన మరియు కనుగొనడం', src='cmp_g1.txt', te='te_g1',
      desc='వినియోగదారులు, వారి ప్రవర్తన, సమస్యలు మరియు వ్యాపార అంచనాలను అర్థం చేసుకునే 15 పోలికలు.\n\n15 comparisons about understanding users, their behaviour, problems and business expectations.'),
 dict(n=2, title='UX Strategy & Design Thinking', sub='UX వ్యూహం మరియు డిజైన్ థింకింగ్', src='cmp_g2.txt', te='te_g2',
      desc=None),
 dict(n=3, title='Information Architecture & User Flows', sub='సమాచార నిర్మాణం మరియు User Flows', src='cmp_g3.txt', te='te_g3',
      desc=None),
 dict(n=4, title='UX Deliverables & Documentation', sub='UX డెలివరబుల్స్ మరియు డాక్యుమెంటేషన్', src='cmp_g4.txt', te='te_g4', desc=None),
 dict(n=5, title='Interaction Design & Prototyping', sub='ఇంటరాక్షన్ డిజైన్ మరియు ప్రోటోటైపింగ్', src='cmp_g5.txt', te='te_g5', desc=None),
 dict(n=6, title='Usability Testing & Evaluation', sub='Usability Testing మరియు మూల్యాంకనం', src='cmp_g6.txt', te='te_g6', desc=None),
 dict(n=7, title='UI Design & Design Systems', sub='UI డిజైన్ మరియు డిజైన్ సిస్టమ్స్', src='cmp_g7.txt', te='g7_items', desc=None),
 dict(n=8, title='Accessibility & Inclusive Design', sub='Accessibility మరియు Inclusive Design', src='cmp_g8.txt', te='g8_items', desc=None),
 dict(n=9, title='Product Design & Development', sub='Product Design మరియు Development', src='cmp_g9.txt', te='g9_items', desc=None),
 dict(n=10, title='UX Metrics & Analytics', sub='UX Metrics మరియు Analytics', src='cmp_g10.txt', te='g10_items', desc=None),
]
def vs_title(t):
    a, b = [x.strip() for x in re.split(r'\s+vs\s+', t, maxsplit=1)]
    return a, b
for g in GROUPS:
    modg = __import__(g['te'])
    if hasattr(modg, 'ITEMS'):
        items, TE = [], {}
        for d in modg.ITEMS:
            items.append({'n': d['n'], 'title': f"{d['A']} vs {d['B']}", 'te_text': parse_pdf.fix_te(d['te']), 'defs': d['defs'], 'hdr': d['hdr'], 'rows': d['rows'],
                          'exTitle': d['ex_title'], 'ex_text': d['ex_en'], 'iv_text': d['iv_en'], 'q_en': d.get('q_en'), 'kd_title': d.get('kd_title')})
            TE[d['n']] = {'q': d['q_te'], 'tbl': d['tbl_te'], 'ex': f"{d['ex_title']}:\n\n" + d['ex_te'], 'iv': d['iv_te']}
    else:
        items = parse_pdf.parse(str(pathlib.Path(__file__).parent / 'vs' / g['src']))
        TE = modg.T
    qs = []
    for it in items:
        n = it['n']; t = TE[n]; A, B = vs_title(it['title'])
        mod0 = __import__(g['te'])
        for old, new in getattr(mod0, 'TE_FIX', {}).get(n, []):
            assert old in it['te_text'], (n, old); it['te_text'] = it['te_text'].replace(old, new)
        for old, new in getattr(mod0, 'EX_FIX', {}).get(n, []):
            assert old in it['ex_text'], (n, old); it['ex_text'] = it['ex_text'].replace(old, new)
        if n in getattr(mod0, 'EX_EN', {}): it['ex_text'] = mod0.EX_EN[n]
        if n in getattr(mod0, 'ROWS_EN', {}): it['rows'] = mod0.ROWS_EN[n]
        tbl_te = '\n'.join(['\t'.join(it['hdr'])] + ['\t'.join(r) for r in t['tbl']])
        tbl_en = '\n'.join(['\t'.join(it['hdr'])] + ['\t'.join(r) for r in it['rows']])
        kd = it.get('kd_title') or f'{A} vs {B}'
        te = (it['te_text'] + f'\n\n### తేడాలు · Key Differences\n{kd}\n\n' + tbl_te +
              '\n\n### ఇంటర్వ్యూలో ఇలా చెప్పండి · Interview Answer\nEnglish లో చెప్పాల్సిన సమాధానం\n\n' + it['iv_text'] +
              '\n\nతెలుగు అర్థం: ' + t['iv'])
        en = ('English Definitions:\n' + '\n'.join('- ' + d for d in it['defs']) +
              f'\n\n### Key Differences\n{kd}\n\n' + tbl_en +
              '\n\n### Interview Answer\nHow to say it in an interview\n\n' + it['iv_text'])
        ex_en = f"Practical Example – {it['exTitle']}:\n\n" + it['ex_text']
        qs.append({'questionId': f"vs-g{g['n']}-{n}", 'questionNumber': n,
                   'questionEnglish': it.get('q_en') or f'What is the difference between {A} and {B}?', 'questionTelugu': t['q'],
                   'answerTelugu': te, 'answerEnglish': en, 'exampleTelugu': t['ex'], 'exampleEnglish': ex_en, 'importantMarkers': []})
    rev = [l for l in open(pathlib.Path(__file__).parent / 'vs' / g['src']).read().split('\n')]
    i0 = next((i for i, l in enumerate(rev) if 'Quick Revision' in l), len(rev))
    rows = [{'cells': [f'Q{k} {a}', r]} for k, a, r in getattr(__import__(g['te']), 'REVISION', [])]
    for l in (rev[i0:] if not rows else []):
        m = re.match(r'^\s*(\d+)\s{2,}(.+?)\s{2,}(.+)$', l)
        if m and qs[0]['questionNumber'] <= int(m.group(1)) <= qs[-1]['questionNumber']: rows.append({'cells': [f"Q{m.group(1)} {m.group(2).strip()}", m.group(3).strip()]})
        if l.strip().startswith(('Complete learning', 'Practical UX Exercise', 'Group ' + str(g['n']) + ' – Interview Practice')): break
    mod = __import__(g['te'])
    desc = g['desc'] or (getattr(mod, 'INTRO_TE', '') + '\n\n' + f"{len(qs)} comparisons · Q{qs[0]['questionNumber']}–Q{qs[-1]['questionNumber']}.")
    extras = []
    if getattr(mod, 'PRACTICE_BODY', None):
        extras.append({'heading': mod.PRACTICE_TITLE, 'body': mod.PRACTICE_BODY, 'full': True})
    for h, body in getattr(mod, 'EXTRAS', []):
        extras.append({'heading': h, 'body': body, 'full': True})
    if getattr(mod, 'PRACTICE', None):
        extras.append({'heading': f"Group {g['n']} – Interview Practice · ఇంటర్వ్యూ సాధన",
                       'body': 'ఈ ప్రశ్నలకు మీ సొంత మాటల్లో English లో సమాధానం చెప్పి practice చేయండి. (Try answering these in your own words.)\n\n' + '\n'.join(f'{i+1}. {x}' for i, x in enumerate(mod.PRACTICE)),
                       'full': True})
    parts.append({'partId': f"vs-{g['n']}", 'partNumber': g['n'], 'title': g['title'], 'subtitle': g['sub'], 'description': desc,
                  'questions': qs, 'revisionHeaders': ['Comparison', 'Remember · గుర్తుంచుకోండి'], 'revision': rows, 'vocabulary': [], 'extras': extras})
(ROOT / 'data/vs.js').write_text('/* Vs tab – from Task_Flow_Vs_User_Journey.pdf. Telugu first, English behind the button. */\nwindow.BOOK_VS_PARTS = ' + json.dumps(parts, ensure_ascii=False, indent=1) + ';\n')
(ROOT / 'data/raw/vs.json').write_text(json.dumps(parts, ensure_ascii=False, indent=1))
print('ok')
