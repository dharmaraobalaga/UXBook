"""Rebuild Telugu text from Apple Pages PDFs using KohinoorTelugu glyph names."""
import io, re, warnings
warnings.filterwarnings('ignore')
import pymupdf as fitz
from fontTools.cffLib import CFFFontSet

CONS = {'K':'క','KH':'ఖ','G':'గ','GH':'ఘ','NG':'ఙ','C':'చ','CH':'ఛ','J':'జ','JH':'ఝ','NY':'ఞ','TT':'ట','TTH':'ఠ','DD':'డ','DDH':'ఢ','NN':'ణ',
        'T':'త','TH':'థ','D':'ద','DH':'ధ','N':'న','P':'ప','PH':'ఫ','B':'బ','BH':'భ','M':'మ','Y':'య','R':'ర','RR':'ఱ','L':'ల','LL':'ళ',
        'V':'వ','SH':'శ','SS':'ష','S':'స','H':'హ'}
INDEP = {'A':'అ','AA':'ఆ','I':'ఇ','II':'ఈ','U':'ఉ','UU':'ఊ','E':'ఎ','EE':'ఏ','AI':'ఐ','O':'ఒ','OO':'ఓ','AU':'ఔ'}
MATRA = {'A':'','AA':'ా','I':'ి','II':'ీ','U':'ు','UU':'ూ','E':'ె','EE':'ే','AI':'ై','O':'ొ','OO':'ో','AU':'ౌ'}
VIR = '్'

def parse(name):
    """-> (kind, cons, vowel)  kind: indep | cv | dead | c2 | other"""
    n = name[2:] if name.startswith('tl') else None
    if n is None: return ('unknown', name, None)
    n = n.split('.')[0]
    if n == 'Anusvara': return ('other', 'ం', None)
    if n == 'Visarga': return ('other', 'ః', None)
    if n == 'mvR': return ('other', 'ృ', None)
    if n == 'AIlengthmark': return ('aimark', '\u0C56', None)
    if n in INDEP: return ('indep', INDEP[n], None)
    if n.endswith('c2'):
        base = n[:-2]
        assert base.endswith('A'), name
        return ('c2', CONS[base[:-1]], None)
    # consonant + vowel: try longest consonant prefix
    for k in sorted(CONS, key=len, reverse=True):
        if n.startswith(k):
            rest = n[len(k):]
            if rest == '': return ('dead', CONS[k], None)       # tlK = క్
            if rest in MATRA: return ('cv', CONS[k], MATRA[rest])
    return ('unknown', name, None)

class Decoder:
    def __init__(self, doc):
        self.doc = doc; self.names = {}; self.gid_uni = {}
    def gid_unicode(self, xref):
        """gid -> first unicode char this subset's ToUnicode reports for it"""
        if xref in self.gid_uni: return self.gid_uni[xref]
        res = {}
        try:
            obj = self.doc.xref_object(xref)
            m = re.search(r'/Differences \[(.*?)\]', obj, re.S)
            code2name = {}
            if m:
                code = None
                for tok in m.group(1).split():
                    if tok.startswith('/'): code2name[code] = tok[1:]; code += 1
                    else: code = int(tok)
            tu = re.search(r'/ToUnicode (\d+) 0 R', obj)
            code2u = {}
            if tu:
                s = self.doc.xref_stream(int(tu.group(1))).decode('latin-1')
                for blk in re.findall(r'beginbfchar(.*?)endbfchar', s, re.S):
                    for a, b in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
                        code2u[int(a, 16)] = chr(int(b[:4], 16))
                for blk in re.findall(r'beginbfrange(.*?)endbfrange', s, re.S):
                    for a, b, c in re.findall(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
                        for k in range(int(a, 16), int(b, 16) + 1): code2u[k] = chr(int(c[:4], 16) + k - int(a, 16))
            names = self.glyphnames(xref); n2g = {n: i for i, n in enumerate(names)}
            for code, nm in code2name.items():
                if nm in n2g and code in code2u: res[n2g[nm]] = code2u[code]
            # widths by gid
            fc = re.search(r'/FirstChar (\d+)', obj); wd = re.search(r'/Widths \[([^\]]*)\]', obj)
            wmap = {}
            if fc and wd:
                ws = [float(x) for x in wd.group(1).split()]
                for code, nm in code2name.items():
                    k = code - int(fc.group(1))
                    if nm in n2g and 0 <= k < len(ws): wmap[n2g[nm]] = ws[k]
            self.gid_w = getattr(self, 'gid_w', {}); self.gid_w[xref] = wmap
        except Exception as e:
            pass
        self.gid_uni[xref] = res
        return res
    def glyphnames(self, xref):
        if xref not in self.names:
            buf = self.doc.extract_font(xref)[3]
            cff = CFFFontSet(); cff.decompile(io.BytesIO(buf), None)
            self.names[xref] = cff[cff.fontNames[0]].charset
        return self.names[xref]

def decode_glyphs(names):
    """names: list of glyph names in stream order -> unicode string"""
    out = []; i = 0
    while i < len(names):
        k, c, v = parse(names[i])
        if k == 'cv' or k == 'dead':
            j = i + 1; conj = ''
            while j < len(names) and parse(names[j])[0] == 'c2':
                conj += VIR + parse(names[j])[1]; j += 1
            if k == 'dead': out.append(c + conj + VIR)   # క్ / క్ట్ : cluster ending in virama
            else: out.append(c + conj + v)
            i = j; continue
        if k == 'c2':   # orphan vattu
            out.append(VIR + c); i += 1; continue
        if k == 'aimark':   # ె + ౖ = ై
            if out and out[-1].endswith('ె'): out[-1] = out[-1][:-1] + 'ై'
            else: out.append('\u0C56')
            i += 1; continue
        if k in ('indep', 'other'): out.append(c); i += 1; continue
        if names[i] == 'space': out.append(' '); i += 1; continue
        if names[i] == 'zwnj': out.append('\u200c'); i += 1; continue
        out.append('�'); i += 1
    return ''.join(out)
