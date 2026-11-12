import sys, os, importlib
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
import pathlib; OUT = str(pathlib.Path(__file__).resolve().parents[2] / 'assets/images/ux')
os.makedirs(OUT, exist_ok=True)
F = {}
for m in sys.argv[1:]:
    F.update(importlib.import_module(m).F)
for k, (fn, alt, cap) in F.items():
    open(f'{OUT}/{k}.svg', 'w').write(fn().render())
print(len(F), 'figures')
