"""Group 0 · 0.3 diagrams (PM vs Product Designer vs UX vs UI) – original drawings by Claude (the PDF's images are from medium.com / behance.net and are not copied)."""
import svgkit
from svgkit import *
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

# bright role colours (fill, text)
ROLE = [('#ff8a3d', 'Product Manager', 'What should we build, and why?', 'Vision · roadmap · priorities'),
        ('#7b5cff', 'Product Designer', 'How should the product solve the problem?', 'End-to-end experience'),
        ('#12b886', 'UX Designer', 'How will users complete tasks easily?', 'Research · flows · usability'),
        ('#2f80ed', 'UI Designer', 'How should the interface look?', 'Visual design · components')]

@reg('vs-roles-glance')
def glance():
    s = SVG(680, 384, 'Four roles at a glance', 'One product, four different questions')
    for i, (c, name, q, out) in enumerate(ROLE):
        x, y = 28 + (i % 2) * 320, 82 + (i // 2) * 146
        s.rect(x, y, 304, 132, c, c, 16)
        s.circle(x + 34, y + 34, 18, WHITE, WHITE); s.text(x + 34, y + 40, ['PM', 'PD', 'UX', 'UI'][i], 12.5, 800, c, 'middle')
        s.text(x + 62, y + 40, name, 16, 800, WHITE)
        s.wrap(x + 20, y + 74, 270, q, 13, 700, WHITE)
        s.text(x + 20, y + 118, out, 11.5, 600, WHITE)
    return s

@reg('vs-roles-workflow')
def wf():
    steps = [('#ff8a3d', 'Product Manager', 'Identifies the business problem, sets priorities', 'Vision, roadmap, requirements'),
             ('#7b5cff', 'Product Designer', 'Shapes the overall product experience', 'Design strategy, concepts, prototypes'),
             ('#12b886', 'UX Designer', 'Structure, user journey and interaction flow', 'Research, journeys, IA, wireframes'),
             ('#2f80ed', 'UI Designer', 'Visual interface and reusable components', 'Hi-fi screens, UI specs'),
             ('#f2c94c', 'Engineering Team', 'Builds the product with the team throughout', 'Functional product'),
             ('#eb5757', 'Product Team', 'Measures results, learns, improves', 'Insights for the next cycle')]
    s = SVG(700, 120 + len(steps) * 66, 'How the four roles work together', 'A conceptual workflow – in real teams these roles overlap and collaborate continuously')
    for i, (c, name, what, out) in enumerate(steps):
        y = 84 + i * 66
        s.circle(52, y + 26, 22, c, c); s.text(52, y + 32, str(i + 1), 16, 800, WHITE if i != 4 else NAVY, 'middle')
        if i < len(steps) - 1: s.line(52, y + 50, 52, y + 68, LINE, 3)
        s.rect(88, y, 584, 54, WHITE, c, 12, 2)
        s.rect(88, y, 10, 54, c, c, 4)
        s.text(112, y + 23, name, 14, 800, INK)
        s.text(112, y + 43, what, 11.5, 600, INK2)
        s.text(660, y + 32, out, 11, 700, INK3, 'end')
    s.path(f'M 30 {84 + 5*66 + 26} C 0 {84 + 5*66}, 0 110, 30 110', '#eb5757', 1.6, dash='5 4')
    return s

@reg('vs-roles-formula')
def formula():
    rows = [('#ff8a3d', 'PM', 'Product Manager', ['What to build', 'Why to build', 'What to prioritise']),
            ('#7b5cff', 'PD', 'Product Designer', ['Problem Solving', 'UX', 'UI', 'Product Thinking']),
            ('#12b886', 'UX', 'UX Designer', ['User Research', 'User Understanding', 'Usability', 'Interaction Design']),
            ('#2f80ed', 'UI', 'UI Designer', ['Visual Design', 'Layout', 'Typography', 'Colour', 'Components'])]
    s = SVG(700, 96 + len(rows) * 74, 'Each role in one line', 'Simple formulas from the guide')
    for i, (c, ab, name, parts) in enumerate(rows):
        y = 80 + i * 74
        s.rect(28, y, 644, 62, c, c, 14)
        s.circle(60, y + 31, 20, WHITE, WHITE); s.text(60, y + 36, ab, 12.5, 800, c, 'middle')
        s.text(92, y + 27, name, 14, 800, WHITE); s.text(92, y + 47, '=', 14, 800, WHITE)
        x = 112
        for j, p_ in enumerate(parts):
            w = len(p_) * 6.4 + 20
            if j: s.text(x - 1, y + 47, '+', 13, 800, WHITE, 'end')
            s.rect(x + 6, y + 32, w, 22, WHITE, WHITE, 11); s.text(x + 6 + w / 2, y + 47, p_, 11, 700, c, 'middle')
            x += w + 20
    return s

@reg('vs-food-journey')
def journey():
    st = [('Discover', 'App open', 'Finding a restaurant', '#ff8a3d'), ('Explore', 'Menu browse', 'Too many choices', '#f2994a'),
          ('Select', 'Food selection', 'Comparing prices', '#f2c94c'), ('Checkout', 'Address & payment', 'Payment confusion', '#eb5757'),
          ('Track', 'Order tracking', 'Status unclear', '#2f80ed'), ('Receive', 'Food delivery', 'Delays', '#12b886')]
    s = SVG(700, 300, 'Food delivery app – user journey', 'Stage → user action → possible pain point')
    for i, (a, b, c, col) in enumerate(st):
        x = 28 + i * 108
        s.rect(x, 82, 100, 44, col, col, 22); s.text(x + 50, 109, a, 13, 800, WHITE if col != '#f2c94c' else NAVY, 'middle')
        if i < 5: s.arrow(x + 101, 104, x + 107, 104, INK3)
        s.box(x, 140, 100, 52, b, fill=WHITE, stroke=col, tc=INK, size=11.5, weight=700, r=10, sw=2)
        s.rect(x, 206, 100, 64, WARN_S, WARN_S, 10); s.text(x + 50, 224, 'Pain point', 9.5, 800, WARN, 'middle')
        s.wrap(x + 50, 244, 90, c, 11, 600, INK2, 'middle')
    return s

@reg('vs-design-process-10')
def process():
    ph = ['Discover', 'Define', 'Ideate', 'Structure', 'Design', 'Visual Design', 'Prototype', 'Validate', 'Develop', 'Measure']
    cols = ['#ff8a3d', '#f2994a', '#f2c94c', '#6fcf97', '#12b886', '#2d9cdb', '#2f80ed', '#7b5cff', '#bb6bd9', '#eb5757']
    s = SVG(700, 330, 'Product design project – 10 phases', 'From discovery to measuring results')
    for i, (p_, c) in enumerate(zip(ph, cols)):
        row, k = divmod(i, 5); k = k if row == 0 else 4 - k
        x, y = 40 + k * 128, 90 + row * 120
        s.circle(x + 28, y + 28, 28, c, c); s.text(x + 28, y + 35, str(i + 1), 18, 800, WHITE if c != '#f2c94c' else NAVY, 'middle')
        s.text(x + 28, y + 76, p_, 12, 800, INK, 'middle')
        if i in (0, 1, 2, 3): s.arrow(x + 60, y + 28, x + 124, y + 28, INK3)
        if i in (5, 6, 7, 8): s.arrow(x - 4, y + 28, x - 68, y + 28, INK3)
    s.path('M 610 118 C 664 130, 664 226, 614 236', INK3, 1.6); s.arrow(626, 232, 612, 238, INK3)
    return s

@reg('vs-hmw-terms')
def hmw_terms():
    rows = [('#ff8a3d', 'Assumption', 'What we believe – not yet proven', 'Users abandon checkout because of too many steps.'),
            ('#f2c94c', 'Question', 'What we want to find out', 'Why are users abandoning checkout?'),
            ('#12b886', 'Hypothesis', 'A testable prediction', 'If we reduce steps, more users may complete orders.'),
            ('#2f80ed', 'Problem Statement', 'The problem to solve', 'Checkout is confusing and the final price is unclear.'),
            ('#7b5cff', 'How Might We', 'A question that opens up solutions', 'HMW make checkout simpler and more transparent?')]
    s = SVG(700, 96 + len(rows) * 64, 'Five words, five purposes', 'Assumption → Question → Hypothesis → Problem Statement → HMW')
    for i, (c, name, what, ex) in enumerate(rows):
        y = 80 + i * 64
        s.rect(28, y, 200, 52, c, c, 12); s.text(128, y + 24, name, 14, 800, WHITE if c != '#f2c94c' else NAVY, 'middle')
        s.text(128, y + 42, what, 10, 600, WHITE if c != '#f2c94c' else NAVY, 'middle')
        s.rect(240, y, 432, 52, WHITE, c, 12, 2); s.text(256, y + 31, ex, 12, 600, INK2)
    return s

@reg('vs-hmw-four-lenses')
def lenses():
    s = SVG(700, 400, 'One problem – four HMW questions', 'Each role looks at the same problem through a different lens')
    s.rect(160, 78, 380, 56, NAVY, NAVY, 14)
    s.text(350, 102, 'Common problem', 11, 700, '#c9d0ea', 'middle'); s.text(350, 122, 'Customers abandon food orders at checkout', 13.5, 800, WHITE, 'middle')
    cards = [('#ff8a3d', 'PM · Business', 'How might we increase checkout conversion and completed orders?'),
             ('#7b5cff', 'PD · Product experience', 'How might we create a seamless and trustworthy checkout experience?'),
             ('#12b886', 'UX · Usability', 'How might we help users complete checkout with fewer steps and less confusion?'),
             ('#2f80ed', 'UI · Visual', 'How might we make pricing, payment options and Place Order more visible?')]
    s.line(350, 134, 350, 148, INK3, 2); s.line(185, 148, 515, 148, INK3, 2); s.line(185, 148, 185, 158, INK3, 2); s.line(515, 148, 515, 158, INK3, 2)
    for i, (c, lab, q) in enumerate(cards):
        x, y = 28 + (i % 2) * 330, 160 + (i // 2) * 116
        s.rect(x, y, 314, 102, c, c, 14)
        s.text(x + 18, y + 26, lab, 13, 800, WHITE)
        s.wrap(x + 18, y + 52, 280, q, 12.5, 600, WHITE)
    return s

@reg('vs-hmw-process')
def hmw_process():
    st = [('Discover', 'Research questions & assumptions', '#ff8a3d'), ('Define', 'Insights, pain points, problem statement', '#f2994a'),
          ('How Might We', 'Turn the problem into opportunities', '#7b5cff'), ('Ideate', 'Brainstorm, Crazy 8s, sketching', '#12b886'),
          ('Prototype', 'Flows, wireframes, UI, prototypes', '#2f80ed'), ('Test', 'Usability testing, validate hypotheses', '#eb5757')]
    s = SVG(700, 320, 'Where HMW fits in the design process', 'A typical design thinking flow – real teams loop back often')
    for i, (n, d, c) in enumerate(st):
        x = 28 + i * 110; hl = n == 'How Might We'
        s.rect(x, 86 if not hl else 76, 100, 170 if not hl else 190, c, c, 14)
        s.circle(x + 50, 116 if not hl else 108, 18, WHITE, WHITE); s.text(x + 50, 122 if not hl else 114, str(i + 1), 14, 800, c, 'middle')
        s.wrap(x + 50, 160 if not hl else 154, 88, n, 12.5, 800, WHITE, 'middle')
        s.wrap(x + 50, 196 if not hl else 196, 88, d, 10, 600, WHITE, 'middle')
    s.path('M 670 266 C 640 306, 90 306, 60 266', INK3, 1.5, dash='5 4'); s.text(350, 312, 'iterate – assumptions are tested throughout', 10.5, 700, INK3, 'middle')
    return s

@reg('vs-frameworks-map')
def fmap():
    rows = [('#ff8a3d', 'A · Product Strategy', 'PM', 'Vision · Roadmap · North Star · RICE · MoSCoW · AARRR'),
            ('#f2c94c', 'B · Discovery & Research', 'PM + PD + UX', 'Design Thinking · Double Diamond · JTBD · Personas · Assumptions · HMW'),
            ('#12b886', 'C · Experience Design', 'PD + UX', 'User Journey · User Flow · Task Flow · IA · Wireframes · Prototypes'),
            ('#2f80ed', 'D · Interface Design', 'PD + UI', 'Visual Hierarchy · Design Systems · Components · Responsive · Accessibility'),
            ('#7b5cff', 'E · Measurement & Growth', 'PM + PD + Analytics', 'Funnels · Loops · HEART · AARRR · Retention · Cohorts · Experiments')]
    s = SVG(700, 96 + len(rows) * 66, 'Where each framework belongs', 'Five areas of product development – and who mainly works there')
    for i, (c, area, who, items) in enumerate(rows):
        y = 80 + i * 66
        s.rect(28, y, 644, 56, c, c, 14)
        s.text(46, y + 24, area, 14, 800, WHITE if c != '#f2c94c' else NAVY)
        w = len(who) * 6.6 + 20; s.rect(652 - w, y + 10, w, 20, WHITE, WHITE, 10); s.text(652 - w / 2, y + 24, who, 10.5, 800, c if c != '#f2c94c' else WARN, 'middle')
        s.text(46, y + 44, items, 11, 600, WHITE if c != '#f2c94c' else NAVY)
    return s

@reg('vs-food-funnel')
def ffunnel():
    st = [('App Open', 10000), ('Restaurant Viewed', 7000), ('Food Added to Cart', 4000), ('Checkout Started', 2500), ('Payment Completed', 2000)]
    cols = ['#2f80ed', '#12b886', '#f2c94c', '#ff8a3d', '#eb5757']
    s = SVG(700, 120 + len(st) * 52, 'Food ordering conversion funnel', 'Illustrative data only – 20% of app opens become paid orders')
    for i, ((n, v), c) in enumerate(zip(st, cols)):
        y = 80 + i * 52; w = 180 + 420 * v / 10000; x = 350 - w / 2
        s.rect(x, y, w, 42, c, c, 10)
        s.text(350, y + 19, n, 12.5, 800, WHITE if c != '#f2c94c' else NAVY, 'middle')
        s.text(350, y + 35, f'{v:,} users · {v // 100}%', 11, 700, WHITE if c != '#f2c94c' else NAVY, 'middle')
    return s

@reg('vs-referral-loop')
def rloop():
    import math
    st = [('Existing user', '#ff8a3d'), ('Referral link', '#f2c94c'), ('New user', '#12b886'), ('First order', '#2f80ed'), ('Reward', '#7b5cff'), ('More referrals', '#eb5757')]
    s = SVG(640, 400, 'Food delivery referral loop', 'The result of one cycle starts the next – existing users bring new users')
    cx, cy, r = 320, 236, 120
    s.circle(cx, cy, r, 'none', LINE, 2.5, '7 6')
    s.circle(cx, cy, 52, NAVY, NAVY); s.text(cx, cy - 2, 'Loop', 15, 800, WHITE, 'middle'); s.text(cx, cy + 16, 'repeats', 11, 600, '#c9d0ea', 'middle')
    for i, (n, c) in enumerate(st):
        a = -math.pi / 2 + i * 2 * math.pi / 6
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        s.rect(x - 64, y - 20, 128, 40, c, c, 20); s.text(x - 46, y + 5, str(i + 1), 13, 800, WHITE if c != '#f2c94c' else NAVY, 'middle')
        s.text(x + 6, y + 5, n, 12, 800, WHITE if c != '#f2c94c' else NAVY, 'middle')
    return s

@reg('vs-double-diamond')
def ddiamond():
    s = SVG(700, 330, 'Double Diamond', 'Diverge → converge, twice: first the problem, then the solution')
    def dia(x0, c, l1, l2, title):
        s.path(f'M {x0} 190 L {x0+150} 100 L {x0+300} 190 L {x0+150} 280 Z', c, 2.5, fill=c + '22')
        s.path(f'M {x0+150} 100 L {x0+150} 280', c, 1.5, dash='4 4')
        s.text(x0 + 75, 196, l1, 14, 800, c, 'middle'); s.text(x0 + 225, 196, l2, 14, 800, c, 'middle')
        s.text(x0 + 150, 304, title, 12, 800, INK2, 'middle')
    dia(40, '#7b5cff', 'Discover', 'Define', 'Problem space')
    dia(360, '#12b886', 'Develop', 'Deliver', 'Solution space')
    s.rect(312, 170, 76, 40, '#ff8a3d', '#ff8a3d', 20); s.text(350, 195, 'HMW', 14, 800, WHITE, 'middle')
    s.text(190, 90, 'diverge · converge', 10.5, 700, INK3, 'middle'); s.text(510, 90, 'diverge · converge', 10.5, 700, INK3, 'middle')
    return s

@reg('vs-e2e-8steps')
def e2e():
    st = [('Product Strategy', 'PM', '#ff8a3d'), ('Discovery', 'PM + PD + UX', '#f2994a'), ('Define', 'PD + UX', '#f2c94c'), ('Ideation', 'PD + UX', '#6fcf97'),
          ('Experience Design', 'PD + UX', '#12b886'), ('Interface Design', 'PD + UI', '#2f80ed'), ('Prototype & Testing', 'PD + UX + UI', '#7b5cff'), ('Launch & Measurement', 'PM + PD + Team', '#eb5757')]
    s = SVG(700, 300, 'End-to-end product discovery & design', 'Food delivery app – new users download but don\'t place a first order')
    for i, (n, who, c) in enumerate(st):
        row, k = divmod(i, 4); k = k if row == 0 else 3 - k; x, y = 28 + k * 164, 82 + row * 104
        tc = WHITE if c not in ('#f2c94c', '#6fcf97') else NAVY
        s.rect(x, y, 152, 88, c, c, 14)
        s.circle(x + 24, y + 24, 14, WHITE, WHITE); s.text(x + 24, y + 29, str(i + 1), 12, 800, c, 'middle')
        s.wrap(x + 46, y + 28, 100, n, 12.5, 800, tc)
        s.text(x + 14, y + 76, who, 11, 700, tc)
        if row == 0 and k < 3: s.arrow(x + 153, y + 44, x + 163, y + 44, INK3)
        if row == 1 and k > 0: s.arrow(x - 1, y + 44, x - 11, y + 44, INK3)
    s.path('M 664 126 C 690 150, 690 160, 664 186', INK3, 1.5)
    return s

@reg('vs-prd-docs')
def prd_docs():
    cards = [('#ff8a3d', 'PRD', 'Product Manager', 'What needs to be built – and why'),
             ('#7b5cff', 'Design Specification', 'Product / UX / UI Designer', 'How the experience and interface should work'),
             ('#2f80ed', 'Technical Specification', 'Engineering', 'How the system will be implemented')]
    s = SVG(700, 250, 'Three documents, three questions', 'Separate documents – some companies combine them into one product document')
    for i, (c, name, who, q) in enumerate(cards):
        x = 28 + i * 220
        s.rect(x, 84, 204, 140, c, c, 16)
        s.text(x + 18, 114, name, 15, 800, WHITE)
        s.wrap(x + 18, 146, 172, q, 12.5, 700, WHITE)
        s.rect(x + 14, 190, 176, 24, WHITE, WHITE, 12); s.text(x + 102, 206, who, 10.5, 800, c, 'middle')
    return s

@reg('vs-prd-structure')
def prd_structure():
    groups = [('#ff8a3d', 'Why', ['Document Overview', 'Feature Overview', 'Problem Statement', 'Background & Context']),
              ('#f2c94c', 'Who & goals', ['Goals & Objectives', 'Target Users / Personas', 'User Needs & JTBD', 'Assumptions & Hypotheses']),
              ('#12b886', 'What', ['Proposed Solution', 'Scope – In / Out', 'User Stories', 'Functional Requirements']),
              ('#2f80ed', 'How it behaves', ['Business Rules', 'User Flow / UX', 'Non-Functional Req.', 'Edge Cases & Errors']),
              ('#7b5cff', 'Done & launch', ['Acceptance Criteria', 'Analytics & Metrics', 'Dependencies & Risks', 'Release Plan & Questions'])]
    s = SVG(700, 300, 'A feature PRD – 20 sections', 'Grouped into five parts')
    n = 1
    for i, (c, g, items) in enumerate(groups):
        x = 28 + i * 131; tc = WHITE if c != '#f2c94c' else NAVY
        s.rect(x, 80, 123, 34, c, c, 10); s.text(x + 61, 102, g, 12, 800, tc, 'middle')
        for j, it in enumerate(items):
            y = 122 + j * 42
            s.rect(x, y, 123, 36, WHITE, c, 9, 1.8)
            s.text(x + 10, y + 22, str(n), 11, 800, c if c != '#f2c94c' else WARN); s.wrap(x + 26, y + 15, 92, it, 9.8, 700, INK2)
            n += 1
    return s

@reg('vs-checkout-flow')
def checkout_flow():
    st = ['Cart', 'Checkout', 'Select Address', 'Review Order Summary', 'Select Payment Method', 'Confirm Order', 'Payment Processing', 'Payment Successful', 'Order Confirmation']
    cols = ['#2f80ed', '#2f80ed', '#12b886', '#12b886', '#7b5cff', '#7b5cff', '#ff8a3d', '#12b886', '#12b886']
    s = SVG(640, 110 + len(st) * 46, 'Simplified checkout – user flow', 'Happy path, plus what happens when payment fails')
    for i, (n, c) in enumerate(zip(st, cols)):
        y = 80 + i * 46
        s.rect(170, y, 220, 34, c, c, 17); s.text(280, y + 22, n, 12.5, 800, WHITE, 'middle')
        if i < len(st) - 1: s.arrow(280, y + 35, 280, y + 45, INK3)
    y = 80 + 6 * 46
    s.arrow(391, y + 17, 440, y + 17, '#eb5757' if False else WARN)
    s.rect(444, y - 4, 172, 42, WARN_S, WARN, 10, 1.6); s.text(530, y + 14, 'Payment failed', 11.5, 800, WARN, 'middle'); s.text(530, y + 30, 'Retry / another method', 10.5, 600, WARN, 'middle')
    s.path(f'M 530 {y - 5} C 530 {y - 70}, 460 {y - 92}, 392 {y - 92 + 17}', WARN, 1.5, dash='5 4')
    return s

@reg('vs-prd-workflow')
def prd_workflow():
    st = ['Understand the business request', 'Analyse data', 'Conduct discovery', 'Define the problem', 'Goals & success metrics',
          'Scope & requirements', 'Collaborate with design & engineering', 'Acceptance criteria', 'Review & approve', 'Monitor after launch']
    cols = ['#ff8a3d', '#f2994a', '#f2c94c', '#6fcf97', '#12b886', '#2d9cdb', '#2f80ed', '#7b5cff', '#bb6bd9', '#eb5757']
    s = SVG(700, 300, "PM's PRD writing workflow", 'Ten steps from business request to post-launch monitoring')
    for i, (n, c) in enumerate(zip(st, cols)):
        row, k = divmod(i, 5); k = k if row == 0 else 4 - k
        x, y = 28 + k * 132, 84 + row * 104
        tc = WHITE if c not in ('#f2c94c', '#6fcf97') else NAVY
        s.rect(x, y, 122, 86, c, c, 14)
        s.circle(x + 22, y + 22, 13, WHITE, WHITE); s.text(x + 22, y + 27, str(i + 1), 11.5, 800, c, 'middle')
        s.wrap(x + 12, y + 52, 102, n, 11, 800, tc)
        if row == 0 and k < 4: s.arrow(x + 123, y + 43, x + 131, y + 43, INK3)
        if row == 1 and k > 0: s.arrow(x - 1, y + 43, x - 9, y + 43, INK3)
    s.path('M 676 128 C 696 150, 696 168, 676 190', INK3, 1.5)
    return s

@reg('vs-prd-review')
def prd_review():
    areas = [('Problem', 'Is the real problem clear?', '#ff8a3d'), ('Research', 'Is there evidence for it?', '#f2994a'),
             ('Users', 'Are target users well defined?', '#f2c94c'), ('Requirements', 'Is every requirement clear?', '#6fcf97'),
             ('UX', 'Journey & flow needs covered?', '#12b886'), ('Edge cases', 'Skip, exit, return…?', '#2f80ed'),
             ('Metrics', 'How is success measured?', '#7b5cff'), ('Scope', 'What is in – and out?', '#eb5757')]
    s = SVG(700, 300, 'Review the PRD before opening Figma', 'Eight areas a Senior Product Designer checks in a PM\'s PRD draft')
    for i, (n, q, c) in enumerate(areas):
        row, k = divmod(i, 4); x, y = 28 + k * 164, 82 + row * 104
        tc = WHITE if c not in ('#f2c94c', '#6fcf97') else NAVY
        s.rect(x, y, 152, 90, c, c, 14)
        s.circle(x + 24, y + 26, 14, WHITE, WHITE); s.text(x + 24, y + 31, str(i + 1), 12, 800, c, 'middle')
        s.text(x + 46, y + 31, n, 14, 800, tc)
        s.wrap(x + 14, y + 62, 128, q, 11.5, 700, tc)
    return s

@reg('vs-assumption-types')
def as_types():
    cols = [('#ff8a3d', 'User & Behaviour', ['Identity', 'Motivation', 'Habits', 'Context']),
            ('#12b886', 'Usability & Design', ['Mental models', 'Friction', 'Accessibility']),
            ('#2f80ed', 'Value & Business', ['Desirability', 'Outcomes', 'Priority']),
            ('#7b5cff', 'Feasibility & Edge cases', ['Data & content', 'Failure states'])]
    s = SVG(700, 320, 'Four kinds of UX assumption', 'Check what you believe before you design – each kind has its own questions')
    for i, (c, name, items) in enumerate(cols):
        x = 28 + i * 164
        s.rect(x, 80, 152, 58, c, c, 14); s.wrap(x + 76, 104, 136, name, 13, 800, WHITE, 'middle')
        for j, it in enumerate(items):
            y = 148 + j * 40
            s.rect(x, y, 152, 32, WHITE, c, 16, 1.8); s.text(x + 76, y + 21, it, 12, 700, c, 'middle')
    return s

@reg('vs-assumption-matrix')
def as_matrix():
    s = SVG(640, 420, 'Assumption risk matrix', 'Importance vs evidence – illustrative examples for Classic Rummy')
    q = [(110, 84, '#eb5757', 'Validate immediately', 'High importance · Low evidence', "New users don't understand Rummy rules."),
         (370, 84, '#2f80ed', 'Monitor and act', 'High importance · High evidence', 'First-game abandonment is a major issue.'),
         (110, 238, '#f2c94c', 'Validate later', 'Low importance · Low evidence', 'Users may prefer a particular tutorial animation.'),
         (370, 238, '#12b886', 'No immediate action', 'Low importance · High evidence', 'Users understand the login screen.')]
    for x, y, c, act, lab, ex in q:
        tc = WHITE if c != '#f2c94c' else NAVY
        s.rect(x, y, 250, 144, c, c, 14)
        s.text(x + 16, y + 28, act, 15, 800, tc); s.text(x + 16, y + 48, lab, 10.5, 700, tc)
        s.wrap(x + 16, y + 80, 218, ex, 12, 600, tc)
    s.text(84, 160, 'High', 11, 800, INK2, 'end'); s.text(84, 314, 'Low', 11, 800, INK2, 'end')
    s.text(56, 237, 'Importance', 11, 800, INK3, 'middle')
    s.text(235, 404, 'Low evidence', 11, 800, INK2, 'middle'); s.text(495, 404, 'High evidence', 11, 800, INK2, 'middle')
    s.rect(110, 84, 250, 144, 'none', NAVY, 14, 3)
    return s

@reg('vs-assumption-research')
def as_research():
    st = [('Assumption', "New users don't understand the rules", '#ff8a3d'), ('Research question', 'What challenges do new users face?', '#f2994a'),
          ('Interview question', 'Describe the first time you played', '#f2c94c'), ('Usability task', 'Arrange these cards into valid sets', '#12b886'),
          ('Observation', 'Where do they hesitate or ask for help?', '#2f80ed'), ('Design decision', 'Full tutorial, hints, or simpler play?', '#7b5cff')]
    s = SVG(700, 300, 'From assumption to design decision', 'Turn a risky assumption into research – and let the findings decide the design')
    for i, (n, d, c) in enumerate(st):
        row, k = divmod(i, 3); k = k if row == 0 else 2 - k
        x, y = 28 + k * 220, 84 + row * 104
        tc = WHITE if c != '#f2c94c' else NAVY
        s.rect(x, y, 204, 86, c, c, 14)
        s.circle(x + 22, y + 22, 13, WHITE, WHITE); s.text(x + 22, y + 27, str(i + 1), 11.5, 800, c, 'middle')
        s.text(x + 44, y + 27, n, 13, 800, tc); s.wrap(x + 14, y + 56, 180, d, 11.5, 600, tc)
        if row == 0 and k < 2: s.arrow(x + 205, y + 43, x + 219, y + 43, INK3)
        if row == 1 and k > 0: s.arrow(x - 1, y + 43, x - 15, y + 43, INK3)
    s.path('M 672 128 C 694 150, 694 168, 672 190', INK3, 1.5)
    return s

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
