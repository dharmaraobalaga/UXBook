#!/usr/bin/env node
/* Rebuild data/ux-process.js from data/raw/ux-process.json (edit the JSON, then run: node tools/build-ux.js) */
'use strict';
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const parts = JSON.parse(fs.readFileSync(path.join(root, 'data/raw/ux-process.json'), 'utf8'));
const hdr = fs.readFileSync(path.join(root, 'data/ux-process.js'), 'utf8').split('window.BOOK_UX_PARTS')[0];
fs.writeFileSync(path.join(root, 'data/ux-process.js'), hdr + 'window.BOOK_UX_PARTS = ' + JSON.stringify(parts, null, 1) + ';\n');
console.log('UX Process: ' + parts.length + ' parts, ' + parts.reduce((n, p) => n + p.questions.length, 0) + ' items');
