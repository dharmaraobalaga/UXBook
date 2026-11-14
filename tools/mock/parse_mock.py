"""Parse Mock_Interview_Guide.pdf text (pdftotext -layout) into 50 questions."""
import re, sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'vs' / 'vs'))
from parse_pdf import fix_te, blocks

SECTIONS = [(1, 'Professional Introduction & Career', 'వృత్తిపరమైన పరిచయం & కెరీర్', 1, 5),
            (2, 'UX Process & Design Strategy', 'UX ప్రాసెస్ & డిజైన్ వ్యూహం', 6, 12),
            (3, 'Product Thinking & Business Strategy', 'Product Thinking & వ్యాపార వ్యూహం', 13, 19),
            (4, 'Leadership & Team Management', 'నాయకత్వం & టీమ్ నిర్వహణ', 20, 27),
            (5, 'Stakeholder & Cross-functional Collaboration', 'Stakeholders & ఇతర టీమ్‌లతో సహకారం', 28, 33),
            (6, 'Design Systems & Technical Collaboration', 'Design Systems & సాంకేతిక సహకారం', 34, 38),
            (7, 'Portfolio & Project Presentation', 'Portfolio & ప్రాజెక్ట్ ప్రజెంటేషన్', 39, 44),
            (8, 'Scenario-based & Strategic Questions', 'సన్నివేశ ఆధారిత & వ్యూహాత్మక ప్రశ్నలు', 45, 50)]

def en_paras(lines):
    out = []
    for l in (x.strip() for x in lines):
        if not l: continue
        if out and not re.search(r'[.?!"”:]$', out[-1]): out[-1] += ' ' + l
        else: out.append(l)
    t = '\n\n'.join(out).strip()
    return t.strip('"“”').strip()

def parse(path):
    raw = open(path).read().replace('\f', '').split('\n')
    qs, cur, mode = [], None, None
    for r in raw:
        s = r.strip()
        m = re.match(r'^Q(\d+)\. (.*)', s)
        if m:
            cur = dict(n=int(m[1]), q=m[2].strip(), en=[], te=[], tip=[]); qs.append(cur); mode = None; continue
        if cur is None: continue
        if s.startswith('Model Answer'): mode = 'en'; continue
        if s.startswith('తెలుగు వివరణ'): mode = 'te'; continue
        if s.startswith('Interview Tip:'): mode = 'tip'; cur['tip'].append(s[14:].strip()); continue
        if s.startswith('SECTION ') or s.startswith('Final Interview Preparation Checklist'): mode = None; cur = None if s.startswith('Final') else cur; continue
        if mode: cur[mode].append(r)
    for q in qs:
        q['en'] = en_paras(q['en'])
        tl = q['te']
        while tl and not tl[-1].strip(): tl.pop()
        ind = min((len(l) - len(l.lstrip(' ')) for l in tl if l.strip()), default=0)
        tl = [l[ind:] for l in tl]
        q['te'] = fix_te(blocks(tl))
        q['tip'] = fix_te(' '.join(x.strip() for x in q['tip'] if x.strip()))
    return qs

if __name__ == '__main__':
    qs = parse(sys.argv[1])
    for q in qs[:12] + qs[38:41] + qs[48:]:
        print(f"=== Q{q['n']} {q['q']}\n--EN\n{q['en'][:300]}\n--TE\n{q['te']}\n--TIP {q['tip']}\n")
