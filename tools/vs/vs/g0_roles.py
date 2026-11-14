# Group 0 · 0.3 – Product Manager vs Product Designer vs UX Designer vs UI Designer
# Source: PM_vs_PD_vs_UX_vs_UI_Designer.pdf (English text kept as the English answer; its section 6 Telugu table/analogy kept).
# Telugu answer = Claude's translation of the PDF's English sections. Diagrams = Claude's own drawings (figs_g0.py);
# the PDF's three images (medium.com, behance.net) are not copied.

def fig(k, alt, te, en): return f'!fig:assets/images/vs/{k}.svg|{alt}|{te}|{en}'

FIG_GLANCE = ('vs-roles-glance', 'Four coloured cards: Product Manager – what and why; Product Designer – how the product solves the problem; UX Designer – how users complete tasks easily; UI Designer – how the interface looks')
FIG_FLOW = ('vs-roles-workflow', 'Six numbered steps: Product Manager, Product Designer, UX Designer, UI Designer, Engineering Team, Product Team, looping back')

Q_EN = 'What is the difference between a Product Manager, Product Designer, UX Designer and UI Designer?'
Q_TE = 'Product Manager, Product Designer, UX Designer మరియు UI Designer మధ్య తేడా ఏమిటి?'

TE = f"""ఈ నాలుగు roles ఒక విజయవంతమైన digital product నిర్మించడానికి దగ్గరగా కలిసి పనిచేస్తాయి, కానీ ప్రతి role కు వేర్వేరు బాధ్యత ఉంటుంది.
Swiggy లేదా Zomato లాంటి ఒక food delivery app నిర్మించడం అనే practical ఉదాహరణతో అర్థం చేసుకుందాం.

### 1 · నాలుగు roles ఒక్క చూపులో
Understand the four roles at a glance

{fig(FIG_GLANCE[0], FIG_GLANCE[1], 'ఒకే product – నాలుగు roles, నాలుగు వేర్వేరు ప్రశ్నలు.', 'One product, four roles, four different questions.')}

Role\tప్రధాన బాధ్యత\tకీలక ప్రశ్న
Product Manager (PM)\tProduct దిశ మరియు business విజయం\tఏమి build చేయాలి, ఎందుకు?
Product Designer\tEnd-to-end product అనుభవం మరియు సమస్య పరిష్కారం\tProduct సమస్యను ఎలా పరిష్కరించాలి?
UX Designer\tUser అవసరాలు, usability, interaction flow\tUsers తమ పనులను సులభంగా ఎలా పూర్తి చేస్తారు?
UI Designer\tVisual interface మరియు presentation\tInterface ఎలా కనిపించాలి?

ముఖ్యమైన తేడా: Product Design ఒక విస్తృత discipline. UX మరియు UI దానిలో ముఖ్యమైన భాగాలు. కొన్ని కంపెనీల్లో ఒకే Product Designer UX మరియు UI రెండింటినీ చూసుకుంటారు; మరికొన్నింటిలో ఈ బాధ్యతలు specialists మధ్య విభజించబడతాయి.

### 2 · ఉదాహరణ: Food delivery app నిర్మించడం
ఒక కంపెనీ కొత్త food delivery app నిర్మించాలనుకుంటోంది అనుకుందాం.

A. Product Manager – ఏమి, ఎందుకు అని నిర్ణయిస్తారు:

సమస్య: Customers payment పూర్తి చేయకముందే food orders ను మధ్యలో వదిలేస్తున్నారు.
Product Manager business సమస్య, customer feedback, product data ను పరిశీలిస్తారు.

బాధ్యతలు:
- Business goals మరియు customer problems అర్థం చేసుకోవడం.
- Product vision మరియు strategy నిర్వచించడం.
- Features కు priority ఇవ్వడం.
- Product roadmap మరియు requirements తయారు చేయడం.
- Business, design, engineering teams ను సమన్వయం చేయడం.
- Success metrics నిర్వచించడం.

ఉదాహరణ నిర్ణయం: "Order abandonment తగ్గించి, పూర్తయ్యే orders పెంచడానికి checkout process ను సరళం చేయాలి."

సాధ్యమైన success metrics:
- Checkout completion rate
- Order conversion rate
- Revenue per order
- Customer retention

B. Product Designer – End-to-end అనుభవానికి బాధ్యత వహిస్తారు:

Product Designer సమస్యను ఒక పూర్తి product అనుభవంగా మారుస్తారు.

బాధ్యతలు:
- User మరియు business అవసరాలు అర్థం చేసుకోవడం.
- User research చేయడం లేదా దానిలో సహకరించడం.
- సమస్యను, design strategy ని నిర్వచించడం.
- User journeys మరియు information architecture రూపొందించడం.
- User flows, wireframes, prototypes design చేయడం.
- Visual UI మరియు design systems రూపొందించడం.
- Usability testing ద్వారా designs ను validate చేయడం.
- Developers మరియు Product Managers తో కలిసి పనిచేయడం.

ఉదాహరణ నిర్ణయం: "తక్కువ steps, స్పష్టమైన pricing, అనేక payment options తో సరళమైన checkout అనుభవం సృష్టిద్దాం."
Product Designer user needs, business goals మరియు technical feasibility ని కలుపుతారు.

C. UX Designer – Usability మరియు user ప్రవర్తనపై దృష్టి:

Users తమ పనులను ఎంత సులభంగా పూర్తి చేయగలరో UX Designer దృష్టి పెడతారు.

బాధ్యతలు:
- User research మరియు interviews.
- Personas మరియు user journeys.
- Information architecture.
- User flows మరియు task flows.
- Wireframes మరియు interaction design.
- Usability testing.
- Accessibility మరియు అనుభవ మెరుగుదలలు.

ఉదాహరణ నిర్ణయం: "Delivery address మరియు payment steps వద్ద users గందరగోళానికి గురవుతున్నారు. అనవసర steps తగ్గించి, order summary ని సులభంగా అర్థమయ్యేలా చేద్దాం."

D. UI Designer – Visual design పై దృష్టి:

UI Designer interface ను దృశ్యపరంగా స్పష్టంగా, స్థిరంగా (consistent), ఆకర్షణీయంగా తయారు చేస్తారు.

బాధ్యతలు:
- Layout మరియు visual hierarchy.
- Typography మరియు colour systems.
- Buttons, icons మరియు components.
- Spacing మరియు visual consistency.
- Responsive interface design.
- Design system మరియు UI specifications.

ఉదాహరణ నిర్ణయం: "Total price ను మరింత ప్రముఖంగా చూపించి, button contrast మెరుగుపరిచి, checkout screens అంతటా ఒకే visual style ఉపయోగిద్దాం."

### 3 · నాలుగు roles కలిసి ఎలా పనిచేస్తాయి
How all four roles work together

{fig(FIG_FLOW[0], FIG_FLOW[1], 'సరళీకరించిన product development workflow – ఇది conceptual మాత్రమే; నిజమైన teams లో roles overlap అవుతూ నిరంతరం కలిసి పనిచేస్తాయి.', 'A simplified, conceptual workflow – in real teams the roles overlap and collaborate continuously.')}

1. Product Manager – Business సమస్యను గుర్తించి, product priorities నిర్వచిస్తారు. Output: Product vision, roadmap, requirements, priorities.
2. Product Designer – సమస్యను అర్థం చేసుకుని మొత్తం product అనుభవాన్ని రూపొందిస్తారు. Output: Design strategy, experience concepts, prototypes.
3. UX Designer – Structure, user journey, interaction flow నిర్వచిస్తారు. Output: User research, journeys, IA, wireframes, usability findings.
4. UI Designer – Visual interface మరియు reusable components సృష్టిస్తారు. Output: High-fidelity screens, visual design, UI specifications.
5. Engineering Team – Team తో కలిసి పనిచేస్తూ product ను develop చేసి implement చేస్తుంది. Output: పనిచేసే product.
6. Product Team – ఫలితాలను కొలిచి, users నుంచి నేర్చుకుని, product ను మెరుగుపరుస్తుంది.

గమనిక: ఇది conceptual workflow మాత్రమే, కఠినమైన handoff process కాదు. ఆధునిక product teams లో ఈ roles నిరంతరం కలిసి పనిచేస్తాయి, ఒకదానితో ఒకటి overlap అవుతాయి.

### 4 · మీ Classic Rummy project తో ఉదాహరణ
Openplay Technologies లో మీ అనుభవం నుంచి ఒక నిజమైన product సన్నివేశం

సమస్య: కొత్త users Rummy game ఆడటం ఎలా ప్రారంభించాలో అర్థం చేసుకోవడంలో ఇబ్బంది పడుతున్నారు.

Role\tవారు ఏమి చేస్తారు
Product Manager\tNew-user activation ను product priority గా గుర్తిస్తారు.
Product Designer\tపూర్తి onboarding మరియు ఆడే అనుభవాన్ని ఎలా మెరుగుపరచాలో explore చేస్తారు.
UX Designer\tUser గందరగోళాన్ని అధ్యయనం చేసి, onboarding ను సరళం చేసి, game-start flow ను మెరుగుపరుస్తారు.
UI Designer\tCard visibility, buttons, instructions, typography, visual hierarchy ను మెరుగుపరుస్తారు.

ఉదాహరణకు:
- PM: New-player activation మెరుగుపరచాలి.
- Product Designer: First-time player అనుభవాన్ని మెరుగుపరుద్దాం.
- UX Designer: Registration, onboarding, table లో join అవ్వడాన్ని సరళం చేద్దాం.
- UI Designer: Screens ను మరింత స్పష్టంగా, actions ను మరింత కనిపించేలా చేద్దాం.

వేర్వేరు roles ఒకే product లక్ష్యానికి ఇలా contribute చేస్తాయి.

### 5 · Deliverables లో తేడా
ఏ deliverable కు ప్రధానంగా ఎవరు బాధ్యులు

Deliverable\tప్రధాన బాధ్యులు
Product vision\tProduct Manager
Product roadmap\tProduct Manager
PRD (Product Requirements Document)\tProduct Manager, team input తో
User research\tUX Designer / Product Designer
Persona\tUX Designer
User journey map\tUX Designer / Product Designer
Information architecture\tUX Designer
User flow\tUX Designer / Product Designer
Wireframes\tUX Designer / Product Designer
Interactive prototype\tProduct Designer / UX Designer
Visual design\tUI Designer / Product Designer
Design system\tUI Designer / Product Designer
Usability testing\tUX Designer / Product Designer
Product analytics\tProduct Manager, design మరియు analytics teams తో

### 6 · సరళమైన తెలుగు వివరణ
Simple Telugu explanation

Role\tతెలుగు అర్థం
Product Manager\tఏ సమస్యను పరిష్కరించాలి? ఎందుకు పరిష్కరించాలి? అని నిర్ణయిస్తారు.
Product Designer\tఆ సమస్యకు పూర్తి స్థాయి ప్రొడక్ట్ అనుభవాన్ని ఎలా రూపొందించాలి అని ఆలోచిస్తారు.
UX Designer\tయూజర్ సులభంగా పని పూర్తి చేసుకునేలా అనుభవాన్ని రూపొందిస్తారు.
UI Designer\tయాప్ లేదా వెబ్‌సైట్ ఎలా కనిపించాలి, రంగులు, ఫాంట్స్, బటన్స్ ఎలా ఉండాలి అని రూపొందిస్తారు.

ఒక చిన్న ఉదాహరణ – ఒక ఇంటిని నిర్మిస్తున్నామని అనుకోండి:
- Product Manager – ఎలాంటి ఇల్లు నిర్మించాలి, ఎందుకు నిర్మించాలి, బడ్జెట్ ఎంత?
- Product Designer – ఇంటి మొత్తం అనుభవం, అవసరాలు, డిజైన్ ఎలా ఉండాలి?
- UX Designer – గదుల అమరిక, మనుషులు సులభంగా తిరగడానికి మార్గాలు ఎలా ఉండాలి?
- UI Designer – ఇంటి రంగులు, లైటింగ్, ఫర్నిచర్, అందం ఎలా ఉండాలి?

ఇది అర్థం చేసుకోవడానికి ఒక analogy మాత్రమే.

### 7 · Career దృష్టికోణం: మీ అనుభవానికి ఏ role సరిపోతుంది?
UX/UI, product design, animation, creative direction అనుభవం ఆధారంగా

Job title\tసాధారణ దృష్టి
Senior UX Designer\tUX research, flows, usability, interaction
Senior UI/UX Designer\tUX + visual interface design
Senior Product Designer\tEnd-to-end product సమస్య పరిష్కారం
Lead Product Designer\tDesign దిశ, mentoring, cross-functional సహకారం
Principal Product Designer\tక్లిష్టమైన product strategy, design ప్రభావం, organisation అంతటా impact
Head of Product Design\tDesign organisation, people leadership, design vision

మీ career దిశకు Senior Product Designer, Lead Product Designer, Principal Product Designer roles ప్రత్యేకంగా సంబంధితమైనవి – ప్రతి కంపెనీ అంచనాలను బట్టి explore చేయండి.

### 8 · ఇంటర్వ్యూలో బలమైన సమాధానం
Question: What is the difference between a Product Manager and a Product Designer?

“A Product Manager primarily focuses on product strategy, business goals, priorities and deciding what problems the product should solve.
A Product Designer focuses on translating those problems into meaningful user experiences by understanding user needs, defining workflows, designing interactions and creating user-friendly interfaces.
UX Design focuses more on usability and the overall user journey, while UI Design focuses on the visual presentation and interface.
In modern product teams, these roles collaborate closely. As a Product Designer, I believe my responsibility is to balance user needs, business objectives and technical feasibility to create successful digital products.”

తెలుగు అర్థం: PM product strategy, business goals, priorities, ఏ సమస్యలు పరిష్కరించాలో నిర్ణయిస్తారు. Product Designer ఆ సమస్యలను అర్థవంతమైన user అనుభవాలుగా మారుస్తారు. UX usability, user journey పై; UI visual presentation పై దృష్టి పెడతాయి. Product Designer గా user needs, business objectives, technical feasibility ని సమతుల్యం చేయడమే నా బాధ్యత."""

EN = f"""These four roles work closely together to build a successful digital product, but each role has a different responsibility.
Let's understand them using a practical example: building a food delivery app like Swiggy or Zomato.

### 1 · The four roles at a glance
Understand the four roles at a glance

{fig(FIG_GLANCE[0], 'Four roles at a glance', '', 'One product, four roles, four different questions.')}

Role\tMain responsibility\tKey question
Product Manager (PM)\tProduct direction and business success\tWhat should we build, and why?
Product Designer\tEnd-to-end product experience and problem-solving\tHow should the product solve the problem?
UX Designer\tUser needs, usability and interaction flow\tHow will users complete their tasks easily?
UI Designer\tVisual interface and presentation\tHow should the interface look?

An important distinction: Product Design is a broader discipline. UX and UI are important parts of Product Design. In some companies, one Product Designer handles UX and UI together; in others, these responsibilities are split across specialists.

### 2 · Example: Building a food delivery app
Imagine a company wants to build a new food delivery app.

A. Product Manager — Decides what and why:

Problem: Customers are abandoning their food orders before completing payment.
The Product Manager investigates the business problem, customer feedback and product data.

Responsibilities:
- Understand business goals and customer problems.
- Define product vision and strategy.
- Prioritise features.
- Prepare product roadmap and requirements.
- Coordinate business, design and engineering teams.
- Define success metrics.

Example decision: "We need to simplify the checkout process to reduce order abandonment and improve completed orders."

Possible success metrics:
- Checkout completion rate
- Order conversion rate
- Revenue per order
- Customer retention

B. Product Designer — Owns the end-to-end experience:

The Product Designer translates the problem into a complete product experience.

Responsibilities:
- Understand user and business needs.
- Conduct or collaborate on user research.
- Define the problem and design strategy.
- Create user journeys and information architecture.
- Design user flows, wireframes and prototypes.
- Create visual UI and design systems.
- Validate designs through usability testing.
- Collaborate with developers and Product Managers.

Example decision: "Let's create a simpler checkout experience with fewer steps, clear pricing and multiple payment options."
The Product Designer connects user needs, business goals and technical feasibility.

C. UX Designer — Focuses on usability and user behaviour:

The UX Designer focuses on how easily users can complete their tasks.

Responsibilities:
- User research and interviews.
- Personas and user journeys.
- Information architecture.
- User flows and task flows.
- Wireframes and interaction design.
- Usability testing.
- Accessibility and experience improvements.

Example decision: "Users are confused by the delivery address and payment steps. Let's reduce unnecessary steps and make the order summary easier to understand."

D. UI Designer — Focuses on visual design:

The UI Designer makes the interface visually clear, consistent and attractive.

Responsibilities:
- Layout and visual hierarchy.
- Typography and colour systems.
- Buttons, icons and components.
- Spacing and visual consistency.
- Responsive interface design.
- Design system and UI specifications.

Example decision: "Let's make the total price more prominent, improve button contrast and use a consistent visual style across checkout screens."

### 3 · How all four roles work together
Here is a simplified product development workflow

{fig(FIG_FLOW[0], 'How the four roles work together', '', 'A simplified, conceptual workflow – in real teams the roles overlap and collaborate continuously.')}

1. Product Manager – Identifies the business problem and defines product priorities. Output: Product vision, roadmap, requirements, priorities.
2. Product Designer – Understands the problem and shapes the overall product experience. Output: Design strategy, experience concepts, prototypes.
3. UX Designer – Defines the structure, user journey and interaction flow. Output: User research, journeys, IA, wireframes, usability findings.
4. UI Designer – Creates the visual interface and reusable components. Output: High-fidelity screens, visual design, UI specifications.
5. Engineering Team – Develops and implements the product, working with the team throughout. Output: Functional product.
6. Product Team – Measures results, learns from users and improves the product.

Note: This is a conceptual workflow, not a strict handoff process. In modern product teams, these roles collaborate continuously and overlap.

### 4 · Example using your Classic Rummy project
A real product scenario from your experience at Openplay Technologies

Problem: New users are finding it difficult to understand how to start playing a Rummy game.

Role\tWhat they would do
Product Manager\tIdentify new-user activation as a product priority.
Product Designer\tExplore how to improve the complete onboarding and playing experience.
UX Designer\tStudy user confusion, simplify onboarding and improve the game-start flow.
UI Designer\tImprove card visibility, buttons, instructions, typography and visual hierarchy.

For example:
- PM: We need to improve new-player activation.
- Product Designer: Let's improve the first-time player experience.
- UX Designer: Let's simplify registration, onboarding and joining a table.
- UI Designer: Let's make the screens clearer and the actions more visible.

This is how different roles contribute to the same product goal.

### 5 · Difference in deliverables
Who primarily owns each deliverable

Deliverable\tPrimary owner
Product vision\tProduct Manager
Product roadmap\tProduct Manager
PRD (Product Requirements Document)\tProduct Manager, with team input
User research\tUX Designer / Product Designer
Persona\tUX Designer
User journey map\tUX Designer / Product Designer
Information architecture\tUX Designer
User flow\tUX Designer / Product Designer
Wireframes\tUX Designer / Product Designer
Interactive prototype\tProduct Designer / UX Designer
Visual design\tUI Designer / Product Designer
Design system\tUI Designer / Product Designer
Usability testing\tUX Designer / Product Designer
Product analytics\tProduct Manager, with design and analytics teams

### 6 · A simple analogy
Building a house

- Product Manager – What kind of house should we build, why, and what is the budget?
- Product Designer – What should the overall experience, needs and design of the house be?
- UX Designer – How should the rooms be arranged so people can move around easily?
- UI Designer – What should the colours, lighting, furniture and look of the house be?

This is only an analogy to help understanding.

### 7 · Career perspective: Which role fits your experience?
Based on your experience across UX/UI, product design, animation and creative direction

Job title\tTypical focus
Senior UX Designer\tUX research, flows, usability and interaction
Senior UI/UX Designer\tUX + visual interface design
Senior Product Designer\tEnd-to-end product problem-solving
Lead Product Designer\tDesign direction, mentoring and cross-functional collaboration
Principal Product Designer\tComplex product strategy, design influence and organisation-wide impact
Head of Product Design\tDesign organisation, people leadership and design vision

For your career direction, Senior Product Designer, Lead Product Designer and Principal Product Designer are particularly relevant roles to explore, depending on each company's expectations.

### 8 · Interview preparation: A strong answer
Question: What is the difference between a Product Manager and a Product Designer?

“A Product Manager primarily focuses on product strategy, business goals, priorities and deciding what problems the product should solve.
A Product Designer focuses on translating those problems into meaningful user experiences by understanding user needs, defining workflows, designing interactions and creating user-friendly interfaces.
UX Design focuses more on usability and the overall user journey, while UI Design focuses on the visual presentation and interface.
In modern product teams, these roles collaborate closely. As a Product Designer, I believe my responsibility is to balance user needs, business objectives and technical feasibility to create successful digital products.”"""

EX_TE = """Food delivery app – checkout సమస్య:
- PM: Order abandonment తగ్గించడానికి checkout ను సరళం చేయాలి.
- Product Designer: తక్కువ steps, స్పష్టమైన pricing, అనేక payment options తో కొత్త checkout అనుభవం.
- UX Designer: Address, payment steps లో గందరగోళం తొలగించి, order summary ని స్పష్టంగా చేయడం.
- UI Designer: Total price ప్రముఖంగా, button contrast మెరుగుగా, ఒకే visual style.

Remember this:
PM = What & Why · Product Designer = End-to-end experience · UX = How easily · UI = How it looks."""
EX_EN = """Food delivery app – checkout problem:
- PM: Simplify checkout to reduce order abandonment.
- Product Designer: A new checkout with fewer steps, clear pricing and multiple payment options.
- UX Designer: Remove confusion in the address and payment steps; make the order summary clear.
- UI Designer: Prominent total price, better button contrast, one consistent visual style.

Remember this:
PM = What & Why · Product Designer = End-to-end experience · UX = How easily · UI = How it looks."""

REVISION = [['Product Manager', 'What to build and why – vision, roadmap, priorities, success metrics'],
            ['Product Designer', 'End-to-end experience – balances user needs, business goals and feasibility'],
            ['UX Designer', 'How easily users complete tasks – research, journeys, IA, flows, usability'],
            ['UI Designer', 'How the interface looks – layout, typography, colour, components']]

QUIZ = ('Test your understanding · 0.3 roles quiz', """ఈ 4 questions‌తో మీ అవగాహనను పరీక్షించుకోండి.

1. Who primarily defines the product roadmap? (UI Designer / Product Manager / UX Designer / Frontend Developer)
2. Who primarily designs the user journey and task flow? (UX Designer / Product Manager / UI Designer / QA Engineer)
3. Who primarily works on typography, colours and visual hierarchy? (Product Manager / UX Researcher / UI Designer / Business Analyst)
4. Who connects user needs, business goals and technical feasibility through end-to-end design? (Product Designer / Only UI Designer / Only Product Manager / QA Engineer)

### Answer key · జవాబులు
1. Product Manager · 2. UX Designer · 3. UI Designer · 4. Product Designer""")
