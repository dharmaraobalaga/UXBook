import json,sys
sys.path.insert(0,'.')
T={}
for f in ['te_01_12.py','te_13_24.py','te_25_35.py']:
    g={}; exec(open(f).read(),g); T.update(g['T'])
g={}; exec(open('te_25_35.py').read(),g); OVT=g['OVT']; PART_TE=g['PART_TE']
P='/home/claude/interview-mastery/data/raw/ux-process.json'
parts=json.load(open(P))
assert sorted(T)==list(range(1,36)), sorted(T)
for part in parts:
    if part['partNumber'] in PART_TE and not part.get('_te'):
        part['description']=PART_TE[part['partNumber']]+"\n\n"+part['description']; part['_te']=1
    for q in part['questions']:
        s=q.pop('slide',None) or {}
        qid=q['questionId']
        if qid.startswith('ux-intro'):
            o=OVT[qid]; q['questionEnglish']=o['q']; q['questionTelugu']=o['tq']
            if qid=='ux-intro-1': te=o['te']
            elif qid=='ux-intro-2': te=o['te']+"\n\nముఖ్యమైనది:\n"+o['imp']
            else: te=(s.get('te') or q['answerTelugu'])+"\n\n"+o['extra_te']
            q['answerTelugu']=te
            continue
        n=q['questionNumber']; t=T[n]
        q['questionEnglish']=t['q']; q['questionTelugu']=t['tq']
        meaning=s.get('te') or q['answerTelugu']
        te=meaning+"\n\nఎలా తయారు చేయాలి:\n"+t['how']
        if t.get('imp'): te+="\n\nముఖ్యమైనది:\n"+t['imp']
        te+="\n\nఇంటర్వ్యూలో ఇలా చెప్పవచ్చు:\n\""+t['iv']+"\""
        if t.get('extra'): te+="\n\n"+t['extra'][0]+":\n"+t['extra'][1]
        q['answerTelugu']=te
        q['exampleTelugu']=t['ex']
        if s.get('extra') and s['extra'][0] not in q['answerEnglish']:
            q['answerEnglish']+="\n\n"+s['extra'][0]+":\n"+s['extra'][1]
        if s.get('ex') and not q.get('exampleEnglish'): q['exampleEnglish']=s['ex']
for part in parts: part.pop('_te',None)
json.dump(parts,open(P,'w'),ensure_ascii=False,indent=1)
print('ok', sum(len(p['questions']) for p in parts))
