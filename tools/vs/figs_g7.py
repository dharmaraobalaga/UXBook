"""Group 7 diagrams – redrawn from the small illustrations in Generate_UX_Vs_Questions_7.pdf."""
import svgkit
from svgkit import *
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

@reg('g7-button-variants')
def bv():
    s = SVG(620, 230, 'Button component – common variants', 'One component, several variants')
    s.rect(28, 84, 564, 116, WHITE, LINE, 12, 1.2, '6 4'); s.text(44, 106, 'Component set: Button', 11.5, 800, INK3)
    for i, (t, f, tc, st) in enumerate([('Primary', NAVY, WHITE, NAVY), ('Secondary', WHITE, NAVY, NAVY), ('Disabled', PAPER2, INK3, PAPER2)]):
        x = 60 + i * 180
        s.rect(x, 124, 150, 46, f, st, 23, 1.6); s.text(x + 75, 153, t, 14, 700, tc, 'middle')
    return s

@reg('g7-atomic')
def at():
    lv = [('Atoms', 'Buttons, Labels, Inputs'), ('Molecules', 'Search Form'), ('Organisms', 'Website Header'), ('Templates', 'Page Structure'), ('Pages', 'Real Content & States')]
    s = SVG(620, 110 + len(lv) * 62, 'Atomic Design – five levels', 'Brad Frost · small building blocks → full pages')
    for i, (a, b) in enumerate(lv):
        y = 86 + i * 62; w = 220 + i * 70; x = (620 - w) / 2
        f = [INDIGO_S, TEAL_S, OK_S, HL_S, PINK_S][i]; c = [INDIGO, TEAL, OK, WARN, PINK][i]
        s.rect(x, y, w, 50, f, c, 10, 1.4); s.text(310, y + 22, a, 14, 800, c, 'middle'); s.text(310, y + 40, b, 11.5, 600, INK2, 'middle')
    return s

@reg('g7-box-model')
def bm():
    s = SVG(560, 330, 'Padding vs Margin', 'Illustrative CSS box-model spacing')
    s.rect(60, 84, 440, 220, HL_S, HL_L, 6, 1.4, '6 4'); s.text(76, 106, 'Margin (outside the border)', 12, 800, WARN)
    s.rect(120, 120, 320, 150, OK_S, OK, 6, 2); s.text(136, 142, 'Padding (inside the border)', 12, 800, OK)
    s.rect(190, 160, 180, 70, WHITE, INDIGO, 6, 1.4); s.text(280, 200, 'Content', 15, 800, NAVY, 'middle')
    s.text(436, 114, 'border', 10.5, 700, INK3, 'end')
    return s

@reg('g7-responsive-grid')
def rg():
    s = SVG(640, 300, 'Responsive grid', 'Desktop: 4 columns · Mobile: 1 column')
    s.rect(28, 84, 380, 190, WHITE, INK3, 10, 1.4); s.text(44, 106, 'Desktop', 12, 800, NAVY)
    for i in range(4): s.rect(44 + i * 88, 120, 80, 136, INDIGO_S, INDIGO_M, 6)
    s.rect(456, 84, 156, 190, WHITE, INK3, 18, 1.4); s.text(472, 106, 'Mobile', 12, 800, NAVY)
    for i in range(4): s.rect(472, 118 + i * 38, 124, 30, INDIGO_S, INDIGO_M, 6)
    s.arrow(414, 180, 450, 180, INK3)
    return s

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
