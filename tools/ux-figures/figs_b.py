from svgkit import *
import math

F = {}
def reg(key, alt, cap):
    def deco(fn):
        F[key] = (fn, alt, cap); return fn
    return deco
W = 760


@reg('ux-13', 'Kano model chart with must-be, performance and attractive curves', 'How satisfaction changes as each type of feature is delivered.')
def d13():
    s = SVG(W, 470, 'Kano Model', 'Classic Rummy · how features affect satisfaction')
    x0, y0, w, h = 90, 84, 400, 330; cx, cy = x0 + w / 2, y0 + h / 2
    s.rect(x0, y0, w, h, WHITE, LINE, 10)
    s.arrow(x0 + 10, cy, x0 + w - 6, cy, INK2); s.arrow(cx, y0 + h - 6, cx, y0 + 8, INK2)
    s.text(cx + 6, y0 + 22, 'Satisfied', 11, 600, INK3); s.text(cx + 6, y0 + h - 10, 'Dissatisfied', 11, 600, INK3)
    s.text(x0 + w, y0 + h + 18, 'Feature fully delivered →', 11, 600, INK3, 'end'); s.text(x0, y0 + h + 18, '← Feature absent', 11, 600, INK3)
    s.path(f'M {x0+20} {y0+h-20} L {x0+w-20} {y0+30}', INDIGO, 3)
    s.path(f'M {x0+20} {y0+h-14} Q {cx-30} {cy+14} {x0+w-20} {cy+8}', WARN, 3)
    s.path(f'M {x0+20} {cy-10} Q {cx+90} {cy-14} {x0+w-20} {y0+16}', OK, 3)
    s.line(x0 + 20, cy - 3, x0 + w - 20, cy - 3, INK3, 2, '6 5')
    leg = [('Must-be', 'Secure login, fair gameplay, reliable withdrawals', WARN, WARN_S), ('Performance', 'Fast table loading, quick withdrawals', INDIGO, INDIGO_S),
           ('Attractive', 'Personalised tips after a game', OK, OK_S), ('Indifferent', 'Changing the lobby background colour', INK3, PAPER2)]
    for i, (t, b, c, f) in enumerate(leg):
        y = 84 + i * 84
        s.rect(512, y, 220, 74, f, c, 10)
        s.rect(524, y + 14, 18, 5, c, c, 2); s.text(550, y + 21, t, 13.5, 700, c)
        s.wrap(524, y + 44, 196, b, 11.5, 500, INK)
    return s


@reg('ux-14', 'Landscape map positioning game categories on two axes', 'See where Classic Rummy sits in the market and which patterns users expect.')
def d14():
    s = SVG(W, 470, 'Landscape Map', 'Card-gaming landscape · illustrative')
    x0, y0, w, h = 70, 92, 390, 320; cx, cy = x0 + w / 2, y0 + h / 2
    s.rect(x0, y0, w, h, WHITE, LINE, 10)
    s.line(x0, cy, x0 + w, cy, LINE, 1.4); s.line(cx, y0, cx, y0 + h, LINE, 1.4)
    s.text(cx, y0 - 8, 'Skill / competitive', 11.5, 700, INK2, 'middle'); s.text(cx, y0 + h + 18, 'Casual / relaxed', 11.5, 700, INK2, 'middle')
    s.text(x0 - 6, cy + 4, 'Solo', 11.5, 700, INK2, 'end'); s.text(x0 + w + 6, cy + 4, 'Social', 11.5, 700, INK2)
    bub = [('Skill tournaments', cx - 90, y0 + 70, 46, INDIGO_S, INDIGO), ('Classic card games', cx + 20, cy - 30, 54, OK_S, OK),
           ('Social casual games', cx + 120, cy + 90, 50, HL_S, WARN), ('Solitaire', cx - 130, cy + 100, 34, PAPER2, INK2)]
    for t, x, y, r, f, c in bub:
        s.circle(x, y, r, f, c, 1.4)
        s.wrap(x, y - 2, r * 1.6, t, 11.5, 700, c, 'middle')
    s.circle(cx + 70, cy - 60, 9, NAVY, NAVY); s.text(cx + 84, cy - 56, 'Classic Rummy', 12, 800, NAVY)
    pats = [('Classic card games', 'Tutorials for new users'), ('Skill tournaments', 'Clear rules & prize info'), ('Social casual', 'Invites & chat drive retention')]
    s.text(540, 100, 'Patterns noticed', 13, 700, NAVY)
    for i, (a, b) in enumerate(pats):
        s.box(540, 114 + i * 84, 192, 72, a, b, WHITE, LINE, NAVY, 12.5, 700, 10, 11.5)
    return s


@reg('ux-15', 'Mind map with central topic and four branches of ideas', 'Branch out from one topic to explore many ideas quickly.')
def d15():
    s = SVG(W, 470, 'Mind Map', 'Classic Rummy · improve first-time gameplay')
    cx, cy = 380, 268
    br = [('Learning', ['Interactive tutorial', 'Practice game', 'Rule cards'], 200, INDIGO, INDIGO_S, -1, -1),
          ('Guidance', ['Contextual tooltips', 'Highlighted valid moves'], 340, OK, OK_S, 1, -1),
          ('Confidence', ['Low-stake tables', 'No-money practice'], 160, WARN, HL_S, -1, 1),
          ('Support', ['Help centre', 'Chat support'], 20, TEAL, TEAL_S, 1, 1)]
    for t, leaves, ang, c, f, sx, sy in br:
        bx = cx + sx * 150; by = cy + sy * 104
        s.path(f'M {cx} {cy} Q {cx + sx*90} {cy} {bx} {by}', c, 4)
        for j, l in enumerate(leaves):
            lx = bx + sx * 132; ly = by + (j - (len(leaves) - 1) / 2) * 44
            s.path(f'M {bx} {by} Q {bx + sx*60} {by} {lx - sx*68} {ly}', c, 1.8)
            s.box(lx - 68, ly - 17, 136, 34, l, None, WHITE, c, INK, 11.5, 600, 17)
        s.box(bx - 60, by - 20, 120, 40, t, None, f, c, c, 13.5, 800, 20, sw=1.8)
    s.box(cx - 92, cy - 34, 184, 68, 'Improve first-time gameplay', None, NAVY, NAVY, WHITE, 14, 700, 34)
    return s


@reg('ux-16', 'Phone mockup of a Rummy lobby with real colours and content', 'A mockup shows the final look – colours, type, real content – but does not click.')
def d16():
    s = SVG(W, 470, 'Mockup', 'Classic Rummy · lobby in final visual style (static)')
    x, y, w, h = phone(s, 60, 84, 210, 370, '#0f3d2e', NAVY)
    s.rect(x, y, w, 40, '#0b2e22', '#0b2e22', 8); s.text(x + 10, y + 25, 'Classic Rummy', 13, 800, '#f2c75c')
    s.rect(x + w - 74, y + 10, 66, 22, '#f2c75c', '#f2c75c', 11); s.text(x + w - 41, y + 25, '₹ 250', 11.5, 800, '#0b2e22', 'middle')
    s.rect(x, y + 50, w, 62, '#f2c75c', '#f2c75c', 10); s.text(x + 12, y + 76, 'Festive offer', 13, 800, '#0b2e22'); s.text(x + 12, y + 96, '100% bonus on first add', 11, 600, '#0b2e22')
    games = [('Points Rummy', '₹10 entry'), ('Pool Rummy', '₹25 entry'), ('Deals Rummy', '₹50 entry')]
    for i, (g, e) in enumerate(games):
        yy = y + 124 + i * 62
        s.rect(x, yy, w, 54, '#14513d', '#1d6b51', 10)
        s.text(x + 12, yy + 23, g, 12.5, 700, WHITE); s.text(x + 12, yy + 41, e, 11, 500, '#bfe3d2')
        s.rect(x + w - 58, yy + 15, 48, 24, '#f2c75c', '#f2c75c', 12); s.text(x + w - 34, yy + 31, 'Play', 11.5, 800, '#0b2e22', 'middle')
    s.rect(x, y + h - 36, w, 36, '#0b2e22', '#0b2e22', 8)
    for i, t in enumerate(['Lobby', 'Wallet', 'Offers', 'Me']): s.text(x + 22 + i * 50, y + h - 13, t, 10.5, 600, '#bfe3d2' if i else '#f2c75c', 'middle')
    notes = [('Final brand colours', 'Deep green + gold'), ('Final typography', 'Real sizes and weights'), ('Real content', 'Game types, entry fees, balance'),
             ('Final icons & banners', 'Offer banner, bottom nav'), ('Not interactive', 'Review the look, then prototype')]
    for i, (a, b) in enumerate(notes):
        yy = 100 + i * 70
        s.circle(330, yy + 20, 13, HL, HL_L); s.text(330, yy + 25, str(i + 1), 12, 800, NAVY, 'middle')
        s.text(356, yy + 18, a, 14, 700, NAVY); s.text(356, yy + 38, b, 12, 500, INK2)
    return s


@reg('ux-17', 'Mood board with colour swatches, textures, type and feeling words', 'Collect colours, imagery and type to agree on a visual direction.')
def d17():
    s = SVG(W, 440, 'Mood Board', 'Classic Rummy refresh · premium, trustworthy, festive')
    s.rect(28, 84, 260, 190, '#0f3d2e', '#0f3d2e', 12)
    for i in range(5):
        s.add(f'<g transform="rotate({-20 + i*10} {158} {250})"><rect x="138" y="{120}" width="44" height="64" rx="5" fill="#fff" stroke="#d4ccb8"/><text x="146" y="138" font-size="13" font-weight="800" fill="{["#a3365f","#1f2328"][i%2]}">{["A","K","Q","J","10"][i]}</text></g>')
    s.text(40, 264, 'Card-table green', 11.5, 700, '#f2c75c')
    s.rect(300, 84, 200, 92, '#f2c75c', '#f2c75c', 12); s.text(316, 160, 'Warm gold accents', 12, 700, '#0b2e22')
    s.add('<circle cx="350" cy="118" r="18" fill="#fff5d1"/><circle cx="420" cy="110" r="10" fill="#fff5d1"/><circle cx="460" cy="130" r="14" fill="#fff5d1"/>')
    s.rect(300, 186, 200, 88, '#2a1f14', '#2a1f14', 12)
    for i in range(7): s.circle(320 + i * 27, 214 + (i % 2) * 18, 6, '#f2c75c', '#f2c75c')
    s.text(316, 264, 'Celebration lights', 12, 700, '#f2c75c')
    s.rect(512, 84, 220, 190, WHITE, LINE, 12)
    s.text(528, 128, 'Aa', 40, 800, NAVY); s.text(528, 160, 'Clear and modern', 14, 700, NAVY); s.text(528, 182, 'Readable on small screens', 12, 500, INK2)
    s.text(528, 220, 'Heading · Body · Caption', 12, 600, INK3)
    pal = ['#0f3d2e', '#14513d', '#f2c75c', '#fff5d1', '#a3365f', '#1f2328']
    for i, c in enumerate(pal): s.rect(28 + i * 60, 290, 52, 52, c, LINE, 8)
    s.text(28, 362, 'Palette', 11.5, 700, INK3)
    words = ['Premium', 'Trustworthy', 'Festive', 'Soft lighting']
    xpos, ypos = 400, 292
    for wd in words:
        wpx = len(wd) * 12.5 * CW + 18
        if xpos + wpx > 732: xpos, ypos = 400, ypos + 34
        s.pill(xpos, ypos, wd, INDIGO_S, INDIGO, 12.5); xpos += wpx + 8
    s.note(384, 'The board aligns the team on feeling and direction before any screen is designed.')
    return s


@reg('ux-18', 'Four MoSCoW columns with onboarding features', 'Must, Should, Could and Won’t (now) – agree on scope for a release.')
def d18():
    s = SVG(W, 392, 'MoSCoW Analysis', 'Classic Rummy · release: improved onboarding')
    cols = [('M', 'Must have', ['Simplified registration', 'Clear game rules'], OK_S, OK), ('S', 'Should have', ['Contextual help in first game'], INDIGO_S, INDIGO),
            ('C', 'Could have', ['Avatar customisation'], HL_S, WARN), ('W', "Won't have (now)", ['Voice chat at tables'], PAPER2, INK2)]
    for i, (L, t, items, f, c) in enumerate(cols):
        x = 28 + i * 178
        s.rect(x, 84, 168, 260, f, c, 14, 1.4)
        s.text(x + 84, 130, L, 34, 800, c, 'middle'); s.text(x + 84, 156, t, 13.5, 700, c, 'middle')
        for j, it in enumerate(items):
            s.box(x + 12, 176 + j * 70, 144, 58, it, None, WHITE, LINE, INK, 12, 600, 8)
    s.arrow(40, 372, 720, 372, INK3); s.text(380, 362, 'priority decreases', 11, 600, INK3, 'middle')
    return s


@reg('ux-19', 'Persona card for Ravi, a beginner player', 'A research-based character that represents a user segment.')
def d19():
    s = SVG(W, 420, 'Persona', 'Classic Rummy · Ravi, beginner player (illustrative)')
    s.rect(28, 84, 704, 310, WHITE, LINE, 16)
    s.rect(28, 84, 220, 310, INDIGO_S, INDIGO_S, 16); s.rect(232, 84, 16, 310, INDIGO_S, INDIGO_S, 0)
    s.circle(138, 160, 48, WHITE, INDIGO, 2); s.circle(138, 146, 17, INDIGO, INDIGO); s.path('M 108 194 Q 138 160 168 194', INDIGO, 4)
    s.text(138, 238, 'Ravi', 20, 800, NAVY, 'middle'); s.text(138, 260, 'Beginner player', 12.5, 600, INDIGO, 'middle')
    s.wrap(138, 296, 180, '28 · works in sales · plays in short breaks', 12, 500, INK2, 'middle')
    s.box(52, 340, 172, 36, '“I just want to learn fast.”', None, WHITE, INDIGO_M, INDIGO, 11.5, 600, 18)
    blocks = [('Goals', 'Learn the game quickly, play for fun', OK), ('Needs', 'Simple rules, low-risk practice', INDIGO),
              ('Behaviours', 'Plays on mobile in 10-minute sessions', TEAL), ('Challenges', 'Confused by card grouping; worried about losing money', WARN)]
    for i, (t, b, c) in enumerate(blocks):
        x = 268 + (i % 2) * 232; y = 104 + (i // 2) * 140
        s.rect(x, y, 3, 110, c, c, 1)
        s.text(x + 14, y + 18, t.upper(), 11.5, 800, c)
        s.wrap(x + 14, y + 44, 196, b, 14, 600, INK)
    return s


@reg('ux-20', 'Fidelity spectrum from paper sketch to interactive prototype, with linked screens', 'Prototypes let users try the flow before any code is written.')
def d20():
    s = SVG(W, 440, 'Prototype', 'Classic Rummy · interactive onboarding prototype')
    scr = ['Welcome', 'Mobile no.', 'OTP', 'Practice game']
    for i, t in enumerate(scr):
        x, y, w, h = phone(s, 40 + i * 180, 84, 130, 200)
        s.rect(x, y, w, 22, INDIGO_S, INDIGO_S, 4); s.text(x + w / 2, y + 15, t, 11, 700, INDIGO, 'middle')
        for r in range(3): s.rect(x + 8, y + 36 + r * 18, w - 16 - r * 20, 9, PAPER2, PAPER2, 4)
        s.rect(x + 8, y + h - 34, w - 16, 26, NAVY, NAVY, 13); s.text(x + w / 2, y + h - 17, 'Tap', 11, 700, WHITE, 'middle')
        if i < 3:
            s.path(f'M {x+w/2+30} {y+h-21} C {x+w+40} {y+h+20}, {x+w+70} {y+h-60}, {x+w+44} {y+100}', OK, 2)
            s.add(f'<circle cx="{x+w/2+30}" cy="{y+h-21}" r="7" fill="{OK}" opacity=".35"/>')
    s.text(40 + 2 * 180 + 65, 304, 'Wrong OTP → error state', 11.5, 700, WARN, 'middle')
    s.text(28, 336, 'FIDELITY', 11, 800, INK3)
    st = [('Paper', PAPER2), ('Clickable wireframe', INDIGO_S), ('Hi-fi interactive', OK_S), ('Coded', TEAL_S)]
    for i, (t, f) in enumerate(st): s.box(28 + i * 178, 346, 170, 34, t, None, f, LINE, NAVY, 12, 700, 17)
    s.note(392, '5 new players try it → the team sees where they hesitate, before development.')
    return s


@reg('ux-21', 'RACI matrix grid with R, A, C, I letters per role', 'Who is Responsible, Accountable, Consulted and Informed for each task.')
def d21():
    s = SVG(W, 430, 'RACI Matrix', 'Classic Rummy · design project roles')
    roles = ['UX Designer', 'Product Mgr', 'Engineering', 'QA']
    rows = [('User research', 'R A C I'), ('Wireframes', 'R/A C C I'), ('Visual design', 'R/A C I I'), ('Development', 'C A R C'), ('Design QA', 'R A C C')]
    col = {'R': (INDIGO, WHITE), 'A': (NAVY, HL), 'C': (OK_S, OK), 'I': (PAPER2, INK2), 'R/A': (INDIGO, HL)}
    s.rect(28, 84, 704, 40, NAVY, NAVY, 10)
    s.text(44, 109, 'Task', 12.5, 700, WHITE)
    for j, r in enumerate(roles): s.text(300 + j * 116, 109, r, 12.5, 700, WHITE, 'middle')
    for i, (t, v) in enumerate(rows):
        y = 132 + i * 46
        s.rect(28, y, 704, 40, WHITE, LINE, 8); s.text(44, y + 25, t, 13, 600, INK)
        for j, c in enumerate(v.split()):
            f, tc = col[c]; s.rect(300 + j * 116 - 26, y + 7, 52, 26, f, f, 13); s.text(300 + j * 116, y + 25, c, 12.5, 800, tc, 'middle')
    leg = [('R', 'Responsible – does the work'), ('A', 'Accountable – final decision'), ('C', 'Consulted – gives input'), ('I', 'Informed – kept updated')]
    for i, (c, t) in enumerate(leg):
        x = 28 + i * 178; f, tc = col[c]
        s.rect(x, 378, 26, 26, f, f, 13); s.text(x + 13, 396, c, 12, 800, tc, 'middle'); s.wrap(x + 34, 389, 140, t, 11, 600, INK2)
    return s


@reg('ux-22', 'Relationship map of stakeholders around the design team', 'Who influences design decisions and how closely to involve them.')
def d22():
    s = SVG(W, 480, 'Relationship Map', 'Classic Rummy · stakeholders around a design project')
    cx, cy = 380, 274
    s.circle(cx, cy, 190, 'none', LINE, 1.2, '5 5'); s.circle(cx, cy, 116, 'none', LINE, 1.2, '5 5')
    s.line(28, 96, 60, 96, INDIGO, 2.2); s.text(68, 100, 'Close collaborators', 11.5, 600, INK2)
    s.line(28, 120, 60, 120, INK3, 1.2, '4 4'); s.text(68, 124, 'Wider stakeholders', 11.5, 600, INK2)
    inner = [('Product Manager', -90), ('Game Designer', 30), ('Developers', 150), ('QA', 90)]
    outer = [('Analytics', -30), ('Marketing', 210), ('Customer Support', 250), ('Leadership', -150)]
    for t, a in inner + outer:
        r = 116 if (t, a) in inner else 190
        x = cx + r * math.cos(math.radians(a)); y = cy + r * math.sin(math.radians(a))
        strong = (t, a) in inner
        s.line(cx, cy, x, y, INDIGO if strong else INK3, 2.2 if strong else 1.2, None if strong else '4 4')
    for t, a in inner + outer:
        r = 116 if (t, a) in inner else 190
        x = cx + r * math.cos(math.radians(a)); y = cy + r * math.sin(math.radians(a))
        strong = (t, a) in inner
        w = len(t) * 7.4 + 22
        s.box(x - w / 2, y - 16, w, 32, t, None, INDIGO_S if strong else WHITE, INDIGO if strong else LINE, NAVY, 12, 700, 16)
    s.circle(cx, cy, 46, NAVY, NAVY); s.text(cx, cy - 2, 'UX / UI', 13, 800, WHITE, 'middle'); s.text(cx, cy + 15, 'Designer', 11, 600, INDIGO_M, 'middle')
    return s


@reg('ux-23', 'RICE formula and two features scored', 'Reach × Impact × Confidence ÷ Effort gives one comparable score.')
def d23():
    s = SVG(W, 420, 'RICE Method', 'Classic Rummy · illustrative estimates')
    parts = [('R', 'Reach', 'users / period', INDIGO_S, INDIGO), ('I', 'Impact', '0.25 – 3', OK_S, OK), ('C', 'Confidence', '% sure', HL_S, WARN), ('E', 'Effort', 'person-weeks', WARN_S, WARN)]
    ops = ['×', '×', '÷']
    for i, (L, t, b, f, c) in enumerate(parts):
        x = 28 + i * 156
        s.rect(x, 84, 120, 96, f, c, 14, 1.4)
        s.text(x + 60, 122, L, 28, 800, c, 'middle'); s.text(x + 60, 146, t, 13, 700, c, 'middle'); s.text(x + 60, 166, b, 11, 500, INK2, 'middle')
        if i < 3: s.text(x + 138, 140, ops[i], 26, 700, INK2, 'middle')
    s.text(732, 140, '= RICE score', 15, 800, NAVY, 'end')
    rows = [('Simplified onboarding', '1000 × 2 × 0.8 ÷ 4', 400), ('Help tutorial', '500 × 1.5 × 0.8 ÷ 3', 200)]
    for i, (t, f, v) in enumerate(rows):
        y = 210 + i * 70
        s.rect(40, y, 680, 58, OK_S if i == 0 else WHITE, OK if i == 0 else LINE, 10)
        s.text(58, y + 35, t, 14, 700, INK); s.text(300, y + 35, f, 13.5, 600, INK2)
        s.rect(500, y + 20, v / 2.5, 18, OK if i == 0 else INDIGO_M, OK if i == 0 else INDIGO_M, 9)
        s.text(500 + v / 2.5 + 10, y + 35, str(v), 15, 800, OK if i == 0 else INK2)
    s.note(360, 'Higher score → simplified onboarding gets priority.')
    return s


@reg('ux-24', 'Two scenario cards: first-time player and experienced player', 'Same feature, different actors and intentions → different experiences.')
def d24():
    s = SVG(W, 400, 'Scenario Map', 'Classic Rummy · same feature, two scenarios')
    sc = [('First-time player', 'Wants to understand the game', 'Complete a practice game', 'Guided tutorial, practice table', INDIGO_S, INDIGO),
          ('Experienced player', 'Wants a quick gaming session', 'Enter a suitable table fast', 'Quick join, saved preferences', OK_S, OK)]
    for i, (a, m, it, d, f, c) in enumerate(sc):
        x = 28 + i * 360
        s.rect(x, 84, 344, 290, f, c, 14, 1.4)
        s.circle(x + 40, 122, 20, WHITE, c, 2); s.circle(x + 40, 116, 7, c, c); s.path(f'M {x+28} {134} Q {x+40} {120} {x+52} {134}', c, 2.4)
        s.text(x + 72, 128, a, 16, 800, c)
        for j, (lab, val) in enumerate([('ACTOR', a), ('MOTIVATOR', m), ('INTENTION', it), ('DESIGN NEEDS', d)][1:]):
            y = 160 + j * 68
            s.rect(x + 16, y, 312, 56, WHITE, LINE, 10)
            s.text(x + 30, y + 20, lab, 10.5, 800, INK3); s.wrap(x + 30, y + 42, 280, val, 13.5, 600, INK)
    return s
