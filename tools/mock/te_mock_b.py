# Mock Interview Guide – Q26–50 (see te_mock_a.py for field meanings). Written by Claude.
T = {
26: dict(q='నిర్మాణాత్మక (constructive) design feedback ను మీరు ఎలా ఇస్తారు?',
 a='''Design objective మరియు user problem ఆధారంగా feedback ఇస్తాను.

నిర్దిష్టంగా ఉండి, ఒక సమస్య వల్ల కలిగే ప్రభావాన్ని వివరించడానికి ప్రయత్నిస్తాను.

ఉదాహరణకు, "screen confusing గా ఉంది" అని చెప్పడానికి బదులు, ఏ information hierarchy లేదా interaction గందరగోళం సృష్టిస్తోంది, అది task completion ను ఎందుకు ప్రభావితం చేయవచ్చు అని వివరిస్తాను.

బాగా పనిచేస్తున్న అంశాలను కూడా ప్రస్తావించి, సాధ్యమైన మెరుగుదలలను సూచిస్తాను.

వ్యక్తిని విమర్శించడం కాదు – design ను మెరుగుపరచి, designer ఎదగడానికి సహాయపడటమే నా ఉద్దేశం.''',
 en='''"This design is not good" is not constructive feedback.

Say what the problem is, why it exists, how it affects the user and how it can be improved.''', tip_en=''),

27: dict(q='మీ leadership style ఏమిటి?',
 a='''నా leadership style సహకారపూర్వకం (collaborative), మద్దతుగా ఉండేది (supportive) మరియు ఫలితాల ఆధారితం (outcome-oriented).

స్పష్టమైన దిశను నిర్ణయిస్తూనే, team members కు explore చేసి ownership తీసుకునే స్వేచ్ఛ ఇవ్వడాన్ని నమ్ముతాను.

బహిరంగ communication, evidence ఆధారిత నిర్ణయాలు, నిరంతర అభ్యాసాన్ని ప్రోత్సహిస్తాను.

Design leader business priorities ను అర్థం చేసుకుని, team అభివృద్ధికి మద్దతు ఇస్తూ, మంచి design నిర్ణయాలు నిలకడగా జరిగే వాతావరణాన్ని సృష్టించాలని కూడా నమ్ముతాను.''',
 en='''Don't describe your leadership style with a single adjective.

Explain a Collaborative + Strategic + Supportive + Accountable approach with practical examples.''', tip_en=''),

28: dict(q='Product Managers తో మీరు ఎలా collaborate చేస్తారు?',
 a='''Product Managers తో discovery ప్రారంభ దశ నుంచే కలిసి పనిచేస్తాను.

Product goals, target users, problem statements, priorities మరియు success metrics పై ఏకాభిప్రాయానికి వస్తాం.

User insights, experience అవకాశాలు, design ప్రత్యామ్నాయాలను నేను అందిస్తాను.

ప్రతిపాదిత experience feasible గా ఉండేలా scope, dependencies మరియు trade-offs కూడా చర్చిస్తాను.

Product Managers మరియు Product Designers వేర్వేరు దశల్లో పనిచేయకుండా భాగస్వాములుగా పనిచేయాలని నమ్ముతాను.''',
 en='''Collaboration is not the PM giving a requirement and the designer making the UI.

Work together from discovery – define product goals, user needs, priorities and metrics together.''', tip_en=''),

29: dict(q='Developers తో మీరు ఎలా collaborate చేస్తారు?',
 a='''Technical constraints మరియు implementation అవకాశాలు అర్థం చేసుకోవడానికి design process ప్రారంభంలోనే developers ను భాగస్వాములను చేస్తాను.

Design explorations, prototypes, component specifications, responsive behavior మరియు interaction states ను వారితో పంచుకుంటాను.

Implementation సమయంలో requirements స్పష్టం చేయడానికి, ప్రత్యామ్నాయాలు చర్చించడానికి అందుబాటులో ఉంటాను.

Development తర్వాత visual మరియు interaction consistency ని verify చేయడానికి design QA లో పాల్గొంటాను.

Developers ను design files అమలు చేసే వ్యక్తులుగా కాకుండా, సమస్య పరిష్కారంలో భాగస్వాములుగా చూస్తాను.''',
 en='''Developer collaboration should not start at the final handoff.

You need early feasibility discussions, design walkthroughs, documentation and implementation reviews.''', tip_en=''),

30: dict(q='Stakeholders మధ్య విరుద్ధమైన requirements ను మీరు ఎలా handle చేస్తారు?',
 a='''ముందుగా ప్రతి stakeholder request వెనుక ఉన్న అసలు లక్ష్యాన్ని గుర్తిస్తాను.

కొన్నిసార్లు stakeholders ఒకే సమస్యలోని వేర్వేరు భాగాలను పరిష్కరించడానికి ప్రయత్నిస్తున్నందువల్ల వేర్వేరు solutions సూచిస్తారు.

చర్చను user needs, product goals, business impact మరియు technical feasibility వైపు తిరిగి తీసుకువస్తాను.

స్పష్టమైన trade-offs తో ప్రత్యామ్నాయాలను present చేసి, evidence ఆధారంగా ఒక దిశను సిఫార్సు చేస్తాను.

నిర్ణయం ముఖ్యమైన priorities ను ప్రభావితం చేస్తే, సంబంధిత decision-makers చివరి approach పై ఏకాభిప్రాయానికి రావడంలో సహాయపడతాను.''',
 en='''Stakeholder A may want one feature and Stakeholder B another.

Find the actual business problem behind their requests and recommend a solution based on the common objective.''', tip_en=''),

31: dict(q='Design నిర్ణయాలను senior management కు మీరు ఎలా present చేస్తారు?',
 a='''సమస్య, evidence, ప్రతిపాదిత solution, ఆశించిన ప్రభావం మరియు ముఖ్యమైన trade-offs పై దృష్టి పెట్టి design నిర్ణయాలను present చేస్తాను.

వెనుక ఉన్న కారణం వివరించకుండా కేవలం screens చూపించడం నివారిస్తాను.

నా సిఫార్సులకు మద్దతుగా user insights, journey maps, prototypes, usability findings మరియు సంబంధిత product metrics ఉపయోగిస్తాను.

Risks, dependencies మరియు తదుపరి steps ను కూడా స్పష్టంగా తెలియజేస్తాను.

Senior stakeholders కోసం చర్చను business విలువ మరియు user ఫలితాలపై కేంద్రీకరిస్తాను.''',
 en='''Don't show senior management only Figma screens. Use this structure:

Problem → Evidence → Solution → Business Impact → Risks → Next Steps.''', tip_en=''),

32: dict(q='Stakeholder మీ design ను reject చేస్తే మీరు ఏమి చేస్తారు?',
 a='''ముందుగా reject చేయడానికి కారణాన్ని అర్థం చేసుకుంటాను.

ఆ ఆందోళన usability, business priorities, brand alignment, technical feasibility లేదా వ్యక్తిగత ఇష్టానికి సంబంధించినదో అడుగుతాను.

Feedback ను మొదటి design objectives మరియు user evidence తో పోల్చి review చేస్తాను.

Feedback సరైనదైతే design ను మెరుగుపరుస్తాను. ప్రస్తుత దిశే బలమైనదని నమ్మితే, నా కారణాలను వివరించి research లేదా testing తో మద్దతు ఇస్తాను.

ఉత్తమ product ఫలితం సాధించడమే లక్ష్యం కాబట్టి చర్చకు సిద్ధంగా ఉంటాను.''',
 en='''Don't change the design immediately because a stakeholder rejected it – but don't defend it out of ego either.

Find the reason, review the evidence and iterate the design if needed.''', tip_en=''),

33: dict(q='క్లిష్టమైన design concepts ను design కాని stakeholders కు ఎలా వివరిస్తారు?',
 a='''క్లిష్టమైన design concepts ను తెలిసిన user problems మరియు business ఫలితాలతో కలిపి సరళంగా వివరిస్తాను.

Design terminology వివరించడానికి బదులు సరళమైన ఉదాహరణలు, user journeys, diagrams, prototypes మరియు నిజమైన సన్నివేశాలు ఉపయోగిస్తాను.

ఒక నిర్ణయం ఎందుకు ముఖ్యం, అది ఎలాంటి ప్రభావం చూపగలదు అని వివరించడంపై దృష్టి పెడతాను.

Visual communication మరియు storytelling నేపథ్యం వేర్వేరు audiences కు ideas ను స్పష్టంగా వివరించడానికి సహాయపడుతుంది.''',
 en='''Don't overload non-design stakeholders with UX terminology.

Use visual examples, simple language, prototypes and real user scenarios.''', tip_en=''),

34: dict(q='Design System ను మీరు ఎలా create చేస్తారు లేదా మెరుగుపరుస్తారు?',
 a='''ముందుగా ప్రస్తుత product interfaces ను audit చేసి, inconsistencies, పదే పదే వచ్చే patterns, common components ను గుర్తిస్తాను.

తర్వాత color, typography, spacing, grids మరియు interaction principles వంటి design foundations ను define చేస్తాను.

స్పష్టమైన variants, states మరియు usage guidelines తో reusable components తయారు చేస్తాను.

Design tokens మరియు component behavior implementation కు అనుగుణంగా ఉండేలా developers తో కలిసి పనిచేస్తాను.

చివరగా documentation, ownership, contribution guidelines మరియు system ను maintain చేసే process ఏర్పాటు చేస్తాను.''',
 en='''To create a Design System:
1. Existing UI audit.
2. Design foundations.
3. Design tokens.
4. Components and variants.
5. Patterns.
6. Documentation.
7. Developer alignment.
8. Governance.

In the ResolveAI concept you could organize reusable dashboard components, forms, tables, navigation and status indicators.''', tip_en=''),

35: dict(q='Responsive design ను మీరు ఎలా నిర్ధారిస్తారు?',
 a='''వేర్వేరు screen sizes, content priorities, interaction patterns మరియు device సందర్భాలను పరిగణించి responsive experiences design చేస్తాను.

ముఖ్యమైన user tasks తో మొదలుపెట్టి, desktop, tablet, mobile లలో layout ఎలా మారాలో నిర్ణయిస్తాను.

Flexible grids, తగిన breakpoints, scalable typography మరియు reusable components ఉపయోగిస్తాను.

ముఖ్యమైన screens ను వేర్వేరు viewport sizes లో validate చేసి, అమలైన experience ఉపయోగించగలిగేలా ఉండేలా developers తో కలిసి పనిచేస్తాను.''',
 en='''Responsive design is not just shrinking the desktop screen.

Content priority, navigation, touch targets, readability and interaction patterns must also adapt.''', tip_en=''),

36: dict(q='మీ designs లో accessibility ని మీరు ఎలా నిర్ధారిస్తారు?',
 a='''Accessibility ని చివరి checklist గా కాకుండా, మొత్తం design process అంతటా పరిగణిస్తాను.

Color contrast, చదవగలిగే typography, keyboard navigation, focus states, స్పష్టమైన labels, semantic structure మరియు screen reader support పై శ్రద్ధ పెడతాను.

వేర్వేరు దృష్టి, motor, వినికిడి మరియు cognitive అవసరాలు ఉన్న users ను కూడా పరిగణిస్తాను.

సంబంధిత WCAG guidance ఉపయోగించి, implementation ను validate చేయడానికి developers మరియు QA teams తో కలిసి పనిచేస్తాను.''',
 en='''Don't check accessibility only at the final stage.

Follow inclusive principles from the start of design – contrast, focus, labels, keyboard access and screen reader support are important.''', tip_en=''),

37: dict(q='Development సమయంలో design consistency ని మీరు ఎలా నిర్ధారిస్తారు?',
 a='''Reusable components, వివరమైన design specifications, shared design tokens మరియు developers తో క్రమమైన communication ద్వారా consistency నిర్ధారిస్తాను.

Component states, spacing, typography, responsive behavior మరియు interaction rules ను document చేస్తాను.

Implementation సమయంలో కీలకమైన screens ను review చేసి, approve అయిన designs తో పోల్చుతాను.

Technical constraints వల్ల మార్పులు అవసరమైతే, ప్రత్యామ్నాయాలు చర్చించి, మొత్తం experience consistent గా ఉండేలా చూస్తాను.''',
 en='''A Figma file is not enough for design consistency.

You need a component library, tokens, clear specifications, communication and design QA.''', tip_en=''),

38: dict(q='మీ design workflow లో AI tools ను ఎలా ఉపయోగిస్తారు?',
 a='''Exploration, research support, content generation, visual ideation మరియు productivity మెరుగుపరచడానికి AI tools ఉపయోగిస్తాను.

Task ను బట్టి ChatGPT, Figma AI, Midjourney, Leonardo AI మరియు ఇతర AI-assisted design platforms వంటి tools explore చేస్తాను.

ఉదాహరణకు, AI ప్రారంభ design directions తయారు చేయడానికి, ideas ను organize చేయడానికి, visual references సృష్టించడానికి లేదా content variations లో సహాయపడుతుంది.

అయితే AI output ను చివరి design నిర్ణయంగా భావించను. ఖచ్చితత్వం, usability, brand alignment, accessibility మరియు user problem కు సంబంధం కోసం దాన్ని review చేస్తాను.

AI design thinking ను పెంచాలి కానీ మనిషి విచక్షణను భర్తీ చేయకూడదని నమ్ముతాను.''',
 en='''AI tools help increase your productivity, but the designer must make the final decisions.

Give specific examples of how you use AI:
- Research synthesis support.
- Design ideation.
- Image generation.
- UX writing exploration.
- Prototype exploration.
- Design documentation.''', tip_en=''),

39: dict(q='మీ portfolio గురించి వివరించండి.',
 a='''నా portfolio వేర్వేరు product domains మరియు design సవాళ్లలో నా అనుభవాన్ని చూపిస్తుంది.

User problems అర్థం చేసుకోవడం, product experiences ను structure చేయడం, interfaces design చేయడం, teams తో కలిసి పనిచేయడం వంటి నా సామర్థ్యాలను చూపించే projects ఎంచుకున్నాను.

ఉదాహరణకు, Classic Rummy నా gaming product design అనుభవాన్ని చూపిస్తుంది. TWAM నా e-commerce design పనిని సూచిస్తుంది. ResolveAI enterprise SaaS మరియు AI-powered workflows ను explore చేస్తుంది; ORRBUS ఒక mobility product concept.

నా స్వతంత్ర design practice మరియు product vision ను చూపించడానికి D'SARAS ను కూడా చేర్చాను.

ప్రతి project లో సమస్య, నా పాత్ర, design process, ముఖ్య నిర్ణయాలు మరియు ఫలితాలపై దృష్టి పెడతాను.''',
 en='''You don't need to show every project in your portfolio – select the 3–5 projects that best represent your skills.

In each case study show:
- Problem.
- Role.
- Process.
- Key decisions.
- Final solution.
- Outcome.''', tip_en=''),

40: dict(q='మీ Classic Rummy project గురించి వివరించండి.',
 a='''Nazara Group లో భాగమైన Openplay Technologies లో Classic Rummy నా ముఖ్యమైన digital gaming product అనుభవాల్లో ఒకటి.

నా పనిలో ఒక mobile gaming product కోసం user experiences design చేయడం ఉంది.

ఈ project కోసం player behavior, game interactions, navigation, visual hierarchy మరియు మొత్తం gameplay experience ను అర్థం చేసుకోవాల్సి వచ్చింది.

ముఖ్యమైన game actions అర్థమయ్యేలా చేయడం, users experience ను స్పష్టంగా navigate చేయగలిగేలా చూడటంపై దృష్టి పెట్టాను.

ఈ project interaction design, gaming UX, mobile usability మరియు స్థిరపడిన digital product వాతావరణంలో పనిచేయడంపై నా అవగాహనను బలపరిచింది.''',
 en='''You can use Classic Rummy as your main professional case study. In the presentation cover:
- Product context.
- Target audience.
- Your exact role.
- Major design challenges.
- User flows.
- Gameplay interaction.
- Design decisions.
- Collaboration.
- Verified outcomes.

Important: mention only the responsibilities you actually handled. If you quote product results or metrics, base them on a source.''', tip_en=''),

41: dict(q='మీ TWAM project గురించి వివరించండి.',
 a='''TWAM అనేది D'SARAS Design Studio ద్వారా అభివృద్ధి చేసిన e-commerce design project.

స్పష్టమైన, ఆకట్టుకునే shopping experience సృష్టించడంపై దృష్టి పెట్టాం.

Product context అర్థం చేసుకోవడం, shopping journey ను organize చేయడం, interface structure ను explore చేయడం, visual experience ను అభివృద్ధి చేయడంపై పనిచేశాను.

Visual exploration కు మద్దతు ఇవ్వడానికి, design ideation ను వేగవంతం చేయడానికి generative AI-assisted workflows ను కూడా explore చేశాను.

ఈ project లో user journeys, product discovery, visual communication మరియు e-commerce UX లో నా అనుభవాన్ని అన్వయించగలిగాను.''',
 en='''Points to explain for TWAM:
- E-commerce problem.
- Product discovery.
- Category navigation.
- Product details.
- Shopping cart.
- Checkout.
- Visual identity.
- AI-assisted design process.''', tip_en=''),

42: dict(q='మీ ResolveAI project గురించి వివరించండి.',
 a='''ResolveAI అనేది product design portfolio project గా నేను అభివృద్ధి చేసిన AI-powered customer support SaaS concept.

Customer support teams tickets నిర్వహించడానికి, response workflows మెరుగుపరచడానికి, support performance అర్థం చేసుకోవడానికి AI ఎలా సహాయపడగలదో explore చేయడమే idea.

Support agents మరియు managers అవసరాలను పరిగణించి దీన్ని సమీపించాను.

Design exploration లో dashboards, ticket management, AI response suggestions, analytics మరియు workflow organization ఉన్నాయి.

ముఖ్యమైన నిర్ణయాలపై human agents నియంత్రణలో ఉంటూనే, క్లిష్టమైన సమాచారాన్ని సులభంగా అర్థమయ్యేలా చేయడంపై దృష్టి పెట్టాను.

ఈ project enterprise SaaS, AI-powered workflows మరియు data-driven product experiences పై నా ఆసక్తిని చూపిస్తుంది.''',
 en='''Say clearly that ResolveAI is a concept project. Skills this project can show:
- B2B SaaS thinking.
- Dashboard IA.
- AI workflow design.
- Data visualization.
- Role-based experiences.
- Human-in-the-loop interaction.
- Design system.''', tip_en=''),

43: dict(q='మీ ORRBUS project గురించి వివరించండి.',
 a='''ORRBUS అనేది మెరుగైన commuter experiences ను explore చేయడంపై దృష్టి పెట్టిన mobility product concept.

Users సంబంధిత ప్రయాణ సమాచారాన్ని ఎలా పొందగలరు, mobility సంబంధిత tasks ను మరింత సమర్థవంతంగా ఎలా navigate చేయగలరు అని అర్థం చేసుకోవడమే idea.

Location-based information, navigation, route discovery మరియు రోజువారీ commuters అవసరాలను పరిగణిస్తూ user journey దృష్టికోణం నుంచి ఈ concept ను సమీపించాను.

ఈ project ద్వారా information architecture, mobile UX, location-based interactions మరియు product thinking ను చూపించగలను.

Concept project గా, ప్రారంభ idea నుంచి product opportunity ని explore చేయగల నా సామర్థ్యాన్ని కూడా ఇది సూచిస్తుంది.''',
 en='''Don't present ORRBUS as a launched product – explain it as a concept project:
- Target users.
- Commuter pain points.
- Core problem.
- Mobility journey.
- Location and navigation.
- Proposed features.
- Validation still required.''', tip_en=''),

44: dict(q='UX case study ను మీరు ఎలా present చేస్తారు?',
 a='''కేవలం final screens చూపించకుండా, సమస్య పరిష్కార ప్రయాణం చుట్టూ నా case studies ను structure చేస్తాను.

Product context, target users, business objectives మరియు నా పాత్రతో మొదలుపెడతాను.

తర్వాత research findings, ముఖ్య సవాళ్లు, design అవకాశాలు, information architecture, user flows మరియు design explorations ను వివరిస్తాను.

ముఖ్యమైన design నిర్ణయాలను చూపించి, ఒక నిర్దిష్ట solution ను ఎందుకు ఎంచుకున్నానో వివరిస్తాను.

చివరగా validation, implementation అంశాలు, అందుబాటులో ఉన్న చోట కొలవగల ఫలితాలను చర్చిస్తాను.

నా వ్యక్తిగత contributions ను మొత్తం team చేసిన పని నుంచి స్పష్టంగా వేరు చేసి చెబుతాను.''',
 en='''Case study presentation flow:
1. Project overview.
2. Problem statement.
3. Business and user goals.
4. Your role.
5. Research.
6. Insights.
7. UX strategy.
8. Wireframes and flows.
9. UI design.
10. Testing and iteration.
11. Outcomes.
12. Learnings.''', tip_en=''),

45: dict(q='Research లేకుండా ఒక feature design చేయమని Product Manager అడిగితే మీరు ఏమి చేస్తారు?',
 a='''ముందుగా ఆ request వెనుక కారణాన్ని, ఆశించిన business ఫలితాన్ని అర్థం చేసుకుంటాను.

ఉన్న product data, customer feedback మరియు అందుబాటులో ఉన్న research ను review చేస్తాను.

సమస్య ఇప్పటికే బాగా అర్థమై ఉంటే, focused design approach తో ముందుకు వెళ్లవచ్చు.

ముఖ్యమైన assumptions అస్పష్టంగా ఉంటే, తేలికపాటి research లేదా validation activity ని సిఫార్సు చేస్తాను.

అనవసర ఆలస్యం నివారిస్తాను, కానీ test చేయని assumptions ఆధారంగా పెద్ద development effort పెట్టకుండా కూడా చూసుకుంటాను.''',
 en='''Don't reject it immediately when asked to design without research.

Review the existing evidence. If needed, suggest quick user interviews, prototype testing or data analysis.''', tip_en=''),

46: dict(q='మీ design బాగుంది, కానీ technically కష్టమని developers అంటే మీరు ఏమి చేస్తారు?',
 a='''ముందుగా technical పరిమితిని, ప్రతిపాదిత experience పై దాని ప్రభావాన్ని అర్థం చేసుకుంటాను.

తర్వాత ప్రత్యామ్నాయ approaches గుర్తించడానికి developers తో కలిసి పనిచేస్తాను.

అవసరమైన user requirements ను, సరళీకరించగలిగే visual లేదా interaction enhancements నుంచి వేరు చేస్తాను.

ప్రత్యామ్నాయం core user విలువను కాపాడితే, design ను మార్చడానికి సిద్ధంగా ఉంటాను.

నిజమైన technical పరిమితుల్లో సాధ్యమైనంత ఉత్తమ experience సాధించడమే నా లక్ష్యం.''',
 en='''Don't see it as a design-vs-development conflict.

Preserve the core user need and design a technically feasible alternative.''', tip_en=''),

47: dict(q='ఒక పెద్ద feature ను deliver చేయడానికి మీ team కు రెండు వారాలే ఉంటే ఎలా సమీపిస్తారు?',
 a='''ముందుగా ఆశించిన ఫలితం, deadline మరియు కీలకమైన requirements ను స్పష్టం చేసుకుంటాను.

తర్వాత feature ను అవసరమైన user journeys గా విభజించి, release కు అవసరమైన కనీస scope ను గుర్తిస్తాను.

అధిక ప్రభావం ఉన్న interactions కు priority ఇచ్చి, product మరియు engineering teams తో ముందుగానే ఏకాభిప్రాయానికి వచ్చి, అనవసర design exploration తగ్గిస్తాను.

సాధ్యమైన ప్రతిచోటా ఇప్పటికే ఉన్న design system components ఉపయోగిస్తాను.

Risks గుర్తించి, validation activities నిర్వచించి, timeline లో వాస్తవంగా ఏమి deliver చేయగలమో తెలియజేస్తాను.''',
 en='''Don't try to build a perfect product in a short timeline.

MVP scope, the core journey, existing components, dependencies and risk management are what matter.''', tip_en=''),

48: dict(q='Product metrics మెరుగుపడి user satisfaction తగ్గితే మీరు ఏమి చేస్తారు?',
 a='''మెరుగైన metrics అంటే experience విజయవంతమైందని భావించకుండా, ఆ తేడా వెనుక కారణాన్ని పరిశోధిస్తాను.

ఉదాహరణకు, conversion పెరగవచ్చు కానీ users ఎక్కువ గందరగోళం, ఒత్తిడి లేదా ఇబ్బంది అనుభవిస్తూ ఉండవచ్చు.

User feedback, usability findings, support complaints మరియు behavior analytics ను review చేస్తాను.

ఏ user segments ప్రభావితమవుతున్నాయో గుర్తించి, ఆ మెరుగుదల స్థిరంగా కొనసాగుతుందో లేదో అంచనా వేస్తాను.

తర్వాత business ఫలితాలను user satisfaction తో సమతుల్యం చేయడానికి product team తో కలిసి పనిచేస్తాను.''',
 en='''Don't assume UX improved just because conversion went up.

A business metric can be positive while the user experience is negative – analyse quantitative data and qualitative feedback together.''', tip_en=''),

49: dict(q='మా organization లో చేరితే మొదటి 90 రోజుల్లో మీరు ఏమి చేస్తారు?',
 a='''మొదటి 30 రోజుల్లో product, business goals, customers, team structure మరియు ప్రస్తుత design processes ను అర్థం చేసుకోవడంపై దృష్టి పెడతాను.

తర్వాతి 30 రోజుల్లో ప్రధాన experience gaps గుర్తించి, design system ను review చేసి, collaboration సవాళ్లను అర్థం చేసుకుని, team తో కలిసి మెరుగుదల అవకాశాలకు priority ఇస్తాను.

చివరి 30 రోజుల్లో ఎంచుకున్న product initiatives కు contribute చేసి, స్పష్టమైన design priorities ఏర్పాటు చేసి, design process కు మెరుగుదలలు ప్రతిపాదిస్తాను.

పెద్ద మార్పులు తీసుకువచ్చే ముందు organization ను అర్థం చేసుకుని, తర్వాత focused design initiatives ద్వారా కొలవగల విలువను సృష్టించడమే నా లక్ష్యం.''',
 en='''90-day plan:

First 30 days – Learn:
- Product.
- Business.
- Users.
- Team.
- Existing processes.

Next 30 days – Evaluate:
- UX gaps.
- Design system.
- Collaboration.
- Priorities.

Final 30 days – Contribute:
- Improve selected journeys.
- Strengthen the design process.
- Establish design priorities.
- Demonstrate impact.''', tip_en=''),

50: dict(q='Product Design Leader గా మీ దీర్ఘకాల vision ఏమిటి?',
 a='''అర్థవంతమైన digital products నిర్మించడం, user-centered thinking ద్వారా క్లిష్టమైన సమస్యలను పరిష్కరించే design teams ను సృష్టించడమే నా దీర్ఘకాల vision.

Product strategy ని ప్రభావితం చేయడం, design maturity పెంచడం, design, product మరియు engineering మధ్య బలమైన సహకారం నిర్మించడం ద్వారా వ్యక్తిగత interface design కు మించి contribute చేయాలనుకుంటున్నాను.

AI మరియు కొత్త technologies digital experiences ను బాధ్యతాయుతంగా ఎలా మెరుగుపరచగలవో explore చేయడంపై కూడా ఆసక్తి ఉంది.

D'SARAS లో నా పని మరియు professional అనుభవం ద్వారా నేర్చుకుంటూ, designers ను mentor చేస్తూ, users మరియు businesses కు శాశ్వత విలువ సృష్టించే products కు contribute చేస్తూ ఉండాలనుకుంటున్నాను.''',
 en='''This question is about your career ambition:
- Influencing product strategy.
- Mentoring design teams.
- Raising design maturity.
- Exploring AI and emerging technologies.
- Building meaningful products.

Connect your long-term vision to the company's goals.''', tip_en=''),
}
