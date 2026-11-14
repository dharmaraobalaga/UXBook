import re, sys
sys.path.insert(0, '.')
from parse_pdf import fix_te, blocks
TOP = ['PRD ఎందుకు', 'PRD ఎవరు', 'PRD Document', 'PRD Writing', 'PRDలో PM', 'How a PM', 'PRD, BRD', 'PRD తయారు', 'PRD Quality', 'Interviewలో', 'నీ తదుపరి']
SHORT = {'1': '1 · PRD ఎందుకు అవసరం?', '2': '2 · PRD ఎవరు, ఎప్పుడు రాస్తారు?', '3': '3 · PRD – Complete Structure', '4': '4 · ప్రతి Section ఎలా రాయాలి?',
         '5': '5 · PM ఏమి రాస్తారు? Designer ఏమి అందిస్తారు?', '6': '6 · PM PRD Writing Workflow', '7': '7 · PRD vs BRD vs FRD vs SRS',
         '8': '8 · PRD Tools', '9': '9 · PRD Quality Checklist', '10': '10 · Interview లో ఎలా చెప్పాలి?', '11': '11 · నీ తదుపరి Practical Learning'}
raw = open('prd.txt').read().split('\n')
out = []; top = 0; i = 0
while i < len(raw):
    r = raw[i]; s = r.strip(); i += 1
    if s in ('ChatGPT said:', 'Official website', 'Plain text', 'Reset checklist') or re.fullmatch(r'[a-z0-9.…-]+\.(?:com|co|net|io|org|edu|pm|so|au)(?: \+\d)?', s) or re.fullmatch(r'\d{1,2}', s): continue
    if i < 4 and s.startswith('How a Product Manager Writes'): continue
    m = re.match(r'^(\d+)\. (.*)$', s)
    if top < len(TOP) and m and int(m.group(1)) == top + 1 and m.group(2).startswith(TOP[top]) and len(r) - len(r.lstrip()) == 0:
        top += 1; n = m.group(1)
        out += ['', f'@@H {SHORT[n]}\n{m.group(2)}', '']; continue
    if re.match(r'^4\.\d+ ', s) and len(r) - len(r.lstrip()) == 0:
        out += ['', s + ':', '']; continue
    out.append(r)
t = fix_te(blocks(out, tables=True))
t = re.sub(r'@@H ([^\n]*)', r'### \1', t)
open('/tmp/prd_te.txt', 'w').write(t); print(len(t), top)

t = open('/tmp/prd_te.txt').read()
def rep(a, b):
    global t
    assert a in t, a[:90]; t = t.replace(a, b, 1)
def between(a, b, new):
    global t
    i = t.index(a); j = t.index(b, i); t = t[:i] + new + t[j:]
rep('Product Requirements Document (PRD) – తెలుగులో పూర్తి వివరణ + English Examples ఒక Product Manager', 'Product Requirements Document (PRD) – తెలుగులో పూర్తి వివరణ + English Examples.\n\nఒక Product Manager')
rep('ఇవి వేర్వేరు డాక్యుమెంట్లు అయినప్పటికీ', '@@FIG1\n\nఇవి వేర్వేరు డాక్యుమెంట్లు అయినప్పటికీ')
rep('PRD Table of Contents\n\n', '@@FIG2\n\nPRD Table of Contents:\n\n')
rep('so that I can complete checkout faster. తెలుగు:', 'so that I can complete checkout faster.\n\nతెలుగు:')
rep('- As a customer, I want to see the complete price breakdown', 'As a customer, I want to see the complete price breakdown')
rep('- As a customer, I want to choose my preferred payment method', 'As a customer, I want to choose my preferred payment method')
rep('Standard User Story Format:\n\nAs a [User Type],\n\nI want [Action / Need],\n\nSo that [Benefit / Goal].', 'Standard User Story Format:\n\nAs a [User Type], I want [Action / Need], so that [Benefit / Goal].')
for n in ['User Story 1 – Address Selection', 'User Story 2 – Price Breakdown', 'User Story 3 – Payment Selection']:
    rep(n + '\n', n + ':\n')
between('Example User Flow:', 'ఈ Flowలో PM ప్రధాన Business Rules', '''Example User Flow:

@@FIG3

Cart → Checkout → Select Address → Review Order Summary → Select Payment Method → Confirm Order → Payment Processing → Payment Successful → Order Confirmation.

Payment Failed అయితే: Retry / Choose Another Method.

''')
rep('System shall display saved\tGiven saved addresses exist, when checkout opens, then the saved addresses\naddresses.\tare displayed.\nSystem shall calculate total amount.\tGiven valid cart items and applicable charges, when checkout loads, then the\n\n- correct total is shown.\n',
    'System shall display saved addresses.\tGiven saved addresses exist, when checkout opens, then the saved addresses are displayed.\nSystem shall calculate total amount.\tGiven valid cart items and applicable charges, when checkout loads, then the correct total is shown.\n')
rep('Checkout Completion Rate.\n\n- Completed Orders\n- Checkout Completion Rate = × 100\n- Checkout Started\n- ​\n', 'Checkout Completion Rate.\n\nCheckout Completion Rate = (Completed Orders ÷ Checkout Started) × 100\n')
for a in ['Given – The customer', 'When – The customer', 'Then – The selected']:
    pass
rep('ట్రా క్', 'ట్రాక్')
STEPS = [('Understand the Business Request', 'Business Team నుంచి వచ్చిన అవసరాన్ని అర్థం చేసుకోవడం.', 'Increase first-time orders.'),
         ('Analyse Data', 'Analytics, customer feedback, support tickets పరిశీలించడం.', 'First-time users are dropping off before payment.'),
         ('Conduct Discovery', 'UX Researcher, Product Designer‌తో కలిసి యూజర్ సమస్యను అర్థం చేసుకోవడం.', 'Users are confused about the total order price.'),
         ('Define the Problem', 'స్పష్టమైన Problem Statement రాయడం.', 'Users lack price transparency during checkout.'),
         ('Define Goals and Success Metrics', 'ఏ ఫలితాన్ని సాధించాలి? ఎలా కొలవాలి?', 'Improve checkout completion rate.'),
         ('Define Scope and Requirements', 'In Scope, Out of Scope, User Stories, Functional Requirements, Business Rules రాయడం.', '—'),
         ('Collaborate with Design & Engineering', 'UX Flow, UI Requirements, Technical Feasibility, Edge Cases చర్చించడం.', '—'),
         ('Define Acceptance Criteria', 'ప్రతి Requirement ఎప్పుడు Complete అని చెప్పవచ్చో నిర్వచించడం.', '—'),
         ('Review and Approve', 'Stakeholders, Design, Engineering, QA టీమ్‌లతో PRD Review చేయడం.', '—'),
         ('Monitor After Launch', 'Analytics ద్వారా Feature ఫలితాలను పరిశీలించి అవసరమైన మార్పులు చేయడం.', '—')]
between("PM's PRD Writing Workflow", '### 7 · ', "PM's PRD Writing Workflow:\n\n@@FIG4\n\nStep\tఏమి చేస్తారు\tExample\n" + '\n'.join(f'{k+1}. {a}\t{b}\t{c}' for k, (a, b, c) in enumerate(STEPS)) + '\n\n')
TOOLS = [('Confluence', 'PRD Documentation, collaboration, version history.'), ('Notion', 'PRD templates, product documentation, team workspace.'),
         ('Jira', 'User Stories, Backlog, Sprint Planning, task tracking.'), ('Figma', 'User Flows, Wireframes, UI Design, Prototypes, Design Specifications.'),
         ('Linear', 'Product Issues, Projects, Roadmaps and team workflows.')]
between('- Confluence\n', '### 9 · ', 'Tool\tఉపయోగం\n' + '\n'.join(f'{a}\t{b}' for a, b in TOOLS) + '\n\n')
rep('PRD Review\t0/16 completed\n', 'PRD Review – 16 ప్రశ్నలు:\n')
between('- When creating a PRD, I first', 'తెలుగు అర్థం:', '''“When creating a PRD, I first understand the business objective and the user problem behind the feature.
I analyse available product data, customer feedback and research insights to identify the actual problem.
Then I define the problem statement, target users, goals, success metrics and feature scope.
Next, I document user stories, functional requirements, business rules, edge cases and acceptance criteria.
I collaborate with Product Designers, UX/UI Designers, Engineering and QA teams to ensure the requirements are clear, feasible and aligned with the user experience.
Finally, I get stakeholder feedback, finalise the PRD and work with the team throughout development, testing and release.
After launch, I monitor product metrics to understand whether the feature has achieved its intended goals.”

''')
open('prd_te.txt', 'w').write(t); print('final', len(t), t.count('@@FIG'))
