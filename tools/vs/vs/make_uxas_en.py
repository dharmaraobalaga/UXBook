"""Build uxas_en.txt from uxas_te.txt: drop each 'తెలుగులో అర్థం:' block (the PDF's English Explanation that follows covers it),
keep English lines, replace remaining Telugu lines from uxas_en_map.M (None = drop)."""
import re, pathlib, sys
HERE = pathlib.Path(__file__).parent
lines = (HERE / 'uxas_te.txt').read_text().split('\n')
keep = []; skip = False
for i, l in enumerate(lines):
    if l.strip() == 'తెలుగులో అర్థం:': skip = True; continue
    if skip and (l.startswith('English Explanation:') or l.startswith('### ') or re.match(r'^\d\.\d ', l)): skip = False
    if not skip: keep.append((i, l))
if len(sys.argv) > 1 and sys.argv[1] == 'list':
    for i, l in keep:
        if re.search(r'[ఀ-౿]', l): print(i, '|', l)
    raise SystemExit
from uxas_en_map import M
out = []
for i, l in keep:
    if re.search(r'[ఀ-౿]', l):
        if i not in M: raise SystemExit(f'missing {i}: {l}')
        if M[i] is None: continue
        out.append(M[i])
    else: out.append(l)
t = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
(HERE / 'uxas_en.txt').write_text(t)
print('ok', len(t), 'telugu left:', len(re.findall(r'[ఀ-౿]', t)))
