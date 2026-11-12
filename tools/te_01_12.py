T = {}
T[1] = dict(q="What is an Affinity Diagram?", tq="Affinity Diagram అంటే ఏమిటి?",
 ex="""మీరు 15 మంది Rummy players ను ఇంటర్వ్యూ చేశారని అనుకోండి.
వారు ఇలా చెప్పారు:
- రూల్స్ అర్థం కావడం లేదు.
- రిజిస్ట్రేషన్‌కు ఎక్కువ సమయం పడుతోంది.
- కార్డులు ఎలా అమర్చాలో తెలియడం లేదు.
- నా transaction history కనిపించడం లేదు.
- గేమ్ మధ్యలో disconnect అవుతోంది.
వీటిని ఇలా గ్రూప్ చేస్తాం:

Theme\tపరిశీలనలు
Onboarding\tగందరగోళమైన రిజిస్ట్రేషన్, అస్పష్టమైన రూల్స్
Gameplay\tకార్డుల అమరిక, అస్పష్టమైన actions
Performance\tDisconnections, loading
Wallet\tTransaction history, payment గందరగోళం""",
 how="""1. User interviews నిర్వహించండి.
2. ప్రతి పరిశీలనను ఒక్కో sticky note పై రాయండి.
3. ఒకేలాంటి పరిశీలనలను తొలగించండి.
4. సమానమైన వాటిని గ్రూప్ చేయండి.
5. Themes గుర్తించండి.
6. ప్రతి theme కు అర్థవంతమైన పేరు ఇవ్వండి.
7. వాటి నుంచి design opportunities గుర్తించండి.""",
 iv="Qualitative research ఫలితాలను విశ్లేషించి, యూజర్లు పదే పదే ఎదుర్కొంటున్న సమస్యలు మరియు ప్రవర్తనా patterns గుర్తించడానికి నేను affinity mapping ఉపయోగిస్తాను.")
T[2] = dict(q="What is an Asset Map?", tq="Asset Map అంటే ఏమిటి?",
 ex="""ఒక కొత్త యూజర్ ప్రయాణంలో ఇవి ఉండవచ్చు:
1. Google Play Store.
2. App installation.
3. Welcome screen.
4. Mobile number registration.
5. OTP verification.
6. అవసరమైతే KYC verification.
7. Lobby.
8. Table selection.
9. Gameplay.
10. Wallet మరియు transaction screens.
ఈ అన్ని touchpoints లో అనుభవం ఒకేలా ఉందో లేదో Asset Map ద్వారా గుర్తించవచ్చు.""",
 how="""- అన్ని touchpoints ను జాబితా చేయండి.
- ఇప్పుడున్న screens మరియు assets సేకరించండి.
- వాటిని క్రమంలో (chronologically) అమర్చండి.
- పునరావృతమైన లేదా భిన్నంగా ఉన్న అనుభవాలను గుర్తించండి.
- లేని screens మరియు ఖాళీలను హైలైట్ చేయండి.""",
 iv="పూర్తి screen ecosystem ను అర్థం చేసుకుని, అన్ని user touchpoints లో consistency ఉండేలా చూడటానికి నేను asset map ఉపయోగిస్తాను.")
T[3] = dict(q="What is a Concept Map?", tq="Concept Map అంటే ఏమిటి?",
 ex="""ప్రధాన అంశం: Online Rummy Platform.
దానికి అనుసంధానమైన అంశాలు:
- User Account → Registration, Login, Profile.
- Gameplay → Tables, Cards, Sequences, Sets.
- Wallet → Deposit, Withdrawal, Transactions.
- Support → Help Centre, FAQs, Complaints.
- Rewards → Bonuses, Loyalty, Offers.""",
 how="""1. ప్రధాన అంశాన్ని గుర్తించండి.
2. దానికి సంబంధించిన అంశాలను గుర్తించండి.
3. వాటిని క్రమానుగతంగా (hierarchically) అమర్చండి.
4. సంబంధం ఉన్న అంశాలను బాణాలతో కలపండి.
5. ప్రతి సంబంధానికి స్పష్టమైన label ఇవ్వండి.""",
 iv="Solution నిర్ణయించే ముందు product capabilities, user needs మరియు వెనుక ఉన్న systems మధ్య సంబంధాలను అర్థం చేసుకోవడానికి concept mapping నాకు సహాయపడుతుంది.")
T[4] = dict(q="What is a CSD Matrix?", tq="CSD Matrix (Certainties, Suppositions, Doubts) అంటే ఏమిటి?",
 ex="""వర్గం\tఅర్థం\tClassic Rummy ఉదాహరణ
Certainties\tనిర్ధారిత విషయాలు\tఅకౌంట్ వాడటానికి యూజర్లు రిజిస్టర్ కావాలి
Suppositions\tఊహలు\tకొత్త యూజర్లకు card grouping కష్టంగా ఉంటుంది
Doubts\tసందేహాలు\tOnboarding సమయంలో యూజర్లు ఎందుకు వెళ్లిపోతున్నారు?""",
 how="""1. Stakeholder workshop నిర్వహించండి.
2. ప్రతి ఒక్కరికీ తెలిసిన విషయాలు అడగండి.
3. ఊహలను (assumptions) వేరుగా జాబితా చేయండి.
4. సమాధానం లేని ప్రశ్నలను గుర్తించండి.
5. ఊహలను ఎలా validate చేయాలో నిర్ణయించండి.
6. ముఖ్యమైన సందేహాలను research questions గా మార్చండి.""",
 imp="ఒక ఊహ (supposition) నిర్ధారిత user insight కాదు. దాన్ని తప్పనిసరిగా validate చేయాలి.",
 iv="Project discovery సమయంలో వాస్తవాలను ఊహల నుంచి వేరు చేసి, validate చేయాల్సిన research questions గుర్తించడానికి నేను CSD matrix ఉపయోగిస్తాను.")
T[5] = dict(q="What is a Design System?", tq="Design System అంటే ఏమిటి?",
 ex="""Classic Rummy లో 50+ screens ఉన్నాయని ఊహించండి.
Design system లేకపోతే, ప్రతి designer కొద్దిగా భిన్నమైన buttons, cards, typography లేదా రంగులు తయారు చేయవచ్చు.
Design system ఉంటే:
- Primary buttons ఒకే ప్రమాణాన్ని పాటిస్తాయి.
- Card components ఒకే ప్రమాణాన్ని పాటిస్తాయి.
- Wallet components ఒకే ప్రమాణాన్ని పాటిస్తాయి.
- Typography ఒకేలా ఉంటుంది.
- Developers సాధారణ components ను మళ్లీ మళ్లీ ఉపయోగిస్తారు.""",
 how="""1. ఇప్పుడున్న UI ను audit చేయండి.
2. Design principles నిర్ణయించండి.
3. Color మరియు typography tokens నిర్వచించండి.
4. Spacing మరియు layout నియమాలు ఏర్పాటు చేయండి.
5. ప్రధాన components తయారు చేయండి.
6. Component states మరియు variants నిర్వచించండి.
7. మళ్లీ ఉపయోగించగల patterns నిర్మించండి.
8. ఉపయోగించే విధానాన్ని document చేయండి.
9. System ను నిర్వహిస్తూ అప్‌డేట్ చేయండి.""",
 iv="Consistency కాపాడటానికి మరియు design-development సామర్థ్యాన్ని పెంచడానికి, design tokens, reusable components, variants మరియు interaction guidelines తో విస్తరించగల design systems ను నేను ఏర్పాటు చేస్తాను.")
T[6] = dict(q="What is an Ecosystem Map?", tq="Ecosystem Map అంటే ఏమిటి?",
 ex="""ఒక Classic Rummy player ecosystem లో ఇవి ఉండవచ్చు:
- వ్యక్తులు: గేమ్‌ను సిఫార్సు చేసిన స్నేహితులు, టేబుల్ వద్ద ఇతర players, customer support agents.
- ప్రొడక్ట్స్: Classic Rummy app, Google Play Store లేదా App Store, ఫోన్.
- సేవలు: Payment gateways, UPI apps, బ్యాంకులు, SMS/OTP providers, KYC verification సేవ.
- మార్గాలు: Push notifications, SMS, email, social media, in-app chat.
OTP SMS ఆలస్యంగా వచ్చినా, UPI payment విఫలమైనా player గేమ్‌నే నిందిస్తారు – సమస్య ecosystem లో వేరే చోట ఉన్నప్పటికీ.""",
 how="""1. మ్యాప్ చేయాల్సిన అనుభవాన్ని నిర్ణయించండి (ఉదా. డబ్బు జమ చేసి టేబుల్‌లో చేరడం).
2. యూజర్‌ను మధ్యలో ఉంచండి.
3. పాల్గొనే వ్యక్తులు, సంస్థలు, ప్రొడక్ట్స్, సేవలను జాబితా చేయండి.
4. యూజర్ వాటితో ఎంత దగ్గరగా సంప్రదిస్తారో దాని ఆధారంగా అమర్చండి.
5. సంబంధిత అంశాలను కలిపి, వాటి మధ్య ఏమి ప్రవహిస్తుందో (సమాచారం, డబ్బు, సహాయం) గుర్తించండి.
6. మన నియంత్రణలో లేని dependencies, ఖాళీలు, risks హైలైట్ చేయండి.""",
 iv="మన ప్రొడక్ట్ బయట ఉన్న partners మరియు సేవలతో సహా యూజర్ అనుభవాన్ని ప్రభావితం చేసే ప్రతిదాన్ని అర్థం చేసుకుని, నిజ జీవిత dependencies కు తగ్గట్టు design చేయడానికి నేను ecosystem maps ఉపయోగిస్తాను.")
T[7] = dict(q="What is an Empathy Map?", tq="Empathy Map అంటే ఏమిటి?",
 ex="""యూజర్: మొదటిసారి Rummy ఆడే player.

భాగం\tపరిశీలనలు
Says (చెబుతారు)\t"నేను సరిగ్గా ఆడుతున్నానో లేదో తెలియడం లేదు."
Thinks (ఆలోచిస్తారు)\t"రూల్స్ అర్థం కాక డబ్బు పోగొట్టుకుంటానా?"
Does (చేస్తారు)\tఇతరులు ఆడటం గమనిస్తారు, cash tables కు దూరంగా ఉంటారు, help section తెరుస్తారు
Feels (భావిస్తారు)\tఆసక్తి ఉంది కానీ భయం; తప్పులు చేస్తానేమో అని ఆందోళన""",
 how="""1. ఒక రకమైన యూజర్‌ను ఎంచుకోండి (ఊహల ఆధారంగా కాదు, research ఆధారంగా).
2. Says, Thinks, Does, Feels అనే నాలుగు భాగాలు గీయండి.
3. ప్రతి భాగాన్ని interviews మరియు పరిశీలనల నుంచి వచ్చిన ఆధారాలతో నింపండి.
4. వైరుధ్యాలు చూడండి – ఉదా. యూజర్లు చెప్పేది మరియు చేసేది వేరుగా ఉండటం.
5. యూజర్ ముఖ్య అవసరాలు మరియు ఇబ్బందులను సంక్షిప్తంగా రాయండి.
6. ఆ insights ను personas మరియు design నిర్ణయాలకు ఉపయోగించండి.""",
 iv="యూజర్లు ఏమి చెబుతారు, ఆలోచిస్తారు, చేస్తారు, భావిస్తారు అనే విషయాలపై టీమ్ మొత్తం ఒకే అవగాహనకు రావడానికి నేను empathy maps ఉపయోగిస్తాను; దీంతో design నిర్ణయాలు నిజమైన user అవగాహనపై ఆధారపడతాయి.")
T[8] = dict(q="What is an Experience Map?", tq="Experience Map అంటే ఏమిటి?",
 ex="""అనుభవం: వినోదంగా card games నేర్చుకుని ఆనందించడం (Classic Rummy కి మాత్రమే పరిమితం కాదు).
దశలు:
1. కుటుంబం లేదా స్నేహితుల నుంచి card games గురించి వినడం.
2. రూల్స్ నేర్చుకోవడం (offline లేదా online).
3. సాధన చేసి నమ్మకం పెంచుకోవడం.
4. సరదాకు లేదా పోటీకి క్రమం తప్పకుండా ఆడటం.
5. అనుభవాన్ని స్నేహితులతో పంచుకోవడం.
దీని ద్వారా ప్రజలు నమ్మకమైన వారితో కలిసి నేర్చుకోవడానికి ఇష్టపడతారని తెలియవచ్చు – practice tables లేదా స్నేహితులతో ఆడటం వంటి features కు ఇది అవకాశం.""",
 how="""1. విస్తృత లక్ష్యం లేదా కార్యకలాపాన్ని నిర్ణయించండి.
2. ప్రజలు దాన్ని వివిధ ప్రొడక్ట్స్‌లో మరియు offline లో ఎలా సాధిస్తారో research చేయండి.
3. ముఖ్యమైన దశలను గుర్తించండి.
4. ప్రతి దశలో చర్యలు, ఆలోచనలు, భావాలను నమోదు చేయండి.
5. ఇబ్బందులు మరియు ముఖ్యమైన క్షణాలను హైలైట్ చేయండి.
6. కొత్త ప్రొడక్ట్స్ లేదా features కు అవకాశాలను గుర్తించండి.""",
 iv="ఒక లక్ష్యం వెనుక ఉన్న విస్తృత మానవ అనుభవాన్ని అర్థం చేసుకోవడానికి నేను experience maps ఉపయోగిస్తాను; దీని ద్వారా ప్రస్తుత ప్రొడక్ట్‌కు మించిన అవకాశాలు కనిపిస్తాయి.")
T[9] = dict(q="What is a Feasibility, Desirability and Viability Scorecard?", tq="Feasibility, Desirability మరియు Viability Scorecard అంటే ఏమిటి?",
 ex="""ఉదాహరణ scores (1–10):

Idea\tDesirability\tFeasibility\tViability\tమొత్తం
Interactive tutorial\t9\t7\t8\t24
Practice table\t8\t9\t7\t24
టేబుల్ వద్ద voice chat\t5\t3\t4\t12
Custom card themes\t6\t8\t5\t19
Tutorial మరియు practice table కు ఎక్కువ score వచ్చింది, కాబట్టి తదుపరి release కు అవి బలమైన ఎంపికలు.""",
 how="""1. Ideas లేదా features ను జాబితా చేయండి.
2. Scoring scale పై అంగీకరించండి (ఉదా. 1–10).
3. Research ఆధారాలతో desirability కు score ఇవ్వండి.
4. Engineering తో feasibility కు score ఇవ్వండి.
5. Business stakeholders తో viability కు score ఇవ్వండి.
6. Scores కలిపి ideas కు ర్యాంక్ ఇవ్వండి.
7. ఫలితాలపై చర్చించండి – score నిర్ణయానికి సహాయపడుతుంది, తీర్పును భర్తీ చేయదు.""",
 iv="Stakeholders తో ideas కు ప్రాధాన్యత ఇచ్చేటప్పుడు user needs, technical effort మరియు business value మధ్య సమతుల్యం కోసం నేను feasibility–desirability–viability scoring ఉపయోగిస్తాను.")
T[10] = dict(q="What is an HTA (Hierarchical Task Analysis) Diagram?", tq="HTA (Hierarchical Task Analysis) Diagram అంటే ఏమిటి?",
 ex="""లక్ష్యం: 0. Cash game లో చేరడం.
1. Log in
 1.1 Mobile number నమోదు
 1.2 OTP నమోదు
2. Wallet కు డబ్బు జమ చేయడం
 2.1 మొత్తాన్ని ఎంచుకోవడం
 2.2 Payment method ఎంచుకోవడం
 2.3 Payment నిర్ధారించడం
3. గేమ్ ఎంచుకోవడం
 3.1 Game type ఎంచుకోవడం
 3.2 Table మరియు entry fee ఎంచుకోవడం
4. Table లో చేరడం
దీన్ని విశ్లేషిస్తే, కొత్త player ఆడటానికి ముందు చాలా steps చేయాల్సి వస్తోందని తెలుస్తుంది – సులభతరం చేయడానికి అవకాశం.""",
 how="""1. ప్రధాన user లక్ష్యాన్ని నిర్ణయించండి.
2. దాన్ని ముఖ్యమైన subtasks గా విభజించండి.
3. ప్రతి subtask ను చిన్న steps గా విభజించండి.
4. Steps కు సంఖ్యలు ఇవ్వండి (1, 1.1, 1.2 …).
5. Plan జోడించండి – steps క్రమం లేదా షరతులు.
6. సంక్లిష్టత, పునరావృతం మరియు విఫలమయ్యే చోట్ల కోసం పరిశీలించండి.""",
 iv="సంక్లిష్టమైన లక్ష్యాలను subtasks గా విభజించడానికి నేను hierarchical task analysis ఉపయోగిస్తాను; దీంతో అనవసరమైన steps గుర్తించి ముఖ్యమైన workflows ను సులభతరం చేయగలను.")
T[11] = dict(q="What is an Impact–Effort Matrix?", tq="Impact–Effort Matrix అంటే ఏమిటి?",
 ex="""భాగం\tClassic Rummy idea (ఉదాహరణ)
Quick Wins\tస్పష్టమైన OTP error messages
Big Bets\tPractice game తో interactive tutorial
Fill-ins\tకొత్త avatar options
Money Pit\tపూర్తిగా custom 3D table environments""",
 how="""1. Ideas ను జాబితా చేయండి.
2. Research మరియు data తో impact అంచనా వేయండి.
3. Engineering తో effort అంచనా వేయండి.
4. ప్రతి idea ను matrix పై ఉంచండి.
5. Quick Wins తో మొదలుపెట్టి, Big Bets ను ప్లాన్ చేయండి.
6. కొత్త సమాచారం వచ్చినప్పుడు matrix ను మళ్లీ పరిశీలించండి.""",
 iv="Quick wins మరియు దీర్ఘకాలిక bets పై టీమ్‌ను త్వరగా ఏకాభిప్రాయానికి తీసుకురావడానికి నేను impact–effort matrix ఉపయోగిస్తాను; దీంతో పెద్ద అవకాశాలను మర్చిపోకుండా ముందుగానే విలువ అందిస్తాం.")
T[12] = dict(q="What is a Journey Map?", tq="Journey Map అంటే ఏమిటి?",
 ex="""యూజర్: కొత్త player. లక్ష్యం: మొదటి గేమ్ ఆడటం.

దశ\tచర్య\tభావం\tఇబ్బంది
Discover\tAd చూసి app install చేస్తారు\tఆసక్తి\tApp నమ్మదగినదో లేదో సందేహం
Register\tMobile number, OTP నమోదు\tఅసహనం\tOTP ఆలస్యం
Learn\tరూల్స్ చదువుతారు\tగందరగోళం\tచాలా ఎక్కువ text
Play\tPractice table లో చేరతారు\tభయం\tఅస్పష్టమైన card actions
Return\tNotification అందుకుంటారు\tఆసక్తి\tసాధారణ (generic) సందేశం""",
 how="""1. ఒక persona మరియు scenario ఎంచుకోండి.
2. లక్ష్యం మరియు journey దశలను నిర్ణయించండి.
3. Research ఆధారంగా చర్యలు, ఆలోచనలు, భావాలను map చేయండి.
4. ఇబ్బందులను గుర్తించండి.
5. అవకాశాలను గుర్తించండి.
6. ప్రతి అవకాశానికి సంస్థలో బాధ్యులను కేటాయించండి.""",
 iv="ఒక నిర్దిష్ట యూజర్ పూర్తి అనుభవాన్ని చూపించి, ఇబ్బందులు గుర్తించి, ముఖ్యమైన అవకాశాలపై టీమ్‌లను ఏకం చేయడానికి నేను journey maps ఉపయోగిస్తాను.")
