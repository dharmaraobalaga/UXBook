from svgkit import *

F = {}
def reg(key, alt, cap, cap_te):
    def deco(fn):
        F[key] = (fn, alt, cap, cap_te); return fn
    return deco
W = 760


@reg('st-p1-map', 'Phase 1 map: inputs, nine activities, deliverables and the handoff to Phase 2',
     'Phase 1 turns inputs into evidence through nine steps, then hands off to Phase 2.',
     'Phase 1 లో 9 steps ద్వారా inputs ను evidence గా మార్చి, Phase 2 కు అందిస్తాం.')
def p1map():
    s = SVG(W, 560, 'Phase 1 · Discovery & Research', 'Inputs → activities → deliverables → Phase 2')
    s.text(28, 96, 'INPUTS', 11, 800, INK3)
    for i, t in enumerate(['Project brief', 'Business goals', 'Analytics & tickets', 'Stakeholders', 'Users', 'Competitors']):
        s.box(28, 106 + i * 54, 140, 42, t, None, WHITE, LINE, INK, 12, 600, 8)
    s.arrow(172, 268, 200, 268, INDIGO, 2.2)
    s.text(206, 96, 'ACTIVITIES (STEPS 1.2 – 1.10)', 11, 800, INK3)
    acts = ['1.2 Kickoff & stakeholders', '1.3 Research plan', '1.4 Analytics & tickets', '1.5 Competitive review', '1.6 User interviews',
            '1.7 CSD Matrix', '1.8 Ecosystem map', '1.9 Empathy map', '1.10 Findings']
    for i, t in enumerate(acts):
        col, row = i % 2, i // 2
        f = OK_S if i == 8 else INDIGO_S
        s.box(206 + col * 168, 106 + row * 66, 158, 54, t, None, f, OK if i == 8 else INDIGO_M, NAVY, 12, 700, 10)
    s.arrow(540, 268, 568, 268, INDIGO, 2.2)
    s.rect(574, 86, 158, 330, NAVY, NAVY, 14)
    s.text(653, 116, 'PHASE 2', 12, 800, HL, 'middle')
    s.text(653, 138, 'Define & Synthesize', 12.5, 700, WHITE, 'middle')
    for i, t in enumerate(['Affinity diagram', 'Personas', 'Journey map', 'Problem statements', 'HMW questions']):
        s.box(588, 160 + i * 48, 130, 38, t, None, '#2a3560', '#2a3560', WHITE, 11.5, 600, 8)
    s.note(436, 'Exit: key questions answered with evidence · facts vs assumptions separated · team agrees on top opportunities.')
    s.text(28, 512, 'Evidence first, solutions later. Discovery repeats in every iteration.', 12.5, 600, INK2)
    return s


@reg('st-funnel', 'Funnel bars from install to first game, and ResolveAI baseline metrics',
     'Analytics shows where users drop; interviews explain why.',
     'Analytics "ఎక్కడ" ఆగుతున్నారో చూపిస్తుంది; interviews "ఎందుకు" అని చెబుతాయి.')
def funnel():
    s = SVG(W, 470, 'Analytics & support review', 'Illustrative numbers · learning example')
    s.text(28, 98, 'CLASSIC RUMMY · NEW-PLAYER FUNNEL', 11, 800, INK3)
    steps = [('Install', 100), ('Registration', 62), ('Verification', 38), ('First game', 21)]
    for i, (t, v) in enumerate(steps):
        y = 112 + i * 52
        s.text(28, y + 27, t, 13, 700, INK)
        s.rect(150, y + 8, 300, 30, PAPER2, PAPER2, 6)
        s.rect(150, y + 8, 3 * v, 30, INDIGO if i < 3 else OK, INDIGO if i < 3 else OK, 6)
        s.text(158 + 3 * v, y + 29, f'{v}%', 13, 800, NAVY)
    s.rect(150, 160, 300, 64, 'none', WARN, 8, 1.8, '6 4')
    s.text(460, 196, '−24 pts: biggest drop', 12, 800, WARN)
    s.text(28, 342, 'TOP SUPPORT TICKETS', 11, 800, INK3)
    for i, (t, v) in enumerate([('Deposit pending', 31), ('Rules confusion', 22), ('KYC rejected', 18)]):
        y = 354 + i * 30
        s.text(28, y + 16, t, 12, 600, INK)
        s.rect(150, y + 4, 4 * v, 16, WARN_S, WARN, 4); s.text(156 + 4 * v, y + 17, f'{v}%', 11.5, 700, WARN)
    s.rect(520, 330, 212, 110, TEAL_S, TEAL, 12)
    s.text(536, 354, 'RESOLVEAI BASELINE', 11, 800, TEAL)
    s.text(536, 380, 'AHT 9 min (refund 14)', 13, 700, NAVY)
    s.text(536, 402, 'AI suggestions used 18%', 13, 700, NAVY)
    s.text(536, 424, '4 tools per ticket', 13, 700, NAVY)
    s.rect(560, 98, 172, 210, HL_S, HL_L, 12)
    s.text(576, 124, 'Data tells WHERE', 13, 800, WARN)
    s.wrap(576, 150, 140, 'Ask WHY in interviews (Step 1.6) before choosing a solution.', 12.5, 600, INK)
    return s
