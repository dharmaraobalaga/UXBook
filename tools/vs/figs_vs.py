"""Diagrams for the Vs tab – redrawn from Task_Flow_Vs_User_Journey.pdf examples."""
import svgkit
from svgkit import *

svgkit.FONT = "Inter, 'Noto Sans Telugu', 'Nirmala UI', 'Telugu MN', Gautami, 'Segoe UI', Roboto, Arial, sans-serif"
F = {}
def reg(key):
    def deco(fn):
        F[key] = fn; return fn
    return deco


def vflow(title, sub, steps, w=560, last_ok=True):
    """Simple vertical step flow: steps = [(en, te)]"""
    h = 96 + len(steps) * 78 + 10
    s = SVG(w, h, title, sub)
    for i, (en, te) in enumerate(steps):
        y = 86 + i * 78
        ok = last_ok and i == len(steps) - 1
        s.rect(90, y, w - 180, 56, OK_S if ok else INDIGO_S, OK if ok else INDIGO_M, 10)
        s.text(w / 2, y + (25 if te else 33), en, 14.5, 700, NAVY, 'middle')
        if te: s.text(w / 2, y + 45, te, 12, 500, INK2, 'middle')
        if i < len(steps) - 1: s.arrow(w / 2, y + 58, w / 2, y + 76, INK3)
    return s


@reg('vs-login-flow')
def login_flow():
    return vflow('Example: user login in the Classic Rummy app', 'User Flow · Login task',
                 [('Open App', 'Open the app'), ('Login Screen', 'Login screen'), ('Enter Mobile Number', 'Enter mobile number'),
                  ('OTP Verification', 'Verify OTP'), ('Home Screen', 'Login successful')])


@reg('vs-journey')
def journey():
    st = [('1', 'Awareness', 'The user learns about the Classic Rummy app through an advertisement.', 'Positive', OK, OK_S, '“This app looks good, I should try it once.”'),
          ('2', 'Consideration', 'Thinks about whether to download it; checks ratings and features.', 'Uncertain', WARN, WARN_S, '“Is this a trustworthy app?”'),
          ('3', 'Registration', 'Opens the app and registers with mobile number and OTP.', 'Possible Friction', WARN, WARN_S, '“Is registration easy?”'),
          ('4', 'First Game', 'Learns how to play and plays the first game.', 'Engaged', OK, OK_S, '“Playing the game is interesting.”'),
          ('5', 'Retention', 'With a good experience, the user opens the app again and plays.', 'Satisfied', OK, OK_S, '“I should use this app again.”')]
    s = SVG(760, 96 + len(st) * 104, 'Example: a new user’s experience in the Classic Rummy app', 'User Journey · 5 stages')
    s.line(52, 96, 52, 96 + len(st) * 104 - 40, LINE, 2)
    for i, (n, t, d, tag, c, f, q) in enumerate(st):
        y = 84 + i * 104
        s.circle(52, y + 18, 14, NAVY, NAVY); s.text(52, y + 23, n, 12, 800, WHITE, 'middle')
        s.text(80, y + 23, t, 15, 700, NAVY)
        s.text(80, y + 46, d, 12.5, 500, INK)
        w = len(tag) * 7 + 20
        s.rect(80, y + 58, w, 22, f, c, 11); s.text(80 + w / 2, y + 73, tag, 11.5, 700, c, 'middle')
        s.text(80 + w + 14, y + 74, q, 12, 500, INK2, 'start', True)
    return s


@reg('vs-wireflow')
def wireflow():
    """Onboarding user flow, redrawn in the spirit of the PDF's wireflow example."""
    s = SVG(760, 470, 'User Flow example: opening an app for the first time', 'Splash → first launch? → onboarding → sign-up → home')
    def scr(x, y, label, kind='plain', w=86, h=140):
        s.rect(x, y, w, h, WHITE, INDIGO, 10, 1.4)
        if kind == 'splash':
            s.circle(x + w / 2, y + h / 2 - 6, 14, 'none', INDIGO, 3, '50 20')
        elif kind == 'blue':
            s.rect(x + 6, y + 18, w - 12, h - 44, INDIGO, INDIGO, 6)
            for r in range(3): s.rect(x + 14, y + 34 + r * 12, w - 30 - r * 10, 5, WHITE, WHITE, 2)
        elif kind == 'form':
            for r in range(3): s.rect(x + 10, y + 36 + r * 20, w - 20, 12, WHITE, LINE, 4)
            s.rect(x + 10, y + h - 34, w - 20, 16, INDIGO, INDIGO, 8)
        else:
            s.rect(x + 10, y + 24, w - 20, 8, INDIGO, INDIGO, 4)
            for r in range(3): s.rect(x + 10, y + 42 + r * 12, w - 20 - r * 12, 5, INDIGO_M, INDIGO_M, 2)
            s.rect(x + w - 40, y + h - 26, 30, 12, INDIGO, INDIGO, 6)
        s.text(x + w / 2, y + h + 16, label, 11, 700, NAVY, 'middle')
    scr(28, 90, 'Splash', 'splash')
    s.add(f'<path d="M 170 160 L 196 136 L 222 160 L 196 184 Z" fill="{HL_S}" stroke="{HL_L}" stroke-width="1.6"/>')
    s.text(196, 158, 'First', 9.5, 700, WARN, 'middle'); s.text(196, 170, 'launch?', 9.5, 700, WARN, 'middle')
    s.arrow(114, 160, 168, 160, INK2)
    for i, t in enumerate(['Intro 1', 'Intro 2', 'Intro 3']):
        scr(262 + i * 120, 90, t)
        if i < 2: s.arrow(262 + i * 120 + 88, 160, 262 + (i + 1) * 120 - 2, 160, INK2)
    s.arrow(224, 160, 260, 160, OK); s.text(240, 150, 'Yes', 10.5, 700, OK, 'middle')
    s.arrow(588, 160, 626, 160, INK2); scr(628, 90, 'Choose interests')
    s.path('M 671 250 L 671 280 L 120 280 L 120 300', INK2, 1.6); s.arrow(120, 296, 120, 302, INK2)
    s.path('M 196 186 L 196 272', WARN, 1.6, 'none', '5 4'); s.text(204, 230, 'No', 10.5, 700, WARN)
    for i, (t, k) in enumerate([('Sign up', 'form'), ('Home', 'blue'), ('Browse', 'plain'), ('Details', 'plain'), ('Chat', 'form'), ('Profile', 'plain')]):
        x = 78 + i * 112
        scr(x, 304, t, k)
        if i < 5: s.arrow(x + 88, 374, x + 110, 374, INK2)
    return s


@reg('vs-journey-map')
def journey_map():
    """Journey-map grid, redrawn after the PDF's bus-ticket booking example."""
    cols = ['Awareness', 'Consideration', 'Acquisition', 'Service', 'Loyalty']
    rows = [('User actions', 'What does the customer do?', ['Realises he must book a bus ticket', 'Explores bus operators incl. the TNSTC site', 'Chooses the TNSTC website to book', 'Selects bus, enters details, pays, gets e-ticket', 'Shows the ticket and boards the bus']),
            ('Goals & experiences', 'What is the customer trying to do?', ['Finds info about TNSTC & traveller concessions', 'Compares features, accessibility, ease of use', 'Wants a smooth, accessible booking', 'Gets a final ticket with concession', 'Reaches the destination hassle-free']),
            ('Feelings & thoughts', 'How might the customer feel?', ['Motivated but wants an accessible site', 'Looking for a platform that respects his needs', 'Hopeful about a seamless booking', 'Happy: screen reader & voice guidance worked', 'Happy he could do everything himself']),
            ('Pain points', 'What causes friction?', ['Little info on accessible booking sites', 'Complex, non-responsive platforms', 'Possible problems with an inaccessible flow', 'Accessibility issues in some steps', 'Whole process on laptop; mobile was hard']),
            ('Opportunities', 'How might we fix it?', ['Clear info on accessible options', 'Make the TNSTC site stand out as accessible', 'Seamless, accessible booking experience', 'Accessibility features without complications', 'Responsive site, as easy on mobile as laptop'])]
    pal = [HL_S, OK_S, PINK_S, INDIGO_S, TEAL_S]
    s = SVG(830, 600, 'User Journey example: journey map', 'Bus-ticket booking (accessible website) · 5 stages × 5 layers')
    lx, cw, top, rh = 28, 128, 82, 90
    s.rect(lx, top, 148, 44 + 5 * rh, '#6b1f45', '#6b1f45', 10)
    s.text(lx + 12, top + 28, 'Customer steps', 13, 800, WHITE)
    for j, c in enumerate(cols):
        x = 182 + j * (cw - 2)
        s.rect(x, top, cw - 6, 40, INK2, INK2, 6); s.text(x + (cw - 6) / 2, top + 25, c, 12, 700, WHITE, 'middle')
    for i, (r, q, cells) in enumerate(rows):
        y = top + 46 + i * rh
        s.text(lx + 12, y + 26, r, 12.5, 800, WHITE); s.wrap(lx + 12, y + 44, 124, q, 9.5, 500, '#f2d7e3')
        for j, t in enumerate(cells):
            x = 182 + j * (cw - 2)
            s.rect(x, y + 4, cw - 6, rh - 10, pal[j], pal[j], 4)
            s.wrap(x + 8, y + 22, cw - 20, t, 10.5, 500, INK)
    return s


@reg('vs-task-flow')
def task_flow():
    s = vflow('Example: login in the Classic Rummy app', 'Task Flow · single path',
              [('Open App', ''), ('Enter Mobile Number', ''), ('Enter OTP', ''), ('Login Successful', '')])
    return s


@reg('vs-user-flow-branch')
def user_flow_branch():
    w = 620
    s = SVG(w, 450, 'Example: login flow in the Classic Rummy app', 'User Flow · with a decision point and alternative path')
    steps = ['Open App', 'Login Screen', 'Enter Mobile Number']
    for i, t in enumerate(steps):
        y = 86 + i * 70
        s.rect(130, y, w - 260, 48, INDIGO_S, INDIGO_M, 10); s.text(w / 2, y + 30, t, 14, 700, NAVY, 'middle')
        s.arrow(w / 2, y + 50, w / 2, y + 68, INK3)
    s.rect(130, 296, w - 260, 48, HL_S, HL_L, 10, 1.6); s.text(w / 2, 326, 'OTP Verification', 14, 700, NAVY, 'middle')
    s.arrow(w / 2 - 80, 346, 170, 370, OK); s.arrow(w / 2 + 80, 346, w - 170, 370, WARN)
    s.rect(28, 372, 270, 56, OK_S, OK, 10); s.text(163, 396, 'Correct OTP', 14, 800, NAVY, 'middle'); s.text(163, 416, 'Login Success', 11.5, 500, INK2, 'middle')
    s.rect(w - 298, 372, 270, 56, WARN_S, WARN, 10); s.text(w - 163, 396, 'Wrong OTP', 14, 800, NAVY, 'middle'); s.text(w - 163, 416, 'Show Error / Retry', 11.5, 500, INK2, 'middle')
    s.path(f'M {w-28} 400 L {w-14} 400 L {w-14} 320 L {w-126} 320', WARN, 1.6, 'none', '5 4'); s.arrow(w - 120, 320, w - 128, 320, WARN)
    return s


if __name__ == '__main__':
    import pathlib
    out = pathlib.Path('/home/claude/interview-mastery/assets/images/vs'); out.mkdir(parents=True, exist_ok=True)
    for k, fn in F.items(): (out / f'{k}.svg').write_text(fn().render())
    print(len(F), 'figures')
