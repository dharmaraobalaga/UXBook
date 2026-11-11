/* ==========================================================================
   Product/UX/UI Design Interview Mastery — core app: books, navigation, reading view,
   English practice panel, highlights, TOC, bookmarks, favourites, progress,
   settings (display, import a part, backup/restore).
   Search → js/search.js · Notebook & My Questions → js/notebook.js
   PDF → js/pdf-export.js
   ========================================================================== */
(function () {
  'use strict';
  var Store = window.EIMStore;
  var S = Store.data;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------------- Icons ---------------- */
  var P = {
    bookmark: '<path d="M6 3h12v18l-6-4-6 4z"/>',
    star: '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/>',
    note: '<path d="M5 3h10l4 4v14H5z"/><path d="M15 3v4h4M8 12h8M8 16h6"/>',
    check: '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.7 2.7L16 10"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    print: '<path d="M6 9V3h12v6M6 18H4v-7h16v7h-2"/><path d="M6 14h12v7H6z"/>',
    gear: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    left: '<path d="M15 5l-7 7 7 7"/>', right: '<path d="M9 5l7 7-7 7"/>',
    first: '<path d="M11 5l-7 7 7 7M19 5l-7 7 7 7"/>', last: '<path d="M13 5l7 7-7 7M5 5l7 7-7 7"/>',
    x: '<path d="M6 6l12 12M18 6L6 18"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    speaker: '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/>',
    stop: '<rect x="6" y="6" width="12" height="12" rx="2"/>',
    eye: '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    eyeOff: '<path d="M3 3l18 18M10.6 5.1A10 10 0 0 1 12 5c6.5 0 10 7 10 7a17 17 0 0 1-3.2 4M6.6 6.6A17 17 0 0 0 2 12s3.5 7 10 7a9.6 9.6 0 0 0 5.4-1.6"/><path d="M9.9 9.9a3 3 0 0 0 4.2 4.2"/>',
    bulb: '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    alert: '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.01"/>',
    mic: '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    plus: '<path d="M12 5v14M5 12h14"/>', edit: '<path d="M4 20h4L19 9l-4-4L4 16z"/>', trash: '<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>',
    upload: '<path d="M12 16V4M7 9l5-5 5 5M4 16v4h16v-4"/>', download: '<path d="M12 4v12M7 11l5 5 5-5M4 20h16"/>',
    book: '<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>',
    copy: '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a1 1 0 0 1 1-1h10"/>',
    pen: '<path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>'
  };
  function icon(name, cls) { return '<svg class="i ' + (cls || '') + '" viewBox="0 0 24 24" aria-hidden="true">' + (P[name] || '') + '</svg>'; }

  /* ---------------- Text helpers ---------------- */
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function boldLabel(html) { return html.replace(/^([A-Za-z][A-Za-z0-9 /&()–-]{0,30}):(\s)/, '<strong>$1:</strong>$2'); }
  function fmt(text) {
    if (!text) return '';
    return String(text).split(/\n{2,}/).map(function (block) {
      var lines = block.split('\n');
      if (lines.every(function (l) { return /^-\s/.test(l); })) {
        return '<ul>' + lines.map(function (l) { return '<li>' + boldLabel(esc(l.replace(/^-\s+/, ''))) + '</li>'; }).join('') + '</ul>';
      }
      return '<p>' + lines.map(function (l) { return boldLabel(esc(l)); }).join('<br>') + '</p>';
    }).join('');
  }
  function isTe(s) { return /[ఀ-౿]/.test(s || ''); }
  function fmtDate(ts) { try { return new Date(ts).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' }); } catch (e) { return ''; } }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function download(name, text, type) {
    var blob = new Blob([text], { type: type || 'application/octet-stream' });
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1500);
  }

  /* ---------------- Toast ---------------- */
  var toastTimer;
  function toast(msg, actionLabel, action) {
    var t = $('#toast');
    t.innerHTML = '<span>' + esc(msg) + '</span>' + (actionLabel ? '<button type="button">' + esc(actionLabel) + '</button>' : '');
    if (actionLabel) $('button', t).onclick = function () { t.classList.remove('on'); action(); };
    t.classList.add('on'); clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove('on'); }, actionLabel ? 5000 : 2600);
  }

  /* ======================================================================
     BOOKS & INDEX
     ====================================================================== */
  var BOOKS = [], INDEX = {};
  var EXPECTED_IQ_PARTS = 57;

  function myQuestionParts() {
    var cats = {}, order = [];
    S.myQuestions.slice().sort(function (a, b) { return a.created - b.created; }).forEach(function (q) {
      var c = q.category || 'My Questions';
      if (!cats[c]) { cats[c] = []; order.push(c); }
      cats[c].push(q);
    });
    var n = 0;
    return order.map(function (c, i) {
      return {
        partId: 'my-cat-' + i, partNumber: i + 1, title: c, description: '', revision: [], vocabulary: [], speakingPractice: null,
        questions: cats[c].map(function (q) {
          n++;
          return {
            questionId: q.id, questionNumber: n, questionEnglish: q.questionEnglish, questionTelugu: q.questionTelugu,
            answerTelugu: q.answerTelugu, answerEnglish: q.answerEnglish, tags: [c], mine: true,
            importantMarkers: q.keyPoints ? [{ type: 'remember', label: 'Key points to remember', text: q.keyPoints }] : []
          };
        })
      };
    });
  }

  function buildBooks() {
    var map = {};
    (window.BOOK_PARTS || []).forEach(function (p) { map[p.partNumber] = clone(p); });
    S.importedParts.forEach(function (ip) { var p = clone(ip.part); p.imported = true; map[p.partNumber] = p; });
    var iqParts = Object.keys(map).map(function (k) { return map[k]; }).sort(function (a, b) { return a.partNumber - b.partNumber; });

    BOOKS = [
      { id: 'ux', title: 'UX Process', short: 'UX Process', te: 'UX ప్రాసెస్', partLabel: 'Part', parts: clone(window.BOOK_UX_PARTS || []), draft: true },
      { id: 'iq', title: 'Interview Questions', short: 'Interview', te: 'ఇంటర్వ్యూ ప్రశ్నలు', partLabel: 'Part', parts: iqParts, expected: EXPECTED_IQ_PARTS },
      { id: 'my', title: 'My Questions', short: 'My Qs', te: 'నా ప్రశ్నలు', partLabel: 'Category', parts: myQuestionParts() }
    ];
    INDEX = {};
    BOOKS.forEach(function (book) {
      book.pages = []; book.items = [];
      book.parts.forEach(function (part) {
        part.bookId = book.id;
        part.questions.forEach(function (q, qi) {
          q.bookId = book.id; q.partId = part.partId; q.first = qi === 0;
          var entry = { item: q, part: part, book: book, page: book.pages.length };
          INDEX[q.questionId] = entry;
          book.pages.push({ type: 'q', id: q.questionId, part: part });
          book.items.push(q);
        });
        var hasReview = (part.revision && part.revision.length) || (part.vocabulary && part.vocabulary.length) ||
          (part.speakingPractice && part.speakingPractice.sentences && part.speakingPractice.sentences.length) || part.nextPreview || (part.extras && part.extras.length);
        if (hasReview) book.pages.push({ type: 'review', part: part });
      });
      var maxN = Math.max.apply(null, [book.expected || 0].concat(book.parts.map(function (p) { return p.partNumber; })));
      book.maxPart = maxN;
      book.missing = [];
      if (book.expected) for (var n = 1; n <= maxN; n++) if (!book.parts.some(function (p) { return p.partNumber === n; })) book.missing.push(n);
    });
  }
  function book(id) { return BOOKS.filter(function (b) { return b.id === id; })[0] || BOOKS[0]; }
  function curBook() { return book(S.position.book); }
  function numLabel(q) { return q.bookId === 'my' ? '#' + q.questionNumber : 'Q' + q.questionNumber; }
  function partLabel(part) { var b = book(part.bookId); return b.partLabel + ' ' + part.partNumber; }
  function rangeLabel(part) {
    if (!part.questions.length) return '';
    var a = part.questions[0], z = part.questions[part.questions.length - 1];
    return a === z ? numLabel(a) : numLabel(a) + '–' + numLabel(z).replace(/^[A-Za-z# ]+/, '');
  }

  /* ======================================================================
     TABS / ROUTING
     ====================================================================== */
  var TABS = ['read', 'toc', 'search', 'bookmarks', 'favourites', 'notes', 'progress'];
  var RENDER = {};

  function setTab(tab, opts) {
    if (TABS.indexOf(tab) < 0) tab = 'read';
    S.position.tab = tab; Store.save();
    $$('#tabs [data-tab]').forEach(function (b) {
      var on = b.getAttribute('data-tab') === tab;
      b.setAttribute('aria-selected', on ? 'true' : 'false'); b.tabIndex = on ? 0 : -1;
    });
    TABS.forEach(function (t) { $('#view-' + t).hidden = t !== tab; });
    if (tab !== 'read') closeEnglish();
    if (RENDER[tab]) RENDER[tab](opts || {});
    if (!(opts && opts.keepScroll)) window.scrollTo(0, 0);
    updateTabCounts();
  }
  function updateTabCounts() {
    var counts = { bookmarks: Object.keys(S.bookmarks).length, favourites: Object.keys(S.favourites).length, notes: S.notes.length };
    $$('#tabs [data-tab]').forEach(function (b) {
      var t = b.getAttribute('data-tab'), c = $('.count', b);
      if (counts[t] === undefined) return;
      if (!c) { c = document.createElement('span'); c.className = 'count'; b.appendChild(c); }
      c.textContent = counts[t]; c.hidden = !counts[t];
    });
  }
  function setBook(id, keepTab) {
    S.position.book = id; Store.save();
    renderBookSwitch();
    setTab(keepTab ? S.position.tab : (S.position.tab === 'read' ? 'read' : S.position.tab));
  }
  function renderBookSwitch() {
    $('#bookSwitch').innerHTML = BOOKS.map(function (b) {
      return '<button role="radio" data-book="' + b.id + '" aria-checked="' + (b.id === S.position.book) + '"><span class="bs-long">' + esc(b.title) + '</span><span class="bs-short">' + esc(b.short) + '</span></button>';
    }).join('');
  }

  function openItem(id, opts) {
    var e = INDEX[id]; if (!e) { toast('That question is not available any more.'); return; }
    S.position.book = e.book.id; S.position.page[e.book.id] = e.page; Store.save();
    renderBookSwitch();
    setTab('read', { dir: 0 });
    if (opts && opts.english) openEnglish();
  }
  function goPage(i, dir) {
    var b = curBook(); if (!b.pages.length) return;
    i = Math.max(0, Math.min(b.pages.length - 1, i));
    if (i === S.position.page[b.id] && dir) return;
    S.position.page[b.id] = i; Store.save();
    var wasOpen = $('#enPanel').classList.contains('open');
    RENDER.read({ dir: dir || 0 });
    if (wasOpen) { var pg = b.pages[i]; if (pg.type === 'q') fillEnglish(pg.id); else closeEnglish(); }
    window.scrollTo({ top: 0, behavior: 'auto' });
  }
  function stepQuestion(delta) {
    var b = curBook(), i = S.position.page[b.id] || 0;
    for (var j = i + delta; j >= 0 && j < b.pages.length; j += delta) if (b.pages[j].type === 'q') return goPage(j, delta);
  }

  /* ======================================================================
     READ VIEW
     ====================================================================== */
  var MARK_ICON = { remember: 'bulb', tip: 'bulb', mistake: 'alert', concept: 'book', speaking: 'mic', vocab: 'book' };

  function markersHTML(q) {
    if (!q.importantMarkers || !q.importantMarkers.length) return '';
    return '<div class="markers">' + q.importantMarkers.map(function (m) {
      var text = m.text || '', label = m.label || '';
      if (label && text.toLowerCase().indexOf(label.toLowerCase() + ':') === 0) text = text.slice(label.length + 1).trim();
      return '<div class="marker ' + esc(m.type) + '">' + icon(MARK_ICON[m.type] || 'bulb', 'm-ic') +
        (label ? '<span class="m-label">' + esc(label) + '</span>' : '') +
        '<span class="m-text' + (isTe(text) ? ' te' : '') + '">' + esc(text) + '</span></div>';
    }).join('') + '</div>';
  }

  function footHTML(b, idx) {
    var total = b.pages.length, pct = total ? Math.round((idx + 1) / total * 100) : 0;
    var hasPrevQ = b.pages.slice(0, idx).some(function (p) { return p.type === 'q'; });
    var hasNextQ = b.pages.slice(idx + 1).some(function (p) { return p.type === 'q'; });
    return '<div class="progress-line" aria-hidden="true"><span style="width:' + pct + '%"></span></div>' +
      '<div class="page-foot">' +
      '<div class="pager">' +
      '<button class="btn sm" data-nav="prev" ' + (idx <= 0 ? 'disabled' : '') + ' aria-label="Previous page">' + icon('left') + '<span class="lbl">Previous page</span></button>' +
      '<button class="btn sm ghost" data-nav="prevq" ' + (hasPrevQ ? '' : 'disabled') + ' aria-label="Previous question">' + icon('first') + '<span class="lbl">Prev question</span></button>' +
      '</div>' +
      '<label class="page-no">Page <input type="number" min="1" max="' + total + '" value="' + (idx + 1) + '" id="jumpPage" aria-label="Jump to page"> of ' + total + '</label>' +
      '<span class="kbd-hint"><kbd>←</kbd> <kbd>→</kbd> pages · <kbd>E</kbd> English · <kbd>B</kbd> bookmark</span>' +
      '<div class="pager">' +
      '<button class="btn sm ghost" data-nav="nextq" ' + (hasNextQ ? '' : 'disabled') + ' aria-label="Next question"><span class="lbl">Next question</span>' + icon('last') + '</button>' +
      '<button class="btn sm primary" data-nav="next" ' + (idx >= total - 1 ? 'disabled' : '') + ' aria-label="Next page"><span class="lbl">Next page</span>' + icon('right') + '</button>' +
      '</div></div>';
  }

  function questionPage(b, q, part) {
    var id = q.questionId;
    var bm = Store.has('bookmarks', id), fav = Store.has('favourites', id), done = Store.has('completed', id);
    var nNotes = S.notes.filter(function (n) { return n.qid === id; }).length;
    var intro = '';
    if (q.first && (part.description || part.subtitle)) {
      intro = '<details class="part-intro"' + ((part.description || '').length < 420 ? ' open' : '') + '><summary>About ' + esc(partLabel(part)) + (part.subtitle ? ' · ' + esc(part.subtitle) : '') + '</summary>' + fmt(part.description).replace(/<p>(?=[^<]*[ఀ-౿])/g, '<p lang="te">') + '</details>';
    }
    var practice = '';
    if (S.settings.practiceMode) {
      var st = S.practice[id] || [false, false, false, false];
      var steps = ['Read the Telugu answer', 'Try answering in English (aloud)', 'Reveal the English answer', 'Practise again without looking'];
      practice = '<div class="practice-box"><h4>Practice checklist</h4>' + steps.map(function (s, i) {
        return '<label><input type="checkbox" data-step="' + i + '" ' + (st[i] ? 'checked' : '') + '> ' + s + '</label>';
      }).join('') + '</div>';
    }
    var mine = q.mine ? '<div class="my-tools"><button class="btn sm" data-act="edit-my">' + icon('edit') + 'Edit question</button><button class="btn sm danger" data-act="del-my">' + icon('trash') + 'Delete</button></div>' : '';

    return '<div class="spread">' +
      '<section class="page page-left">' +
        '<div class="q-kicker"><span>' + esc(partLabel(part)) + '</span><span aria-hidden="true">·</span><span>Question</span></div>' +
        '<div class="q-num">' + esc(numLabel(q)) + '</div>' +
        '<h2 class="q-en" lang="en">' + esc(q.questionEnglish) + '</h2>' +
        (q.questionTelugu ? '<p class="q-te" lang="te">' + esc(q.questionTelugu) + '</p>' : '') +
        '<div class="q-actions">' +
          '<button class="act bm" data-act="bm" aria-pressed="' + bm + '">' + icon('bookmark') + (bm ? 'Bookmarked' : 'Bookmark') + '</button>' +
          '<button class="act fav" data-act="fav" aria-pressed="' + fav + '">' + icon('star') + (fav ? 'Favourite' : 'Favourite') + '</button>' +
          '<button class="act nb' + (nNotes ? ' has' : '') + '" data-act="note">' + icon('note') + (nNotes ? 'Notebook (' + nNotes + ')' : 'Add to Notebook') + '</button>' +
          '<button class="act done" data-act="done" aria-pressed="' + done + '">' + icon('check') + (done ? 'Completed' : 'Mark completed') + '</button>' +
        '</div>' + intro + markersHTML(q) +
        (q.exampleTelugu ? '<aside class="example-box" lang="te"><span class="ex-label">' + icon('bulb') + '<span class="ex-te">ఉదాహరణ</span> · Example</span>' + fmt(q.exampleTelugu) + '</aside>' : '') +
        practice + mine +
      '</section>' +
      '<section class="page page-right">' +
        '<div class="ans-head"><span class="ans-label" lang="te">తెలుగు సమాధానం</span>' +
          (q.answerEnglish ? '<button class="btn-en" data-act="english" aria-expanded="false" aria-controls="enPanel">' + icon('globe') + '<span>View <span class="long">English </span>Answer</span></button>' : '<span class="muted">No English answer in source</span>') +
        '</div>' +
        '<div class="te-answer" lang="te" id="teAnswer">' + (q.answerTelugu ? fmt(q.answerTelugu) : '<p class="muted">Telugu answer missing in the source.</p>') + '</div>' +
        '<p class="hl-hint">' + icon('pen') + '<span>Select any words in the Telugu answer to highlight them. Click a highlight to remove it.</span></p>' +
      '</section></div>';
  }

  function reviewPage(b, part) {
    var h = '<div class="review"><div class="q-kicker">' + esc(partLabel(part)) + ' · Review</div><h2>' + esc(part.title) + '</h2><div class="review-grid">';
    var left = '', right = '';
    if (part.revision && part.revision.length) {
      left += '<h3>' + icon('bulb') + 'Quick Revision</h3><table class="tbl"><thead><tr><th>Question</th><th>Key points to remember</th></tr></thead><tbody>' +
        part.revision.map(function (r) {
          var target = part.questions.filter(function (q) { return q.questionNumber === r.questionNumber; })[0];
          var label = (r.questionNumber ? 'Q' + r.questionNumber + '. ' : '') + r.topic;
          return '<tr><td>' + (target ? '<a href="#' + esc(target.questionId) + '" data-open="' + esc(target.questionId) + '">' + esc(label) + '</a>' : esc(label)) + '</td><td><span class="hl-ink">' + esc(r.keyPoints) + '</span></td></tr>';
        }).join('') + '</tbody></table>';
    }
    if (part.vocabulary && part.vocabulary.length) {
      right += '<h3>' + icon('book') + 'Important English Vocabulary</h3><table class="tbl"><thead><tr><th>English</th><th>తెలుగు అర్థం</th><th></th></tr></thead><tbody>' +
        part.vocabulary.map(function (v) {
          return '<tr><td><b>' + esc(v.english) + '</b></td><td class="te" lang="te">' + esc(v.telugu) + '</td><td>' + (speechOK ? '<button class="speak-btn" data-say="' + esc(v.english) + '" aria-label="Pronounce ' + esc(v.english) + '">' + icon('speaker') + '</button>' : '') + '</td></tr>';
        }).join('') + '</tbody></table>';
    }
    if (part.speakingPractice && part.speakingPractice.sentences && part.speakingPractice.sentences.length) {
      left += '<h3>' + icon('mic') + 'Speaking Practice</h3>' + (part.speakingPractice.intro ? '<p lang="te" class="te">' + esc(part.speakingPractice.intro) + '</p>' : '') +
        '<ul class="say-list">' + part.speakingPractice.sentences.map(function (s) {
          return '<li><span>' + esc(s) + '</span>' + (speechOK ? '<button class="speak-btn" data-say="' + esc(s) + '" aria-label="Listen">' + icon('speaker') + '</button>' : '') + '</li>';
        }).join('') + '</ul>';
    }
    if (part.extras && part.extras.length) {
      part.extras.forEach(function (x, i) {
        var block = '<h3>' + icon(i ? 'note' : 'mic') + esc(x.heading) + '</h3><div class="extra-box">' + fmt(x.body) + '</div>';
        if (i % 2 === 0) left += block; else right += block;
      });
    }
    if (part.nextPreview) {
      right += '<h3>' + icon('right') + esc(part.nextPreview.heading || 'Next Part') + '</h3><div class="next-preview">' +
        (part.nextPreview.title ? '<b>' + esc(part.nextPreview.title) + '</b>' : '') +
        (part.nextPreview.questions.length ? '<ol>' + part.nextPreview.questions.map(function (q) { return '<li>' + esc(q) + '</li>'; }).join('') + '</ol>' : '') + '</div>';
    }
    return h + '<div>' + left + '</div><div>' + right + '</div></div></div>';
  }

  RENDER.read = function (opts) {
    var b = curBook(), view = $('#view-read');
    if (!b.pages.length) {
      view.innerHTML = '<div class="empty">' + icon('book') + (b.id === 'my'
        ? '<h3>Create your own important questions</h3><p>Add interview questions you want to prepare, with your own Telugu and English answers. They get search, bookmarks, notes, progress and PDF export like the rest of the book.</p><p style="margin-top:16px"><button class="btn primary" data-act="add-my">' + icon('plus') + 'Add a question</button></p>'
        : '<h3>No content yet</h3><p>Use Settings → Import a Part to add content.</p>') + '</div>';
      return;
    }
    var idx = Math.min(S.position.page[b.id] || 0, b.pages.length - 1);
    S.position.page[b.id] = idx;
    var pg = b.pages[idx], part = pg.part;
    var q = pg.type === 'q' ? INDEX[pg.id].item : null;
    var crumbs = '<div class="read-top"><div class="crumb"><b>' + esc(partLabel(part)) + '</b><span class="part-title">' + esc(part.title) + '</span>' +
      (rangeLabel(part) ? '<span class="muted">· ' + esc(rangeLabel(part)) + '</span>' : '') + '</div>' +
      (b.draft ? '<span class="draft-flag" title="Answers are from your handbook. Telugu question translations and examples were added by Claude — review them.">Examples &amp; Telugu questions added by Claude</span>' : '') +
      (part.imported ? '<span class="draft-flag" style="background:var(--indigo-soft);color:var(--indigo)">Imported in this browser</span>' : '') + '</div>';
    view.innerHTML = crumbs + '<article class="book ' + (opts.dir > 0 ? 'turn-next' : opts.dir < 0 ? 'turn-prev' : '') + '" id="bookEl">' +
      (q ? questionPage(b, q, part) : reviewPage(b, part)) + footHTML(b, idx) + '</article>';
    fitBook();
    if (q) { applyHighlights(q.questionId); Store.visit(q.questionId); }
    if (location.hash !== '#' + (q ? q.questionId : '')) history.replaceState(null, '', q ? '#' + q.questionId : location.pathname + location.search);
  };

  /* Fit the book to the window on desktop: no page scroll, long pages scroll inside */
  function fitBook() {
    var el = $('#bookEl'); if (!el) return;
    if (window.innerWidth <= 1100) { el.classList.remove('fit'); el.style.height = ''; return; }
    el.classList.add('fit');
    var top = el.getBoundingClientRect().top + window.scrollY;
    el.style.height = Math.max(460, window.innerHeight - top - 22) + 'px';
  }
  window.addEventListener('resize', function () { if (S.position.tab === 'read') fitBook(); });

  /* ---------------- Read view events (delegated) ---------------- */
  function onReadClick(e) {
    var t = e.target.closest('[data-nav],[data-act],[data-open],[data-say]'); if (!t) return;
    var b = curBook(), idx = S.position.page[b.id] || 0, pg = b.pages[idx];
    var id = pg && pg.type === 'q' ? pg.id : null;
    if (t.hasAttribute('data-open')) { e.preventDefault(); openItem(t.getAttribute('data-open')); return; }
    if (t.hasAttribute('data-say')) { speak(t.getAttribute('data-say')); return; }
    var nav = t.getAttribute('data-nav');
    if (nav === 'prev') return goPage(idx - 1, -1);
    if (nav === 'next') return goPage(idx + 1, 1);
    if (nav === 'prevq') return stepQuestion(-1);
    if (nav === 'nextq') return stepQuestion(1);
    var act = t.getAttribute('data-act');
    if (act === 'add-my') return window.EIM.openMyQuestionEditor();
    if (!id) return;
    if (act === 'bm') { var on = Store.toggle('bookmarks', id); toast(on ? 'Bookmarked' : 'Bookmark removed'); RENDER.read({}); updateTabCounts(); }
    else if (act === 'fav') { var f = Store.toggle('favourites', id); toast(f ? 'Added to favourites' : 'Removed from favourites'); RENDER.read({}); updateTabCounts(); }
    else if (act === 'done') { var d = Store.toggle('completed', id); toast(d ? 'Marked as completed' : 'Marked as not completed'); RENDER.read({}); }
    else if (act === 'note') window.EIM.openNoteEditor({ qid: id });
    else if (act === 'english') { if ($('#enPanel').classList.contains('open')) closeEnglish(); else openEnglish(); }
    else if (act === 'edit-my') window.EIM.openMyQuestionEditor(id);
    else if (act === 'del-my') window.EIM.deleteMyQuestion(id);
  }
  function onReadChange(e) {
    var t = e.target;
    if (t.id === 'jumpPage') { var n = parseInt(t.value, 10); if (n) goPage(n - 1, n - 1 > (S.position.page[curBook().id] || 0) ? 1 : -1); }
    if (t.hasAttribute('data-step')) {
      var b = curBook(), id = b.pages[S.position.page[b.id]].id;
      var st = S.practice[id] || [false, false, false, false];
      st[+t.getAttribute('data-step')] = t.checked; S.practice[id] = st;
      if (st.every(Boolean) && !Store.has('completed', id)) { S.completed[id] = Date.now(); toast('All practice steps done — marked as completed'); }
      Store.save();
    }
  }

  /* ======================================================================
     ENGLISH PRACTICE PANEL
     ====================================================================== */
  var speechOK = 'speechSynthesis' in window;
  function speak(text, lang) {
    if (!speechOK) return;
    speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(text);
    u.lang = lang || 'en-IN';
    var voices = speechSynthesis.getVoices();
    var v = voices.filter(function (x) { return x.lang === u.lang; })[0] || voices.filter(function (x) { return /^en/.test(x.lang); })[0];
    if (v) u.voice = v;
    u.rate = .95;
    speechSynthesis.speak(u);
  }
  function currentQ() { var b = curBook(), pg = b.pages[S.position.page[b.id] || 0]; return pg && pg.type === 'q' ? INDEX[pg.id] : null; }

  function fillEnglish(id) {
    var e = INDEX[id]; if (!e) return;
    var q = e.item, masked = !!S.settings.practiceMode, panel = $('#enPanel');
    panel.setAttribute('data-id', id);
    panel.innerHTML =
      '<div class="en-head"><div style="flex:1"><span class="en-tag">' + icon('globe') + 'English Practice · ' + esc(numLabel(q)) + '</span>' +
      '<p class="en-q" lang="en">' + esc(q.questionEnglish) + '</p></div>' +
      '<button class="icon-btn" data-en="close" aria-label="Close English answer" title="Close (Esc)">' + icon('x') + '</button></div>' +
      '<div class="en-body">' +
        (masked ? '<div class="en-steps"><b>Practice mode:</b> try saying the answer in English first, then reveal it.<ol><li>Read the Telugu answer</li><li>Try answering in English aloud</li><li>Reveal and compare</li><li>Hide again and repeat</li></ol></div>' : '') +
        '<div class="en-answer' + (masked ? ' masked' : '') + '" lang="en" id="enAnswer">' + fmt(q.answerEnglish) +
          (q.exampleEnglish ? '<aside class="example-box en"><span class="ex-label">' + icon('bulb') + 'Example</span>' + fmt(q.exampleEnglish) + '</aside>' : '') + '</div>' +
        '<p class="mask-note"><button class="btn accent" data-en="reveal">' + icon('eye') + 'Reveal English answer</button></p>' +
      '</div>' +
      '<div class="en-tools">' +
        (speechOK ? '<button class="btn sm" data-en="speak">' + icon('speaker') + 'Read aloud</button><button class="btn sm ghost" data-en="stop">' + icon('stop') + 'Stop</button>' : '') +
        '<button class="btn sm" data-en="mask">' + icon(masked ? 'eye' : 'eyeOff') + (masked ? 'Reveal' : 'Hide &amp; try yourself') + '</button>' +
        '<button class="btn sm ghost" data-en="copy">' + icon('copy') + 'Copy</button>' +
        '<span class="spacer"></span><button class="btn sm ghost" data-en="close">Back to Telugu</button>' +
      '</div>';
    markVocab($('#enAnswer'), e.part.vocabulary || []);
  }
  function markVocab(root, vocab) {
    if (!root || !vocab.length) return;
    vocab.forEach(function (v) {
      var term = v.english; if (!term || term.length < 3) return;
      var rx = new RegExp('\\b(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\w{0,3})\\b', 'i');
      var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), node;
      while ((node = walker.nextNode())) {
        if (node.parentNode.classList && node.parentNode.classList.contains('vocab')) continue;
        var m = node.data.match(rx);
        if (m) {
          var r = document.createRange(); r.setStart(node, m.index); r.setEnd(node, m.index + m[0].length);
          var span = document.createElement('span'); span.className = 'vocab'; span.title = v.english + ' — ' + v.telugu;
          r.surroundContents(span); break;
        }
      }
    });
  }
  function openEnglish() {
    var e = currentQ(); if (!e || !e.item.answerEnglish) return;
    fillEnglish(e.item.questionId);
    var panel = $('#enPanel'), scrim = $('#enScrim');
    panel.classList.add('open'); panel.setAttribute('aria-hidden', 'false');
    document.body.classList.add('en-open');
    fitBook(); setTimeout(fitBook, 340);
    if (window.matchMedia('(max-width: 1100px)').matches) { scrim.hidden = false; requestAnimationFrame(function () { scrim.classList.add('on'); }); }
    var btn = $('[data-act="english"]'); if (btn) btn.setAttribute('aria-expanded', 'true');
    setTimeout(function () { panel.focus({ preventScroll: true }); }, 50);
  }
  function closeEnglish() {
    var panel = $('#enPanel'), scrim = $('#enScrim');
    if (!panel.classList.contains('open')) return;
    panel.classList.remove('open'); panel.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('en-open');
    fitBook(); setTimeout(fitBook, 340);
    scrim.classList.remove('on'); setTimeout(function () { scrim.hidden = true; }, 250);
    if (speechOK) speechSynthesis.cancel();
    var btn = $('[data-act="english"]'); if (btn) { btn.setAttribute('aria-expanded', 'false'); btn.focus({ preventScroll: true }); }
  }
  function onPanelClick(e) {
    var t = e.target.closest('[data-en]'); if (!t) return;
    var a = t.getAttribute('data-en'), ans = $('#enAnswer');
    if (a === 'close') closeEnglish();
    else if (a === 'speak') speak(ans.innerText);
    else if (a === 'stop') speechSynthesis.cancel();
    else if (a === 'reveal' || a === 'mask') {
      var masked = a === 'reveal' ? false : !ans.classList.contains('masked');
      ans.classList.toggle('masked', masked);
      var mb = $('[data-en="mask"]'); mb.innerHTML = icon(masked ? 'eye' : 'eyeOff') + (masked ? 'Reveal' : 'Hide &amp; try yourself');
    } else if (a === 'copy') {
      (navigator.clipboard ? navigator.clipboard.writeText(ans.innerText) : Promise.reject()).then(function () { toast('English answer copied'); }, function () { toast('Copy not available here'); });
    }
  }

  /* ======================================================================
     USER HIGHLIGHTS (yellow marker on the Telugu answer)
     ====================================================================== */
  function wrapText(root, text, idx) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), nodes = [], full = '', n;
    while ((n = walker.nextNode())) { nodes.push({ node: n, start: full.length }); full += n.data; }
    var at = full.indexOf(text); if (at < 0) return false;
    var end = at + text.length;
    nodes.forEach(function (o) {
      var s = Math.max(at, o.start), e = Math.min(end, o.start + o.node.data.length);
      if (s >= e) return;
      var r = document.createRange(); r.setStart(o.node, s - o.start); r.setEnd(o.node, e - o.start);
      var mark = document.createElement('mark'); mark.className = 'user-hl'; mark.setAttribute('data-h', idx); mark.title = 'Click to remove highlight';
      r.surroundContents(mark);
    });
    return true;
  }
  function applyHighlights(id) {
    var root = $('#teAnswer'); if (!root) return;
    (S.highlights[id] || []).forEach(function (t, i) { wrapText(root, t, i); });
  }
  var pendingSel = null;
  function onSelection() {
    var f = $('#hlFloat'), sel = window.getSelection();
    var root = $('#teAnswer');
    if (!root || !sel || sel.isCollapsed || !sel.rangeCount) { f.hidden = true; pendingSel = null; return; }
    var range = sel.getRangeAt(0);
    if (!root.contains(range.commonAncestorContainer)) { f.hidden = true; return; }
    var text = sel.toString();
    if (!text.trim() || text.trim().length < 2) { f.hidden = true; return; }
    pendingSel = text;
    var rect = range.getBoundingClientRect();
    f.style.left = Math.max(8, rect.left + window.scrollX + rect.width / 2 - 45) + 'px';
    f.style.top = (rect.top + window.scrollY - 42) + 'px';
    f.hidden = false;
  }
  function saveHighlight() {
    var e = currentQ(); if (!e || !pendingSel) return;
    var text = pendingSel;
    if (/\n/.test(text.trim())) { toast('Please highlight within one paragraph at a time.'); $('#hlFloat').hidden = true; return; }
    text = text.replace(/\s+$/, '').replace(/^\s+/, '');
    var id = e.item.questionId;
    (S.highlights[id] = S.highlights[id] || []).push(text); Store.save();
    window.getSelection().removeAllRanges(); $('#hlFloat').hidden = true; pendingSel = null;
    RENDER.read({}); toast('Highlighted');
  }
  function onMarkClick(e) {
    var m = e.target.closest('mark.user-hl'); if (!m) return;
    var q = currentQ(); if (!q) return;
    var id = q.item.questionId, i = +m.getAttribute('data-h'), list = S.highlights[id] || [];
    var removed = list.splice(i, 1)[0]; Store.save(); RENDER.read({});
    toast('Highlight removed', 'Undo', function () { list.splice(i, 0, removed); S.highlights[id] = list; Store.save(); RENDER.read({}); });
  }

  /* ======================================================================
     TABLE OF CONTENTS
     ====================================================================== */
  function statusIcons(id) {
    return '<span class="tq-s">' +
      (Store.has('bookmarks', id) ? '<span class="on-bm" title="Bookmarked">' + icon('bookmark') + '</span>' : '') +
      (Store.has('favourites', id) ? '<span class="on-fav" title="Favourite">' + icon('star') + '</span>' : '') +
      (Store.has('completed', id) ? '<span class="on-done" title="Completed">' + icon('check') + '</span>' : '') + '</span>';
  }
  function partDone(part) { return part.questions.filter(function (q) { return Store.has('completed', q.questionId); }).length; }

  RENDER.toc = function () {
    var b = curBook(), view = $('#view-toc');
    var nQ = b.items.length;
    var audit = '';
    if (b.missing && b.missing.length) {
      audit = '<div class="audit-banner">' + icon('alert') + '<div><b>' + (b.parts.length) + ' of ' + b.maxPart + ' parts are in the book (' + nQ + ' questions).</b>' +
        'Missing: ' + (b.missing.length > 1 ? 'Parts ' : 'Part ') + compactRange(b.missing) + '. These were not in the supplied source, so nothing has been invented. Paste each part from ChatGPT using <a href="#" data-act="import">Import a Part</a>, or add files to <code>data/raw/</code>.</div></div>';
    }
    if (b.draft) audit = '<div class="audit-banner">' + icon('bulb') + '<div><b>Product Design Interview Preparation Handbook — 88 questions.</b>English answers and Telugu explanations are your original text, unchanged. The Telugu question translations and the practical examples (ఉదాహరణ) were added by Claude — review them, and replace illustrative examples with your real project facts. Source: <code>data/raw/ux-handbook.txt</code> + <code>ux-additions-*.json</code>.</div></div>';
    var rows = [];
    for (var n = 1; n <= Math.max(b.maxPart, b.parts.length); n++) {
      var part = b.parts.filter(function (p) { return p.partNumber === n; })[0];
      if (!part) {
        if (!b.expected) continue;
        var runEnd = n;
        while (runEnd + 1 <= b.maxPart && !b.parts.some(function (p) { return p.partNumber === runEnd + 1; })) runEnd++;
        var lbl = runEnd > n ? n + '–' + runEnd : '' + n;
        rows.push('<div class="toc-part missing" data-filter="' + esc(b.partLabel.toLowerCase()) + ' ' + lbl + '"><summary style="display:grid"><div class="toc-pn">' + esc(b.partLabel) + (runEnd > n ? 's' : '') + '<b>' + lbl + '</b></div><div><div class="toc-title">Not added yet</div><div class="toc-meta">' + (runEnd - n + 1) + ' part' + (runEnd > n ? 's' : '') + ' · source not supplied, nothing invented</div></div><div class="toc-stat"><button class="btn sm" data-act="import">' + icon('upload') + 'Import a Part</button></div></summary></div>');
        n = runEnd;
        continue;
      }
      var done = partDone(part), pct = part.questions.length ? Math.round(done / part.questions.length * 100) : 0;
      var filterText = (part.title + ' ' + part.questions.map(function (q) { return q.questionEnglish + ' ' + q.questionTelugu + ' ' + q.questionNumber; }).join(' ')).toLowerCase();
      rows.push('<details class="toc-part" data-filter="' + esc(b.partLabel.toLowerCase() + ' ' + n + ' ' + filterText) + '"' + (b.parts.length <= 3 ? ' open' : '') + '>' +
        '<summary><div class="toc-pn">' + esc(b.partLabel) + '<b>' + n + '</b></div>' +
        '<div><div class="toc-title">' + esc(part.title) + '</div><div class="toc-meta">' + esc(rangeLabel(part)) + ' · ' + part.questions.length + ' question' + (part.questions.length === 1 ? '' : 's') + (part.imported ? ' · imported' : '') + '</div></div>' +
        '<div class="toc-stat"><span>' + done + '/' + part.questions.length + '</span><span class="mini-bar"><span style="width:' + pct + '%"></span></span></div></summary>' +
        '<ul class="toc-qs">' + part.questions.map(function (q) {
          return '<li><button data-open="' + esc(q.questionId) + '"><span class="tq-n">' + esc(numLabel(q)) + '</span><span class="tq-t">' + esc(q.questionEnglish) + (q.questionTelugu ? '<small lang="te">' + esc(q.questionTelugu) + '</small>' : '') + '</span>' + statusIcons(q.questionId) + '</button></li>';
        }).join('') +
        (b.pages.some(function (p) { return p.type === 'review' && p.part === part; }) ? '<li><button data-review="' + esc(part.partId) + '"><span class="tq-n">' + icon('bulb') + '</span><span class="tq-t">Part review — revision, vocabulary &amp; speaking practice</span><span></span></button></li>' : '') +
        '</ul></details>');
    }
    view.innerHTML = '<div class="view-head"><div><h2 class="view-title">Table of Contents</h2><p class="view-sub">' + esc(b.title) + ' · <span lang="te">' + esc(b.te) + '</span> · ' + b.parts.length + ' ' + esc(b.partLabel.toLowerCase()) + (b.parts.length === 1 ? '' : 's') + ' · ' + nQ + ' questions</p></div>' +
      '<div class="row">' + (b.id === 'my' ? '<button class="btn primary" data-act="add-my">' + icon('plus') + 'Add a question</button>' : '') + '</div></div>' + audit +
      '<div class="toc-tools"><input class="input" id="tocFilter" placeholder="Jump to a part or question (English / తెలుగు / number)…" style="flex:1;min-width:220px" aria-label="Filter contents">' +
      '<button class="btn" data-act="expand">Expand all</button><button class="btn" data-act="collapse">Collapse all</button></div>' +
      '<div class="toc-list">' + (rows.join('') || '<div class="empty"><h3>Nothing here yet</h3><p>' + (b.id === 'my' ? 'Add your own important questions to build this book.' : '') + '</p></div>') + '</div>';
  };
  function compactRange(nums) {
    var out = [], s = nums[0], p = nums[0];
    for (var i = 1; i <= nums.length; i++) {
      if (nums[i] === p + 1) { p = nums[i]; continue; }
      out.push(s === p ? '' + s : s + '–' + p); s = p = nums[i];
    }
    return out.join(', ');
  }
  function onTocClick(e) {
    var t = e.target.closest('[data-open],[data-act],[data-review]'); if (!t) return;
    if (t.hasAttribute('data-open')) return openItem(t.getAttribute('data-open'));
    if (t.hasAttribute('data-review')) {
      var b = curBook(), pid = t.getAttribute('data-review');
      var i = b.pages.findIndex(function (p) { return p.type === 'review' && p.part.partId === pid; });
      S.position.page[b.id] = i; Store.save(); return setTab('read');
    }
    var a = t.getAttribute('data-act');
    if (a === 'expand' || a === 'collapse') $$('#view-toc details').forEach(function (d) { d.open = a === 'expand'; });
    if (a === 'import') { e.preventDefault(); openSettings('import'); }
    if (a === 'add-my') window.EIM.openMyQuestionEditor();
  }
  function onTocInput(e) {
    if (e.target.id !== 'tocFilter') return;
    var v = e.target.value.trim().toLowerCase().replace(/^q\s?/, '');
    $$('#view-toc .toc-part').forEach(function (d) {
      var hit = !v || (d.getAttribute('data-filter') || '').indexOf(v) >= 0;
      d.hidden = !hit;
      if (d.tagName === 'DETAILS') {
        d.open = !!v && hit;
        $$('.toc-qs li', d).forEach(function (li) { li.hidden = !!v && li.textContent.toLowerCase().indexOf(v) < 0 && (d.getAttribute('data-filter').split(' ').slice(0, 2).join(' ').indexOf(v) < 0); });
      }
    });
  }

  /* ======================================================================
     BOOKMARKS & FAVOURITES
     ====================================================================== */
  function qCard(id, setName, ts) {
    var e = INDEX[id];
    if (!e) return '<div class="q-card"><div class="qc-num">—</div><div><p class="qc-en">Content not available (' + esc(id) + ')</p><p class="muted" style="margin:0">It may have been an imported part or a question you deleted.</p></div><div class="qc-actions"><button class="btn sm danger" data-remove="' + esc(id) + '" data-set="' + setName + '">Remove</button></div></div>';
    var q = e.item;
    return '<div class="q-card"><div class="qc-num">' + esc(numLabel(q)) + '</div>' +
      '<button class="qc-open" data-open="' + esc(id) + '"><div class="qc-part">' + esc(e.book.title) + ' · ' + esc(partLabel(e.part)) + ' — ' + esc(e.part.title) + (ts ? ' · saved ' + fmtDate(ts) : '') + '</div>' +
      '<p class="qc-en">' + esc(q.questionEnglish) + '</p>' + (q.questionTelugu ? '<p class="qc-te" lang="te">' + esc(q.questionTelugu) + '</p>' : '') + '</button>' +
      '<div class="qc-actions">' + (setName ? '<button class="btn sm ghost danger" data-remove="' + esc(id) + '" data-set="' + setName + '" title="Remove">' + icon('x') + '<span class="sr-only">Remove</span></button>' : '') +
      '<button class="btn sm" data-open="' + esc(id) + '">Open</button></div></div>';
  }
  function listView(setName, title, sub, emptyIcon, emptyText) {
    var ids = Object.keys(S[setName]).sort(function (a, b) { return S[setName][b] - S[setName][a]; });
    return '<div class="view-head"><div><h2 class="view-title">' + title + '</h2><p class="view-sub">' + sub + ' · ' + ids.length + ' saved</p></div></div>' +
      (ids.length ? '<div class="card-list">' + ids.map(function (id) { return qCard(id, setName, S[setName][id]); }).join('') + '</div>'
        : '<div class="empty">' + icon(emptyIcon) + '<h3>Nothing saved yet</h3><p>' + emptyText + '</p></div>');
  }
  RENDER.bookmarks = function () { $('#view-bookmarks').innerHTML = listView('bookmarks', 'Bookmarks', 'Questions you want to come back to', 'bookmark', 'Use the Bookmark button on any question page to keep your place or mark a question to revisit.'); };
  RENDER.favourites = function () { $('#view-favourites').innerHTML = listView('favourites', 'Favourites', 'Your best and most-loved answers', 'star', 'Tap the ★ Favourite button on any question to collect the answers you like most.'); };
  function onListClick(e) {
    var t = e.target.closest('[data-open],[data-remove]'); if (!t) return;
    if (t.hasAttribute('data-open')) return openItem(t.getAttribute('data-open'));
    var id = t.getAttribute('data-remove'), set = t.getAttribute('data-set'), ts = S[set][id];
    delete S[set][id]; Store.save(); RENDER[set](); updateTabCounts();
    toast('Removed', 'Undo', function () { S[set][id] = ts; Store.save(); RENDER[set](); updateTabCounts(); });
  }

  /* ======================================================================
     READING PROGRESS
     ====================================================================== */
  RENDER.progress = function () {
    var all = [], partsTotal = 0, partsDone = 0;
    BOOKS.forEach(function (b) {
      all = all.concat(b.items);
      b.parts.forEach(function (p) { if (!p.questions.length) return; partsTotal++; if (partDone(p) === p.questions.length) partsDone++; });
    });
    var qDone = all.filter(function (q) { return Store.has('completed', q.questionId); }).length;
    var pct = all.length ? Math.round(qDone / all.length * 100) : 0;
    var cb = curBook(), cIdx = S.position.page[cb.id] || 0, cPg = cb.pages[cIdx];
    var posLabel = cPg ? (cPg.type === 'q' ? numLabel(INDEX[cPg.id].item) + ' · ' + partLabel(cPg.part) : partLabel(cPg.part) + ' review') : '—';
    var h = '<div class="view-head"><div><h2 class="view-title">Reading Progress</h2><p class="view-sub">Across all books · mark questions as completed on each page</p></div>' +
      '<button class="btn primary" data-act="resume">' + icon('book') + 'Continue reading — ' + esc(cb.title) + ', ' + esc(posLabel) + '</button></div>';
    h += '<div class="stats">' +
      '<div class="stat big"><div class="ring" style="--p:' + pct + '"></div><div class="s-v">' + pct + '%</div><div class="s-l">Overall completion</div></div>' +
      '<div class="stat"><div class="s-v">' + qDone + ' / ' + all.length + '</div><div class="s-l">Questions completed</div></div>' +
      '<div class="stat"><div class="s-v">' + partsDone + ' / ' + partsTotal + '</div><div class="s-l">Parts completed</div></div>' +
      '<div class="stat"><div class="s-v">' + book('iq').parts.length + ' / ' + book('iq').maxPart + '</div><div class="s-l">Interview parts in book</div></div>' +
      '<div class="stat"><div class="s-v" style="font-size:1.25rem;padding-top:8px">' + esc(posLabel) + '</div><div class="s-l">Current position (' + esc(cb.title) + ')</div></div></div>';
    var books = '<div class="panel"><h3>By book</h3>' + BOOKS.map(function (b) {
      var d = b.items.filter(function (q) { return Store.has('completed', q.questionId); }).length, p = b.items.length ? Math.round(d / b.items.length * 100) : 0;
      return '<div class="bar-row"><span>' + esc(b.title) + ' <span class="muted">(' + d + '/' + b.items.length + ')</span></span><span class="bar"><span style="width:' + p + '%"></span></span><span class="muted">' + p + '%</span></div>';
    }).join('') + '<h3 style="margin-top:24px">' + esc(cb.title) + ' — by ' + esc(cb.partLabel.toLowerCase()) + '</h3>' +
      (cb.parts.length ? cb.parts.map(function (p) {
        var d = partDone(p), pc = p.questions.length ? Math.round(d / p.questions.length * 100) : 0;
        return '<div class="bar-row"><span>' + esc(partLabel(p)) + ' · ' + esc(p.title) + '</span><span class="bar"><span style="width:' + pc + '%"></span></span><span class="muted">' + d + '/' + p.questions.length + '</span></div>';
      }).join('') : '<p class="muted">No content yet.</p>') + '</div>';
    var hist = '<div class="panel"><h3>Reading history</h3>' + (S.history.length ? S.history.slice(0, 15).map(function (hh) {
      var e = INDEX[hh.id]; if (!e) return '';
      return '<button class="hist-item" data-open="' + esc(hh.id) + '"><span class="h-n">' + esc(numLabel(e.item)) + '</span><span class="h-t">' + esc(e.item.questionEnglish) + '</span><span class="h-d">' + fmtDate(hh.ts) + '</span></button>';
    }).join('') : '<p class="muted">Questions you open will appear here.</p>') + '</div>';
    $('#view-progress').innerHTML = h + '<div class="prog-grid">' + books + hist + '</div>';
  };
  function onProgressClick(e) {
    var t = e.target.closest('[data-open],[data-act]'); if (!t) return;
    if (t.hasAttribute('data-open')) return openItem(t.getAttribute('data-open'));
    if (t.getAttribute('data-act') === 'resume') setTab('read');
  }

  /* ======================================================================
     SETTINGS DIALOG — display · import a part · backup · PDF
     ====================================================================== */
  var dlg = $('#dlg');
  function openDialog(html, onClick) {
    $('#dlgBody').innerHTML = html;
    dlg.onclick = function (e) {
      if (e.target === dlg) return dlg.close();
      var x = e.target.closest('[data-close]'); if (x) return dlg.close();
      if (onClick) onClick(e);
    };
    if (!dlg.open) dlg.showModal();
  }
  function closeDialog() { if (dlg.open) dlg.close(); }

  var importDraft = null;
  function settingsHTML(section) {
    var navs = [['display', 'Display & practice'], ['import', 'Import a Part'], ['pdf', 'PDF export'], ['backup', 'Backup & restore']];
    var h = '<button class="icon-btn modal-x" data-close aria-label="Close">' + icon('x') + '</button><h2>Settings &amp; tools</h2>' +
      '<div class="settings-nav">' + navs.map(function (n) { return '<button class="chip" data-sec="' + n[0] + '" aria-pressed="' + (n[0] === section) + '">' + n[1] + '</button>'; }).join('') + '</div>';
    if (section === 'display') {
      h += '<h3>Reading</h3><div class="field"><label for="fScale">Text size — ' + Math.round(S.settings.fontScale * 100) + '%</label><input type="range" id="fScale" min="0.9" max="1.35" step="0.05" value="' + S.settings.fontScale + '"></div>' +
        '<div class="field"><label>Theme</label><div class="seg"><button data-theme-set="paper" aria-pressed="' + (S.settings.theme === 'paper') + '">Paper</button><button data-theme-set="night" aria-pressed="' + (S.settings.theme === 'night') + '">Night</button></div></div>' +
        '<h3>Practice</h3><label class="switch"><input type="checkbox" id="practiceMode" ' + (S.settings.practiceMode ? 'checked' : '') + '> Practice Mode — show a 4-step checklist on each question, and keep the English answer blurred until you reveal it</label>' +
        '<p class="muted" style="font-size:.86rem">English answers are always hidden by default. Practice Mode adds the checklist and an extra "reveal" step.</p>';
    } else if (section === 'import') {
      var imported = S.importedParts.map(function (ip, i) {
        return '<div class="bar-row" style="grid-template-columns:1fr auto auto"><span><b>Part ' + ip.part.partNumber + '</b> · ' + esc(ip.part.title) + ' <span class="muted">(' + ip.part.questions.length + ' Q)</span></span><button class="btn sm ghost" data-dl-raw="' + i + '">' + icon('download') + '.txt</button><button class="btn sm ghost danger" data-rm-import="' + i + '">' + icon('trash') + '</button></div>';
      }).join('');
      h += '<p class="muted" style="font-size:.9rem;margin-top:12px">Copy one complete part from ChatGPT (from the "Part N – Title" heading to the end of Speaking Practice) and paste it here. Text is stored exactly as pasted — nothing is rewritten.</p>' +
        '<div class="field"><label for="importText">Part text</label><textarea class="tall" id="importText" placeholder="Part 12 – Usability Testing&#10;&#10;Q90. What is usability testing?&#10;&#10;తెలుగు అర్థం: …&#10;&#10;తెలుగు సమాధానం:&#10;…&#10;&#10;English Answer:&#10;…">' + esc(importDraft || '') + '</textarea></div>' +
        '<div class="row"><button class="btn" data-act="check-import">Check content</button><span class="spacer"></span><span id="importStatus"></span></div><div id="importReport"></div>' +
        '<h3>Imported in this browser</h3>' + (imported || '<p class="muted">None yet.</p>') +
        '<h3>Publish to GitHub</h3><p class="muted" style="font-size:.88rem">Imported parts live in this browser only. To make them part of the published book for every device, download the updated data file and replace <code>data/parts.js</code> in your repository (or save each part\'s .txt into <code>data/raw/</code> and run <code>node tools/build-data.js</code>).</p>' +
        '<button class="btn" data-act="dl-parts">' + icon('download') + 'Download updated data/parts.js</button>';
    } else if (section === 'pdf') {
      h += '<p class="muted" style="font-size:.9rem;margin-top:12px">Creates a landscape, book-style print layout with page numbers. In the print dialog choose <b>Save as PDF</b>. Telugu fonts are bundled, so characters render correctly.</p>' +
        '<h3>What to include</h3><div class="field"><label for="pdfScope">Content</label><select id="pdfScope">' +
        '<option value="book">This book — ' + esc(curBook().title) + '</option><option value="part">Current ' + esc(curBook().partLabel.toLowerCase()) + ' only</option><option value="all">All books</option><option value="saved">My bookmarks + favourites</option></select></div>' +
        '<label class="switch"><input type="checkbox" id="pdfEnglish" ' + (S.settings.pdfEnglish ? 'checked' : '') + '> Include English answers (side by side with Telugu)</label>' +
        '<label class="switch"><input type="checkbox" id="pdfReview" checked> Include revision tables, vocabulary &amp; speaking practice</label>' +
        '<label class="switch"><input type="checkbox" id="pdfNotes"> Include my notebook entries under each question</label>' +
        '<div class="modal-foot"><button class="btn" data-close>Cancel</button><button class="btn primary" data-act="make-pdf">' + icon('print') + 'Create PDF</button></div>';
    } else if (section === 'backup') {
      h += '<p class="muted" style="font-size:.9rem;margin-top:12px">Your bookmarks, favourites, highlights, notes, my questions, imported parts and progress are saved in this browser. Download a backup to keep them safe or move them to another device.</p>' +
        '<div class="row" style="margin:14px 0"><button class="btn primary" data-act="backup">' + icon('download') + 'Download backup (.json)</button>' +
        '<label class="btn">' + icon('upload') + 'Restore from backup<input type="file" id="restoreFile" accept=".json,application/json" hidden></label></div>' +
        '<h3>Danger zone</h3><button class="btn danger" data-act="reset">Erase all my data in this browser</button>';
    }
    return h;
  }
  function openSettings(section) {
    section = section || 'display';
    openDialog(settingsHTML(section), function (e) {
      var t = e.target.closest('[data-sec],[data-act],[data-theme-set],[data-rm-import],[data-dl-raw]'); if (!t) return;
      if (t.hasAttribute('data-sec')) { saveImportDraft(); return openSettings(t.getAttribute('data-sec')); }
      if (t.hasAttribute('data-theme-set')) { S.settings.theme = t.getAttribute('data-theme-set'); Store.save(); applySettings(); return openSettings('display'); }
      if (t.hasAttribute('data-rm-import')) {
        var i = +t.getAttribute('data-rm-import'), ip = S.importedParts[i];
        S.importedParts.splice(i, 1); Store.save(); rebuild(); toast('Removed imported Part ' + ip.part.partNumber); return openSettings('import');
      }
      if (t.hasAttribute('data-dl-raw')) { var r = S.importedParts[+t.getAttribute('data-dl-raw')]; return download('part-' + String(r.part.partNumber).padStart(2, '0') + '.txt', r.raw, 'text/plain;charset=utf-8'); }
      var a = t.getAttribute('data-act');
      if (a === 'check-import') checkImport();
      else if (a === 'add-import') addImport();
      else if (a === 'dl-parts') downloadParts();
      else if (a === 'backup') download('interview-mastery-backup-' + new Date().toISOString().slice(0, 10) + '.json', Store.exportJSON(), 'application/json');
      else if (a === 'reset') {
        if (t.getAttribute('data-armed')) { Store.reset(); location.reload(); }
        else { t.setAttribute('data-armed', '1'); t.textContent = 'Click again to permanently erase everything'; }
      } else if (a === 'make-pdf') {
        var opts = { scope: $('#pdfScope').value, english: $('#pdfEnglish').checked, review: $('#pdfReview').checked, notes: $('#pdfNotes').checked };
        S.settings.pdfEnglish = opts.english; Store.save(); closeDialog();
        window.EIM.exportPDF(opts);
      }
    });
    var fs = $('#fScale'); if (fs) fs.oninput = function () { S.settings.fontScale = +fs.value; Store.save(); applySettings(); fs.previousElementSibling.textContent = 'Text size — ' + Math.round(S.settings.fontScale * 100) + '%'; };
    var pm = $('#practiceMode'); if (pm) pm.onchange = function () { S.settings.practiceMode = pm.checked; Store.save(); if (S.position.tab === 'read') RENDER.read({}); toast(pm.checked ? 'Practice Mode on' : 'Practice Mode off'); };
    var rf = $('#restoreFile'); if (rf) rf.onchange = function () {
      var f = rf.files[0]; if (!f) return;
      var rd = new FileReader();
      rd.onload = function () {
        try { Store.importJSON(rd.result); S = Store.data; closeDialog(); applySettings(); rebuild(); toast('Backup restored'); }
        catch (err) { toast(err.message || 'Could not read that file'); }
      };
      rd.readAsText(f);
    };
  }
  function saveImportDraft() { var ta = $('#importText'); if (ta) importDraft = ta.value; }
  var parsedImport = null;
  function checkImport() {
    var raw = $('#importText').value; importDraft = raw;
    if (!raw.trim()) { $('#importReport').innerHTML = '<div class="parse-report bad">Paste a part first.</div>'; return; }
    var res = window.PartParser.parsePart(raw);
    parsedImport = { part: res.part, raw: raw };
    var p = res.part, ok = p.partNumber !== null && p.questions.length > 0;
    var exists = book('iq').parts.some(function (x) { return x.partNumber === p.partNumber; });
    $('#importReport').innerHTML = '<div class="parse-report ' + (ok ? (res.warnings.length ? '' : 'ok') : 'bad') + '">' +
      (ok ? '<b>Part ' + p.partNumber + ' – ' + esc(p.title) + '</b><br>' + p.questions.length + ' questions (' + esc(rangeLabel({ bookId: 'iq', questions: p.questions.map(function (q) { q.bookId = 'iq'; return q; }) })) + ') · ' + p.revision.length + ' revision rows · ' + p.vocabulary.length + ' vocabulary words · ' + (p.speakingPractice ? p.speakingPractice.sentences.length : 0) + ' speaking sentences'
        : '<b>Could not find a "Part N – Title" heading or any "Q123." questions.</b>') +
      (res.warnings.length ? '<ul>' + res.warnings.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join('') + '</ul>' : '') + '</div>' +
      (ok ? '<div class="modal-foot"><button class="btn primary" data-act="add-import">' + icon('plus') + (exists ? 'Replace Part ' + p.partNumber : 'Add Part ' + p.partNumber + ' to the book') + '</button></div>' : '');
  }
  function addImport() {
    if (!parsedImport) return;
    var n = parsedImport.part.partNumber;
    S.importedParts = S.importedParts.filter(function (ip) { return ip.part.partNumber !== n; });
    S.importedParts.push(parsedImport); S.importedParts.sort(function (a, b) { return a.part.partNumber - b.part.partNumber; });
    if (!Store.save()) { toast('Browser storage is full — download a backup and try a smaller part.'); return; }
    importDraft = ''; parsedImport = null; rebuild();
    toast('Part ' + n + ' added to the book'); openSettings('import');
  }
  function downloadParts() {
    var parts = book('iq').parts.map(function (p) {
      var c = clone(p); delete c.bookId; delete c.imported;
      c.questions.forEach(function (q) { delete q.bookId; delete q.partId; delete q.first; }); return c;
    });
    var n = parts.reduce(function (s, p) { return s + p.questions.length; }, 0);
    download('parts.js', '/* Exported from the app on ' + new Date().toISOString() + '. Parts: ' + parts.length + ' · Questions: ' + n + ' */\nwindow.BOOK_PARTS = ' + JSON.stringify(parts, null, 1) + ';\n', 'text/javascript;charset=utf-8');
  }

  function applySettings() {
    document.documentElement.setAttribute('data-theme', S.settings.theme === 'night' ? 'night' : 'paper');
    document.documentElement.style.setProperty('--scale', S.settings.fontScale || 1);
  }

  /* ======================================================================
     KEYBOARD
     ====================================================================== */
  function onKey(e) {
    if (dlg.open) return;
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === 'Escape') return closeEnglish();
    if (S.position.tab !== 'read') { if (e.key === '/') { e.preventDefault(); setTab('search'); } return; }
    var b = curBook(), i = S.position.page[b.id] || 0;
    if (e.key === 'ArrowRight') { e.preventDefault(); goPage(i + 1, 1); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); goPage(i - 1, -1); }
    else if (e.key === 'e' || e.key === 'E') { var btn = $('[data-act="english"]'); if (btn) btn.click(); }
    else if (e.key === 'b' || e.key === 'B') { var bb = $('[data-act="bm"]'); if (bb) bb.click(); }
    else if (e.key === 'f' || e.key === 'F') { var fb = $('[data-act="fav"]'); if (fb) fb.click(); }
    else if (e.key === '/') { e.preventDefault(); setTab('search'); }
  }

  /* ======================================================================
     INIT
     ====================================================================== */
  function rebuild() { buildBooks(); renderBookSwitch(); setTab(S.position.tab, { keepScroll: true }); }

  function init() {
    applySettings();
    $('#btnPrint').innerHTML = icon('print');
    $('#btnSettings').innerHTML = icon('gear');
    buildBooks();
    renderBookSwitch();

    $('#tabs').addEventListener('click', function (e) { var b = e.target.closest('[data-tab]'); if (b) setTab(b.getAttribute('data-tab')); });
    $('#tabs').addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      var i = TABS.indexOf(S.position.tab) + (e.key === 'ArrowRight' ? 1 : -1);
      i = (i + TABS.length) % TABS.length; setTab(TABS[i]); $('#tabs [data-tab="' + TABS[i] + '"]').focus(); e.stopPropagation();
    });
    $('#bookSwitch').addEventListener('click', function (e) { var b = e.target.closest('[data-book]'); if (b) setBook(b.getAttribute('data-book')); });
    $('#btnSettings').onclick = function () { openSettings('display'); };
    $('#btnPrint').onclick = function () { openSettings('pdf'); };

    var vr = $('#view-read');
    vr.addEventListener('click', onReadClick);
    vr.addEventListener('change', onReadChange);
    vr.addEventListener('click', onMarkClick);
    document.addEventListener('mouseup', function () { setTimeout(onSelection, 10); });
    document.addEventListener('touchend', function () { setTimeout(onSelection, 250); });
    document.addEventListener('selectionchange', function () { var s = window.getSelection(); if (!s || s.isCollapsed) { $('#hlFloat').hidden = true; } });
    $('#hlFloat').addEventListener('mousedown', function (e) { e.preventDefault(); });
    $('#hlFloat').addEventListener('click', saveHighlight);

    $('#enPanel').addEventListener('click', onPanelClick);
    $('#enScrim').addEventListener('click', closeEnglish);
    $('#view-toc').addEventListener('click', onTocClick);
    $('#view-toc').addEventListener('input', onTocInput);
    $('#view-bookmarks').addEventListener('click', onListClick);
    $('#view-favourites').addEventListener('click', onListClick);
    $('#view-progress').addEventListener('click', onProgressClick);
    document.addEventListener('keydown', onKey);
    window.addEventListener('hashchange', function () { var id = location.hash.slice(1); if (INDEX[id]) openItem(id); });

    if (!Store.available()) toast('Browser storage is blocked — your notes and progress will not be saved.');

    var hashId = decodeURIComponent(location.hash.slice(1));
    if (INDEX[hashId]) openItem(hashId);
    else setTab(S.position.tab || 'read');
  }

  /* ---------------- Public API for other modules ---------------- */
  window.EIM = {
    get books() { return BOOKS; }, get index() { return INDEX; },
    store: Store, icon: icon, esc: esc, fmt: fmt, isTe: isTe, fmtDate: fmtDate, toast: toast, download: download,
    numLabel: numLabel, partLabel: partLabel, curBook: curBook, openItem: openItem, setTab: setTab,
    rebuild: rebuild, openDialog: openDialog, closeDialog: closeDialog, render: RENDER, updateTabCounts: updateTabCounts,
    currentQ: currentQ
  };
  document.addEventListener('DOMContentLoaded', init);
})();
