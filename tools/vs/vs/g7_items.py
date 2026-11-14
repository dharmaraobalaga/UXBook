# Group 7 – UI Design & Design Systems (Q91–Q105), assembled from Generate_UX_Vs_Questions_7.pdf.
# te / iv_en / English "def" lines from the PDF = PDF text. Items marked # Claude: written/translated by Claude.
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

ITEMS = [
dict(n=91, A='UI Design', B='UX Design', q_te='UI Design మరియు UX Design మధ్య తేడా ఏమిటి?',
 te='''UX Design (User Experience Design):

ఒక ప్రొడక్ట్‌ను ఉపయోగించేటప్పుడు యూజర్‌కు కలిగే మొత్తం అనుభవాన్ని డిజైన్ చేయడం.

UI Design (User Interface Design):

యూజర్ ప్రొడక్ట్‌తో ఇంటరాక్ట్ అయ్యే స్క్రీన్లు, బటన్లు, కలర్స్, టైపోగ్రఫీ, విజువల్ ఎలిమెంట్స్‌ను డిజైన్ చేయడం.''',
 defs=['UX Design: UX Design focuses on the overall user experience, including usability, accessibility, user flows, and problem-solving.',
       'UI Design: UI Design focuses on the visual and interactive elements of a digital product.'],
 hdr=['UX Design', 'UI Design'],
 rows=[['User experience', 'Visual interface'], ['Research & usability', 'Colors & typography'], ['User journeys & flows', 'Buttons & components'], ['Information architecture', 'Visual consistency'], ['How it works and feels', 'How it looks and responds']],
 tbl_te=[['User అనుభవం','Visual interface'],['Research మరియు usability','రంగులు మరియు typography'],['User journeys మరియు flows','Buttons మరియు components'],['Information architecture','Visual consistency'],['ఎలా పనిచేస్తుంది, ఎలా అనిపిస్తుంది','ఎలా కనిపిస్తుంది, ఎలా స్పందిస్తుంది']],
 ex_title='Banking App',
 ex_te='''- UX Designer: యూజర్ డబ్బులు ఎలా ట్రాన్స్‌ఫర్ చేయాలి? ఎన్ని స్టెప్స్ ఉండాలి? ఎక్కడ కన్ఫ్యూజన్ వస్తుంది?
- UI Designer: Transfer button ఎలా ఉండాలి? Color, typography, spacing, icons ఎలా ఉండాలి?

గుర్తుంచుకోండి: UX – Structure & flow · UI – Visual interface.''',
 ex_en='''- UX Designer: How should the user transfer money? How many steps should there be? Where does confusion occur?
- UI Designer: How should the Transfer button look? What colour, typography, spacing and icons should it use?

Remember: UX – structure & flow · UI – visual interface.''',
 iv_en='"UX Design focuses on creating meaningful, usable, and accessible experiences, while UI Design focuses on the visual and interactive presentation of those experiences. Both disciplines work together to create successful digital products."',
 iv_te='UX అర్థవంతమైన, ఉపయోగకరమైన అనుభవాన్ని సృష్టిస్తుంది; UI ఆ అనుభవాన్ని దృశ్యంగా, interactive గా అందిస్తుంది – రెండూ కలిసి పనిచేస్తాయి.'),

dict(n=92, A='Design System', B='Style Guide', q_te='Design System మరియు Style Guide మధ్య తేడా ఏమిటి?',
 te='''Design System:

ఒక ప్రొడక్ట్ లేదా సంస్థలో consistent digital experiences తయారు చేయడానికి ఉపయోగించే components, patterns, tokens, guidelines, documentation, governance కలిగిన వ్యవస్థ.

Style Guide:

ఒక బ్రాండ్ లేదా ప్రొడక్ట్ యొక్క visual appearance ఎలా ఉండాలో చెప్పే నియమాలు.''',
 defs=['Design System: A Design System is a structured collection of reusable components, design foundations, patterns, and guidelines.',
       'Style Guide: A Style Guide defines visual standards such as colors, typography, logos, and spacing.'],
 hdr=['Design System', 'Style Guide'],
 rows=[['Broader system', 'Visual rules'], ['Components & patterns', 'Colors & fonts'], ['Design tokens', 'Brand guidelines'], ['Documentation & governance', 'Visual consistency'], ['Design–development alignment', 'Appearance alignment']],
 tbl_te=[['విస్తృతమైన వ్యవస్థ','Visual నియమాలు'],['Components మరియు patterns','రంగులు మరియు fonts'],['Design tokens','Brand guidelines'],['Documentation మరియు governance','Visual consistency'],['Design–development సమన్వయం','రూపం (appearance) సమన్వయం']],
 ex_title="D'SARAS Website",
 ex_te='''D’SARAS వెబ్‌సైట్ కోసం colors, typography, logo usage మాత్రమే document చేస్తే అది Style Guide.

అదే reusable buttons, navigation, forms, tokens, responsive patterns, usage rules, code alignment కలిపితే Design System.''',
 ex_en='''If only the colours, typography and logo usage are documented for the D'SARAS website, that is a Style Guide.

If reusable buttons, navigation, forms, tokens, responsive patterns, usage rules and code alignment are added, it becomes a Design System.''',
 iv_en='"A Style Guide defines the visual language of a product, whereas a Design System provides a comprehensive framework of reusable components, patterns, tokens, and guidelines to ensure consistency and scalability."',
 iv_te='Style Guide visual భాషను నిర్ణయిస్తుంది; Design System consistency మరియు scalability కోసం పూర్తి framework ఇస్తుంది.'),

dict(n=93, A='Design System', B='Component Library', q_te='Design System మరియు Component Library మధ్య తేడా ఏమిటి?',
 te='''Design System:

Components‌తో పాటు principles, patterns, tokens, accessibility standards, documentation, governance కలిగి ఉంటుంది.

Component Library:

Reusable UI components యొక్క collection.''',
 defs=['Design System: Includes components plus principles, patterns, tokens, accessibility standards, documentation and governance.',  # Claude
       'Component Library: A collection of reusable UI components.'],  # Claude
 hdr=['Design System', 'Component Library'],
 rows=[['Complete framework', 'Reusable UI elements'], ['Includes design principles', 'Buttons, cards, inputs'], ['Guidelines & governance', 'Component states'], ['Supports scalability', 'Supports implementation']],
 tbl_te=[['పూర్తి framework','Reusable UI elements'],['Design principles ఉంటాయి','Buttons, cards, inputs'],['Guidelines మరియు governance','Component states'],['Scalability కి సహాయం','Implementation కి సహాయం']],
 ex_title='Material Design',
 ex_te='Material Design ఒక Design System. దాని Material UI component implementations అనేవి component libraries.',
 ex_en='Material Design is a Design System. Its Material UI component implementations are component libraries.',
 iv_en='"A Component Library is one part of a Design System. A Design System additionally defines design principles, usage guidelines, accessibility standards, and governance."',
 iv_te='Component Library అనేది Design System లో ఒక భాగం మాత్రమే.'),

dict(n=94, A='Component', B='Pattern', q_te='Component మరియు Pattern మధ్య తేడా ఏమిటి?',
 te='''Component:

ఒక నిర్దిష్ట UI functionality అందించే reusable building block.
ఉదాహరణలు: Button, Checkbox, Text Field, Modal.

Pattern:

ఒక common user problem‌ను పరిష్కరించడానికి ఉపయోగించే repeatable design solution. ఇందులో అనేక components ఉండవచ్చు.
ఉదాహరణలు: Login Flow, Search & Filter, Checkout, Multi-step Form.''',
 defs=['Component: A reusable building block that provides a specific UI function – e.g. Button, Checkbox, Text Field, Modal.',  # Claude
       'Pattern: A repeatable design solution to a common user problem, which can contain several components – e.g. Login Flow, Search & Filter, Checkout, Multi-step Form.'],  # Claude
 hdr=['Component', 'Pattern'],
 rows=[['UI building block', 'Reusable solution'], ['Usually smaller scope', 'Often broader scope'], ['Button, input, card', 'Checkout, authentication'], ['Implementation-focused', 'Interaction-focused']],
 tbl_te=[['UI building block','మళ్లీ ఉపయోగించగల పరిష్కారం'],['సాధారణంగా చిన్న పరిధి','తరచుగా విస్తృత పరిధి'],['Button, input, card','Checkout, authentication'],['Implementation పై దృష్టి','Interaction పై దృష్టి']],
 ex_title='E-commerce',
 ex_te='''- Search Input = Component.
- Search + Suggestions + Filters + Results + Empty State = Search Pattern.''',
 ex_en='''- Search Input = Component.
- Search + Suggestions + Filters + Results + Empty State = Search Pattern.''',
 iv_en='"A Component is a reusable interface element, while a Pattern is a repeatable solution to a common user interaction problem, often combining multiple components."',
 iv_te='Component ఒక element; Pattern అనేక components కలిపి ఒక సాధారణ సమస్యకు ఇచ్చే పరిష్కారం.'),

dict(n=95, A='Component', B='Variant', q_te='Component మరియు Variant మధ్య తేడా ఏమిటి?',
 te='''Component:

ఒక reusable UI element యొక్క base definition.

Variant:

అదే component‌కు చెందిన different versions లేదా properties ఆధారంగా మారే రూపాలు.''',
 defs=['Component: The base definition of a reusable UI element.',  # Claude
       'Variant: Different versions of the same component that change based on its properties.'],  # Claude
 hdr=['Component', 'Variant'],
 rows=[['Base reusable element', 'Version of that element'], ['Button', 'Primary, Secondary'], ['Input Field', 'Default, Error, Success'], ['Card', 'Compact, Expanded']],
 tbl_te=[['మూల (base) reusable element','ఆ element యొక్క version'],['Button','Primary, Secondary'],['Input Field','Default, Error, Success'],['Card','Compact, Expanded']],
 ex_title='Figma',
 ex_te=fig('g7-button-variants', 'Button component with Primary, Secondary and Disabled variants', 'Button component – సాధారణ variants. నిజమైన component లో states మరియు interaction ప్రవర్తన కూడా ఉంటాయి.', 'Illustrative button variants; a real component also defines states and interaction behaviour.') +
       '\n\nFigma ఉదాహరణ: Button Component Set → Properties: Type, Size, State.',
 ex_en=fig('g7-button-variants', 'Button component with variants', '', 'Illustrative button variants; a real component also defines states and interaction behavior.') +
       '\n\nFigma Example: Button Component Set → Properties: Type, Size, State.',
 iv_en='"A Component defines a reusable UI element, while Variants represent different configurations of that component, helping designers manage consistency and reduce duplication."',
 iv_te='Variants ఒకే component యొక్క వేర్వేరు రూపాలను ఒకే చోట నిర్వహించి, duplication తగ్గిస్తాయి.'),

dict(n=96, A='Design Tokens', B='Design Variables', q_te='Design Tokens మరియు Design Variables మధ్య తేడా ఏమిటి?',
 te='''Design Tokens:

Design decisions‌ను meaningful names‌తో represent చేసే reusable values.

ఉదాహరణలు:
- color.primary = #2563EB
- spacing.md = 16px
- radius.card = 12px

Design Variables:

Figma వంటి tools‌లో values‌ను store చేసి, reuse చేసి, modes ద్వారా manage చేయడానికి ఉపయోగించే features.''',
 defs=['Design Tokens: Reusable values that represent design decisions with meaningful names – e.g. color.primary = #2563EB, spacing.md = 16px, radius.card = 12px.',  # Claude
       'Design Variables: Features in tools such as Figma used to store, reuse and manage values through modes.'],  # Claude
 hdr=['Design Tokens', 'Design Variables'],
 rows=[['Named design decisions', 'Tool-managed values'], ['Tool-independent concept', 'Tool-specific implementation'], ['Can be exported to code', 'Can support modes'], ['Supports cross-platform systems', 'Supports design workflows']],
 tbl_te=[['పేరు పెట్టిన design నిర్ణయాలు','Tool నిర్వహించే values'],['Tool తో సంబంధం లేని concept','Tool కు ప్రత్యేకమైన implementation'],['Code లోకి export చేయవచ్చు','Modes కు మద్దతు ఇవ్వగలదు'],['Cross-platform systems కు సహాయం','Design workflows కు సహాయం']],
 ex_title='Light & Dark Mode',
 ex_te='color.background.primary అనే token‌ను Figma Variable‌తో link చేయవచ్చు. Light Mode, Dark Mode‌లో వేర్వేరు values ఇవ్వవచ్చు.',
 ex_en='A token named color.background.primary can be linked to a Figma Variable, with different values in Light Mode and Dark Mode.',
 iv_en='"Design Tokens represent named design decisions, while Design Variables are mechanisms used by design tools to store, reference, and manage values. Variables can implement tokens, but the two concepts are not identical."',
 iv_te='Variables tokens ను అమలు చేయగలవు, కానీ రెండూ ఒకటే కాదు.'),

dict(n=97, A='Atomic Design', B='Design System', q_te='Atomic Design మరియు Design System మధ్య తేడా ఏమిటి?',
 te='''Atomic Design:

UI‌ను చిన్న building blocks నుంచి పెద్ద structures వరకు organize చేసే methodology.

Brad Frost పరిచయం చేసిన Atomic Design methodologyలో ఐదు levels ఉన్నాయి:
1. Atoms — Buttons, Labels, Inputs
2. Molecules — Search Form
3. Organisms — Website Header
4. Templates — Page Structure
5. Pages — Real Content & States

Design System:

Reusable UI, design principles, standards, documentation, governance అన్నింటినీ నిర్వహించే framework.''',
 defs=['Atomic Design: A methodology, introduced by Brad Frost, that organises UI from small building blocks into larger structures across five levels – Atoms, Molecules, Organisms, Templates and Pages.',  # Claude
       'Design System: A framework that manages reusable UI, design principles, standards, documentation and governance.'],  # Claude
 hdr=['Atomic Design', 'Design System'],  # Claude: the PDF has no table for Q97
 rows=[['A methodology', 'A complete framework'], ['Organises UI into five levels', 'Covers components, principles, standards'], ['Guides how to structure components', 'Guides how to create, maintain and govern'], ['Can be used to build a design system', 'Can use Atomic Design as its structure']],
 tbl_te=[['ఒక పద్ధతి (methodology)','పూర్తి framework'],['UI ని ఐదు స్థాయిలుగా క్రమబద్ధం చేస్తుంది','Components, principles, standards అన్నీ'],['Components ను ఎలా నిర్మించాలో చెబుతుంది','ఎలా సృష్టించాలి, నిర్వహించాలి, govern చేయాలో చెబుతుంది'],['Design system నిర్మించడానికి ఉపయోగించవచ్చు','Atomic Design ను తన నిర్మాణంగా ఉపయోగించవచ్చు']],
 ex_title='Atomic levels',
 ex_te=fig('g7-atomic', 'Five Atomic Design levels from atoms to pages', 'Atoms → Molecules → Organisms → Templates → Pages.', 'Atoms → Molecules → Organisms → Templates → Pages.'),
 ex_en=fig('g7-atomic', 'Five Atomic Design levels', '', 'Atoms → Molecules → Organisms → Templates → Pages.'),
 iv_en='"Atomic Design is a methodology for structuring interfaces into hierarchical building blocks. A Design System is a broader framework for creating, maintaining, and governing consistent product experiences."',
 iv_te='Atomic Design ఒక methodology; Design System దాని కంటే విస్తృతమైన framework.'),

dict(n=98, A='Typography', B='Font', q_te='Typography మరియు Font మధ్య తేడా ఏమిటి?',
 te='''Typography:

Text‌ను readable, accessible, visually organized విధంగా arrange చేసే design discipline.

Font:

ఒక typeface యొక్క specific style, weight, size లేదా implementation.''',
 defs=['Typography: The design discipline of arranging text so it is readable, accessible and visually organised.',  # Claude
       'Font: A specific style, weight, size or implementation of a typeface.'],  # Claude
 hdr=['Typography', 'Font'],
 rows=[['Complete text design discipline', 'Specific text style/resource'], ['Hierarchy', 'Typeface, weight, style'], ['Line height & spacing', 'Font selection'], ['Readability & legibility', 'Character appearance']],
 tbl_te=[['పూర్తి text design విభాగం','నిర్దిష్ట text style / resource'],['Hierarchy','Typeface, weight, style'],['Line height మరియు spacing','Font ఎంపిక'],['Readability మరియు legibility','అక్షరాల రూపం']],
 ex_title='Font vs Typography system',
 ex_te='''- Roboto Bold 24px ఒక font specification.
- Heading hierarchy, line height, paragraph spacing, alignment కలిపి Typography System.''',
 ex_en='''- Roboto Bold 24px is a font specification.
- Heading hierarchy, line height, paragraph spacing and alignment together form a Typography System.''',
 iv_en='"Typography is the art and system of arranging text for readability and visual communication, while a font is a specific representation of a typeface."',
 iv_te='Typography ఒక వ్యవస్థ; font అందులో ఉపయోగించే ఒక నిర్దిష్ట రూపం మాత్రమే.'),

dict(n=99, A='Padding', B='Margin', q_te='Padding మరియు Margin మధ్య తేడా ఏమిటి?',
 te='''Padding:

ఒక element యొక్క content మరియు దాని boundary మధ్య ఉండే internal spacing.

Margin:

ఒక element boundary బయట, ఇతర elements‌తో దూరం కల్పించే external spacing.''',
 defs=["Padding: The internal spacing between an element's content and its boundary.",  # Claude
       "Margin: The external spacing outside an element's boundary that separates it from other elements."],  # Claude
 hdr=['Padding', 'Margin'],  # Claude: the PDF has no table for Q99
 rows=[['Inside the boundary', 'Outside the boundary'], ['Space around the content', 'Space between elements'], ['Takes the element background', 'Usually transparent'], ['Example: 16px around button text', 'Example: 12px gap between two buttons']],
 tbl_te=[['Boundary లోపల','Boundary బయట'],['Content చుట్టూ స్థలం','Elements మధ్య దూరం'],['Element background రంగు ఉంటుంది','సాధారణంగా పారదర్శకం'],['ఉదా: Button text చుట్టూ 16px','ఉదా: రెండు buttons మధ్య 12px']],
 ex_title='Button spacing',
 ex_te=fig('g7-box-model', 'Box model: margin outside the border, padding inside around the content', 'Margin – బయటి స్థలం · Padding – లోపలి స్థలం · Content.', 'Illustrative CSS box-model spacing.') +
       '\n\nButton లో text చుట్టూ 16px internal spacing = Padding.\n\nరెండు buttons మధ్య 12px gap కోసం ఒక button‌కు external margin ఇవ్వవచ్చు. Modern layouts‌లో parent gap property కూడా ఉపయోగిస్తారు.',
 ex_en=fig('g7-box-model', 'CSS box model', '', 'Illustrative CSS box-model spacing.') +
       '\n\n16px of internal spacing around a button\'s text = Padding.\n\nFor a 12px gap between two buttons, one button can be given an external margin. Modern layouts also use the parent\'s gap property.',
 iv_en='"Padding controls the internal space between content and an element\'s boundary, while Margin controls the external space around the element."',
 iv_te='Padding లోపలి స్థలం; Margin బయటి స్థలం.'),

dict(n=100, A='Grid System', B='Layout System', q_te='Grid System మరియు Layout System మధ్య తేడా ఏమిటి?',
 te='''Grid System:

Columns, gutters, margins ఉపయోగించి elements‌ను align చేసే structure.

Layout System:

Grid‌తో పాటు spacing, positioning, containers, responsive behavior, Flexbox వంటి rules‌ను కలిగి ఉండే broader arrangement framework.''',
 defs=['Grid System: A structure that aligns elements using columns, gutters and margins.',  # Claude
       'Layout System: A broader arrangement framework that includes the grid plus rules for spacing, positioning, containers, responsive behaviour and Flexbox.'],  # Claude
 hdr=['Grid System', 'Layout System'],
 rows=[['Alignment framework', 'Overall arrangement rules'], ['Columns & gutters', 'Grid, flex, spacing'], ['Structural consistency', 'Responsive composition'], ['Often a layout technique', 'Broader layout approach']],
 tbl_te=[['Alignment framework','మొత్తం అమరిక నియమాలు'],['Columns మరియు gutters','Grid, flex, spacing'],['నిర్మాణ consistency','Responsive కూర్పు'],['తరచుగా ఒక layout technique','విస్తృత layout విధానం']],
 ex_title='Website layout',
 ex_te='''- 12-column desktop grid = Grid System.
- Sidebar + Header + Main Content + responsive behavior = Layout System.''',
 ex_en='''- 12-column desktop grid = Grid System.
- Sidebar + Header + Main Content + responsive behaviour = Layout System.''',
 iv_en='"A Grid System provides a structured alignment framework, while a Layout System defines how all interface elements are arranged and adapt across screen sizes."',
 iv_te='Grid alignment కోసం; Layout System అన్ని elements అమరిక, screen sizes కు సర్దుబాటు కోసం.'),

dict(n=101, A='Responsive Grid', B='Fixed Grid', q_te='Responsive Grid మరియు Fixed Grid మధ్య తేడా ఏమిటి?',
 te='''Responsive Grid:

Screen size లేదా container width ఆధారంగా columns, spacing, dimensions మారే grid.

Fixed Grid:

నిర్దిష్ట width లేదా column dimensions‌తో పనిచేసే grid.''',
 defs=['Responsive Grid: A grid whose columns, spacing and dimensions change with the screen size or container width.',  # Claude
       'Fixed Grid: A grid that works with a set width or fixed column dimensions.'],  # Claude
 hdr=['Responsive Grid', 'Fixed Grid'],  # Claude: the PDF has no table for Q101
 rows=[['Adapts to screen or container width', 'Keeps predefined dimensions'], ['Column count can change', 'Column count and width stay fixed'], ['Suits multi-device products', 'Suits controlled, single-width layouts'], ['Example: 4 columns on desktop, 1 on mobile', 'Example: 960px layout with 12 fixed columns']],
 tbl_te=[['Screen లేదా container width కు సర్దుకుంటుంది','ముందే నిర్ణయించిన కొలతలు ఉంటాయి'],['Columns సంఖ్య మారవచ్చు','Columns సంఖ్య, width స్థిరం'],['అనేక devices products కు సరిపోతుంది','నియంత్రిత, ఒకే width layouts కు'],['ఉదా: Desktop లో 4, mobile లో 1 column','ఉదా: 12 స్థిర columns తో 960px layout']],
 ex_title='Desktop vs Mobile',
 ex_te=fig('g7-responsive-grid', 'Responsive grid: four columns on desktop, one column on mobile', 'Desktop: 4 columns · Mobile: 1 column.', 'Responsive grid illustration – desktop: 4 columns, mobile: 1 column.'),
 ex_en=fig('g7-responsive-grid', 'Responsive grid', '', 'Responsive grid illustration – desktop: 4 columns, mobile: 1 column.'),
 iv_en='"A Responsive Grid adapts its structure to different screen sizes or containers, whereas a Fixed Grid maintains predefined dimensions. Responsive grids are generally more suitable for multi-device digital products."',
 iv_te='అనేక devices కోసం responsive grid సాధారణంగా మెరుగైన ఎంపిక.'),

dict(n=102, A='Visual Hierarchy', B='Information Hierarchy', q_te='Visual Hierarchy మరియు Information Hierarchy మధ్య తేడా ఏమిటి?',
 te='''Visual Hierarchy:

Size, color, contrast, position, spacing ద్వారా యూజర్ attention‌ను guide చేయడం.

Information Hierarchy:

Content‌ను importance, relationships, logical structure ఆధారంగా organize చేయడం.''',
 defs=["Visual Hierarchy: Guiding the user's attention through size, colour, contrast, position and spacing.",  # Claude
       'Information Hierarchy: Organising content by importance, relationships and logical structure.'],  # Claude
 hdr=['Visual Hierarchy', 'Information Hierarchy'],
 rows=[['Visual priority', 'Content priority'], ['Size, color, contrast', 'Meaning, grouping, order'], ['Guides attention', 'Guides understanding'], ['Presentation-focused', 'Content-structure-focused']],
 tbl_te=[['దృశ్య ప్రాధాన్యత','Content ప్రాధాన్యత'],['Size, రంగు, contrast','అర్థం, grouping, క్రమం'],['దృష్టిని నడిపిస్తుంది','అవగాహనను నడిపిస్తుంది'],['ప్రదర్శనపై దృష్టి','Content నిర్మాణంపై దృష్టి']],
 ex_title='Product Detail Page',
 ex_te='''- Information Hierarchy: Product Name → Price → Description → Reviews.
- Visual Hierarchy: పెద్ద Product Name → Bold Price → ప్రముఖంగా Buy Button.''',
 ex_en='''- Information Hierarchy: Product Name → Price → Description → Reviews.
- Visual Hierarchy: Large Product Name → Bold Price → Prominent Buy Button.''',
 iv_en='"Information Hierarchy organizes content based on meaning and importance, while Visual Hierarchy uses visual design techniques to communicate that importance and guide user attention."',
 iv_te='ముందు information hierarchy (ఏది ముఖ్యం), తర్వాత visual hierarchy (దాన్ని ఎలా కనిపించేలా చేయాలి).'),

dict(n=103, A='Contrast', B='Accessibility', q_te='Contrast మరియు Accessibility మధ్య తేడా ఏమిటి?',
 te='''Contrast:

రెండు visual elements మధ్య ఉన్న difference. ఉదాహరణకు text మరియు background మధ్య brightness difference.

Accessibility:

వివిధ abilities ఉన్న వ్యక్తులు కూడా digital products‌ను perceive, understand, navigate, operate చేయగలిగేలా డిజైన్ చేయడం.

WCAG 2.2 ముఖ్యమైన contrast guidelines:
- Normal text: కనీసం 4.5:1
- Large text: కనీసం 3:1
- Essential UI components మరియు graphical objects: సాధారణంగా 3:1

ఈ ratios WCAG AAలో సంబంధిత success criteriaకి వర్తిస్తాయి; అన్ని visual elements‌కు ఒకే నియమం కాదు.''',
 defs=['Contrast: The difference between two visual elements – for example, the brightness difference between text and its background.',  # Claude
       'Accessibility: Designing digital products so that people with different abilities can perceive, understand, navigate and operate them.',  # Claude
       'WCAG 2.2 AA contrast: normal text at least 4.5:1; large text at least 3:1; essential UI components and graphical objects generally 3:1. These apply to the relevant success criteria, not to every visual element.'],  # Claude
 hdr=['Contrast', 'Accessibility'],
 rows=[['Visual property', 'Broader inclusive requirement'], ['Helps distinguish elements', 'Supports diverse abilities'], ['Text/background readability', 'Keyboard, screen reader, touch'], ['One accessibility consideration', 'Multiple accessibility dimensions']],
 tbl_te=[['ఒక visual లక్షణం','విస్తృత inclusive అవసరం'],['Elements ను వేరుగా గుర్తించడంలో సహాయం','విభిన్న సామర్థ్యాలకు మద్దతు'],['Text / background readability','Keyboard, screen reader, touch'],['ఒక accessibility అంశం','అనేక accessibility కోణాలు']],
 ex_title='Banking App',  # Claude: the PDF has no separate example for Q103
 ex_te='''- Contrast: "Transfer" button లో తెల్లని text, ముదురు నీలి background – కనీసం 4.5:1 ratio.
- Accessibility: అదే button కు screen reader label, keyboard focus, తగినంత touch size కూడా ఉండాలి.''',
 ex_en='''- Contrast: white text on a dark blue "Transfer" button – at least 4.5:1.
- Accessibility: the same button also needs a screen-reader label, keyboard focus and an adequate touch size.''',
 iv_en='"Contrast is one important aspect of visual accessibility, but accessibility is broader. It also includes keyboard navigation, screen-reader support, meaningful labels, focus management, and inclusive interaction patterns."',
 iv_te='Contrast accessibility లో ఒక భాగం మాత్రమే; accessibility అంతకంటే చాలా విస్తృతం.'),

dict(n=104, A='Brand Identity', B='Visual Identity', q_te='Brand Identity మరియు Visual Identity మధ్య తేడా ఏమిటి?',
 te='''Brand Identity:

ఒక బ్రాండ్ ఏమిటి, దాని values, personality, positioning, purpose, communication ఎలా ఉండాలి అనే broader identity.

Visual Identity:

ఆ బ్రాండ్‌ను visually represent చేసే logo, colors, typography, imagery, graphic elements.''',
 defs=['Brand Identity: The broader identity of a brand – what it is, its values, personality, positioning, purpose and how it communicates.',  # Claude
       'Visual Identity: The logo, colours, typography, imagery and graphic elements that represent the brand visually.'],  # Claude
 hdr=['Brand Identity', 'Visual Identity'],
 rows=[['Brand personality', 'Visual representation'], ['Mission & values', 'Logo & colors'], ['Positioning & voice', 'Typography & imagery'], ['Broader brand expression', 'Visual expression']],
 tbl_te=[['Brand వ్యక్తిత్వం','దృశ్య ప్రాతినిధ్యం'],['Mission మరియు values','Logo మరియు రంగులు'],['Positioning మరియు voice','Typography మరియు imagery'],['విస్తృత brand వ్యక్తీకరణ','దృశ్య వ్యక్తీకరణ']],
 ex_title="D'SARAS",
 ex_te='''- Brand Identity: Design, Knowledge, Intelligence అనే positioning, purpose, personality.
- Visual Identity: D’SARAS Logo, VIBGYOR-inspired palette, typography, graphic style.''',
 ex_en='''- Brand Identity: the positioning, purpose and personality of Design, Knowledge and Intelligence.
- Visual Identity: the D'SARAS logo, VIBGYOR-inspired palette, typography and graphic style.''',
 iv_en='"Brand Identity represents the overall personality, values, and positioning of a brand, while Visual Identity expresses that brand through visual elements such as logos, colors, typography, and imagery."',
 iv_te='Brand Identity బ్రాండ్ అర్థం; Visual Identity ఆ అర్థాన్ని కనిపించేలా చేసే రూపం.'),

dict(n=105, A='Icon', B='Illustration', q_te='Icon మరియు Illustration మధ్య తేడా ఏమిటి?',
 te='''Icon:

ఒక action, object లేదా concept‌ను చిన్న, simplified visual symbol ద్వారా represent చేయడం.

Illustration:

ఒక idea, story, emotion లేదా context‌ను communicate చేసే detailed visual artwork.''',
 defs=['Icon: A small, simplified visual symbol that represents an action, object or concept.',  # Claude
       'Illustration: Detailed visual artwork that communicates an idea, story, emotion or context.'],  # Claude
 hdr=['Icon', 'Illustration'],
 rows=[['Simplified symbol', 'Expressive artwork'], ['Functional communication', 'Storytelling & emotion'], ['Usually small', 'Variable size'], ['Navigation & actions', 'Onboarding, empty states']],
 tbl_te=[['సరళమైన చిహ్నం','భావవ్యక్తీకరణ కళాకృతి'],['క్రియాత్మక (functional) సమాచారం','కథ చెప్పడం, భావోద్వేగం'],['సాధారణంగా చిన్నది','పరిమాణం మారుతుంది'],['Navigation మరియు actions','Onboarding, empty states']],
 ex_title='Shopping Cart',
 ex_te='''- Cart Icon → Shopping Cart screen‌కు navigation.
- Empty Cart Illustration → Cart ఖాళీగా ఉందని friendly visual message ఇవ్వడం.''',
 ex_en='''- Cart icon → navigates to the Shopping Cart screen (functional symbol).
- Empty-cart illustration → gives a friendly visual message that the cart is empty (context & storytelling).''',
 iv_en='"Icons are simplified visual symbols used for quick recognition and interaction, while Illustrations communicate ideas, emotions, or stories and help create engaging product experiences."',
 iv_te='Icon త్వరగా గుర్తించి చర్య తీసుకోవడానికి; Illustration భావాన్ని, కథను చెప్పడానికి.'),
]

INTRO_TE = 'ఈ గ్రూప్‌లో UI Design, Design Systems, Components, Typography, Layouts, Visual Hierarchy, Branding వంటి ముఖ్యమైన అంశాలను నేర్చుకుందాం. Senior UX Designer, Lead Product Designer, Principal Designer, UX Manager ఇంటర్వ్యూలలో ఈ అంశాలపై ప్రశ్నలు ఎక్కువగా వస్తాయి.'
REVISION = [(91, 'UI vs UX', 'Interface vs Experience'), (92, 'Design System vs Style Guide', 'Framework vs Visual Rules'),
 (93, 'Design System vs Component Library', 'Complete System vs Components'), (94, 'Component vs Pattern', 'Element vs Solution'),
 (95, 'Component vs Variant', 'Base Element vs Version'), (96, 'Tokens vs Variables', 'Design Decisions vs Value Management'),
 (97, 'Atomic Design vs Design System', 'Methodology vs Framework'), (98, 'Typography vs Font', 'Text System vs Font Specification'),
 (99, 'Padding vs Margin', 'Internal vs External Spacing'), (100, 'Grid vs Layout', 'Alignment vs Arrangement'),
 (101, 'Responsive vs Fixed Grid', 'Adaptive vs Fixed Dimensions'), (102, 'Visual vs Information Hierarchy', 'Visual Priority vs Content Priority'),
 (103, 'Contrast vs Accessibility', 'Visual Property vs Inclusive Usability'), (104, 'Brand vs Visual Identity', 'Brand Meaning vs Visual Expression'),
 (105, 'Icon vs Illustration', 'Symbol vs Storytelling')]
PRACTICE_TITLE = 'Practical Interview Quiz'
PRACTICE_BODY = '''Test your understanding · మీ అవగాహనను పరీక్షించుకోండి.

1. A checkout flow combines forms, progress indicators, validation, and confirmation. What is it? (Component / Pattern / Variant)
2. Which concept defines reusable values such as color.primary and spacing.md? (Design Tokens / Font / Visual Hierarchy)
3. What is the minimum WCAG AA contrast ratio for normal text? (3:1 / 4.5:1 / 7:1)
4. Which term describes the space inside a button between its text and boundary? (Margin / Gutter / Padding)
5. Which is broader: Design System or Component Library? (Component Library / Design System / Both are identical)

### Answer key · జవాబులు
1. Pattern · 2. Design Tokens · 3. 4.5:1 · 4. Padding · 5. Design System'''
