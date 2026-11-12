"""Tiny SVG helper for the UX Process figures (consistent book style)."""
from xml.sax.saxutils import escape

NAVY = '#1c2541'; INDIGO = '#3d4b8f'; INDIGO_S = '#e9ebf6'; INDIGO_M = '#c9d0ea'
HL = '#ffe27a'; HL_S = '#fff4c2'; HL_L = '#e8c547'
OK = '#2f7a55'; OK_S = '#e5f2ea'; WARN = '#9a4b2b'; WARN_S = '#f8e9e1'
PAPER = '#faf6ec'; PAPER2 = '#ece6d8'; LINE = '#d4ccb8'; INK = '#1f2328'; INK2 = '#4a4f57'; INK3 = '#7a7f87'
WHITE = '#ffffff'; PINK_S = '#fbe7ef'; PINK = '#a3365f'; TEAL_S = '#e2f2f3'; TEAL = '#1f6f78'
FONT = "Inter, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
CW = 0.56  # approx char width factor


def wrap_lines(s, width, size):
    maxc = max(4, int(width / (size * CW)))
    out = []
    for para in str(s).split('\n'):
        words = para.split(' '); cur = ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if len(t) <= maxc or not cur:
                cur = t
            else:
                out.append(cur); cur = w
        out.append(cur)
    return out


class SVG:
    def __init__(self, w, h, title, sub=''):
        self.w, self.h = w, h; self.el = []
        self.title, self.sub = title, sub
        self.el.append(f'<rect x="0" y="0" width="{w}" height="{h}" rx="16" fill="{PAPER}"/>')
        self.text(28, 38, title, 19, 700, NAVY)
        if sub: self.text(28, 60, sub, 12.5, 500, INK3)

    def add(self, s): self.el.append(s); return self

    def rect(self, x, y, w, h, fill=WHITE, stroke=LINE, r=10, sw=1.2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def circle(self, cx, cy, r, fill=WHITE, stroke=LINE, sw=1.2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, stroke=INK3, sw=1.4, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def path(self, d, stroke=INK3, sw=1.6, fill='none', dash=None):
        dd = f' stroke-dasharray="{dash}"' if dash else ''
        return self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round"{dd}/>')

    def arrow(self, x1, y1, x2, y2, stroke=INK2, sw=1.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        mk = 'a' + stroke.strip('#')
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" marker-end="url(#{mk})"{d}/>')

    def text(self, x, y, s, size=13, weight=500, fill=INK, anchor='start', italic=False):
        it = ' font-style="italic"' if italic else ''
        return self.add(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{it}>{escape(str(s))}</text>')

    def wrap(self, x, y, w, s, size=13, weight=500, fill=INK, anchor='start', lh=1.32):
        lines = wrap_lines(s, w, size)
        for i, l in enumerate(lines):
            self.text(x, y + i * size * lh, l, size, weight, fill, anchor)
        return len(lines) * size * lh

    def box(self, x, y, w, h, label, body=None, fill=WHITE, stroke=LINE, tc=INK, size=13, weight=600, r=10, bsize=11.5, bfill=INK2, sw=1.2, dash=None):
        """Box with centred label (and optional body below)."""
        self.rect(x, y, w, h, fill, stroke, r, sw, dash)
        ll = wrap_lines(label, w - 16, size)
        bl = wrap_lines(body, w - 16, bsize) if body else []
        th = len(ll) * size * 1.25 + (len(bl) * bsize * 1.3 + 4 if bl else 0)
        ty = y + (h - th) / 2 + size * 0.95
        for i, l in enumerate(ll):
            self.text(x + w / 2, ty + i * size * 1.25, l, size, weight, tc, 'middle')
        by = ty + len(ll) * size * 1.25 + 4
        for i, l in enumerate(bl):
            self.text(x + w / 2, by + i * bsize * 1.3, l, bsize, 500, bfill, 'middle')
        return self

    def pill(self, x, y, s, fill=INDIGO_S, tc=INDIGO, size=11.5):
        w = len(s) * size * CW + 18
        self.rect(x, y, w, size + 10, fill, fill, (size + 10) / 2)
        self.text(x + w / 2, y + size + 2.5, s, size, 600, tc, 'middle')
        return w

    def note(self, y, s):
        """Caption line at the bottom (key takeaway)."""
        self.rect(28, y, self.w - 56, 40, HL_S, HL_L, 10)
        self.wrap(44, y + 25, self.w - 88, s, 12.5, 600, INK2)
        return self

    def render(self):
        cols = {NAVY, INDIGO, INK2, INK3, OK, WARN, PINK, TEAL, HL_L}
        markers = ''.join(
            f'<marker id="a{c.strip("#")}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            for c in cols)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" font-family="{FONT}" role="img">'
                f'<title>{escape(self.title)}</title><defs>{markers}</defs>' + ''.join(self.el) + '</svg>')


def sticky(s, x, y, txt, fill=HL_S, w=118, h=58, rot=0):
    g = f'<g transform="rotate({rot} {x + w/2} {y + h/2})">'
    s.add(g)
    s.add(f'<rect x="{x+2}" y="{y+3}" width="{w}" height="{h}" rx="3" fill="#000" opacity=".06"/>')
    s.rect(x, y, w, h, fill, fill, 3)
    ll = wrap_lines(txt, w - 14, 11)
    ty = y + (h - len(ll) * 13.5) / 2 + 10
    for i, l in enumerate(ll):
        s.text(x + w / 2, ty + i * 13.5, l, 11, 500, INK, 'middle')
    s.add('</g>')


def phone(s, x, y, w=150, h=270, fill=WHITE, stroke=INK3):
    s.rect(x, y, w, h, fill, stroke, 18, 1.6)
    s.rect(x + w/2 - 18, y + 8, 36, 5, PAPER2, PAPER2, 2.5)
    return (x + 10, y + 22, w - 20, h - 34)
