import re, sys
sys.path.insert(0, '.')
from parse_pdf import fix_te, blocks
TOP = ['Product Manager (PM)', 'Product Designer (PD)', 'UX Designer', 'UI Designer', 'PM, PD, UX, UI', 'Product Design Process',
       'Assumption vs Hypothesis', 'మంచి HMW', 'నీ ప్రా', 'Practical Exercise']
SHORT = {'5': '5 · ఒకే సమస్య – నాలుగు HMW ప్రశ్నలు', '6': '6 · Design Process లో HMW ఎక్కడ?', '7': '7 · Assumption vs Hypothesis vs HMW',
         '8': '8 · మంచి HMW ఎలా రాయాలి?', '9': '9 · నీ projects ఆధారంగా HMW', '10': '10 · Practical Exercise'}
raw = open('hmw.txt').read().split('\n')
out = []; top = 0; i = 0; ended = False
while i < len(raw):
    r = raw[i]; s = r.strip(); i += 1
    if s == 'ChatGPT said:' or re.fullmatch(r'[a-z0-9.-]+\.(?:com|co|net|io|org|edu)', s) or re.fullmatch(r'\d{1,2}', s): continue
    if i < 4 and s.startswith('Product Designలో Assumption'): continue
    if re.fullmatch(r'[ఀ-౿ ]{1,40}', s) and len(s.split()) >= 3 and 'ర్డ' in s and len(s) < 40: continue  # stray glyph line
    m = re.match(r'^(\d+)\. (.*)$', s)
    if top < len(TOP) and m and int(m.group(1)) == top + 1 and m.group(2).startswith(TOP[top]) and len(r) - len(r.lstrip()) == 0:
        top += 1; n = m.group(1)
        out += ['', f'@@H {SHORT.get(n, n + " · " + m.group(2))}\n{m.group(2)}', '']
        continue
    if re.match(r'^[A-E]\. ', s) and len(r) - len(r.lstrip()) == 0:
        out += ['', s.rstrip(':') + ':', '']; continue
    if s.startswith('Step 1 – ') or s == 'Submit my answer': break
    out.append(r)
t = fix_te(blocks(out, tables=True))
t = re.sub(r'@@H ([^\n]*)', r'### \1', t)
open('/tmp/hmw_te.txt', 'w').write(t); print(len(t), top)

t = open('/tmp/hmw_te.txt').read()
for a, b in [('ఆధారాలతో నిరూపించలేదు. Example:', 'ఆధారాలతో నిరూపించలేదు.\nExample:'), ('భావించడం. Example:', 'భావించడం.\nExample:'),
             ('ఉత్పత్తు లను', 'ఉత్పత్తులను'), ('Context? Example:', 'Context?\n\nExample:'),
             ('during checkout. కస్టమర్లు ఫుడ్', 'during checkout.\nకస్టమర్లు ఫుడ్'),
             ('ముందుగా ఈ ఐదు పదాల మధ్య తేడా తెలుసుకుందాం.', 'ముందుగా ఈ ఐదు పదాల మధ్య తేడా తెలుసుకుందాం.\n\n@@FIG1')]:
    assert a in t, a; t = t.replace(a, b)
t = t.replace('Common Problem\n\n', '@@FIG2\n\nCommon Problem:\n\n', 1)
for p in ['PM – Business Perspective', 'PD – Product Experience Perspective', 'UX – Usability Perspective', 'UI – Visual Perspective']:
    t = t.replace(p + '\n\n', p + ':\n\n', 1)
SEC6 = '''ఇప్పుడు ఒక పూర్తి Design Thinking ప్రక్రియలో Assumptions, Questions, HMW ఎక్కడ ఉపయోగిస్తారో చూద్దాం.

@@FIG3

1. Discover – Research: యూజర్, బిజినెస్, మార్కెట్ గురించి తెలుసుకోవడం.
- User interviews
- Surveys
- Analytics
- Competitor analysis

ఇక్కడ Research Questions, Assumptions వస్తాయి.

2. Define – Problem Identification: సేకరించిన సమాచారాన్ని విశ్లేషించి అసలు సమస్యను గుర్తించడం.
- Research insights
- Pain points
- User needs
- Problem statement

ఇక్కడ Assumptions‌ను పరిశీలించి, నిర్ధారించని వాటిని పరీక్షించాలి.

3. How Might We – Opportunity Framing: గుర్తించిన సమస్యను పరిష్కార అవకాశంగా మార్చడం.
- HMW questions
- Design challenges
- Opportunity areas

ఇది Ideationకు దారి చూపుతుంది.

4. Ideate – Solution Exploration: అనేక పరిష్కారాల గురించి ఆలోచించడం.
- Brainstorming
- Crazy 8s
- Sketching
- Solution prioritisation

5. Prototype – Design Solutions: ఎంపిక చేసిన పరిష్కారాలను డిజైన్ నమూనాలుగా రూపొందించడం.
- User flows
- Wireframes
- UI designs
- Interactive prototypes

6. Test – Validation: యూజర్లతో డిజైన్‌ను పరీక్షించడం.
- Usability testing
- Feedback
- Hypothesis validation
- Design iterations

'''
i = t.index('ఇప్పుడు ఒక పూర్తి Design Thinking'); j = t.index('గమనిక: ఇది ఒక సాధారణ Design Thinking workflow')
t = t[:i] + SEC6 + t[j:]
SEC9 = '''నీ Portfolioలో ఉన్న ప్రాజెక్టులను తీసుకొని కొన్ని ఉదాహరణలు చూద్దాం.

A. Classic Rummy – Openplay:
- Problem: New users struggle to understand the game.
- HMW: How might we help new players understand Rummy rules and start playing confidently?
- తెలుగు: కొత్త యూజర్లు Rummy నియమాలను అర్థం చేసుకొని నమ్మకంగా ఆడటం ప్రారంభించేలా ఎలా చేయగలం?

B. TWAM – E-commerce App:
- Problem: Users find it difficult to discover suitable products.
- HMW: How might we help users discover products that match their preferences more easily?
- తెలుగు: యూజర్లు తమ అభిరుచులకు సరిపోయే ఉత్పత్తులను సులభంగా కనుగొనేలా ఎలా చేయగలం?

C. ResolveAI – SaaS Concept:
- Problem: Support teams spend too much time handling repetitive queries.
- HMW: How might we help support teams resolve repetitive customer queries faster using AI?
- తెలుగు: AI సహాయంతో Support Teams పదే పదే వచ్చే కస్టమర్ ప్రశ్నలను త్వరగా పరిష్కరించేలా ఎలా చేయగలం?

D. ORRBUS – Mobility Concept:
- Problem: Commuters find it difficult to plan convenient journeys.
- HMW: How might we help commuters plan reliable and convenient journeys using real-time travel information?
- తెలుగు: రియల్‌టైమ్ ప్రయాణ సమాచారంతో ప్రయాణికులు సులభమైన, నమ్మకమైన ప్రయాణాలను ప్లాన్ చేసుకునేలా ఎలా చేయగలం?

'''
i = t.index('నీ Portfolioలో ఉన్న ప్రాజెక్టులను'); j = t.index('ఇవి Portfolioలో చూపించగలిగే Problem Framing')
t = t[:i] + SEC9 + t[j:]
t = t.rstrip() + '''

1. Step 1 – ఏ పాత్రలో ఆలోచిస్తున్నావు? Product Manager / Product Designer / UX Designer / UI Designer
2. Step 2 – నీ Assumption ఏమిటి? (ఉదా: Users find the app difficult to understand.)
3. Step 3 – నీ HMW Question రాయండి: How might we...
4. Step 4 – ఈ ప్రశ్న ఎందుకు ఎంచుకున్నావు? English లేదా తెలుగులో నీ ఆలోచన వివరించు.

నీ సమాధానాన్ని Senior Product Designer స్థాయిలో పరిశీలించు: Assumption సరైనదా, HMW ప్రశ్న స్పష్టంగా ఉందా, అది సరైన Role‌కు సరిపోతుందా, English ఎలా మెరుగుపరచాలి. ఒక నమూనా సమాధానం Group 0 review page లో ఉంది.'''
open('hmw_te.txt', 'w').write(t); print('final', len(t), t.count('@@FIG'))
t = open('hmw_te.txt').read()
for a, b in [('Users abandon checkout due to too many\tAt which exact step do users abandon checkout?\n\nsteps.\n\n', 'Users abandon checkout due to too many steps.\tAt which exact step do users abandon checkout?\n'),
             ('help users understand the checkout\n\n- process?', 'help users understand the checkout process?'),
             ('రెస్టా రెంట్', 'రెస్టారెంట్'), ('వృద్ధు లు', 'వృద్ధులు')]:
    assert a in t, a; t = t.replace(a, b)
open('hmw_te.txt', 'w').write(t); print('fixed')
