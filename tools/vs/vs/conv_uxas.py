import re, sys, json
sys.path.insert(0, '.')
from parse_pdf import fix_te, blocks
TOP = ['User & Behavioral', 'Usability & Design', 'Value & Business', 'Feasibility & Edge', 'How to Use', 'Assumption vs Question', 'Interviewలో', 'మీ కోసం']
SHORT = {'1': '1 · User & Behavioral Assumptions', '2': '2 · Usability & Design Assumptions', '3': '3 · Value & Business Assumptions',
         '4': '4 · Feasibility & Edge-Case Assumptions', '5': '5 · UX Workflow లో ఎలా ఉపయోగించాలి?', '6': '6 · Assumption vs Question vs Hypothesis vs HMW',
         '7': '7 · Interview లో ఎలా Explain చేయాలి?', '8': '8 · Practical Exercise – Classic Rummy'}
raw = open('uxas.txt').read().split('\n')
out = []; top = 0; i = 0
while i < len(raw):
    r = raw[i]; s = r.strip(); i += 1
    if s in ('ChatGPT said:', 'Submit my answers', 'Write your research question...') or re.fullmatch(r'\d{1,2}', s): continue
    if i < 4 and s.startswith('UX Assumption Questions – Complete'): continue
    m = re.match(r'^(\d+)\. (.*)$', s)
    if top < len(TOP) and m and int(m.group(1)) == top + 1 and m.group(2).startswith(TOP[top]) and len(r) - len(r.lstrip()) == 0:
        top += 1; n = m.group(1)
        # next non-blank is a tagline (sections 1-4)
        sub = m.group(2)
        out += ['', f'@@H {SHORT[n]}\n{sub}', '']; continue
    if re.match(r'^\d\.\d ', s) and len(r) - len(r.lstrip()) == 0:
        out += ['', s + ':', '']; continue
    out.append(r)
t = fix_te(blocks(out, tables=True))
t = re.sub(r'@@H ([^\n]*)', r'### \1', t)
open('/tmp/uxas_te.txt', 'w').write(t); print(len(t), top)

t = open('/tmp/uxas_te.txt').read()
def rep(a, b, cnt=1):
    global t
    assert a in t, a[:90]; t = t.replace(a, b, cnt)
def between(a, b, new):
    global t
    i = t.index(a); j = t.index(b, i); t = t[:i] + new + t[j:]
t = re.sub(r'(?<=\S) English Explanation:', '\n\nEnglish Explanation:', t)
t = t.replace('English Explanation:\n', 'English Explanation:\n\n')
t = re.sub(r'\n{3,}', '\n\n', t)
rep('తెలుగు ప్రధానంగా + English Explanation + Practical Examples\n', 'తెలుగు ప్రధానంగా + English Explanation + Practical Examples.\n')
rep('ఇలాంటి సందేహాలను పరిశీలించడానికి Assumption Questions ఉపయోగపడతాయి.', 'ఇలాంటి సందేహాలను పరిశీలించడానికి Assumption Questions ఉపయోగపడతాయి.\n\n@@FIG1')
for tag in ['Understanding the User', 'Understanding the Experience', 'Understanding Product Value', 'Understanding Technical Possibilities']:
    rep('\n' + tag + '\n', '\nవిభాగం: ' + tag + '\n')
between('- 1 Open App', 'యూజర్ Tutorialలో ఎక్కువ సమయం', 'Open App → Login / Register → View Tutorial → Learn Rummy Rules → Learn Card Arrangement → Start First Game.\n\n')
between('Team Assumption Mapping', 'ఈ నాలుగు Assumptionsను పరిశీలించి', '''Team Assumption Mapping:

Role\tAssumption
Product Manager\tNew users are not starting their first game because they don't understand Rummy rules.
UX Designer\tUsers may be confused by the card arrangement and gameplay instructions.
Developer\tInteractive tutorials may require additional engineering effort.
Business Team\tBetter onboarding may improve first-game activation.

''')
between('Assumption Risk Matrix Illustrative examples for Classic Rummy', 'ఈ Matrix ఒక practical prioritization example', '''Assumption Risk Matrix – illustrative examples for Classic Rummy:

@@FIG2

Quadrant\tExample assumption\tAction
High Importance + Low Evidence (High priority)\tNew users don't understand Rummy rules.\tValidate immediately
High Importance + High Evidence (Investigate)\tFirst-game abandonment is a major issue.\tMonitor and act
Low Importance + Low Evidence (Lower priority)\tUsers may prefer a particular tutorial animation.\tValidate later
Low Importance + High Evidence (Low priority)\tUsers understand the login screen.\tNo immediate action

''')
rep('usability testing activities. Example:', 'usability testing activities.\n\nExample:')
between('Step 1 – Assumption', 'ఇక్కడ మనం ఒక ముఖ్యమైన విషయం గుర్తుంచుకోవాలి', '''@@FIG3

Step\tExample
1. Assumption\tNew users don't understand Rummy rules.
2. Research Question\tWhat challenges do new users face when learning Rummy?
3. User Interview Question\t"Can you describe your experience when you first tried playing Rummy?"
4. Usability Testing Task\t"Imagine you are playing Rummy for the first time. Please try to arrange these cards into valid combinations."
5. Research Observation\tObserve where users hesitate, make mistakes, or ask for help.
6. Design Decision\tBased on the findings, decide whether users need a full tutorial, contextual guidance, or a simplified gameplay experience.

''')
between('UX Processలో వీటి స్థానం', 'గమనిక: ఇది ఒక సాధారణ Design Thinking Workflow', '''UX Processలో వీటి స్థానం:

Discover (Assumptions + Research Questions) → Define (Validated Insights + Problem Statement) → Ideate (HMW + Ideas + Hypotheses) → Prototype & Test (Design + Validation).

''')
rep('English – Interview Answer\n\n"Before', 'English – Interview Answer:\n\n“Before')
rep('user needs and business objectives."', 'user needs and business objectives.”')
rep('తెలుగు అర్థం డిజైన్ ప్రారంభించే ముందు', 'తెలుగు అర్థం:\n\nడిజైన్ ప్రారంభించే ముందు')
rep('పని చేస్తున్నట్లు గా', 'పని చేస్తున్నట్లుగా')
between('1. Assumption\n\nNew users', 'నా సూచన:', '''1. New users don't understand Rummy rules.
2. Users prefer interactive tutorials over videos.
3. A shorter onboarding flow will improve activation.
4. Users understand card arrangement icons.
5. Users will return to the tutorial when needed.

ఒక నమూనా సమాధానం (Model answer) Group 0 review page లో ఉంది.

''')
rep('ప్రతి Assumptionకు సరైన Research Question రాయండి. మీ సమాధానాలను నేను Review చేస్తాను.', 'ప్రతి Assumptionకు సరైన Research Question రాయండి. తర్వాత Model Answer తో పోల్చండి.')
open('uxas_te.txt', 'w').write(t); print('final', len(t), t.count('@@FIG'))
