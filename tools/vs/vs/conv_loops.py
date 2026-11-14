import re, sys
sys.path.insert(0, '.')
from parse_pdf import fix_te, blocks
TOP = ['Product Developmentలో', 'Funnel', 'Loop –', 'Productలో ముఖ్యమైన', 'AARRR', 'HEART', 'JTBD', 'Double Diamond', 'Design Thinking',
       'Prioritisation', 'Product Metrics', 'ఈ Frameworksలో', 'Complete Product', 'ఏ Concept', 'నీ కోసం', 'Recommended Reading']
SHORT = {'1': '1 · Product Development లో స్థానం', '2': '2 · Funnel', '3': '3 · Loop', '4': '4 · Loop రకాలు', '5': '5 · AARRR – Pirate Metrics',
         '6': '6 · HEART Framework', '7': '7 · JTBD – Jobs To Be Done', '8': '8 · Double Diamond', '9': '9 · Design Thinking',
         '10': '10 · Prioritisation Frameworks', '11': '11 · Product Metrics', '12': '12 · ఎవరు ఏ Framework ఉపయోగిస్తారు?',
         '13': '13 · Complete Example – ఒకే project లో', '14': '14 · Quick Reference', '15': '15 · Learning Priority', '16': '16 · Reading & References'}
raw = open('loops.txt').read().split('\n')
out = []; top = 0; i = 0
while i < len(raw):
    r = raw[i]; s = r.strip(); i += 1
    if s == 'ChatGPT said:' or re.fullmatch(r'[a-z0-9.…-]+\.(?:com|co|net|io|org|edu|pm|so|au|com\.au)(?: \+\d)?', s) or re.fullmatch(r'\d{1,2}', s): continue
    if re.fullmatch(r'(Amplitude|odr\.chalmer…|[a-z.]+…) \+\d', s): continue
    if i < 4 and s.startswith('Product Designలో Loops'): continue
    m = re.match(r'^(\d+)\. (.*)$', s)
    if top < len(TOP) and m and int(m.group(1)) == top + 1 and m.group(2).startswith(TOP[top]) and len(r) - len(r.lstrip()) == 0:
        top += 1; n = m.group(1)
        out += ['', f'@@H {SHORT[n]}\n{m.group(2)}', '']; continue
    if re.match(r'^[A-F]\. ', s) and len(r) - len(r.lstrip()) == 0:
        out += ['', s.rstrip(':') + ':', '']; continue
    out.append(r)
t = fix_te(blocks(out, tables=True))
t = re.sub(r'@@H ([^\n]*)', r'### \1', t)
open('/tmp/loops_te.txt', 'w').write(t); print(len(t), top)

import json
t = open('/tmp/loops_te.txt').read()
def rep(a, b):
    global t
    assert a in t, a[:80]; t = t.replace(a, b, 1)
def between(a, b, new):
    global t
    i = t.index(a); j = t.index(b, i); t = t[:i] + new + t[j:]
# section 1 – five areas
between('- A. Product Strategy – PM', 'ఇప్పుడు Funnels, Loops', '''@@FIG1

A. Product Strategy – PM: ఏం నిర్మించాలి? ఎందుకు? ఏది ముందు చేయాలి?
- Product Vision · Roadmap · North Star Metric · RICE · MoSCoW · AARRR

B. Discovery & Research – PM + PD + UX: యూజర్ల సమస్యలు, అవసరాలు ఏమిటి?
- Design Thinking · Double Diamond · JTBD · Personas · Assumptions · HMW

C. Experience Design – PD + UX: యూజర్ ప్రొడక్ట్‌లో ఎలా ప్రయాణిస్తాడు?
- User Journey · User Flow · Task Flow · Information Architecture · Wireframes · Prototypes

D. Interface Design – PD + UI: ప్రొడక్ట్ ఎలా కనిపించాలి, ఎలా స్పందించాలి?
- Visual Hierarchy · Design Systems · Components · Responsive Design · Accessibility

E. Measurement & Growth – PM + PD + Analytics: యూజర్లు ఎలా ఉపయోగిస్తున్నారు? ప్రొడక్ట్ విజయవంతమైందా?
- Funnels · Loops · HEART · AARRR · Retention · Cohort Analysis · Experiments

''')
rep('Food Ordering Conversion Funnel\n\n', '@@FIG2\n\nFood Ordering Conversion Funnel:\n\n')
rep('Stage	1', 'Stage	1') if 'Stage\t1' in t else None
rep('మొత్తం Conversion Rate:\n\n- 2000\n- × 100 = 20%\n- 10000\n- ​\n', 'మొత్తం Conversion Rate:\n\nConversion Rate = (2,000 ÷ 10,000) × 100 = 20%\n')
between('- 1 Existing User', 'ఈ ప్రక్రియలో కొత్త యూజర్లు', '''@@FIG3

1. Existing User – యాప్‌ను ఉపయోగిస్తున్న కస్టమర్
2. Referral – స్నేహితుడికి యాప్ లింక్ పంపుతాడు
3. New User – స్నేహితుడు యాప్‌ను డౌన్‌లోడ్ చేస్తాడు
4. First Order – కొత్త కస్టమర్ మొదటి ఆర్డర్ చేస్తాడు
5. Reward – Referral Reward లభిస్తుంది
6. More Referrals – కొత్త కస్టమర్ కూడా మరొకరికి యాప్‌ను సూచించవచ్చు

Loop repeats – మళ్లీ మొదటి దశకు.

''')
rep('invite new users? తెలుగు:', 'invite new users?\n\nతెలుగు:')
rep('- Product Management + Product Design\n', 'Product Management + Product Design\n')
rep('Formula:\n\n- Reach × Impact × Confidence\n- RICE = ​\n- Effort\n', 'Formula:\n\nRICE = (Reach × Impact × Confidence) ÷ Effort\n')
rep('Feature Reach Impact Confidence Effort\n\nSimplified Checkout 1000 3 80% 4\n\nDark Mode 500 1 90% 3\n', 'Feature\tReach\tImpact\tConfidence\tEffort\nSimplified Checkout\t1000\t3\t80%\t4\nDark Mode\t500\t1\t90%\t3\n')
rows = json.load(open('/tmp/role_rows.json'))
between('Framework / Concept PM Product Designer', 'Primary అంటే సాధారణంగా', 'Framework / Concept\tPM\tProduct Designer\tUX Designer\tUI Designer\n' + '\n'.join('\t'.join(r) for r in rows) + '\n\n')
rep('Product: Food Delivery App Business Problem:', 'Product: Food Delivery App\n\nBusiness Problem:')
STEPS = [('Product Strategy – PM', 'Product Vision, Business Goals, North Star Metric, Product Roadmap, RICE Prioritisation', 'What should we improve?'),
         ('Discovery – PM + PD + UX', 'User Research, Assumptions, JTBD, Personas, Empathy Mapping', 'Why are users not placing their first order?'),
         ('Define – PD + UX', 'Research Insights, Problem Statement, Pain Points, HMW Questions, Double Diamond Define', 'Which problem should we solve?'),
         ('Ideation – PD + UX', 'Brainstorming, Design Thinking, Solution Exploration, Feature Prioritisation', 'What are the possible solutions?'),
         ('Experience Design – PD + UX', 'Information Architecture, User Journey, User Flow, Task Flow, Wireframes', 'How should users complete the task?'),
         ('Interface Design – PD + UI', 'Visual Hierarchy, Typography, Colours, Components, Design System, Responsive UI', 'How should the interface look and respond?'),
         ('Prototype & Testing – PD + UX + UI', 'Interactive Prototype, Usability Testing, A/B Testing, Hypothesis Validation', 'Does the solution actually work?'),
         ('Launch & Measurement – PM + PD + Team', 'Conversion Funnel, AARRR, HEART, Retention, Cohort Analysis, Growth Loops', 'Did we improve the product, and what should we improve next?')]
between('- 1 Product Strategy – PM', '### 14 · ', '@@FIG5\n\n' + 'Step\tదశ – ఎవరు\tConcepts\tప్రధాన ప్రశ్న\n' + '\n'.join(f'{k+1}\t{a}\t{b}\t{c}' for k, (a, b, c) in enumerate(STEPS)) + '\n\n')
rep('మొదటి Diamond – Problem Space', '@@FIG4\n\nమొదటి Diamond – Problem Space')
for a, b in [('Product Design Learning Roadmap\n\n', 'Product Design Learning Roadmap:\n\n')]:
    rep(a, b)
for lv in ['Level 1 – Core UX & Product Design', 'Level 2 – UX & Interaction', 'Level 3 – Product Strategy & Analytics', 'Level 4 – Senior / Lead Product Designer']:
    rep(lv + '\n\n', lv + ':\n')
open('loops_te.txt', 'w').write(t); print('final', len(t), t.count('@@FIG'))
t = open('loops_te.txt').read()
rep('మొదటి Diamond – Problem Space Discover:', 'మొదటి Diamond – Problem Space:\n\nDiscover:')
rep('రెండవ Diamond – Solution Space Develop:', 'రెండవ Diamond – Solution Space:\n\nDevelop:')
rep('ఇందులో Divergent & Convergent Thinking\n\n', 'ఇందులో Divergent & Convergent Thinking:\n\n')
open('loops_te.txt', 'w').write(t); print('ok2')
t = open('loops_te.txt').read()
for tag in ['Product Analytics + Growth', 'Product Growth + Engagement + Retention', 'Product Management + Growth Analytics', 'UX Research + Product Design',
            'Product Discovery + UX Strategy', 'Design Strategy + UX Process', 'Product Discovery + UX Design', 'Product Management + Product Design']:
    rep('\n' + tag + '\n', '\nవిభాగం: ' + tag + '\n')
open('loops_te.txt', 'w').write(t); print('ok3')
