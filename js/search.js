/* ==========================================================================
   Search — local, instant, English + Telugu. No external API.
   Indexes: part titles, English & Telugu questions, Telugu & English answers,
   key points / markers, vocabulary, speaking practice and your own notes.
   The index is rebuilt from the books, so new parts are searchable automatically.
   ========================================================================== */
(function () {
  'use strict';
  var E = window.EIM, scope = 'all', lastQuery = '';
  var FIELDS = [
    ['questionEnglish', 'English question', 6], ['questionTelugu', 'Telugu question', 6],
    ['answerTelugu', 'Telugu answer', 3], ['answerEnglish', 'English answer', 2],
    ['exampleTelugu', 'Example (తెలుగు)', 2.2], ['exampleEnglish', 'Example (English)', 1.8]
  ];

  function norm(s) { return String(s || '').toLowerCase().normalize('NFC'); }

  function snippet(text, q, len) {
    len = len || 90;
    var t = String(text).replace(/\s+/g, ' '), i = norm(t).indexOf(q);
    if (i < 0) return E.esc(t.slice(0, len * 2)) + (t.length > len * 2 ? '…' : '');
    var s = Math.max(0, i - len), e = Math.min(t.length, i + q.length + len);
    var pre = (s > 0 ? '…' : '') + t.slice(s, i), hit = t.slice(i, i + q.length), post = t.slice(i + q.length, e) + (e < t.length ? '…' : '');
    return E.esc(pre) + '<mark class="hit">' + E.esc(hit) + '</mark>' + E.esc(post);
  }

  function run(query) {
    var q = norm(query.trim()); if (!q) return [];
    var qNum = q.replace(/^(q|ux|#)\s?/, ''), results = [];
    E.books.forEach(function (b) {
      if (scope !== 'all' && scope !== b.id) return;
      b.parts.forEach(function (part) {
        var partHit = norm(part.title).indexOf(q) >= 0;
        part.questions.forEach(function (it) {
          var best = null;
          if (/^\d+$/.test(qNum) && String(it.questionNumber) === qNum) best = { field: 'Question number', score: 20, text: it.questionEnglish };
          FIELDS.forEach(function (f) {
            if (best && best.score >= f[2]) return;
            var v = it[f[0]]; if (v && norm(v).indexOf(q) >= 0) best = { field: f[1], score: f[2], text: v, en: f[0] === 'answerEnglish' || f[0] === 'exampleEnglish' };
          });
          if (!best) (it.importantMarkers || []).forEach(function (m) { if (!best && norm(m.text).indexOf(q) >= 0) best = { field: m.label || 'Key point', score: 4, text: m.text }; });
          if (!best && partHit) best = { field: b.partLabel + ' title', score: 1, text: part.title };
          if (best) results.push({ kind: 'q', id: it.questionId, item: it, part: part, book: b, hit: best });
        });
        (part.vocabulary || []).forEach(function (v) {
          if (norm(v.english).indexOf(q) >= 0 || norm(v.telugu).indexOf(q) >= 0)
            results.push({ kind: 'vocab', part: part, book: b, hit: { field: 'Vocabulary', score: 5, text: v.english + ' — ' + v.telugu } });
        });
        (part.extras || []).forEach(function (x) {
          if (norm(x.heading + ' ' + x.body).indexOf(q) >= 0) results.push({ kind: 'rev', part: part, book: b, hit: { field: x.heading, score: 2, text: norm(x.body).indexOf(q) >= 0 ? x.body : x.heading } });
        });
        if (part.speakingPractice) part.speakingPractice.sentences.forEach(function (s) {
          if (norm(s).indexOf(q) >= 0) results.push({ kind: 'speak', part: part, book: b, hit: { field: 'Speaking practice', score: 2, text: s } });
        });
        (part.revision || []).forEach(function (r) {
          if (norm(r.keyPoints).indexOf(q) >= 0 || norm(r.topic).indexOf(q) >= 0) {
            var already = results.some(function (x) { return x.kind === 'q' && x.item && x.item.questionNumber === r.questionNumber && x.part === part; });
            if (!already) results.push({ kind: 'rev', part: part, book: b, hit: { field: 'Learning tip / revision', score: 3, text: 'Q' + r.questionNumber + '. ' + r.topic + ' — ' + r.keyPoints } });
          }
        });
      });
    });
    if (scope === 'all' || scope === 'notes') E.store.data.notes.forEach(function (n) {
      var txt = (n.title || '') + ' ' + (n.body || '');
      if (norm(txt).indexOf(q) >= 0) results.push({ kind: 'note', note: n, hit: { field: 'My notebook', score: 2.5, text: n.body || n.title } });
    });
    return results.sort(function (a, b) { return b.hit.score - a.hit.score; });
  }

  function resultHTML(r, q, i) {
    var meta, title, open;
    if (r.kind === 'note') {
      var e = r.note.qid && E.index[r.note.qid];
      meta = '<span class="r-field">' + E.esc(r.hit.field) + '</span><span>' + E.esc(r.note.category || '') + '</span>';
      title = E.esc(r.note.title || (e ? E.numLabel(e.item) + '. ' + e.item.questionEnglish : 'Note'));
      open = 'data-note="' + E.esc(r.note.id) + '"';
    } else {
      var pl = E.partLabel(r.part);
      meta = '<span class="r-field' + (r.hit.en ? ' en' : '') + '">' + E.esc(r.hit.field) + '</span><span>' + E.esc(r.book.title) + ' · ' + E.esc(pl) + ' — ' + E.esc(r.part.title) + '</span>';
      if (r.kind === 'q') { title = E.esc(E.numLabel(r.item) + '. ' + r.item.questionEnglish); open = 'data-open="' + E.esc(r.id) + '"'; }
      else { title = E.esc(pl + ' review'); open = 'data-review="' + E.esc(r.book.id + '|' + r.part.partId) + '"'; }
    }
    return '<button class="result" ' + open + ' data-i="' + i + '"><div class="r-meta">' + meta + '</div><div class="r-title">' + title + '</div>' +
      '<div class="r-snip' + (E.isTe(r.hit.text) ? ' te' : '') + '">' + snippet(r.hit.text, q) + '</div>' +
      (r.hit.en ? '<div class="muted" style="font-size:.78rem;margin-top:4px">Match is in the English answer — opens the Telugu page; press “View English Answer” to see it.</div>' : '') + '</button>';
  }

  function renderResults() {
    var input = document.getElementById('searchInput'), out = document.getElementById('searchOut');
    if (!input || !out) return;
    var q = input.value; lastQuery = q;
    if (!q.trim()) { out.innerHTML = '<div class="empty">' + E.icon('search') + '<h3>Search the whole library</h3><p>Type in English or తెలుగు — e.g. <b>stakeholder</b>, <b>STAR</b>, <b lang="te">గడువు</b>, or a question number like <b>Q452</b>.</p></div>'; return; }
    var res = run(q), nq = norm(q.trim());
    out.innerHTML = '<p class="muted" style="margin:0 0 10px">' + res.length + ' result' + (res.length === 1 ? '' : 's') + '</p>' +
      (res.length ? '<div class="card-list">' + res.slice(0, 200).map(function (r, i) { return resultHTML(r, nq, i); }).join('') + '</div>' : '<div class="empty"><h3>No matches</h3><p>Try a shorter word, or switch the filter to “All books”.</p></div>');
  }

  function render() {
    E = window.EIM;
    var chips = [['all', 'All books']].concat(E.books.map(function (b) { return [b.id, b.title]; })).concat([['notes', 'My notebook']]);
    document.getElementById('view-search').innerHTML =
      '<div class="view-head"><div><h2 class="view-title">Search</h2><p class="view-sub">English &amp; Telugu · questions, answers, vocabulary, tips and your notes · press <kbd>/</kbd> anywhere</p></div></div>' +
      '<div class="search-box">' + E.icon('search') + '<input id="searchInput" type="search" autocomplete="off" placeholder="Search in English or తెలుగు…" aria-label="Search" value="' + E.esc(lastQuery) + '"></div>' +
      '<div class="search-filters" role="group" aria-label="Search scope">' + chips.map(function (c) { return '<button class="chip" data-scope="' + c[0] + '" aria-pressed="' + (scope === c[0]) + '">' + E.esc(c[1]) + '</button>'; }).join('') + '</div>' +
      '<div id="searchOut"></div>';
    renderResults();
    var input = document.getElementById('searchInput');
    setTimeout(function () { input.focus(); input.setSelectionRange(input.value.length, input.value.length); }, 30);
  }

  var timer;
  document.addEventListener('DOMContentLoaded', function () {
    var view = document.getElementById('view-search');
    view.addEventListener('input', function (e) { if (e.target.id === 'searchInput') { clearTimeout(timer); timer = setTimeout(renderResults, 120); } });
    view.addEventListener('click', function (e) {
      var c = e.target.closest('[data-scope]');
      if (c) { scope = c.getAttribute('data-scope'); render(); return; }
      var r = e.target.closest('.result'); if (!r) return;
      if (r.hasAttribute('data-open')) return E.openItem(r.getAttribute('data-open'));
      if (r.hasAttribute('data-note')) { window.EIM.focusNote = r.getAttribute('data-note'); return E.setTab('notes'); }
      if (r.hasAttribute('data-review')) {
        var parts = r.getAttribute('data-review').split('|'), b = E.books.filter(function (x) { return x.id === parts[0]; })[0];
        var idx = b.pages.findIndex(function (p) { return p.type === 'review' && p.part.partId === parts[1]; });
        E.store.data.position.book = b.id; E.store.data.position.page[b.id] = idx; E.store.save();
        E.rebuild(); E.setTab('read');
      }
    });
  });
  window.addEventListener('load', function () { window.EIM.render.search = render; });
  // register immediately as well (EIM exists once app.js ran)
  if (window.EIM) window.EIM.render.search = render;
})();
