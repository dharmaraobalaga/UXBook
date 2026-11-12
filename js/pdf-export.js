/* ==========================================================================
   PDF export — builds a landscape, book-style print layout and opens the
   browser's print dialog ("Save as PDF"). Fonts are bundled locally, and the
   export waits for them, so Telugu never falls back to broken glyphs.
   Default: Telugu questions + Telugu answers only. English is optional.
   ========================================================================== */
(function () {
  'use strict';
  var E = window.EIM;

  function partsFor(scope) {
    var cur = E.curBook(), D = E.store.data;
    if (scope === 'all') return E.books.map(function (b) { return { book: b, parts: b.parts }; }).filter(function (g) { return g.parts.length; });
    if (scope === 'part') {
      var pg = cur.pages[D.position.page[cur.id] || 0];
      return pg ? [{ book: cur, parts: [pg.part] }] : [];
    }
    if (scope === 'saved') {
      var ids = {}; Object.keys(D.bookmarks).concat(Object.keys(D.favourites)).forEach(function (id) { ids[id] = true; });
      return E.books.map(function (b) {
        return { book: b, saved: true, parts: b.parts.map(function (p) {
          var c = Object.assign({}, p); c.questions = p.questions.filter(function (q) { return ids[q.questionId]; }); return c;
        }).filter(function (p) { return p.questions.length; }) };
      }).filter(function (g) { return g.parts.length; });
    }
    return [{ book: cur, parts: cur.parts }];
  }

  function qBlock(q, opts) {
    var notes = opts.notes ? E.store.data.notes.filter(function (n) { return n.qid === q.questionId && (n.body || n.title); }) : [];
    var markers = (q.importantMarkers || []).map(function (m) {
      return '<div class="p-marker ' + E.esc(m.type) + '"><b>' + E.esc(m.label || '') + '</b> ' + E.esc((m.text || '').replace(/^Note:\s*/, '')) + '</div>';
    }).join('');
    if (q.slide) {
      var s = q.slide, body = '';
      body += '<div class="p-en" lang="en"><h4>' + (s.kind === 'overview' ? 'Overview' : 'English – Meaning') + '</h4>' + E.fmt(s.en) + '</div>';
      if (s.te) body += '<div class="p-te" lang="te"><h4>తెలుగు – అర్థం</h4>' + E.fmt(s.te) + '</div>';
      if (s.kind === 'overview') (s.sections || []).forEach(function (sec) { body += '<div class="p-en"><h4>' + E.esc(sec[0]) + '</h4>' + E.fmt(sec[1]) + '</div>'; });
      else {
        body += '<div class="p-example"><b>' + E.esc(s.exTitle || 'Classic Rummy example') + '</b>' + E.fmt(s.ex) + '</div>';
        body += '<div class="p-en"><h4>How to create it</h4>' + E.fmt(s.how) + '</div>';
        if (s.important) body += '<div class="p-marker mistake"><b>Important</b> ' + E.esc(s.important) + '</div>';
        body += '<div class="p-en"><h4>Interview explanation</h4><p><i>“' + E.esc(s.iv) + '”</i></p></div>';
        if (s.extra) body += '<div class="p-en"><h4>' + E.esc(s.extra[0]) + '</h4>' + E.fmt(s.extra[1]) + '</div>';
      }
      return '<section class="p-q">' +
        '<header class="p-qhead"><span class="p-num">' + E.esc(E.numLabel(q)) + '</span><div><h3 lang="en">' + E.esc(q.questionEnglish) + '</h3></div></header>' +
        '<div class="p-slide">' + body + '</div>' +
        (notes.length ? '<div class="p-notes"><h4>My notebook</h4>' + notes.map(function (n) { return '<p><b>' + E.esc(E.noteTypes[n.type] || n.type) + (n.title ? ' — ' + E.esc(n.title) : '') + ':</b> ' + E.esc(n.body) + '</p>'; }).join('') + '</div>' : '') +
        '</section>';
    }
    return '<section class="p-q">' +
      '<header class="p-qhead"><span class="p-num">' + E.esc(E.numLabel(q)) + '</span><div><h3 lang="en">' + E.esc(q.questionEnglish) + '</h3>' +
      (q.questionTelugu ? '<p class="p-qte" lang="te">' + E.esc(q.questionTelugu) + '</p>' : '') + '</div></header>' +
      '<div class="p-ans' + (opts.english ? ' two' : '') + '">' +
        '<div class="p-te" lang="te"><h4>తెలుగు సమాధానం</h4>' + E.fmt(q.answerTelugu || '') + (q.exampleTelugu ? '<div class="p-example"><b>ఉదాహరణ</b> ' + E.fmt(q.exampleTelugu) + '</div>' : '') + '</div>' +
        (opts.english ? '<div class="p-en" lang="en"><h4>English Answer</h4>' + E.fmt(q.answerEnglish || '') + (q.exampleEnglish ? '<div class="p-example"><b>Example</b> ' + E.fmt(q.exampleEnglish) + '</div>' : '') + '</div>' : '') +
      '</div>' + (q.figure ? '<figure class="p-figure"><img src="' + E.esc(q.figure.src) + '" alt="' + E.esc(q.figure.alt || '') + '">' + ((q.figure.captionTelugu || q.figure.caption) ? '<figcaption>' + (q.figure.captionTelugu ? '<span lang="te">' + E.esc(q.figure.captionTelugu) + '</span> · ' : '') + E.esc(q.figure.caption || '') + '</figcaption>' : '') + '</figure>' : '') + markers +
      (notes.length ? '<div class="p-notes"><h4>My notebook</h4>' + notes.map(function (n) { return '<p><b>' + E.esc(E.noteTypes[n.type] || n.type) + (n.title ? ' — ' + E.esc(n.title) : '') + ':</b> ' + E.esc(n.body) + '</p>'; }).join('') + '</div>' : '') +
      '</section>';
  }

  function reviewBlock(part, opts) {
    var h = '';
    if (part.revision && part.revision.length && part.revision[0].cells) h += '<h4>Quick Revision</h4><table><thead><tr>' + part.revisionHeaders.map(function (x) { return '<th>' + E.esc(x) + '</th>'; }).join('') + '</tr></thead><tbody>' +
      part.revision.map(function (r) { return '<tr>' + r.cells.map(function (c) { return '<td' + (E.isTe(c) ? ' lang="te"' : '') + '>' + E.esc(c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table>';
    else if (part.revision && part.revision.length) h += '<h4>Quick Revision</h4><table><thead><tr><th>' + E.esc((part.revisionHeaders || ['Question'])[0]) + '</th><th>' + E.esc((part.revisionHeaders || [0, 'Key points to remember'])[1]) + '</th></tr></thead><tbody>' +
      part.revision.map(function (r) { return '<tr><td>' + (r.questionNumber ? 'Q' + r.questionNumber + '. ' : '') + E.esc(r.topic) + '</td><td>' + E.esc(r.keyPoints) + '</td></tr>'; }).join('') + '</tbody></table>';
    if (part.vocabulary && part.vocabulary.length) h += '<h4>Important English Vocabulary</h4><table><thead><tr><th>English</th><th>తెలుగు అర్థం</th></tr></thead><tbody>' +
      part.vocabulary.map(function (v) { return '<tr><td>' + E.esc(v.english) + '</td><td lang="te">' + E.esc(v.telugu) + '</td></tr>'; }).join('') + '</tbody></table>';
    if (part.speakingPractice && part.speakingPractice.sentences.length) h += '<h4>Speaking Practice</h4>' + (part.speakingPractice.intro ? '<p lang="te">' + E.esc(part.speakingPractice.intro) + '</p>' : '') +
      '<ol>' + part.speakingPractice.sentences.map(function (s) { return '<li>' + E.esc(s) + '</li>'; }).join('') + '</ol>';
    (part.extras || []).forEach(function (x) { h += '<h4>' + E.esc(x.heading) + '</h4><div class="p-extra">' + E.fmt(x.body) + (x.bodyEnglish && opts.english ? '<p><b>English answer:</b></p>' + E.fmt(x.bodyEnglish) : '') + '</div>'; });
    return h ? '<section class="p-review"><h3>' + E.esc(E.partLabel(part)) + ' · Review</h3><div class="p-review-grid">' + h + '</div></section>' : '';
  }

  function build(opts) {
    var groups = partsFor(opts.scope);
    var nQ = 0, nP = 0;
    groups.forEach(function (g) { nP += g.parts.length; g.parts.forEach(function (p) { nQ += p.questions.length; }); });
    var scopeLabel = { book: E.curBook().title, part: 'Selected part', all: 'All books', saved: 'My bookmarks & favourites' }[opts.scope];

    var cover = '<section class="p-cover"><div class="p-cover-inner">' +
      '<div class="p-logo"><img src="assets/brand/dsaras-mark.svg" alt="D\'Saras logo"></div>' +
      '<p class="p-eyebrow">D\'Saras · Complete Digital Learning Edition</p>' +
      '<h1>Product/UX/UI Design Interview Mastery</h1>' +
      '<p class="p-sub" lang="te">తెలుగులో నేర్చుకోండి. ఇంగ్లీష్‌లో ఆత్మవిశ్వాసంగా మాట్లాడండి.</p>' +
      '<p class="p-desc">A Telugu-First Interview Preparation Guide for UX/UI, Product Design and Professional Growth.</p>' +
      '<p class="p-meta">' + E.esc(scopeLabel) + ' · ' + nP + ' part' + (nP === 1 ? '' : 's') + ' · ' + nQ + ' questions · ' + (opts.english ? 'Telugu + English answers' : 'Telugu answers') + '</p>' +
      '<p class="p-author">Dharma Rao</p></div></section>';

    var toc = '<section class="p-toc"><h2>Contents</h2>' + groups.map(function (g) {
      return '<h3>' + E.esc(g.book.title) + '' + '</h3><ol>' + g.parts.map(function (p) {
        var a = p.questions[0], z = p.questions[p.questions.length - 1];
        return '<li><span>' + E.esc(E.partLabel(p)) + ' — ' + E.esc(p.title) + '</span><span class="p-dots"></span><span>' + (a ? E.esc(E.numLabel(a)) + (z !== a ? '–' + E.esc(E.numLabel(z)) : '') : '') + '</span></li>';
      }).join('') + '</ol>';
    }).join('') + '</section>';

    var body = groups.map(function (g) {
      return g.parts.map(function (p) {
        return '<article class="p-part"><header class="p-part-head"><p class="p-eyebrow">' + E.esc(g.book.title) + ' · ' + E.esc(E.partLabel(p)) + '</p><h2>' + E.esc(p.title) + '</h2>' +
          (p.description && !g.saved ? '<div class="p-intro">' + E.fmt(p.description) + '</div>' : '') + '</header>' +
          p.questions.map(function (q) { return qBlock(q, opts); }).join('') +
          (opts.review && !g.saved ? reviewBlock(p, opts) : '') + '</article>';
      }).join('');
    }).join('');

    return cover + toc + body;
  }

  function exportPDF(opts) {
    var root = document.getElementById('printRoot');
    root.innerHTML = build(opts);
    root.setAttribute('aria-hidden', 'false');
    document.body.classList.add('printing');
    var fontsReady = document.fonts && document.fonts.load ? Promise.all([
      document.fonts.load('400 16px "Noto Sans Telugu"', 'తెలుగు'), document.fonts.load('600 16px "Noto Sans Telugu"', 'తెలుగు'),
      document.fonts.load('400 16px Inter'), document.fonts.load('600 16px Inter'), document.fonts.load('600 16px Fraunces')
    ]).then(function () { return document.fonts.ready; }) : Promise.resolve();
    E.toast('Preparing PDF…');
    fontsReady.catch(function () {}).then(function () {
      setTimeout(function () { window.print(); }, 150);
    });
  }
  window.addEventListener('afterprint', function () {
    var root = document.getElementById('printRoot');
    if (!document.body.classList.contains('printing')) return;
    document.body.classList.remove('printing');
    root.innerHTML = ''; root.setAttribute('aria-hidden', 'true');
  });

  E.exportPDF = exportPDF;
  E.buildPrint = build; // used by tests / for previewing
})();
