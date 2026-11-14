# Group 10 – UX Metrics & Analytics (Q131–Q142), assembled from Generate_UX_Vs_Questions_10.pdf.
# Telugu explanations/examples, English definitions, tables, examples and interview answers = PDF text.
# tbl_te, iv_te, and translations of single-language examples/notes = written by Claude.
# Diagrams (assets/images/vs/g10-*.svg) are redrawn by Claude from the PDF's illustrations (tools/vs/figs_g10.py).

def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

ITEMS = [
dict(n=131, A='Qualitative Data', B='Quantitative Data', q_te='Qualitative Data మరియు Quantitative Data మధ్య తేడా ఏమిటి?',
 te='''Qualitative Data (గుణాత్మక సమాచారం):

యూజర్లు ఏం ఆలోచిస్తున్నారు, ఎందుకు ఒక సమస్య ఎదుర్కొంటున్నారు, వారి భావాలు మరియు అనుభవాలు ఏమిటి అనే విషయాలను అర్థం చేసుకోవడానికి ఉపయోగించే descriptive information.

ఉదాహరణలు:
- User interviews
- Open-ended survey responses
- Usability testing observations
- Customer feedback

Quantitative Data (పరిమాణాత్మక సమాచారం):

సంఖ్యల రూపంలో కొలవగలిగే information.

ఉదాహరణలు:
- Conversion rate
- Task completion rate
- Number of active users
- Time on task
- Revenue''',
 defs=["Qualitative Data: Qualitative Data describes users' opinions, motivations, experiences, and behaviors, helping teams understand why something happens. Examples: user interviews, open-ended survey responses, usability testing observations, customer feedback.",
       'Quantitative Data: Quantitative Data consists of measurable numerical information used to identify patterns, compare performance, and measure outcomes. Examples: conversion rate, task completion rate, number of active users, time on task, revenue.'],
 hdr=['Qualitative Data', 'Quantitative Data'],
 rows=[['Descriptive', 'Numerical'], ['Explains Why and How', 'Explains How Much and How Often'], ['Interviews', 'Analytics'], ['User observations', 'Conversion rates'], ['Open-ended feedback', 'Structured survey results']],
 tbl_te=[['వివరణాత్మకం','సంఖ్యాత్మకం'],['ఎందుకు, ఎలా అని వివరిస్తుంది','ఎంత, ఎంత తరచుగా అని వివరిస్తుంది'],['Interviews','Analytics'],['User పరిశీలనలు','Conversion rates'],['Open-ended feedback','నిర్మాణాత్మక survey ఫలితాలు']],
 ex_title='Classic Rummy',
 ex_te='''Qualitative:
- Users‌కు game table navigation confusing‌గా ఉందని feedback వచ్చింది.
- New users‌కు rules అర్థం కావడం లేదని usability testing‌లో గుర్తించారు.

Quantitative:
- 35% users tutorial మధ్యలో exit అవుతున్నారు.
- Tutorial completion rate 65% ఉంది.
- మొదటి game ప్రారంభించడానికి సగటు సమయం 3 నిమిషాలు.''',
 ex_en='''Qualitative:
- Feedback said that game-table navigation is confusing.
- Usability testing found that new users don't understand the rules.

Quantitative:
- 35% of users exit midway through the tutorial.
- Tutorial completion rate is 65%.
- Average time to start the first game: 3 minutes.''',
 iv_en='"Qualitative data helps me understand why users behave in a particular way through interviews, observations, and feedback. Quantitative data helps me measure how frequently or effectively they behave through metrics such as conversion rates, task completion, and engagement. I use both together to make evidence-based design decisions."',
 iv_te='Qualitative "ఎందుకు" అని, Quantitative "ఎంత, ఎంత తరచుగా" అని చెబుతుంది – evidence ఆధారిత design నిర్ణయాలకు రెండింటినీ కలిపి ఉపయోగిస్తాను.'),

dict(n=132, A='KPI', B='UX Metrics', q_te='KPI మరియు UX Metrics మధ్య తేడా ఏమిటి?',
 te='''KPI – Key Performance Indicator:

ఒక business లేదా product యొక్క ముఖ్యమైన objectives సాధిస్తున్నామా లేదా అనేది measure చేసే key metric.

ఉదాహరణలు:
- Revenue growth
- Customer acquisition
- Subscription conversion
- Customer retention

UX Metrics:

ఒక product‌ను యూజర్లు ఎంత సులభంగా, సమర్థవంతంగా, సంతృప్తికరంగా ఉపయోగిస్తున్నారో measure చేసే metrics.

Important: కొన్ని UX metrics కూడా business KPIs‌గా ఉపయోగించవచ్చు. ఇవి పూర్తిగా వేర్వేరు categories కావు.''',
 defs=['KPI: A KPI is a measurable indicator used to evaluate progress toward important business or organizational objectives. Examples: revenue growth, customer acquisition, subscription conversion, customer retention.',
       'UX Metrics: UX Metrics measure the quality of user experiences, including usability, satisfaction, efficiency, and engagement.',
       'Important: Some UX metrics can also be used as business KPIs – they are not completely separate categories.'],  # last: Claude translation
 hdr=['KPI', 'UX Metrics'],
 rows=[['Business performance indicator', 'User experience measurement'], ['Revenue and growth', 'Task success and usability'], ['Business objectives', 'User-centered objectives'], ['Conversion and retention', 'SUS, CSAT, task completion'], ['Strategic measurement', 'Experience evaluation']],
 tbl_te=[['Business పనితీరు సూచిక','User experience కొలత'],['ఆదాయం, వృద్ధి','Task విజయం, usability'],['Business లక్ష్యాలు','User కేంద్రిత లక్ష్యాలు'],['Conversion, retention','SUS, CSAT, task completion'],['వ్యూహాత్మక కొలత','Experience మూల్యాంకనం']],
 ex_title='E-commerce',
 ex_te='''Business KPI:
- Purchase conversion rate ను 10% పెంచడం.

UX Metrics:
- Checkout task completion rate.
- Checkout పూర్తి చేయడానికి సగటు సమయం.
- Checkout error rate.
- Customer satisfaction.''',
 ex_en='''Business KPI:
- Increase purchase conversion rate by 10%.

UX Metrics:
- Checkout task completion rate.
- Average time to complete checkout.
- Checkout error rate.
- Customer satisfaction.''',
 iv_en='"KPIs measure progress toward key business objectives, while UX metrics evaluate how effectively users interact with a product. I connect UX metrics with business KPIs to understand how improvements in user experience contribute to product success."',
 iv_te='KPIs business లక్ష్యాల పురోగతిని, UX metrics user experience నాణ్యతను కొలుస్తాయి – రెండింటినీ కలిపి UX మెరుగుదల product విజయానికి ఎలా తోడ్పడిందో చూపిస్తాను.'),

dict(n=133, A='DAU', B='MAU', q_te='DAU మరియు MAU మధ్య తేడా ఏమిటి?',
 te='''DAU – Daily Active Users:

ఒక రోజులో product‌ను meaningful‌గా ఉపయోగించిన unique users సంఖ్య.

MAU – Monthly Active Users:

ఒక నెలలో product‌ను meaningful‌గా ఉపయోగించిన unique users సంఖ్య.''',
 defs=['DAU: DAU measures the number of unique active users within a single day.',
       'MAU: MAU measures the number of unique active users within a month.'],
 hdr=['DAU', 'MAU'],
 rows=[['Daily active users', 'Monthly active users'], ['Daily engagement', 'Monthly engagement'], ['Short-term usage', 'Longer-term usage'], ['Daily product activity', 'Monthly product activity']],
 tbl_te=[['రోజువారీ active users','నెలవారీ active users'],['రోజువారీ engagement','నెలవారీ engagement'],['స్వల్పకాల వాడకం','దీర్ఘకాల వాడకం'],['రోజువారీ product activity','నెలవారీ product activity']],
 ex_title='Learning App',
 ex_te=fig('g10-dau-mau', 'Bar chart of daily active users peaking at 5,500 on Tuesday next to a monthly active users total of 40,000', 'ఉదాహరణ (illustrative): DAU – ప్రతి రోజు unique users; MAU – నెలలో కనీసం ఒకసారి active అయిన unique users.', 'Illustrative: DAU counts unique users per day; MAU counts unique users active at least once in the month.') + '''

ఒక learning app‌లో:
- Monday active users = 5,000
- Tuesday active users = 5,500
- Monthly unique active users = 40,000

ఇక్కడ DAU అనేది ఒక్కో రోజు unique active users‌ను కొలుస్తుంది. MAU అనేది మొత్తం నెలలో కనీసం ఒకసారి active అయిన unique users‌ను కొలుస్తుంది.''',
 ex_en=fig('g10-dau-mau', 'DAU bars vs MAU total', '', 'Illustrative: DAU counts unique users per day; MAU counts unique users active at least once in the month.') + '''

In a learning app:
- Monday active users = 5,000
- Tuesday active users = 5,500
- Monthly unique active users = 40,000

DAU counts the unique active users on each day. MAU counts the unique users who were active at least once during the whole month.''',
 iv_en='"DAU measures the number of unique active users in a day, whereas MAU measures unique active users over a month. Together, they help evaluate product engagement and usage patterns. The definition of an active user should be based on meaningful product activity."',
 iv_te='DAU రోజుకు, MAU నెలకు unique active users – "active user" నిర్వచనం అర్థవంతమైన product activity ఆధారంగా ఉండాలి.'),

dict(n=134, A='Conversion Rate', B='Retention Rate', q_te='Conversion Rate మరియు Retention Rate మధ్య తేడా ఏమిటి?',
 te='''Conversion Rate:

ఒక specific desired action పూర్తి చేసిన users percentage.

Formula:
Conversion Rate = (Conversions ÷ Eligible Users) × 100

Retention Rate:

ఒక నిర్దిష్ట కాలం తర్వాత కూడా product‌ను ఉపయోగిస్తున్న users percentage.

Cohort-based formula:
Retention Rate = (Users from Original Cohort Active at Time t ÷ Original Cohort Users) × 100''',
 defs=['Conversion Rate: Conversion Rate measures the percentage of users who complete a desired action out of the relevant audience. Formula: (Conversions ÷ Eligible Users) × 100.',
       'Retention Rate: Retention Rate measures the percentage of users who continue using a product over a defined period. Cohort-based formula: (Users from Original Cohort Active at Time t ÷ Original Cohort Users) × 100.'],
 hdr=['Conversion Rate', 'Retention Rate'],
 rows=[['Desired action completion', 'Continued product usage'], ['Purchase, signup, subscription', 'Returning users'], ['Measures acquisition funnel outcomes', 'Measures ongoing engagement'], ['Short-term or event-based', 'Time-based']],
 tbl_te=[['కోరిన చర్య పూర్తి చేయడం','Product ను కొనసాగించి ఉపయోగించడం'],['Purchase, signup, subscription','తిరిగి వచ్చే users'],['Acquisition funnel ఫలితాలను కొలుస్తుంది','కొనసాగే engagement ను కొలుస్తుంది'],['స్వల్పకాల లేదా event ఆధారితం','కాల ఆధారితం']],
 ex_title='E-commerce',
 ex_te='''Conversion:
- 1,000 users product page ను సందర్శించారు.
- 100 users కొనుగోలు చేశారు.
- Conversion Rate = 10%.

Retention:
- January లో 1,000 users sign up అయ్యారు.
- February లో 300 users తిరిగి వచ్చారు.
- February retention = 30%.''',
 ex_en='''Conversion:
- 1,000 users visit the product page.
- 100 users purchase.
- Conversion Rate = 10%.

Retention:
- 1,000 users sign up in January.
- 300 users return in February.
- February retention = 30%.''',
 iv_en='"Conversion Rate measures how many users complete a specific desired action, such as signing up or making a purchase. Retention Rate measures how many users continue using the product over time. Both are important for understanding product growth and long-term value."',
 iv_te='Conversion – ఎంతమంది కోరిన చర్య పూర్తి చేశారు; Retention – ఎంతమంది కాలక్రమంలో కొనసాగుతున్నారు. వృద్ధి, దీర్ఘకాల విలువకు రెండూ ముఖ్యం.'),

dict(n=135, A='Bounce Rate', B='Exit Rate', q_te='Bounce Rate మరియు Exit Rate మధ్య తేడా ఏమిటి?',
 te='''Bounce Rate:

ఒక website‌లో user ఒక page‌ను visit చేసి, meaningful engagement లేదా further navigation లేకుండా session‌ను వదిలిపెట్టిన సందర్భాలను measure చేస్తుంది.
GA4లో Bounce Rate అనేది Engagement Rate‌కు complement. Engaged Session‌గా పరిగణించబడని sessions percentage.

Exit Rate:

ఒక specific page‌ను చివరిగా చూసి users తమ session‌ను ముగించిన percentage.''',
 defs=['Bounce Rate: In GA4, Bounce Rate is the percentage of sessions that were not engaged sessions (the complement of Engagement Rate).',
       'Exit Rate: Exit Rate measures the percentage of page views for a particular page that were the final page views of sessions.'],
 hdr=['Bounce Rate', 'Exit Rate'],
 rows=[['Session-level concept', 'Page-level concept'], ['GA4: Not engaged sessions', 'Page is last in session'], ['Helps evaluate landing-page engagement', 'Helps identify where users leave'], ['Does not mean every user disliked the page', 'Exit can be expected or normal']],
 tbl_te=[['Session స్థాయి భావన','Page స్థాయి భావన'],['GA4: engage కాని sessions','Session లో చివరి page'],['Landing page engagement ను అంచనా వేయడానికి','Users ఎక్కడ వెళ్లిపోతున్నారో గుర్తించడానికి'],['ప్రతి user page ను ఇష్టపడలేదని అర్థం కాదు','Exit ఆశించినదే లేదా సాధారణమే కావచ్చు']],
 ex_title='E-commerce Website',
 ex_te='''Page A – Product Landing Page:
- Users నేరుగా ఈ page కు వస్తారు.
- మరింత engage కాకుండా వెళ్లిపోతారు.
- ఇది Bounce Rate కు కారణం కావచ్చు.

Page B – Order Confirmation:
- Users purchase పూర్తి చేస్తారు.
- Confirmation page చూస్తారు.
- Website నుండి exit అవుతారు.

ఇక్కడ Order Confirmation page‌కు Exit Rate ఎక్కువగా ఉండవచ్చు. కానీ అది తప్పనిసరిగా UX సమస్య కాదు.''',
 ex_en='''Page A – Product Landing Page:
- Users directly visit this page.
- They leave without engaging further.
- This may contribute to Bounce Rate.

Page B – Order Confirmation:
- Users complete purchase.
- They see confirmation page.
- They exit the website.

Here the Order Confirmation page may have a high Exit Rate, but that is not necessarily a UX problem.''',
 iv_en='"Bounce Rate in GA4 measures the percentage of sessions that were not engaged, whereas Exit Rate measures how often a particular page is the last page viewed in a session. I interpret both in context rather than assuming a high value always indicates a design problem."',
 iv_te='Bounce Rate – engage కాని sessions; Exit Rate – ఒక page session లో చివరిది అయిన శాతం. ఎక్కువ విలువ ఎప్పుడూ design సమస్య కాదు – context లో అర్థం చేసుకోవాలి.'),

dict(n=136, A='Task Success Rate', B='Task Completion Rate', q_te='Task Success Rate మరియు Task Completion Rate మధ్య తేడా ఏమిటి?',
 te='''ఈ రెండు terms చాలా సందర్భాల్లో similar meaning‌తో ఉపయోగిస్తారు. అయితే usability evaluationలో వీటి మధ్య useful distinction ఇలా ఉంటుంది.

Task Success Rate:

యూజర్లు ఒక task‌ను predefined success criteria ప్రకారం విజయవంతంగా పూర్తి చేసిన percentage.

Task Completion Rate:

ఒక task‌ను పూర్తిగా finish చేసిన users percentage. కొన్ని testing frameworks‌లో ఇది Task Success Rate‌కు సమానంగా నిర్వచించబడుతుంది.

Formula (binary completion ఉపయోగించినప్పుడు):
Task Completion Rate = (Completed Tasks ÷ Total Attempts) × 100''',
 defs=['Note: The two terms are often used with similar meaning; in usability evaluation a useful distinction is as follows.',  # Claude translation
       'Task Success Rate: Task Success Rate measures the percentage of users who successfully achieve a defined task goal.',
       'Task Completion Rate: Task Completion Rate measures the percentage of users who complete a specified task, with the exact success criteria defined by the study. Formula (binary completion): (Completed Tasks ÷ Total Attempts) × 100.'],
 hdr=['Task Success Rate', 'Task Completion Rate'],
 rows=[['Focuses on achieving success criteria', 'Focuses on task completion'], ['May consider correct outcome', 'Measures completed tasks'], ['Partial or incorrect outcomes may fail', 'Depends on defined completion rules'], ['Usability outcome', 'Task completion outcome']],
 tbl_te=[['Success criteria సాధించడంపై దృష్టి','Task పూర్తి చేయడంపై దృష్టి'],['సరైన ఫలితాన్ని పరిగణించవచ్చు','పూర్తైన tasks ను కొలుస్తుంది'],['పాక్షిక / తప్పు ఫలితాలు fail కావచ్చు','నిర్వచించిన completion నియమాలపై ఆధారం'],['Usability ఫలితం','Task completion ఫలితం']],
 ex_title='Banking App',
 ex_te='''Task: ₹5,000 ను మరో account కు transfer చేయడం.
- User A: విజయవంతంగా డబ్బు transfer చేశారు.
- User B: అన్ని steps పూర్తి చేశారు కానీ తప్పు account వివరాలు ఇచ్చారు.
- User C: మధ్యలోనే వదిలేశారు.

Success rate‌ను predefined correct-transfer criteria ఆధారంగా measure చేస్తాం.
Task completion rate‌ను task పూర్తయిందా లేదా అనే study definition ఆధారంగా measure చేస్తాం.''',
 ex_en='''Task: Transfer ₹5,000 to another account.
- User A: Successfully transfers money.
- User B: Completes all steps but enters incorrect account details.
- User C: Leaves halfway.

Success rate is measured against predefined correct-transfer criteria.
Task completion rate is measured by the study's definition of whether the task was finished.''',
 iv_en='"Task Success Rate focuses on whether users achieve the intended outcome correctly, while Task Completion Rate focuses on whether they finish the task. In practice, the terms can overlap, so I always define success and completion criteria clearly before testing."',
 iv_te='Success – సరైన ఫలితం సాధించారా; Completion – task పూర్తి చేశారా. ఇవి overlap అవుతాయి కాబట్టి testing కు ముందే criteria స్పష్టంగా నిర్వచిస్తాను.'),

dict(n=137, A='SUS', B='NPS', q_te='SUS మరియు NPS మధ్య తేడా ఏమిటి?',
 te='''SUS – System Usability Scale:

ఒక product లేదా system usability‌ను measure చేయడానికి ఉపయోగించే standardized 10-question questionnaire.
- 10 questions.
- Five-point response scale.
- Score 0 నుండి 100 వరకు.
- ఎక్కువ score సాధారణంగా మెరుగైన perceived usability ని సూచిస్తుంది.

NPS – Net Promoter Score:

ఒక product లేదా service‌ను ఇతరులకు recommend చేసే user willingness‌ను measure చేసే metric.

Question: "How likely are you to recommend this product to a friend or colleague?"
Response: 0–10 scale.
- Detractors: 0–6
- Passives: 7–8
- Promoters: 9–10

NPS = % Promoters − % Detractors

''' + fig('g10-nps', 'NPS scale from 0 to 10 with detractors 0 to 6, passives 7 to 8 and promoters 9 to 10', 'NPS scale – Detractors (0–6), Passives (7–8), Promoters (9–10).', 'NPS scale: Detractors 0–6, Passives 7–8, Promoters 9–10.'),
 defs=["SUS: SUS is a standardized questionnaire consisting of 10 statements that measures users' perceived usability of a system. 10 questions, five-point scale, score 0–100; higher generally means better perceived usability.",
       'NPS: NPS measures customer loyalty or advocacy by asking how likely users are to recommend a product or service to others. 0–10 scale: Detractors 0–6, Passives 7–8, Promoters 9–10. NPS = % Promoters − % Detractors.'],
 hdr=['SUS', 'NPS'],
 rows=[['Measures perceived usability', 'Measures recommendation likelihood'], ['10 questions', 'Usually one core question'], ['Score 0–100', 'Score -100 to +100'], ['Usability evaluation', 'Loyalty and advocacy'], ['Product interaction experience', 'Overall recommendation sentiment']],
 tbl_te=[['గ్రహించిన usability ని కొలుస్తుంది','Recommend చేసే అవకాశాన్ని కొలుస్తుంది'],['10 ప్రశ్నలు','సాధారణంగా ఒక ప్రధాన ప్రశ్న'],['Score 0–100','Score -100 నుండి +100'],['Usability మూల్యాంకనం','Loyalty, advocacy'],['Product interaction అనుభవం','మొత్తం recommendation భావన']],
 ex_title='Design Acharya Learning Platform',
 ex_te='''SUS:
- Course navigation easyగా ఉందా?
- Lessons access చేయడం simpleగా ఉందా?
- Students platform ఉపయోగించడంలో confident‌గా ఉన్నారా?

NPS:
- "Would you recommend Design Acharya to another student?"''',
 ex_en='''SUS:
- Is course navigation easy?
- Is accessing lessons simple?
- Are students confident using the platform?

NPS:
- "Would you recommend Design Acharya to another student?"''',
 iv_en='"SUS is a standardized 10-item questionnaire used to assess perceived system usability, while NPS measures how likely customers are to recommend a product. SUS focuses on usability, whereas NPS focuses on loyalty and advocacy."',
 iv_te='SUS – 10 ప్రశ్నలతో usability; NPS – recommend చేసే అవకాశం, అంటే loyalty.'),

dict(n=138, A='CSAT', B='CES', q_te='CSAT మరియు CES మధ్య తేడా ఏమిటి?',
 te='''CSAT – Customer Satisfaction Score:

ఒక product, service లేదా specific interaction పట్ల user satisfaction‌ను measure చేయడం.
Example question: "How satisfied are you with your experience?"

CES – Customer Effort Score:

ఒక task పూర్తి చేయడానికి user ఎంత effort పెట్టాల్సి వచ్చిందో measure చేయడం.
Example question: "How easy was it to resolve your issue today?"''',
 defs=['CSAT: CSAT measures how satisfied customers are with a product, service, or specific interaction. Example: "How satisfied are you with your experience?"',
       'CES: CES measures how easy or difficult it was for customers to complete a particular task. Example: "How easy was it to resolve your issue today?"'],
 hdr=['CSAT', 'CES'],
 rows=[['Satisfaction', 'Effort'], ['How happy is the user?', 'How easy was the task?'], ['Measures experience sentiment', 'Measures friction'], ['Satisfaction surveys', 'Effort-based surveys']],
 tbl_te=[['సంతృప్తి','శ్రమ (effort)'],['User ఎంత సంతోషంగా ఉన్నారు?','Task ఎంత సులభంగా ఉంది?'],['అనుభవ భావనను కొలుస్తుంది','Friction ను కొలుస్తుంది'],['సంతృప్తి surveys','Effort ఆధారిత surveys']],
 ex_title='Customer Support Platform',
 ex_te='''CSAT:
- Support agent response పట్ల customer సంతృప్తిగా ఉన్నారా?

CES:
- Customer తన issue‌ను resolve చేయడానికి ఎన్ని steps తీసుకోవాల్సి వచ్చింది?
- Support ticket submit చేయడం easyగా ఉందా?''',
 ex_en='''CSAT:
- Is the customer satisfied with the support agent's response?

CES:
- How many steps did the customer need to resolve their issue?
- Was submitting a support ticket easy?''',
 iv_en='"CSAT measures how satisfied users are with an experience, while CES measures how much effort users need to complete a task. I use CSAT to understand satisfaction and CES to identify unnecessary friction in user journeys."',
 iv_te='CSAT – సంతృప్తి; CES – task కు పట్టిన శ్రమ. CES తో journeys లో అనవసర friction గుర్తిస్తాను.'),

dict(n=139, A='A/B Testing', B='Multivariate Testing', q_te='A/B Testing మరియు Multivariate Testing మధ్య తేడా ఏమిటి?',
 te='''A/B Testing:

ఒక design లేదా experience యొక్క రెండు versions‌ను వేర్వేరు user groups‌కు చూపించి, ఏ version better results ఇస్తుందో statistically evaluate చేయడం.

ఉదాహరణ:
- Version A: Blue CTA button.
- Version B: Green CTA button.

''' + fig('g10-ab-test', 'Two page versions with a blue Buy Now button and a green Buy Now button, 50/50 traffic split', 'ఉదాహరణ CTA color experiment – ఇవి నిజమైన test ఫలితాలు కావు.', 'Illustrative CTA colour experiment, not real test results.') + '''

Multivariate Testing (MVT):

ఒకే experiment‌లో multiple design elements యొక్క combinations‌ను పరీక్షించడం.

Important: A/B testing మరియు multivariate testing రెండింటికీ సరైన experiment design, sufficient sample size, statistical analysis అవసరం.''',
 defs=['A/B Testing: A/B Testing compares two versions of an experience to determine which performs better against a defined metric. Example: Version A – blue CTA button; Version B – green CTA button.',
       'Multivariate Testing: Multivariate Testing evaluates multiple combinations of changes across different elements to understand their individual and combined effects.',
       'Important: Both A/B testing and multivariate testing need proper experiment design, a sufficient sample size and statistical analysis.'],  # last: Claude translation
 hdr=['A/B Testing', 'Multivariate Testing'],
 rows=[['Compares versions', 'Compares combinations'], ['Usually one main variation', 'Multiple element variations'], ['Simpler experiment', 'More complex experiment'], ['Lower traffic needs in many cases', 'Often requires more traffic'], ['Identifies better variant', 'Helps understand interactions between elements']],
 tbl_te=[['Versions ను పోల్చుతుంది','Combinations ను పోల్చుతుంది'],['సాధారణంగా ఒక ప్రధాన మార్పు','అనేక elements లో మార్పులు'],['సరళమైన experiment','సంక్లిష్టమైన experiment'],['చాలా సందర్భాల్లో తక్కువ traffic చాలు','తరచుగా ఎక్కువ traffic అవసరం'],['మెరుగైన variant ను గుర్తిస్తుంది','Elements మధ్య ప్రభావాన్ని అర్థం చేసుకోవడానికి']],
 ex_title='E-commerce Checkout',
 ex_te='''A/B Testing:
- A: "Continue to Payment"
- B: "Proceed to Pay"

Multivariate Testing:
- Headline: 2 versions.
- CTA color: 2 versions.
- CTA text: 2 versions.

మొత్తం సాధ్యమయ్యే combinations = 2 × 2 × 2 = 8.''',
 ex_en='''A/B Testing:
- A: "Continue to Payment"
- B: "Proceed to Pay"

Multivariate Testing:
- Headline: 2 versions.
- CTA color: 2 versions.
- CTA text: 2 versions.

Total possible combinations = 2 × 2 × 2 = 8.''',
 iv_en='"A/B Testing compares different versions of a design to identify which performs better, while Multivariate Testing evaluates multiple combinations of design elements to understand their individual and combined impact. I select the method based on the hypothesis, traffic volume, and experiment complexity."',
 iv_te='A/B – versions పోలిక; Multivariate – elements combinations పోలిక. Hypothesis, traffic, సంక్లిష్టత ఆధారంగా పద్ధతి ఎంచుకుంటాను.'),

dict(n=140, A='Heatmap', B='Session Recording', q_te='Heatmap మరియు Session Recording మధ్య తేడా ఏమిటి?',
 te='''Heatmap:

Users ఒక page‌లో ఎక్కడ click చేస్తున్నారు, ఏ ప్రాంతాలపై ఎక్కువ attention చూపిస్తున్నారు, ఎక్కడ scroll చేస్తున్నారు అనే aggregate behavior‌ను visual representation రూపంలో చూపిస్తుంది.

Types:
- Click Heatmap
- Scroll Heatmap
- Move Heatmap

Session Recording:

ఒక individual user session‌లో జరిగిన interactions‌ను playback రూపంలో చూడటానికి ఉపయోగించే tool.

Privacy note: Session recording tools ఉపయోగించేటప్పుడు sensitive information masking, consent, and applicable privacy requirements తప్పనిసరిగా పరిగణించాలి.''',
 defs=['Heatmap: A Heatmap visualizes aggregated user interactions such as clicks, taps, scrolling, or attention patterns on a page. Types: click, scroll, move heatmaps.',
       "Session Recording: Session Recording captures a replay of an individual user's interaction with a website or application, helping teams identify usability issues.",
       'Privacy note: When using session recording tools, masking sensitive information, consent and applicable privacy requirements must be considered.'],  # last: Claude translation
 hdr=['Heatmap', 'Session Recording'],
 rows=[['Aggregated interaction patterns', 'Individual session playback'], ['Shows where users interact', 'Shows how users interact'], ['Visual summary', 'Step-by-step behavior'], ['Identifies interaction hotspots', 'Reveals friction and confusion']],
 tbl_te=[['సమగ్ర interaction patterns','ఒక్కో session playback'],['Users ఎక్కడ interact చేస్తున్నారో','Users ఎలా interact చేస్తున్నారో'],['దృశ్య సారాంశం','Step-by-step ప్రవర్తన'],['Interaction hotspots గుర్తిస్తుంది','Friction, గందరగోళాన్ని బయటపెడుతుంది']],
 ex_title='SaaS Dashboard',
 ex_te=fig('g10-heatmap-recording', 'Heatmap with red click hotspots on a page next to a session recording showing one user path and a rage-click', 'Heatmap – అందరు users యొక్క patterns; Session Recording – ఒక్క user ప్రయాణం.', 'Heatmap: patterns across all users. Session recording: one user\'s journey.') + '''

Heatmap:
- Users ఎక్కువగా ఏ navigation items click చేస్తున్నారు?
- Primary CTA కనిపిస్తున్నదా?
- Users page‌లో ఎంతవరకు scroll చేస్తున్నారు?

Session Recording:
- Users filter apply చేయడంలో struggle అవుతున్నారా?
- Form errors తర్వాత ఏమి చేస్తున్నారు?
- ఒక particular workflowలో ఎక్కడ ఆగిపోతున్నారు?''',
 ex_en=fig('g10-heatmap-recording', 'Heatmap vs session recording', '', 'Heatmap: patterns across all users. Session recording: one user\'s journey.') + '''

Heatmap:
- Which navigation items do users click most?
- Is the primary CTA visible?
- How far down the page do users scroll?

Session Recording:
- Are users struggling to apply filters?
- What do they do after form errors?
- Where do they stop in a particular workflow?''',
 iv_en='"Heatmaps show aggregated patterns of user interactions, while Session Recordings help us observe individual user journeys in detail. I use heatmaps to identify patterns and recordings to investigate specific usability issues."',
 iv_te='Heatmap తో patterns గుర్తిస్తాను; Session Recording తో నిర్దిష్ట usability సమస్యలను లోతుగా పరిశీలిస్తాను.'),

dict(n=141, A='Funnel Analysis', B='Cohort Analysis', q_te='Funnel Analysis మరియు Cohort Analysis మధ్య తేడా ఏమిటి?',
 te='''Funnel Analysis:

ఒక user goal పూర్తి చేయడానికి ఎన్ని steps దాటాలి, ఏ step వద్ద ఎక్కువ మంది drop-off అవుతున్నారు అనే విషయాలను analyze చేయడం.

Cohort Analysis:

ఒక common characteristic లేదా starting event ఆధారంగా users‌ను groups‌గా విభజించి, కాలక్రమంలో వారి behavior‌ను compare చేయడం.

''' + fig('g10-funnel', 'Signup funnel: 1,000 visit, 700 start signup, 500 verify email, 400 complete signup', 'ఉదాహరణ funnel – 1,000 మందిలో 40% signup పూర్తి చేశారు; అతిపెద్ద drop-off మొదటి step లో.', 'Illustrative funnel: 40% of initial visitors completed signup; the biggest drop-off is at the first step.'),
 defs=['Funnel Analysis: Funnel Analysis measures how users progress through a sequence of steps toward a specific conversion goal and identifies drop-off points.',
       'Cohort Analysis: Cohort Analysis groups users based on shared characteristics or experiences and tracks their behavior over time.'],
 hdr=['Funnel Analysis', 'Cohort Analysis'],
 rows=[['Step-by-step conversion', 'Group-based behavior over time'], ['Identifies drop-off', 'Identifies retention patterns'], ['Signup and checkout', 'Monthly user groups'], ['Conversion optimization', 'Retention and engagement analysis']],
 tbl_te=[['Step-by-step conversion','కాలక్రమంలో group ప్రవర్తన'],['Drop-off గుర్తిస్తుంది','Retention patterns గుర్తిస్తుంది'],['Signup, checkout','నెలవారీ user groups'],['Conversion మెరుగుదల','Retention, engagement విశ్లేషణ']],
 ex_title='Learning App',
 ex_te='''Funnel Analysis:
1. Website సందర్శించడం.
2. Register చేయడం.
3. Course ఎంచుకోవడం.
4. Payment చేయడం.
5. Learning ప్రారంభించడం.

Cohort Analysis:
- January signup users.
- February signup users.
- March signup users.

ఈ cohorts‌లో 7-day retention, 30-day retention compare చేయవచ్చు.''',
 ex_en='''Funnel Analysis:
1. Visit website.
2. Register.
3. Select course.
4. Make payment.
5. Start learning.

Cohort Analysis:
- January signup users.
- February signup users.
- March signup users.

7-day and 30-day retention can be compared across these cohorts.''',
 iv_en='"Funnel Analysis helps identify where users drop off during a sequence of actions, while Cohort Analysis tracks the behavior of specific user groups over time. I use funnel analysis to improve conversion and cohort analysis to understand retention and long-term engagement."',
 iv_te='Funnel – users ఎక్కడ drop-off అవుతున్నారు (conversion); Cohort – user groups కాలక్రమంలో ఎలా ప్రవర్తిస్తున్నారు (retention).'),

dict(n=142, A='Vanity Metrics', B='Actionable Metrics', q_te='Vanity Metrics మరియు Actionable Metrics మధ్య తేడా ఏమిటి?',
 te='''Vanity Metrics:

చూడటానికి impressive‌గా కనిపించే కానీ business లేదా product decisions తీసుకోవడానికి ఉపయోగకరమైన insight ఇవ్వని metrics.

ఉదాహరణలు:
- Active usage లేని total downloads.
- Conversion context లేని total page views.
- Engagement లేని total social media followers.

Actionable Metrics:

ఒక meaningful decision లేదా product improvement‌కు దారితీసే metrics.

ఉదాహరణలు:
- Checkout abandonment rate.
- Task success rate.
- 30-day retention.
- Conversion rate.
- Support ticket resolution time.''',
 defs=['Vanity Metrics: Vanity Metrics are numbers that may look impressive but do not necessarily provide meaningful insights into product performance or business outcomes. Examples: total downloads without active usage, total page views without conversion context, total social media followers without engagement.',
       'Actionable Metrics: Actionable Metrics provide meaningful insights that help teams make informed decisions and improve product performance. Examples: checkout abandonment rate, task success rate, 30-day retention, conversion rate, support ticket resolution time.'],
 hdr=['Vanity Metrics', 'Actionable Metrics'],
 rows=[['Looks impressive', 'Drives decisions'], ['Often surface-level', 'Provides meaningful insights'], ['Total downloads', 'Active users'], ['Total page views', 'Qualified conversion'], ['Total followers', 'Engagement and retention']],
 tbl_te=[['ఆకట్టుకునేలా కనిపిస్తుంది','నిర్ణయాలకు దారితీస్తుంది'],['తరచుగా పైపై స్థాయి','అర్థవంతమైన insights ఇస్తుంది'],['మొత్తం downloads','Active users'],['మొత్తం page views','అర్హత ఉన్న conversion'],['మొత్తం followers','Engagement, retention']],
 ex_title='Design Acharya',
 ex_te='''Vanity Metrics:
- 10,000 website visitors.
- 5,000 social media followers.
- 2,000 app downloads.

Actionable Metrics:
- 500 qualified course enquiries.
- 100 paid admissions.
- 80% course completion.
- 70% student retention.
- Placement, portfolio completion rates.''',
 ex_en='''Vanity Metrics:
- 10,000 website visitors.
- 5,000 social media followers.
- 2,000 app downloads.

Actionable Metrics:
- 500 qualified course enquiries.
- 100 paid admissions.
- 80% course completion.
- 70% student retention.
- Placement and portfolio completion rates.''',
 iv_en='"Vanity Metrics show numbers that may look impressive but do not necessarily guide decisions. Actionable Metrics help teams understand actual user behavior and business performance, enabling measurable product improvements."',
 iv_te='Vanity metrics ఆకట్టుకునే సంఖ్యలు మాత్రమే; Actionable metrics నిజమైన ప్రవర్తన, పనితీరును చూపి కొలవగల మెరుగుదలకు దారితీస్తాయి.'),
]

INTRO_TE = 'ఇది మన 142-question UX Interview Preparation Guide‌లో చివరి గ్రూప్. ఈ గ్రూప్‌లో UX Metrics, Product Analytics, User Behavior, Conversion, Retention, A/B Testing వంటి ముఖ్యమైన అంశాలను నేర్చుకుందాం. ఇంటర్వ్యూలలో ఒక ముఖ్యమైన ప్రశ్న: "How do you measure the success of your design?" దీనికి సమాధానం ఇవ్వాలంటే కేవలం మంచి UI Design చూపించడం సరిపోదు; మన design వల్ల user behavior, usability, engagement, conversion, retention లో వచ్చిన మార్పులను metrics ద్వారా అర్థం చేసుకోవాలి.'
REVISION = [(131, 'Qualitative vs Quantitative', 'Descriptive vs Numerical'), (132, 'KPI vs UX Metrics', 'Business Performance vs Experience'),
 (133, 'DAU vs MAU', 'Daily vs Monthly Active Users'), (134, 'Conversion vs Retention', 'Action Completion vs Continued Usage'),
 (135, 'Bounce vs Exit Rate', 'Non-engaged Sessions vs Last Page'), (136, 'Task Success vs Completion', 'Achieving Goal vs Finishing Task'),
 (137, 'SUS vs NPS', 'Perceived Usability vs Recommendation'), (138, 'CSAT vs CES', 'Satisfaction vs Effort'),
 (139, 'A/B vs Multivariate', 'Version Comparison vs Combination Testing'), (140, 'Heatmap vs Session Recording', 'Aggregate Patterns vs Individual Playback'),
 (141, 'Funnel vs Cohort', 'Conversion Steps vs User Groups Over Time'), (142, 'Vanity vs Actionable', 'Impressive Numbers vs Decision-making Insights')]
PRACTICE_TITLE = 'Practical Interview Quiz – UX Metrics Knowledge Check'
PRACTICE_BODY = '''ఈ 5 questions ద్వారా UX Metrics & Analytics concepts‌ను పరీక్షించుకోండి.

1. Which data type helps explain why users are struggling with a feature? (Quantitative Data / Qualitative Data / Vanity Metrics)
2. Which metric measures users returning to a product over time? (Conversion Rate / Retention Rate / Bounce Rate)
3. Which method measures perceived system usability using 10 questions? (NPS / SUS / CES)
4. Which technique helps identify where users drop off during checkout? (Cohort Analysis / Funnel Analysis / Heatmap)
5. Which is an actionable metric for improving a checkout experience? (Total website downloads / Checkout abandonment rate / Total social followers)

### Answer key · జవాబులు
1. Qualitative Data · 2. Retention Rate · 3. SUS · 4. Funnel Analysis · 5. Checkout abandonment rate'''

# Closing pages of the PDF (guide completed, revision plan, final advice)
EXTRAS = [
('Congratulations! – 142 Questions Completed · గైడ్ పూర్తయింది', '''UX Interview Preparation Guide పూర్తయింది – 10 Groups · 142 Comparison Questions.

Group\tTopic\tQuestions
0\tUser Flow vs User Journey, Task Flow vs User Flow (bonus)\t2
1\tUX Research & Discovery\t15
2\tUX Strategy & Design Thinking\t10
3\tInformation Architecture & User Flows\t15
4\tUX Deliverables & Documentation\t15
5\tInteraction Design & Prototyping\t20
6\tUsability Testing & Evaluation\t15
7\tUI Design & Design Systems\t15
8\tAccessibility & Inclusive Design\t10
9\tProduct Design & Development\t15
10\tUX Metrics & Analytics\t12
Total\t10 Groups (+ Group 0)\t142 (+2)

### How to use this guide for Senior UX interviews · ఈ గైడ్‌ను ఎలా ఉపయోగించాలి
మీ 20+ years design experience మరియు product design leadership background‌ను దృష్టిలో ఉంచుకుంటే, ఈ 142 questions‌ను definitions కంఠస్థం చేసుకోవడం కంటే, మీ actual project experiences‌తో connect చేయడం మంచిది.

ఈ 5 projects ఆధారంగా examples సిద్ధం చేసుకోండి:
- Classic Rummy – Openplay: Game UX, onboarding, user flows, interaction design, engagement, usability, analytics.
- TWAM – D'SARAS: E-commerce UX, product discovery, shopping journey, checkout, responsive UI.
- ResolveAI – Concept Project: Enterprise SaaS, dashboard, AI workflows, design systems, accessibility, data visualization.
- ORRBUS – Concept Project: Mobility UX, location-based experiences, navigation, information architecture.
- Design Acharya – D'SARAS: EdTech product strategy, bilingual UX, inclusive design, learning journeys, product vision.'''),
('Suggested 7-day interview revision plan · 7 రోజుల revision ప్లాన్', '''Day\tPreparation\tFocus
1\tGroups 1–2\tResearch & Strategy
2\tGroups 3–4\tIA & Deliverables
3\tGroups 5–6\tInteraction & Testing
4\tGroups 7–8\tUI & Accessibility
5\tGroups 9–10\tProduct & Analytics
6\tProject-based preparation\tClassic Rummy, TWAM, ResolveAI
7\tMock interviews\tSenior & Leadership questions

### Final advice: Move from Definitions to Decision-making
Senior-level interviews‌లో interviewer మీకు UX terminology తెలుసా అని మాత్రమే అడగరు. ఆ concepts‌ను real-world product problems‌లో ఎలా apply చేశారో తెలుసుకోవాలనుకుంటారు.

ప్రతి question‌కు ఈ 4 steps‌లో సమాధానం సిద్ధం చేసుకోండి:
1. Definition: Concept అంటే ఏమిటి?
2. Difference: Related concept‌తో తేడా ఏమిటి?
3. Application: Real project‌లో ఎలా ఉపయోగించారు?
4. Impact: User లేదా business‌కు వచ్చిన measurable benefit ఏమిటి?

### Example: "How do you measure the success of your design?"
"I measure design success through a combination of usability metrics, user satisfaction, and business outcomes. For example, I track task success rate, task completion time, conversion rate, and retention. I also combine quantitative analytics with qualitative user feedback to identify improvement opportunities. My goal is to ensure that the design solves real user problems while contributing to business objectives."

తెలుగు అర్థం: Usability metrics, user సంతృప్తి, business ఫలితాలు – ఈ మూడింటి కలయికతో design విజయాన్ని కొలుస్తాను; quantitative analytics ను qualitative feedback తో కలిపి మెరుగుదల అవకాశాలు గుర్తిస్తాను.'''),
]
