import sys, re, pickle
sys.path.insert(0, '/home/claude/tools')
from pages_pdf_extract import Extractor

def assemble(path):
    E = Extractor(path); out = []          # list of blocks: ('p', text) | ('h', text, size) | ('t', rows)
    last_y = None; last_page = -1
    for pno in range(len(E.doc)):
        for it in E.page_items(pno):
            if it[0] == 'table':
                rows = [[c.replace('Questio n', 'Question') for c in r] for r in it[1]]
                if out and out[-1][0] == 't' and (pno != last_page or True) and _first_on_page:
                    out[-1][1].extend(rows)
                elif out and out[-1][0] == 'hdr':
                    out[-1] = ('t', [out[-1][1]] + rows)
                else:
                    out.append(('t', rows))
                last_y = it[3]; last_page = pno; _first_on_page = False
                continue
            _, txt, y, _, bold, size = it
            txt = txt.strip()
            newpage = pno != last_page
            if newpage: _first_on_page = True
            heading = bold and size >= 18
            if bold and size < 18 and out and out[-1][0] == 'h' and out[-1][1].startswith('Quick Revision'):
                out.append(('hdr', [txt.replace('topicKey', 'topic\tKey').split('\t')[0], txt.split('topicKey')[-1] if 'topicKey' in txt else ''])); 
                out[-1] = ('hdr', ['Interview topic', 'Key points to remember']) if 'topicKey' in txt else out[-1]
                last_y, last_page = y, pno; _first_on_page = False; continue
            startlist = re.match(r'^(•|\d+\.)\s', txt)
            prev = out[-1] if out else None
            if heading:
                if prev and prev[0] == 'h' and not newpage and y - last_y < 34 and not re.match(r'^Q\d+\.', txt):
                    out[-1] = ('h', _join(prev[1], txt), size)
                else: out.append(('h', txt, size))
            elif re.match(r'^Part \d+ – ', txt):
                out.append(('h', txt, 24))
            else:
                cont = False
                if prev and prev[0] == 'p' and not startlist:
                    if not newpage and y - last_y <= 21: cont = True
                    elif newpage and not re.search(r'[.:?!”"]$', prev[1]) and not re.match(r'^(Scenario|English|తెలుగు)', txt): cont = True
                if cont: out[-1] = ('p', _join(prev[1], txt))
                else: out.append(('p', txt))
            last_y, last_page = y, pno; _first_on_page = False
    print('font fallbacks:', getattr(E, 'fallbacks', 0), 'reattached vattu:', getattr(E, 'reattached', 0), file=sys.stderr)
    return out

def _join(a, b):
    if re.search(r'[A-Za-z]-$', a): return a + b
    return a + ' ' + b

def to_text(blocks):
    L = []
    for b in blocks:
        if b[0] == 'h':
            L += ['', b[1]]
        elif b[0] == 't':
            L += ['\t'.join(c.strip() for c in r) for r in b[1]]
        elif b[0] == 'hdr':
            L += ['\t'.join(b[1])]
        else:
            t = b[1]
            t = re.sub(r'^•\s+', '- ', t)
            L.append(t)
    return '\n'.join(L).strip() + '\n'

if __name__ == '__main__':
    blocks = assemble(sys.argv[1])
    open(sys.argv[2], 'w', encoding='utf-8').write(to_text(blocks))
