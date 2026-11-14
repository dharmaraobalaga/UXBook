# Group 0 · 0.9 – UX Assumption Questions: user & behaviour, usability & design, value & business, feasibility & edge cases – with Classic Rummy examples.
# Source: UX_Assumptions.pdf (Telugu-first, with the PDF's own English explanations). Telugu answer = PDF text (uxas_te.txt, converted by conv_uxas.py;
# flow, team mapping, risk matrix, research steps and process rebuilt). English answer = the PDF's English explanations and examples plus Claude's
# translation of the other Telugu lines (uxas_en_map.py → make_uxas_en.py → uxas_en.txt). Diagrams and the exercise model answer = Claude.
import pathlib
HERE = pathlib.Path(__file__).parent
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'
FIGS = {
 '@@FIG1': ('vs-assumption-types', 'Four coloured columns of assumption types: User & Behaviour (identity, motivation, habits, context), Usability & Design (mental models, friction, accessibility), Value & Business (desirability, outcomes, priority), Feasibility & Edge cases (data & content, failure states)',
            'నాలుగు రకాల UX Assumptions – ప్రతి రకానికి దాని ప్రశ్నలు.', 'Four kinds of UX assumption – each with its own questions.'),
 '@@FIG2': ('vs-assumption-matrix', 'Two-by-two matrix of importance against evidence: validate immediately, monitor and act, validate later, no immediate action, with Classic Rummy examples',
            'Importance vs Evidence – High Importance + Low Evidence = Highest Risk.', 'Importance vs evidence – high importance with low evidence is the highest risk.'),
 '@@FIG3': ('vs-assumption-research', 'Six coloured steps from an assumption to a research question, interview question, usability task, observation and design decision',
            'Assumption నుంచి Design Decision వరకు – 6 దశలు.', 'From assumption to design decision – six steps.'),
}
def _load(name, lang):
    t = (HERE / name).read_text().strip()
    if lang == 'en': t = t.replace('English Explanation:', 'Explanation:')
    for k, (src, alt, te, en) in FIGS.items():
        t = t.replace(k, fig(src, alt, te if lang == 'te' else '', en))
    return t

Q_EN = 'What are UX assumption questions, and how do you use them before designing? (Classic Rummy examples)'
Q_TE = 'UX Assumption Questions అంటే ఏమిటి? Design ప్రారంభించే ముందు వాటిని ఎలా ఉపయోగించాలి? (Classic Rummy ఉదాహరణలతో)'
TE = _load('uxas_te.txt', 'te')
EN = _load('uxas_en.txt', 'en')

EX_TE = """Classic Rummy – "కొత్త ప్లేయర్లకు Rules తెలియవు, అందుకే Tutorial అవసరం" అనేది Fact కాదు, Assumption:
- Identity: ఈ users నిజంగా Rummy కి కొత్తవారా, లేక card games తెలిసినవారా?
- Friction: ఏ step లో ఎక్కువ drop-off?
- Desirability: Users నిజంగా tutorial కోరుకుంటున్నారా, లేక ఆడుతూ నేర్చుకోవాలనుకుంటున్నారా?
- Failure states: Tutorial మధ్యలో exit / network loss అయితే?
- Risk: High importance + low evidence → ముందుగా research తో validate చేయాలి.

Leading question కాదు: "What was difficult when you first played Rummy?\""""
EX_EN = """Classic Rummy – "new players don't know the rules, so they need a tutorial" is an assumption, not a fact:
- Identity: are these users really new to Rummy, or experienced card-game players?
- Friction: which step has the highest drop-off?
- Desirability: do users actually want a tutorial, or prefer learning by playing?
- Failure states: what if they exit the tutorial midway or lose the network?
- Risk: high importance + low evidence → validate with research first.

Not a leading question: "What was difficult when you first played Rummy?\""""

REVISION = [['UX assumption types', 'User & behaviour · Usability & design · Value & business · Feasibility & edge cases'],
            ['Assumption risk', 'High importance + low evidence = highest risk – validate first; avoid leading questions']]

MODEL = ('UX assumptions exercise · 0.9 – model answer', """Task: convert each assumption into a research (validation) question. ముందుగా మీ సమాధానాలు రాసి, తర్వాత ఈ నమూనాతో పోల్చండి. (Model answer written by Claude.)

Assumption\tResearch question\tHow to validate
New users don't understand Rummy rules.\tWhat do first-time players find hardest when they start their first Rummy game?\tInterviews + usability test: ask new players to arrange cards into valid sets
Users prefer interactive tutorials over videos.\tHow do new players prefer to learn a new card game, and which format helps them start playing sooner?\tCompare a clickable prototype with a short video in testing; check time to first game
A shorter onboarding flow will improve activation.\tHow does the length of onboarding affect whether new players start their first game?\tFunnel data on current drop-off; A/B test a short vs full flow
Users understand card arrangement icons.\tCan first-time players tell what each card-arrangement icon does without a label?\tFirst-click / icon recognition test with new players
Users will return to the tutorial when needed.\tWhen new players get stuck mid-game, where do they look for help?\tObserve gameplay sessions; track help and tutorial re-entry events

Why this works: each question is neutral (not leading), focuses on behaviour, and points to a method – and each finding leads to a design decision (full tutorial, in-game hints, or a simpler first game).

తెలుగు సారాంశం: ప్రతి Assumption ను neutral research question గా మార్చి, దానిని ఎలా validate చేయాలో (interview, usability test, funnel data, A/B test, observation) నిర్ణయించి, ఫలితాల ఆధారంగా design decision తీసుకోవాలి.""")
