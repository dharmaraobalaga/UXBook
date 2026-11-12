# Product/UX/UI Design Interview Mastery
### తెలుగులో నేర్చుకోండి. ఇంగ్లీష్‌లో ఆత్మవిశ్వాసంగా మాట్లాడండి.

A Telugu-first, interactive interview-preparation e-book for UX/UI, Product Design and design
leadership roles — by **Dharma Rao**. Plain HTML/CSS/JavaScript. No backend, no build step,
no paid services. Runs from a folder, from GitHub Pages, and offline.

---

## What's inside

| Area | What it does |
|---|---|
| **Three books** (switch top-right) | **UX Process** (NN/g UX deliverables guide: overview + 35 deliverables in the Interview Questions layout: Telugu first, English behind the button, Classic Rummy examples) · **Interview Questions** (all 57 parts, Q1–Q454, with examples) · **My Questions** (your own questions) |
| **Read Book** | Landscape two-page spread: question number, English question, Telugu question, **Telugu answer only**. Yellow key-point markers. Previous/Next page, Previous/Next question, page X of Y, jump-to-page, ← → keys |
| **View English Answer** | Hidden by default. Opens a right-side panel (bottom sheet on mobile) next to the Telugu answer — never replaces it. Read aloud, Hide & try yourself, Copy |
| **Practice Mode** | Settings → 4-step checklist per question; English stays blurred until you reveal it |
| **Highlights** | Select words in a Telugu answer → *Highlight*. Click a highlight to remove it (with Undo) |
| **Table of Contents** | All parts in order, question ranges, counts, progress, expandable question lists, filter box. Missing parts are shown honestly with an *Import* button |
| **Search** | Instant local search in English and తెలుగు across titles, questions, both answers, key points, vocabulary, speaking practice and your notes. Type `Q452` to jump by number. Press `/` anywhere |
| **Bookmarks / Favourites** | Two separate lists, one tap on each question |
| **My Notes (notebook)** | Save questions, write your own answers, examples/stories, vocabulary, questions to prepare. Custom categories. Edit/delete. Export Markdown or JSON |
| **My Questions** | Create your own important questions with Telugu + English answers — they get every feature above |
| **Reading Progress** | Overall %, questions & parts completed, per-book and per-part bars, continue reading, reading history |
| **PDF export** | Printer icon → A4 landscape, cover, contents, page numbers, part page breaks. Default Telugu only; tick *Include English answers* for side-by-side. Bundled Telugu fonts |
| **Backup & restore** | Settings → download/restore a JSON of all your data |

Keyboard: `←` `→` pages · `E` English answer · `B` bookmark · `F` favourite · `/` search · `Esc` close panel.

---

## Run it locally
Double-click `index.html`. That's it (data is loaded as `.js`, so it works from `file://`).

## Deploy on GitHub Pages
1. Create a repository (e.g. `interview-mastery`) and upload **the contents of this folder**
   (`index.html` must be at the repository root). Keep the empty `.nojekyll` file.
2. Repository → **Settings → Pages** → *Source*: **Deploy from a branch** → Branch **main**, folder **/ (root)** → Save.
3. After ~1 minute the book is live at `https://<your-username>.github.io/interview-mastery/`.

Using git:
```bash
cd interview-mastery
git init && git add . && git commit -m "Product/UX/UI Design Interview Mastery e-book"
git branch -M main
git remote add origin https://github.com/<your-username>/interview-mastery.git
git push -u origin main
```

> Personal data (bookmarks, notes, highlights, progress) is stored in each browser's
> localStorage — it is **not** uploaded to GitHub. Use *Backup* to move it between devices.

---

## Adding more parts (58, 59 …)

All 57 parts (Q1–Q454) are in the book — see `CONTENT-AUDIT.md`. Two ways to add new parts:

### A. In the app (no tools needed)
1. Settings ⚙ → **Import a Part**.
2. In ChatGPT, copy one whole part (from `Part N – Title` to the end of *Speaking Practice*) and paste it.
3. **Check content** → review the counts and any warnings → **Add Part N to the book**.
4. To publish it for every device: **Download updated data/parts.js** and replace `data/parts.js` in your repo.

### B. In the repository (best for many parts)
1. Save each part as a text file in `data/raw/`, named `part-01.txt` … `part-58.txt` (paste exactly as ChatGPT shows it).
2. Run: `node tools/build-data.js`
3. It regenerates `data/parts.js` and `data/content-audit.json`, and prints missing parts and any
   question with a missing Telugu/English answer. Commit and push.

The parser recognises this format (headings may start with `##`):

```
Part 58 – Leadership Interviews, Team Management & Design Leadership

Q455–Q462 | English Interview Preparation with Telugu Explanation

Q455. How do you lead a design team?
తెలుగు అర్థం: డిజైన్ టీమ్‌ను మీరు ఎలా నడిపిస్తారు?
తెలుగు సమాధానం:
…Telugu answer…
English Answer:
…English answer…

Q456. How do you mentor junior designers?
తెలుగు అర్థం: …
తెలుగు సమాధానం:
…
English Answer:
…

Quick Revision – Part 58
Question | Key points to remember
Q455. Leading a team | …

Important English Vocabulary
English | తెలుగు అర్థం
Mentor | …

Speaking Practice
- sentence one
- sentence two
```
A fill-in version is in `data/raw/TEMPLATE.txt` (the build script ignores it).

**Why nothing breaks when you add parts:** question IDs come from the question number
(`q-455`), so bookmarks, favourites, notes, highlights and progress stay attached. Page numbers,
contents, search and progress are all calculated from the data on load.

---

## Project structure
```
interview-mastery/
├── index.html               app shell (header, tabs, panel, dialogs)
├── css/styles.css           design system + screen layout (responsive)
├── css/print.css            A4-landscape PDF / print layout
├── js/parser.js             turns pasted ChatGPT text into structured parts (browser + Node)
├── js/storage.js            localStorage: bookmarks, favourites, notes, progress, settings, backup
├── js/app.js                books, navigation, reading view, English panel, highlights, TOC, progress, settings
├── js/search.js             local English + Telugu search
├── js/notebook.js           My Notebook + My Questions
├── js/pdf-export.js         builds the print layout and opens Save-as-PDF
├── data/parts.js            Interview Questions content (generated)
├── data/handbook.js         Interview Questions Parts 1–57, Q1–Q454 (generated)
├── data/ux-process.js       UX Process book (generated by tools/build-ux.js from data/raw/ux-process.json)
├── data/raw/handbook-q1-q88.txt, handbook-additions-*.json   handbook source + examples
├── data/raw/archive-removed-questions.txt   questions from the earlier handbook version that were replaced by your rewritten Parts 7–12
├── data/raw/archive-part-57-chatgpt-original.txt   the earlier Part 57 (from the ChatGPT link), replaced by your Part 57 PDF
├── data/content-audit.json  generated audit
├── tools/build-data.js      node tools/build-data.js → rebuilds data/parts.js
├── tools/build-handbook.js  node tools/build-handbook.js → rebuilds data/handbook.js
├── assets/fonts/            Noto Sans Telugu, Inter, Fraunces (SIL OFL)
├── assets/icon.svg, manifest.json, .nojekyll
├── CONTENT-AUDIT.md
└── README.md
```

## Data model
```js
Part     { partId, partNumber, title, subtitle, description, questionStart, questionEnd,
           questions[], revision[], vocabulary[], speakingPractice{intro, sentences[]}, nextPreview }
Question { questionId, questionNumber, questionEnglish, questionTelugu, answerTelugu, answerEnglish,
           note, importantMarkers[{type, label, text}], tags[] }
```
Marker types: `remember` (yellow highlighter), `tip`, `concept`, `mistake`, `speaking`.

## Interview Questions, Parts 1–51 (Q1–Q406)
These come from your **Product Design Interview Preparation Handbook**:
- `data/raw/handbook-q1-q88.txt` — the original text (English answers + Telugu explanations), kept verbatim.
- `data/raw/handbook-additions-a/b/c.json` — added by Claude: a Telugu translation of each question (`te`) and a practical
  example in English (`exEn`) and Telugu (`exTe`). Edit these to use your real project facts.
- Rebuild with `node tools/build-handbook.js` → regenerates `data/handbook.js`.

The Telugu example (ఉదాహరణ) appears on the left page under the question; the English example sits inside the English
answer panel, so it stays hidden until you choose to practise. IDs are `q-1` … `q-94`.

Note: importing a part with the same number (e.g. an original "Part 5") replaces that handbook part in the app.

## Adding the UX Process book
`data/ux-process.js` is empty and contains a commented example. Use the same Part / Question model and IDs `ux-1`, `ux-2` …

## Fonts & licence
Noto Sans Telugu, Inter and Fraunces are bundled under the SIL Open Font License (`assets/fonts/LICENSE-OFL.txt`).
Content © Dharma Rao.

### Adding a picture to a question
Put the image in `assets/images/`, then add an `img` entry for that question number in `data/raw/handbook-additions-*.json`:
`"img": { "src": "assets/images/your-file.jpg", "alt": "what the picture shows", "caption": "credit or title" }`
and rebuild with `node tools/build-handbook.js`. The picture appears under the Telugu answer and in PDF exports (see Q196).

### UX Process layout
The UX Process book uses the same page layout as Interview Questions. Each item has an English and a Telugu question (e.g. "What is an Affinity Diagram?" / "Affinity Diagram అంటే ఏమిటి?"). The Telugu answer (meaning, how to create it, interview line) and the Telugu example are shown first. **View English Answer** (or the E key) opens the English answer and example.

Every UX item (except Intro 1) has a diagram of its Classic Rummy example at the top of the answer page, with a Telugu and English caption. Click the picture to open it full size. The 37 diagrams are SVG files in `assets/images/ux/`, drawn by `tools/ux-figures/` (run `python3 tools/ux-figures/render.py figs_a figs_b figs_c` from that folder to redraw them). Bookmarks, favourites, notes, progress, search and PDF export work the same as in Interview Questions.
To edit: change `data/raw/ux-process.json`, then run `node tools/build-ux.js`.
