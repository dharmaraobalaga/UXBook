# D'Saras – Product/UX/UI Design Interview Mastery
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

### UX-Step by step (first tab)
A phased, step-by-step journey through one complete UX project. It follows Classic Rummy and ResolveAI through the 8 phases. It is not a Q&A book: each page is a **Step** (e.g. Step 1.7 – CSD Matrix) covering WHY / WHAT / WHEN / HOW, the deliverable (purpose, structure, creation), how it connects to the next step, senior-designer decisions and an Agile example. The Telugu explanation is shown first; **View English Explanation** opens the English version. Each phase ends with a knowledge check.

Added so far: Phase 0 (project setup) and Phase 1 – Discovery & Research (14 steps). Phases 2–8 will be added one at a time. Content: `tools/ux-steps/steps/*.py` → `python3 build_steps.py` (run from `tools/ux-steps` after copying `svgkit.py` and the `figs_*.py` files from `tools/ux-figures`) → `data/ux-steps.js`. Based on *End-to-End UX Design Lifecycle – Telugu + English Guide*, expanded by Claude; all numbers are illustrative.

### Vs
Difference questions laid out like the UX Process pages: Telugu answer first, with a **View English Answer** button that opens the English sidebar. Group 0 (0.1 User Flow vs User Journey, 0.2 Task Flow vs User Flow) comes from *Task_Flow_Vs_User_Journey.pdf*; 0.3 (Product Manager vs Product Designer vs UX Designer vs UI Designer) comes from *PM_vs_PD_vs_UX_vs_UI_Designer.pdf* (`tools/vs/vs/g0_roles.py`) – the PDF's English text is the English answer, the Telugu answer was written by Claude, and the two colourful role diagrams (`assets/images/vs/vs-roles-*.svg`, `tools/vs/figs_g0.py`) are Claude's own drawings because the PDF's images come from medium.com and behance.net. 0.4 (the four roles explained in detail) comes from *PM_PD_UX_UI_indetail_explanation.pdf*, which is Telugu-first: its Telugu text is the Telugu answer (`tools/vs/vs/detail_te.txt`, converted by `conv_detail.py`), the English answer is Claude's translation (`detail_en.txt`), and its role-formula, food-delivery journey and 10-phase process diagrams (`assets/images/vs/vs-roles-formula.svg`, `vs-food-journey.svg`, `vs-design-process-10.svg`) are Claude's own drawings; the PDF's 4-scenario assessment is on the Group 0 review page with an answer key. 0.5 (Assumptions, Hypothesis and How Might We questions by role) comes from *How_might_we.pdf* in the same way: Telugu text from the PDF (`tools/vs/vs/hmw_te.txt`, `conv_hmw.py`), English translation by Claude (`hmw_en.txt`), and Claude's own colourful diagrams (`assets/images/vs/vs-hmw-terms.svg`, `vs-hmw-four-lenses.svg`, `vs-hmw-process.svg`); the practical exercise has a sample answer, written by Claude, on the Group 0 review page. 0.6 (Funnels, Loops, AARRR, HEART, JTBD, Double Diamond, prioritisation and product metrics – where they fit and who uses them) comes from *Loops.pdf* the same way (`tools/vs/vs/loops_te.txt`, `conv_loops.py`, `loops_en.txt`); the PM/PD/UX/UI framework table was rebuilt from the PDF's column positions, and the frameworks map, funnel, referral loop, Double Diamond and 8-step diagrams (`assets/images/vs/vs-frameworks-map.svg`, `vs-food-funnel.svg`, `vs-referral-loop.svg`, `vs-double-diamond.svg`, `vs-e2e-8steps.svg`) are Claude's own drawings. 0.7 (how a Product Manager writes a PRD, with the Simplified Checkout example) comes from *PRD.pdf*: Telugu text from the PDF (`tools/vs/vs/prd_te.txt`, `conv_prd.py`); the English answer keeps the PDF's English text and adds Claude's translation of the Telugu lines (`prd_en_map.py` → `make_prd_en.py` → `prd_en.txt`); the document-types, 20-section structure, checkout-flow and PM-workflow diagrams (`assets/images/vs/vs-prd-*.svg`, `vs-checkout-flow.svg`) are Claude's own drawings. 0.8 (a practical PRD-review exercise: the PM's PRD draft for Classic Rummy first-time player onboarding, the eight review areas and Question 1) comes from *Example_PRD.pdf*, assembled by hand in `tools/vs/vs/g0_exprd.py` (PDF text kept; English translation of the Telugu lines, the review-areas diagram `assets/images/vs/vs-prd-review.svg` and the model answer to Question 1 on the Group 0 review page are by Claude). 0.9 (UX assumption questions – user & behaviour, usability & design, value & business, feasibility & edge cases – with Classic Rummy examples, the risk matrix and research planning) comes from *UX_Assumptions.pdf*: Telugu text from the PDF (`tools/vs/vs/uxas_te.txt`, `conv_uxas.py`); the English answer keeps the PDF's own English explanations and adds Claude's translation of the other Telugu lines (`uxas_en_map.py` → `make_uxas_en.py` → `uxas_en.txt`); the assumption-types, risk-matrix and research-steps diagrams (`assets/images/vs/vs-assumption-*.svg`) and the exercise model answer are by Claude. Group 1 – UX Research & Discovery (Q1–Q15) comes from *UX_Process_Comparisons.pdf*: its Telugu explanation, English definitions, table, example and interview answer are kept as in the PDF, and the Telugu table, Telugu example and Telugu meaning of the interview answer were added by Claude. Group 2 – UX Strategy & Design Thinking (Q16–Q25) comes from *Generate_UX_Vs_Questions-2.pdf* in the same way; its review page also lists the PDF's 5 interview-practice questions. Group 3 – Information Architecture & User Flows (Q26–Q40) comes from *Generate_UX_Vs_Questions-3.pdf*; its flow, sitemap and screen-flow diagrams are redrawn in `assets/images/vs/g3-*.svg`. Groups 4 – UX Deliverables & Documentation (Q41–Q55) and 5 – Interaction Design & Prototyping (Q56–Q75) come from *Generate_UX_Vs_Questions4.pdf*; images that were missing from the PDF (Q46, Q51, Q53, Q61) are drawn in `assets/images/vs/g4-*.svg` and `g5-*.svg`, and the Group 4 quick-revision lines were written by Claude because the PDF has none. Group 6 – Usability Testing & Evaluation (Q76–Q90) comes from *Generate_UX_Vs_Questions_6.pdf*. Group 7 – UI Design & Design Systems (Q91–Q105) comes from *Generate_UX_Vs_Questions_7.pdf*, which uses a different layout, so it is assembled by hand in `tools/vs/vs/g7_items.py` (PDF text kept; Claude's translations and the tables missing for Q97, Q99 and Q101 are marked there). Group 8 – Accessibility & Inclusive Design (Q106–Q115) comes from *Generate_UX_Vs_Questions_8.pdf* and is assembled the same way in `tools/vs/vs/g8_items.py`; Q110 (WCAG A vs AA vs AAA) uses a three-column table. Group 9 – Product Design & Development (Q116–Q130) comes from *Generate_UX_Vs_Questions_9.pdf* (`tools/vs/vs/g9_items.py`); its workflow, Prototype/MVP, Agile/Waterfall, Scrum/Kanban, Sprint/Design Thinking, Frontend/Backend and handoff diagrams are redrawn in `assets/images/vs/g9-*.svg` (`tools/vs/figs_g9.py`). Group 10 – UX Metrics & Analytics (Q131–Q142) comes from *Generate_UX_Vs_Questions_10.pdf* (`tools/vs/vs/g10_items.py`), with DAU/MAU, NPS, A/B, heatmap/recording and funnel diagrams in `assets/images/vs/g10-*.svg` (`tools/vs/figs_g10.py`); its review page ends with the PDF's closing pages (curriculum summary, 7-day revision plan, final advice), added through the module's `EXTRAS`. All 10 groups are now in; to add more, create a module like `g10_items.py`, continuing the numbering (`tools/vs/vs/te_gN.py` + `cmp_gN.txt`, then add the group to `GROUPS` in `vs_build.py`). The text follows *Task_Flow_Vs_User_Journey.pdf*, and its examples are shown as inline diagrams (`assets/images/vs/`). The English versions were translated by Claude. Inline diagrams use the answer syntax `!fig:src|alt|Telugu caption|English caption`. Rebuild with `python3 tools/vs/vs_build.py`.

### MockInt Guide (last tab)
*Senior / Lead / Principal Product Designer – Mock Interview Guide* (*Mock_Interview_Guide.pdf*): 50 questions in 8 sections, laid out like Interview Questions – Telugu answer first, **View English Answer** opens the English model answer. Kept from the PDF: the English model answers, the Telugu explanations (shown under "తెలుగు వివరణ · How to answer"), the Interview Tips (shown as tip markers), the intro, project list, interview structure, final checklist, practice guidance and portfolio order (Section 1 and Section 8 review pages). Added by Claude: the Telugu question titles, the Telugu answers (translations of the model answers) and English versions of the Telugu explanations. Question ids are `mk-1` … `mk-50`. Sources and builder: `tools/mock/` – edit `te_mock_a.py` / `te_mock_b.py`, then run `python3 tools/mock/build_mock.py` to regenerate `data/mock.js`.

### UX Process layout
The UX Process book uses the same page layout as Interview Questions. Each item has an English and a Telugu question (e.g. "What is an Affinity Diagram?" / "Affinity Diagram అంటే ఏమిటి?"). The Telugu answer (meaning, how to create it, interview line) and the Telugu example are shown first. **View English Answer** (or the E key) opens the English answer and example.

Every UX item (except Intro 1) has a diagram of its Classic Rummy example at the top of the answer page, with a Telugu and English caption. Click the picture to open it full size. The 37 diagrams are SVG files in `assets/images/ux/`, drawn by `tools/ux-figures/` (run `python3 tools/ux-figures/render.py figs_a figs_b figs_c` from that folder to redraw them). Bookmarks, favourites, notes, progress, search and PDF export work the same as in Interview Questions.
To edit: change `data/raw/ux-process.json`, then run `node tools/build-ux.js`.
