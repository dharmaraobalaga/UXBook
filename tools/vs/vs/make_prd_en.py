"""Build prd_en.txt from prd_te.txt: English lines are kept, Telugu lines are replaced from prd_en_map.M (None = dropped)."""
import re, pathlib
from prd_en_map import M
HERE = pathlib.Path(__file__).parent
lines = (HERE / 'prd_te.txt').read_text().split('\n')
out = []
for i, l in enumerate(lines):
    if re.search(r'[ఀ-౿]', l):
        if i not in M: raise SystemExit(f'missing translation for line {i}: {l}')
        if M[i] is None: continue
        out.append(M[i])
    else:
        out.append(l)
t = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))
(HERE / 'prd_en.txt').write_text(t)
print('ok', len(t), 'telugu left:', len(re.findall(r'[ఀ-౿]', t)))
