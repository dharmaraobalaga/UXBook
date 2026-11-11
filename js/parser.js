/* ==========================================================================
   Part parser — turns a pasted ChatGPT "Part" into structured book data.
   Used in the browser (Import a Part) and in Node (tools/build-data.js).

   Recognised source format (headings may or may not start with "## "):
     Part 57 – Title
     Q447–Q454 | subtitle
     intro paragraphs…
     Q447. English question
     తెలుగు అర్థం: Telugu question
     తెలుగు సమాధానం:   …Telugu answer…
     English Answer:     …English answer…
     Note: …            (optional, kept as a reader note)
     Quick Revision …   (table: Question | Key points)
     Important English Vocabulary (table: English | తెలుగు)
     Speaking Practice  (intro line + sentences)
     Next Part – …      (preview, optional)
   Nothing is rewritten: text is only split, trimmed and stored.
   ========================================================================== */
(function (root) {
  'use strict';

  var H = '(?:#{1,4}\\s*)?';
  var RX = {
    part: new RegExp('^' + H + 'Part\\s+(\\d+)\\s*[–—:-]\\s*(.+)$', 'i'),
    question: new RegExp('^' + H + 'Q\\s?(\\d+)[.):]\\s*(.+)$'),
    teQ: /^(?:\*\*)?తెలుగు\s*అర్థం(?:\*\*)?\s*[:：]\s*(.*)$/,
    teA: /^(?:\*\*)?తెలుగు\s*సమాధానం(?:\*\*)?\s*[:：]\s*(.*)$/,
    enA: /^(?:\*\*)?English\s+Answer(?:\*\*)?\s*[:：]\s*(.*)$/i,
    note: /^(?:\*\*)?Note(?:\*\*)?\s*[:：]\s*(.+)$/i,
    revision: new RegExp('^' + H + '(Quick\\s+Revision.*)$', 'i'),
    vocab: new RegExp('^' + H + '(Important\\s+(?:English\\s+)?Vocabulary.*|Vocabulary.*)$', 'i'),
    speaking: new RegExp('^' + H + '(Speaking\\s+Practice.*)$', 'i'),
    next: new RegExp('^' + H + '(Next\\s+Part.*)$', 'i'),
    range: /^Q\s?(\d+)\s*[–—-]\s*Q?\s?(\d+)\s*(?:\|\s*(.*))?$/
  };

  function clean(s) { return String(s || '').replace(/\r\n?/g, '\n').replace(/ /g, ' '); }
  function stripMd(s) { return s.replace(/^#{1,4}\s*/, '').replace(/\*\*/g, '').trim(); }

  /** Join lines into paragraphs; keep "- " list lines as their own lines. */
  function toBlocks(lines) {
    var out = [], buf = [];
    function flush() { if (buf.length) { out.push(buf.join(' ').trim()); buf = []; } }
    lines.forEach(function (l) {
      var t = l.trim();
      if (!t) { flush(); return; }
      if (/^[-•*]\s+/.test(t)) { flush(); out.push('- ' + t.replace(/^[-•*]\s+/, '')); return; }
      buf.push(t);
    });
    flush();
    // paragraphs are separated by a blank line; consecutive list items by a single newline
    return out.reduce(function (acc, b, i) {
      if (!i) return b;
      var bothList = /^- /.test(b) && /^- /.test(out[i - 1]);
      return acc + (bothList ? '\n' : '\n\n') + b;
    }, '');
  }

  /** Parse a 2-column table from "a | b", "a\tb" or alternating lines. */
  function parseTable(lines) {
    var cells = [], rows = [];
    var piped = lines.filter(function (l) { return /\||\t/.test(l.trim()) && l.trim().replace(/[|\t\s]/g, ''); });
    if (piped.length) {
      piped.forEach(function (l) {
        var parts = l.split(/\s*\|\s*|\t+/).map(function (x) { return x.trim(); }).filter(Boolean);
        if (parts.length >= 2) rows.push([parts[0], parts.slice(1).join(' | ')]);
      });
    } else {
      lines.forEach(function (l) { var t = l.trim(); if (t) cells.push(t); });
      for (var i = 0; i + 1 < cells.length; i += 2) rows.push([cells[i], cells[i + 1]]);
    }
    // drop the header row (e.g. "Question | Key points", "English | తెలుగు అర్థం")
    if (rows.length && /^(question|english|word|term)$/i.test(rows[0][0])) rows.shift();
    return rows;
  }

  function parsePart(text, opts) {
    opts = opts || {};
    var lines = clean(text).split('\n');
    var warnings = [];
    var part = {
      partId: null, partNumber: null, title: '', subtitle: '', description: '',
      questionStart: null, questionEnd: null,
      questions: [], revision: [], vocabulary: [], speakingPractice: null, nextPreview: null
    };

    // ---- split into labelled segments --------------------------------------
    var segs = [], cur = { type: 'intro', head: '', lines: [] };
    lines.forEach(function (raw) {
      var l = raw.trim(), m;
      if (part.partNumber === null && (m = l.match(RX.part))) {
        part.partNumber = +m[1]; part.title = stripMd(m[2]); return;
      }
      var inTable = cur.type === 'revision' || cur.type === 'vocab';
      if (!inTable && !/\||\t/.test(l) && (m = l.match(RX.question))) { segs.push(cur); cur = { type: 'q', num: +m[1], head: stripMd(m[2]), lines: [] }; return; }
      if ((m = l.match(RX.revision))) { segs.push(cur); cur = { type: 'revision', head: stripMd(m[1]), lines: [] }; return; }
      if ((m = l.match(RX.vocab))) { segs.push(cur); cur = { type: 'vocab', head: stripMd(m[1]), lines: [] }; return; }
      if ((m = l.match(RX.speaking))) { segs.push(cur); cur = { type: 'speaking', head: stripMd(m[1]), lines: [] }; return; }
      if ((m = l.match(RX.next))) { segs.push(cur); cur = { type: 'next', head: stripMd(m[1]), lines: [] }; return; }
      cur.lines.push(raw);
    });
    segs.push(cur);

    if (part.partNumber === null && opts.partNumber) part.partNumber = +opts.partNumber;
    if (part.partNumber === null) warnings.push('No "Part N – Title" heading found.');
    if (!part.title && opts.title) part.title = opts.title;

    segs.forEach(function (s) {
      if (s.type === 'intro') {
        var body = [];
        s.lines.forEach(function (l) {
          var m = l.trim().match(RX.range);
          if (m && !part.subtitle) { part.subtitle = (m[3] || '').trim(); return; }
          body.push(l);
        });
        part.description = toBlocks(body);
      } else if (s.type === 'q') {
        var q = { questionNumber: s.num, questionEnglish: s.head, questionTelugu: '', answerTelugu: '', answerEnglish: '', note: '' };
        var mode = 'pre', te = [], en = [], notes = [];
        s.lines.forEach(function (l) {
          var t = l.trim(), m;
          if ((m = t.match(RX.teQ))) { q.questionTelugu = m[1].trim(); mode = 'teq'; return; }
          if ((m = t.match(RX.teA))) { mode = 'te'; if (m[1]) te.push(m[1]); return; }
          if ((m = t.match(RX.enA))) { mode = 'en'; if (m[1]) en.push(m[1]); return; }
          if (mode === 'en' && (m = t.match(RX.note))) { mode = 'note'; notes.push(t); return; }
          if (mode === 'teq' && t && !q.questionTelugu) { q.questionTelugu = t; return; }
          if (mode === 'te') te.push(l);
          else if (mode === 'en') en.push(l);
          else if (mode === 'note') notes.push(l);
        });
        q.answerTelugu = toBlocks(te);
        q.answerEnglish = toBlocks(en);
        q.note = toBlocks(notes);
        if (!q.questionTelugu) warnings.push('Q' + s.num + ': Telugu question (తెలుగు అర్థం) missing.');
        if (!q.answerTelugu) warnings.push('Q' + s.num + ': Telugu answer missing.');
        if (!q.answerEnglish) warnings.push('Q' + s.num + ': English answer missing.');
        part.questions.push(q);
      } else if (s.type === 'revision') {
        part.revision = parseTable(s.lines).map(function (r) {
          var m = r[0].match(/^Q\s?(\d+)[.)]?\s*(.*)$/);
          return { questionNumber: m ? +m[1] : null, topic: m ? m[2] : r[0], keyPoints: r[1] };
        });
      } else if (s.type === 'vocab') {
        part.vocabulary = parseTable(s.lines).map(function (r) { return { english: r[0], telugu: r[1] }; });
      } else if (s.type === 'speaking') {
        var intro = [], sentences = [];
        s.lines.forEach(function (l) {
          var t = l.trim(); if (!t) return;
          if (/^[-•*]\s+/.test(t) || /^\d+[.)]\s+/.test(t)) sentences.push(t.replace(/^([-•*]|\d+[.)])\s+/, ''));
          else if (!sentences.length && /[ఀ-౿]/.test(t)) intro.push(t);
          else sentences.push(t);
        });
        part.speakingPractice = { intro: intro.join(' '), sentences: sentences };
      } else if (s.type === 'next') {
        var nl = s.lines.map(function (l) { return l.trim(); }).filter(Boolean);
        part.nextPreview = {
          heading: s.head,
          title: nl.length && !/^[-•*]\s/.test(nl[0]) ? nl[0] : '',
          questions: nl.filter(function (l) { return /^[-•*]\s/.test(l); }).map(function (l) { return l.replace(/^[-•*]\s+/, ''); })
        };
      }
    });

    // ---- derived fields -----------------------------------------------------
    var nums = part.questions.map(function (q) { return q.questionNumber; });
    if (nums.length) { part.questionStart = Math.min.apply(null, nums); part.questionEnd = Math.max.apply(null, nums); }
    var seen = {};
    nums.forEach(function (n, i) {
      if (seen[n]) warnings.push('Q' + n + ' appears more than once (kept both, in source order).');
      seen[n] = true;
      if (i && n !== nums[i - 1] + 1) warnings.push('Gap or out-of-order numbering between Q' + nums[i - 1] + ' and Q' + n + '.');
    });
    part.partId = part.partNumber !== null ? 'part-' + String(part.partNumber).padStart(2, '0') : 'part-x';
    var dupCount = {};
    part.questions.forEach(function (q) {
      var base = 'q-' + q.questionNumber;
      dupCount[base] = (dupCount[base] || 0) + 1;
      q.questionId = dupCount[base] > 1 ? base + '-' + dupCount[base] : base;
      var rev = part.revision.filter(function (r) { return r.questionNumber === q.questionNumber; })[0];
      q.importantMarkers = rev ? [{ type: 'remember', label: 'Key points to remember', text: rev.keyPoints }] : [];
      if (q.note) q.importantMarkers.push({ type: 'tip', label: 'Note', text: q.note });
      q.tags = rev ? [rev.topic] : [];
    });

    return { part: part, warnings: warnings };
  }

  var api = { parsePart: parsePart };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.PartParser = api;
})(this);
