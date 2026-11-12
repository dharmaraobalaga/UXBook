import json, sys
sys.path.insert(0, '.')
from figs_a import F as A; from figs_b import F as B; from figs_c import F as C
from captions_te import CAP_TE
F = {**A, **B, **C}
P = '/home/claude/interview-mastery/data/raw/ux-process.json'
parts = json.load(open(P)); n = 0
for part in parts:
    for q in part['questions']:
        k = q['questionId']
        if k in F:
            _, alt, cap = F[k]
            q['figure'] = {'src': f'assets/images/ux/{k}.svg', 'alt': alt, 'caption': cap, 'captionTelugu': CAP_TE[k], 'top': True}; n += 1
json.dump(parts, open(P, 'w'), ensure_ascii=False, indent=1)
print('attached', n)
