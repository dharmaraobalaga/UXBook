from svgkit import *
import math

F = {}
def reg(key, alt, cap):
    def deco(fn):
        F[key] = (fn, alt, cap); return fn
    return deco
W = 760


@reg('ux-25', 'Service blueprint lanes for withdrawing winnings with line of visibility', 'What the player sees, and the hidden steps behind it.')
def d25():
    s = SVG(W, 520, 'Service Blueprint', 'Classic Rummy · withdrawing winnings')
    lanes = [('Customer', ['Requests withdrawal', 'Waits', 'Checks status', 'Money received'], INDIGO_S, INDIGO),
             ('Evidence', ['Withdraw screen', 'Confirmation', 'SMS update', 'Bank credit'], PAPER2, INK2),
             ('Frontstage', ['App form', 'Status: pending', 'Support chat', 'Status: paid'], OK_S, OK),
             ('Backstage', ['KYC check', 'Fraud review', 'Finance approval', 'Payout'], HL_S, WARN),
             ('Support', ['Verification system', 'Risk engine', 'Payment gateway', 'Banking partner'], TEAL_S, TEAL)]
    for i, (t, cells, f, c) in enumerate(lanes):
        y = 84 + i * 74
        s.rect(28, y, 704, 64, f, f, 10)
        s.text(40, y + 37, t, 12.5, 800, c)
        for j, cell in enumerate(cells):
            x = 140 + j * 148
            s.box(x, y + 10, 132, 44, cell, None, WHITE, c, INK, 11.5, 600, 8)
            if i == 0 and j < 3: s.arrow(x + 132, y + 32, x + 148, y + 32, INDIGO)
    s.line(28, 304, 732, 304, WARN, 2, '8 5'); s.rect(560, 294, 172, 20, PAPER, PAPER, 6); s.text(728, 309, 'line of visibility', 11.5, 700, WARN, 'end')
    s.note(462, 'Delay is backstage (KYC + fraud review) → show clearer status updates frontstage.')
    return s


@reg('ux-26', 'Site map tree from Home / Lobby to five sections', 'The structure of all pages, before designing screens.')
def d26():
    s = SVG(W, 420, 'Site Map', 'Classic Rummy · information architecture (illustrative)')
    s.box(300, 80, 160, 44, 'Home / Lobby', None, NAVY, NAVY, WHITE, 14, 700)
    secs = [('Games', ['Game types', 'Tables'], INDIGO), ('Wallet', ['Add money', 'Withdraw', 'Transactions'], OK), ('Account', ['Profile', 'KYC', 'Settings'], TEAL),
            ('Rewards', ['Offers', 'Bonuses'], WARN), ('Support', ['Help centre', 'FAQs', 'Contact us'], PINK)]
    for i, (t, ch, c) in enumerate(secs):
        x = 28 + i * 144
        s.path(f'M 380 124 L 380 146 L {x+64} 146 L {x+64} 162', INK3, 1.4)
        s.box(x, 162, 128, 40, t, None, WHITE, c, c, 13.5, 800, 8, sw=1.8)
        for j, cc in enumerate(ch):
            y = 222 + j * 50
            s.path(f'M {x+14} 202 L {x+14} {y+18} L {x+24} {y+18}', LINE, 1.4)
            s.box(x + 24, y, 104, 36, cc, None, WHITE, LINE, INK, 11.5, 500, 8)
    s.note(372, 'Validate with tree testing: can players find “Withdraw” on the first try?')
    return s


@reg('ux-27', 'Skill map heat grid of designers and skills', 'Spot team strengths and gaps at a glance.')
def d27():
    s = SVG(W, 410, 'Skill Map', 'Classic Rummy design team · illustrative')
    ppl = ['Designer A', 'Designer B', 'Designer C']
    rows = [('User research', 'SBB'), ('Visual design', 'BSS'), ('Motion design', 'BBS'), ('Prototyping', 'SSB'), ('Data & analytics', 'BBB')]
    for j, p in enumerate(ppl): s.text(330 + j * 140, 100, p, 13, 700, NAVY, 'middle')
    for i, (t, v) in enumerate(rows):
        y = 114 + i * 50; gap = v == 'BBB'
        s.text(40, y + 28, t, 13.5, 700, WARN if gap else INK)
        for j, c in enumerate(v):
            strong = c == 'S'
            s.rect(266 + j * 140, y + 4, 128, 38, OK if strong else (WARN_S if gap else PAPER2), OK if strong else (WARN if gap else LINE), 8)
            s.text(330 + j * 140, y + 28, 'Strong' if strong else 'Basic', 12.5, 700, WHITE if strong else (WARN if gap else INK2), 'middle')
    s.rect(28, 312, 704, 46, 'none', WARN, 10, 1.6, '6 4')
    s.note(366, 'Gap: nobody is strong in analytics → training or new hire before a metrics-driven redesign.')
    return s


@reg('ux-28', 'Six storyboard panels of Ravi learning Rummy on the bus', 'A short visual story shows the idea in the user’s real context.')
def d28():
    s = SVG(W, 500, 'Storyboard', '“Learning Rummy on the way home” · illustrative')
    caps = ['Friend recommends · Ravi installs', 'On the bus, unsure of rules', 'Tutorial guides one hand', 'Valid groups highlighted', 'Finishes · feels confident', 'Joins a low-stake table']
    for i, cp in enumerate(caps):
        x = 28 + (i % 3) * 238; y = 80 + (i // 3) * 206
        s.rect(x, y, 226, 196, WHITE, INK2, 8, 1.6)
        s.rect(x + 10, y + 10, 206, 128, PAPER, LINE, 4)
        s.circle(x + 24, y + 24, 12, NAVY, NAVY); s.text(x + 24, y + 28, str(i + 1), 11, 800, WHITE, 'middle')
        px, py = x + 70, y + 74
        s.circle(px, py - 22, 12, 'none', INK, 2); s.path(f'M {px} {py-10} L {px} {py+24} M {px} {py+24} L {px-12} {py+48} M {px} {py+24} L {px+12} {py+48} M {px} {py} L {px+24} {py+8}', INK, 2)
        s.rect(px + 22, py - 4, 16, 26, WHITE, INK, 3, 1.6)
        face = ['', '?', '', '', '', ''][i]
        if i == 0:
            s.circle(px + 90, py - 22, 12, 'none', INK3, 2); s.path(f'M {px+90} {py-10} L {px+90} {py+24}', INK3, 2)
            s.rect(px + 40, py - 60, 90, 24, HL_S, HL_L, 12); s.text(px + 85, py - 44, 'Try this!', 11, 700, WARN, 'middle')
        if i == 1:
            s.rect(x + 120, y + 24, 86, 54, PAPER2, INK3, 8); s.rect(x + 128, y + 32, 30, 22, WHITE, LINE, 3); s.rect(x + 166, y + 32, 30, 22, WHITE, LINE, 3)
            s.text(x + 163, y + 72, 'BUS', 10.5, 800, INK3, 'middle'); s.circle(x + 136, y + 84, 6, INK3, INK3); s.circle(x + 190, y + 84, 6, INK3, INK3)
            s.text(px + 46, py - 26, '?', 26, 800, WARN)
        if i in (2, 3):
            s.rect(x + 120, y + 30, 86, 98, WHITE, INDIGO, 8)
            for k in range(3): s.rect(x + 128 + k * 26, y + 70, 22, 32, OK_S if i == 3 else WHITE, OK if i == 3 else LINE, 3)
            s.text(x + 163, y + 52, 'Tutorial' if i == 2 else 'Valid set ✓', 10.5, 700, INDIGO if i == 2 else OK, 'middle')
        if i == 4:
            s.text(px + 46, py - 12, '✓', 26, 800, OK); s.rect(x + 120, y + 40, 88, 26, OK_S, OK, 13); s.text(x + 164, y + 58, 'Well played!', 11, 700, OK, 'middle')
        if i == 5:
            s.rect(x + 116, y + 30, 92, 92, '#0f3d2e', '#0f3d2e', 46); s.text(x + 162, y + 72, '₹1', 14, 800, '#f2c75c', 'middle'); s.text(x + 162, y + 90, 'table', 11, 600, WHITE, 'middle')
        s.wrap(x + 113, y + 160, 200, cp, 12.5, 600, INK, 'middle')
    return s


@reg('ux-29', 'Style guide sheet with colours, type scale, buttons and icons', 'Document visual rules so every screen looks the same.')
def d29():
    s = SVG(W, 460, 'Style Guide', 'Classic Rummy · visual standards (illustrative)')
    s.text(28, 100, 'COLOURS', 11, 800, INK3)
    cols = [('#0f3d2e', 'Primary', '#0F3D2E'), ('#f2c75c', 'Secondary', '#F2C75C'), ('#a3365f', 'Hearts red', '#A3365F'), ('#1f2328', 'Text', '#1F2328'), ('#faf6ec', 'Surface', '#FAF6EC')]
    for i, (c, n, h) in enumerate(cols):
        x = 28 + i * 84
        s.rect(x, 110, 74, 60, c, LINE, 8); s.text(x, 188, n, 11.5, 700, INK); s.text(x, 204, h, 10.5, 500, INK3)
    s.text(470, 100, 'TYPOGRAPHY', 11, 800, INK3)
    for i, (sz, w, t) in enumerate([(26, 800, 'H1 · 26 Bold'), (18, 700, 'H2 · 18 Bold'), (14, 500, 'Body · 14 Regular'), (11, 600, 'CAPTION · 11')]):
        s.text(470, 128 + sum([30, 26, 22, 18][:i]) + 4, t, sz, w, NAVY if i < 2 else INK2)
    s.text(28, 246, 'BUTTONS', 11, 800, INK3)
    s.rect(28, 258, 120, 40, '#0f3d2e', '#0f3d2e', 20); s.text(88, 283, 'Primary', 13, 700, WHITE, 'middle')
    s.rect(160, 258, 120, 40, '#f2c75c', '#f2c75c', 20); s.text(220, 283, 'Secondary', 13, 700, '#0b2e22', 'middle')
    s.rect(292, 258, 120, 40, WHITE, '#0f3d2e', 20, 1.6); s.text(352, 283, 'Outline', 13, 700, '#0f3d2e', 'middle')
    s.rect(28, 308, 120, 40, PAPER2, PAPER2, 20); s.text(88, 333, 'Disabled', 13, 700, INK3, 'middle')
    s.text(470, 246, 'ICONS & CARDS', 11, 800, INK3)
    for i in range(4):
        x = 470 + i * 50; s.rect(x, 258, 40, 40, WHITE, LINE, 10)
    s.circle(490, 278, 8, 'none', '#0f3d2e', 2); s.path('M 528 270 L 548 270 L 548 288 L 528 288 Z M 528 276 L 548 276', '#0f3d2e', 2)
    s.path('M 580 268 L 584 276 L 592 277 L 586 282 L 588 290 L 580 286 L 572 290 L 574 282 L 568 277 L 576 276 Z', '#0f3d2e', 1.8)
    s.path('M 620 270 L 640 270 M 620 278 L 640 278 M 620 286 L 634 286', '#0f3d2e', 2)
    s.rect(470, 308, 58, 44, WHITE, INK2, 5); s.text(478, 326, 'A', 14, 800, '#a3365f'); s.text(500, 344, '♥', 14, 700, '#a3365f')
    s.rect(536, 308, 58, 44, WHITE, INK2, 5); s.text(544, 326, 'K', 14, 800, INK); s.text(566, 344, '♠', 14, 700, INK)
    s.note(400, 'Style guide = visual rules. A design system adds coded components, tokens and patterns.')
    return s


@reg('ux-30', 'Usability report summary with findings and severity', 'Findings, severity and recommendations from testing with 10 participants.')
def d30():
    s = SVG(W, 430, 'Usability Report', 'Classic Rummy onboarding · 10 participants')
    st = [('10', 'participants'), ('6/10', 'completed first game'), ('3', 'key findings')]
    for i, (n, t) in enumerate(st):
        x = 28 + i * 240
        s.rect(x, 84, 224, 70, WHITE, LINE, 12); s.text(x + 18, y := 128, n, 26, 800, NAVY); s.text(x + 18 + len(n) * 16 + 10, 126, t, 12.5, 600, INK2)
    rows = [('Users cannot understand OTP errors', 'High', 8, 'Improve error messages'), ('Users struggle with card arrangement', 'High', 7, 'Add guided instructions'),
            ('Users miss the help option', 'Medium', 4, 'Make help more visible')]
    s.text(40, 186, 'FINDING', 11, 800, INK3); s.text(352, 186, 'SEVERITY', 11, 800, INK3); s.text(452, 186, 'USERS AFFECTED', 11, 800, INK3); s.text(596, 186, 'FIX', 11, 800, INK3)
    for i, (f, sv, n, rec) in enumerate(rows):
        y = 198 + i * 62; hi = sv == 'High'
        s.rect(28, y, 704, 54, WHITE, LINE, 10)
        s.wrap(40, y + 23, 290, f, 13, 600, INK)
        s.rect(352, y + 15, 72, 24, WARN if hi else HL, WARN if hi else HL_L, 12); s.text(388, y + 32, sv, 11.5, 800, WHITE if hi else WARN, 'middle')
        for k in range(10): s.circle(458 + k * 13, y + 27, 5, (WARN if hi else HL_L) if k < n else PAPER2, 'none', 0)
        s.wrap(596, y + 23, 130, rec, 12, 600, OK)
    s.note(386, 'Each finding = evidence + severity + a clear recommendation, then retest.')
    return s


@reg('ux-31', 'User-story map with activities backbone, stories and a release line', 'Activities across the top, stories below, cut into releases.')
def d31():
    s = SVG(W, 480, 'User-Story Map', 'Classic Rummy · activity: play a game')
    acts = [('Access game', ['Open app', 'Login', 'Verify OTP']), ('Discover', ['Enter lobby', 'Browse tables', 'Filter by fee']), ('Join game', ['Select table', 'View rules', 'Entry details']),
            ('Play', ['Arrange cards', 'Make moves', 'Declare']), ('Complete', ['Finish game', 'View result', 'History'])]
    s.text(28, 98, 'BACKBONE', 10.5, 800, INK3)
    for i, (a, st) in enumerate(acts):
        x = 28 + i * 142
        s.box(x, 106, 132, 44, a, None, NAVY, NAVY, WHITE, 13, 700, 8)
        if i < 4: s.arrow(x + 132, 128, x + 142, 128, INK2)
        for j, t in enumerate(st):
            y = 170 + j * 66 + (24 if j >= 2 else 0)
            sticky(s, x + 6, y, t, [INDIGO_S, INDIGO_S, HL_S][j], 120, 50)
    s.line(28, 304, 732, 304, OK, 2.2, '8 5'); s.rect(620, 294, 112, 20, PAPER, PAPER, 6); s.text(728, 309, 'Release 1 (MVP)', 11.5, 800, OK, 'end')
    s.text(28, 396, 'Release 2', 11.5, 800, WARN)
    s.note(430, 'Release 1 = the thinnest slice that lets a player complete a whole game.')
    return s


@reg('ux-32', 'UX roadmap with Now, Next and Future columns', 'Plan experience improvements in time horizons, not fixed dates.')
def d32():
    s = SVG(W, 380, 'UX Roadmap', 'Classic Rummy · experience priorities')
    cols = [('NOW', ['Improve onboarding', 'Fix usability issues', 'Gameplay clarity'], OK_S, OK), ('NEXT', ['Improve accessibility', 'Redesign wallet', 'Expand design system'], INDIGO_S, INDIGO),
            ('FUTURE', ['Personalised learning', 'Advanced player insights', 'Intelligent assistance'], PAPER2, INK2)]
    for i, (t, items, f, c) in enumerate(cols):
        x = 28 + i * 240
        s.add(f'<path d="M {x} 84 L {x+206} 84 L {x+226} 108 L {x+206} 132 L {x} 132 L {x+16} 108 Z" fill="{c}"/>')
        s.text(x + 113, 114, t, 15, 800, WHITE, 'middle')
        for j, it in enumerate(items):
            s.box(x + 8, 148 + j * 66, 206, 54, it, None, f, c, INK, 13, 600, 10)
    s.text(28, 360, 'Certainty decreases →  revisit the roadmap as evidence comes in', 12, 600, INK3)
    return s


@reg('ux-33', 'Wireflow of registration screens with success and error paths', 'Wireframes + arrows: screens and the logic between them.')
def d33():
    s = SVG(W, 470, 'Wireflow', 'Classic Rummy · registration')
    scr = [('Welcome', 28), ('Mobile no.', 178), ('OTP', 328), ('Profile', 478), ('Lobby', 628)]
    for t, x in scr:
        X, Y, Wd, H = phone(s, x, 84, 104, 180, WHITE, INK3)
        s.text(X + Wd / 2, Y + 14, t, 11, 800, NAVY, 'middle')
        for r in range(3): s.rect(X + 4, Y + 26 + r * 16, Wd - 8 - r * 18, 8, PAPER2, PAPER2, 4)
        if t == 'OTP':
            for k in range(4): s.rect(X + 6 + k * 20, Y + 80, 16, 20, WHITE, INK3, 3)
        s.rect(X + 4, Y + H - 28, Wd - 8, 22, NAVY, NAVY, 11)
    for i in range(4):
        x = scr[i][1] + 104; s.arrow(x + 2, 174, x + 44, 174, OK, 2)
    s.box(300, 330, 160, 54, 'Wrong OTP', 'show error, keep input', WARN_S, WARN, WARN, 12.5, 700, 10, 11)
    s.arrow(380, 266, 380, 326, WARN, 1.8, '5 4'); s.path('M 300 357 C 250 357, 250 300, 340 268', WARN, 1.8, 'none', '5 4')
    s.box(500, 330, 140, 54, 'Resend OTP', 'timer 30s', HL_S, HL_L, WARN, 12.5, 700, 10, 11)
    s.path('M 460 357 L 500 357', HL_L, 1.8); s.path('M 570 330 C 570 290, 440 300, 420 268', HL_L, 1.8, 'none', '5 4')
    s.box(100, 330, 160, 54, 'Registration fails', 'retry / contact support', WARN_S, WARN, WARN, 12.5, 700, 10, 11)
    s.arrow(230, 266, 190, 326, WARN, 1.8, '5 4')
    s.line(28, 420, 60, 420, OK, 2); s.text(68, 424, 'Success path', 11.5, 600, INK2)
    s.line(180, 420, 212, 420, WARN, 1.8, '5 4'); s.text(220, 424, 'Error / alternative path', 11.5, 600, INK2)
    return s


@reg('ux-34', 'Grey-box wireframe of the gameplay screen with labelled areas', 'Layout and hierarchy only – no colours or decoration yet.')
def d34():
    s = SVG(W, 500, 'Wireframe', 'Classic Rummy · gameplay screen (low fidelity)')
    X, Y = 200, 84; w, h = 360, 390
    s.rect(X, Y, w, h, WHITE, INK2, 14, 1.6)
    areas = [(1, 'Top navigation', X + 10, Y + 10, w - 20, 34), (2, 'Player info', X + 10, Y + 54, w - 20, 40), (3, 'Game table', X + 10, Y + 104, w - 20, 120),
             (6, 'Timer', X + w - 74, Y + 114, 54, 30), (4, 'Card area', X + 10, Y + 234, w - 20, 64), (5, 'Action buttons', X + 10, Y + 308, w - 20, 34), (7, 'Bottom navigation', X + 10, Y + 352, w - 20, 28)]
    for n, t, x, y, ww, hh in areas:
        s.rect(x, y, ww, hh, PAPER2 if n != 6 else WHITE, INK3, 6, 1.2)
        if n == 3: s.path(f'M {x} {y} L {x+ww} {y+hh} M {x+ww} {y} L {x} {y+hh}', LINE, 1.2)
        if n == 4:
            for k in range(9): s.rect(x + 12 + k * 36, y + 10, 30, 44, WHITE, INK3, 3)
        if n == 5:
            for k, b in enumerate(['Drop', 'Group', 'Discard', 'Declare']): s.rect(x + 6 + k * 84, y + 5, 76, 24, WHITE, INK3, 12); s.text(x + 44 + k * 84, y + 21, b, 10.5, 600, INK2, 'middle')
    labels = [(1, Y + 27, 'L'), (2, Y + 74, 'L'), (3, Y + 164, 'L'), (4, Y + 266, 'L'), (5, Y + 325, 'R'), (6, Y + 129, 'R'), (7, Y + 366, 'R')]
    names = {1: 'Top navigation', 2: 'Player info', 3: 'Game table', 4: 'Card area', 5: 'Action buttons', 6: 'Timer', 7: 'Bottom navigation'}
    for n, y, side in labels:
        if side == 'L':
            s.line(150, y, X + 10, y, INK3, 1, '3 3'); s.circle(140, y, 11, HL, HL_L); s.text(140, y + 4, str(n), 11, 800, NAVY, 'middle'); s.text(124, y + 4, names[n], 12, 700, NAVY, 'end')
        else:
            s.line(X + w - 10, y, 610, y, INK3, 1, '3 3'); s.circle(620, y, 11, HL, HL_L); s.text(620, y + 4, str(n), 11, 800, NAVY, 'middle'); s.text(636, y + 4, names[n], 12, 700, NAVY)
    return s


@reg('ux-35', 'Flowchart from opening the app to joining a table, with decisions', 'Steps, decisions and alternative paths to complete one goal.')
def d35():
    s = SVG(W, 630, 'User Flow', 'Classic Rummy · goal: join a game table')
    def node(x, y, t, kind='step'):
        if kind == 'term':
            s.box(x - 80, y - 20, 160, 40, t, None, NAVY, NAVY, WHITE, 12.5, 700, 20)
        elif kind == 'dec':
            s.add(f'<path d="M {x} {y-34} L {x+92} {y} L {x} {y+34} L {x-92} {y} Z" fill="{HL_S}" stroke="{HL_L}" stroke-width="1.6"/>')
            s.wrap(x, y - 2, 120, t, 11.5, 700, WARN, 'middle')
        else:
            s.box(x - 80, y - 20, 160, 40, t, None, WHITE, INDIGO, INK, 12, 600, 8)
    C, R = 300, 590
    ys = [100, 158, 222, 290, 346, 402, 470, 538, 594]
    node(C, ys[0], 'START', 'term'); node(C, ys[1], 'Open Classic Rummy'); node(C, ys[2], 'Logged in?', 'dec')
    node(C, ys[3], 'Enter lobby'); node(C, ys[4], 'Select game type'); node(C, ys[5], 'Select table')
    node(C, ys[6], 'Eligible? balance · KYC', 'dec'); node(C, ys[7], 'Join table'); node(C, ys[8], 'END – game started', 'term')
    node(R, ys[2], 'Login / Register'); node(R, ys[6], 'Add money / complete KYC')
    for a, b in [(0, 1), (1, 2), (3, 4), (4, 5), (5, 6), (7, 8)]:
        top = ys[a] + (34 if a in (2, 6) else 20); bot = ys[b] - (34 if b in (2, 6) else 20)
        s.arrow(C, top, C, bot - 2)
    s.arrow(C, ys[2] + 34, C, ys[3] - 22, OK); s.text(C - 10, ys[2] + 50, 'Yes', 11.5, 700, OK, 'end')
    s.arrow(C, ys[6] + 34, C, ys[7] - 22, OK); s.text(C - 10, ys[6] + 50, 'Yes', 11.5, 700, OK, 'end')
    s.arrow(C + 92, ys[2], R - 82, ys[2], WARN); s.text(C + 104, ys[2] - 8, 'No', 11.5, 700, WARN)
    s.path(f'M {R} {ys[2]+20} L {R} {ys[3]} L {C+84} {ys[3]}', INK2, 1.6); s.arrow(C + 96, ys[3], C + 82, ys[3])
    s.arrow(C + 92, ys[6], R - 82, ys[6], WARN); s.text(C + 104, ys[6] - 8, 'No', 11.5, 700, WARN)
    s.path(f'M {R} {ys[6]-20} L {R} {ys[5]} L {C+96} {ys[5]}', INK2, 1.6, 'none', '5 4'); s.arrow(C + 98, ys[5], C + 82, ys[5], INK2)
    s.text(R - 10, ys[5] - 8, 'try again', 11, 600, INK3, 'end')
    return s
