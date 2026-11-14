# Group 0 · 0.6 – Funnels, Loops and other product frameworks (AARRR, HEART, JTBD, Double Diamond, RICE …) – where they fit and who uses them.
# Source: Loops.pdf (Telugu-first). Telugu answer = PDF text (loops_te.txt, converted by conv_loops.py; the section-1 cards, the referral-loop
# steps, the formulas, the RICE example, the 8-step example and the PM/PD/UX/UI table were rebuilt from the PDF's layout).
# English answer = Claude's translation (loops_en.txt). Diagrams = Claude's own drawings (figs_g0.py); the PDF's images come from other sites.
import pathlib
HERE = pathlib.Path(__file__).parent
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'
FIGS = {
 '@@FIG1': ('vs-frameworks-map', 'Five coloured bands: Product Strategy (PM), Discovery & Research (PM + PD + UX), Experience Design (PD + UX), Interface Design (PD + UI), Measurement & Growth (PM + PD + Analytics), each listing its frameworks',
            'ఏ Framework ఏ విభాగానికి చెందుతుంది – ఐదు విభాగాలు, ఎవరు ప్రధానంగా పనిచేస్తారు.', 'Where each framework belongs – five areas and who mainly works there.'),
 '@@FIG2': ('vs-food-funnel', 'Funnel of five coloured bars narrowing from 10,000 app opens to 2,000 completed payments',
            'Food ordering conversion funnel – ఉదాహరణ సంఖ్యలు మాత్రమే.', 'Food ordering conversion funnel – illustrative numbers only.'),
 '@@FIG3': ('vs-referral-loop', 'Six coloured steps arranged in a circle around the word Loop: existing user, referral link, new user, first order, reward, more referrals',
            'Referral loop – ఒక cycle ఫలితం తదుపరి cycle ను ప్రారంభిస్తుంది.', 'Referral loop – the result of one cycle starts the next.'),
 '@@FIG4': ('vs-double-diamond', 'Two diamonds: Discover and Define in the problem space, Develop and Deliver in the solution space, with HMW between them',
            'Double Diamond – Problem space, Solution space; మధ్యలో HMW.', 'Double Diamond – problem space, then solution space, with HMW in between.'),
 '@@FIG5': ('vs-e2e-8steps', 'Eight coloured cards from Product Strategy to Launch & Measurement, each with the roles involved',
            'End-to-end product discovery & design – 8 దశలు, ఎవరు పాల్గొంటారు.', 'End-to-end product discovery and design – 8 stages and who is involved.'),
}
def _load(name, lang):
    t = (HERE / name).read_text().strip()
    for k, (src, alt, te, en) in FIGS.items():
        t = t.replace(k, fig(src, alt, te if lang == 'te' else '', en))
    return t

Q_EN = 'Where do Funnels, Loops and other frameworks (AARRR, HEART, JTBD, Double Diamond, RICE) fit in Product Design?'
Q_TE = 'Product Designలో Funnels, Loops మరియు ఇతర Frameworks (AARRR, HEART, JTBD, Double Diamond, RICE) ఎక్కడ వస్తాయి?'
TE = _load('loops_te.txt', 'te')
EN = _load('loops_en.txt', 'en')

EX_TE = """Food delivery app – ఒకే సమస్య, అనేక frameworks:
- Funnel: App Open 10,000 → Payment 2,000 = 20% conversion; ఎక్కడ drop-off ఉందో చూపిస్తుంది.
- Loop: Existing user → Referral → New user → First order → Reward → More referrals – మళ్లీ మొదలవుతుంది.
- AARRR: Acquisition → Activation → Retention → Referral → Revenue.
- HEART: Happiness, Engagement, Adoption, Retention, Task Success – UX నాణ్యత కొలవడానికి.
- JTBD: "త్వరగా, నమ్మకంగా భోజనం పొందాలి" – user పూర్తి చేయాలనుకునే పని.

Remember: Funnel = ఎక్కడ వదిలేస్తున్నారు? · Loop = మళ్లీ ఎందుకు వస్తున్నారు?"""
EX_EN = """Food delivery app – one problem, many frameworks:
- Funnel: App Open 10,000 → Payment 2,000 = 20% conversion; shows where the drop-off is.
- Loop: Existing user → Referral → New user → First order → Reward → More referrals – and round again.
- AARRR: Acquisition → Activation → Retention → Referral → Revenue.
- HEART: Happiness, Engagement, Adoption, Retention, Task Success – to measure UX quality.
- JTBD: "get a reliable meal quickly" – the job the user wants done.

Remember: Funnel = where do users leave? · Loop = why do they come back?"""

REVISION = [['Funnel vs Loop', 'Funnel shows where users drop off; a loop shows how one cycle feeds the next (growth, engagement)'],
            ['AARRR vs HEART', 'AARRR = growth stages (PM); HEART = UX quality measures (PD/UX)'],
            ['JTBD · Double Diamond · RICE', 'The job users want done · Discover–Define–Develop–Deliver · (Reach × Impact × Confidence) ÷ Effort']]
