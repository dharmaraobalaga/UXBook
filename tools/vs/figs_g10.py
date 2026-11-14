"""Group 10 diagrams – redrawn (not copied) from the illustrations in Generate_UX_Vs_Questions_10.pdf. Illustrative numbers only."""
import svgkit
from svgkit import *
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

@reg('g10-dau-mau')
def dm():
    s = SVG(640, 330, 'DAU vs MAU', 'Illustrative user activity – learning app')
    days = [('Mon', 5000), ('Tue', 5500), ('Wed', 4800), ('Thu', 5200), ('Fri', 4600), ('Sat', 3900), ('Sun', 3600)]
    s.rect(28, 78, 340, 230, WHITE, LINE, 12); s.text(44, 102, 'DAU – unique active users per day', 12, 800, INDIGO)
    for i, (d, v) in enumerate(days):
        h = v / 5500 * 130; x = 52 + i * 44
        s.rect(x, 260 - h, 30, h, INDIGO_S if d != 'Tue' else INDIGO, INDIGO, 4, 1)
        s.text(x + 15, 280, d, 10.5, 600, INK2, 'middle')
    s.text(52 + 44 + 15, 260 - 130 - 8, '5,500', 11, 800, INDIGO, 'middle')
    s.rect(392, 78, 220, 230, OK_S, OK, 12); s.text(408, 102, 'MAU – unique users per month', 12, 800, OK)
    s.text(502, 192, '40,000', 34, 800, OK, 'middle'); s.text(502, 220, 'active at least once', 11.5, 600, INK2, 'middle')
    s.text(502, 238, 'in the month', 11.5, 600, INK2, 'middle')
    return s

@reg('g10-nps')
def nps():
    s = SVG(640, 250, 'NPS scale', 'How likely are you to recommend us? (0–10)')
    for i in range(11):
        c, f = (WARN, WARN_S) if i <= 6 else ((HL_L, HL_S) if i <= 8 else (OK, OK_S))
        x = 40 + i * 52
        s.rect(x, 96, 44, 44, f, c, 8, 1.4); s.text(x + 22, 124, str(i), 15, 800, c if c != HL_L else WARN, 'middle')
    for (a, b, t, c) in [(0, 6, 'Detractors 0–6', WARN), (7, 8, 'Passives 7–8', INK2), (9, 10, 'Promoters 9–10', OK)]:
        x1, x2 = 40 + a * 52, 40 + b * 52 + 44
        s.line(x1, 154, x2, 154, c, 2); s.text((x1 + x2) / 2, 174, t, 12, 800, c, 'middle')
    s.rect(160, 196, 320, 36, INDIGO_S, INDIGO_S, 8); s.text(320, 219, 'NPS = % Promoters − % Detractors', 13.5, 800, NAVY, 'middle')
    return s

@reg('g10-ab-test')
def ab():
    s = SVG(640, 300, 'A/B Testing – example', 'Illustrative CTA colour experiment, not real test results')
    for i, (lab, col) in enumerate([('Version A', INDIGO), ('Version B', OK)]):
        x = 40 + i * 340
        s.text(x + 110, 90, lab, 13, 800, col, 'middle')
        s.rect(x, 102, 220, 170, WHITE, LINE, 12)
        s.rect(x + 20, 120, 180, 14, PAPER2, PAPER2, 4); s.rect(x + 20, 144, 130, 10, PAPER2, PAPER2, 4); s.rect(x + 20, 162, 150, 10, PAPER2, PAPER2, 4)
        s.rect(x + 50, 206, 120, 40, col, col, 8); s.text(x + 110, 231, 'Buy Now', 13, 800, WHITE, 'middle')
    s.text(320, 192, '50 / 50', 11, 700, INK3, 'middle'); s.text(320, 208, 'traffic split', 10.5, 600, INK3, 'middle')
    return s

@reg('g10-heatmap-recording')
def hr():
    s = SVG(660, 330, 'Heatmap vs Session Recording', 'Aggregate interaction patterns vs one user\'s playback')
    s.rect(28, 78, 290, 230, WHITE, LINE, 12); s.text(44, 102, 'Heatmap (all users)', 12, 800, PINK)
    s.rect(44, 126, 258, 22, PAPER2, PAPER2, 4)
    for cx, cy, r, op in [(110, 137, 18, .55), (110, 137, 8, .9), (230, 200, 44, .35), (230, 200, 22, .6), (230, 200, 9, .9), (90, 250, 30, .3)]:
        s.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e2483d" opacity="{op}"/>')
    s.text(230, 260, 'CTA hotspot', 10.5, 700, INK2, 'middle')
    s.rect(342, 78, 290, 230, WHITE, LINE, 12); s.text(358, 102, 'Session Recording (one user)', 12, 800, INDIGO)
    s.rect(358, 114, 258, 150, PAPER, LINE, 6)
    s.path('M 380 140 L 450 150 L 430 200 L 520 190 L 560 230', INDIGO, 1.8, dash='5 4')
    for x, y, t in [(450, 150, '1'), (430, 200, '2'), (520, 190, '3')]:
        s.circle(x, y, 9, INDIGO, INDIGO); s.text(x, y + 4, t, 10, 800, WHITE, 'middle')
    s.text(560, 250, 'rage-click on filter', 10, 700, WARN, 'middle'); s.circle(560, 230, 7, WARN_S, WARN, 1.6)
    s.rect(358, 274, 258, 22, INDIGO_S, INDIGO_S, 11); s.text(372, 289, '▶  00:42 / 03:15', 10.5, 700, INDIGO)
    s.rect(470, 283, 90, 4, INDIGO, INDIGO, 2)
    return s

@reg('g10-funnel')
def fn():
    st = [('Visit Website', 1000), ('Start Signup', 700), ('Verify Email', 500), ('Complete Signup', 400)]
    s = SVG(640, 110 + len(st) * 52 + 50, 'Funnel Analysis – signup example', 'Illustrative: 40% of initial visitors completed signup')
    for i, (t, v) in enumerate(st):
        y = 86 + i * 52; w = v / 1000 * 340
        s.text(40, y + 25, t, 12.5, 700, INK2)
        s.rect(180, y + 6, w, 30, [INDIGO, INDIGO_M, TEAL_S, OK_S][i], INDIGO if i == 0 else LINE, 6)
        s.text(180 + w + 10, y + 26, f'{v:,}', 12.5, 800, NAVY)
        if i: s.text(620, y + 26, f'−{st[i-1][1]-v}', 11, 700, WARN, 'end')
    y = 86 + len(st) * 52 + 6
    s.text(620, 74, 'drop-off', 10.5, 700, WARN, 'end')
    s.rect(40, y, 560, 34, HL_S, HL_L, 8); s.text(320, y + 22, 'Biggest drop: Visit → Start Signup (300 users)', 12.5, 700, INK2, 'middle')
    return s

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn_ in F.items(): (out / f'{k}.svg').write_text(fn_().render())
    print(len(F), 'figures')
