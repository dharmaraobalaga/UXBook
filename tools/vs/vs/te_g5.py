# Group 5 – Telugu tables, examples, interview meanings (written by Claude from the PDF's English)
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

T = {
56: dict(q='Interaction Design మరియు Visual Design మధ్య తేడా ఏమిటి?',
  tbl=[['ఎలా పనిచేస్తుందో దృష్టి','ఎలా కనిపిస్తుందో దృష్టి'],['User చర్యలను design చేస్తుంది','Visual elements ను design చేస్తుంది'],['Interaction ప్రవర్తనను నిర్ణయిస్తుంది','Visual ప్రదర్శనను నిర్ణయిస్తుంది'],['Transitions, feedback ఉంటాయి','రంగులు, typography ఉంటాయి'],['Interaction అనుభవాన్ని మెరుగుపరుస్తుంది','Visual communication ను మెరుగుపరుస్తుంది']],
  ex='Banking App:\n- Interaction Design: User "Transfer Money" నొక్కి, amount నమోదు చేసి, transaction confirm చేసి, success feedback పొందుతారు.\n- Visual Design: Transfer button రంగు, typography, amount field layout, icons మరియు confirmation screen రూపం.',
  iv='Interaction Design "ఎలా పనిచేస్తుంది", Visual Design "ఎలా కనిపిస్తుంది" – మంచి product కు రెండూ కలిసి పనిచేయాలి.'),
57: dict(q='Interaction Design మరియు UI Design మధ్య తేడా ఏమిటి?',
  tbl=[['Interaction ప్రవర్తనపై దృష్టి','Interface design పై దృష్టి'],['చర్య మరియు స్పందనను నిర్ణయిస్తుంది','Interface elements ను నిర్ణయిస్తుంది'],['Feedback, transitions ఉంటాయి','Buttons, forms, icons ఉంటాయి'],['Visual screens కు మించి విస్తరించవచ్చు','ప్రధానంగా digital interfaces కు సంబంధించినది'],['Interaction logic కు ప్రాధాన్యత','Visual మరియు interaction నిర్ణయాలను కలుపుతుంది']],
  ex='Mobile Login:\n- Interaction Design: తప్పు OTP నమోదు చేస్తే ఏమి జరుగుతుంది? User కొత్త OTP ఎప్పుడు అడగవచ్చు?\n- UI Design: OTP screen ఎలా కనిపిస్తుంది? Input boxes, button styles, error message రంగులు ఏమిటి?',
  iv='Interaction Design ప్రవర్తన, logic ని; UI Design interface elements రూపాన్ని నిర్ణయిస్తుంది.'),
58: dict(q='Static Design మరియు Interactive Design మధ్య తేడా ఏమిటి?',
  tbl=[['Interactive కాదు','User చర్యలకు స్పందిస్తుంది'],['Visual రూపాన్ని చూపిస్తుంది','ప్రవర్తన, interactions చూపిస్తుంది'],['Navigation simulation లేదు','Navigation simulation ఉంటుంది'],['Visual reviews కోసం','అనుభవ validation కోసం'],['ఉదా: Static mockup','ఉదా: Clickable prototype']],
  ex='E-commerce App:\n- Static Design: Image, ధర, rating మరియు Add to Cart button ఉన్న product details screen.\n- Interactive Design: Add to Cart నొక్కితే cart count update అయి confirmation message కనిపిస్తుంది.',
  iv='Static design రూపాన్ని review చేయడానికి; interactive design అనుభవాన్ని validate చేయడానికి.'),
59: dict(q='Wireframe మరియు Wireflow మధ్య తేడా ఏమిటి?',
  tbl=[['ఒక screen నిర్మాణంపై దృష్టి','అనుసంధానించిన అనేక screens పై దృష్టి'],['Layout, content చూపిస్తుంది','Layout మరియు interaction క్రమాన్ని చూపిస్తుంది'],['సాధారణంగా ఒకసారి ఒక screen','End-to-end flow ను సూచిస్తుంది'],['Screen నిర్మాణం design చేయడంలో సహాయం','Screens మధ్య సంబంధాలను తెలియజేస్తుంది'],['స్వతంత్రంగా ఉండవచ్చు','Screens ను flow connections తో కలుపుతుంది']],
  ex='Registration App:\n- Wireframe: Name, email, password మరియు Submit button ఉన్న mobile registration screen design చేయడం.\n- Wireflow: Registration → OTP Verification → Profile Setup → Welcome Screen ను కలపడం.',
  iv='Wireframe ఒక screen; Wireflow అనుసంధానించిన screens మరియు వాటి మధ్య కదలిక.'),
60: dict(q='Prototype మరియు MVP మధ్య తేడా ఏమిటి?',
  tbl=[['ఆలోచనలను అన్వేషించి validate చేయడానికి','Market లో product ను validate చేయడానికి'],['పనిచేయకపోయినా (non-functional) ఉండవచ్చు','పనిచేసే functionality తప్పనిసరి'],['తాత్కాలికం కావచ్చు','నిజమైన వినియోగం కోసం'],['తరచుగా development కు ముందు','Development ద్వారా విడుదల'],['ప్రధానంగా design assumptions test చేస్తుంది','Product విలువ, market assumptions test చేస్తుంది']],
  ex='Food Delivery App:\n\nPrototype:\n\nRestaurant discovery, cart, checkout మరియు payment confirmation screens ను చూపించే Figma prototype.\n\nMVP:\n\nనిజమైన users register అయి, food order చేసి, pay చేసి, deliveries track చేయగల పనిచేసే application.',
  iv='Prototype design ఆలోచనను test చేస్తుంది; MVP నిజమైన users తో product విలువను test చేస్తుంది.'),
61: dict(q='Low-Fidelity Prototype మరియు High-Fidelity Prototype మధ్య తేడా ఏమిటి?',
  tbl=[['ప్రాథమిక నిర్మాణం','వివరమైన visual design'],['సరళమైన interactions','వాస్తవిక interactions'],['త్వరగా తయారు చేయవచ్చు','ఎక్కువ శ్రమ అవసరం'],['ప్రారంభ అన్వేషణకు','వివరమైన validation కు'],['తక్కువ visual polish','తుది product అనుభవానికి దగ్గరగా']],
  ex='Mobile Banking:\n\n' + fig('g5-lofi-hifi-prototype', 'Three linked screens as a low-fidelity prototype and as a high-fidelity prototype', 'Low-Fidelity – ప్రాథమిక screen layouts, navigation. High-Fidelity – వివరమైన UI, వాస్తవిక interactions.', 'Low-fidelity: basic screen layouts and navigation. High-fidelity: detailed UI and realistic interactions.'),
  iv='ప్రారంభ ఆలోచనలకు low-fidelity, తుది validation కు high-fidelity prototypes ఉపయోగిస్తాను.'),
62: dict(q='Clickable Prototype మరియు Functional Prototype మధ్య తేడా ఏమిటి?',
  tbl=[['Navigation ను simulate చేస్తుంది','Functional ప్రవర్తనను చూపిస్తుంది'],['తరచుగా Figma లో తయారు చేస్తారు','తరచుగా code లేదా functional tools తో'],['Link చేసిన screens ఉపయోగిస్తుంది','పనిచేసే components ఉండవచ్చు'],['పరిమిత logic ఉండవచ్చు','మరింత వాస్తవిక logic ఉంటుంది'],['Navigation, layout ను validate చేస్తుంది','Functional సాధ్యాసాధ్యాలను validate చేస్తుంది']],
  ex='Login Screen:\n\nClickable Prototype:\n\nClick Login → OTP Screen → Dashboard.\n\nFunctional Prototype:\n- Mobile number నమోదు.\n- Input ను validate చేయడం.\n- OTP generate లేదా simulate చేయడం.\n- నమోదు చేసిన OTP ని verify చేయడం.\n- Success లేదా error state చూపించడం.',
  iv='Clickable prototype navigation ను; functional prototype నిజమైన logic, సాధ్యాసాధ్యాలను validate చేస్తుంది.'),
63: dict(q='Microinteractions మరియు Animations మధ్య తేడా ఏమిటి?',
  tbl=[['చిన్న user interactions పై దృష్టి','Visual కదలికపై దృష్టి'],['సాధారణంగా user చర్యతో మొదలవుతాయి','User చర్యతో లేదా స్వయంచాలకంగా'],['System feedback ను తెలియజేస్తాయి','కదలిక లేదా transitions ను తెలియజేయవచ్చు'],['నిర్దిష్ట interaction ఉద్దేశం ఉంటుంది','Functional లేదా అలంకార ఉద్దేశం ఉండవచ్చు'],['ఉదా: Like button feedback','ఉదా: Page transition animation']],
  ex='Social Media App:\n\nMicrointeraction:\n\nUser Like నొక్కుతారు → Heart icon state మారుతుంది → Like count update అవుతుంది.\n\nAnimation:\n\nHome Feed నుంచి Profile screen కు వెళ్లేటప్పుడు full-screen transition.',
  iv='ప్రతి microinteraction లో animation ఉండవచ్చు, కానీ ప్రతి animation microinteraction కాదు.'),
64: dict(q='Hover State మరియు Focus State మధ్య తేడా ఏమిటి?',
  tbl=[['Pointer స్థానంతో trigger అవుతుంది','Keyboard లేదా programmatic focus తో'],['సాధారణంగా mouse తో ఉపయోగిస్తారు','Keyboard accessibility కు ముఖ్యం'],['Pointer దూరమైతే మాయమవుతుంది','Focus వేరే చోటికి వెళ్లే వరకు ఉంటుంది'],['Pointer feedback ఇస్తుంది','ప్రస్తుత interactive స్థానాన్ని చూపిస్తుంది'],['Focus కు ప్రత్యామ్నాయం కాదు','స్పష్టంగా కనిపించాలి']],
  ex='Website Button:\n- Hover: User mouse ను Submit పైకి తీసుకెళ్తారు → Button background ముదురుగా మారుతుంది.\n- Focus: User Tab నొక్కుతారు → Submit button కు కనిపించే outline వస్తుంది.',
  iv='Keyboard users కోసం focus state తప్పనిసరిగా స్పష్టంగా కనిపించాలి; hover దానికి ప్రత్యామ్నాయం కాదు.'),
65: dict(q='Active State మరియు Selected State మధ్య తేడా ఏమిటి?',
  tbl=[['ప్రస్తుత interaction ను సూచిస్తుంది','User ఎంపికను సూచిస్తుంది'],['తరచుగా తాత్కాలికం','మార్చే వరకు ఉంటుంది'],['నొక్కుతున్నప్పుడు లేదా activate చేసేటప్పుడు','ఒక option ఎంచుకున్న తర్వాత'],['ఉదా: నొక్కిన button','ఉదా: ఎంచుకున్న radio option'],['చర్య స్థితిని సూచిస్తుంది','ఎంపిక స్థితిని సూచిస్తుంది']],
  ex='Music App:\n- Active State: User Play button నొక్కినప్పుడు అది దృశ్యంగా స్పందిస్తుంది.\n- Selected State: User "Podcasts" tab ఎంచుకుంటారు; ఆ section చూస్తున్నంత సేపు అది selected గా ఉంటుంది.',
  iv='Active అనేది నొక్కుతున్న క్షణం; Selected అనేది ఎంచుకున్న తర్వాత కొనసాగే స్థితి.'),
66: dict(q='Modal మరియు Dialog మధ్య తేడా ఏమిటి?',
  tbl=[['Interaction ప్రవర్తనను వివరిస్తుంది','ఒక UI component ను వివరిస్తుంది'],['వెనుక interaction ను block చేస్తుంది','Modal లేదా non-modal కావచ్చు'],['User దృష్టిని కేంద్రీకరిస్తుంది','సమాచారం ఇస్తుంది లేదా చర్య అడుగుతుంది'],['తరచుగా overlay ఉపయోగిస్తుంది','Modal లేదా non-modal window గా రావచ్చు'],['ఉదా: Blocking checkout overlay','ఉదా: Confirmation dialog']],
  ex='Banking App:\n\nModal:\n\nపూర్తి screen ను block చేసే payment verification interface.\n\nDialog:\n\n"మీరు ఈ transaction ను cancel చేయాలనుకుంటున్నారా?"\n\nButtons: Cancel / Continue.',
  iv='Modal అనేది ప్రవర్తన (వెనుక భాగాన్ని block చేయడం); Dialog అనేది component – అది modal లేదా non-modal కావచ్చు.'),
67: dict(q='Modal మరియు Bottom Sheet మధ్య తేడా ఏమిటి?',
  tbl=[['మధ్యలో లేదా full-screen గా రావచ్చు','కింది నుంచి వస్తుంది'],['Desktop, mobile రెండింటిలో సాధారణం','Mobile interfaces లో సాధారణం'],['సంక్లిష్ట interactions ఉండవచ్చు','తరచుగా సందర్భ చర్యలు ఉంటాయి'],['వెనుక interaction ను block చేయవచ్చు','Modal లేదా non-modal కావచ్చు'],['ఉదా: Payment confirmation','ఉదా: Share లేదా filter options']],
  ex='Food Delivery App:\n\nModal:\n\n"మీరు మీ order ను cancel చేయాలనుకుంటున్నారా?"\n\nBottom Sheet:\n\nUser Filter నొక్కుతారు → Bottom Sheet ఇవి చూపిస్తుంది:\n- Price Range.\n- Rating.\n- Delivery Time.\n- Apply Filters.',
  iv='ముఖ్యమైన నిర్ణయాలకు modal; mobile లో సందర్భ ఎంపికలకు bottom sheet బాగా సరిపోతుంది.'),
68: dict(q='Tooltip మరియు Popover మధ్య తేడా ఏమిటి?',
  tbl=[['చిన్న సమాచారం ఇస్తుంది','మరింత విస్తృత సందర్భ content ఇస్తుంది'],['సాధారణంగా text మాత్రమే','Interactive elements ఉండవచ్చు'],['తరచుగా hover లేదా focus తో వస్తుంది','సాధారణంగా click తో వస్తుంది'],['తేలికైనది','మరింత సంక్లిష్టం'],['ఉదా: Icon వివరణ','ఉదా: Profile settings panel']],
  ex='Dashboard:\n- Tooltip: Information icon పై hover → "Monthly revenue అంటే మొత్తం sales."\n- Popover: Profile icon నొక్కితే → Profile వివరాలు, account settings, logout action చూపిస్తుంది.',
  iv='చిన్న వివరణకు tooltip; చర్యలు ఉన్న విస్తృత content కు popover.'),
69: dict(q='Accordion మరియు Tabs మధ్య తేడా ఏమిటి?',
  tbl=[['Content ను విస్తరించి, ముడుచుకుంటుంది','Content panels మధ్య మారుస్తుంది'],['అనేక sections ఒకేసారి చూపించవచ్చు','సాధారణంగా ఒకసారి ఒక panel'],['పొడవైన content కు ఉపయోగకరం','సంబంధిత categories కు ఉపయోగకరం'],['ప్రారంభ content సాంద్రతను తగ్గిస్తుంది','Category వారీగా content ను క్రమబద్ధం చేస్తుంది'],['ఉదా: FAQs','ఉదా: Product Details మరియు Reviews']],
  ex='E-commerce Product Page:\n\nAccordion:\n- Product Description.\n- Specifications.\n- Warranty.\n- Delivery Information.\n\nTabs:\n- Overview.\n- Specifications.\n- Reviews.\n- Q&A.',
  iv='పొడవైన, ఒకదాని కింద ఒకటి చదివే content కు accordion; సమాన స్థాయి categories మధ్య మారడానికి tabs.'),
70: dict(q='Toggle మరియు Checkbox మధ్య తేడా ఏమిటి?',
  tbl=[['ఒక setting ను On లేదా Off చేస్తుంది','ఒక option ను ఎంచుకుంటుంది లేదా తీసేస్తుంది'],['తరచుగా వెంటనే అమలవుతుంది','తరచుగా forms లో ఉపయోగిస్తారు'],['Active స్థితిని తెలియజేస్తుంది','Selected స్థితిని తెలియజేస్తుంది'],['సాధారణంగా ఒక control కు ఒక setting','అనేక ఎంపికల కోసం గ్రూప్ చేయవచ్చు'],['ఉదా: Dark Mode','ఉదా: ఆసక్తులు ఎంచుకోవడం']],
  ex='Mobile App:\n\nToggle:\n\nPush Notifications ను enable చేయడం.\n\nCheckbox:\n\nఇష్టమైన communication channels ఎంచుకోండి:\n- Email.\n- SMS.\n- WhatsApp.',
  iv='వెంటనే అమలయ్యే on/off setting కు toggle; form లో ఒకటి లేదా అనేక ఎంపికలకు checkbox.'),
71: dict(q='Radio Button మరియు Checkbox మధ్య తేడా ఏమిటి?',
  tbl=[['ఒకే ఎంపిక','అనేక ఎంపికలు'],['Options పరస్పరం ప్రత్యేకమైనవి','Options స్వతంత్రమైనవి'],['ఒక group కు ఒక ఎంపిక','ఒకటి లేదా అంతకంటే ఎక్కువ'],['తప్పనిసరి group లో వేరేది ఎంచుకోకుండా ఉన్న ఒక్క ఎంపికను తీసేయలేము','స్వతంత్రంగా uncheck చేయవచ్చు'],['ఉదా: Payment Method','ఉదా: ఇష్టమైన Categories']],
  ex='Shopping App:\n\nRadio Buttons:\n\nPayment Method ఎంచుకోండి:\n- UPI.\n- Credit Card.\n- Net Banking.\n- Cash on Delivery.\n\nCheckboxes:\n\nఆసక్తులు ఎంచుకోండి:\n- Electronics.\n- Fashion.\n- Sports.\n- Books.',
  iv='ఒక్కటే ఎంచుకోవాల్సినప్పుడు radio buttons; అనేకం ఎంచుకోవచ్చినప్పుడు checkboxes.'),
72: dict(q='Responsive Design మరియు Adaptive Design మధ్య తేడా ఏమిటి?',
  tbl=[['అందుబాటులో ఉన్న స్థలానికి సాఫీగా సర్దుకుంటుంది','ముందే నిర్ణయించిన layouts నుంచి ఎంచుకుంటుంది'],['Flexible layouts ఉపయోగిస్తుంది','నిర్దిష్ట layout breakpoints ఉపయోగిస్తుంది'],['నిరంతర సర్దుబాటు','విడివిడి layout మార్పులు'],['ఒకే flexible layout system','అనేక ప్రత్యేక layouts'],['విస్తృత screens కు సరిపోతుంది','నిర్దిష్ట device అనుభవాలు అవసరమైనప్పుడు ఉపయోగకరం']],
  ex="D'SARAS Website:\n\nResponsive:\n\nViewport desktop నుంచి tablet, mobile కు మారుతున్న కొద్దీ అదే website layout సాఫీగా సర్దుకుంటుంది.\n\nAdaptive:\n\nDesktop, tablet మరియు mobile screen categories కోసం వేర్వేరుగా ముందే design చేసిన layouts.",
  iv='విస్తృత screens కు responsive design; నిర్దిష్ట device అనుభవాలు అవసరమైనప్పుడు adaptive design.'),
73: dict(q='Progressive Disclosure మరియు Progressive Enhancement మధ్య తేడా ఏమిటి?',
  tbl=[['UX design technique','Web development వ్యూహం'],['సమాచారం ఎంత కనిపించాలో నియంత్రిస్తుంది','Technical సామర్థ్యాలను పెంచుతుంది'],['Cognitive load ను తగ్గిస్తుంది','Accessibility, compatibility ని మెరుగుపరుస్తుంది'],['అవసరమైనప్పుడు advanced options చూపిస్తుంది','మద్దతు ఉన్నప్పుడు advanced functionality జోడిస్తుంది'],['ఉదా: Advanced settings','ఉదా: JavaScript తో మెరుగుపడిన form']],
  ex='Banking App:\n\nProgressive Disclosure:\n\nMoney-transfer screen మొదట ఇవి మాత్రమే చూపిస్తుంది:\n- Beneficiary.\n- Amount.\n- Continue.\n\nTransaction limits, charges, reference notes వంటి అదనపు వివరాలు అవసరమైనప్పుడు కనిపిస్తాయి.\n\nProgressive Enhancement:\n\nప్రాథమిక transfer సమాచార page సాధారణ HTML తో పనిచేస్తుంది; మద్దతు ఉన్న browsers కు interactive validation, dynamic updates వంటి అదనపు మెరుగుదలలు వస్తాయి.',
  iv='Progressive Disclosure UX technique (సమాచారాన్ని దశలవారీగా చూపించడం); Progressive Enhancement development వ్యూహం (ప్రాథమిక స్థాయి నుంచి మెరుగుదలలు జోడించడం).'),
74: dict(q='Affordance మరియు Signifier మధ్య తేడా ఏమిటి?',
  tbl=[['సాధ్యమైన చర్యను సూచిస్తుంది','ఆ చర్యను ఎలా చేయాలో తెలియజేస్తుంది'],['చర్య సాధ్యతకు సంబంధించినది','Visual లేదా గ్రహించగల సూచనలకు సంబంధించినది'],['స్పష్టమైన సూచన లేకుండానూ ఉండవచ్చు','చర్యను సులభంగా కనుగొనేలా చేస్తుంది'],['ఉదా: Click చేయగల button','ఉదా: Button label "Submit"'],['Interaction సామర్థ్యం','Interaction మార్గదర్శనం']],
  ex='Mobile App:\n- Affordance: Text field లో user సమాచారం నమోదు చేయవచ్చు.\n- Signifier: "Enter your mobile number" placeholder text ఏ సమాచారం కావాలో సూచిస్తుంది.\n\nమరొక ఉదాహరణ:\n- Affordance: ఒక card click చేయగలిగేది కావచ్చు.\n- Signifier: Arrow icon మరియు "View Details" label ఆ card మరో screen తెరుస్తుందని సూచిస్తాయి.',
  iv='Affordance "ఏమి చేయవచ్చు", Signifier "ఎలా/ఎక్కడ చేయాలి" అని తెలియజేస్తుంది.'),
75: dict(q='Feedback మరియు Feedforward మధ్య తేడా ఏమిటి?',
  tbl=[['చర్య తర్వాత వస్తుంది','చర్యకు ముందు వస్తుంది'],['ఫలితాన్ని తెలియజేస్తుంది','ఏమి జరుగుతుందో వివరిస్తుంది'],['System స్పందనను నిర్ధారిస్తుంది','User ప్రవర్తనకు మార్గదర్శనం చేస్తుంది'],['ఫలితాలను అర్థం చేసుకోవడంలో సహాయం','తప్పులు నివారించడంలో సహాయం'],['ఉదా: Payment Successful','ఉదా: "మీకు ₹500 charge అవుతుంది"']],
  ex='Banking App:\n\nFeedforward:\n\nPayment confirm చేసే ముందు:\n\n"₹5,000 రమేష్ కుమార్‌కు transfer అవుతుంది. ₹5 transaction fee వర్తించవచ్చు."\n\nFeedback:\n\nPayment పూర్తయిన తర్వాత:\n\n"మీ ₹5,000 transfer విజయవంతమైంది. Transaction ID: XXXX."',
  iv='Feedforward చర్యకు ముందు ఏమి జరుగుతుందో చెప్పి తప్పులను నివారిస్తుంది; Feedback చర్య తర్వాత ఫలితాన్ని నిర్ధారిస్తుంది.'),
}
EX_EN = {
61: fig('g5-lofi-hifi-prototype', 'Low- and high-fidelity prototypes for mobile banking', '', 'Mobile banking.') + '\n\nLow-Fidelity\tHigh-Fidelity\nBasic screen layouts and navigation.\tDetailed UI and realistic interactions.',
}
# Q71 table: one row wrapped across two lines in the PDF
ROWS_EN = {71: [['Single selection', 'Multiple selections'], ['Options are mutually exclusive', 'Options are independent'], ['One choice per group', 'One or more choices'],
                ['Cannot deselect the only selected option in a required group without choosing another', 'Can be unchecked independently'], ['Example: Payment Method', 'Example: Preferred Categories']]}
INTRO_TE = 'ఈ గ్రూప్‌లో ఒక యాప్ లేదా వెబ్‌సైట్‌లో యూజర్ చేసే ప్రతి చర్యకు డిజైన్ ఎలా స్పందించాలి? Buttons, Forms, Modals, Tabs, Toggles, Animations మరియు Responsive Layouts ఎలా పనిచేయాలి? అనే విషయాలను నేర్చుకుందాం. ఇది ముఖ్యంగా Figma, Interaction Design, Prototyping మరియు Product Design ఇంటర్వ్యూలకు చాలా ఉపయోగపడుతుంది.'
PRACTICE_TITLE = 'Practical Interview Exercise – UX Interaction Design Quiz'
PRACTICE_BODY = '''Apply these concepts to a mobile banking application.
ఈ concepts ను ఒక mobile banking app కు అన్వయించండి.

1. Which design pattern is appropriate for showing additional filter options from the bottom of a mobile screen? (Tooltip / Bottom Sheet / Accordion)
2. Which state should be visible when navigating with the keyboard? (Hover State / Focus State / Active State)
3. Which concept tells users what will happen before confirming a transaction? (Feedback / Feedforward / Animation)
4. Which control allows users to select only one payment method? (Checkbox / Toggle / Radio Button)
5. Which concept communicates how a button should be used through a label or icon? (Affordance / Signifier / Prototype)

### Answer key · జవాబులు
1. Bottom Sheet · 2. Focus State · 3. Feedforward · 4. Radio Button · 5. Signifier'''
