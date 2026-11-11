/* ==========================================================================
   Storage — all personal data lives in localStorage under one key.
   Everything is keyed by stable question IDs ("q-447", "ux-5", "my-…"),
   so adding new parts never breaks bookmarks, notes or progress.
   ========================================================================== */
(function () {
  'use strict';
  var KEY = 'eim.userdata.v1';

  function defaults() {
    return {
      version: 1,
      bookmarks: {},        // id -> timestamp
      favourites: {},       // id -> timestamp
      completed: {},        // id -> timestamp
      highlights: {},       // id -> [selected text, …]
      practice: {},         // id -> [step1, step2, step3, step4] booleans
      notes: [],            // notebook entries
      categories: ['General', 'Must Prepare', 'My Stories (STAR)', 'Vocabulary'],
      myQuestions: [],      // user-created questions
      importedParts: [],    // parts pasted in through "Import a Part"
      position: { book: 'ux', page: { iq: 0, ux: 0, my: 0 }, tab: 'read' },
      history: [],          // [{id, ts}] most recent first
      settings: { fontScale: 1, theme: 'paper', practiceMode: false, pdfEnglish: false }
    };
  }

  function merge(base, saved) {
    Object.keys(saved || {}).forEach(function (k) {
      if (base[k] && typeof base[k] === 'object' && !Array.isArray(base[k]) && saved[k] && typeof saved[k] === 'object' && !Array.isArray(saved[k])) {
        base[k] = merge(base[k], saved[k]);
      } else base[k] = saved[k];
    });
    return base;
  }

  var data = defaults(), available = true;
  try {
    var raw = localStorage.getItem(KEY);
    if (raw) data = merge(defaults(), JSON.parse(raw));
  } catch (e) { available = false; }

  var Store = {
    get data() { return data; },
    available: function () { return available; },
    save: function () {
      try { localStorage.setItem(KEY, JSON.stringify(data)); return true; }
      catch (e) { available = false; return false; }
    },
    toggle: function (setName, id) {
      var s = data[setName];
      if (s[id]) delete s[id]; else s[id] = Date.now();
      Store.save();
      return !!s[id];
    },
    has: function (setName, id) { return !!data[setName][id]; },
    visit: function (id) {
      data.history = data.history.filter(function (h) { return h.id !== id; });
      data.history.unshift({ id: id, ts: Date.now() });
      if (data.history.length > 60) data.history.length = 60;
      Store.save();
    },
    exportJSON: function () {
      return JSON.stringify({ app: 'english-interview-mastery', exportedAt: new Date().toISOString(), data: data }, null, 2);
    },
    importJSON: function (text) {
      var parsed = JSON.parse(text);
      var incoming = parsed && parsed.data ? parsed.data : parsed;
      if (!incoming || typeof incoming !== 'object' || !('bookmarks' in incoming)) throw new Error('This file is not an Product/UX/UI Design Interview Mastery backup.');
      data = merge(defaults(), incoming);
      Store.save();
    },
    reset: function () { data = defaults(); Store.save(); },
    uid: function (prefix) { return (prefix || 'id') + '-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }
  };

  window.EIMStore = Store;
})();
