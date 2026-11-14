"""Group 9 diagrams – redrawn (not copied) from the illustrations in Generate_UX_Vs_Questions_9.pdf."""
import svgkit
from svgkit import *
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

def chain(s, y, items, fill, stroke, tc, x0=40, w=None, gap=26, h=48):
    n = len(items); w = w or (s.w - 2 * x0 - gap * (n - 1)) / n
    for i, t in enumerate(items):
        x = x0 + i * (w + gap)
        s.box(x, y, w, h, t, fill=fill, stroke=stroke, tc=tc, size=12.5, weight=700)
        if i < n - 1: s.arrow(x + w + 3, y + h / 2, x + w + gap - 3, y + h / 2, tc)

@reg('g9-product-workflow')
def pw():
    s = SVG(720, 400, 'Typical product workflow', 'Discovery → Delivery → Continuous Learning')
    rows = [('Discovery', ['Research', 'Problem Definition', 'Ideation', 'Validation'], INDIGO_S, INDIGO_M, INDIGO),
            ('Delivery', ['Design', 'Development', 'QA', 'Release'], OK_S, OK, OK),
            ('Continuous Learning', ['Analytics', 'Feedback', 'Improvements'], HL_S, HL_L, WARN)]
    for i, (h, items, f, st, c) in enumerate(rows):
        y = 84 + i * 104
        s.text(40, y + 4, h, 14, 800, c)
        n = len(items); chain(s, y + 16, items, f, st, c, w=(600 - 26 * (n - 1)) / n)
        if i < 2: s.arrow(340, y + 70, 340, y + 96, INK3)
    s.path('M 644 340 C 690 300, 690 120, 644 124', INK3, 1.4, dash='5 4')
    s.text(700, 236, 'learn', 10.5, 700, INK3, 'middle')
    return s

@reg('g9-prototype-mvp')
def pm():
    s = SVG(640, 430, 'Prototype vs MVP', 'Simulated interaction vs working core product')
    x, y, w, h = phone(s, 70, 104, 170, 290, WHITE, INK3)
    s.text(155, 96, 'Prototype', 14, 800, INDIGO, 'middle')
    for i, t in enumerate(['Restaurants', 'Menu', 'Cart', 'Checkout']):
        s.rect(x + 6, y + 14 + i * 56, w - 12, 44, INDIGO_S, INDIGO_M, 6, 1.2, '5 3')
        s.text(x + w / 2, y + 41 + i * 56, t, 12, 700, INDIGO, 'middle')
    s.text(155, 418, 'clickable screens · fake data', 11, 600, INK3, 'middle')
    x, y, w, h = phone(s, 400, 104, 170, 290, WHITE, OK)
    s.text(485, 96, 'MVP', 14, 800, OK, 'middle')
    for i, (t, b) in enumerate([('Real listings', 'live restaurants'), ('Place order', 'actual ordering'), ('Pay', 'payment integration'), ('Track', 'basic order status')]):
        s.box(x + 6, y + 14 + i * 56, w - 12, 44, t, b, OK_S, OK, OK, 12, 700, 6, 10)
    s.text(485, 418, 'working product · real users', 11, 600, INK3, 'middle')
    s.arrow(262, 249, 378, 249, INK2); s.text(320, 238, 'validate, then build', 10.5, 700, INK3, 'middle')
    return s

@reg('g9-agile-waterfall')
def aw():
    s = SVG(700, 380, 'Agile vs Waterfall', 'Iterative cycles vs sequential phases')
    s.text(170, 84, 'Agile – repeat every sprint', 13, 800, INDIGO, 'middle')
    import math
    cx, cy, r = 170, 226, 100
    st = ['Plan', 'Design', 'Build', 'Test', 'Release', 'Feedback']
    s.circle(cx, cy, r, 'none', INDIGO_M, 2, '6 5')
    s.circle(cx, cy, 40, INDIGO, INDIGO); s.text(cx, cy + 5, 'Sprint', 13, 800, WHITE, 'middle')
    for i, t in enumerate(st):
        a = -math.pi / 2 + i * 2 * math.pi / len(st)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        s.rect(px - 42, py - 15, 84, 30, INDIGO_S, INDIGO, 15, 1.4); s.text(px, py + 5, t, 11.5, 700, INDIGO, 'middle')
    s.text(480, 84, 'Waterfall – one phase after another', 13, 800, WARN, 'middle')
    ph = ['Requirements', 'Design', 'Development', 'Testing', 'Release']
    for i, t in enumerate(ph):
        x, y = 344 + i * 54, 104 + i * 50
        s.box(x, y, 124, 36, t, fill=WARN_S, stroke=WARN, tc=WARN, size=12, weight=700, r=6)
        if i < len(ph) - 1: s.path(f'M {x+124} {y+18} L {x+140} {y+18} L {x+140} {y+48}', WARN, 1.5)
    return s

@reg('g9-scrum-kanban')
def sk():
    s = SVG(700, 360, 'Scrum vs Kanban', 'Time-boxed sprint vs continuous flow with WIP limits')
    s.rect(28, 78, 300, 260, INDIGO_S, INDIGO_M, 12); s.text(44, 102, 'Scrum – 2-week Sprint', 13, 800, INDIGO)
    ev = ['Sprint Planning', 'Daily Scrum (every day)', 'Sprint Review', 'Retrospective']
    for i, t in enumerate(ev):
        y = 118 + i * 54
        s.box(52, y, 252, 40, t, fill=WHITE, stroke=INDIGO, tc=INDIGO, size=12.5, weight=700, r=8)
        if i < 3: s.arrow(178, y + 41, 178, y + 52, INDIGO)
    s.text(372, 102, 'Kanban – continuous flow', 13, 800, OK)
    cols = [('To Do', 3, None), ('In Progress', 2, 'WIP ≤ 2'), ('Review', 1, 'WIP ≤ 2'), ('Done', 2, None)]
    for i, (t, n, lim) in enumerate(cols):
        x = 360 + i * 82
        s.rect(x, 114, 76, 224, WHITE, LINE, 8); s.text(x + 38, 134, t, 11, 800, INK2, 'middle')
        if lim: s.text(x + 38, 150, lim, 9.5, 700, WARN, 'middle')
        for j in range(n): s.rect(x + 8, 160 + j * 46, 60, 38, [HL_S, PINK_S, OK_S, TEAL_S][i], [HL_L, PINK, OK, TEAL][i], 4, 1)
    return s

@reg('g9-sprint-thinking')
def st():
    s = SVG(700, 350, 'Design Sprint vs Design Thinking', 'Five-day sprint format vs five iterative stages')
    s.text(40, 90, 'Design Sprint (GV five-day format)', 13, 800, INDIGO)
    days = [('Mon', 'Map'), ('Tue', 'Sketch'), ('Wed', 'Decide'), ('Thu', 'Prototype'), ('Fri', 'Test')]
    for i, (d, t) in enumerate(days):
        x = 40 + i * 126
        s.box(x, 104, 112, 58, d, t, INDIGO_S, INDIGO, INDIGO, 12, 800, 8, 12)
        if i < 4: s.arrow(x + 113, 133, x + 124, 133, INDIGO)
    s.text(40, 210, 'Design Thinking (iterative, no fixed duration)', 13, 800, OK)
    sts = ['Empathize', 'Define', 'Ideate', 'Prototype', 'Test']
    for i, t in enumerate(sts):
        x = 40 + i * 126
        s.box(x, 224, 112, 44, t, fill=OK_S, stroke=OK, tc=OK, size=12.5, weight=800, r=22)
        if i < 4: s.arrow(x + 113, 246, x + 124, 246, OK)
    s.path('M 656 270 C 640 318, 120 318, 96 270', OK, 1.4, dash='5 4')
    s.text(370, 330, 'iterate – go back to any stage', 10.5, 700, OK, 'middle')
    return s

@reg('g9-frontend-backend')
def fb():
    s = SVG(700, 340, 'Frontend vs Backend', 'Client side (what users see) vs server side (logic and data)')
    s.rect(28, 78, 230, 230, TEAL_S, TEAL, 12); s.text(143, 102, 'CLIENT SIDE – Frontend', 12.5, 800, TEAL, 'middle')
    s.box(48, 118, 190, 52, 'Browser / App', 'HTML · CSS · JavaScript', WHITE, TEAL, TEAL, 12.5, 800, 8, 10.5)
    s.box(48, 186, 190, 104, 'Presentation layer', 'Login form, buttons, error messages, layouts', WHITE, TEAL, TEAL, 12.5, 800, 8, 10.5)
    s.rect(380, 78, 292, 230, INDIGO_S, INDIGO, 12); s.text(526, 102, 'SERVER SIDE – Backend', 12.5, 800, INDIGO, 'middle')
    s.box(398, 118, 124, 76, 'Business logic', 'validate credentials', WHITE, INDIGO, INDIGO, 12, 800, 8, 10.5)
    s.box(536, 118, 120, 76, 'Data layer', 'database', WHITE, INDIGO, INDIGO, 12, 800, 8, 10.5)
    s.box(398, 214, 258, 76, 'Authentication & 3rd-party services', 'identity, payments, email', WHITE, INDIGO, INDIGO, 12, 800, 8, 10.5)
    s.arrow(523, 156, 534, 156, INDIGO)
    s.arrow(262, 160, 376, 160, INK2); s.text(319, 150, 'API request', 10.5, 700, INK2, 'middle')
    s.arrow(376, 236, 262, 236, INK2); s.text(319, 226, 'JSON response', 10.5, 700, INK2, 'middle')
    return s

@reg('g9-handoff-redline')
def hr():
    s = SVG(640, 360, 'Developer handoff – redline specs', 'Illustrative spacing, size and state annotations')
    x, y, w, h = phone(s, 60, 76, 220, 268)
    s.rect(x + 8, y + 10, w - 16, 26, INDIGO_S, INDIGO_S, 4); s.text(x + 18, y + 28, 'Recipe   Reviews', 11.5, 700, INDIGO)
    s.text(x + 10, y + 70, 'Lemon Sponge Cake', 17, 800, NAVY)
    s.text(x + 10, y + 94, 'Serves 10', 12, 600, INK2)
    s.rect(x + 10, y + 180, w - 20, 40, NAVY, NAVY, 8); s.text(x + w / 2, y + 205, 'Add to list', 13, 700, WHITE, 'middle')
    def spec(y1, y2, lab):
        s.line(x + w + 14, y1, x + w + 14, y2, PINK, 1.4); s.line(x + w + 8, y1, x + w + 20, y1, PINK, 1.4); s.line(x + w + 8, y2, x + w + 20, y2, PINK, 1.4)
        s.rect(x + w + 24, (y1 + y2) / 2 - 10, 34, 20, PINK, PINK, 4); s.text(x + w + 41, (y1 + y2) / 2 + 4, lab, 11, 800, WHITE, 'middle')
    spec(y + 10, y + 36, '24'); spec(y + 46, y + 100, '48'); spec(y + 180, y + 220, '40')
    notes = ['Title: 24/32 Bold, #1C2541', 'Spacing: 16 px grid', 'Button: default · hover · pressed · disabled', 'Loading + error states', 'Assets: SVG icons, @2x images']
    for i, t in enumerate(notes):
        s.rect(372, 96 + i * 50, 240, 38, WHITE, LINE, 8); s.text(386, 120 + i * 50, t, 11, 600, INK2)
    return s

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
