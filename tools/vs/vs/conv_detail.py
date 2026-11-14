import re, sys
sys.path.insert(0, '.')
from parse_pdf import fix_te, blocks
TOP = [('1', 'Product Manager (PM)'), ('2', 'Product Designer (PD)'), ('3', 'UX Designer (UX)'), ('4', 'UI Designer (UI)'),
       ('5', 'Product Designer vs UX Designer vs UI Designer'), ('6', 'ఒకే ప్రా'), ('7', 'ఒక ముఖ్యమైన ఉదాహరణ'), ('8', 'Career Perspective'),
       ('9', 'Product Design Project'), ('10', 'Interview Preparation'), ('11', 'ఇంటర్వ్యూలో చెప్పడానికి'), ('12', 'ఇప్పుడు నీ అవగాహన')]
raw = open('pm_detail.txt').read().split('\n')
out = []; i = 0; top_i = 0; quiz = False
while i < len(raw):
    r = raw[i]; s = r.strip(); i += 1
    if s in ('ChatGPT said:',) or re.fullmatch(r'[a-z0-9.-]+\.(?:com|co|net|io|org)', s) or re.fullmatch(r'\d{1,2}', s): continue
    if i < 6 and s.startswith('Product Manager vs Product Designer vs UX'): continue
    m = re.match(r'^(\d+)\. (.*)$', s)
    if top_i < len(TOP) and m and m.group(1) == TOP[top_i][0] and m.group(2).startswith(TOP[top_i][1]) and (len(r) - len(r.lstrip())) == 0:
        top_i += 1
        # next non-blank line is the subtitle (for sections 1–4)
        sub = ''
        if top_i <= 4:
            while not raw[i].strip(): i += 1
            sub = raw[i].strip(); i += 1
        out += ['', f'@@H {m.group(1)} · {m.group(2)}' + ('\n' + sub if sub else '\n' + m.group(2)), '']
        continue
    if re.match(r'^\d+\.\d+ ', s) and len(r) - len(r.lstrip()) == 0:
        out += ['', s.rstrip(':') + ':', '']; continue
    out.append(r)
txt = blocks(out, tables=True)
txt = re.sub(r'@@H ([^\n]*)', r'### \1', txt)
txt = fix_te(txt)
open('/tmp/detail_te.txt', 'w').write(txt)
print(len(txt))

# ---- post-processing
t = open('/tmp/detail_te.txt').read()
t = t.replace('పూర్తి వివరణ – తెలుగు ప్రధానంగా + English terminology ఈ నాలుగు', 'పూర్తి వివరణ – తెలుగు ప్రధానంగా + English terminology.\n\nఈ నాలుగు')
for a, b in [('ట్రా క్', 'ట్రాక్'), ('దృష్టి )', 'దృష్టి)'), ('పెట్టు కుంటే', 'పెట్టుకుంటే'), ('రెస్టా రెంట్', 'రెస్టారెంట్')]:
    t = t.replace(a, b)
SHORT = {'5': '5 · PD vs UX vs UI – అసలు తేడా', '6': '6 · ఒకే ప్రాజెక్ట్‌లో నాలుగు పాత్రలు', '7': '7 · Classic Rummy ఉదాహరణ',
         '8': '8 · Career Perspective', '9': '9 · పూర్తి Product Design ప్రక్రియ', '10': '10 · Interview Preparation',
         '11': '11 · English Summary', '12': '12 · ముఖ్యమైన సూచన'}
def hdr(m):
    n, title, sub = m.group(1), m.group(2), m.group(3)
    return f'### {SHORT[n]}\n{title}' if n in SHORT else m.group(0)
t = re.sub(r'### (\d+) · ([^\n]*)\n([^\n]*)', hdr, t)
# section 9 table
i = t.index('Phase\tActivities\tDeliverables'); j = t.index('ఈ మొత్తం ప్రక్రియలో:')
rows = []
for l in t[i:j].split('\n')[1:]:
    m = re.match(r'^(\d+)\. (\S+(?: Design)?) (.+)$', l.strip())
    if m: rows.append(l.strip())
PH = [('1. Discover', 'Business understanding, user research', 'Research insights'), ('2. Define', 'Problem identification, goals', 'Problem statement'),
      ('3. Ideate', 'Brainstorming, solutions', 'Concepts'), ('4. Structure', 'IA, sitemap, user flows', 'User flows'),
      ('5. Design', 'Wireframes, interaction design', 'Wireframes'), ('6. Visual Design', 'UI, typography, colours', 'High-fidelity UI'),
      ('7. Prototype', 'Interactive prototype', 'Figma prototype'), ('8. Validate', 'Usability testing', 'Testing findings'),
      ('9. Develop', 'Developer collaboration', 'Functional product'), ('10. Measure', 'Analytics, feedback', 'Improvement opportunities')]
assert len(rows) == 10
t = t[:i] + '@@FIG3\n\n' + 'Phase\tActivities\tDeliverables\n' + '\n'.join('\t'.join(p) for p in PH) + '\n\n' + t[j:]
# quiz -> extras; keep final advice paragraph
k = t.index('### 12 · ')
advice = t[t.index('నా ముఖ్యమైన సూచన:'):].strip()
t = t[:k] + '### 12 · ముఖ్యమైన సూచన\nSenior / Lead Product Designer ఇంటర్వ్యూలకు\n\n' + advice + '\n\nPractical role-based assessment (4 scenarios) – Group 0 review page లో ఉంది.'
# figures
t = t.replace('### 1 · Product Manager (PM)', '@@FIG1\n\n### 1 · Product Manager (PM)', 1)
t = t.replace('Stage\tUser Action\tPossible Pain Point', '@@FIG2\n\nStage\tUser Action\tPossible Pain Point', 1)
open('detail_te.txt', 'w').write(t)
print('final', len(t), t.count('@@FIG'))
