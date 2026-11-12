#!/usr/bin/env node
/* --------------------------------------------------------------------------
   Build data/handbook.js — Parts 1–12 (Q1–Q88) of the Interview Questions book — from:
     data/raw/handbook-q1-q88.txt        — the original ChatGPT handbook (88 Qs, 12 parts),
                                       English answers + Telugu explanations, kept verbatim
     data/raw/handbook-additions-*.json    — added by Claude: Telugu question translation (te),
                                       practical example in English (exEn) and Telugu (exTe)
   Usage: node tools/build-handbook.js
   IDs are "q-<question number>" (same scheme as the rest of the Interview Questions book).
   -------------------------------------------------------------------------- */
'use strict';
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const raw = path.join(root, 'data', 'raw');

const lines = fs.readFileSync(path.join(raw, 'handbook-q1-q88.txt'), 'utf8').replace(/\r\n?/g, '\n').split('\n');
const add = {};
fs.readdirSync(raw).filter(f => /^handbook-additions-.*\.json$/.test(f)).sort()
  .forEach(f => Object.assign(add, JSON.parse(fs.readFileSync(path.join(raw, f), 'utf8'))));

const find = (re, from = 0) => { for (let i = from; i < lines.length; i++) if (re.test(lines[i])) return i; return -1; };
const slice = (a, b) => lines.slice(a, b);

/* paragraphs: blank-line separated; table rows "a\tb" become "- a — b" */
function blocks(arr) {
  const out = []; let buf = [];
  const flush = () => { if (buf.length) { out.push(buf.join('\n').trim()); buf = []; } };
  arr.forEach(l => { const t = l.trim(); if (!t) return flush(); buf.push(t); });
  flush();
  return out.join('\n\n');
}
/* turn alternating "cell / blank / cell" tables (ChatGPT copy) into rows */
function altTable(arr, cols) {
  const cells = arr.map(l => l.trim()).filter(Boolean);
  const rows = [];
  for (let i = 0; i + cols - 1 < cells.length; i += cols) rows.push(cells.slice(i, i + cols));
  return rows;
}

/* ---------------- questions ---------------- */
const startQ = find(/^Part 1 – /);
const endQ = find(/^Final preparation – Important interview vocabulary/);
const parts = []; let part = null, q = null, mode = null, te = [], en = [], notes = [];
function closeQ() {
  if (!q) return;
  q.answerEnglish = blocks(en); q.answerTelugu = blocks(te);
  const a = add[q.questionNumber] || {};
  q.questionTelugu = q.teQ || a.te || ''; delete q.teQ;
  q.exampleEnglish = a.exEn || ''; q.exampleTelugu = a.exTe || ''; if (a.img) q.figure = a.img;
  q.importantMarkers = notes.map(n => ({ type: 'mistake', label: 'Important', text: n.replace(/^Important:\s*/, '') }));
  if (q.prep) { q.importantMarkers.unshift({ type: 'tip', label: q.prepLabel, text: blocks(q.prep) }); delete q.prep; delete q.prepLabel; }
  part.questions.push(q); q = null; te = []; en = []; notes = [];
}
for (let i = startQ; i < endQ; i++) {
  const l = lines[i].trim(); let m;
  if (/^(Part \d+ – Quick revision|Quick revision – Part \d+)/i.test(l)) { closeQ(); mode = 'rev'; continue; }
  if (/^మీ Portfolio Projects ను ఎలా ప్రెజెంట్ చేయాలి/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^మీ Portfolio లో AI Project/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Leadership Interview – Three Important Scenarios$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (/^Final Interview Practice – Three Important Questions$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (/^A Leadership Statement to Remember$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Your Personal Interview Preparation – Final Checklist$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Whiteboard Interview – A Practical Framework$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Interviewer అడిగితే వెంటనే చెప్పాల్సిన/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Practical Interview Practice$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Important Interview Tip – /.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Important: Salary Negotiation/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^(Practice – Interview Speaking Exercise|Interview Practice – Self Assessment|Speaking Practice – Executive-Level English|Practical Speaking Exercise|Practical Interview Exercise)$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^(English Speaking Practice|Interview Speaking Practice|Speaking Practice|Interview Practice – Use This 6-Step Framework)$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/Important Concepts to Revise$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/WCAG Principles$/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Special Practice/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (/^Special Note/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Practical .*Scenario/i.test(l) && !/^Practical office scenarios?\b/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (/^Special Preparation/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^మీ కోసం ఒక ముఖ్యమైన /.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Special Interview Practice/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (/^ప్రత్యేకంగా సిద్ధం కావాల్సిన ప్రశ్న:/.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (/^Practical office scenarios?\b/i.test(l)) { closeQ(); mode = 'scenario'; part.extras.push({ heading: l, body: '', _lines: [] }); continue; }
  if (mode === 'scenario' && /^Important:\s/.test(l)) { part.extras.push({ heading: l, body: '', _lines: [], full: true }); continue; }
  if (mode === 'scenario' && /^Scenario \d+[.:]\s/.test(l)) { part.extras.push({ heading: l, body: '', _lines: [], scenario: true }); continue; }
  if (mode === 'scenario') {
    if (/^(Part \d+ – |Q\d+\. )/.test(l)) { mode = null; }
    else { part.extras[part.extras.length - 1]._lines.push(lines[i]); continue; }
  }
  if ((mode === 'rev' || mode === 'vocab') && /^Important English vocabulary/i.test(l)) { mode = 'vocab'; continue; }
  if (mode === 'vocab') {
    if (l.includes('\t')) { const [a, b] = l.split('\t').map(x => x.trim()); if (!/^English( phrase| term)?$/i.test(a)) part.vocabulary.push({ english: a, telugu: b }); continue; }
    if (!/^(Part \d+ – |Q\d+\. )/.test(l)) continue;
  }
  if (mode === 'rev') {
    if (l.includes('\t')) {
      const cells = l.split('\t').map(x => x.trim());
      if (!part.revisionHeaders) part.revisionHeaders = cells;
      else part.revision.push({ questionNumber: null, topic: cells[0], keyPoints: cells.slice(1).join(' · '), cells: cells });
      continue;
    }
    if ((m = l.match(/^తదుపరి భాగం:\s*(.+)$/))) { part.nextPreview = { heading: 'తదుపరి భాగం · Next part', title: m[1].trim(), questions: [] }; continue; }
    if (!/^(Part \d+ – |Q\d+\. )/.test(l)) continue;
  }
  if ((m = l.match(/^Part (\d+) – (.+)$/))) { closeQ(); mode = null; part = { partId: 'part-' + String(m[1]).padStart(2, '0'), handbook: true, partNumber: +m[1], title: m[2], description: '', questions: [], revision: [], vocabulary: [], speakingPractice: null, extras: [] }; parts.push(part); continue; }
  if (!q && part && l && !/^Q\d+\. /.test(l)) {
    if (!part.subtitle && /^(ప్రశ్నలు|Questions|Q\d+–Q\d+ \||Interview Preparation – Questions \d)/.test(l)) part.subtitle = l;
    else part.description = (part.description ? part.description + '\n\n' : '') + l;
    continue;
  }
  if ((m = l.match(/^Q(\d+)\. (.+)$/))) { closeQ(); q = { questionId: 'q-' + m[1], questionNumber: +m[1], questionEnglish: m[2], tags: [part.title] }; mode = null; continue; }
  if (/^English answer.*:$/i.test(l)) { mode = 'en'; continue; }
  if (/^(తెలుగు వివరణ|తెలుగు సమాధానం):$/.test(l)) { mode = 'te'; continue; }
  if (q && mode === null && (m = l.match(/^తెలుగులో:?\s+(.+)$/))) { q.teQ = m[1].trim(); continue; }
  if (/^Important:/.test(l)) { notes.push(l); continue; }
  if (q && /^మీరు తప్పనిసరిగా సిద్ధం చేసుకోవాల్సిన విషయం$/.test(l)) { mode = 'prep'; q.prepLabel = l; q.prep = []; continue; }
  if (mode === 'prep') { q.prep.push(lines[i]); continue; }
  if (mode === 'en') en.push(lines[i]); else if (mode === 'te') te.push(lines[i]);
}
closeQ();

parts.forEach(p => p.extras.forEach(x => {
  if (!x._lines) return;
  const ls = x._lines.map(s => s.trim()).filter(Boolean);
  let ei = ls.findIndex(s => /^English answer:$/i.test(s));
  if (x.full) x._lines = x._lines.reduce((acc, s) => { if (/^[A-Z] – \S/.test(s.trim()) || /^POUR Principles$/.test(s.trim())) acc.push(''); acc.push(s); return acc; }, []);
  x.body = x.full ? blocks(x._lines) : (ei < 0 ? ls.filter(s => !/^English:\s/.test(s)) : ls.slice(0, ei)).join('\n\n');
  if (ei >= 0) x.bodyEnglish = ls.slice(ei + 1).join('\n\n');
  else { const en = ls.filter(s => /^English:\s/.test(s)); if (en.length) x.bodyEnglish = en.map(s => s.replace(/^English:\s*/, '')).join('\n\n'); }
  delete x._lines;
}));

/* ---------------- part 1 front matter & extras ---------------- */
const p1 = parts[0], p12 = parts.find(p => p.partNumber === 12) || parts[parts.length - 1];
const iPoint = find(/^One important point:/), iHow = find(/^How to use this handbook:/);
p1.subtitle = 'Product Design Interview Preparation Handbook';
p1.description = [lines[iHow].trim(), lines[iPoint].trim()].join('\n\n');

const iIntro = find(/^Professional introduction – Interview version/), iConcepts = find(/^3\. Important concepts to understand/);
p1.extras.push({ heading: 'Model answer – 2-minute professional introduction', body: blocks(slice(iIntro + 1, iConcepts)) });
const iCoach = find(/^4\. My interview coaching advice/), iPractise = find(/^5\. Let's practise your introduction/), iNextQ = find(/^Next interview question:/);
p1.extras.push({ heading: 'Interview coaching advice', body: blocks(slice(iCoach + 1, iPractise)) });
p1.extras.push({ heading: 'Practice task – deliver your introduction', body: blocks(slice(iPractise + 1, iNextQ)) });
p1.vocabulary = altTable(slice(iConcepts + 1, iCoach), 2).filter(r => !/^Interview phrase$/.test(r[0])).map(r => ({ english: r[0], telugu: r[1] }));

/* ---------------- final sections → Part 12 ---------------- */
const iFw = find(/^Your personal interview answer framework/), iFacts = find(/^Personal project facts to prepare/), iCheck = find(/^Final speaking practice checklist/), iPlan = find(/^Recommended study plan/), iEnd = find(/^Once you have practised these answers/);
p12.vocabulary = p12.vocabulary.concat(slice(endQ + 2, iFw).filter(l => l.includes('\t')).map(l => { const [a, b] = l.split('\t'); return { english: a.trim(), telugu: b.trim() }; }));
p12.extras.push({ heading: 'Your answer framework – STAR + Learning', body: blocks(slice(iFw + 1, iFacts)) });
const factLines = slice(iFacts + 1, iCheck);
p12.extras.push({ heading: 'Personal project facts to prepare', body:
  factLines.filter(l => l.trim() && !l.includes('\t')).slice(0, 1).join('') + '\n\n' +
  factLines.filter(l => l.includes('\t') && !/^Project\t/.test(l)).map(l => { const [a, b] = l.split('\t'); return '- ' + a.trim() + ': ' + b.trim(); }).join('\n') + '\n\n' +
  factLines.filter(l => /^A critical interview rule/.test(l)).join('') });
p12.extras.push({ heading: 'Final speaking practice checklist', body: slice(iCheck + 1, iPlan).map(l => l.trim()).filter(Boolean).map(l => '- ' + l).join('\n') });
const planLines = slice(iPlan + 1, iEnd);
const planIntro = planLines.find(l => l.trim()) || '';
const tbl = altTable(planLines.slice(planLines.findIndex(l => l.trim() === 'Day') + 0, planLines.findIndex(l => /^My recommendation/.test(l))), 3).slice(1);
p12.extras.push({ heading: 'Recommended 10-day study plan', body: planIntro.trim() + '\n\n' + tbl.map(r => '- Day ' + r[0] + ': ' + r[1] + ' (Q' + r[2] + ')').join('\n') + '\n\n' +
  planLines.filter(l => /^(My recommendation|One final suggestion)/.test(l)).map(l => l.trim()).join('\n\n') + '\n\n' + lines[iEnd].trim() });

/* ---------------- write ---------------- */
parts.forEach(p => { const n = p.questions.map(x => x.questionNumber); p.questionStart = Math.min(...n); p.questionEnd = Math.max(...n); });
const total = parts.reduce((s, p) => s + p.questions.length, 0);
const missing = [];
parts.forEach(p => p.questions.forEach(x => { if (!x.answerEnglish || !x.answerTelugu) missing.push(x.questionNumber); if (!x.exampleEnglish) missing.push('ex' + x.questionNumber); }));
const banner = `/* AUTO-GENERATED by tools/build-handbook.js on ${new Date().toISOString()}.
   Interview Questions, Parts 1–12 = "Product Design Interview Preparation Handbook" (source: data/raw/handbook-q1-q88.txt, verbatim)
   + Telugu question translations and practical examples added by Claude (data/raw/handbook-additions-*.json).
   Parts: ${parts.length} · Questions: ${total} */\n`;
fs.writeFileSync(path.join(root, 'data', 'handbook.js'), banner + 'window.BOOK_HANDBOOK_PARTS = ' + JSON.stringify(parts, null, 1) + ';\n');
console.log(`Handbook: ${parts.length} parts, ${total} questions. Missing answers/examples: ${missing.length ? missing.join(', ') : 'none'}`);
parts.forEach(p => console.log(`  Part ${p.partNumber} – ${p.title}: Q${p.questionStart}–Q${p.questionEnd} (${p.questions.length}) vocab ${p.vocabulary.length} extras ${p.extras.length}`));
