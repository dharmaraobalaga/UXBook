# Group 3 – Telugu tables, examples and interview-answer meanings (written by Claude from the PDF's English)
def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

T = {
26: dict(q='Task Flow మరియు User Flow మధ్య తేడా ఏమిటి?',
  tbl=[['ఒక నిర్దిష్ట task పై దృష్టి','లక్ష్యం వైపు మొత్తం interaction మార్గంపై దృష్టి'],['సాధారణంగా linear (ఒకే వరుస)','అనేక శాఖలు (branches) ఉండవచ్చు'],['Task steps చూపిస్తుంది','Screens, నిర్ణయాలు, interactions చూపిస్తుంది'],['సరళమైన రూపం','మరింత సమగ్రమైన రూపం'],['ఉదా: Login process','ఉదా: Account ను access చేసే వివిధ మార్గాలు']],
  ex='Banking App – Money Transfer:\n\n' + fig('g3-task-flow', 'Task flow: Open Banking App, Login, Select Beneficiary, Enter Amount, Confirm Transfer, Transaction Successful', 'Task Flow – ఒకే వరుసలో సరళమైన దశలు.', 'Task Flow: a simple linear flow.') +
     '\n\n' + fig('g3-user-flow', 'User flow with Existing Beneficiary and New Beneficiary branches', 'User Flow – Existing Beneficiary / New Beneficiary అనే ప్రత్యామ్నాయ మార్గాలతో.', 'User Flow: with alternative paths.') +
     '\n\nTask Flow ప్రాథమిక transfer దశలను మాత్రమే చూపిస్తుంది; User Flow beneficiary ఇప్పటికే ఉన్నారా లేదా కొత్తగా జోడించాలా అనే నిర్ణయాన్ని కూడా చూపిస్తుంది.',
  iv='Money transfer task flow ప్రాథమిక దశలను చూపిస్తుంది; user flow beneficiary ఇప్పటికే ఉన్నారా, కొత్తగా జోడించాలా అనే పరిస్థితులను కూడా పరిగణిస్తుంది.'),
27: dict(q='User Flow మరియు User Journey మధ్య తేడా ఏమిటి?',
  tbl=[['Product interactions పై దృష్టి','మొత్తం అనుభవంపై దృష్టి'],['Screens మరియు navigation చూపిస్తుంది','దశలు (stages) మరియు touchpoints చూపిస్తుంది'],['నిర్ణయాలు, actions ఉంటాయి','భావోద్వేగాలు, అంచనాలు ఉంటాయి'],['సాధారణంగా ఒక product కు ప్రత్యేకం','Online మరియు offline అనుభవాలు ఉండవచ్చు'],['Navigation మెరుగుపరచడానికి','మొత్తం అనుభవాన్ని మెరుగుపరచడానికి']],
  ex='Online Shopping:\n\nUser Flow:\n\nOpen App → Search Product → Product Details → Add to Cart → Checkout → Payment → Order Confirmation.\n\nUser Journey:\n\nదశ\tవినియోగదారు అనుభవం\tభావన\nఅవసరం గుర్తించడం\tMobile కొనాలనుకుంటారు\tఆసక్తి\nProduct కనుగొనడం\tవివిధ models వెతుకుతారు\tకుతూహలం\nపోలిక\tFeatures, ధరలను పోలుస్తారు\tగందరగోళం\nకొనుగోలు\tPayment పూర్తి చేస్తారు\tనమ్మకం\nDelivery\tOrder ను track చేస్తారు\tఉత్సాహం\nకొనుగోలు తర్వాత\tProduct అందుకుంటారు\tసంతృప్తి',
  iv='User Flow ఒక digital product లో లక్ష్యం సాధించే navigation ను చూపిస్తుంది; User Journey అన్ని దశల్లో ఆలోచనలు, భావోద్వేగాలు, touchpoints మరియు pain points తో మొత్తం అనుభవాన్ని చూపిస్తుంది.'),
28: dict(q='User Journey మరియు Customer Journey మధ్య తేడా ఏమిటి?',
  tbl=[['Product వినియోగంపై దృష్టి','మొత్తం brand సంబంధంపై దృష్టి'],['వినియోగదారుల interactions','Customer lifecycle'],['Product లేదా service కు పరిమితం','Marketing, sales, support కూడా కలిపి'],['Product అనుభవాన్ని మెరుగుపరుస్తుంది','మొత్తం customer అనుభవాన్ని మెరుగుపరుస్తుంది'],['UX teams ఉపయోగిస్తాయి','CX, marketing మరియు UX teams ఉపయోగిస్తాయి']],
  ex='Food Delivery App:\n\nUser Journey:\n\nOpen App → Search Restaurant → Select Food → Place Order → Track Delivery → Rate Food.\n\nCustomer Journey:\n- Awareness: ఒక ప్రకటన చూస్తారు.\n- Consideration: Food delivery platforms ను పోలుస్తారు.\n- Acquisition: App download చేసి register అవుతారు.\n- Purchase: మొదటి order ఇస్తారు.\n- Retention: App ను క్రమం తప్పకుండా ఉపయోగిస్తారు.\n- Loyalty: App ను స్నేహితులకు సిఫార్సు చేస్తారు.',
  iv='User Journey తరచుగా మొత్తం Customer Journey లో ఒక భాగం.'),
29: dict(q='Sitemap మరియు Information Architecture మధ్య తేడా ఏమిటి?',
  tbl=[['Pages hierarchy చూపిస్తుంది','మొత్తం సమాచార నిర్మాణాన్ని నిర్ణయిస్తుంది'],['Pages పై దృష్టి','Content, labels, సంబంధాలపై దృష్టి'],['ఒక visual deliverable','విస్తృతమైన design discipline'],['Website నిర్మాణాన్ని ప్లాన్ చేయడంలో సహాయం','కనుగొనడం (findability), navigation మెరుగుపరుస్తుంది'],['IA documentation లో ఒక భాగం','Sitemap, taxonomy, navigation అన్నీ కలిపి']],
  ex='E-commerce Website:\n\n' + fig('g3-sitemap', 'Sitemap: Home with Products, Offers and Account; below them Categories, Deals and Orders', 'Sitemap – Home కింద Products, Offers, Account పేజీలు.', 'Illustrative website sitemap.') +
     '\n\nInformation Architecture:\n- Products ను అర్థవంతమైన categories గా విభజించడం.\n- అర్థమయ్యే labels ఉపయోగించడం.\n- Product filters ను క్రమబద్ధం చేయడం.\n- Navigation hierarchy నిర్ణయించడం.\n- Users products ను సులభంగా కనుగొనగలిగేలా చూడటం.',
  iv='Sitemap అనేది ఆ నిర్మాణంలోని page hierarchy ని చూపించే ఒక deliverable మాత్రమే; IA విస్తృతమైన discipline.'),
30: dict(q='Sitemap మరియు Navigation Structure మధ్య తేడా ఏమిటి?',
  tbl=[['Pages మరియు వాటి సంబంధాలను చూపిస్తుంది','Users ఎలా navigate చేస్తారో నిర్ణయిస్తుంది'],['నిర్మాణం (structure) పై దృష్టి','యాక్సెస్ మరియు కదలికపై దృష్టి'],['Pages hierarchy ని map చేస్తుంది','Menus, tabs, links ను ప్లాన్ చేస్తుంది'],['ఎక్కువగా planning కోసం','నేరుగా interface లో కనిపిస్తుంది'],['ఏ pages ఉన్నాయో చూపిస్తుంది','Users వాటిని ఎలా చేరుకుంటారో చూపిస్తుంది']],
  ex='Corporate Website:\n\nSitemap:\n\nHome → About Us → Services → Portfolio → Contact.\n\nNavigation Structure:\n- Header navigation.\n- Services కింద dropdown menu.\n- Portfolio category tabs.\n- Footer links.\n- లోపలి pages కోసం breadcrumbs.',
  iv='Sitemap pages hierarchy ని నిర్ణయిస్తుంది; navigation structure users ఆ pages మధ్య ఎలా కదులుతారో నిర్ణయిస్తుంది.'),
31: dict(q='Card Sorting మరియు Tree Testing మధ్య తేడా ఏమిటి?',
  tbl=[['సమాచారాన్ని క్రమబద్ధం చేయడంలో సహాయం','నిర్మాణాన్ని test చేయడంలో సహాయం'],['IA design కు ముందు లేదా సమయంలో','IA ప్రతిపాదించిన తర్వాత'],['Users కంటెంట్‌ను గ్రూపులుగా విభజిస్తారు','Users సమాచారం కోసం వెతుకుతారు'],['Mental models ను గుర్తిస్తుంది','Findability ను కొలుస్తుంది'],['Categories సృష్టిస్తుంది లేదా మెరుగుపరుస్తుంది','Hierarchy ని validate చేస్తుంది']],
  ex='E-commerce Website:\n\nCard Sorting:\n\nUsers కు ఈ కార్డులు ఇవ్వండి:\n- Mobile Phones\n- Laptops\n- Headphones\n- Smart Watches\n- Chargers\n- Speakers\n\nవాటిని categories గా విభజించమని అడగండి.\n\nTree Testing:\n\nUsers కు ఈ task ఇవ్వండి:\n\n"₹2,000 లోపు wireless headphones కనుగొనండి."\n\nవారు సరైన category ద్వారా వెళ్లి సమాచారాన్ని కనుగొంటున్నారో గమనించండి.',
  iv='Card Sorting users సహజంగా సమాచారాన్ని ఎలా వర్గీకరిస్తారో చెబుతుంది; Tree Testing ఆ నిర్మాణంలో users సమాచారాన్ని కనుగొనగలరో అంచనా వేస్తుంది.'),
32: dict(q='Open Card Sorting మరియు Closed Card Sorting మధ్య తేడా ఏమిటి?',
  tbl=[['Users categories సృష్టిస్తారు','Categories ముందే నిర్ణయించబడి ఉంటాయి'],['అన్వేషణాత్మకం (exploratory)','మూల్యాంకనాత్మకం (evaluative)'],['Mental models కనుగొంటుంది','ఉన్న categories ను test చేస్తుంది'],['ప్రారంభ IA design కు ఉపయోగకరం','IA ను మెరుగుపరచడానికి ఉపయోగకరం'],['కొత్త labels చూపించవచ్చు','Label స్పష్టతను validate చేస్తుంది']],
  ex='Online Shopping App:\n\nOpen Card Sorting:\n\nUsers కు 20 product cards ఇచ్చి, వారి సొంత categories సృష్టించమని అడగండి.\n\nవారు ఇలా సృష్టించవచ్చు:\n- Electronics\n- Home Appliances\n- Personal Accessories\n\nClosed Card Sorting:\n\nముందే నిర్ణయించిన categories ఇవ్వండి:\n- Electronics\n- Fashion\n- Home & Kitchen\n\nప్రతి product ను సరైన category లో ఉంచమని users ను అడగండి.',
  iv='Open Card Sorting users mental models ను అర్థం చేసుకోవడానికి; Closed Card Sorting ఇప్పటికే ఉన్న categories ను validate చేయడానికి.'),
33: dict(q='Hierarchical Navigation మరియు Flat Navigation మధ్య తేడా ఏమిటి?',
  tbl=[['అనేక స్థాయిలు (levels)','తక్కువ స్థాయిలు'],['పెద్ద content కు సరిపోతుంది','చిన్న products కు సరిపోతుంది'],['ఎక్కువ clicks అవసరం కావచ్చు','త్వరగా చేరుకోవచ్చు'],['స్పష్టమైన categorisation','సరళమైన navigation'],['ఉదా: e-commerce, ప్రభుత్వ websites','ఉదా: చిన్న mobile apps']],
  ex='E-commerce App:\n\nHierarchical:\n\nHome → Electronics → Mobiles → Android → Samsung.\n\nFlat:\n\nHome → Mobiles | Laptops | Tablets | Accessories.',
  iv='పెద్ద, సంక్లిష్ట content కు hierarchical navigation; త్వరగా చేరుకోవాల్సిన చిన్న products కు flat navigation బాగా సరిపోతుంది.'),
34: dict(q='Global Navigation మరియు Local Navigation మధ్య తేడా ఏమిటి?',
  tbl=[['అన్ని pages లో కనిపిస్తుంది','ఒక section లో కనిపిస్తుంది'],['ప్రధాన sections కు యాక్సెస్','Subsections కు యాక్సెస్'],['స్థిరంగా (consistent) ఉంటుంది','సందర్భానికి తగ్గట్టు మారుతుంది'],['మొత్తం product నిర్మాణానికి మద్దతు','లోతైన navigation కు మద్దతు'],['సాధారణంగా header లో','Sidebar, tabs లేదా submenu లో']],
  ex="D'SARAS Website:\n\nGlobal Navigation:\n- Home\n- About\n- Design Services\n- Design Acharya\n- Animation Films\n- Contact\n\nLocal Navigation:\n\nDesign Acharya లోపల:\n- Courses\n- Curriculum\n- Mentors\n- Projects\n- Admissions",
  iv='Global navigation ప్రధాన sections కు స్థిరమైన యాక్సెస్ ఇస్తుంది; local navigation ఒక section లోపలి subsections మధ్య కదలడానికి సహాయపడుతుంది.'),
35: dict(q='Breadcrumb Navigation మరియు Tab Navigation మధ్య తేడా ఏమిటి?',
  tbl=[['ప్రస్తుత స్థానాన్ని చూపిస్తుంది','సంబంధిత sections మధ్య మారుస్తుంది'],['Hierarchy ని ప్రతిబింబిస్తుంది','సమాన స్థాయి content ను క్రమబద్ధం చేస్తుంది'],['వెనక్కి వెళ్లడంలో సహాయం','అడ్డంగా (horizontal) మారడంలో సహాయం'],['లోతైన websites లో ఉపయోగకరం','Dashboards, product pages లో ఉపయోగకరం'],['ద్వితీయ (secondary) navigation','తరచుగా ప్రాథమిక section navigation']],
  ex='E-commerce Website:\n\nBreadcrumb:\n\nHome → Electronics → Mobiles → Samsung Galaxy.\n\nTabs:\n\nProduct Details | Specifications | Reviews | FAQs.',
  iv='Breadcrumb hierarchy లో ప్రస్తుత స్థానాన్ని చూపించి వెనక్కి వెళ్లడానికి; tabs ఒకే స్థాయి సంబంధిత content మధ్య త్వరగా మారడానికి.'),
36: dict(q='User Flow మరియు Wireflow మధ్య తేడా ఏమిటి?',
  tbl=[['Flow logic పై దృష్టి','Flow మరియు screen layout రెండింటిపై దృష్టి'],['Boxes, arrows ఉపయోగిస్తుంది','Wireframes, arrows ఉపయోగిస్తుంది'],['తక్కువ visual detail','ఎక్కువ visual context'],['ప్రారంభ planning కు మంచిది','Design communication కు మంచిది'],['Steps, నిర్ణయాలు చూపిస్తుంది','Screens మరియు interactions చూపిస్తుంది']],
  ex='Mobile Login:\n\nUser Flow:\n\nOpen App → Enter Mobile Number → Verify OTP → Login Successful.\n\nWireflow:\n\nఅదే క్రమాన్ని చూపిస్తుంది, అదనంగా:\n- Mobile number input screen.\n- OTP entry screen.\n- Resend OTP button.\n- Error message layout.\n- విజయవంతమైన login screen.',
  iv='User Flow interaction క్రమం, నిర్ణయాలపై దృష్టి పెడుతుంది; Wireflow ఆ flow ను wireframes తో కలిపి ప్రతి దశలో screen ఎలా ఉంటుందో చూపిస్తుంది.'),
37: dict(q='Happy Path మరియు Edge Case మధ్య తేడా ఏమిటి?',
  tbl=[['ఆదర్శ పరిస్థితి (ideal scenario)','అసాధారణ పరిస్థితి'],['ఆశించిన user ప్రవర్తన','అనుకోని పరిస్థితులు'],['అత్యంత సాధారణ మార్గం','తక్కువగా జరిగే మార్గం'],['విజయవంతంగా పూర్తయ్యే task','Errors లేదా అంతరాయాలు'],['ప్రాథమిక design దృష్టి','దృఢమైన (robust) design కు అవసరం']],
  ex='Banking App:\n\nHappy Path:\n\nLogin → Select Beneficiary → Enter Amount → Confirm → డబ్బు విజయవంతంగా transfer అయింది.\n\nEdge Cases:\n- Account లో సరిపడా balance లేదు.\n- తప్పు OTP.\n- Internet connection పోయింది.\n- Beneficiary account inactive గా ఉంది.\n- రోజువారీ transaction పరిమితి దాటింది.\n- Bank server అందుబాటులో లేదు.',
  iv='Happy path మీద మాత్రమే కాకుండా edge cases ను కూడా design చేయడం వల్ల నమ్మదగిన, దృఢమైన product తయారవుతుంది.'),
38: dict(q='User Scenario మరియు Use Case మధ్య తేడా ఏమిటి?',
  tbl=[['కథనం (narrative) రూపం','నిర్మాణాత్మక (structured) రూపం'],['User context పై దృష్టి','System interaction పై దృష్టి'],['ప్రేరణ మరియు పరిస్థితిని వివరిస్తుంది','Steps మరియు system స్పందనలను వివరిస్తుంది'],['Empathy నిర్మించడంలో సహాయం','Functionality ని నిర్వచించడంలో సహాయం'],['UX research లో ఉపయోగిస్తాం','Requirements మరియు design లో ఉపయోగిస్తాం']],
  ex='Food Delivery App:\n\nUser Scenario:\n\n"రవి పని నుంచి ఇంటికి తిరిగి వస్తున్నాడు. అలసిపోయాడు, food delivery app ద్వారా త్వరగా dinner order చేయాలనుకుంటున్నాడు."\n\nUse Case: Order Food\n- Actor: Customer.\n- Precondition: User login అయి ఉన్నారు.\n- Step 1: Restaurant కోసం వెతకడం.\n- Step 2: Food items ఎంచుకోవడం.\n- Step 3: Items ను cart కు జోడించడం.\n- Step 4: Delivery address నమోదు చేయడం.\n- Step 5: Payment చేయడం.\n- Step 6: Order confirmation పొందడం.\n\nAlternative: Payment విఫలమైతే user వేరే payment method ఎంచుకుంటారు.',
  iv='User scenario సందర్భం, ప్రేరణను వివరిస్తుంది; use case user మరియు system మధ్య interaction ను దశలవారీగా వివరిస్తుంది.'),
39: dict(q='Use Case మరియు User Story మధ్య తేడా ఏమిటి?',
  tbl=[['వివరమైన interaction వివరణ','చిన్న requirement statement'],['System ప్రవర్తనపై దృష్టి','User విలువపై దృష్టి'],['Main flow, alternative flows ఉంటాయి','Agile backlog లో ఉపయోగిస్తాం'],['సాధారణంగా పొడవుగా ఉంటుంది','సాధారణంగా చిన్నదిగా ఉంటుంది'],['మరింత నిర్మాణాత్మకం, వివరంగా','తేలికైనది, సౌలభ్యం ఉంటుంది']],
  ex='Banking App:\n\nUser Story:\n\n"ఒక banking customer గా, నేను saved beneficiaries కు డబ్బు transfer చేయాలనుకుంటున్నాను, తద్వారా transactions ను త్వరగా పూర్తి చేయగలను."\n\nUse Case: Money Transfer\n- Actor: Banking Customer.\n- Preconditions: Customer login అయి ఉన్నారు.\n- Main Flow: Beneficiary ఎంచుకోవడం, amount నమోదు, వివరాలు verify, authenticate చేసి transfer చేయడం.\n- Alternative Flow: తప్పు OTP లేదా సరిపడా balance లేకపోవడం.\n- Postcondition: Transaction status update అవుతుంది.',
  iv='User Stories Agile backlogs లో ఎక్కువగా ఉపయోగిస్తారు; Use Cases మరింత వివరమైన functional అవగాహన ఇస్తాయి.'),
40: dict(q='User Flow మరియు Screen Flow మధ్య తేడా ఏమిటి?',
  tbl=[['User actions, నిర్ణయాలపై దృష్టి','Screens క్రమంపై దృష్టి'],['Decision logic ఉంటుంది','Screen transitions చూపిస్తుంది'],['అనేక మార్గాలు ఉండవచ్చు','Screens సంబంధాలను map చేస్తుంది'],['User ప్రవర్తన ఆధారితం','Interface-navigation ఆధారితం'],['Users లక్ష్యాలను ఎలా సాధిస్తారో వివరిస్తుంది','Screens ఎలా కలుస్తాయో వివరిస్తుంది']],
  ex='Mobile Banking App:\n\nUser Flow:\n\nOpen App → Login → Choose Transfer Type → Check Beneficiary → Transfer → Confirmation.\n\n' + fig('g3-screen-flow', 'Screen flow: Splash, Login, Dashboard, Beneficiary, Transfer, Success screens', 'Screen Flow – app లోని screens క్రమం.', 'Illustrative screen sequence.'),
  iv='User Flow interaction logic ను నిర్ణయిస్తుంది; Screen Flow screen-స్థాయి navigation ను క్రమబద్ధం చేస్తుంది.'),
}

# English examples that are diagrams in the PDF – redrawn as images
EX_EN = {
26: 'Task Flow: Money Transfer\n\n' + fig('g3-task-flow', 'Task flow for money transfer', '', 'Simple linear task flow.') +
    '\n\nUser Flow: Money Transfer\n\n' + fig('g3-user-flow', 'User flow for money transfer with alternative paths', '', 'Illustrative user flow with alternative paths.'),
29: 'Sitemap:\n\n' + fig('g3-sitemap', 'E-commerce sitemap', '', 'Illustrative website sitemap.') +
    '\n\nInformation Architecture:\n- Group products into meaningful categories.\n- Use understandable labels.\n- Organise product filters.\n- Define navigation hierarchy.\n- Ensure users can find products easily.',
40: 'User Flow:\n\nOpen App → Login → Choose Transfer Type → Check Beneficiary → Transfer → Confirmation.\n\nScreen Flow:\n\n' + fig('g3-screen-flow', 'Screen flow for a mobile banking app', '', 'Illustrative screen sequence.'),
}
# Telugu text fixes (paragraph run together in the PDF)
TE_FIX = {37: [('సాధారణ మార్గం. Edge Case:', 'సాధారణ మార్గం.\n\nEdge Case:')]}

INTRO_TE = 'ఈ గ్రూప్ UX Designలో చాలా ముఖ్యమైనది. ఒక వినియోగదారుడు యాప్ లేదా వెబ్‌సైట్‌లోకి వచ్చినప్పటి నుంచి తన లక్ష్యాన్ని పూర్తి చేసే వరకు అతని ప్రయాణాన్ని ఎలా డిజైన్ చేయాలి? సమాచారాన్ని ఎలా క్రమబద్ధీకరించాలి? సరైన Navigation మరియు User Flow ఎలా రూపొందించాలి? అనే అంశాలను నేర్చుకుందాం.'
PRACTICE_TITLE = 'Practical UX Exercise – Test Your Understanding'
PRACTICE_BODY = '''Scenario: You are designing a mobile banking application. A user wants to transfer ₹5,000 to a new beneficiary.
సందర్భం: మీరు ఒక mobile banking app design చేస్తున్నారు. ఒక user కొత్త beneficiary కు ₹5,000 transfer చేయాలనుకుంటున్నారు.

1. Which deliverable explains the user's complete steps to transfer money? (Task Flow / Customer Journey / Empathy Map)
2. Which research method helps discover how users naturally group banking services? (Tree Testing / Card Sorting / A/B Testing)
3. Which deliverable shows the actual screen layouts connected by arrows? (Sitemap / User Journey / Wireflow)
4. What represents an incorrect OTP or insufficient balance? (Happy Path / Edge Case / User Persona)
5. Which deliverable describes the entire customer experience from awareness to loyalty? (Screen Flow / Customer Journey / Task Flow)

### Answer key · జవాబులు
1. Task Flow · 2. Card Sorting · 3. Wireflow · 4. Edge Case · 5. Customer Journey'''
