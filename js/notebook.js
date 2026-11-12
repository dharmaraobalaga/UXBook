/* ==========================================================================
   My Personal Notebook + My Questions
   - Notebook entries are separate from bookmarks and favourites.
   - Each entry can link to a question (qid) and keeps that reference.
   - Export to Markdown or JSON.
   - "My Questions": create your own important questions with Telugu and
     English answers; they become a full book (search, bookmarks, PDF…).
   ========================================================================== */
(function () {
  'use strict';
  var E = window.EIM;
  var TYPES = {
    saved: 'Saved question', note: 'Personal note', answer: 'My own answer',
    example: 'Example / story', vocab: 'Vocabulary to practise', prepare: 'Question to prepare'
  };
  var filterCat = 'all', filterType = 'all';
  function D() { return E.store.data; }
  function $(s, r) { return (r || document).querySelector(s); }

  /* ---------------- Note editor ---------------- */
  function catOptions(sel) {
    return D().categories.map(function (c) { return '<option' + (c === sel ? ' selected' : '') + '>' + E.esc(c) + '</option>'; }).join('') + '<option value="__new">+ New category…</option>';
  }
  function openNoteEditor(opts) {
    opts = opts || {};
    var existing = opts.id ? D().notes.filter(function (n) { return n.id === opts.id; })[0] : null;
    var qid = existing ? existing.qid : opts.qid;
    var e = qid && E.index[qid];
    var others = qid && !existing ? D().notes.filter(function (n) { return n.qid === qid; }) : [];
    var type = existing ? existing.type : (opts.type || (qid ? 'note' : 'note'));
    var h = '<button class="icon-btn modal-x" data-close aria-label="Close">' + E.icon('x') + '</button>' +
      '<h2>' + (existing ? 'Edit notebook entry' : 'Add to My Notebook') + '</h2>' +
      (e ? '<p class="muted" style="margin:4px 0 0">' + E.esc(E.numLabel(e.item)) + ' · ' + E.esc(E.partLabel(e.part)) + ' — ' + E.esc(e.item.questionEnglish) + '</p>' : '<p class="muted" style="margin:4px 0 0">A free note (not linked to a question).</p>') +
      (others.length ? '<p style="font-size:.86rem;margin:10px 0 0">This question already has ' + others.length + ' notebook entr' + (others.length === 1 ? 'y' : 'ies') + '. <a href="#" data-go-notes>View them</a></p>' : '') +
      '<h3>Entry</h3><div class="field-2"><div class="field"><label for="nType">Type</label><select id="nType">' +
      Object.keys(TYPES).filter(function (k) { return qid || k !== 'saved'; }).map(function (k) { return '<option value="' + k + '"' + (k === type ? ' selected' : '') + '>' + TYPES[k] + '</option>'; }).join('') + '</select></div>' +
      '<div class="field"><label for="nCat">Category</label><select id="nCat">' + catOptions(existing ? existing.category : (opts.category || 'General')) + '</select><input id="nCatNew" placeholder="New category name" hidden></div></div>' +
      '<div class="field"><label for="nTitle">Title' + (qid ? ' (optional)' : '') + '</label><input id="nTitle" value="' + E.esc(existing ? existing.title || '' : '') + '" placeholder="' + (qid ? 'e.g. My Classic Rummy story' : 'e.g. Questions to ask the interviewer') + '"></div>' +
      '<div class="field"><label for="nBody">Note</label><textarea id="nBody" placeholder="Write in English or తెలుగు — your own answer, an example, words to practise…">' + E.esc(existing ? existing.body || '' : '') + '</textarea></div>' +
      '<div class="modal-foot">' + (existing ? '<button class="btn danger" data-n="delete">' + E.icon('trash') + 'Delete</button><span class="spacer"></span>' : '') +
      '<button class="btn" data-close>Cancel</button><button class="btn primary" data-n="save">Save to notebook</button></div>';
    E.openDialog(h, function (ev) {
      var t = ev.target.closest('[data-n],[data-go-notes]'); if (!t) return;
      if (t.hasAttribute('data-go-notes')) { ev.preventDefault(); E.closeDialog(); filterCat = 'all'; E.setTab('notes'); return; }
      if (t.getAttribute('data-n') === 'delete') { E.closeDialog(); return deleteNote(existing.id); }
      var cat = $('#nCat').value === '__new' ? $('#nCatNew').value.trim() : $('#nCat').value;
      if (!cat) { $('#nCatNew').focus(); return E.toast('Enter a category name'); }
      if (D().categories.indexOf(cat) < 0) D().categories.push(cat);
      var tp = $('#nType').value, body = $('#nBody').value.trim(), title = $('#nTitle').value.trim();
      if (!body && tp !== 'saved' && !title) { $('#nBody').focus(); return E.toast('Write something first (or choose "Saved question")'); }
      if (existing) { existing.type = tp; existing.category = cat; existing.title = title; existing.body = body; existing.updated = Date.now(); }
      else D().notes.unshift({ id: E.store.uid('n'), qid: qid || null, type: tp, category: cat, title: title, body: body, created: Date.now(), updated: Date.now() });
      E.store.save(); E.closeDialog(); E.toast(existing ? 'Note updated' : 'Saved to My Notebook');
      E.updateTabCounts(); refresh();
    });
    $('#nCat').onchange = function () { var nw = this.value === '__new'; $('#nCatNew').hidden = !nw; if (nw) $('#nCatNew').focus(); };
    setTimeout(function () { $('#nBody').focus(); }, 40);
  }
  function deleteNote(id) {
    var list = D().notes, i = list.findIndex(function (n) { return n.id === id; }); if (i < 0) return;
    var removed = list.splice(i, 1)[0]; E.store.save(); refresh(); E.updateTabCounts();
    E.toast('Note deleted', 'Undo', function () { list.splice(i, 0, removed); E.store.save(); refresh(); E.updateTabCounts(); });
  }
  function refresh() {
    var tab = D().position.tab;
    if (tab === 'notes') render(); else if (tab === 'read') E.render.read({});
  }

  /* ---------------- Categories ---------------- */
  function manageCategories() {
    var h = '<button class="icon-btn modal-x" data-close aria-label="Close">' + E.icon('x') + '</button><h2>Notebook categories</h2>' +
      '<p class="muted" style="font-size:.9rem">Rename or remove categories. Notes in a removed category move to “General”.</p><div style="display:grid;gap:8px;margin:14px 0">' +
      D().categories.map(function (c, i) {
        return '<div class="row"><input class="input" style="flex:1" data-cat-i="' + i + '" value="' + E.esc(c) + '">' + (c === 'General' ? '' : '<button class="btn sm ghost danger" data-cat-del="' + i + '">' + E.icon('trash') + '</button>') + '</div>';
      }).join('') + '</div><div class="row"><input class="input" id="catNew" placeholder="New category" style="flex:1"><button class="btn" data-cat-add>' + E.icon('plus') + 'Add</button></div>' +
      '<div class="modal-foot"><button class="btn primary" data-cat-save>Done</button></div>';
    E.openDialog(h, function (ev) {
      var t = ev.target.closest('[data-cat-del],[data-cat-add],[data-cat-save]'); if (!t) return;
      saveRenames();
      if (t.hasAttribute('data-cat-del')) {
        var c = D().categories.splice(+t.getAttribute('data-cat-del'), 1)[0];
        D().notes.forEach(function (n) { if (n.category === c) n.category = 'General'; });
        E.store.save(); return manageCategories();
      }
      if (t.hasAttribute('data-cat-add')) {
        var v = $('#catNew').value.trim(); if (v && D().categories.indexOf(v) < 0) D().categories.push(v);
        E.store.save(); return manageCategories();
      }
      E.store.save(); E.closeDialog(); render();
    });
  }
  function saveRenames() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-cat-i]'), function (inp) {
      var i = +inp.getAttribute('data-cat-i'), old = D().categories[i], nw = inp.value.trim();
      if (nw && nw !== old && D().categories.indexOf(nw) < 0) {
        D().categories[i] = nw;
        D().notes.forEach(function (n) { if (n.category === old) n.category = nw; });
      }
    });
  }

  /* ---------------- Notes view ---------------- */
  function noteCard(n) {
    var e = n.qid && E.index[n.qid];
    return '<article class="note" id="note-' + E.esc(n.id) + '"><div class="note-top"><span class="badge ' + E.esc(n.type) + '">' + E.esc(TYPES[n.type] || n.type) + '</span><span>' + E.esc(n.category) + '</span><span>· ' + E.fmtDate(n.updated || n.created) + '</span></div>' +
      (n.title ? '<p class="note-title">' + E.esc(n.title) + '</p>' : '') +
      (e ? '<button class="note-link" data-open="' + E.esc(n.qid) + '">' + E.esc(E.numLabel(e.item)) + ' · ' + E.esc(e.item.questionEnglish) + ' <span class="muted">(' + E.esc(E.partLabel(e.part)) + ')</span></button>' + (n.type === 'saved' && e.item.questionTelugu ? '<p class="qc-te" lang="te" style="margin:4px 0 0">' + E.esc(e.item.questionTelugu) + '</p>' : '')
        : (n.qid ? '<span class="muted" style="font-size:.86rem">Linked question ' + E.esc(n.qid) + ' is not in the book right now</span>' : '')) +
      (n.body ? '<p class="note-body">' + E.esc(n.body) + '</p>' : '') +
      '<div class="note-foot"><button class="btn sm ghost" data-edit="' + E.esc(n.id) + '">' + E.icon('edit') + 'Edit</button><button class="btn sm ghost danger" data-del="' + E.esc(n.id) + '">' + E.icon('trash') + 'Delete</button></div></article>';
  }
  function render() {
    var notes = D().notes, cats = D().categories.slice();
    notes.forEach(function (n) { if (cats.indexOf(n.category) < 0) cats.push(n.category); });
    var shown = notes.filter(function (n) { return (filterCat === 'all' || n.category === filterCat) && (filterType === 'all' || n.type === filterType); });
    var count = function (c) { return notes.filter(function (n) { return n.category === c; }).length; };
    var h = '<div class="view-head"><div><h2 class="view-title">My Notebook</h2><p class="view-sub">Your saved questions, own answers, examples and vocabulary · ' + notes.length + ' entries</p></div>' +
      '<div class="row"><button class="btn primary" data-act="new">' + E.icon('plus') + 'New note</button><button class="btn" data-act="my-q">' + E.icon('pen') + 'Create my own question</button>' +
      '<button class="btn" data-act="md">' + E.icon('download') + 'Markdown</button><button class="btn" data-act="json">' + E.icon('download') + 'JSON</button></div></div>' +
      '<div class="notes-layout"><nav class="cat-list" aria-label="Categories">' +
      '<button data-cat="all" aria-pressed="' + (filterCat === 'all') + '">All entries <span class="n">' + notes.length + '</span></button><hr>' +
      cats.map(function (c) { return '<button data-cat="' + E.esc(c) + '" aria-pressed="' + (filterCat === c) + '">' + E.esc(c) + ' <span class="n">' + count(c) + '</span></button>'; }).join('') +
      '<hr><button data-act="cats">' + E.icon('gear') + ' Manage categories</button></nav><div>' +
      '<div class="search-filters">' + [['all', 'All types']].concat(Object.keys(TYPES).map(function (k) { return [k, TYPES[k]]; })).map(function (t) { return '<button class="chip" data-type="' + t[0] + '" aria-pressed="' + (filterType === t[0]) + '">' + t[1] + '</button>'; }).join('') + '</div>' +
      (shown.length ? '<div class="card-list">' + shown.map(noteCard).join('') + '</div>'
        : '<div class="empty">' + E.icon('note') + '<h3>' + (notes.length ? 'No entries match this filter' : 'Your notebook is empty') + '</h3><p>On any question page, use <b>Add to Notebook</b> to save the question, write your own answer, add an example or record vocabulary. Or start a free note here.</p></div>') +
      '</div></div>';
    document.getElementById('view-notes').innerHTML = h;
    if (E.focusNote) { var el = document.getElementById('note-' + E.focusNote); E.focusNote = null; if (el) { el.scrollIntoView({ block: 'center' }); el.style.outline = '2px solid var(--indigo)'; } }
  }

  function exportMarkdown() {
    var by = {};
    D().notes.forEach(function (n) { (by[n.category] = by[n.category] || []).push(n); });
    var md = '# My Personal Notebook — D\'Saras – Product/UX/UI Design Interview Mastery\n\n_Exported ' + new Date().toLocaleString() + '_\n';
    Object.keys(by).forEach(function (c) {
      md += '\n## ' + c + '\n';
      by[c].forEach(function (n) {
        var e = n.qid && E.index[n.qid];
        md += '\n### ' + (n.title || (e ? E.numLabel(e.item) + '. ' + e.item.questionEnglish : TYPES[n.type])) + '\n\n';
        md += '- **Type:** ' + (TYPES[n.type] || n.type) + '\n';
        if (e) md += '- **Question:** ' + E.numLabel(e.item) + ' (' + E.partLabel(e.part) + ' — ' + e.part.title + ')\n' + (e.item.questionTelugu ? '- **తెలుగు:** ' + e.item.questionTelugu + '\n' : '');
        else if (n.qid) md += '- **Question ID:** ' + n.qid + '\n';
        md += '- **Updated:** ' + new Date(n.updated || n.created).toLocaleDateString() + '\n';
        if (n.body) md += '\n' + n.body + '\n';
      });
    });
    if (D().myQuestions.length) {
      md += '\n## My Questions\n';
      D().myQuestions.forEach(function (q) {
        md += '\n### ' + q.questionEnglish + '\n\n' + (q.questionTelugu ? '**తెలుగు అర్థం:** ' + q.questionTelugu + '\n\n' : '') +
          (q.answerTelugu ? '**తెలుగు సమాధానం:**\n\n' + q.answerTelugu + '\n\n' : '') + (q.answerEnglish ? '**English Answer:**\n\n' + q.answerEnglish + '\n' : '');
      });
    }
    E.download('my-notebook-' + new Date().toISOString().slice(0, 10) + '.md', md, 'text/markdown;charset=utf-8');
  }
  function exportJSON() {
    E.download('my-notebook-' + new Date().toISOString().slice(0, 10) + '.json', JSON.stringify({ categories: D().categories, notes: D().notes, myQuestions: D().myQuestions }, null, 2), 'application/json');
  }

  /* ---------------- My Questions ---------------- */
  function openMyQuestionEditor(id) {
    var q = id ? D().myQuestions.filter(function (x) { return x.id === id; })[0] : null;
    var cats = [];
    D().myQuestions.forEach(function (x) { if (cats.indexOf(x.category) < 0) cats.push(x.category); });
    var h = '<button class="icon-btn modal-x" data-close aria-label="Close">' + E.icon('x') + '</button>' +
      '<h2>' + (q ? 'Edit my question' : 'Create my own question') + '</h2><p class="muted" style="margin:4px 0 0">It appears in the “My Questions” book with the same Telugu-first layout.</p>' +
      '<div class="field" style="margin-top:16px"><label for="mCat">Category (becomes a section of the book)</label><input id="mCat" list="mCats" value="' + E.esc(q ? q.category : (cats[0] || 'My Important Questions')) + '"><datalist id="mCats">' + cats.map(function (c) { return '<option value="' + E.esc(c) + '">'; }).join('') + '</datalist></div>' +
      '<div class="field"><label for="mQEn">Question in English *</label><input id="mQEn" value="' + E.esc(q ? q.questionEnglish : '') + '" placeholder="e.g. Walk me through your Classic Rummy case study."></div>' +
      '<div class="field"><label for="mQTe">తెలుగు అర్థం (Telugu question)</label><input id="mQTe" lang="te" value="' + E.esc(q ? q.questionTelugu : '') + '"></div>' +
      '<div class="field"><label for="mATe">తెలుగు సమాధానం (Telugu answer)</label><textarea id="mATe" lang="te">' + E.esc(q ? q.answerTelugu : '') + '</textarea></div>' +
      '<div class="field"><label for="mAEn">English answer (hidden until “View English Answer”)</label><textarea id="mAEn">' + E.esc(q ? q.answerEnglish : '') + '</textarea></div>' +
      '<div class="field"><label for="mKey">Key points to remember (optional, shown as a yellow marker)</label><input id="mKey" value="' + E.esc(q ? q.keyPoints || '' : '') + '"></div>' +
      '<p class="muted" style="font-size:.82rem">Tip: leave a blank line between paragraphs. Start a line with “- ” for a bullet list.</p>' +
      '<div class="modal-foot"><button class="btn" data-close>Cancel</button><button class="btn primary" data-m="save">' + (q ? 'Save changes' : 'Add question') + '</button></div>';
    E.openDialog(h, function (ev) {
      if (!ev.target.closest('[data-m="save"]')) return;
      var en = $('#mQEn').value.trim(); if (!en) { $('#mQEn').focus(); return E.toast('The English question is required'); }
      var rec = q || { id: E.store.uid('my'), created: Date.now() };
      rec.category = $('#mCat').value.trim() || 'My Important Questions';
      rec.questionEnglish = en; rec.questionTelugu = $('#mQTe').value.trim();
      rec.answerTelugu = $('#mATe').value.trim(); rec.answerEnglish = $('#mAEn').value.trim();
      rec.keyPoints = $('#mKey').value.trim(); rec.updated = Date.now();
      if (!q) D().myQuestions.push(rec);
      E.store.save(); E.closeDialog(); E.rebuild();
      E.toast(q ? 'Question updated' : 'Question added to My Questions');
      E.openItem(rec.id);
    });
    setTimeout(function () { $('#mQEn').focus(); }, 40);
  }
  function deleteMyQuestion(id) {
    var list = D().myQuestions, i = list.findIndex(function (x) { return x.id === id; }); if (i < 0) return;
    var removed = list.splice(i, 1)[0]; E.store.save(); E.rebuild();
    E.toast('Question deleted', 'Undo', function () { list.splice(i, 0, removed); E.store.save(); E.rebuild(); E.openItem(id); });
  }

  /* ---------------- events ---------------- */
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('view-notes').addEventListener('click', function (ev) {
      var t = ev.target.closest('[data-cat],[data-type],[data-act],[data-open],[data-edit],[data-del]'); if (!t) return;
      if (t.hasAttribute('data-cat')) { filterCat = t.getAttribute('data-cat'); return render(); }
      if (t.hasAttribute('data-type')) { filterType = t.getAttribute('data-type'); return render(); }
      if (t.hasAttribute('data-open')) return E.openItem(t.getAttribute('data-open'));
      if (t.hasAttribute('data-edit')) return openNoteEditor({ id: t.getAttribute('data-edit') });
      if (t.hasAttribute('data-del')) return deleteNote(t.getAttribute('data-del'));
      var a = t.getAttribute('data-act');
      if (a === 'new') openNoteEditor({ category: filterCat !== 'all' ? filterCat : 'General' });
      else if (a === 'my-q') openMyQuestionEditor();
      else if (a === 'md') exportMarkdown();
      else if (a === 'json') exportJSON();
      else if (a === 'cats') manageCategories();
    });
  });

  E.render.notes = render;
  E.openNoteEditor = openNoteEditor;
  E.openMyQuestionEditor = openMyQuestionEditor;
  E.deleteMyQuestion = deleteMyQuestion;
  E.noteTypes = TYPES;
})();
