# Group 8 – Accessibility & Inclusive Design (Q106–Q115), assembled from Generate_UX_Vs_Questions_8.pdf.
# Telugu explanations/examples, English definitions, tables and interview answers = PDF text.
# tbl_te, iv_te and ex_en (English versions of the PDF's Telugu examples) = written by Claude.

ITEMS = [
dict(n=106, A='Accessibility', B='Usability', q_te='Accessibility మరియు Usability మధ్య తేడా ఏమిటి?',
 te='''Accessibility (అందుబాటులో ఉండేలా డిజైన్ చేయడం):

విభిన్న సామర్థ్యాలు ఉన్న వ్యక్తులు కూడా digital products‌ను perceive, understand, navigate, and interact చేయగలిగేలా డిజైన్ చేయడం.

Usability (సులభంగా ఉపయోగించగలగడం):

ఒక ప్రొడక్ట్‌ను యూజర్లు సులభంగా, సమర్థవంతంగా, సంతృప్తికరంగా ఉపయోగించగలిగేలా డిజైన్ చేయడం.''',
 defs=['Accessibility: Accessibility ensures that digital products can be used by people with diverse abilities, including people with visual, auditory, motor, and cognitive disabilities.',
       'Usability: Usability measures how effectively, efficiently, and satisfactorily users can achieve their goals.'],
 hdr=['Accessibility', 'Usability'],
 rows=[['Inclusive access', 'Ease of use'], ['Considers diverse abilities', 'Considers user effectiveness'], ['Screen reader support', 'Simple navigation'], ['Keyboard accessibility', 'Efficient task completion'], ['Accessible interaction', 'Understandable interaction']],
 tbl_te=[['అందరికీ అందుబాటు','ఉపయోగ సౌలభ్యం'],['విభిన్న సామర్థ్యాలను పరిగణిస్తుంది','User ప్రభావశీలతను పరిగణిస్తుంది'],['Screen reader మద్దతు','సరళమైన navigation'],['Keyboard accessibility','సమర్థవంతంగా task పూర్తి'],['అందుబాటులో ఉండే interaction','అర్థమయ్యే interaction']],
 ex_title='Banking App',
 ex_te='''Accessibility:
- Blind users కోసం screen reader labels.
- Motor disabilities ఉన్నవారికి keyboard navigation.
- Low vision users కోసం sufficient contrast.

Usability:
- Money transfer process‌ను simple steps‌లో రూపొందించడం.
- Clear instructions ఇవ్వడం.
- Unnecessary steps తగ్గించడం.''',
 ex_en='''Accessibility:
- Screen reader labels for blind users.
- Keyboard navigation for people with motor disabilities.
- Sufficient contrast for low-vision users.

Usability:
- Designing the money-transfer process in simple steps.
- Giving clear instructions.
- Removing unnecessary steps.''',
 iv_en='"Accessibility ensures that people with diverse abilities can access and interact with a product, while usability focuses on how easily and effectively users can achieve their goals. Both are essential for creating inclusive digital experiences."',
 iv_te='Accessibility అందరూ ఉపయోగించగలిగేలా, Usability సులభంగా ఉపయోగించగలిగేలా – inclusive అనుభవానికి రెండూ అవసరం.'),

dict(n=107, A='Accessibility', B='Inclusive Design', q_te='Accessibility మరియు Inclusive Design మధ్య తేడా ఏమిటి?',
 te='''Accessibility:

ప్రత్యేకంగా disabilities ఉన్న వ్యక్తులు digital products‌ను ఉపయోగించగలిగేలా barriers తొలగించడం.

Inclusive Design:

విభిన్న backgrounds, abilities, ages, languages, cultures, and circumstances ఉన్న వ్యక్తుల అవసరాలను design process‌లో పరిగణనలోకి తీసుకోవడం.''',
 defs=['Accessibility: Accessibility focuses on removing barriers that prevent people with disabilities from using products and services.',
       'Inclusive Design: Inclusive Design is an approach that considers human diversity and includes people with different needs and circumstances throughout the design process.'],
 hdr=['Accessibility', 'Inclusive Design'],
 rows=[['Removes access barriers', 'Considers human diversity'], ['Often focuses on disabilities', 'Broader range of differences'], ['Standards and guidelines', 'Research and design approach'], ['WCAG is an important reference', 'Co-design and diverse research']],
 tbl_te=[['యాక్సెస్ అడ్డంకులను తొలగిస్తుంది','మానవ వైవిధ్యాన్ని పరిగణిస్తుంది'],['తరచుగా disabilities పై దృష్టి','విస్తృత తేడాలపై దృష్టి'],['ప్రమాణాలు, guidelines','Research మరియు design విధానం'],['WCAG ముఖ్యమైన reference','Co-design, విభిన్న research']],
 ex_title='E-commerce App',
 ex_te='''Accessibility:
- Screen reader support.
- Keyboard navigation.
- Text contrast.

Inclusive Design:
- Multiple language options.
- వివిధ literacy levels కోసం simple language.
- Different payment methods.
- వివిధ age groups మరియు user needs కు support.''',
 ex_en='''Accessibility:
- Screen reader support.
- Keyboard navigation.
- Text contrast.

Inclusive Design:
- Multiple language options.
- Simple language for different literacy levels.
- Different payment methods.
- Support for different age groups and user needs.''',
 iv_en='"Accessibility focuses on ensuring that people with disabilities can use a product, while Inclusive Design is a broader approach that considers diverse human needs, abilities, backgrounds, and situations throughout the design process."',
 iv_te='Accessibility disabilities ఉన్నవారికి అడ్డంకులు తొలగిస్తుంది; Inclusive Design మొత్తం మానవ వైవిధ్యాన్ని design లో పరిగణిస్తుంది.'),

dict(n=108, A='Inclusive Design', B='Universal Design', q_te='Inclusive Design మరియు Universal Design మధ్య తేడా ఏమిటి?',
 te='''Inclusive Design:

విభిన్న అవసరాలు ఉన్న వ్యక్తులను design process‌లో భాగస్వామ్యం చేసి, వారి అవసరాలకు అనుగుణంగా solutions రూపొందించడం.

Universal Design:

సాధ్యమైనంత వరకు ఎక్కువ మంది వ్యక్తులు ప్రత్యేక adaptations అవసరం లేకుండా ఉపయోగించగలిగే products and environments‌ను రూపొందించడం.''',
 defs=['Inclusive Design: Inclusive Design involves designing with diverse people and adapting experiences to accommodate different needs.',
       'Universal Design: Universal Design aims to create products and environments usable by the widest range of people, to the greatest extent possible, without the need for adaptation or specialized design.'],
 hdr=['Inclusive Design', 'Universal Design'],
 rows=[['Process-oriented approach', 'Broad design philosophy'], ['Includes diverse users in design', 'Aims for broad usability'], ['Adapts based on user needs', 'Reduces need for special adaptations'], ['Can support tailored solutions', 'Seeks widely usable solutions']],
 tbl_te=[['Process ఆధారిత విధానం','విస్తృత design తత్వం'],['విభిన్న users ను design లో భాగస్వాములను చేస్తుంది','విస్తృత usability లక్ష్యం'],['User అవసరాల ఆధారంగా సర్దుకుంటుంది','ప్రత్యేక adaptations అవసరాన్ని తగ్గిస్తుంది'],['ప్రత్యేక (tailored) పరిష్కారాలకు మద్దతు','విస్తృతంగా ఉపయోగపడే పరిష్కారాలు']],
 ex_title='Public Website',
 ex_te='''Inclusive Design:
- Different language preferences తెలుసుకోవడానికి user research చేయడం.
- Users‌తో కలిసి design solutions test చేయడం.

Universal Design:
- Clear navigation.
- Readable text.
- Easy-to-use controls.
- Simple, consistent interactions.''',
 ex_en='''Inclusive Design:
- Doing user research to learn different language preferences.
- Testing design solutions together with users.

Universal Design:
- Clear navigation.
- Readable text.
- Easy-to-use controls.
- Simple, consistent interactions.''',
 iv_en='"Inclusive Design emphasizes involving diverse users and addressing their specific needs, whereas Universal Design aims to create solutions that are usable by the widest possible range of people without requiring special adaptations."',
 iv_te='Inclusive Design విభిన్న users ను చేర్చుకునే process; Universal Design ప్రత్యేక మార్పులు లేకుండా ఎక్కువ మంది ఉపయోగించగలిగే లక్ష్యం.'),

dict(n=109, A='WCAG', B='ADA', q_te='WCAG మరియు ADA మధ్య తేడా ఏమిటి?',
 te='''WCAG – Web Content Accessibility Guidelines:

W3C యొక్క Web Accessibility Initiative (WAI) అభివృద్ధి చేసిన web accessibility guidelines.

ADA – Americans with Disabilities Act:

United States‌లో disabilities ఉన్న వ్యక్తులపై discrimination‌ను నిషేధించే civil rights law.

Important Interview Point:

WCAG అనేది law కాదు; అది technical accessibility guidelines. ADA అనేది US law. WCAG compliance అనేది అనేక సందర్భాల్లో web accessibilityని evaluate చేయడానికి ఉపయోగించే ముఖ్యమైన technical reference.''',
 defs=['WCAG: WCAG provides internationally recognized technical guidelines for making web content more accessible to people with disabilities.',
       'ADA: ADA is a US civil rights law that prohibits discrimination against people with disabilities, including in areas covered by its requirements.',
       'Important interview point: WCAG is not a law – it is a set of technical accessibility guidelines. ADA is a US law. WCAG compliance is an important technical reference used in many cases to evaluate web accessibility.'],  # last line: Claude's translation
 hdr=['WCAG', 'ADA'],
 rows=[['Technical guidelines', 'US civil rights law'], ['Developed by W3C', 'US federal law'], ['Explains accessibility requirements for web content', 'Prohibits disability discrimination'], ['Uses conformance levels A, AA, AAA', 'Legal obligations depend on applicable provisions'], ['Internationally used', 'Applies within the United States']],
 tbl_te=[['Technical guidelines','US civil rights చట్టం'],['W3C అభివృద్ధి చేసింది','US federal చట్టం'],['Web content కు accessibility అవసరాలను వివరిస్తుంది','Disability వివక్షను నిషేధిస్తుంది'],['A, AA, AAA conformance levels ఉపయోగిస్తుంది','చట్టపరమైన బాధ్యతలు వర్తించే నిబంధనలపై ఆధారపడతాయి'],['అంతర్జాతీయంగా ఉపయోగిస్తారు','United States లో వర్తిస్తుంది']],
 ex_title='US-based SaaS company',
 ex_te='ఒక US-based SaaS company తన website‌ను accessibility-friendlyగా రూపొందించాలనుకుంటే, WCAG guidelines‌ను technical implementation కోసం ఉపయోగించవచ్చు. దాని legal obligations మాత్రం వర్తించే ADA provisions మరియు ఇతర చట్టాలపై ఆధారపడతాయి.',
 ex_en='If a US-based SaaS company wants an accessibility-friendly website, it can use the WCAG guidelines for the technical implementation. Its legal obligations, however, depend on the applicable ADA provisions and other laws.',
 iv_en='"WCAG is a set of technical accessibility guidelines developed by W3C, whereas ADA is a US civil rights law that prohibits disability discrimination. WCAG helps teams implement accessible digital experiences, while ADA establishes legal obligations."',
 iv_te='WCAG technical guidelines (ఎలా చేయాలి); ADA US చట్టం (చట్టపరమైన బాధ్యతలు).'),

dict(n=110, A='WCAG A', B='AA vs AAA', q_en='What is the difference between WCAG Level A, AA and AAA?', kd_title='WCAG A vs AA vs AAA',
 q_te='WCAG Level A, AA మరియు AAA మధ్య తేడా ఏమిటి?',
 te='''WCAGలో మూడు conformance levels ఉంటాయి.

Level A – Minimum accessibility requirements:

అత్యంత ప్రాథమిక accessibility barriers‌ను పరిష్కరించే requirements.

Level AA – Recommended practical target:

ఎక్కువ web accessibility projects‌లో సాధారణంగా లక్ష్యంగా పెట్టుకునే level.

Level AAA – Highest conformance level:

మరింత కఠినమైన accessibility requirements. అన్ని content‌కు AAA సాధించడం ఎల్లప్పుడూ సాధ్యం కాకపోవచ్చు.

WCAG 2.2 ముఖ్యమైన Contrast Ratios:

Requirement\tAA\tAAA
Normal text\t4.5:1\t7:1
Large text\t3:1\t4.5:1

Note: Large text సాధారణంగా కనీసం 18pt regular లేదా 14pt bold. Contrast criteria కు కొన్ని ప్రత్యేక మినహాయింపులు ఉంటాయి.''',
 defs=['Level A – Minimum accessibility requirements: requirements that remove the most basic accessibility barriers.',  # Claude translation
       'Level AA – Recommended practical target: the level most web accessibility projects commonly aim for.',  # Claude translation
       'Level AAA – Highest conformance level: stricter requirements; achieving AAA for all content may not always be possible.',  # Claude translation
       'WCAG 2.2 contrast ratios: normal text – AA 4.5:1, AAA 7:1; large text – AA 3:1, AAA 4.5:1. Large text generally means at least 18pt regular or 14pt bold. Contrast criteria have specific exceptions.'],
 hdr=['Level', 'Meaning', 'Example'],
 rows=[['A', 'Basic', 'Keyboard accessibility'], ['AA', 'Stronger requirements', 'Normal text contrast 4.5:1'], ['AAA', 'Highest', 'Normal text contrast 7:1']],
 tbl_te=[['A','ప్రాథమికం','Keyboard accessibility'],['AA','మరింత బలమైన అవసరాలు','Normal text contrast 4.5:1'],['AAA','అత్యున్నతం','Normal text contrast 7:1']],
 ex_title='Mobile Banking App',
 ex_te='''ఒక mobile banking app‌లో:
- Level A: అన్ని controls keyboard ద్వారా accessible‌గా ఉండాలి.
- Level AA: Normal text contrast కనీసం 4.5:1 ఉండాలి.
- Level AAA: Normal text contrast కనీసం 7:1 ఉండాలి.''',
 ex_en='''In a mobile banking app:
- Level A: all controls must be accessible by keyboard.
- Level AA: normal text contrast must be at least 4.5:1.
- Level AAA: normal text contrast must be at least 7:1.''',
 iv_en='"WCAG defines three conformance levels: A, AA, and AAA. Level A covers basic requirements, Level AA addresses a broader range of accessibility needs and is a common target, and Level AAA represents the highest level of conformance."',
 iv_te='A ప్రాథమికం, AA సాధారణ లక్ష్యం, AAA అత్యున్నత స్థాయి.'),

dict(n=111, A='Alt Text', B='ARIA Label', q_te='Alt Text మరియు ARIA Label మధ్య తేడా ఏమిటి?',
 te='''Alt Text (Alternative Text):

Image యొక్క meaning లేదా purpose‌ను text రూపంలో వివరించే alternative description.

ARIA Label:

Interactive element‌కు accessible name అందించడానికి ఉపయోగించే ARIA attribute.

Important:

Decorative images‌కు సాధారణంగా empty alt (alt="") ఉపయోగిస్తారు. Visible label ఉన్న button‌కు unnecessary aria-label పెట్టకుండా, visible label‌ను accessible name‌గా ఉపయోగించడం మంచిది.''',
 defs=['Alt Text: Alt Text provides a textual alternative for meaningful images, especially for users relying on screen readers.',
       'ARIA Label: aria-label provides an accessible name for an element when a suitable visible label is not available or when additional accessible naming is needed.',
       'Important: Decorative images usually use an empty alt (alt=""). For a button that already has a visible label, use the visible label as the accessible name instead of adding an unnecessary aria-label.'],  # last line: Claude's translation
 hdr=['Alt Text', 'ARIA Label'],
 rows=[['Describes image content or purpose', 'Names an interface element'], ['Commonly uses alt attribute', 'Uses aria-label'], ['Useful for meaningful images', 'Useful for controls without visible labels'], ['Can describe image function', 'Can name buttons, controls, etc.']],
 tbl_te=[['Image content లేదా ఉద్దేశాన్ని వివరిస్తుంది','Interface element కు పేరు ఇస్తుంది'],['సాధారణంగా alt attribute','aria-label ఉపయోగిస్తుంది'],['అర్థవంతమైన images కు ఉపయోగకరం','కనిపించే label లేని controls కు ఉపయోగకరం'],['Image పనిని వివరించగలదు','Buttons, controls మొదలైనవాటికి పేరు ఇవ్వగలదు']],
 ex_title='Product page',
 ex_te='''Alt Text ఉదాహరణ:
- Product image
- Alt: "Red mountain bicycle with black tires"

ARIA Label ఉదాహరణ:
- Search button (icon మాత్రమే)
- aria-label="Search products"''',
 ex_en='''Alt Text example:
- Product image
- Alt: "Red mountain bicycle with black tires"

ARIA Label example:
- Search button (icon only)
- aria-label="Search products"''',
 iv_en='"Alt Text provides a textual alternative for meaningful images, while ARIA Label provides an accessible name for interface elements such as buttons and controls. Both help assistive technologies communicate information to users."',
 iv_te='Alt text images కోసం; aria-label buttons, controls కోసం – రెండూ assistive technologies కు సమాచారం అందిస్తాయి.'),

dict(n=112, A='Keyboard Navigation', B='Screen Reader Navigation', q_te='Keyboard Navigation మరియు Screen Reader Navigation మధ్య తేడా ఏమిటి?',
 te='''Keyboard Navigation:

Mouse ఉపయోగించకుండా keyboard ద్వారా website లేదా application‌ను navigate చేయడం.

Common keys:
- Tab – Next focusable element.
- Shift + Tab – Previous focusable element.
- Enter / Space – Activate controls.
- Arrow Keys – Navigate within certain controls.
- Esc – Close dialogs or menus, where supported.

Screen Reader Navigation:

Screen reader software ద్వారా interface content‌ను speech లేదా braille రూపంలో తెలుసుకుని navigate చేయడం.
ఉదాహరణలు: NVDA, JAWS, VoiceOver, TalkBack.''',
 defs=['Keyboard Navigation: Keyboard Navigation allows users to interact with interface elements using keyboard input instead of a mouse or touch. Common keys: Tab, Shift + Tab, Enter / Space, Arrow keys, Esc.',
       'Screen Reader Navigation: Screen Reader Navigation enables users to explore content and understand interface semantics through assistive technology – e.g. NVDA, JAWS, VoiceOver, TalkBack.'],
 hdr=['Keyboard Navigation', 'Screen Reader Navigation'],
 rows=[['Keyboard-based interaction', 'Assistive technology-based access'], ['Focus order', 'Semantic reading and navigation'], ['Tab, Enter, Space', 'Headings, landmarks, labels'], ['Supports motor accessibility', 'Supports blind and low-vision users']],
 tbl_te=[['Keyboard ఆధారిత interaction','Assistive technology ఆధారిత యాక్సెస్'],['Focus క్రమం','Semantic reading మరియు navigation'],['Tab, Enter, Space','Headings, landmarks, labels'],['Motor accessibility కి సహాయం','అంధులు, low-vision users కు సహాయం']],
 ex_title='Login Form',
 ex_te='''Keyboard user:
1. Tab → Username.
2. Tab → Password.
3. Tab → Login button.
4. Enter → Submit.

Screen reader user:
- Username field label వింటారు.
- Password field label వింటారు.
- Login button ఉద్దేశం అర్థం చేసుకుంటారు.
- అర్థవంతమైన error messages పొందుతారు.''',
 ex_en='''Keyboard user:
1. Tab → Username.
2. Tab → Password.
3. Tab → Login button.
4. Enter → Submit.

Screen reader user:
- Hears the Username field label.
- Hears the Password field label.
- Understands the Login button's purpose.
- Receives meaningful error messages.''',
 iv_en='"Keyboard Navigation enables users to operate an interface without a mouse, while Screen Reader Navigation helps users understand and navigate content through assistive technology. A well-designed product should support both."',
 iv_te='మంచి product keyboard మరియు screen reader రెండింటికీ మద్దతు ఇవ్వాలి.'),

dict(n=113, A='Color Blindness', B='Low Vision', q_te='Color Blindness మరియు Low Vision మధ్య తేడా ఏమిటి?',
 te='''Color Blindness:

కొన్ని colors మధ్య తేడాను గుర్తించడంలో ఇబ్బంది ఉండే visual condition.

Common types:
- Protanopia – Difficulty perceiving red.
- Deuteranopia – Difficulty perceiving green.
- Tritanopia – Difficulty perceiving blue-yellow differences.

Low Vision:

Glasses లేదా ఇతర correction ఉపయోగించినా కూడా రోజువారీ పనుల్లో vision-related difficulty ఉండే పరిస్థితి.''',
 defs=['Color Blindness: Color blindness is a condition that affects how a person perceives certain colors, often making some color combinations difficult to distinguish. Common types: Protanopia (red), Deuteranopia (green), Tritanopia (blue-yellow).',
       'Low Vision: Low vision refers to significant visual impairment that cannot be fully corrected with standard glasses, contact lenses, or treatment.'],
 hdr=['Color Blindness', 'Low Vision'],
 rows=[['Color perception differences', 'Reduced visual function'], ['Difficulty distinguishing colors', 'Difficulty seeing details'], ['Color combinations matter', 'Text size and clarity matter'], ['Use labels and patterns', 'Use zoom and readable layouts']],
 tbl_te=[['రంగులను గ్రహించడంలో తేడాలు','దృష్టి సామర్థ్యం తగ్గడం'],['రంగులను వేరుగా గుర్తించడంలో ఇబ్బంది','వివరాలను చూడడంలో ఇబ్బంది'],['రంగుల కలయికలు ముఖ్యం','Text size, స్పష్టత ముఖ్యం'],['Labels, patterns ఉపయోగించాలి','Zoom, చదవగలిగే layouts ఉపయోగించాలి']],
 ex_title='Dashboard',
 ex_te='''Color Blindness:
- Red = Failed, Green = Success అని colors మాత్రమే వాడకూడదు.
- Labels, icons, patterns కూడా ఉపయోగించాలి.

Low Vision:
- Text resizing support.
- High contrast.
- Clear typography.
- Browser zoom support.''',
 ex_en='''Color Blindness:
- Don't rely only on colour, such as Red = Failed and Green = Success.
- Also use labels, icons and patterns.

Low Vision:
- Text resizing support.
- High contrast.
- Clear typography.
- Browser zoom support.''',
 iv_en='"Color blindness affects the ability to distinguish certain colors, while low vision involves reduced visual function. As designers, we should avoid color-only communication and provide readable text, sufficient contrast, and flexible layouts."',
 iv_te='రంగుపై మాత్రమే ఆధారపడకుండా, చదవగలిగే text, తగిన contrast, flexible layouts ఇవ్వాలి.'),

dict(n=114, A='Responsive Design', B='Accessible Design', q_te='Responsive Design మరియు Accessible Design మధ్య తేడా ఏమిటి?',
 te='''Responsive Design:

వివిధ screen sizes మరియు devices‌కు అనుగుణంగా layout adapt అయ్యేలా డిజైన్ చేయడం.

Accessible Design:

విభిన్న abilities ఉన్న వ్యక్తులు కూడా interface‌ను ఉపయోగించగలిగేలా డిజైన్ చేయడం.''',
 defs=['Responsive Design: Responsive Design ensures that a digital interface adapts to different screen sizes, orientations, and device contexts.',
       'Accessible Design: Accessible Design ensures that interfaces can be perceived, understood, navigated, and operated by people with diverse abilities.'],
 hdr=['Responsive Design', 'Accessible Design'],
 rows=[['Adapts to screen sizes', 'Adapts to diverse abilities'], ['Mobile, tablet, desktop', 'Visual, auditory, motor, cognitive needs'], ['Flexible layouts', 'Assistive technology support'], ['Breakpoints and fluid grids', 'Semantic HTML and accessible controls']],
 tbl_te=[['Screen sizes కు సర్దుకుంటుంది','విభిన్న సామర్థ్యాలకు సర్దుకుంటుంది'],['Mobile, tablet, desktop','దృష్టి, వినికిడి, motor, cognitive అవసరాలు'],['Flexible layouts','Assistive technology మద్దతు'],['Breakpoints, fluid grids','Semantic HTML, accessible controls']],
 ex_title='E-commerce Website',
 ex_te='''Responsive:
- Desktopలో 4 product columns.
- Tabletలో 2 columns.
- Mobileలో 1 column.

Accessible:
- Images‌కు meaningful alt text.
- Buttons‌కు accessible names.
- Keyboard navigation.
- Text contrast.''',
 ex_en='''Responsive:
- 4 product columns on desktop.
- 2 columns on tablet.
- 1 column on mobile.

Accessible:
- Meaningful alt text for images.
- Accessible names for buttons.
- Keyboard navigation.
- Text contrast.''',
 iv_en='"Responsive Design adapts the interface to different devices and screen sizes, whereas Accessible Design ensures that people with diverse abilities can use the interface. A successful digital product should be both responsive and accessible."',
 iv_te='విజయవంతమైన product responsive మరియు accessible రెండూ కావాలి.'),

dict(n=115, A='Accessibility Audit', B='Usability Testing', q_te='Accessibility Audit మరియు Usability Testing మధ్య తేడా ఏమిటి?',
 te='''Accessibility Audit:

ఒక digital product accessibility guidelines మరియు standards‌ను ఎంతవరకు follow చేస్తుందో systematic‌గా evaluate చేయడం.

Usability Testing:

నిజమైన లేదా representative users‌తో tasks చేయించి, product‌ను ఎంత సులభంగా ఉపయోగిస్తున్నారో observe చేయడం.''',
 defs=['Accessibility Audit: An Accessibility Audit evaluates a product against accessibility standards such as WCAG and identifies barriers affecting users with disabilities.',
       'Usability Testing: Usability Testing involves observing users as they perform tasks to identify usability issues and improve the overall experience.'],
 hdr=['Accessibility Audit', 'Usability Testing'],
 rows=[['Checks accessibility barriers', 'Checks usability problems'], ['Uses WCAG criteria', 'Uses task-based observation'], ['Automated and manual checks', 'Moderated or unmoderated sessions'], ['Expert evaluation and assistive technology testing', 'Representative user participation'], ['Focuses on accessibility conformance', 'Focuses on effectiveness and experience']],
 tbl_te=[['Accessibility అడ్డంకులను తనిఖీ చేస్తుంది','Usability సమస్యలను తనిఖీ చేస్తుంది'],['WCAG ప్రమాణాలు ఉపయోగిస్తుంది','Task ఆధారిత పరిశీలన ఉపయోగిస్తుంది'],['Automated మరియు manual checks','Moderated లేదా unmoderated sessions'],['నిపుణుల మూల్యాంకనం, assistive technology testing','ప్రతినిధి users పాల్గొనడం'],['Accessibility conformance పై దృష్టి','ప్రభావశీలత, అనుభవంపై దృష్టి']],
 ex_title='Banking App',
 ex_te='''Accessibility Audit:
- Contrast ratios తనిఖీ చేయడం.
- Form labels verify చేయడం.
- Keyboard access test చేయడం.
- Screen readers తో test చేయడం.
- Focus indicators review చేయడం.

Usability Testing:
- Users ను డబ్బు transfer చేయమని అడగడం.
- ఎక్కడ ఇబ్బంది పడుతున్నారో గమనించడం.
- Task completion కొలవడం.
- గందరగోళమైన సూచనలను గుర్తించడం.''',
 ex_en='''Accessibility Audit:
- Check contrast ratios.
- Verify form labels.
- Test keyboard access.
- Test with screen readers.
- Review focus indicators.

Usability Testing:
- Ask users to transfer money.
- Observe where they struggle.
- Measure task completion.
- Identify confusing instructions.''',
 iv_en='"An Accessibility Audit evaluates whether a product meets accessibility requirements and identifies barriers, while Usability Testing observes real users performing tasks to understand how effectively they can use the product. Both methods complement each other."',
 iv_te='Accessibility Audit ప్రమాణాలతో పోల్చి అడ్డంకులు గుర్తిస్తుంది; Usability Testing నిజమైన users ను గమనిస్తుంది – రెండూ ఒకదానికొకటి పూరకం.'),
]

INTRO_TE = 'ఈ గ్రూప్‌లో Accessibility, Inclusive Design, WCAG Guidelines, Screen Readers, Keyboard Navigation, Color Blindness వంటి ముఖ్యమైన అంశాలను నేర్చుకుందాం. Senior UX Designer, Lead Product Designer, Principal Designer మరియు UX Manager ఇంటర్వ్యూలలో Accessibility గురించి ప్రశ్నలు రావడం సాధారణం. ఈ గ్రూప్ లక్ష్యం: ప్రతి ఒక్కరూ digital products‌ను సులభంగా అర్థం చేసుకోవడానికి, ఉపయోగించడానికి వీలుగా ఎలా డిజైన్ చేయాలో తెలుసుకోవడం.'
REVISION = [(106, 'Accessibility vs Usability', 'Inclusive Access vs Ease of Use'), (107, 'Accessibility vs Inclusive Design', 'Barrier Removal vs Human Diversity'),
 (108, 'Inclusive vs Universal Design', 'Inclusive Process vs Broad Usability'), (109, 'WCAG vs ADA', 'Technical Guidelines vs US Law'),
 (110, 'WCAG A vs AA vs AAA', 'Basic vs Stronger vs Highest'), (111, 'Alt Text vs ARIA Label', 'Image Alternative vs Accessible Name'),
 (112, 'Keyboard vs Screen Reader', 'Keyboard Input vs Assistive Technology'), (113, 'Color Blindness vs Low Vision', 'Color Perception vs Visual Function'),
 (114, 'Responsive vs Accessible Design', 'Screen Adaptation vs Ability Inclusion'), (115, 'Accessibility Audit vs Usability Testing', 'Standards Evaluation vs User Observation')]
PRACTICE_TITLE = 'Practical Interview Quiz – Accessibility Knowledge Check'
PRACTICE_BODY = '''ఈ 5 questions‌కు సమాధానాలు select చేసి మీ understanding‌ను పరీక్షించుకోండి.

1. Which guideline defines technical web accessibility requirements? (ADA / WCAG / ISO 9001)
2. Which WCAG level is a common accessibility target for many digital products? (Level A / Level AA / Level AAA)
3. Which attribute provides an accessible name for a button? (aria-label / alt / margin)
4. Which technique helps users navigate without a mouse? (Color palette / Keyboard Navigation / Illustration)
5. What is the main purpose of an Accessibility Audit? (Improve brand colors / Evaluate accessibility barriers and conformance / Increase animations)

### Answer key · జవాబులు
1. WCAG · 2. Level AA · 3. aria-label · 4. Keyboard Navigation · 5. Evaluate accessibility barriers and conformance'''
