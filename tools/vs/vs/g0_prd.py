# Group 0 · 0.7 – How a Product Manager writes a PRD (Product Requirements Document) – complete guide with the Simplified Checkout example.
# Source: PRD.pdf (Telugu-first). Telugu answer = PDF text (prd_te.txt, converted by conv_prd.py; the user-flow ASCII art, wrapped table rows,
# formula, 10-step workflow and tools list were rebuilt). English answer = English text kept from the PDF plus Claude's translation of the
# Telugu lines (prd_en_map.py → make_prd_en.py → prd_en.txt). Diagrams = Claude's own drawings (figs_g0.py); the PDF's images come from other sites.
import pathlib
HERE = pathlib.Path(__file__).parent
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'
FIGS = {
 '@@FIG1': ('vs-prd-docs', 'Three coloured cards: PRD – what and why (Product Manager); Design Specification – how the experience works (designers); Technical Specification – how it is implemented (engineering)',
            'PRD, Design Specification, Technical Specification – మూడు documents, మూడు ప్రశ్నలు.', 'PRD, Design Specification and Technical Specification – three documents, three questions.'),
 '@@FIG2': ('vs-prd-structure', 'Twenty numbered PRD sections in five coloured columns: Why, Who & goals, What, How it behaves, Done & launch',
            'ఒక Feature PRD లోని 20 విభాగాలు – ఐదు భాగాలుగా.', 'The 20 sections of a feature PRD, grouped into five parts.'),
 '@@FIG3': ('vs-checkout-flow', 'Vertical checkout flow from Cart to Order Confirmation, with a payment-failed branch that loops back to payment method selection',
            'Simplified checkout user flow – Payment failed అయితే retry / వేరే method.', 'Simplified checkout user flow – if payment fails, retry or choose another method.'),
 '@@FIG4': ('vs-prd-workflow', "Ten coloured step cards for the PM's PRD workflow, from understanding the business request to monitoring after launch",
            "PM's PRD writing workflow – 10 దశలు.", "The PM's PRD writing workflow – 10 steps."),
}
def _load(name, lang):
    t = (HERE / name).read_text().strip()
    for k, (src, alt, te, en) in FIGS.items():
        t = t.replace(k, fig(src, alt, te if lang == 'te' else '', en))
    return t

Q_EN = 'How does a Product Manager write a PRD (Product Requirements Document)?'
Q_TE = 'ఒక Product Manager PRD (Product Requirements Document) ను ఎలా రాస్తారు?'
TE = _load('prd_te.txt', 'te')
EN = _load('prd_en.txt', 'en')

EX_TE = """Simplified Checkout – Food Delivery App PRD:
- Problem: Delivery charges స్పష్టంగా లేవు, address ఎంచుకోవడం గందరగోళం, payment క్లిష్టం → order abandonment.
- Goal: Checkout completion rate పెంచడం (ఉదా: launch తర్వాత 8 వారాల్లో 10% – target example మాత్రమే).
- Scope: Saved addresses, price breakdown, payment selection, confirmation · Out: loyalty, subscriptions, AI recommendations.
- FR-04: The system shall display item price, taxes and delivery charges.
- Acceptance: Given saved addresses exist, when checkout opens, then the saved addresses are displayed.

PRD = What & Why · Design Spec = How it works · Tech Spec = How it's built"""
EX_EN = """Simplified Checkout – Food Delivery App PRD:
- Problem: unclear delivery charges, confusing address selection, complicated payment → order abandonment.
- Goal: improve checkout completion rate (e.g. 10% within 8 weeks of launch – a target example only).
- Scope: saved addresses, price breakdown, payment selection, confirmation · Out: loyalty, subscriptions, AI recommendations.
- FR-04: The system shall display item price, taxes and delivery charges.
- Acceptance: Given saved addresses exist, when checkout opens, then the saved addresses are displayed.

PRD = What & Why · Design Spec = How it works · Tech Spec = How it's built"""

REVISION = [['PRD', 'What needs to be built and why – problem, goals, scope, requirements, metrics (PM owns, team contributes)'],
            ['Functional Req. vs Acceptance Criteria', 'What to build vs how to test it works (Given–When–Then)'],
            ['PRD vs BRD vs FRD vs SRS', 'Product requirements vs business needs vs detailed functions vs software system specs']]
