"""Build the "MockInt Guide" tab (data/mock.js) from Mock_Interview_Guide.pdf.
PDF text kept: English model answers, Telugu explanations (తెలుగు వివరణ), Interview Tips, intro, checklist.
Written by Claude: Telugu questions + Telugu answers, English versions of the Telugu explanations (te_mock_a/b.py)."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from parse_mock import parse, SECTIONS
from te_mock_a import T as TA
from te_mock_b import T as TB
T = {**TA, **TB}

SRC = pathlib.Path(__file__).parent / 'mock.txt'
OUT = pathlib.Path(__file__).resolve().parent.parent.parent / 'data'

INTRO = '''ఈ guide‌ను మీ nearly 20 years of experience, IIT Bombay M.Des background, UX/UI leadership experience, Openplay Technologies experience, మరియు D'SARAS Design Studio projects ఆధారంగా రూపొందించారు.

ఇది కేవలం UX terminology interview guide కాదు. Senior, Lead, Principal Product Designer మరియు Design Manager roles కోసం మీరు ఎలా ఆలోచిస్తారు, decisions ఎలా తీసుకుంటారు, teams‌ను ఎలా lead చేస్తారు, business impact ఎలా చూపిస్తారు అనే అంశాలపై దృష్టి పెడుతుంది.

Important interview guidance: The answers below are model answers, not claims that every project has already achieved specific business results. Add your actual project details, team sizes, metrics, and outcomes wherever available. For concept projects such as ResolveAI and ORRBUS, clearly identify them as concept work rather than launched products.'''

PROJECTS = '''1. Classic Rummy – Openplay Technologies: Gaming UX, mobile product design, user journeys, interaction design.
2. TWAM – D'SARAS: E-commerce, generative AI-assisted design, shopping experience.
3. ResolveAI – Concept Project: AI-powered customer support SaaS, enterprise UX, analytics dashboard.
4. ORRBUS – Concept Project: Mobility, navigation, location-based product experience.
5. D'SARAS & Design Acharya: Design entrepreneurship, product vision, education, inclusive learning.'''

STRUCTURE = 'Section\tTopic\tQuestions\n' + '\n'.join(f'{n}\t{t}\t{a}–{b}' for n, t, _, a, b in SECTIONS) + '\nTotal\t\t50'

CHECKLIST = '''Before attending an interview, prepare the following:

- 90-second professional introduction.
- Career journey with key achievements.
- Three strong UX case studies.
- Clear explanation of your role in each project.
- One difficult design challenge and how you solved it.
- One stakeholder disagreement example.
- One leadership or mentoring example.
- One example of collaborating with developers.
- One measurable product outcome, if verified.
- A clear 30-60-90-day plan.
- Questions to ask the interviewer.

Final reminder: Do not memorize all 50 answers word for word. Understand the structure, prepare your own project stories, and communicate naturally.

తెలుగు అర్థం: 50 సమాధానాలను పదం పదం కంఠస్థం చేయకండి. Structure అర్థం చేసుకుని, మీ సొంత project stories సిద్ధం చేసుకుని, సహజంగా మాట్లాడండి.'''

PRACTISE = '''ఒకేసారి మొత్తం 50 questions చదవడం కంటే, mock interview format‌లో practice చేయడం మంచిది.

Interview level: Senior Product Designer · Lead Product Designer · Principal Product Designer · Design Manager – ఒక level ఎంచుకుని, ఆ స్థాయికి తగినట్లు సమాధానాలు చెప్పండి.

Interview section: ఒక్కో section (Q1–Q5, Q6–Q12, …, Q45–Q50) ఎంచుకుని, English answer చూడకుండా బిగ్గరగా చెప్పి practice చేయండి. తర్వాత "View English Answer" తో పోల్చండి.

### Recommended portfolio preparation · Portfolio order
మీ portfolio presentation కోసం ఈ order ఉపయోగించండి:

1. Classic Rummy: Strongest professional product experience.
2. TWAM: E-commerce and independent consulting.
3. ResolveAI: Enterprise SaaS and AI product thinking.
4. ORRBUS: Mobility product concept.
5. D'SARAS / Design Acharya: Entrepreneurial vision and design leadership.

నా recommendation: Senior లేదా Lead role interview కోసం ముందుగా Q1–Q5, Q20–Q33, Q39–Q50 practice చేయండి. ఇవి మీ experience, leadership, communication, portfolio presentation‌ను బలంగా చూపించడానికి ఉపయోగపడతాయి.'''


def build():
    qs = {q['n']: q for q in parse(SRC)}
    assert sorted(qs) == list(range(1, 51)), sorted(qs)
    parts = []
    for n, title, te_title, a, b in SECTIONS:
        items = []
        for k in range(a, b + 1):
            q, t = qs[k], T[k]
            te = (t['a'] + '\n\n### తెలుగు వివరణ · How to answer\nఈ ప్రశ్నకు సమాధానం ఇలా సిద్ధం చేసుకోండి\n\n' + q['te'])
            en_notes = t['en'] + (('\n\nInterview Tip: ' + t['tip_en']) if t.get('tip_en') else '')
            en = q['en'] + '\n\n### How to answer · Coaching notes\nWhat the interviewer is looking for\n\n' + en_notes
            markers = [{'type': 'tip', 'label': 'Interview Tip', 'text': q['tip']}] if q['tip'] else []
            items.append({'questionId': f'mk-{k}', 'questionNumber': k, 'questionEnglish': q['q'], 'questionTelugu': t['q'],
                          'tags': [title], 'answerTelugu': te, 'answerEnglish': en, 'importantMarkers': markers})
        extras = []
        if n == 1:
            extras = [{'heading': 'Your project examples · మీ project ఉదాహరణలు', 'body': PROJECTS, 'full': True},
                      {'heading': 'Interview structure – 50 questions', 'body': STRUCTURE, 'full': True}]
        if n == 8:
            extras = [{'heading': 'Final Interview Preparation Checklist · చివరి checklist', 'body': CHECKLIST, 'full': True},
                      {'heading': 'How to practise these 50 questions · ఎలా practice చేయాలి', 'body': PRACTISE, 'full': True}]
        parts.append({'partId': f'mock-s{n}', 'partNumber': n, 'title': title, 'subtitle': te_title,
                      'description': (INTRO + '\n\n' if n == 1 else '') + f'Section {n} · Q{a}–Q{b} · {b - a + 1} questions.',
                      'questions': items, 'revision': [], 'vocabulary': [], 'speakingPractice': None, 'extras': extras})
    (OUT / 'raw').mkdir(parents=True, exist_ok=True)
    (OUT / 'raw' / 'mock.json').write_text(json.dumps(parts, ensure_ascii=False, indent=1))
    head = ('/* AUTO-GENERATED by tools/mock/build_mock.py – "MockInt Guide" tab.\n'
            '   Source: Mock_Interview_Guide.pdf (Senior / Lead / Principal Product Designer – Mock Interview Guide, 50 questions).\n'
            '   PDF text: English model answers, Telugu explanations, Interview Tips, intro, checklist.\n'
            '   Added by Claude: Telugu questions and Telugu answers, English versions of the Telugu explanations. */\n')
    (OUT / 'mock.js').write_text(head + 'window.BOOK_MOCK_PARTS = ' + json.dumps(parts, ensure_ascii=False, indent=1) + ';\n')
    print('ok', sum(len(p['questions']) for p in parts), 'questions,', len(parts), 'sections')

if __name__ == '__main__':
    build()
