# Group 0 · 0.5 – Assumptions, Questions, Hypothesis and How Might We (HMW) – by role.
# Source: How_might_we.pdf (Telugu-first). Telugu answer = PDF text (hmw_te.txt, converted by conv_hmw.py; sections 6 and 9 rebuilt from the
# PDF's card layout). English answer = Claude's translation (hmw_en.txt). Diagrams = Claude's own drawings (figs_g0.py) – the PDF's images
# come from other sites and are not copied. The sample answer to the practical exercise was written by Claude.
import pathlib
HERE = pathlib.Path(__file__).parent
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'
FIGS = {
 '@@FIG1': ('vs-hmw-terms', 'Five coloured rows: Assumption, Question, Hypothesis, Problem Statement and How Might We, each with a checkout example',
            'ఐదు పదాలు – ఐదు ఉద్దేశాలు, checkout ఉదాహరణతో.', 'Five words, five purposes – with a checkout example.'),
 '@@FIG2': ('vs-hmw-four-lenses', 'One common problem – customers abandon orders at checkout – branching into four coloured HMW cards for PM, PD, UX and UI',
            'ఒకే సమస్య – PM, PD, UX, UI నాలుగు కోణాల్లో HMW ప్రశ్నలు.', 'One problem, four HMW questions – PM, PD, UX and UI lenses.'),
 '@@FIG3': ('vs-hmw-process', 'Six coloured steps: Discover, Define, How Might We (highlighted), Ideate, Prototype, Test, with an iteration loop',
            'Design process లో HMW – Define తర్వాత, Ideate ముందు; దశలు మళ్లీ మళ్లీ రావచ్చు.', 'HMW sits after Define and before Ideate – and the stages repeat.'),
}
def _load(name, lang):
    t = (HERE / name).read_text().strip()
    for k, (src, alt, te, en) in FIGS.items():
        t = t.replace(k, fig(src, alt, te if lang == 'te' else '', en))
    return t

Q_EN = 'What are Assumptions, Hypotheses and How Might We (HMW) questions, and how do PM, PD, UX and UI use them?'
Q_TE = 'Assumptions, Hypothesis, How Might We (HMW) ప్రశ్నలు అంటే ఏమిటి? PM, PD, UX, UI వాటిని ఎక్కడ, ఎందుకు ఉపయోగిస్తారు?'
TE = _load('hmw_te.txt', 'te')
EN = _load('hmw_en.txt', 'en')

EX_TE = """ఒకే సమస్య – కస్టమర్లు checkout దశలో ఆర్డర్ వదిలేస్తున్నారు:
- Assumption: Steps ఎక్కువగా ఉన్నందువల్ల users వెళ్లిపోతున్నారు.
- Question: Users checkout ను ఎందుకు వదిలేస్తున్నారు?
- Hypothesis: Steps తగ్గిస్తే ఎక్కువ మంది orders పూర్తి చేయవచ్చు.
- Problem Statement: Process గందరగోళంగా ఉంది, చివరి ధర స్పష్టంగా లేదు.
- HMW: How might we make checkout simpler and more transparent?

HMW Formula: How might we + User + Desired Outcome + Context?"""
EX_EN = """One problem – customers abandon orders at checkout:
- Assumption: Users leave because there are too many steps.
- Question: Why are users abandoning checkout?
- Hypothesis: If we reduce steps, more users may complete orders.
- Problem Statement: The process is confusing and the final price is unclear.
- HMW: How might we make checkout simpler and more transparent?

HMW Formula: How might we + User + Desired Outcome + Context?"""

REVISION = [['Assumption', 'What we believe but have not proven'], ['Hypothesis', 'A testable prediction: if we change X, Y may happen'],
            ['How Might We', 'Turns a problem into an open opportunity – no solution decided in advance']]

EXERCISE = ('Practical exercise · 0.5 – a sample answer', """Scenario: ఒక Food Delivery Appలో కొత్త యూజర్లు యాప్‌ను డౌన్‌లోడ్ చేస్తున్నారు, కానీ చాలామంది మొదటి ఆర్డర్ చేయకుండానే వదిలేస్తున్నారు.

ముందుగా మీ సొంత సమాధానం రాసి, తర్వాత ఈ నమూనాతో పోల్చండి. (Sample answer written by Claude – one good way to answer, not the only one.)

1. Role: Product Designer – activation is a whole first-time experience problem (onboarding, discovery, trust, checkout), not one screen.
2. Assumption: New users don't see enough value or trust before their first order – e.g. they can't quickly find suitable restaurants near them, or they're unsure about total cost and delivery time.
3. HMW: How might we help first-time users find a restaurant they trust and place their first order with confidence?
4. Why: It names the user (first-time users), the outcome (first order) and the barrier (trust and discovery), and it leaves room for many solutions – better onboarding, location-based suggestions, clear pricing up front, first-order offers. Before designing, I'd validate the assumption with funnel analytics (where do new users drop?) and a few user interviews.

తెలుగు సారాంశం: Role – Product Designer; Assumption – కొత్త users కు మొదటి ఆర్డర్ ముందు తగిన విలువ, నమ్మకం కనిపించడం లేదు; HMW – మొదటిసారి users నమ్మకమైన restaurant కనుగొని నమ్మకంగా మొదటి ఆర్డర్ చేసేలా ఎలా చేయగలం? Design ముందు analytics, interviews తో assumption ను validate చేయాలి.""")
