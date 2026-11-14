import re
TEL = r'[ఀ-౿]'
JOIN = re.compile(r'(ప్రొ|ప్రా|ప్రో|స్తు|స్తా|క్తు|ట్లా|ప్లా|ర్టు|గ్రూ|స్థా|ళ్లా|ర్గా|ళ్తా|ళ్తు|ర్ధా|జ్ఞా|ల్గొ|త్తు(?= లో)|క్టు(?= ల)|ర్డు(?= (?:ను|ల)))(?: +)(?=[\u0C15-\u0C39])')
joins = []
def fix_te(s):
    for m in JOIN.finditer(s):
        joins.append(s[max(0, m.start()-6):m.end()+4])
    s = JOIN.sub(r'\1', s)
    s = re.sub(r' +([,.?])', r'\1', s)
    s = re.sub(r'(?<=\S)  +(?=\S)', ' ', s)
    return s

def blocks(raw_lines, tables=False):
    """Rebuild paragraphs, numbered lists, bullets (indented lines) and 2-column tables from pdftotext -layout lines."""
    out = []  # list of (kind, text)
    for raw in raw_lines + ['']:
        s = raw.strip()
        if not s:
            out.append(('blank', '')); continue
        indent = len(raw) - len(raw.lstrip(' '))
        cells = [c for c in re.split(r'\s{2,}', s) if c]
        if re.match(r'^\d+\.\s', s):
            out.append(('ol', s)); continue
        if tables and re.fullmatch(r'[a-z0-9-]+\.(?:com|org|io|net)', s):
            continue  # image source label (image not copied)
        if tables and indent < 3 and 2 <= len(cells) <= 4:
            out.append(('tr', '\t'.join(cells))); continue
        if re.fullmatch(r'\d{1,2}', s):
            continue  # stray page number
        if indent >= 3:
            prev = next((o for o in reversed(out) if o[0] != 'blank'), None)
            if out and out[-1][0] == 'li' and not re.search(r'[.!?"”):]$', out[-1][1]) and (s[0].islower() or s[0] in '(&' or out[-1][1].endswith(',')):
                out[-1] = ('li', out[-1][1] + ' ' + s); continue
            out.append(('li', s)); continue
        if out and out[-1][0] == 'p' and not out[-1][1].endswith(':'):
            out[-1] = ('p', out[-1][1] + ' ' + s); continue
        out.append(('p', s))
    # group into blocks
    res, block, kind = [], [], None
    def flush():
        nonlocal block
        if block: res.append('\n'.join(block)); block = []
    for k, t in out:
        if k == 'blank':
            if kind in ('li', 'ol', 'tr'): continue  # lists/tables may have blank lines between rows
            flush(); kind = None; continue
        if k in ('li', 'ol', 'tr'):
            if kind not in (k,) : flush() if kind not in ('p',) or not (block and block[-1].endswith(':')) else None
            block.append(('- ' + t) if k == 'li' else t); kind = k; continue
        if kind in ('li', 'ol', 'tr'): flush()
        if kind == 'p' and block and not block[-1].endswith(':'): flush()
        block.append(t); kind = 'p'
    flush()
    return '\n\n'.join(res)

def parse(path, first_heading_no=1):
    lines = open(path).read().replace('\f', '').split('\n')
    items = []; cur = None; sec = None
    head = re.compile(r'^(\d+)\. (.+ vs .+)$')
    for raw in lines:
        l = raw.rstrip()
        m = head.match(l.strip())
        if m and not raw.startswith(' '):
            cur = {'n': int(m.group(1)), 'title': m.group(2).strip(), 'te': [], 'defs': [], 'hdr': None, 'rows': [], 'exTitle': '', 'ex': [], 'iv': [], 'te_raw': [], 'ex_raw': []}
            items.append(cur); sec = None; continue
        if cur is None: continue
        s = l.strip()
        if s.startswith('Group ') and 'Quick Revision' in s: cur = None; continue
        if s == 'తెలుగు వివరణ': sec = 'te'; continue
        if s == 'English Definitions': sec = 'defs'; continue
        if s == 'Key Differences': sec = 'tbl'; continue
        if s.startswith('Practical Example'): sec = 'ex'; cur['exTitle'] = s.split('–', 1)[-1].strip() if '–' in s else ''; continue
        if s.startswith('Interview Answer'): sec = 'iv'; continue
        if sec == 'tbl':
            if not s: continue
            cells = [c.strip() for c in re.split(r'\s{2,}', s) if c.strip()]
            if len(cells) == 2:
                if cur['hdr'] is None: cur['hdr'] = cells
                else: cur['rows'].append(cells)
            continue
        if sec == 'ex':
            cur['ex_raw'].append(l); continue
        if sec in ('defs',):
            if not s: continue
            if re.match(r'^[A-Z][^:]{1,45}:', s) and raw.startswith('   '): cur[sec].append(s)
            elif cur[sec]: cur[sec][-1] += ' ' + s
            continue
        if sec == 'iv':
            if s: cur['iv'].append(s)
            continue
        if sec == 'te':
            cur['te'].append(s); cur['te_raw'].append(l)
    for it in items:
        # Telugu: paragraphs separated by blank lines; join wrapped lines; indented "X = y" lines become bullets
        paras, buf = [], []
        for s in it['te'] + ['']:
            if not s:
                if buf: paras.append(buf); buf = []
                continue
            buf.append(s)
        out = []
        for p in paras:
            if all(re.match(r'^\S+ = ', x) for x in p) and len(p) > 1:
                out.append('\n'.join('- ' + x for x in p))
            elif len(p) > 1 and p[0].endswith(':') and all(re.match(r'^\S+ = ', x) for x in p[1:]):
                out.append(p[0] + '\n' + '\n'.join('- ' + x for x in p[1:]))
            else:
                out.append(' '.join(p))
        it['te_text'] = fix_te(blocks(it['te_raw']))
        it['ex_text'] = blocks(it['ex_raw'], tables=True)
        it['ex'] = [x[2:] for x in it['ex_text'].split('\n') if x.startswith('- ')]
        it['iv_text'] = ' '.join(it['iv']).strip()
    return items
