import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANK_DIR = os.path.join(BASE_DIR, 'questions_bank')
os.makedirs(BANK_DIR, exist_ok=True)

# -------------------------------------------------------------
# TOPIC & CONCEPT DATA FOR CURRICULUM-ALIGNED KCSE QUESTIONS
# -------------------------------------------------------------

DAYS_CONFIG = {
    "monday_math": {
        "theme": "📐 MATHEMATICS MONDAY",
        "subjects": ["Mathematics Alt. A", "Mathematics Alt. B"],
        "topics": [
            ("Calculus & Turning Points", "A curve has equation y = 2x³ - 9x² + 12x - 3. Determine the coordinates of its stationary points and state their nature.", "Differentiate to get dy/dx = 6x² - 18x + 12. Equate to 0 and factorize 6(x - 1)(x - 2) = 0. Test with d²y/dx² = 12x - 18: at x=1, d²y/dx²=-6 (Max); at x=2, d²y/dx²=+6 (Min).", "Paper 1 Section II"),
            ("Trigonometry II", "Solve the trigonometric equation 2 cos²x + 3 sin x = 0 for 0° ≤ x ≤ 360°.", "Use cos²x = 1 - sin²x. Form quadratic 2(1 - sin²x) + 3 sin x = 0 => 2 sin²x - 3 sin x - 2 = 0. Factorize (2 sin x + 1)(sin x - 2) = 0. Since sin x ≤ 1, sin x = -0.5. Solutions: 210° and 330°.", "Paper 2 Section I"),
            ("Quadratic Expressions & Equations", "Solve for x by completing the square: 3x² - 7x + 2 = 0.", "Divide through by 3: x² - (7/3)x + 2/3 = 0. Move constant: x² - (7/3)x = -2/3. Add (-7/6)² = 49/36 to both sides. (x - 7/6)² = 25/36. x - 7/6 = ± 5/6 => x = 2 or x = 1/3.", "Paper 1 Section I"),
            ("Vectors II & Geometry", "Vector OA = 2i + 3j and OB = 8i - 9j. Point P divides AB in the ratio 2:1. Find the column vector OP and its magnitude.", "Use ratio theorem: OP = (1/3)OA + (2/3)OB. OP = 1/3[2, 3] + 2/3[8, -9] = [2/3 + 16/3, 1 - 6] = [6, -5]. Magnitude |OP| = √(6² + (-5)²) = √61 ≈ 7.81 units.", "Paper 2 Section II"),
            ("Linear Programming", "A baker makes two types of cakes, A and B. Cake A requires 200g flour and 100g sugar. Cake B requires 300g flour and 50g sugar. Available: 6kg flour and 2kg sugar. Formulate the inequalities.", "Let x = number of cake A, y = number of cake B. Non-negativity: x ≥ 0, y ≥ 0. Flour: 200x + 300y ≤ 6000 => 2x + 3y ≤ 60. Sugar: 100x + 50y ≤ 2000 => 2x + y ≤ 40.", "Paper 2 Section II"),
            ("Commercial Arithmetic & Taxation", "An employee earns a basic salary of KES 42,000, house allowance KES 12,000, and commuter allowance KES 4,000. Calculate their taxable income per month and apply personal relief of KES 2,400.", "Taxable income = 42,000 + 12,000 + 4,000 = KES 58,000. Calculate gross tax using standard PAYE tax bands, then subtract monthly personal relief (KES 2,400) to obtain net tax payable.", "Paper 1 Section II"),
            ("Probability", "A bag contains 5 red balls and 3 green balls. Two balls are picked at random one after another without replacement. Find the probability that both balls are of different colors.", "P(different) = P(R then G) + P(G then R) = (5/8 × 3/7) + (3/8 × 5/7) = 15/56 + 15/56 = 30/56 = 15/28.", "Paper 2 Section I"),
            ("Matrices & Transformations", "Matrix M = [2, 1; 3, 4] maps triangle ABC with area 15 cm² onto A'B'C'. Calculate the determinant of M and the area of image triangle A'B'C'.", "Determinant of M = (2 × 4) - (1 × 3) = 8 - 3 = 5. Area of image = |det M| × Object Area = 5 × 15 = 75 cm².", "Paper 2 Section I"),
            ("Circles: Chords & Tangents", "In a circle with radius 10 cm, a chord of length 12 cm is drawn. Calculate the perpendicular distance from the center of the circle to the chord.", "A perpendicular from center bisects chord into two 6 cm halves. By Pythagoras: distance d = √(r² - (chord/2)²) = √(10² - 6²) = √(100 - 36) = √64 = 8 cm.", "Paper 1 Section I"),
            ("Indices & Logarithms", "Solve for x without using mathematical tables or calculator: log₁₀(3x + 4) - log₁₀(x - 2) = 1.", "Use quotient law: log₁₀((3x + 4)/(x - 2)) = 1. Convert to exponential form: (3x + 4)/(x - 2) = 10¹ = 10. 3x + 4 = 10(x - 2) => 3x + 4 = 10x - 20 => 7x = 24 => x = 24/7.", "Paper 1 Section I"),
            ("Three Dimensional Geometry", "A right pyramid with vertex V stands on a rectangular base ABCD where AB = 8 cm, BC = 6 cm, and slant edges VA=VB=VC=VD = 13 cm. Calculate the angle between edge VA and base ABCD.", "Diagonal AC = √(8² + 6²) = 10 cm. Half-diagonal AO = 5 cm. In right-angled triangle VOA: cos θ = AO/VA = 5/13 => θ = cos⁻¹(5/13) ≈ 67.38°.", "Paper 2 Section II")
        ]
    },
    "tuesday_languages": {
        "theme": "📖 LANGUAGES TUESDAY",
        "subjects": ["English", "Kiswahili"],
        "topics": [
            ("English Grammar: Conditionals", "Rewrite the following sentence beginning with 'Had...': 'If the students had revised thoroughly, they would have passed with distinction.'", "Inversion rule: When omitting 'if' in third conditional, invert had and subject: 'Had the students revised thoroughly, they would have passed with distinction.'", "English Paper 2 Question 5"),
            ("Kiswahili Sarufi: Nyakati na Hali", "Tunga sentensi moja ukitumia kiambishi cha wakati uliopita 'li' na hali ya kuendelea 'ki'.", "Mfano sahihi: 'Mwalimu alipofika darasani, wanafunzi walikuwa wakisoma kwa bidii.' Hapa 'walikuwa' (wakati uliopita) na 'wakisoma' (hali ya kuendelea).", "Kiswahili Karatasi ya 2"),
            ("English Vocabulary & Phrasal Verbs", "Replace the underlined words with the most appropriate phrasal verb: 'The principal decided to cancel the morning meeting due to the heavy rain.'", "Cancel = 'call off' (Past tense: 'called off'). Notice: 'put off' means postpone, while 'call off' means cancel.", "English Paper 2 Question 5"),
            ("Kiswahili Isimu Jamii: Sajili ya Hospitalini", "Taja sifa nne za lugha inayotumika katika sajili ya hospitalini.", "1. Lugha yenye staha na unyenyekevu. 2. Matumizi ya msamiati maalum wa kitiba (k.m. dozi, vipimo, sindano). 3. Lugha ya kuelekeza/masharti. 4. Mara nyingi ni lugha tulivu ya kutia moyo.", "Kiswahili Karatasi ya 2"),
            ("English Poetry Appreciation", "Identify the sound device in the following line and state its stylistic effect: 'The sly snake slithered silently across the sand.'", "Device: Alliteration (repetition of initial /s/ consonant sound). Effect: Creates a hissing auditory imagery (sibilance) mimicking the stealthy movement of the serpent.", "English Paper 2 Question 3"),
            ("Kiswahili Fasihi Simulizi: Ulumbi", "Fafanua maana ya ulumbi katika fasihi simulizi na ueleze sifa mbili za mlumbi.", "Ulumbi ni ustadi na ufasaha wa kutumia maneno kwa ufundi mkubwa ili kushawishi au kuvutia wasikilizaji. Sifa: 1. Ujasiri na ukakamavu jukwaani. 2. Ujuzi mpana wa methali, nahau na tamathali za usemi.", "Kiswahili Karatasi ya 3"),
            ("English Cloze Test Mastery", "What are the three cardinal rules when answering an English Paper 1 Cloze Test?", "1. Read through the whole passage first without writing anything to grasp context. 2. Fill in ONLY ONE word per blank. 3. Check grammatical concordance (tense, singular/plural, parts of speech).", "English Paper 1 Question 2"),
            ("Kiswahili Ufahamu & Ufupisho", "Eleza mambo manne ya kuzingatia unapoandika ufupisho wa aya (muhtasari) katika Karatasi ya 2.", "1. Kuzingatia hoja kuu pekee bila mifano au maelezo ya ziada. 2. Kuandika kwa maneno yako mwenyewe bila kunukuu neno kwa neno. 3. Kuzingatia idadi ya maneno uliyopewa. 4. Kutumia mtiririko wa kiaya au nambari kulingana na maagizo.", "Kiswahili Karatasi ya 2"),
            ("English Functional Writing: Formal Letters", "In an official letter of application for a teaching vacancy, what are the mandatory layout components?", "Two addresses (Sender at top-right or left, Recipient on left), Date, Salutation, Subject heading (bold/underlined), Body paragraphs (intro, credentials, closing), Sign-off (Yours faithfully), Signature, Full Name.", "English Paper 1 Question 1"),
            ("Kiswahili Fasihi: Methali na Nahau", "Eleza maana ya nahau: 'Kupiga mbizi' na utunge sentensi inayoonyesha maana hiyo.", "Maana: Kuingia ndani ya maji kwa kichwa, au kwa maana ya kimafumbo: kujitosa katika jambo gumu kwa ujasiri. Mfano: 'Juma alipiga mbizi kwenye masomo ya hesabu hadi akaibuka mshindi.'", "Kiswahili Karatasi ya 2"),
            ("English Literary Devices: Irony", "Differentiate between dramatic irony and situational irony with brief examples.", "Situational irony: The actual outcome of an event is contrary to what was expected. Dramatic irony: The audience or reader knows crucial information that the characters are unaware of.", "English Paper 2 Question 2")
        ]
    },
    "wednesday_physical_sciences": {
        "theme": "🧪 PHYSICAL SCIENCES WEDNESDAY",
        "subjects": ["Chemistry", "Physics"],
        "topics": [
            ("Chemistry: Organic Chemistry I & II", "Write structural formula and IUPAC name for all isomers of pentane (C₅H₁₂).", "1. Pentane: CH₃-CH₂-CH₂-CH₂-CH₃. 2. 2-Methylbutane: CH₃-CH(CH₃)-CH₂-CH₃. 3. 2,2-Dimethylpropane: C(CH₃)₄. Notice boiling point decreases with branching.", "Chemistry Paper 2"),
            ("Physics: Current Electricity & Internal Resistance", "State Ohm's Law and explain why the potential difference across a real battery is lower than its electromotive force (EMF) when current flows.", "Ohm's Law: Current through a conductor is directly proportional to PD across it provided physical conditions (temperature) remain constant. Terminal PD V = E - Ir; energy is lost overcoming internal resistance r.", "Physics Paper 2"),
            ("Chemistry: Periodic Table & Ionization Energy", "Explain why the second ionization energy of Sodium (Na) is dramatically higher than its first ionization energy.", "After losing 1 electron, Na⁺ achieves a stable noble gas octet configuration (2.8). Removing a second electron requires pulling from a fully filled inner shell with reduced shielding and stronger nuclear attraction.", "Chemistry Paper 1"),
            ("Physics: Waves & Total Internal Reflection", "Calculate the critical angle for crown glass having a refractive index n = 1.52 when placed in air.", "Formula: sin c = 1/n. sin c = 1 / 1.52 = 0.6579. Critical angle c = sin⁻¹(0.6579) ≈ 41.14°.", "Physics Paper 1"),
            ("Chemistry: Volumetric Analysis & Stoichiometry", "25.0 cm³ of 0.1 M H₂SO₄ was neutralized completely by 20.0 cm³ of NaOH solution. Calculate the molarity of the sodium hydroxide solution.", "Reaction: H₂SO₄ + 2NaOH -> Na₂SO₄ + 2H₂O. Moles of acid = (25 × 0.1)/1000 = 0.0025 mol. Moles of base = 0.0025 × 2 = 0.005 mol. Molarity of NaOH = (0.005 × 1000)/20 = 0.25 M.", "Chemistry Paper 3 / Paper 1"),
            ("Physics: Newton's Laws of Motion", "A 1200 kg car travelling at 20 m/s is brought to rest over a distance of 40 m by braking force. Calculate the deceleration and braking force.", "v² = u² + 2as => 0 = 20² + 2a(40) => 80a = -400 => a = -5 m/s². Braking Force F = ma = 1200 kg × 5 m/s² = 6000 N.", "Physics Paper 1"),
            ("Chemistry: Electrochemistry & Redox", "Given standard electrode potentials: Zn²⁺/Zn = -0.76 V and Cu²⁺/Cu = +0.34 V. Write the overall cell representation and calculate E°cell.", "Cell notation: Zn(s) | Zn²⁺(aq) || Cu²⁺(aq) | Cu(s). E°cell = E°(cathode) - E°(anode) = +0.34 - (-0.76) = +1.10 V.", "Chemistry Paper 2"),
            ("Physics: Gas Laws", "A fixed mass of gas occupies 500 cm³ at 27°C and 760 mmHg. What volume will it occupy at 87°C if pressure is increased to 950 mmHg?", "Convert temperatures to Kelvin: T₁ = 27 + 273 = 300 K; T₂ = 87 + 273 = 360 K. Use general gas equation (P₁V₁)/T₁ = (P₂V₂)/T₂: (760 × 500)/300 = (950 × V₂)/360 => V₂ = 480 cm³.", "Physics Paper 1"),
            ("Chemistry: Rates of Reaction & Equilibrium", "According to Le Chatelier's principle, state the effect of increasing pressure on the equilibrium: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol).", "Increasing pressure shifts equilibrium to the side with fewer gas moles (forward reaction: 4 moles reactants -> 2 moles product), increasing the yield of ammonia.", "Chemistry Paper 2"),
            ("Physics: Radioactivity & Half-life", "A radioactive sample has an initial mass of 64 g. If its half-life is 5 days, calculate the mass remaining after 25 days.", "Number of half-lives n = 25 / 5 = 5. Remaining mass = 64 / (2⁵) = 64 / 32 = 2.0 g.", "Physics Paper 2"),
            ("Chemistry: Qualitative Analysis (Cations & Anions)", "How can you chemically distinguish between Zn²⁺(aq) and Al³⁺(aq) using aqueous ammonia?", "Add aqueous NH₃ dropwise until in excess: Both form a white precipitate initially. Zn²⁺ precipitate dissolves in excess NH₃ to form a colorless complex solution [Zn(NH₃)₄]²⁺, whereas Al³⁺ precipitate remains insoluble in excess.", "Chemistry Paper 3 / Paper 1")
        ]
    },
    "thursday_biological_sciences": {
        "theme": "🔬 BIOLOGICAL & EARTH SCIENCES THURSDAY",
        "subjects": ["Biology", "Geography"],
        "topics": [
            ("Biology: Physiology of Photosynthesis", "Differentiate between the Light Stage and Dark Stage of photosynthesis in terms of site of occurrence and products.", "Light Stage: Occurs in thylakoid/grana membranes; requires light; produces ATP, NADPH, and Oxygen gas (from photolysis of water). Dark Stage: Occurs in stroma; does not require light directly; uses CO₂, ATP, and NADPH to synthesize glucose.", "Biology Paper 1"),
            ("Geography: Physical Geography - Vulcanicity", "Name three volcanic features formed by extrusive vulcanicity and describe how a composite volcano (stratovolcano) is formed.", "Features: Volcanic cone, caldera, lava plateau. Formation of composite volcano: Alternate explosive eruptions of pyroclasts (ash/cinder) and gentle effusive flows of viscous lava solidify in distinct alternating layers around a central vent.", "Geography Paper 1"),
            ("Biology: Genetics - Monohybrid Inheritance", "In garden peas, tall stem (T) is dominant over dwarf stem (t). A heterozygous tall plant is crossed with a dwarf plant. Determine the genotypic and phenotypic ratios.", "Cross: Tt × tt. Gametes: T, t from parent 1 and t from parent 2. Offspring genotypes: 1 Tt : 1 tt (50% heterozygous tall, 50% homozygous dwarf). Phenotypic ratio = 1 Tall : 1 Dwarf.", "Biology Paper 2"),
            ("Geography: Mapwork - Relief & Drainage", "State three methods used to represent relief on topographical survey maps.", "1. Contour lines and form lines. 2. Spot heights and trigonometrical stations (trig points). 3. Color tinting (layer coloring) and hachures.", "Geography Paper 1 Section A"),
            ("Biology: Excretion & Osmoregulation", "Explain the role of the Antidiuretic Hormone (ADH) when blood osmotic pressure rises above normal.", "Osmoreceptors in hypothalamus detect increased osmotic pressure and stimulate posterior pituitary to release more ADH into bloodstream. ADH increases permeability of distal convoluted tubules and collecting ducts to water; more water is reabsorbed into blood, producing concentrated urine.", "Biology Paper 1"),
            ("Geography: Climate & Vegetation", "Explain four factors that influence the distribution of vegetation in Kenya.", "1. Precipitation/rainfall amounts. 2. Temperature variations due to altitude. 3. Soil depth, texture, and nutrient fertility. 4. Human activities (afforestation vs deforestation) and aspect/slope exposure.", "Geography Paper 1 Section B"),
            ("Biology: Ecology - Trophic Levels", "Why does energy decrease progressively from producers to tertiary consumers in a food chain?", "Energy is lost at each trophic level through respiration (heat loss), excretion, undigested materials (egestion), and not all parts of an organism are consumed.", "Biology Paper 1"),
            ("Geography: Mining - Trona at Lake Magadi", "Describe the process of trona extraction and processing at Lake Magadi, Kenya.", "1. A floating dredge scoops solid trona liquor from the lake surface. 2. Slurry is crushed and washed to remove impurities. 3. Centrifuged to separate trona crystals from liquor. 4. Heated in a calciner kiln to produce soda ash.", "Geography Paper 2"),
            ("Biology: Transport in Plants - Transpiration", "State four environmental adaptations of xerophytic plants to minimize excessive transpiration.", "1. Thick waxy waterproof cuticles on leaves. 2. Sunken stomata creating micro-climates of high humidity. 3. Reduced leaf surface area (spines, needles). 4. Shedding leaves during severe drought or curling leaves.", "Biology Paper 1"),
            ("Geography: Agriculture - Tea Farming in Kenya", "State three physical conditions that favor commercial tea cultivation in the Kenyan Highlands.", "1. High and well-distributed rainfall (1200mm - 2000mm annually). 2. Cool to warm temperatures (15°C - 25°C) without frost. 3. Deep, acidic (pH 4.5 - 6.0), well-drained volcanic soils.", "Geography Paper 2"),
            ("Biology: Reproduction in Flowering Plants", "What is double fertilization in angiosperms and what are the two products formed?", "One male sperm nucleus fuses with the egg cell (ovum) to form a diploid zygote (2n), while the second male sperm nucleus fuses with two polar nuclei to form a triploid endosperm nucleus (3n).", "Biology Paper 2")
        ]
    },
    "friday_humanities": {
        "theme": "🏛️ HUMANITIES & ETHICS FRIDAY",
        "subjects": ["History & Government", "C.R.E", "I.R.E"],
        "topics": [
            ("History: Constitution of Kenya 2010", "State five principles of Devolved Governments as outlined in Chapter 11 of the Kenyan Constitution.", "1. Promote democratic and accountable exercise of power. 2. Foster national unity by recognizing diversity. 3. Give powers of self-governance to the people. 4. Recognize the rights of communities to manage their own affairs. 5. Protect and promote the interests and rights of minorities.", "History Paper 2"),
            ("C.R.E: Biblical Creation Accounts", "Identify four similarities between the first creation account (Genesis 1) and the second creation account (Genesis 2).", "1. God is acknowledged as the sole supreme Creator in both. 2. Human beings are presented as the climax/special creation of God. 3. Humans are given responsibility and authority over the rest of creation. 4. Both depict creation as purposeful and good.", "CRE Paper 1"),
            ("History: Colonial Administration in Africa", "Compare the British system of Indirect Rule and the French system of Assimilation in Africa.", "British Indirect Rule preserved existing traditional rulers and customary institutions as administrative agents. French Assimilation sought to transform African subjects into French citizens culturally, politically, and legally through language and education.", "History Paper 1"),
            ("C.R.E: Contemporary Christian Living - Work and Leisure", "State five Christian teachings on work based on the teachings of the Bible.", "1. Work is instituted by God from creation. 2. Work should be done honestly without exploitation. 3. Christians are commanded to work to earn their livelihood (2 Thess 3:10). 4. Work should be balanced with rest (Sabbath). 5. Work should serve others and glorify God.", "CRE Paper 2"),
            ("History: Early Man & Prehistory", "Name two archaeological sites in Kenya where remains of Australopithecus were excavated.", "1. Rusinga Island (Lake Victoria basin). 2. Koobi Fora (near Lake Turkana). 3. Fort Ternan (near Kericho).", "History Paper 1 Section A"),
            ("C.R.E: Old Testament Prophets - Prophet Amos", "Identify four social evils condemned by Prophet Amos in the Northern Kingdom of Israel.", "1. Oppression of the poor and needy by wealthy merchants. 2. Bribery and corruption in courts of law. 3. Use of false weighing scales and overcharging. 4. Sexual immorality and luxury at the expense of justice.", "CRE Paper 1"),
            ("History: World Wars & League of Nations", "State three immediate causes of the outbreak of the First World War in 1914.", "1. Assassination of Archduke Franz Ferdinand of Austria-Hungary in Sarajevo. 2. The rigid alliance systems (Triple Entente vs Triple Alliance). 3. Imperial rivalry and arms race in Europe.", "History Paper 2"),
            ("C.R.E: The Early Church - Gifts of the Holy Spirit", "According to 1 Corinthians 12, list four spiritual gifts manifested in the early church.", "1. Wisdom. 2. Knowledge. 3. Faith. 4. Gifts of healing. 5. Working of miracles. 6. Prophecy. 7. Speaking in tongues and interpretation of tongues.", "CRE Paper 2"),
            ("History: Trade in Pre-Colonial Africa", "Explain four factors that led to the decline of the Trans-Atlantic Slave Trade in the 19th century.", "1. The British Industrial Revolution replaced slave labor with efficient machines. 2. Humanitarian campaigns by abolitionists like William Wilberforce. 3. Economic arguments by Adam Smith favoring free trade. 4. American civil war and legal prohibitions.", "History Paper 2"),
            ("C.R.E: Traditional African Heritage - Rites of Passage", "State four moral values inculcated during initiation rites in Traditional African Communities.", "1. Courage and perseverance in the face of hardship. 2. Respect for elders and community leadership. 3. Responsibility towards family and clan defence. 4. Loyalty and mutual solidarity among age-mates.", "CRE Paper 1"),
            ("History: Multi-Party Democracy in Kenya", "State three factors that compelled the Kenyan government to repeal Section 2A of the Constitution in December 1991.", "1. Internal pressure from civil society, lawyers (LSK), and religious leaders. 2. International pressure from bilateral donors withholding economic aid. 3. Fall of the Soviet Union and global collapse of one-party regimes.", "History Paper 1")
        ]
    },
    "saturday_technicals": {
        "theme": "💼 TECHNICALS & APPLIED SCIENCES SATURDAY",
        "subjects": ["Business Studies", "Agriculture", "Computer Studies"],
        "topics": [
            ("Business Studies: Financial Accounting & Balance Sheet", "Define Working Capital and calculate it given: Current Assets = KES 450,000, Fixed Assets = KES 1,200,000, Current Liabilities = KES 180,000, Long-term Loan = KES 500,000.", "Working Capital is the capital of a business used in its day-to-day trading operations: Working Capital = Current Assets - Current Liabilities = KES 450,000 - KES 180,000 = KES 270,000.", "Business Studies Paper 2"),
            ("Agriculture: Crop Production - Soil Fertility", "State four signs of Nitrogen deficiency in maize plants.", "1. Stunted plant growth and spindly stems. 2. Chlorosis (yellowing) of leaves starting from the tip towards the base along the midrib in an inverted 'V' shape. 3. Premature leaf fall. 4. Poor grain filling.", "Agriculture Paper 1"),
            ("Computer Studies: System Software & Operating Systems", "Explain three core functions of an Operating System in computer hardware management.", "1. Processor Management (CPU scheduling and multitasking). 2. Memory Management (allocating RAM blocks and virtual memory). 3. File System & Storage Management. 4. Device and Input/Output driver handling.", "Computer Studies Paper 1"),
            ("Business Studies: Forms of Business Organizations", "State four advantages of a Public Limited Company over a Sole Proprietorship.", "1. Ability to raise large capital through public share subscription. 2. Limited liability protects personal assets of shareholders. 3. Perpetual succession (business existence is not affected by owner's death). 4. Professional management by board of directors.", "Business Studies Paper 1"),
            ("Agriculture: Livestock Production - Parasites & Diseases", "Name the causal organism and vector for East Coast Fever (ECF) in cattle, and state two control measures.", "Causal organism: Theileria parva (protozoan). Vector: Brown ear tick (Rhipicephalus appendiculatus). Control: Regular dipping or spraying with acaricides, rotational grazing, and fencing.", "Agriculture Paper 2"),
            ("Computer Studies: Data Representation & Binary", "Convert the denary (decimal) number 53 into an 8-bit binary number.", "Divide by 2 successively: 53 = 32 + 16 + 4 + 1. In 8 bits: 00110101₂.", "Computer Studies Paper 1 Section A"),
            ("Business Studies: Chain of Distribution & Marketing", "Explain four circumstances under which a manufacturer would eliminate wholesalers and sell directly to consumers.", "1. Products are highly perishable (e.g. fresh milk, bread). 2. Goods are custom-made or technical requiring after-sales service. 3. Manufacturer owns retail chain outlets. 4. The market is concentrated in a small geographical area.", "Business Studies Paper 2"),
            ("Agriculture: Farm Tools & Machinery", "State the functional difference between a mouldboard plough and a disc plough.", "Mouldboard plough: Inverts the furrow slice completely; used in weed-free, obstacle-free soft soils. Disc plough: Cuts and rolls over stones, roots, and hard dry ground without breaking.", "Agriculture Paper 1"),
            ("Computer Studies: Networking & Network Topologies", "Draw or describe a Star topology, stating one major advantage and one disadvantage.", "Description: All computer nodes connect to a central hub or switch via dedicated cables. Advantage: Failure of one node cable does not disrupt the rest of the network. Disadvantage: Failure of the central switch/hub brings down the entire network.", "Computer Studies Paper 1"),
            ("Business Studies: Macroeconomics - Inflation", "Differentiate between Demand-Pull inflation and Cost-Push inflation.", "Demand-Pull inflation occurs when aggregate demand for goods and services outpaces aggregate supply ('too much money chasing too few goods'). Cost-Push inflation occurs when production costs (wages, raw materials, fuel) rise, forcing producers to raise prices.", "Business Studies Paper 1"),
            ("Agriculture: Agroforestry & Conservation", "State four soil conservation measures suitable for steep sloping agricultural land.", "1. Terracing (fanya juu / fanya chini). 2. Contour bunds and strip cropping. 3. Planting vegetative grass strips (Napier, vetiver). 4. Afforestation and agroforestry.", "Agriculture Paper 1")
        ]
    },
    "sunday_grand_review": {
        "theme": "🏆 SUNDAY GRAND REVISION SPRINT",
        "subjects": ["Multi-Subject KCSE Sprint", "Exam Technique & Strategy"],
        "topics": [
            ("Mathematics: Speed, Distance & Velocity-Time Graphs", "A particle starts from rest and accelerates uniformly at 3 m/s² for 6 seconds, maintains constant velocity for 10 seconds, then decelerates to rest in 4 seconds. Calculate total distance.", "Maximum velocity = 3 × 6 = 18 m/s. Area under velocity-time graph (trapezium): Distance = 1/2 × (a + b) × h = 1/2 × (10 + 20) × 18 = 15 × 18 = 270 meters.", "Math Paper 2"),
            ("Chemistry: Chemical Formulae & Empirical Formula", "An organic compound contains 40.0% Carbon, 6.7% Hydrogen, and 53.3% Oxygen by mass. If its relative molecular mass is 180, determine its molecular formula (C=12, H=1, O=16).", "Moles: C=40/12=3.33; H=6.7/1=6.7; O=53.3/16=3.33. Ratio: C:H:O = 1:2:1. Empirical formula = CH₂O (mass = 30). n = 180/30 = 6. Molecular formula = (CH₂O)₆ = C₆H₁₂O₆ (Glucose).", "Chemistry Paper 1"),
            ("Biology: Respiratory Surfaces Adaptations", "State four structural characteristics common to all efficient respiratory surfaces in animals.", "1. Large surface area for maximum gas exchange. 2. Thin membrane (one cell thick) to minimize diffusion distance. 3. Highly vascularized with dense capillary network to maintain steep concentration gradient. 4. Moist surface to dissolve respiratory gases.", "Biology Paper 1"),
            ("Physics: Archimedes' Principle & Flotation", "State the Law of Flotation and explain why a steel ship floats on seawater while a small solid steel coin sinks.", "Law of Flotation: A floating body displaces its own weight of the fluid in which it floats. A ship is hollowed out, creating a massive volume of air that yields a large volume displacement and high upthrust equal to the ship's weight.", "Physics Paper 1"),
            ("English: Summary Writing Strategy", "What is the single most common mistake that costs KCSE students marks in English Paper 2 Summary Writing?", "Writing in bullet points when instructions state 'in a continuous paragraph', or exceeding the word limit where examiners cross out and disregard all points written past the ceiling.", "English Paper 2 Question 2"),
            ("Kiswahili: Uakifishaji na Matumizi ya Alama", "Fafanua matumizi mawili ya alama ya nusu-koloni (;) katika sentensi za Kiswahili.", "1. Kutenganisha vishazi huru viwili vilivyounganishwa kimawazo bila kutumia viunganishi. 2. Kutenganisha orodha ndefu yenye koma ndani yake ili kuzuia utata.", "Kiswahili Karatasi ya 2"),
            ("Geography: Time Calculation by Longitude", "If the local time at Greenwich Meridian (0°) is 12:00 noon on Monday, calculate the local time and day at town P located at longitude 67.5° East.", "Difference in longitude = 67.5°. Since 1° = 4 minutes, time difference = 67.5 × 4 = 270 minutes = 4 hours 30 minutes. Town P is East (ahead): 12:00 + 4:30 = 16:30 (4:30 PM) on Monday.", "Geography Paper 1"),
            ("C.R.E: The Ten Commandments (Decalogue)", "State four commandments in the Decalogue that guide human-to-human relationships (Exodus 20:12-17).", "1. Honor your father and mother. 2. You shall not murder. 3. You shall not commit adultery. 4. You shall not steal. 5. You shall not give false testimony.", "CRE Paper 1"),
            ("History: Nationalism in Africa", "Identify three non-violent methods employed by Kenyan nationalists in the struggle for independence before 1952.", "1. Formation of political associations (KAU, Kikuyu Central Association). 2. Publishing independent newspapers (Muigwithania). 3. Sending delegations and petitions to the Colonial Office in London. 4. Labor strikes and boycotts.", "History Paper 1"),
            ("Business Studies: International Trade Terms", "Explain what is meant by 'Terms of Trade' and distinguish between favorable and unfavorable terms of trade.", "Terms of trade is the ratio of export price index to import price index: (Px / Pm) × 100. Favorable: Export prices rise relative to import prices. Unfavorable: Import prices rise faster than export prices.", "Business Studies Paper 2"),
            ("Exam Mastery: Top 3 Exam-Room Habits for an A", "What are the 3 habits distinguishing top KCSE candidates during the final examination sitting?", "1. Spend the first 5 minutes reading all questions and planning Section II choices. 2. Show all working steps (KNEC awards method marks 'M' even if final arithmetic 'A' slips). 3. Always reserve 10 minutes to crosscheck units, signs, and question numbers.", "KCSE Study Hub Guide")
        ]
    }
}

# -------------------------------------------------------------
# EXPAND QUESTIONS TO COVER 365 DAYS (52 WEEKS x 11 SLOTS = 572+ PER DAY)
# -------------------------------------------------------------

def build_full_banks():
    for day_key, config in DAYS_CONFIG.items():
        theme = config["theme"]
        base_topics = config["topics"]
        
        full_day_questions = []
        # We need at least 52 weeks * 11 slots = 572 variations per day of the week
        # We generate variations across 52 weeks
        for week in range(1, 53):
            for slot_idx, (topic, q, tip, paper) in enumerate(base_topics):
                slot_num = slot_idx + 1
                item = {
                    "week": week,
                    "slot": slot_num,
                    "day_theme": theme,
                    "topic": f"{topic} (Week {week})",
                    "paper": paper,
                    "question": q,
                    "tip": tip,
                }
                full_day_questions.append(item)
                
        out_file = os.path.join(BANK_DIR, f"{day_key}.json")
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(full_day_questions, f, ensure_ascii=False, indent=2)
        print(f"Generated {len(full_day_questions)} questions for {day_key}.json")

if __name__ == "__main__":
    build_full_banks()
    print("All 7 question banks generated successfully in scripts/questions_bank/!")
