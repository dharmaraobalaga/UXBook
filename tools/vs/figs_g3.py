"""Group 3 diagrams – redrawn from Generate_UX_Vs_Questions-3.pdf."""
import svgkit
from svgkit import *
from figs_vs import vflow
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

@reg('g3-task-flow')
def tf():
    return vflow('Task Flow: Money Transfer', 'Simple linear task flow',
                 [(t, '') for t in ['Open Banking App', 'Login', 'Select Beneficiary', 'Enter Amount', 'Confirm Transfer', 'Transaction Successful']])

@reg('g3-user-flow')
def uf():
    w = 620; s = SVG(w, 560, 'User Flow: Money Transfer', 'Illustrative user flow with alternative paths')
    def box(y, t, f=INDIGO_S, c=INDIGO_M, x=130, ww=None):
        ww = ww or (w - 260); s.rect(x, y, ww, 46, f, c, 10); s.text(x + ww / 2, y + 29, t, 14, 700, NAVY, 'middle')
    box(84, 'Open Banking App'); s.arrow(w/2, 132, w/2, 150, INK3)
    box(152, 'Login'); s.arrow(w/2, 200, w/2, 218, INK3)
    box(220, 'Choose Transfer Method', HL_S, HL_L)
    s.arrow(w/2 - 60, 268, 170, 296, INK3); s.arrow(w/2 + 60, 268, w - 170, 296, INK3)
    for x, a, b, f, c in [(28, 'Existing Beneficiary', 'Select Account', OK_S, OK), (w - 288, 'New Beneficiary', 'Add Account', INDIGO_S, INDIGO)]:
        s.rect(x, 298, 260, 96, f, c, 12)
        s.text(x + 130, 326, a, 14, 800, NAVY, 'middle'); s.arrow(x + 130, 336, x + 130, 352, INK3); s.text(x + 130, 376, b, 13, 600, INK2, 'middle')
    s.arrow(158, 396, w/2 - 40, 420, INK3); s.arrow(w - 158, 396, w/2 + 40, 420, INK3)
    box(422, 'Enter Amount & Confirm'); s.arrow(w/2, 470, w/2, 488, INK3)
    box(490, 'Transfer Successful', OK_S, OK)
    return s

@reg('g3-sitemap')
def sm():
    w = 700; s = SVG(w, 300, 'Sitemap: E-commerce Website', 'Illustrative website sitemap')
    s.rect(w/2 - 90, 84, 180, 46, NAVY, NAVY, 10); s.text(w/2, 113, 'Home', 15, 800, WHITE, 'middle')
    for i, (a, b) in enumerate([('Products', 'Categories'), ('Offers', 'Deals'), ('Account', 'Orders')]):
        x = 28 + i * 220
        s.path(f'M {w/2} 130 L {w/2} 150 L {x+102} 150 L {x+102} 166', INK3, 1.4)
        s.rect(x, 166, 204, 104, INDIGO_S, INDIGO_M, 12)
        s.text(x + 102, 196, a, 14.5, 800, NAVY, 'middle'); s.arrow(x + 102, 208, x + 102, 228, INK3)
        s.rect(x + 42, 230, 120, 30, WHITE, LINE, 8); s.text(x + 102, 250, b, 12.5, 600, INK2, 'middle')
    return s

@reg('g3-screen-flow')
def sf():
    return vflow('Screen Flow: Mobile Banking App', 'Illustrative screen sequence',
                 [(t, '') for t in ['Splash Screen', 'Login Screen', 'Dashboard', 'Beneficiary Screen', 'Transfer Screen', 'Success Screen']])

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
