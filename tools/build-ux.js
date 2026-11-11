#!/usr/bin/env node
/* --------------------------------------------------------------------------
   Build data/ux-process.js (the "UX Process" book) from:
     data/raw/ux-handbook.txt        — the original ChatGPT handbook (88 Qs, 12 parts),
                                       English answers + Telugu explanations, kept verbatim
     data/raw/ux-additions-*.json    — added by Claude: Telugu question translation (te),
                                       practical example in English (exEn) and Telugu (exTe)
   Usage: node tools/build-ux.js
   IDs are "ux-<question number>", so notes/bookmarks stay linked across rebuilds.
   -------------------------------------------------------------------------- */
'use strict';
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const raw = path.join(root, 'data', 'raw');

const lines = fs.readFileSync(path.join(raw, 'ux-handbook.txt'), 'utf8').replace(/\r\n?/g, '\n').split('\n');
const add = {};
fs.readdirSync(raw).filter(f => /^ux-additions-.*\.json$/.test(f)).sort()
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
  q.questionTelugu = a.te || '';
  q.exampleEnglish = a.exEn || ''; q.exampleTelugu = a.exTe || '';
  q.importantMarkers = notes.map(n => ({ type: 'mistake', label: 'Important', text: n.replace(/^Important:\s*/, '') }));
  part.questions.push(q); q = null; te = []; en = []; notes = [];
}
for (let i = startQ; i < endQ; i++) {
  const l = lines[i].trim(); let m;
  if ((m = l.match(/^Part (\d+) – (.+)$/))) { closeQ(); part = { partId: 'ux-' + String(m[1]).padStart(2, '0'), partNumber: +m[1], title: m[2], description: '', questions: [], revision: [], vocabulary: [], speakingPractice: null, extras: [] }; parts.push(part); continue; }
  if ((m = l.match(/^Q(\d+)\. (.+)$/))) { closeQ(); q = { questionId: 'ux-' + m[1], questionNumber: +m[1], questionEnglish: m[2], tags: [part.title] }; mode = null; continue; }
  if (/^English answer.*:$/.test(l)) { mode = 'en'; continue; }
  if (/^తెలుగు వివరణ:$/.test(l)) { mode = 'te'; continue; }
  if (/^Important:/.test(l)) { notes.push(l); continue; }
  if (mode === 'en') en.push(lines[i]); else if (mode === 'te') te.push(lines[i]);
}
closeQ();

/* ---------------- part 1 front matter & extras ---------------- */
const p1 = parts[0], p12 = parts[parts.length - 1];
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
p12.vocabulary = slice(endQ + 2, iFw).filter(l => l.includes('\t')).map(l => { const [a, b] = l.split('\t'); return { english: a.trim(), telugu: b.trim() }; });
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
const banner = `/* AUTO-GENERATED by tools/build-ux.js on ${new Date().toISOString()}.
   UX Process book = "Product Design Interview Preparation Handbook" (source: data/raw/ux-handbook.txt, verbatim)
   + Telugu question translations and practical examples added by Claude (data/raw/ux-additions-*.json).
   Parts: ${parts.length} · Questions: ${total} */\n`;
fs.writeFileSync(path.join(root, 'data', 'ux-process.js'), banner + 'window.BOOK_UX_PARTS = ' + JSON.stringify(parts, null, 1) + ';\n');
console.log(`UX book: ${parts.length} parts, ${total} questions. Missing answers/examples: ${missing.length ? missing.join(', ') : 'none'}`);
parts.forEach(p => console.log(`  Part ${p.partNumber} – ${p.title}: Q${p.questionStart}–Q${p.questionEnd} (${p.questions.length}) vocab ${p.vocabulary.length} extras ${p.extras.length}`));
