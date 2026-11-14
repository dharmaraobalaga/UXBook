# Group 6 – Telugu tables, examples, interview meanings (written by Claude from the PDF's English)
T = {
76: dict(q='Usability Testing మరియు User Testing మధ్య తేడా ఏమిటి?',
  tbl=[['ఉపయోగ సౌలభ్యం (ease of use) పై దృష్టి','విస్తృత product మూల్యాంకనం కూడా ఉండవచ్చు'],['Task performance ను కొలుస్తుంది','Concepts, అనుభవాలను అంచనా వేయవచ్చు'],['Usability సమస్యలను గుర్తిస్తుంది','వినియోగదారుల feedback ను గుర్తిస్తుంది'],['Task ఆధారిత scenarios ఉపయోగిస్తుంది','వివిధ research కార్యకలాపాలు ఉపయోగించవచ్చు'],['మరింత నిర్దిష్ట పద్ధతి','విస్తృతమైన పదం']],
  ex='Classic Rummy:\n- Usability Testing: Players ను ఒక rummy table లో చేరమని చెప్పి, గందరగోళం లేకుండా task పూర్తి చేయగలుగుతున్నారో గమనించడం.\n- User Testing: కొత్త rummy game concept ను players అంచనా వేసి, అది ఎంత ఆకర్షణీయంగా ఉందో, మొత్తం అనుభవంపై feedback ఇవ్వమని అడగడం.',
  iv='Usability Testing ఉపయోగ సౌలభ్యాన్ని కొలిచే నిర్దిష్ట పద్ధతి; User Testing విస్తృతంగా concepts, అనుభవాలను అంచనా వేయగలదు.'),
77: dict(q='Moderated Testing మరియు Unmoderated Testing మధ్య తేడా ఏమిటి?',
  tbl=[['Researcher ఉంటారు','Live researcher అవసరం లేదు'],['తదుపరి ప్రశ్నలు (follow-up) అడగవచ్చు','అప్పటికప్పుడు స్పష్టత అడిగే అవకాశం తక్కువ'],['లోతైన సందర్భం ఇస్తుంది','ఎక్కువ మంది పాల్గొనడానికి ఉపయోగకరం'],['Scheduling అవసరం','మరింత సౌలభ్యం ఉంటుంది'],['నిర్వహణ శ్రమ ఎక్కువ','ఒక్కో session కు నిర్వహణ శ్రమ తక్కువ']],
  ex='Banking App:\n\nModerated:\n\nResearcher ఒక customer ను ₹5,000 transfer చేయమని చెప్పి, వారి చర్యలను గమనిస్తూ, confirmation screen వద్ద ఎందుకు సంకోచిస్తున్నారో అడుగుతారు.\n\nUnmoderated:\n\nCustomer కు డబ్బు transfer చేయమనే సూచనలతో ఒక prototype link వస్తుంది. Tool task completion, clicks మరియు session feedback ను రికార్డ్ చేస్తుంది.',
  iv='లోతైన "ఎందుకు" కావాలంటే moderated; ఎక్కువ మంది నుంచి త్వరగా data కావాలంటే unmoderated testing.'),
78: dict(q='Remote Testing మరియు In-Person Testing మధ్య తేడా ఏమిటి?',
  tbl=[['Online లో జరుగుతుంది','ముఖాముఖి (face-to-face) జరుగుతుంది'],['ప్రాంతం పరంగా సౌలభ్యం','భౌతికంగా హాజరు అవసరం'],['Screen sharing, recordings','నేరుగా గమనించడం'],['ప్రయాణ అవసరం తక్కువ','Venue, scheduling అవసరం'],['Technical పరిమితులు ఉండవచ్చు','పరిసరాలను నేరుగా గమనించవచ్చు']],
  ex='E-commerce App:\n- Remote: హైదరాబాద్, బెంగళూరు, చెన్నై users తో video calls ద్వారా checkout prototype ను test చేయడం.\n- In-Person: Customers ను usability lab కు పిలిచి, వారు checkout screens తో ఎలా interact చేస్తున్నారో గమనించడం.',
  iv='విస్తృత ప్రాంతాల users కోసం remote; body language, పరిసరాలు ముఖ్యమైనప్పుడు in-person testing.'),
79: dict(q='Formative Testing మరియు Summative Testing మధ్య తేడా ఏమిటి?',
  tbl=[['Design ను మెరుగుపరుస్తుంది','Design పనితీరును కొలుస్తుంది'],['Development సమయంలో జరుగుతుంది','తరచుగా implementation తర్వాత లేదా నిర్ణీత milestone వద్ద'],['Usability సమస్యలను గుర్తిస్తుంది','Usability ఫలితాలను కొలుస్తుంది'],['Iteration కు సహాయపడుతుంది','మూల్యాంకనం, reporting కు సహాయపడుతుంది'],['మెరుగుదలపై దృష్టి','కొలతపై దృష్టి']],
  ex='Banking App:\n\nFormative Testing:\n\nప్రారంభ money-transfer prototype ను ఐదుగురు users తో test చేయడం. Beneficiary ఎంపికలో గందరగోళాన్ని గుర్తించి flow ను మెరుగుపరచడం.\n\nSummative Testing:\n\nమెరుగుదలల తర్వాత, ఎక్కువ మంది participants తో test చేసి, ముందే నిర్ణయించిన లక్ష్యాలతో task success rate, completion time మరియు error rate ను కొలవడం.',
  iv='Formative "మెరుగుపరచడానికి", Summative "కొలవడానికి".'),
80: dict(q='A/B Testing మరియు Multivariate Testing మధ్య తేడా ఏమిటి?',
  tbl=[['పూర్తి versions లేదా నిర్ణీత variants ను పోలుస్తుంది','అనేక elements కలయికలను (combinations) test చేస్తుంది'],['సాధారణంగా set up చేయడం సులభం','Set up చేయడం మరింత సంక్లిష్టం'],['మెరుగ్గా పనిచేసే variant ను గుర్తిస్తుంది','Elements కలయికల ప్రభావాన్ని అర్థం చేసుకోవడంలో సహాయం'],['తరచుగా తక్కువ traffic సరిపోతుంది','సాధారణంగా ఎక్కువ traffic అవసరం'],['ఉదా: CTA A vs CTA B','ఉదా: Button + Headline + Image కలయికలు']],
  ex='E-commerce App:\n\nA/B Testing:\n- Version A: "Buy Now" button.\n- Version B: "Add to Cart" button.\n\nఎంచుకున్న conversion metric ను ఏ version మెరుగుపరుస్తుందో కొలవడం.\n\nMultivariate Testing:\n\nఈ కలయికలను test చేయడం:\n- రెండు headline variations.\n- రెండు CTA రంగులు.\n- రెండు product banner images.\n\nదీని వల్ల 2 × 2 × 2 = 8 సాధ్యమైన కలయికలు వస్తాయి.',
  iv='రెండు versions పోలికకు A/B; అనేక elements కలయికల ప్రభావం తెలుసుకోవడానికి (తగినంత traffic ఉంటే) multivariate testing.'),
81: dict(q='Usability Testing మరియు A/B Testing మధ్య తేడా ఏమిటి?',
  tbl=[['Usability సమస్యలను గుర్తిస్తుంది','Design పనితీరును పోలుస్తుంది'],['తరచుగా qualitative మరియు quantitative','ప్రధానంగా quantitative'],['గమనించడం, task analysis ఉపయోగిస్తుంది','నియంత్రిత ప్రయోగాలు (controlled experiments) ఉపయోగిస్తుంది'],['సమస్యలు ఎందుకు వస్తున్నాయో అర్థం చేసుకోవడంలో సహాయం','ఏ variant మెరుగ్గా పనిచేస్తుందో గుర్తించడంలో సహాయం'],['సాధారణంగా చిన్న research samples','తగిన experimental sample size అవసరం']],
  ex='Checkout Page:\n\nUsability Testing:\n\nUsers ను checkout process పూర్తి చేయమని చెప్పి, address entry లో ఎందుకు ఇబ్బంది పడుతున్నారో గమనించడం.\n\nA/B Testing:\n- Version A: ఐదు దశల checkout.\n- Version B: మూడు దశల checkout.\n\nCheckout completion rate లో తేడాను కొలవడం.',
  iv='Usability Testing "ఎందుకు" సమస్యలు వస్తున్నాయో; A/B Testing "ఏది" మెరుగ్గా పనిచేస్తుందో చెబుతుంది.'),
82: dict(q='Heuristic Evaluation మరియు Cognitive Walkthrough మధ్య తేడా ఏమిటి?',
  tbl=[['Usability సూత్రాల ఆధారంగా','దశలవారీ user చర్యల ఆధారంగా'],['మొత్తం interface usability ని అంచనా వేస్తుంది','నిర్దిష్ట tasks నేర్చుకోవడం (learnability) పై దృష్టి'],['UX నిపుణులు చేస్తారు','User ప్రవర్తనను simulate చేసే evaluators చేస్తారు'],['Heuristic ఉల్లంఘనలను గుర్తిస్తుంది','చర్యలను కనుగొనడంలో ఇబ్బందులను గుర్తిస్తుంది'],['సాధారణంగా Nielsen 10 heuristics ఉపయోగిస్తుంది','Task క్రమాలు, learning ప్రశ్నలు ఉపయోగిస్తుంది']],
  ex='Banking App:\n\nHeuristic Evaluation:\n\nఒక నిపుణుడు banking app ను పరిశీలించి ఇవి గుర్తిస్తారు:\n- Money transfer తర్వాత స్పష్టమైన confirmation లేదు.\n- Button styles స్థిరంగా లేవు.\n- కొన్ని చర్యలను సులభంగా undo చేసే మార్గం లేదు.\n\nCognitive Walkthrough:\n\nమొదటిసారి user డబ్బు transfer చేసే ప్రయత్నాన్ని evaluator అనుసరించి ఇలా అడుగుతారు:\n1. User తాను ఏమి సాధించాలనుకుంటున్నారో తెలుసుకుంటారా?\n2. సరైన చర్యను user గమనిస్తారా?\n3. ఆ చర్య సరైనదని user అర్థం చేసుకుంటారా?\n4. చర్య తర్వాత, లక్ష్యం వైపు పురోగతిని user గుర్తిస్తారా?',
  iv='మొత్తం interface ను సూత్రాలతో పరిశీలించడానికి heuristic evaluation; కొత్త users ఒక task ను నేర్చుకోగలరో చూడడానికి cognitive walkthrough.'),
83: dict(q='Expert Review మరియు Peer Review మధ్య తేడా ఏమిటి?',
  tbl=[['నిపుణుడు (specialist) చేస్తారు','సహోద్యోగులు చేస్తారు'],['లోతైన domain నైపుణ్యం ఉపయోగిస్తుంది','Team యొక్క ఉమ్మడి జ్ఞానం ఉపయోగిస్తుంది'],['సంక్లిష్ట usability సమస్యలను గుర్తించగలదు','Design అస్థిరతలను గుర్తించడంలో సహాయం'],['బయటి లేదా లోపలి వ్యక్తి కావచ్చు','సాధారణంగా team లోపలే'],['మరింత ప్రత్యేక మూల్యాంకనం','సహకార feedback ప్రక్రియ']],
  ex='SaaS Dashboard:\n\nExpert Review:\n\nఒక Senior UX Consultant dashboard ను review చేసి information architecture సమస్యలు, accessibility సమస్యలు మరియు usability ఉల్లంఘనలను గుర్తిస్తారు.\n\nPeer Review:\n\nఇద్దరు Product Designers ఒకరి dashboard designs ను మరొకరు review చేసి spacing, typography, component consistency మరియు interaction patterns లో మెరుగుదలలు సూచిస్తారు.',
  iv='లోతైన, ప్రత్యేక మూల్యాంకనానికి expert review; team లో నాణ్యత, consistency కోసం peer review.'),
84: dict(q='Usability మరియు Accessibility మధ్య తేడా ఏమిటి?',
  tbl=[['ఉపయోగ సౌలభ్యంపై దృష్టి','విభిన్న సామర్థ్యాల వారికి యాక్సెస్ పై దృష్టి'],['సామర్థ్యం (efficiency), సంతృప్తిని మెరుగుపరుస్తుంది','Interaction అడ్డంకులను తొలగిస్తుంది'],['Task పూర్తిని అంచనా వేస్తుంది','అందరికీ అందుబాటును (inclusive access) అంచనా వేస్తుంది'],['అందరు users కు వర్తిస్తుంది','ముఖ్యంగా వైకల్యం ఉన్న users అవసరాలను పరిష్కరిస్తుంది'],['ఉదా: సరళమైన checkout','ఉదా: Screen reader మద్దతు']],
  ex='Banking App:\n\nUsability:\n- సరళమైన money-transfer flow.\n- స్పష్టమైన labels.\n- అనవసర steps తక్కువ.\n- సులభంగా అర్థమయ్యే transaction status.\n\nAccessibility:\n- Screen reader కు అనుకూలమైన labels.\n- Keyboard navigation.\n- తగినంత colour contrast.\n- పెంచగలిగే text.\n- కనిపించే focus indicators.',
  iv='Usability అందరికీ సులభంగా ఉండేలా; Accessibility ఎవరూ బయట ఉండిపోకుండా – రెండూ కలిస్తేనే మంచి అనుభవం.'),
85: dict(q='Effectiveness మరియు Efficiency మధ్య తేడా ఏమిటి?',
  tbl=[['Task విజయాన్ని కొలుస్తుంది','శ్రమ, వనరులను కొలుస్తుంది'],['ఖచ్చితత్వంపై దృష్టి','వేగం, శ్రమపై దృష్టి'],['Completion rate ను కొలవవచ్చు','Time on task ను కొలవవచ్చు'],['సమాధానం: Task పూర్తయిందా?','సమాధానం: ఎంత సమర్థవంతంగా పూర్తయింది?'],['ఉదా: విజయవంతమైన payment','ఉదా: తక్కువ steps లో payment పూర్తి']],
  ex='Money Transfer:\n\n10 మంది users ను డబ్బు transfer చేయమని అడిగారనుకోండి.\n- 9 మంది transfer ను విజయవంతంగా పూర్తి చేశారు.\n- సగటు completion సమయం 2 నిమిషాలు.\n\nEffectiveness: 90% task success rate.\n\nEfficiency: సగటు task completion సమయం 2 నిమిషాలు.\n\nRedesign తర్వాత success తగ్గకుండా సగటు సమయం 45 సెకన్లకు తగ్గితే, efficiency మెరుగుపడింది.',
  iv='Effectiveness "పని పూర్తయిందా", Efficiency "ఎంత తక్కువ శ్రమతో, సమయంతో పూర్తయింది".'),
86: dict(q='SUS మరియు NPS మధ్య తేడా ఏమిటి?',
  tbl=[['గ్రహించిన usability ని కొలుస్తుంది','సిఫార్సు చేసే అవకాశాన్ని కొలుస్తుంది'],['10 ప్రశ్నల questionnaire','సాధారణంగా ఒక ముఖ్య ప్రశ్న'],['Score 0–100 మధ్య','Score -100 నుంచి +100 మధ్య'],['ఉపయోగ సౌలభ్యాన్ని అంచనా వేస్తుంది','Customer advocacy ని అంచనా వేస్తుంది'],['UX usability మూల్యాంకనం','Customer loyalty కొలత']],
  ex='Banking App:\n\nSUS:\n\nBanking app ఉపయోగ సౌలభ్యం గురించి users ను 10 ప్రామాణిక ప్రశ్నలు అడగడం.\n\nఉదాహరణ ఫలితం: SUS score = 78.\n\nNPS:\n\nBanking app ను ఇతరులకు సిఫార్సు చేసే అవకాశం ఎంత అని users ను అడగడం.\n\nఅనుకోండి:\n- Promoters = 60%.\n- Passives = 25%.\n- Detractors = 15%.\n- NPS = 60 − 15 = 45\n\n(ఉదాహరణ scores. SUS score 78 అంటే 78% usability అని కాదు.)',
  iv='SUS usability ని, NPS loyalty / సిఫార్సు అవకాశాన్ని కొలుస్తుంది – రెండూ వేర్వేరు ప్రశ్నలకు సమాధానాలు.'),
87: dict(q='Task Success Rate మరియు Completion Rate మధ్య తేడా ఏమిటి?',
  tbl=[['విజయవంతంగా లక్ష్యం సాధించడాన్ని కొలుస్తుంది','ముగింపు స్థానానికి చేరడాన్ని కొలుస్తుంది'],['Success ప్రమాణాలు అవసరం','నిర్ణీత completion point అవసరం'],['Task సరిగ్గా జరిగిందా అని పరిగణిస్తుంది','Process పూర్తయిందా అని మాత్రమే పరిగణించవచ్చు'],['పాక్షిక, విఫల tasks ను వేరు చేయగలదు','తరచుగా పూర్తయిందా లేదా అనే దానిపై'],['ఉదా: సరైన payment','ఉదా: Payment confirmation కు చేరడం']],
  ex='E-commerce Checkout:\n\n100 మంది users checkout మొదలుపెట్టారు.\n- 80 మంది తుది confirmation screen కు చేరారు.\n- 70 మంది సరైన payment, సరైన వివరాలతో order పూర్తి చేశారు.\n\nCompletion Rate: 80%.\n\nTask Success Rate: 70%.\n\n(ఉదాహరణ మాత్రమే; metric నిర్వచనాలు experiment యొక్క కొలత నియమాలపై ఆధారపడతాయి.)',
  iv='Completion rate "చివరికి చేరారా"; Task success rate "సరిగ్గా లక్ష్యం సాధించారా".'),
88: dict(q='Error Rate మరియు Task Failure Rate మధ్య తేడా ఏమిటి?',
  tbl=[['Interaction సమయంలో తప్పులను కొలుస్తుంది','విఫలమైన task ఫలితాలను కొలుస్తుంది'],['సరిదిద్దగల errors కూడా ఉండవచ్చు','Task వైఫల్యంపై దృష్టి'],['ఒక task లో అనేక errors రావచ్చు','సాధారణంగా విజయం లేదా వైఫల్యం కొలుస్తుంది'],['Interaction సమస్యలను గుర్తించడంలో సహాయం','మొత్తం task విఫలమయ్యే చోటును గుర్తించడంలో సహాయం'],['ఉదా: తప్పు OTP ప్రయత్నాలు','ఉదా: Transfer పూర్తి చేయలేకపోవడం']],
  ex='Banking App:\n\n100 మంది users money transfer ప్రయత్నించారు.\n- 25 తప్పు OTP ప్రయత్నాలు జరిగాయి.\n- 10 మంది చివరికి transfer పూర్తి చేయలేకపోయారు.\n\nError Rate: నిర్ణయించిన కొలత యూనిట్ (ఒక task కు errors లేదా ఒక user కు errors) పై ఆధారపడుతుంది.\n\nTask Failure Rate: 10%.',
  iv='Error rate మధ్యలో జరిగే తప్పులను; task failure rate పూర్తిగా విఫలమైన tasks ను చూపిస్తుంది.'),
89: dict(q='Qualitative Feedback మరియు Quantitative Metrics మధ్య తేడా ఏమిటి?',
  tbl=[['ఎందుకు, ఎలా అని వివరిస్తుంది','ఎంత, ఎంత తరచుగా అని కొలుస్తుంది'],['మాటలు, పరిశీలనలు','సంఖ్యలు, గణాంకాలు'],['Interviews, observations','Analytics, structured surveys'],['ప్రేరణలు, సమస్యలను గుర్తిస్తుంది','Patterns, trends ను కొలుస్తుంది'],['లోతైన సందర్భం ఇస్తుంది','కొలవగల ఆధారాలు ఇస్తుంది']],
  ex='E-commerce Checkout:\n\nQualitative Feedback:\n\nUsers ఇలా అంటారు:\n\n"App నా address ను మళ్లీ ఎందుకు అడుగుతోందో అర్థం కావడం లేదు." – సమాచారాన్ని మళ్లీ మళ్లీ నమోదు చేయాల్సి రావడంపై అసహనాన్ని ఇది చూపిస్తుంది.\n\nQuantitative Metrics:\n\nAnalytics ఇలా చూపిస్తుంది:\n- 35% checkout abandonment.\n- 20% users address entry వద్ద వెళ్లిపోతున్నారు.\n- సగటు checkout సమయం: 3 నిమిషాలు.\n\nఈ రెండూ కలిపి చూస్తే address-entry అనుభవాన్ని మెరుగుపరచాలని తెలుస్తుంది.',
  iv='Qualitative "ఎందుకు", Quantitative "ఎంత" – రెండింటినీ కలిపితే నమ్మదగిన నిర్ణయం.'),
90: dict(q='First-Click Testing మరియు Tree Testing మధ్య తేడా ఏమిటి?',
  tbl=[['మొదటి navigation నిర్ణయాన్ని అంచనా వేస్తుంది','మొత్తం navigation hierarchy ని అంచనా వేస్తుంది'],['మొదటి click ఖచ్చితత్వంపై దృష్టి','కనుగొనగలగడం (findability) పై దృష్టి'],['Visual interfaces ఉపయోగించవచ్చు','సాధారణంగా text మాత్రమే ఉన్న నిర్మాణాలు'],['తప్పుదారి పట్టించే entry points ను గుర్తిస్తుంది','Navigation hierarchy సమస్యలను గుర్తిస్తుంది'],['ఉదా: Search button కనుగొనడం','ఉదా: Product category కనుగొనడం']],
  ex='E-commerce Website:\n\nFirst-Click Testing:\n\nTask: "Order tracking option ను కనుగొనండి."\n\nWebsite homepage చూపించి user మొదట ఎక్కడ click చేస్తున్నారో గమనించడం.\n\nTree Testing:\n\nఅదే task ను text hierarchy తో ఇవ్వడం:\n- Home → Products\n- Home → My Account → Orders\n- Home → My Account → Addresses\n- Home → My Account → Payments\n- Home → Support\n\nUser My Account → Orders ను కనుగొంటున్నారో గమనించడం.',
  iv='First-click testing ప్రారంభ navigation నిర్ణయాన్ని; tree testing మొత్తం information architecture ని validate చేస్తుంది.'),
}
TE_FIX = {81: [('ప్రత్యక్షంగా అర్థం చేసుకోవడం. A/B Testing:', 'ప్రత్యక్షంగా అర్థం చేసుకోవడం.\n\nA/B Testing:')]}
EX_FIX = {86: [('NP S =', 'NPS =')]}
EX_EN = {90: 'First-Click Testing:\n\nTask: "Find the order tracking option."\n\nShow the website homepage and observe where the user clicks first.\n\nTree Testing:\n\nGive the same task using a text hierarchy:\n- Home → Products\n- Home → My Account → Orders\n- Home → My Account → Addresses\n- Home → My Account → Payments\n- Home → Support\n\nObserve whether the user finds My Account → Orders.'}
INTRO_TE = 'ఈ గ్రూప్‌లో మనం రూపొందించిన Design నిజంగా వినియోగదారులకు ఉపయోగపడుతోందా? వారు సులభంగా పనులు పూర్తి చేయగలుగుతున్నారా? ఎక్కడ ఇబ్బందులు ఎదుర్కొంటున్నారు? అనే విషయాలను పరీక్షించడం నేర్చుకుందాం. UX Interviews లో ఈ గ్రూప్ చాలా ముఖ్యమైనది. ముఖ్యంగా Senior UX Designer, Lead Product Designer మరియు Principal Designer పాత్రలకు.'
PRACTICE_TITLE = 'Practical Interview Exercise – UX Evaluation Knowledge Check'
PRACTICE_BODY = '''Scenario: You are redesigning the checkout process of an e-commerce application.
సందర్భం: మీరు ఒక e-commerce app లో checkout process ను redesign చేస్తున్నారు.

1. You want to understand why users abandon checkout. Which method would you choose? (Usability Testing / A/B Testing / NPS)
2. You want to compare two checkout button designs using conversion data. (Cognitive Walkthrough / A/B Testing / Card Sorting)
3. You want to evaluate a design against Nielsen's 10 principles. (Tree Testing / Heuristic Evaluation / First-Click Testing)
4. You want to measure how easily users can find a category in a navigation hierarchy. (Tree Testing / NPS / SUS)
5. You want to measure whether users can complete checkout correctly. (NPS / Task Success Rate / Hover State)

### Answer key · జవాబులు
1. Usability Testing · 2. A/B Testing · 3. Heuristic Evaluation · 4. Tree Testing · 5. Task Success Rate'''
