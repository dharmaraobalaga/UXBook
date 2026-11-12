from svgkit import *
import math

F = {}

def reg(key, alt, cap):
    def deco(fn):
        F[key] = (fn, alt, cap); return fn
    return deco

W = 760

@reg('ux-intro-2', 'Eight UX phases arranged as a repeating loop', 'The 8 UX phases form a loop – in Agile teams they overlap and repeat.')
def intro2():
    s = SVG(W, 560, 'End-to-end UX design lifecycle', 'Learning framework · phases overlap and repeat in real Agile teams')
    ph = [('1 Discovery & Research', 'Interviews · CSD · Empathy'), ('2 Define & Synthesize', 'Affinity · Persona · Journey'),
          ('3 Ideation & Strategy', 'Mind map · Kano · RICE'), ('4 IA & Interaction', 'Sitemap · User flow · HTA'),
          ('5 Wireframe & Prototype', 'Wireframes · Usability test'), ('6 Visual & Design System', 'Mood board · Style guide'),
          ('7 Handoff & Collaboration', 'Specs · RACI · Asset map'), ('8 Test, Measure, Improve', 'Report · Analytics · Roadmap')]
    cx, cy, R, RY = 380, 312, 262, 196
    s.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{R}" ry="{RY}" fill="none" stroke="{INDIGO_M}" stroke-width="2" stroke-dasharray="6 6"/>')
    fills = [INDIGO_S, INDIGO_S, HL_S, HL_S, OK_S, OK_S, TEAL_S, TEAL_S]
    for i, (a, b) in enumerate(ph):
        ang = -math.pi / 2 + i * 2 * math.pi / 8
        x = cx + R * math.cos(ang); y = cy + RY * math.sin(ang)
        s.box(x - 92, y - 33, 184, 66, a, b, fills[i], LINE, NAVY, 12.5, 700, 12, 10.5)
    s.circle(cx, cy, 62, NAVY, NAVY)
    s.text(cx, cy - 4, 'User + business', 13, 700, WHITE, 'middle')
    s.text(cx, cy + 14, 'at the centre', 12, 500, INDIGO_M, 'middle')
    return s

@reg('ux-intro-3', 'Four boxes: process, method, deliverable, artifact', 'Process = what we do · Method = how · Deliverable = the outcome · Artifact = the form it takes.')
def intro3():
    s = SVG(W, 300, 'What is a UX deliverable?', 'Four words that are often mixed up')
    items = [('UX Process', 'The activities we do', 'e.g. Research → Design → Test', INDIGO_S, INDIGO),
             ('UX Method', 'How we do an activity', 'e.g. User interviews, card sorting', HL_S, WARN),
             ('UX Deliverable', 'The outcome we produce', 'e.g. Persona, Journey map', OK_S, OK),
             ('UX Artifact', 'The form or work product', 'e.g. Figma file, PDF, poster', TEAL_S, TEAL)]
    for i, (t, a, b, f, c) in enumerate(items):
        x = 28 + i * 180
        s.rect(x, 88, 164, 170, f, c, 14, 1.4)
        s.text(x + 82, 122, t, 15, 700, c, 'middle')
        s.wrap(x + 82, 154, 140, a, 13, 600, INK, 'middle')
        s.wrap(x + 82, 210, 140, b, 11.5, 500, INK2, 'middle')
        if i < 3: s.arrow(x + 164, 173, x + 180, 173, INK3)
    return s

@reg('ux-1', 'Sticky notes from player interviews grouped into four themes', 'Many scattered comments become a few clear themes.')
def d1():
    s = SVG(W, 470, 'Affinity Diagram', 'Classic Rummy · 15 player interviews → themes')
    s.text(28, 96, 'Raw observations', 12, 700, INK3)
    raw = ['Cannot understand rules', 'Registration too long', 'How to arrange cards?', 'Where is my history?', 'Game disconnects', 'Slow loading']
    for i, t in enumerate(raw):
        sticky(s, 28 + (i % 2) * 112, 108 + (i // 2) * 74, t, HL_S, 102, 60, [-3, 2, 3, -2, -1, 3][i])
    s.arrow(262, 230, 300, 230, INDIGO, 2.2)
    themes = [('Onboarding', ['Registration too long', 'Unclear rules'], INDIGO_S, INDIGO),
              ('Gameplay', ['Card arrangement', 'Unclear actions'], OK_S, OK),
              ('Performance', ['Disconnections', 'Loading'], WARN_S, WARN),
              ('Wallet', ['Transaction history', 'Payment confusion'], TEAL_S, TEAL)]
    for i, (t, notes, f, c) in enumerate(themes):
        x = 312 + (i % 2) * 220; y = 86 + (i // 2) * 160
        s.rect(x, y, 206, 148, f, c, 12, 1.4)
        s.text(x + 14, y + 26, t, 14, 700, c)
        for j, n in enumerate(notes):
            sticky(s, x + 12 + j * 96, y + 46, n, WHITE, 88, 70)
    s.note(412, 'Insight: most pain is in onboarding and gameplay → design opportunities.')
    return s

@reg('ux-2', 'Row of screens and touchpoints from Play Store to wallet', 'Every screen across every channel, in order – check they feel consistent.')
def d2():
    s = SVG(W, 400, 'Asset Map', 'Classic Rummy · new-user journey across all touchpoints')
    steps = [('Play Store', 'Store'), ('Install', 'Store'), ('Welcome', 'App'), ('Mobile no.', 'App'), ('OTP', 'SMS'),
             ('KYC', 'App'), ('Lobby', 'App'), ('Table', 'App'), ('Gameplay', 'App'), ('Wallet', 'App')]
    ch = {'Store': (TEAL_S, TEAL), 'App': (INDIGO_S, INDIGO), 'SMS': (HL_S, WARN)}
    for i, (t, c) in enumerate(steps):
        x = 28 + (i % 5) * 144; y = 92 + (i // 5) * 140
        f, k = ch[c]
        s.rect(x, y, 112, 112, WHITE, k, 10, 1.4)
        s.rect(x, y, 112, 26, f, k, 10, 1.4); s.rect(x, y + 14, 112, 12, f, f, 0, 0)
        s.text(x + 56, y + 18, c, 11, 700, k, 'middle')
        for r in range(3): s.rect(x + 14, y + 40 + r * 14, 84 - r * 20, 7, PAPER2, PAPER2, 3)
        s.text(x + 56, y + 100, f'{i+1}. {t}', 12, 700, NAVY, 'middle')
        if i % 5 != 4: s.arrow(x + 114, y + 56, x + 142, y + 56, INK3)
    s.note(352, 'Check: do colours, words and buttons stay consistent from Store to Wallet?')
    return s

@reg('ux-3', 'Concept map with Online Rummy Platform at the centre and labelled links', 'Concepts connected by labelled arrows show how the system fits together.')
def d3():
    s = SVG(W, 470, 'Concept Map', 'Classic Rummy · how the main concepts relate')
    cx, cy = 380, 262
    s.box(cx - 90, cy - 30, 180, 60, 'Online Rummy Platform', None, NAVY, NAVY, WHITE, 14, 700, 30)
    nodes = [('User Account', 'Registration · Login · Profile', 'has', 130, 120), ('Gameplay', 'Tables · Cards · Sequences · Sets', 'offers', 630, 120),
             ('Wallet', 'Deposit · Withdrawal · Transactions', 'uses', 130, 400), ('Support', 'Help centre · FAQs · Complaints', 'provides', 630, 400),
             ('Rewards', 'Bonuses · Loyalty · Offers', 'gives', 380, 110)]
    def edge(dx, dy, hw, hh):
        k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9); return dx * k, dy * k
    for t, b, lab, x, y in nodes:
        s.box(x - 110, y - 30, 220, 60, t, b, WHITE, INDIGO_M, NAVY, 13.5, 700, 12, 10.5)
    for t, b, lab, x, y in nodes:
        dx, dy = x - cx, y - cy
        ex, ey = edge(dx, dy, 90, 30); x1, y1 = cx + ex, cy + ey
        ex, ey = edge(-dx, -dy, 114, 34); x2, y2 = x + ex, y + ey
        s.arrow(x1, y1, x2, y2, INDIGO, 1.6)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s.rect(mx - 32, my - 12, 64, 22, PAPER, PAPER, 6); s.text(mx, my + 4, lab, 11.5, 600, INDIGO, 'middle', True)
    return s

@reg('ux-4', 'Three columns: certainties, suppositions, doubts', 'Separate what we know, what we assume and what we must find out.')
def d4():
    s = SVG(W, 400, 'CSD Matrix', 'Classic Rummy · Certainties, Suppositions and Doubts')
    cols = [('C', 'Certainties', 'What we know', ['Users must register to access an account', 'Most players use mobile'], OK_S, OK),
            ('S', 'Suppositions', 'What we assume', ['New users find card grouping difficult', 'Users want quick tables'], HL_S, WARN),
            ('D', 'Doubts', 'What we must find out', ['Why do users leave during onboarding?', 'Do rules feel too long?'], WARN_S, WARN)]
    for i, (L, t, sub, items, f, c) in enumerate(cols):
        x = 28 + i * 240
        s.rect(x, 86, 224, 250, f, c, 14, 1.4)
        s.circle(x + 34, 120, 20, c, c); s.text(x + 34, 126, L, 16, 800, WHITE, 'middle')
        s.text(x + 64, 118, t, 15, 700, c); s.text(x + 64, 136, sub, 11.5, 500, INK2)
        for j, it in enumerate(items):
            s.box(x + 14, 160 + j * 82, 196, 70, it, None, WHITE, LINE, INK, 12, 500, 8)
    s.arrow(510, 360, 690, 360, WARN, 1.6); s.text(500, 365, 'Doubts become research questions', 12, 600, WARN, 'end')
    return s

@reg('ux-5', 'Design system layers: tokens, components, patterns, screens', 'Small shared parts build every screen the same way.')
def d5():
    s = SVG(W, 440, 'Design System', 'Classic Rummy · 50+ screens built from shared parts')
    layers = [('Tokens', 'colour · type · spacing · radius', INDIGO_S, INDIGO), ('Components', 'button · card · input · chip', OK_S, OK),
              ('Patterns', 'wallet form · table list · OTP step', HL_S, WARN), ('Screens', 'lobby · gameplay · wallet', TEAL_S, TEAL)]
    for i, (t, b, f, c) in enumerate(layers):
        y = 300 - i * 66; w = 300 - i * 50; x = 40 + (300 - w) / 2 + i * 0
        x = 190 - w / 2 + 20
        s.box(x, y, w, 58, t, b, f, c, c, 14, 700, 10, 11)
    # sample tokens/components on right
    s.text(420, 100, 'Tokens', 12, 700, INK3)
    for i, col in enumerate([NAVY, INDIGO, OK, HL, WARN]): s.rect(420 + i * 54, 110, 44, 44, col, col, 8)
    s.text(420, 190, 'Aa  Heading 24 / Body 15 / Caption 12', 13, 600, NAVY)
    s.text(420, 232, 'Components', 12, 700, INK3)
    s.rect(420, 244, 120, 40, NAVY, NAVY, 20); s.text(480, 269, 'Play now', 13, 700, WHITE, 'middle')
    s.rect(552, 244, 120, 40, WHITE, NAVY, 20); s.text(612, 269, 'Add cash', 13, 700, NAVY, 'middle')
    s.rect(420, 298, 252, 70, WHITE, LINE, 12); s.text(436, 322, 'Points Rummy · 2 players', 12.5, 700, NAVY)
    s.text(436, 344, 'Entry ₹10 · Prize ₹18', 11.5, 500, INK2); s.rect(604, 320, 54, 26, OK_S, OK, 13); s.text(631, 337, 'Join', 11.5, 700, OK, 'middle')
    s.note(390, 'Same button, card and type everywhere → consistent UI and faster development.')
    return s

@reg('ux-6', 'Concentric rings of people, products, services and channels around a player', 'The player sits inside a wider ecosystem – a failure anywhere feels like the game’s fault.')
def d6():
    s = SVG(W, 560, 'Ecosystem Map', 'Classic Rummy · everything around a player')
    cx, cy = 380, 312
    for r, f in [(232, TEAL_S), (166, HL_S), (100, INDIGO_S)]: s.circle(cx, cy, r, f, LINE)
    s.circle(cx, cy, 44, NAVY, NAVY); s.text(cx, cy + 5, 'Player', 14, 700, WHITE, 'middle')
    s.text(cx, cy - 82, 'PEOPLE', 11, 800, INDIGO, 'middle')
    s.text(cx, cy - 134, 'PRODUCTS', 11, 800, WARN, 'middle')
    s.text(cx, cy - 202, 'SERVICES & CHANNELS', 11, 800, TEAL, 'middle')
    tags = [('Friends', 76, 212, INDIGO), ('Other players', 76, 328, INDIGO), ('Support agent', 74, 90, INDIGO),
            ('Rummy app', 134, 145, WARN), ('Play Store', 134, 35, WARN), ('Phone', 134, 90, WARN),
            ('UPI / Bank', 200, 205, TEAL), ('OTP SMS', 200, 335, TEAL), ('KYC service', 200, 178, TEAL), ('Push / Email', 200, 2, TEAL), ('Payment gateway', 200, 125, TEAL), ('Social media', 200, 55, TEAL)]
    for t, r, a, c in tags:
        a = math.radians(a); x = cx + r * math.cos(a); y = cy + r * math.sin(a)
        w = len(t) * 6.6 + 18; s.rect(x - w / 2, y - 11, w, 22, WHITE, c, 11); s.text(x, y + 4, t, 11, 600, c, 'middle')
    return s

@reg('ux-7', 'Empathy map with Says, Thinks, Does and Feels quadrants around a new player', 'What a first-time player says, thinks, does and feels.')
def d7():
    s = SVG(W, 440, 'Empathy Map', 'Classic Rummy · a first-time player')
    q = [('SAYS', '“I don’t know if I’m playing correctly.”', INDIGO_S, INDIGO), ('THINKS', '“Will I lose money because I don’t understand the rules?”', HL_S, WARN),
         ('DOES', 'Watches others play, avoids cash tables, opens Help', OK_S, OK), ('FEELS', 'Curious but nervous; worried about mistakes', PINK_S, PINK)]
    for i, (t, b, f, c) in enumerate(q):
        x = 28 + (i % 2) * 356; y = 80 + (i // 2) * 170
        s.rect(x, y, 348, 162, f, c, 14, 1.4)
        tx = x + 18 if i % 2 == 0 else x + 70
        s.text(tx, y + 30, t, 14, 800, c)
        s.wrap(tx, y + 64, 250, b, 14, 500, INK)
    s.circle(380, 250, 46, WHITE, NAVY, 2)
    s.circle(380, 238, 13, NAVY, NAVY); s.path('M 358 274 Q 380 248 402 274', NAVY, 3)
    s.rect(338, 300, 84, 22, NAVY, NAVY, 11); s.text(380, 315, 'New player', 11.5, 700, WHITE, 'middle')
    return s

@reg('ux-8', 'Experience map with five phases and an emotion curve', 'The broader experience of card games – not just our app.')
def d8():
    s = SVG(W, 420, 'Experience Map', 'Card games as entertainment (not specific to Classic Rummy)')
    ph = ['Hear about it', 'Learn rules', 'Practise', 'Play regularly', 'Share with friends']
    em = [0.55, 0.25, 0.5, 0.85, 0.9]
    for i, p in enumerate(ph):
        x = 28 + i * 142
        s.box(x, 84, 134, 44, p, None, INDIGO_S, INDIGO_M, NAVY, 13, 700, 8)
    s.rect(28, 140, 704, 170, WHITE, LINE, 12)
    s.text(40, 160, '😊', 14); s.text(40, 300, '😟', 14)
    s.line(60, 225, 720, 225, PAPER2, 1, '4 4')
    pts = [(95 + i * 142, 300 - e * 140) for i, e in enumerate(em)]
    d = 'M ' + ' '.join(f'{x},{y}' for x, y in pts)
    s.path('M ' + ' S '.join([f'{pts[0][0]},{pts[0][1]}'] + [f'{x-50},{y} {x},{y}' for x, y in pts[1:]]), INDIGO, 2.6)
    for x, y in pts: s.circle(x, y, 6, INDIGO, WHITE, 2)
    s.text(237, 284, 'confusing alone', 11.5, 600, WARN, 'middle')
    s.note(328, 'Opportunity: people learn best with someone they trust → practice tables, play with friends.')
    return s

@reg('ux-9', 'Scorecard table rating four ideas on desirability, feasibility and viability', 'Score each idea on three lenses; highest totals go first.')
def d9():
    s = SVG(W, 380, 'Feasibility · Desirability · Viability Scorecard', 'Classic Rummy · illustrative scores out of 10')
    rows = [('Interactive tutorial', 9, 7, 8), ('Practice table', 8, 9, 7), ('Custom card themes', 6, 8, 5), ('Voice chat at tables', 5, 3, 4)]
    hd = ['Idea', 'Desirability', 'Feasibility', 'Viability', 'Total']; xs = [28, 260, 380, 500, 620]
    s.rect(28, 84, 704, 40, NAVY, NAVY, 10)
    for h, x in zip(hd, xs): s.text(x + (12 if h == 'Idea' else 50), 109, h, 12.5, 700, WHITE, 'start' if h == 'Idea' else 'middle')
    for r, (n, a, b, c) in enumerate(rows):
        y = 132 + r * 50; tot = a + b + c; top = tot >= 24
        s.rect(28, y, 704, 44, OK_S if top else WHITE, OK if top else LINE, 8)
        s.text(40, y + 27, n, 13, 600, INK)
        for v, x in zip((a, b, c), xs[1:4]):
            s.rect(x + 10, y + 16, 80, 12, PAPER2, PAPER2, 6); s.rect(x + 10, y + 16, 8 * v, 12, INDIGO, INDIGO, 6)
            s.text(x + 100, y + 27, str(v), 12, 700, INK2)
        s.text(670, y + 28, str(tot), 15, 800, OK if top else INK2, 'middle')
    s.note(336, 'Tutorial and practice table score highest → strong candidates for the next release.')
    return s

@reg('ux-10', 'Task tree: join a cash game broken into sub-tasks', 'A goal broken into tasks and sub-tasks reveals how many steps a player needs.')
def d10():
    s = SVG(W, 430, 'HTA – Hierarchical Task Analysis', 'Classic Rummy · goal: join a cash game')
    s.box(280, 80, 200, 46, '0. Join a cash game', None, NAVY, NAVY, WHITE, 14, 700)
    tasks = [('1. Log in', ['1.1 Mobile number', '1.2 Enter OTP']), ('2. Add money', ['2.1 Choose amount', '2.2 Payment method', '2.3 Confirm']),
             ('3. Choose a game', ['3.1 Game type', '3.2 Table & fee']), ('4. Join the table', [])]
    for i, (t, subs) in enumerate(tasks):
        x = 28 + i * 180
        s.path(f'M 380 126 L 380 150 L {x+80} 150 L {x+80} 166', INK3, 1.4)
        s.box(x, 166, 160, 42, t, None, INDIGO_S, INDIGO, NAVY, 13, 700)
        for j, st in enumerate(subs):
            y = 228 + j * 46
            s.path(f'M {x+16} 208 L {x+16} {y+19} L {x+28} {y+19}', INK3, 1.2)
            s.box(x + 28, y, 132, 38, st, None, WHITE, LINE, INK, 11.5, 500, 8)
    s.note(380, '4 tasks + 7 sub-tasks before the first game → opportunity to simplify.')
    return s

@reg('ux-11', '2x2 matrix of impact versus effort with four Rummy ideas', 'Do quick wins first, plan big bets, avoid the money pit.')
def d11():
    s = SVG(W, 470, 'Impact–Effort Matrix', 'Classic Rummy · illustrative ideas')
    x0, y0, w, h = 110, 84, 600, 330
    q = [('Quick Wins', 'Clearer OTP error messages', OK_S, OK), ('Big Bets', 'Interactive tutorial + practice game', INDIGO_S, INDIGO),
         ('Fill-ins', 'New avatar options', PAPER2, INK2), ('Money Pit', 'Fully custom 3D table environments', WARN_S, WARN)]
    for i, (t, b, f, c) in enumerate(q):
        x = x0 + (i % 2) * w / 2; y = y0 + (i // 2) * h / 2
        s.rect(x + 3, y + 3, w / 2 - 6, h / 2 - 6, f, c, 12, 1.2)
        s.text(x + 20, y + 32, t, 15, 800, c)
        s.wrap(x + 20, y + 70, 240, b, 13, 600, INK)
    s.arrow(x0 - 16, y0 + h, x0 - 16, y0, INK2, 1.8); s.arrow(x0, y0 + h + 16, x0 + w, y0 + h + 16, INK2, 1.8)
    s.add(f'<text x="{x0-30}" y="{y0+h/2}" font-size="12" font-weight="700" fill="{INK2}" text-anchor="middle" transform="rotate(-90 {x0-30} {y0+h/2})">IMPACT</text>')
    s.text(x0 + w / 2, y0 + h + 40, 'EFFORT →', 12, 700, INK2, 'middle')
    s.text(x0 - 24, y0 + h + 4, 'low', 10, 500, INK3, 'end'); s.text(x0 - 24, y0 + 8, 'high', 10, 500, INK3, 'end')
    return s

@reg('ux-12', 'Journey map with phases, actions, emotion curve and pain points', 'A new player’s first game, phase by phase, with emotions and pain points.')
def d12():
    s = SVG(W, 500, 'Journey Map', 'Classic Rummy · new player · goal: play the first game')
    ph = [('Discover', 'Sees ad, installs', 'Curious', 'Is the app trustworthy?', 0.6), ('Register', 'Mobile no. + OTP', 'Impatient', 'OTP delay', 0.3),
          ('Learn', 'Reads rules', 'Confused', 'Too much text', 0.15), ('Play', 'Practice table', 'Nervous', 'Unclear card actions', 0.4), ('Return', 'Gets notification', 'Interested', 'Generic message', 0.7)]
    s.text(28, 112, 'PHASE', 10.5, 800, INK3); s.text(28, 160, 'ACTION', 10.5, 800, INK3); s.text(28, 228, 'EMOTION', 10.5, 800, INK3); s.text(28, 386, 'PAIN', 10.5, 800, INK3)
    pts = []
    s.rect(100, 196, 632, 150, WHITE, LINE, 10)
    for i, (p, a, e, pain, v) in enumerate(ph):
        x = 100 + i * 128
        s.box(x, 88, 120, 36, p, None, NAVY, NAVY, WHITE, 13, 700, 8)
        s.box(x, 136, 120, 44, a, None, WHITE, LINE, INK, 11.5, 500, 8)
        y = 330 - v * 130; pts.append((x + 60, y))
        s.text(x + 60, y - 14, e, 11.5, 700, INDIGO, 'middle')
        s.box(x, 360, 120, 52, pain, None, WARN_S, WARN, WARN, 11.5, 600, 8)
    s.path('M ' + ' S '.join([f'{pts[0][0]},{pts[0][1]}'] + [f'{x-45},{y} {x},{y}' for x, y in pts[1:]]), INDIGO, 2.6)
    for x, y in pts: s.circle(x, y, 6, INDIGO, WHITE, 2)
    s.note(436, 'Lowest point = “Learn” → biggest opportunity: shorter, interactive rules.')
    return s
