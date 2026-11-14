"""Group 4/5 diagrams – drawn for examples that were images in Generate_UX_Vs_Questions4.pdf."""
import svgkit
from svgkit import *
svgkit.FONT = "Inter, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(k):
    def d(fn): F[k] = fn; return fn
    return d

def label(s, x, y, t, sub, c):
    s.text(x, y, t, 15, 800, c, 'middle'); s.text(x, y + 20, sub, 11.5, 500, INK2, 'middle')

def login_wire(s, x, y):
    X, Y, w, h = phone(s, x, y, 200, 330, WHITE, INK3)
    s.rect(X + 50, Y + 20, w - 100, 40, 'none', INK3, 6, 1.2, '4 3'); s.path(f'M {X+50} {Y+20} L {X+w-50} {Y+60} M {X+w-50} {Y+20} L {X+50} {Y+60}', LINE, 1)
    s.rect(X + 14, Y + 80, w - 60, 10, PAPER2, PAPER2, 3)
    for i in range(2): s.rect(X + 14, Y + 110 + i * 50, w - 28, 34, WHITE, INK3, 4); s.rect(X + 22, Y + 123 + i * 50, 60, 8, PAPER2, PAPER2, 3)
    s.rect(X + 14, Y + 220, w - 28, 36, PAPER2, INK3, 4); s.text(X + w / 2, Y + 243, 'BUTTON', 10, 700, INK3, 'middle')
    s.rect(X + 50, Y + 268, w - 100, 8, PAPER2, PAPER2, 3)

def login_mock(s, x, y):
    X, Y, w, h = phone(s, x, y, 200, 330, WHITE, NAVY)
    s.rect(X, Y, w, 96, '#0f3d2e', '#0f3d2e', 10)
    s.circle(X + w / 2, Y + 36, 18, '#f2c75c', '#f2c75c'); s.text(X + w / 2, Y + 42, 'CR', 13, 800, '#0b2e22', 'middle')
    s.text(X + w / 2, Y + 80, 'Welcome back', 13, 700, WHITE, 'middle')
    for i, (lab, val) in enumerate([('Mobile number', '+91 98765 43210'), ('Password', '••••••••')]):
        s.text(X + 14, Y + 118 + i * 54, lab, 9.5, 700, INK2); s.rect(X + 14, Y + 124 + i * 54, w - 28, 30, WHITE, '#0f3d2e', 8); s.text(X + 24, Y + 144 + i * 54, val, 11.5, 600, INK)
    s.rect(X + 14, Y + 226, w - 28, 36, '#0f3d2e', '#0f3d2e', 18); s.text(X + w / 2, Y + 249, 'Login', 13, 800, WHITE, 'middle')
    s.text(X + w / 2, Y + 282, 'Forgot password?', 11, 600, '#a3365f', 'middle')

@reg('g4-wireframe-mockup')
def wm():
    s = SVG(640, 470, 'Wireframe vs Mockup', 'Login screen · structure first, then visual design')
    login_wire(s, 80, 84); login_mock(s, 360, 84)
    label(s, 180, 438, 'Wireframe', 'Structure, content placement, layout', INK2)
    label(s, 460, 438, 'Mockup', 'Colours, typography, branding', NAVY)
    return s

def dash(s, x, y, hi):
    w, h = 270, 250
    s.rect(x, y, w, h, WHITE, NAVY if hi else INK3, 10, 1.4)
    if not hi:
        s.rect(x + 10, y + 10, w - 20, 24, PAPER2, INK3, 4)
        for i in range(3): s.rect(x + 10 + i * 86, y + 46, 78, 54, 'none', INK3, 4, 1.2, '4 3')
        s.rect(x + 10, y + 112, 160, 126, 'none', INK3, 4, 1.2, '4 3'); s.path(f'M {x+10} {y+112} L {x+170} {y+238} M {x+170} {y+112} L {x+10} {y+238}', LINE, 1)
        s.rect(x + 180, y + 112, 80, 126, 'none', INK3, 4, 1.2, '4 3')
    else:
        s.rect(x + 10, y + 10, w - 20, 24, INDIGO_S, INDIGO_M, 4); s.text(x + 20, y + 26, 'Dashboard', 11, 800, NAVY); s.text(x + w - 20, y + 26, 'Nov 2026 ▾', 9.5, 600, INK2, 'end')
        for i, (t, v) in enumerate([('Balance', '₹82,400'), ('Spent', '₹14,250'), ('Saved', '₹6,000')]):
            bx = x + 10 + i * 86; s.rect(bx, y + 46, 78, 54, WHITE, INDIGO_M, 6); s.text(bx + 8, y + 64, t, 9, 600, INK3); s.text(bx + 8, y + 86, v, 12, 800, NAVY)
        s.rect(x + 10, y + 112, 160, 126, WHITE, INDIGO_M, 6); s.text(x + 18, y + 128, 'Monthly spending (px: 160×126)', 8.5, 600, INK3)
        for i, hgt in enumerate([40, 64, 52, 80, 70, 92]): s.rect(x + 22 + i * 24, y + 228 - hgt, 14, hgt, INDIGO, INDIGO, 2)
        s.rect(x + 180, y + 112, 80, 126, WHITE, INDIGO_M, 6); s.text(x + 188, y + 128, 'Recent', 9, 700, NAVY)
        for i in range(4): s.rect(x + 188, y + 140 + i * 24, 64, 16, PAPER, LINE, 3)
    return x, y, w, h

@reg('g4-lofi-hifi-wireframe')
def lh():
    s = SVG(640, 400, 'Low-Fidelity vs High-Fidelity Wireframe', 'Dashboard')
    dash(s, 28, 84, False); dash(s, 342, 84, True)
    label(s, 163, 362, 'Low-Fidelity', 'Rough layout and content blocks', INK2)
    label(s, 477, 362, 'High-Fidelity', 'Detailed structure and dimensions', NAVY)
    return s

@reg('g5-lofi-hifi-prototype')
def lp():
    s = SVG(700, 360, 'Low-Fidelity vs High-Fidelity Prototype', 'Mobile banking · money transfer')
    for j, hi in enumerate([False, True]):
        bx = 28 + j * 340
        for i, t in enumerate(['Home', 'Transfer', 'Done']):
            X, Y, w, h = phone(s, bx + i * 106, 96, 96, 190, WHITE, NAVY if hi else INK3)
            if hi:
                s.rect(X, Y, w, 22, INDIGO, INDIGO, 4); s.text(X + w / 2, Y + 15, t, 9.5, 700, WHITE, 'middle')
                if t == 'Done': s.circle(X + w / 2, Y + 70, 18, OK_S, OK, 2); s.text(X + w / 2, Y + 76, '✓', 16, 800, OK, 'middle'); s.text(X + w / 2, Y + 108, '₹5,000 sent', 9.5, 700, NAVY, 'middle')
                else:
                    for r in range(3): s.rect(X + 6, Y + 32 + r * 26, w - 12, 20, WHITE, INDIGO_M, 4)
                s.rect(X + 6, Y + h - 30, w - 12, 18, NAVY, NAVY, 9)
            else:
                s.rect(X + 4, Y + 2, w - 8, 14, PAPER2, INK3, 3); s.text(X + w / 2, Y + 12, t, 8.5, 700, INK3, 'middle')
                for r in range(3): s.rect(X + 6, Y + 32 + r * 26, w - 12, 18, 'none', INK3, 3, 1, '3 3')
                s.rect(X + 6, Y + h - 30, w - 12, 18, PAPER2, INK3, 3)
            if i < 2: s.arrow(X + w + 6, Y + h - 21, X + w + 20, Y + h - 21, OK if hi else INK3, 1.4)
    label(s, 186, 316, 'Low-Fidelity', 'Basic screen layouts and navigation', INK2)
    label(s, 526, 316, 'High-Fidelity', 'Detailed UI and realistic interactions', NAVY)
    return s

@reg('g4-usecase-diagram')
def uc():
    s = SVG(620, 380, 'Use Case Diagram: Banking System', 'Conceptual representation')
    s.rect(220, 84, 372, 270, PAPER, NAVY, 14, 1.6); s.text(236, 108, 'BANKING SYSTEM  ·  system boundary', 10.5, 800, INK3)
    uses = ['Login', 'View Balance', 'Transfer Money', 'View Transactions']
    for i, u in enumerate(uses):
        y = 128 + i * 54
        s.add(f'<ellipse cx="406" cy="{y+20}" rx="120" ry="21" fill="{INDIGO_S}" stroke="{INDIGO}" stroke-width="1.4"/>')
        s.text(406, y + 25, u, 13, 700, NAVY, 'middle')
        s.line(112, 220, 286, y + 20, INK2, 1.3)
    s.circle(84, 182, 14, 'none', NAVY, 2.4); s.path('M 84 196 L 84 238 M 60 212 L 108 212 M 84 238 L 64 270 M 84 238 L 104 270', NAVY, 2.4)
    s.text(84, 294, 'Customer', 13, 800, NAVY, 'middle'); s.text(84, 312, '(actor)', 11, 500, INK3, 'middle')
    return s

if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
