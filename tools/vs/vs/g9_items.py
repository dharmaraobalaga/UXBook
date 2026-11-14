# Group 9 – Product Design & Development (Q116–Q130), assembled from Generate_UX_Vs_Questions_9.pdf.
# Telugu explanations/examples, English definitions, tables, examples and interview answers = PDF text.
# tbl_te, iv_te, ex_en for Telugu-only examples, and Telugu versions of English-only examples = written by Claude.
# Diagrams (assets/images/vs/g9-*.svg) are redrawn by Claude from the PDF's illustrations (tools/vs/figs_g9.py).

def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

ITEMS = [
dict(n=116, A='Product Design', B='UX Design', q_te='Product Design మరియు UX Design మధ్య తేడా ఏమిటి?',
 te='''Product Design:

ఒక digital product‌ను business goals, user needs, technology constraints ఆధారంగా end-to-endగా రూపొందించే విస్తృతమైన discipline.
ఇందులో UX Research, UX Design, UI Design, Product Strategy, Interaction Design, Business Alignment ఉంటాయి.

UX Design:

యూజర్ అవసరాలు, ప్రవర్తన, సమస్యలను అర్థం చేసుకొని usable, accessible, meaningful experiences రూపొందించడం.''',
 defs=['Product Design: Product Design is a holistic discipline that combines user experience, business objectives, and technical feasibility to create successful products.',
       'UX Design: UX Design focuses on understanding user needs and creating effective, efficient, and satisfying user experiences.'],
 hdr=['Product Design', 'UX Design'],
 rows=[['Broader product discipline', 'User experience discipline'], ['User + Business + Technology', 'User needs and usability'], ['Product strategy and execution', 'Research, flows and interactions'], ['End-to-end product thinking', 'Experience-focused problem-solving'], ['Business outcomes', 'User experience outcomes']],
 tbl_te=[['విస్తృత product discipline','User experience discipline'],['User + Business + Technology','User అవసరాలు, usability'],['Product strategy, అమలు','Research, flows, interactions'],['End-to-end product ఆలోచన','Experience పై దృష్టి పెట్టిన సమస్య పరిష్కారం'],['Business ఫలితాలు','User experience ఫలితాలు']],
 ex_title='Banking App',
 ex_te='''Product Designer:
- Customer needs అర్థం చేసుకోవడం.
- Business goals గుర్తించడం.
- Money transfer feature scope నిర్ణయించడం.
- UX/UI design మరియు development teams‌తో కలిసి పని చేయడం.

UX Designer:
- Money transfer user journey.
- User flows.
- Wireframes.
- Usability testing.
- Interaction improvements.''',
 ex_en='''Product Designer:
- Understands customer needs.
- Identifies business goals.
- Decides the scope of the money-transfer feature.
- Works with the UX/UI design and development teams.

UX Designer:
- Money transfer user journey.
- User flows.
- Wireframes.
- Usability testing.
- Interaction improvements.''',
 iv_en='"Product Design takes a holistic approach by balancing user needs, business goals, and technical feasibility. UX Design focuses specifically on creating effective and meaningful user experiences. UX is a critical part of Product Design."',
 iv_te='Product Design user, business, technology మూడింటినీ సమతుల్యం చేస్తుంది; UX Design user experience పై దృష్టి పెడుతుంది – UX, Product Design లో కీలక భాగం.'),

dict(n=117, A='Product Manager', B='Product Designer', q_te='Product Manager మరియు Product Designer మధ్య తేడా ఏమిటి?',
 te='''Product Manager (PM):

Product ఏమి నిర్మించాలి, ఎందుకు నిర్మించాలి, ఎప్పుడు విడుదల చేయాలి అనే అంశాలను business strategy, customer needs, market opportunities ఆధారంగా నిర్ణయిస్తారు.

Product Designer:

Product‌ను యూజర్లు ఎలా ఉపయోగించాలి, వారి సమస్యలను ఎలా పరిష్కరించాలి, experience ఎలా ఉండాలి అనే అంశాలను design చేస్తారు.''',
 defs=['Product Manager: A Product Manager defines product strategy, prioritizes opportunities, and aligns stakeholders to deliver business and customer value.',
       'Product Designer: A Product Designer translates user needs and product requirements into usable, accessible, and valuable experiences.'],
 hdr=['Product Manager', 'Product Designer'],
 rows=[['What and Why', 'How the experience works'], ['Product strategy', 'Experience strategy'], ['Roadmap & priorities', 'User flows & interaction'], ['Business metrics', 'Usability & experience metrics'], ['Stakeholder alignment', 'Design and user alignment']],
 tbl_te=[['ఏమిటి, ఎందుకు','Experience ఎలా పనిచేస్తుంది'],['Product strategy','Experience strategy'],['Roadmap, ప్రాధాన్యతలు','User flows, interaction'],['Business metrics','Usability, experience metrics'],['Stakeholders ఏకాభిప్రాయం','Design, users తో ఏకాభిప్రాయం']],
 ex_title='E-commerce App',
 ex_te='''Product Manager: Cart abandonment తగ్గించడానికి checkout improvements అవసరమని నిర్ణయిస్తారు.

Product Designer:
- Checkout flow analyze చేస్తారు.
- User pain points identify చేస్తారు.
- Simplified checkout design చేస్తారు.
- Prototype test చేస్తారు.''',
 ex_en='''Product Manager: decides that checkout improvements are needed to reduce cart abandonment.

Product Designer:
- Analyses the checkout flow.
- Identifies user pain points.
- Designs a simplified checkout.
- Tests the prototype.''',
 iv_en='"A Product Manager focuses on product strategy, priorities, and business outcomes, while a Product Designer focuses on translating user and business needs into effective product experiences. Both collaborate closely to deliver customer value."',
 iv_te='PM strategy, ప్రాధాన్యతలు, business ఫలితాలపై; Product Designer ఆ అవసరాలను మంచి experience గా మార్చడంపై – ఇద్దరూ కలిసి customer value అందిస్తారు.'),

dict(n=118, A='Product Discovery', B='Product Delivery', q_te='Product Discovery మరియు Product Delivery మధ్య తేడా ఏమిటి?',
 te='''Product Discovery:

ఏ సమస్యను పరిష్కరించాలి, ఎవరికి పరిష్కరించాలి, ఏ solution ఎక్కువ విలువ ఇస్తుంది అనే విషయాలను research మరియు experimentation ద్వారా తెలుసుకోవడం.

Product Delivery:

Validated solution‌ను design, development, testing ద్వారా working product‌గా తయారు చేసి users‌కు అందించడం.

''' + fig('g9-product-workflow', 'Product workflow: Discovery (Research, Problem Definition, Ideation, Validation), Delivery (Design, Development, QA, Release), Continuous Learning (Analytics, Feedback, Improvements)', 'Typical Product Workflow – Discovery → Delivery → Continuous Learning, మళ్లీ Discovery కు.', 'Typical product workflow: Discovery → Delivery → Continuous Learning, feeding back into Discovery.'),
 defs=['Product Discovery: Product Discovery identifies the right problems and validates potential solutions before significant development investment.',
       'Product Delivery: Product Delivery is the process of building, testing, and releasing a product or feature.',
       'Typical product workflow: Discovery (Research → Problem Definition → Ideation → Validation) → Delivery (Design → Development → QA → Release) → Continuous Learning (Analytics → Feedback → Improvements).'],
 hdr=['Product Discovery', 'Product Delivery'],
 rows=[['Find the right problem', 'Build the right solution'], ['Research & validation', 'Development & testing'], ['Prototypes & experiments', 'Working product'], ['Reduce uncertainty', 'Deliver product value'], ['Learn and decide', 'Build and release']],
 tbl_te=[['సరైన సమస్యను కనుగొనడం','సరైన solution నిర్మించడం'],['Research, validation','Development, testing'],['Prototypes, experiments','Working product'],['అనిశ్చితిని తగ్గించడం','Product విలువ అందించడం'],['నేర్చుకుని నిర్ణయించడం','నిర్మించి విడుదల చేయడం']],
 ex_title='Money Transfer Feature',
 ex_te='''Discovery:
- Users‌కు money transfer‌లో ఏ సమస్యలు ఉన్నాయి?
- User interviews నిర్వహించడం.
- Competitor analysis.
- Prototype testing.

Delivery:
- Final UI design.
- Developer handoff.
- API integration.
- QA testing.
- Production release.''',
 ex_en='''Discovery:
- What problems do users have with money transfer?
- Conducting user interviews.
- Competitor analysis.
- Prototype testing.

Delivery:
- Final UI design.
- Developer handoff.
- API integration.
- QA testing.
- Production release.''',
 iv_en='"Product Discovery helps teams identify and validate the right problems and solutions, while Product Delivery focuses on building and releasing those validated solutions. Both activities are continuous and often overlap in modern product teams."',
 iv_te='Discovery సరైన సమస్య, solution ను validate చేస్తుంది; Delivery వాటిని నిర్మించి విడుదల చేస్తుంది – ఆధునిక teams లో రెండూ నిరంతరం, కలిసి జరుగుతాయి.'),

dict(n=119, A='MVP', B='Prototype', q_te='MVP మరియు Prototype మధ్య తేడా ఏమిటి?',
 te='''MVP – Minimum Viable Product:

ఒక product యొక్క core user problem‌ను పరిష్కరించడానికి అవసరమైన కనీస ముఖ్యమైన functionalityతో users‌కు release చేసే working product.

Prototype:

ఒక idea లేదా design ఎలా పనిచేస్తుందో simulate చేసి, interactions మరియు assumptions test చేయడానికి రూపొందించే model.''',
 defs=['MVP: An MVP is the smallest usable version of a product that delivers core value and enables teams to learn from real users.',
       'Prototype: A Prototype is an early representation of a product used to explore, demonstrate, and test concepts before full development.'],
 hdr=['MVP', 'Prototype'],
 rows=[['Working product', 'Simulated product model'], ['Delivers core user value', 'Tests design assumptions'], ['Real users can use it', 'Test participants interact with it'], ['May be released to market', 'Usually used before release'], ['Real usage feedback', 'Concept and interaction feedback']],
 tbl_te=[['పనిచేసే product','Simulate చేసిన product model'],['ముఖ్యమైన user విలువ అందిస్తుంది','Design assumptions ను test చేస్తుంది'],['నిజమైన users ఉపయోగించగలరు','Test participants ఉపయోగిస్తారు'],['Market కు విడుదల కావచ్చు','సాధారణంగా విడుదలకు ముందే'],['నిజమైన వాడకం feedback','Concept, interaction feedback']],
 ex_title='Food Delivery App',
 ex_te=fig('g9-prototype-mvp', 'Prototype phone with clickable Restaurants, Menu, Cart, Checkout screens next to an MVP phone with real listings, ordering, payment and tracking', 'Prototype – simulate చేసిన screens; MVP – నిజమైన users ఉపయోగించే పనిచేసే core product.', 'Prototype: simulated screens. MVP: a working core product used by real users.') + '''

Prototype:
- Restaurant selection.
- Menu browsing.
- Cart interaction.
- Simulated checkout.

MVP:
- నిజమైన restaurant listings.
- నిజంగా order చేయడం.
- Payment integration.
- Basic order tracking.''',
 ex_en=fig('g9-prototype-mvp', 'Prototype vs MVP phones', '', 'Prototype: simulated screens. MVP: a working core product used by real users.') + '''

Prototype:
- Restaurant selection.
- Menu browsing.
- Cart interaction.
- Simulated checkout.

MVP:
- Real restaurant listings.
- Actual ordering.
- Payment integration.
- Basic order tracking.''',
 iv_en='"A Prototype is used to test and validate an idea or interaction, whereas an MVP is a working product with essential functionality that delivers real value to users and helps validate the product in the market."',
 iv_te='Prototype idea లేదా interaction ను test చేయడానికి; MVP నిజమైన users కు విలువ ఇచ్చే, market లో validate చేసే పనిచేసే product.'),

dict(n=120, A='MVP', B='MLP (Minimum Lovable Product)', q_te='MVP మరియు MLP (Minimum Lovable Product) మధ్య తేడా ఏమిటి?',
 te='''MVP – Minimum Viable Product:

Core problem‌ను పరిష్కరించడానికి అవసరమైన minimum functionality అందించడం.

MLP – Minimum Lovable Product:

Core functionalityతో పాటు users‌కు మంచి experience, emotional connection, satisfaction కలిగించే minimum product experience‌ను అందించడం.''',
 defs=['MVP: The minimum product that delivers essential value.',
       'MLP: The minimum product designed to deliver essential value along with a delightful and memorable user experience.'],
 hdr=['MVP', 'MLP'],
 rows=[['Minimum viable functionality', 'Minimum lovable experience'], ['Focus on core value', 'Focus on value + delight'], ['Validate assumptions', 'Build satisfaction and affinity'], ['Basic but usable', 'Polished and engaging'], ['Learn from usage', 'Encourage engagement and loyalty']],
 tbl_te=[['కనీస viable functionality','కనీస lovable experience'],['ముఖ్య విలువపై దృష్టి','విలువ + ఆనందంపై దృష్టి'],['Assumptions validate చేయడం','సంతృప్తి, అనుబంధం పెంచడం'],['సాధారణం కానీ ఉపయోగించగలిగేది','మెరుగుపెట్టిన, ఆకట్టుకునేది'],['వాడకం నుండి నేర్చుకోవడం','Engagement, loyalty ప్రోత్సహించడం']],
 ex_title='Learning App',
 ex_te='''MVP:
- User registration.
- Course listing.
- Video lessons.
- Basic progress tracking.

MLP:
- Personalized learning journey.
- Friendly feedback.
- Progress celebrations.
- Clear learning milestones.
- Smooth and accessible interface.''',
 ex_en='''MVP:
- User registration.
- Course listing.
- Video lessons.
- Basic progress tracking.

MLP:
- Personalized learning journey.
- Friendly feedback.
- Progress celebrations.
- Clear learning milestones.
- Smooth and accessible interface.''',
 iv_en='"An MVP focuses on delivering the minimum functionality required to validate a product idea, while an MLP adds thoughtful experience elements that make the product more engaging and enjoyable. The goal is to balance essential functionality with user satisfaction."',
 iv_te='MVP idea ను validate చేసే కనీస functionality; MLP దానికి ఆకట్టుకునే experience జోడిస్తుంది – ముఖ్య functionality మరియు user సంతృప్తి మధ్య సమతుల్యం లక్ష్యం.'),

dict(n=121, A='Agile', B='Waterfall', q_te='Agile మరియు Waterfall మధ్య తేడా ఏమిటి?',
 te='''Agile:

Product‌ను చిన్న iterations‌లో develop చేస్తూ, continuous feedback ఆధారంగా improvements చేయడం.

Waterfall:

Project‌ను sequential phases‌గా విభజించి, ఒక phase పూర్తయిన తర్వాత తదుపరి phase‌కు వెళ్లే development approach.''',
 defs=['Agile: Agile is an iterative approach to software development that emphasizes collaboration, adaptability, and continuous delivery of value.',
       'Waterfall: Waterfall is a sequential development approach where each project phase is typically completed before the next begins.'],
 hdr=['Agile', 'Waterfall'],
 rows=[['Iterative', 'Sequential'], ['Continuous feedback', 'Feedback often comes later'], ['Flexible scope', 'Scope generally defined earlier'], ['Frequent releases', 'Typically phase-based delivery'], ['Adaptable to changes', 'Changes can be more costly']],
 tbl_te=[['పునరావృత (iterative)','వరుస క్రమం (sequential)'],['నిరంతర feedback','Feedback తరచుగా ఆలస్యంగా'],['సర్దుబాటు చేయగల scope','Scope సాధారణంగా ముందే నిర్ణయం'],['తరచుగా releases','సాధారణంగా phase ఆధారిత delivery'],['మార్పులకు సులభంగా సర్దుకుంటుంది','మార్పులు ఎక్కువ ఖర్చు కావచ్చు']],
 ex_title='Agile vs Waterfall',
 ex_te=fig('g9-agile-waterfall', 'Agile cycle of Plan, Design, Build, Test, Release, Feedback around a sprint, next to Waterfall steps Requirements, Design, Development, Testing, Release', 'Agile – ప్రతి sprint లో పునరావృతమయ్యే cycle; Waterfall – ఒక phase తర్వాత మరొకటి.', 'Agile repeats a cycle every sprint; Waterfall moves through one phase after another.') + '''

Agile:
- Sprint 1: Login and registration.
- Sprint 2: Dashboard.
- Sprint 3: Payments.
- Feedback ఆధారంగా continuous improvements.

Waterfall:
- Requirements పూర్తిగా document చేయడం.
- Design phase.
- Development phase.
- Testing phase.
- Final release.''',
 ex_en=fig('g9-agile-waterfall', 'Agile cycle vs Waterfall phases', '', 'Agile repeats a cycle every sprint; Waterfall moves through one phase after another.') + '''

Agile:
- Sprint 1: Login and registration.
- Sprint 2: Dashboard.
- Sprint 3: Payments.
- Continuous improvements based on feedback.

Waterfall:
- Fully documenting the requirements.
- Design phase.
- Development phase.
- Testing phase.
- Final release.''',
 iv_en='"Agile supports iterative development, continuous feedback, and flexibility, while Waterfall follows a sequential process with predefined phases. Agile is useful when requirements evolve, whereas Waterfall can work well when requirements and delivery constraints are clearly defined."',
 iv_te='Requirements మారుతుంటే Agile; requirements, పరిమితులు స్పష్టంగా ఉంటే Waterfall బాగా పనిచేస్తుంది.'),

dict(n=122, A='Scrum', B='Kanban', q_te='Scrum మరియు Kanban మధ్య తేడా ఏమిటి?',
 te='''Scrum:

Agile framework. ఇందులో work‌ను fixed-length iterations అయిన Sprints‌లో organize చేస్తారు.

Common Scrum roles:
- Product Owner
- Scrum Master
- Developers

Common events:
- Sprint Planning
- Daily Scrum
- Sprint Review
- Sprint Retrospective

Kanban:

Work‌ను visual board ద్వారా manage చేస్తూ, workflow‌లో bottlenecks తగ్గించి continuous flow‌ను మెరుగుపరిచే method.''',
 defs=['Scrum: Scrum is an Agile framework that organizes work into time-boxed Sprints with defined accountabilities, events, and artifacts. Roles: Product Owner, Scrum Master, Developers. Events: Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.',
       'Kanban: Kanban is a method for managing and improving the flow of work through visualization and work-in-progress limits.'],
 hdr=['Scrum', 'Kanban'],
 rows=[['Fixed-length Sprints', 'Continuous flow'], ['Sprint planning', 'Continuous prioritization'], ['Defined accountabilities', 'No mandatory Scrum roles'], ['Sprint commitment', 'Work-in-progress limits'], ['Sprint review & retrospective', 'Continuous flow improvement']],
 tbl_te=[['నిర్ణీత కాల Sprints','నిరంతర ప్రవాహం'],['Sprint planning','నిరంతర ప్రాధాన్యత నిర్ణయం'],['నిర్వచించిన బాధ్యతలు','తప్పనిసరి Scrum roles లేవు'],['Sprint commitment','Work-in-progress పరిమితులు'],['Sprint review, retrospective','నిరంతర flow మెరుగుదల']],
 ex_title='Design Team',
 ex_te=fig('g9-scrum-kanban', 'Scrum sprint events next to a Kanban board with To Do, In Progress, Review and Done columns and WIP limits', 'Scrum – time-boxed sprint events; Kanban – WIP limits తో నిరంతర work flow.', 'Scrum: time-boxed sprint events. Kanban: continuous flow with WIP limits.') + '''

Scrum:
- రెండు వారాల design sprint.
- Sprint planning.
- Daily stand-up.
- Sprint review.

Kanban:
- To Do → In Progress → Review → Done.
- Priority మరియు అందుబాటులో ఉన్న capacity ఆధారంగా designers tasks ఎంచుకుంటారు.
- Work-in-progress limits bottlenecks ను తగ్గిస్తాయి.''',
 ex_en=fig('g9-scrum-kanban', 'Scrum events vs Kanban board', '', 'Scrum: time-boxed sprint events. Kanban: continuous flow with WIP limits.') + '''

Scrum:
- Two-week design sprint.
- Sprint planning.
- Daily stand-up.
- Sprint review.

Kanban:
- To Do → In Progress → Review → Done.
- Designers pick tasks based on priority and available capacity.
- Work-in-progress limits reduce bottlenecks.''',
 iv_en='"Scrum organizes work into fixed-length Sprints with defined accountabilities and events, whereas Kanban focuses on continuous workflow management, visualization, and limiting work in progress. Both help teams improve delivery."',
 iv_te='Scrum నిర్ణీత కాల Sprints లో పని; Kanban board, WIP limits తో నిరంతర ప్రవాహం – రెండూ delivery ని మెరుగుపరుస్తాయి.'),

dict(n=123, A='Design Sprint', B='Design Thinking', q_te='Design Sprint మరియు Design Thinking మధ్య తేడా ఏమిటి?',
 te='''Design Sprint:

ఒక specific product challenge‌ను short, time-boxed process ద్వారా understand చేసి, prototype తయారు చేసి users‌తో test చేసే structured method.
Google Ventures ఐదు రోజుల Design Sprint format‌ను ప్రాచుర్యంలోకి తెచ్చింది.

Design Thinking:

Human-centered problem-solving approach. ఇది users అవసరాలను అర్థం చేసుకొని, ideas generate చేసి, solutions test చేస్తూ problems‌ను పరిష్కరించడంపై దృష్టి పెడుతుంది.

Common five stages:
1. Empathize
2. Define
3. Ideate
4. Prototype
5. Test''',
 defs=['Design Sprint: A Design Sprint is a time-boxed process for understanding a challenge, exploring solutions, prototyping, and testing with users. Google Ventures popularized a five-day Design Sprint format.',
       'Design Thinking: Design Thinking is a human-centered, iterative approach to solving problems through empathy, ideation, experimentation, and testing. Common stages: Empathize, Define, Ideate, Prototype, Test.'],
 hdr=['Design Sprint', 'Design Thinking'],
 rows=[['Time-boxed method', 'Broader methodology'], ['Often five-day format', 'No fixed duration'], ['Focuses on specific challenge', 'Can address broad problems'], ['Structured activities', 'Iterative problem-solving'], ['Prototype and test quickly', 'Understand, ideate and iterate']],
 tbl_te=[['నిర్ణీత కాల పద్ధతి','విస్తృత methodology'],['తరచుగా ఐదు రోజుల format','నిర్ణీత వ్యవధి లేదు'],['ఒక నిర్దిష్ట challenge పై దృష్టి','విస్తృత సమస్యలను పరిష్కరించగలదు'],['నిర్మాణాత్మక activities','పునరావృత సమస్య పరిష్కారం'],['త్వరగా prototype, test','అర్థం చేసుకోవడం, ideate, iterate']],
 ex_title='Banking App',
 ex_te=fig('g9-sprint-thinking', 'Design Sprint days Monday Map to Friday Test, and Design Thinking stages Empathize, Define, Ideate, Prototype, Test with an iteration loop', 'Design Sprint – ఐదు రోజుల format; Design Thinking – ఏ దశకైనా తిరిగి వెళ్లగల ఐదు దశలు.', 'Design Sprint: a five-day format. Design Thinking: five stages you can loop back through.') + '''

Design Thinking:
- Users money transfers ను ఎందుకు మధ్యలో వదిలేస్తున్నారో అర్థం చేసుకోవడం.
- ముఖ్యమైన problems ను define చేయడం.
- Solutions explore చేయడం.
- Prototype చేసి test చేయడం.

Design Sprint:
- ఒక నిర్దిష్ట money transfer challenge పై focused workshop నిర్వహించడం.
- వేర్వేరు solutions sketch చేయడం.
- ఒక solution ఎంచుకోవడం.
- Prototype తయారు చేయడం.
- తక్కువ సమయంలో users తో test చేయడం.''',
 ex_en=fig('g9-sprint-thinking', 'Design Sprint days vs Design Thinking stages', '', 'Design Sprint: a five-day format. Design Thinking: five stages you can loop back through.') + '''

Design Thinking:
- Understand why users abandon money transfers.
- Define key problems.
- Explore solutions.
- Prototype and test.

Design Sprint:
- Conduct a focused workshop around a specific money transfer challenge.
- Sketch alternative solutions.
- Select one solution.
- Build a prototype.
- Test with users within a short period.''',
 iv_en='"Design Thinking is a broader human-centered problem-solving approach, while a Design Sprint is a structured, time-boxed method that helps teams quickly prototype and test a solution to a specific challenge."',
 iv_te='Design Thinking విస్తృత human-centered విధానం; Design Sprint ఒక నిర్దిష్ట challenge కు త్వరగా prototype చేసి test చేసే time-boxed పద్ధతి.'),

dict(n=124, A='Frontend', B='Backend', q_te='Frontend మరియు Backend మధ్య తేడా ఏమిటి?',
 te='''Frontend Development:

యూజర్‌కు కనిపించే interface‌ను develop చేయడం.

ఉదాహరణలు:
- Buttons
- Forms
- Navigation
- Responsive layouts
- Animations

Backend Development:

Server-side logic, databases, APIs, authentication, business rules వంటి అంశాలను develop చేయడం.

''' + fig('g9-frontend-backend', 'Client side with browser and presentation layer exchanging API requests and JSON responses with a server side of business logic, data layer and authentication services', 'Frontend (client side) API request పంపుతుంది; Backend (server side) logic, data ద్వారా JSON response ఇస్తుంది.', 'The frontend (client side) sends API requests; the backend (server side) responds with JSON from its logic and data.'),
 defs=['Frontend Development: Frontend Development focuses on implementing the user-facing interface and interactions of a digital product. Examples: buttons, forms, navigation, responsive layouts, animations.',
       'Backend Development: Backend Development handles server-side processing, data management, business logic, and communication with other systems.'],
 hdr=['Frontend', 'Backend'],
 rows=[['User-facing', 'Server-side'], ['UI and interactions', 'Business logic'], ['HTML, CSS, JavaScript', 'Server languages and databases'], ['Browser / app interface', 'Server and data layer'], ['Visual implementation', 'Data and system operations']],
 tbl_te=[['User కు కనిపించేది','Server వైపు'],['UI, interactions','Business logic'],['HTML, CSS, JavaScript','Server languages, databases'],['Browser / app interface','Server, data layer'],['దృశ్య అమలు','Data, system operations']],
 ex_title='Login Screen',
 ex_te='''Frontend:
- Username field.
- Password field.
- Login button.
- Error message design.

Backend:
- Credentials validate చేయడం.
- User identity verify చేయడం.
- Database కు connect అవ్వడం.
- Authentication response generate చేయడం.''',
 ex_en='''Frontend:
- Username field.
- Password field.
- Login button.
- Error message design.

Backend:
- Validate credentials.
- Verify user identity.
- Connect to database.
- Generate authentication response.''',
 iv_en='"Frontend development implements the user-facing interface and interactions, while Backend development manages server-side logic, databases, authentication, and APIs. Designers collaborate closely with frontend developers to ensure accurate design implementation."',
 iv_te='Frontend user కు కనిపించే interface; Backend server logic, databases, APIs – design సరిగ్గా అమలవ్వడానికి designers frontend developers తో దగ్గరగా పనిచేస్తారు.'),

dict(n=125, A='API', B='SDK', q_te='API మరియు SDK మధ్య తేడా ఏమిటి?',
 te='''API – Application Programming Interface:

రెండు software systems మధ్య communication చేయడానికి ఉపయోగించే defined interface లేదా set of rules.

SDK – Software Development Kit:

ఒక platform లేదా service కోసం applications develop చేయడానికి అవసరమైన tools, libraries, documentation, and APIs కలిగిన development package.''',
 defs=['API: An API defines how software applications communicate and exchange data or functionality.',
       'SDK: An SDK is a collection of tools, libraries, documentation, and resources that helps developers build applications for a specific platform or service.'],
 hdr=['API', 'SDK'],
 rows=[['Communication interface', 'Development toolkit'], ['Defines how to interact', 'Provides tools to build'], ['Endpoints and methods', 'Libraries, tools, APIs'], ['Can be used independently', 'May include multiple APIs'], ['Connects systems', 'Simplifies development']],
 tbl_te=[['Communication interface','Development toolkit'],['ఎలా interact చేయాలో నిర్వచిస్తుంది','నిర్మించడానికి tools ఇస్తుంది'],['Endpoints, methods','Libraries, tools, APIs'],['స్వతంత్రంగా ఉపయోగించవచ్చు','అనేక APIs ఉండవచ్చు'],['Systems ను కలుపుతుంది','Development ను సులభం చేస్తుంది']],
 ex_title='Payment Integration',
 ex_te='''API:
- App payment request‌ను payment gateway‌కు పంపుతుంది.
- Payment status response అందుకుంటుంది.

SDK:
- Payment gateway SDK ఉపయోగించి developers payment integration‌ను సులభంగా implement చేస్తారు.
- SDKలో API wrappers, libraries, documentation ఉండవచ్చు.''',
 ex_en='''API:
- The app sends the payment request to the payment gateway.
- It receives the payment status response.

SDK:
- Using the payment gateway's SDK, developers implement the payment integration easily.
- The SDK may include API wrappers, libraries and documentation.''',
 iv_en='"An API defines how different software systems communicate, while an SDK provides a broader toolkit for developers, often including APIs, libraries, and documentation to build applications more efficiently."',
 iv_te='API systems ఎలా మాట్లాడుకోవాలో నిర్వచిస్తుంది; SDK APIs, libraries, documentation కలిగిన విస్తృత toolkit.'),

dict(n=126, A='Functional Requirements', B='Non-functional Requirements', q_te='Functional Requirements మరియు Non-functional Requirements మధ్య తేడా ఏమిటి?',
 te='''Functional Requirements:

System ఏమి చేయాలి అనే functionality‌ను వివరిస్తాయి.

ఉదాహరణలు:
- User login.
- Password reset.
- Money transfer.
- Search products.
- Generate reports.

Non-functional Requirements:

System ఎలా పనిచేయాలి, దాని performance, security, reliability, accessibility వంటి quality attributes‌ను వివరిస్తాయి.''',
 defs=['Functional Requirements: Functional Requirements describe the specific features, behaviors, and operations a system must perform. Examples: user login, password reset, money transfer, search products, generate reports.',
       'Non-functional Requirements: Non-functional Requirements define quality attributes and constraints such as performance, security, reliability, and accessibility.'],
 hdr=['Functional Requirements', 'Non-functional Requirements'],
 rows=[['What system does', 'How system performs'], ['Features and behavior', 'Quality attributes'], ['Login and payments', 'Speed and security'], ['Search and filters', 'Reliability and scalability'], ['User actions', 'Performance constraints']],
 tbl_te=[['System ఏమి చేస్తుంది','System ఎంత బాగా పనిచేస్తుంది'],['Features, ప్రవర్తన','నాణ్యత లక్షణాలు'],['Login, payments','వేగం, భద్రత'],['Search, filters','విశ్వసనీయత, scalability'],['User చర్యలు','Performance పరిమితులు']],
 ex_title='E-commerce App',
 ex_te='''Functional:
- User products ను cart కు add చేయగలరు.
- User coupon apply చేయగలరు.
- User order place చేయగలరు.

Non-functional:
- Product page అంగీకరించిన performance targets లోపు load అవుతుంది.
- Payment data సురక్షితంగా handle చేయబడుతుంది.
- Interface accessibility requirements కు మద్దతు ఇస్తుంది.
- System ఆశించిన traffic ను handle చేస్తుంది.''',
 ex_en='''Functional:
- User can add products to cart.
- User can apply coupon.
- User can place an order.

Non-functional:
- Product page loads within agreed performance targets.
- Payment data is securely handled.
- Interface supports accessibility requirements.
- System handles expected traffic.''',
 iv_en='"Functional Requirements define what a system should do, such as login, search, and payments. Non-functional Requirements define how well the system should perform, including security, performance, reliability, and accessibility."',
 iv_te='Functional – system ఏమి చేయాలి; Non-functional – ఎంత బాగా (security, performance, reliability, accessibility) చేయాలి.'),

dict(n=127, A='User Story', B='Use Case', q_te='User Story మరియు Use Case మధ్య తేడా ఏమిటి?',
 te='''User Story:

ఒక user‌కు ఏ functionality ఎందుకు అవసరమో simple format‌లో వివరిస్తుంది.

Common format:
"As a [user], I want [goal], so that [benefit]."

Use Case:

ఒక user మరియు system మధ్య జరిగే interaction‌ను step-by-stepగా వివరిస్తుంది.''',
 defs=['User Story: A User Story is a concise description of a feature from the perspective of the user and the value they expect. Format: "As a [user], I want [goal], so that [benefit]."',
       'Use Case: A Use Case describes how an actor interacts with a system to achieve a specific goal, including possible flows and alternative scenarios.'],
 hdr=['User Story', 'Use Case'],
 rows=[['Short requirement', 'Detailed interaction scenario'], ['User need and value', 'Actor-system interaction'], ['Simple format', 'Main and alternative flows'], ['Agile backlog', 'System behavior documentation']],
 tbl_te=[['చిన్న requirement','వివరమైన interaction సన్నివేశం'],['User అవసరం, విలువ','Actor-system interaction'],['సరళమైన format','Main, alternative flows'],['Agile backlog','System ప్రవర్తన documentation']],
 ex_title='Password Reset',
 ex_te='''User Story:
"As a registered user, I want to reset my password so that I can regain access to my account."
(నమోదైన user గా, నా account ను మళ్లీ యాక్సెస్ చేయడానికి password reset చేయాలనుకుంటున్నాను.)

Use Case:
1. User Forgot Password ఎంచుకుంటారు.
2. System నమోదైన email అడుగుతుంది.
3. User email నమోదు చేస్తారు.
4. System verification link లేదా OTP పంపుతుంది.
5. User identity verify చేసుకుంటారు.
6. User కొత్త password సృష్టిస్తారు.
7. System విజయవంతమైన reset ను నిర్ధారిస్తుంది.''',
 ex_en='''User Story:
"As a registered user, I want to reset my password so that I can regain access to my account."

Use Case:
1. User selects Forgot Password.
2. System requests registered email.
3. User enters email.
4. System sends verification link or OTP.
5. User verifies identity.
6. User creates a new password.
7. System confirms successful reset.''',
 iv_en='"A User Story describes a feature from the user\'s perspective and highlights its value, while a Use Case provides detailed steps explaining how the user and system interact to achieve a goal."',
 iv_te='User Story user దృష్టి నుండి feature, దాని విలువ; Use Case user–system interaction ను step-by-step వివరిస్తుంది.'),

dict(n=128, A='Acceptance Criteria', B='Definition of Done', q_te='Acceptance Criteria మరియు Definition of Done మధ్య తేడా ఏమిటి?',
 te='''Acceptance Criteria:

ఒక specific feature లేదా user story ఎప్పుడు acceptable‌గా పరిగణించాలో తెలిపే conditions.

Definition of Done (DoD):

ఒక task, feature, లేదా increment పూర్తయిందని team అంగీకరించడానికి వర్తించే shared quality standards.''',
 defs=['Acceptance Criteria: Acceptance Criteria are specific conditions that a feature or user story must satisfy to be accepted.',
       'Definition of Done: Definition of Done is a shared set of quality criteria that work must satisfy before it is considered complete.'],
 hdr=['Acceptance Criteria', 'Definition of Done'],
 rows=[['Feature-specific', 'Team-wide quality standard'], ['Defines expected behavior', 'Defines completion quality'], ['Applies to a user story', 'Applies to work meeting DoD'], ['Functional conditions', 'Testing, review, documentation, etc.']],
 tbl_te=[['Feature కు ప్రత్యేకం','Team మొత్తానికి నాణ్యత ప్రమాణం'],['ఆశించిన ప్రవర్తనను నిర్వచిస్తుంది','పూర్తి నాణ్యతను నిర్వచిస్తుంది'],['ఒక user story కు వర్తిస్తుంది','DoD కి లోబడే అన్ని పనులకు వర్తిస్తుంది'],['Functional conditions','Testing, review, documentation మొదలైనవి']],
 ex_title='Login Feature',
 ex_te='''Acceptance Criteria:
- సరైన credentials తో login అవుతుంది.
- తప్పు password ఇస్తే error చూపిస్తుంది.
- Forgot Password link పనిచేస్తుంది.
- ఖాళీ fields కు validation చూపిస్తుంది.

Definition of Done:
- Code review పూర్తయింది.
- అవసరమైన tests pass అయ్యాయి.
- Accessibility checks పూర్తయ్యాయి.
- Design implementation review అయింది.
- అవసరమైన చోట documentation update అయింది.''',
 ex_en='''Acceptance Criteria:
- Valid credentials allow login.
- Invalid password displays an error.
- Forgot Password link works.
- Empty fields show validation.

Definition of Done:
- Code reviewed.
- Required tests passed.
- Accessibility checks completed.
- Design implementation reviewed.
- Documentation updated, where required.''',
 iv_en='"Acceptance Criteria define the specific conditions a feature must satisfy, whereas Definition of Done establishes the shared quality standards required for a deliverable to be considered complete."',
 iv_te='Acceptance Criteria ఒక feature కు ప్రత్యేక షరతులు; Definition of Done పని పూర్తయిందని చెప్పడానికి team మొత్తం పాటించే నాణ్యత ప్రమాణాలు.'),

dict(n=129, A='Design Handoff', B='Developer Handoff', q_te='Design Handoff మరియు Developer Handoff మధ్య తేడా ఏమిటి?',
 te='''ఈ రెండు terms చాలా సందర్భాల్లో interchangeable‌గా వాడతారు. కానీ ఈ guideలో వీటి scope‌ను ఇలా అర్థం చేసుకుందాం.

Design Handoff:

Approved design files, interaction details, assets, responsive behavior, and specifications‌ను implementation team‌కు అందించడం.

Developer Handoff:

Developers‌కు implementation కోసం అవసరమైన design information, technical specifications, component details, edge cases, and assets అందించడం.''',
 defs=['Note: The two terms are often used interchangeably; this guide separates their scope as follows.',  # Claude translation
       'Design Handoff: Design Handoff is the process of transferring approved design specifications, assets, and interaction details to the implementation team.',
       'Developer Handoff: Developer Handoff focuses on providing developers with the technical and design information required to implement the product accurately.'],
 hdr=['Design Handoff', 'Developer Handoff'],
 rows=[['Broad transfer of design information', 'Developer-focused implementation details'], ['Screens and prototypes', 'Specs and component behavior'], ['Design assets', 'Exportable assets and technical details'], ['Interaction documentation', 'States, validations, edge cases'], ['Cross-functional alignment', 'Implementation readiness']],
 tbl_te=[['Design సమాచారాన్ని విస్తృతంగా అందించడం','Developers కోసం implementation వివరాలు'],['Screens, prototypes','Specs, component ప్రవర్తన'],['Design assets','Export చేయగల assets, technical వివరాలు'],['Interaction documentation','States, validations, edge cases'],['Teams మధ్య ఏకాభిప్రాయం','అమలుకు సిద్ధంగా ఉండటం']],
 ex_title='Mobile App',
 ex_te=fig('g9-handoff-redline', 'Mobile recipe screen with pink spacing redlines and notes for typography, spacing grid, button states, loading and error states and asset exports', 'Developer Handoff – spacing, sizes, states, assets వంటి redline specs (ఉదాహరణ).', 'Developer handoff: redline specs for spacing, sizes, states and assets (illustrative).') + '''

Design Handoff:
- Approve అయిన Figma screens.
- User flows.
- Interactive prototype.
- Design system references.

Developer Handoff:
- Component dimensions.
- Spacing, typography values.
- Responsive behavior.
- Button states.
- Error, loading states.
- Asset export వివరాలు.''',
 ex_en=fig('g9-handoff-redline', 'Redline specs on a mobile screen', '', 'Developer handoff: redline specs for spacing, sizes, states and assets (illustrative).') + '''

Design Handoff:
- Approved Figma screens.
- User flows.
- Interactive prototype.
- Design system references.

Developer Handoff:
- Component dimensions.
- Spacing and typography values.
- Responsive behavior.
- Button states.
- Error and loading states.
- Asset export details.''',
 iv_en='"Design Handoff communicates the approved design and interaction specifications to the team, while Developer Handoff provides implementation-ready details such as component behavior, dimensions, assets, states, and responsive rules. The goal is to reduce ambiguity and ensure design fidelity."',
 iv_te='Design Handoff approve అయిన design ను team కు అందిస్తుంది; Developer Handoff అమలుకు సిద్ధమైన వివరాలు ఇస్తుంది – లక్ష్యం: అస్పష్టత తగ్గించి design fidelity నిలపడం.'),

dict(n=130, A='Design QA', B='Product QA', q_te='Design QA మరియు Product QA మధ్య తేడా ఏమిటి?',
 te='''Design QA – Design Quality Assurance:

Developers implement చేసిన interface approved design specifications‌కు ఎంతవరకు match అవుతుందో check చేయడం.

Product QA – Product Quality Assurance:

Product యొక్క functionality, reliability, performance, security, and overall quality‌ను verify చేయడం.''',
 defs=['Design QA: Design QA verifies whether the implemented interface matches the approved design in terms of layout, typography, spacing, colors, components, and interactions.',
       'Product QA: Product QA evaluates whether the product works correctly and meets functional and non-functional quality requirements.'],
 hdr=['Design QA', 'Product QA'],
 rows=[['Visual and interaction accuracy', 'Overall product quality'], ['Design specifications', 'Functional requirements'], ['Typography and spacing', 'Feature behavior'], ['Responsive UI', 'Performance and reliability'], ['Design consistency', 'Product correctness']],
 tbl_te=[['దృశ్య, interaction ఖచ్చితత్వం','మొత్తం product నాణ్యత'],['Design specifications','Functional requirements'],['Typography, spacing','Feature ప్రవర్తన'],['Responsive UI','Performance, విశ్వసనీయత'],['Design స్థిరత్వం','Product సరిగ్గా పనిచేయడం']],
 ex_title='Banking App',
 ex_te='''Design QA:
- Button colors correct‌గా ఉన్నాయా?
- Typography మరియు spacing match అవుతున్నాయా?
- Mobile responsive layout correct‌గా ఉందా?
- Error states design ప్రకారం ఉన్నాయా?

Product QA:
- Login పనిచేస్తుందా?
- Money transfer successful‌గా జరుగుతుందా?
- Invalid transaction handle చేస్తున్నదా?
- Payment data secure‌గా ఉందా?''',
 ex_en='''Design QA:
- Are the button colours correct?
- Do typography and spacing match?
- Is the mobile responsive layout correct?
- Are the error states as designed?

Product QA:
- Does login work?
- Does the money transfer complete successfully?
- Are invalid transactions handled?
- Is payment data secure?''',
 iv_en='"Design QA focuses on visual consistency and interaction fidelity between the approved designs and implemented interface. Product QA validates the overall functionality, reliability, performance, and quality of the product. Both are necessary before release."',
 iv_te='Design QA design కు అమలుకు మధ్య దృశ్య ఖచ్చితత్వం; Product QA మొత్తం functionality, నాణ్యత – release కు ముందు రెండూ అవసరం.'),
]

INTRO_TE = 'ఈ గ్రూప్‌లో Product Design, Product Management, Agile Development, MVP, Scrum, Technical Concepts, Design Handoff వంటి ముఖ్యమైన అంశాలను నేర్చుకుందాం. Senior UX Designer, Lead Product Designer, Principal Designer, Product Design Manager ఇంటర్వ్యూలలో ఈ concepts చాలా ముఖ్యమైనవి. ముఖ్యంగా Product Managers, Developers, QA Teams‌తో ఎలా collaborate చేయాలో అర్థం చేసుకోవడానికి ఇవి ఉపయోగపడతాయి.'
REVISION = [(116, 'Product Design vs UX Design', 'Holistic Product vs User Experience'), (117, 'Product Manager vs Product Designer', 'Strategy & Priorities vs Experience'),
 (118, 'Discovery vs Delivery', 'Validate vs Build & Release'), (119, 'MVP vs Prototype', 'Working Product vs Simulation'),
 (120, 'MVP vs MLP', 'Minimum Value vs Value + Delight'), (121, 'Agile vs Waterfall', 'Iterative vs Sequential'),
 (122, 'Scrum vs Kanban', 'Time-boxed vs Continuous Flow'), (123, 'Design Sprint vs Design Thinking', 'Time-boxed Method vs Broader Approach'),
 (124, 'Frontend vs Backend', 'User Interface vs Server Logic'), (125, 'API vs SDK', 'Communication Interface vs Toolkit'),
 (126, 'Functional vs Non-functional', 'What vs How Well'), (127, 'User Story vs Use Case', 'User Need vs Detailed Interaction'),
 (128, 'Acceptance Criteria vs DoD', 'Feature Conditions vs Quality Standard'), (129, 'Design vs Developer Handoff', 'Design Communication vs Implementation Details'),
 (130, 'Design QA vs Product QA', 'Design Fidelity vs Product Quality')]
PRACTICE_TITLE = 'Practical Interview Quiz – Product Design Knowledge Check'
PRACTICE_BODY = '''ఈ 5 questions ద్వారా Product Design & Development concepts‌ను పరీక్షించుకోండి.

1. Which activity helps a team validate whether it is solving the right user problem? (Product Delivery / Product Discovery / Product QA)
2. Which is a working product with essential functionality? (Prototype / MVP / Wireframe)
3. Which method uses time-boxed Sprints? (Kanban / Scrum / Waterfall)
4. What defines the conditions a specific feature must satisfy? (Definition of Done / Acceptance Criteria / Design Tokens)
5. Which process checks whether the implemented UI matches approved designs? (Product QA / Design QA / Product Discovery)

### Answer key · జవాబులు
1. Product Discovery · 2. MVP · 3. Scrum · 4. Acceptance Criteria · 5. Design QA'''
