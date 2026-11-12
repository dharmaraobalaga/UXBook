"""Extract Apple-Pages PDF (Telugu+English) into the handbook .txt format."""
import sys, re, collections
sys.path.insert(0, '/home/claude/tools')
from te_decode import fitz, Decoder, decode_glyphs, parse

def te(u): return 0x0C00 <= u <= 0x0C7F

class Extractor:
    def __init__(self, path):
        self.doc = fitz.open(path); self.dec = Decoder(self.doc)
        from fontmap import page_fontmaps
        self.fmaps = page_fontmaps(path)
    def exact_fonts(self, page):
        bf = {f[3]: f[0] for f in page.get_fonts(full=True)}
        return {(round(x, 1), round(y, 1)): bf.get(fn) for x, y, fn in self.fmaps[page.number]}
    def font_candidates(self, page, fname):
        return [f[0] for f in page.get_fonts(full=True) if f[3].split('+')[-1] == fname]
    def pick_font(self, page, span):
        cands = self.font_candidates(page, span['font'])
        if len(cands) == 1: return cands[0]
        best, bs = cands[0], None
        for x in cands:
            gu = self.dec.gid_unicode(x); names = self.dec.glyphnames(x); s = 0
            for u, g, *_ in span['chars']:
                if u == 0x20: continue
                if g >= len(names): s -= 100; continue
                if g in gu and u > 0 and u != 0xFFFD: s += 1 if gu[g] == chr(u) else -10
            if bs is None or s > bs: best, bs = x, s
        return best
    def pieces(self, page):
        """decoded text pieces with geometry: (x0, ybase, x1, text, bold, size)"""
        out = []
        tr = page.get_texttrace(); flat = [(si, ci, c) for si, sp in enumerate(tr) for ci, c in enumerate(sp['chars'])]
        zw = set()
        for k, (si, ci, c) in enumerate(flat[:-1]):
            n = flat[k + 1][2]
            if c[0] == 0x20 and abs(n[2][1] - c[2][1]) < 2 and abs(n[2][0] - c[2][0]) < 0.5: zw.add((si, ci))
        ex = self.exact_fonts(page); self.fallbacks = getattr(self, 'fallbacks', 0)
        pend = []   # Telugu glyph run that may span several spans / font subsets
        def flush_te():
            if pend:
                # re-attach vattu glyphs drawn out of stream order to the base they sit under
                fixed = []
                for q in pend:
                    if q[0].split('.')[0].endswith('c2') or 'lengthmark' in q[0]:
                        if fixed and q[1][2][0] < fixed[-1][1][2][0] - 1:
                            k = max((i for i, f in enumerate(fixed) if f[1][2][0] <= q[1][2][0] + 0.5 and not f[0].split('.')[0].endswith('c2') and 'lengthmark' not in f[0] and f[0] not in ('space', 'zwnj')), default=None)
                            if k is not None:
                                j = k + 1
                                while j < len(fixed) and fixed[j][0].split('.')[0].endswith('c2'): j += 1
                                fixed.insert(j, q); self.reattached = getattr(self, 'reattached', 0) + 1; continue
                    fixed.append(q)
                pend[:] = fixed
                txt = decode_glyphs([q[0] for q in pend])
                out.append((pend[0][1][2][0], round(pend[0][1][2][1], 1), pend[-1][1][3][2], txt, pend[0][2], pend[0][3]))
                pend.clear()
        for si, sp in enumerate(tr):
            chars = sp['chars']
            if not chars: continue
            bold = 'Bold' in sp['font']
            if 'Telugu' in sp['font']:
                fallback = None
                for ci, c in enumerate(chars):
                    x = ex.get((round(c[2][0], 1), round(c[2][1], 1)))
                    if x is None:
                        if fallback is None: fallback = self.pick_font(page, sp)
                        x = fallback; self.fallbacks += 1
                    names = self.dec.glyphnames(x)
                    nm = (('zwnj' if (si, ci) in zw else 'space') if c[0] == 0x20 else names[c[1]])
                    is_c2 = nm.split('.')[0].endswith('c2') or 'lengthmark' in nm
                    if pend and not is_c2:
                        base_y = next((q[1][2][1] for q in reversed(pend) if not (q[0].split('.')[0].endswith('c2') or 'lengthmark' in q[0])), pend[-1][1][2][1])
                        if abs(c[2][1] - base_y) > 2: flush_te()
                    elif pend and is_c2 and abs(c[2][1] - pend[-1][1][2][1]) > 12: flush_te()
                    pend.append((nm, c, bold, sp['size']))
                continue
            # non-Telugu span: a run of plain spaces between Telugu spans is kept inside the run
            if pend and all(c[0] == 0x20 for c in chars) and abs(chars[0][2][1] - pend[-1][1][2][1]) <= 2:
                for ci, c in enumerate(chars): pend.append((('zwnj' if (si, ci) in zw else 'space'), c, bold, sp['size']))
                continue
            flush_te()
            cur = []
            for ci, c in enumerate(chars):
                if cur and abs(c[2][1] - cur[-1][1][2][1]) > 2:
                    out.append((cur[0][1][2][0], round(cur[0][1][2][1], 1), cur[-1][1][3][2], ''.join(x for x, _ in cur), bold, sp['size'])); cur = []
                ch = ('\u200c' if (si, ci) in zw else ' ') if c[0] == 0x20 else (chr(c[0]) if c[0] > 0 else '')
                cur.append((ch, c))
            if cur: out.append((cur[0][1][2][0], round(cur[0][1][2][1], 1), cur[-1][1][3][2], ''.join(x for x, _ in cur), bold, sp['size']))
        flush_te()
        return out
    @staticmethod
    def join_line(ps):
        ps = sorted(ps, key=lambda p: p[0]); s = ''
        for i, p in enumerate(ps):
            if i and p[0] - ps[i-1][2] > 6 and not s.endswith(' ') and re.fullmatch(r'\s*(•|\d+\.|[a-z]\.)\s*', s): s += ' '   # bullet/number tab
            s += p[3]
        return s.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff')
    def page_items(self, pno):
        """returns list of items in reading order: ('text', line_str, y_top, y_bot, bold, size) or ('table', rows)"""
        page = self.doc[pno]; ps = self.pieces(page)
        tabs = page.find_tables().tables
        items = []; used = set()
        for t in tabs:
            rows = []
            for r in t.rows:
                cells = []
                for cb in r.cells:
                    if cb is None: cells.append(''); continue
                    x0, y0, x1, y1 = cb
                    inside = [i for i, p in enumerate(ps) if x0 - 1 <= p[0] <= x1 and y0 - 1 <= p[1] <= y1 + 1]
                    used.update(inside)
                    lines = collections.defaultdict(list)
                    for i in inside: lines[round(ps[i][1])].append(ps[i])
                    cells.append(' '.join(self.join_line(v).strip() for k, v in sorted(lines.items())).replace('  ', ' ').strip())
                rows.append(cells)
            items.append(('table', rows, t.bbox[1], t.bbox[3]))
        # remaining pieces -> lines
        lines = collections.defaultdict(list)
        for i, p in enumerate(ps):
            if i in used: continue
            key = None
            for k in lines:
                if abs(k - p[1]) <= 2.5: key = k; break
            lines[key if key is not None else p[1]].append(p)
        for y, v in lines.items():
            txt = self.join_line(v)
            if not txt.strip(): continue
            items.append(('text', txt.rstrip(), y, y, all(p[4] for p in v if p[3].strip()), max(p[5] for p in v)))
        items.sort(key=lambda it: it[2])
        return items
