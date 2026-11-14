# Group 0 · 0.4 – PM vs PD vs UX vs UI: detailed explanation.
# Source: PM_PD_UX_UI_indetail_explanation.pdf (Telugu-first). Telugu answer = PDF text (detail_te.txt, converted by conv_detail.py;
# the 10-phase table was rebuilt and the 4-scenario quiz moved to the review page). English answer = Claude's translation (detail_en.txt).
# Diagrams = Claude's own drawings (figs_g0.py); the PDF's ~20 images come from dribbble, medium, behance etc. and are not copied.
import pathlib
HERE = pathlib.Path(__file__).parent
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

FIGS = {
 '@@FIG1': ('vs-roles-formula', 'Four coloured rows: PM = what to build + why + what to prioritise; PD = problem solving + UX + UI + product thinking; UX = research + understanding + usability + interaction design; UI = visual design + layout + typography + colour + components',
            'ప్రతి పాత్ర ఒక్క వాక్యంలో – guide లోని సరళమైన formulas.', 'Each role in one line – the simple formulas from the guide.'),
 '@@FIG2': ('vs-food-journey', 'Food delivery journey: Discover, Explore, Select, Checkout, Track, Receive, each with a user action and a pain point',
            'Food delivery app user journey – ప్రతి దశ, user చర్య, సాధ్యమైన pain point.', 'Food delivery user journey – each stage, the user action and a possible pain point.'),
 '@@FIG3': ('vs-design-process-10', 'Ten numbered phases: Discover, Define, Ideate, Structure, Design, Visual Design, Prototype, Validate, Develop, Measure',
            'Product design project లోని 10 దశలు – Discover నుంచి Measure వరకు.', 'The 10 phases of a product design project – from Discover to Measure.'),
}
def _load(name, lang):
    t = (HERE / name).read_text().strip()
    for k, (src, alt, te, en) in FIGS.items():
        t = t.replace(k, fig(src, alt, te if lang == 'te' else '', en))
    return t

Q_EN = 'Explain the roles of Product Manager, Product Designer, UX Designer and UI Designer in detail.'
Q_TE = 'Product Manager, Product Designer, UX Designer, UI Designer పాత్రలను వివరంగా తెలపండి.'
TE = _load('detail_te.txt', 'te')
EN = _load('detail_en.txt', 'en')

EX_TE = """Food delivery app – Checkout సమస్య: 40% మంది కస్టమర్లు పేమెంట్‌కు ముందే వెళ్లిపోతున్నారు.
- PM: Analytics, feedback పరిశీలించి checkout ను ప్రాధాన్యతగా నిర్ణయిస్తారు; లక్ష్యం పెట్టి ఫలితాలు కొలుస్తారు.
- Product Designer: Address selection సులభం, delivery charges ముందుగానే, స్పష్టమైన order summary, తక్కువ steps.
- UX Designer: Interviews → checkout journey విశ్లేషణ → pain points → user flow → wireframes → prototype → usability testing.
- UI Designer: Brand colours, typography, button styles, price hierarchy, error/success states.

Formulas:
PM = What + Why + Prioritise · PD = Problem Solving + UX + UI + Product Thinking · UX = Research + Usability + Interaction · UI = Visual + Layout + Typography + Colour + Components"""
EX_EN = """Food delivery app – checkout problem: 40% of customers leave before payment.
- PM: Reviews analytics and feedback, makes checkout the priority, sets a target and measures results.
- Product Designer: Easier address selection, delivery charges up front, a clear order summary, fewer steps.
- UX Designer: Interviews → checkout journey analysis → pain points → user flow → wireframes → prototype → usability testing.
- UI Designer: Brand colours, typography, button styles, price hierarchy, error/success states.

Formulas:
PM = What + Why + Prioritise · PD = Problem Solving + UX + UI + Product Thinking · UX = Research + Usability + Interaction · UI = Visual + Layout + Typography + Colour + Components"""

REVISION = [['Product design process', 'Discover → Define → Ideate → Structure → Design → Visual → Prototype → Validate → Develop → Measure']]

QUIZ = ('Practical role-based assessment · 0.4 – 4 scenarios', """ఈ చిన్న practical exercise ఒక Senior Product Designer interview‌లో కూడా ఉపయోగపడుతుంది.

1. A company wants to increase food orders by 20%. Who primarily defines the business target and product priorities? (Product Manager / UX Designer / UI Designer)
2. Users are unable to find the checkout button. Who investigates the user flow and usability problem? (Product Manager / UX Designer / Marketing Manager)
3. The checkout screen has poor typography, inconsistent buttons and weak colour contrast. Who primarily addresses the visual design? (Product Manager / UI Designer / Business Analyst)
4. You need to redesign the complete first-time user experience, from onboarding to placing an order. Which role has the broader design responsibility? (Product Designer / Only UI Designer / Only Product Manager)

### Answer key · జవాబులు
1. Product Manager · 2. UX Designer · 3. UI Designer · 4. Product Designer""")
