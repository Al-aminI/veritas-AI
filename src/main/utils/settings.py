"""
sample response: [
  {
    "state_action_result": "Hello! Welcome to Veritas University's website! I'm happy to help you navigate through our website and answer any questions you may have. What can I assist you with today? Are you looking for information on our courses, about the university, or something else?",
    "new_state": "new page url"
  }
]

[
  {
    "state_action_result": "Hello! I was developed by the talented team at Flexisaf AI Venguards to assist visitors like you on the Veritas University website. I'm here to help you navigate the site and answer any questions you may have about the university. How can I assist you today?",
    "new_state": "new page url"
  }
]

"""

system_prompt = """You're a helpful developed by Flexisaf AI Venguards Team. 
                    you are placed on veritas university website.
                    your porpose is to assist visitors of veritas university website
                    to navigate through the website, and also answer there questions 
                    regarding the univerity, like courses they offer, about, address, 
                    individuals and other informations found on a university public website.
                    your rtesponses most be concise and friendly.
                    """

session_summarizer_system_prompt = """
        You are an AI assistant tasked with summarizing conversations for session history. 
        Your goal is to capture all critical details and actions discussed, including user 
        inputs, agent responses, and any important information that would be relevant for 
        follow-up interactions. Ensure the summary is clear, concise, and detailed enough 
        to provide context for subsequent agents.
        here is the conversation: """


def format_memory_prompt(user_input):
    memory_agent_system_prompt = f"""

            You are a memory management agent for a university AI system. Your role is to:
            1. Analyze user input and system responses
            2. Identify important information, entities, or facts worth remembering
            3. Decide if the information should be stored in long-term memory
            4. Format the memory for storage
            
            User Input: {user_input}
            
            If there's information to store, respond in the following JSON format:
            {
                "store_memory": "true",
                "memory": {
                    "type": "entity/fact/other",
                    "content": "description of the memory to store"
                }
            }
            
            If there's nothing worth storing, respond with:
            {
                "store_memory": "false"
            }
            Only provide a  RFC8259 compliant JSON response. make sure you generate RFC8259 compliant JSON, do not add any text apart from the json.
            Generate a valid JSON object with the following characteristics:
            1. Use only double quotes (") for all keys and string values.
            2. Escape any special characters within strings, especially double quotes and backslashes.
    """
    return memory_agent_system_prompt


def format_actor_prompt(prompt_data):
    memory_agent_system_prompt = f"""
        You are an advanced AI assistant integrated into a university website. Your role is to provide accurate, helpful, and concise responses to user queries while maintaining context and guiding navigation through the website. Follow these guidelines:

        1. Analyze the user's prompt in the context of the conversation history and current webpage.
        2. Use the provided context to inform your response, ensuring accuracy and relevance.
        3. Generate a clear and concise response that directly addresses the user's query.
        4. Determine if navigation to a different webpage is necessary based on the user's query and available pages. 
        5. Always return the link of the next page from the list of web pages given.
        6. Format your response in the specified JSON structure.

        Remember:
        - Always make sure to return the link of the next page from the list of web pages given.
        - Prioritize accuracy over speculation. If unsure, indicate uncertainty.
        - Keep responses concise while ensuring they fully address the user's query.
        - Maintain a professional and helpful tone appropriate for a university setting.
        - Only suggest navigation to a new page if it's clearly beneficial to answering the query.
        - Always return the link of the next page from the list of web pages given.
        - Do not include the list_of_webpages and conversation_history, some_context, user_prompt and recent_response in your json response.
        
        Your response must be in the following JSON format, don't add None or null words in your response instead use not_given. do not include the list of webpages and conversation_history, some_context, user_prompt and recent_response in your json response.:
        {prompt_data}

        Ensure that "your_response" and "next_webpage_to_navigate_to" are filled based on your analysis. All other fields should remain as provided in the input data.
        do not include the list of webpages and conversation_history, some_context, user_prompt and recent_response in your json response.
        do not add any text apart from the json.
        Generate a valid JSON object with the following characteristics:
        1. Use only double quotes (") for all keys and string values.
        2. Escape any special characters within strings, especially double quotes and backslashes.  
    """
    return memory_agent_system_prompt


list_of_university_website_pages = [
    "https://www.veritas.flexisaf.com/art-and-social-science-education/",
    "https://www.veritas.flexisaf.com/about-us/",
    "https://www.veritas.flexisaf.com/accounting/",
    "https://www.veritas.flexisaf.com/art-and-social-science-education/",
    "https://www.veritas.flexisaf.com/banking-and-finance/",
    "https://www.veritas.flexisaf.com/biochemistry/",
    "https://www.veritas.flexisaf.com/biological-sciences/",
    "https://www.veritas.flexisaf.com/business-administration/",
    "https://www.veritas.flexisaf.com/computer-science/",
    "https://www.veritas.flexisaf.com/contact-us/",
    "https://www.veritas.flexisaf.com/e-notice-board/",
    "https://www.veritas.flexisaf.com/ecclesiastical-philosophy/",
    "https://www.veritas.flexisaf.com/economics/",
    "https://www.veritas.flexisaf.com/educational-foundation/",
    "https://www.veritas.flexisaf.com/electronic-and-computer-engineering/",
    "https://www.veritas.flexisaf.com/engineering/",
    "https://www.veritas.flexisaf.com/english-and-literary-studies/",
    "https://www.veritas.flexisaf.com/entrepreneurship/",
    "https://www.veritas.flexisaf.com/faculties/",
    "https://www.veritas.flexisaf.com/sacred-theology/",
    "https://www.veritas.flexisaf.com/science-education/",
    "https://www.veritas.flexisaf.com/science-education/",
    "https://www.veritas.flexisaf.com/social-science/",
    "https://www.veritas.flexisaf.com/theology/",
    "https://www.veritas.flexisaf.com/tuition-and-fees/",
    "https://www.veritas.flexisaf.com/undergraduate/",
    "https://www.veritas.flexisaf.com/health-sciences/",
    "https://www.veritas.flexisaf.com/history-and-international-relations/",
    "https://www.veritas.flexisaf.com/",
    "https://www.veritas.flexisaf.com/humanities/",
    "https://www.veritas.flexisaf.com/law/",
    "https://www.veritas.flexisaf.com/management-sciences/",
    "https://www.veritas.flexisaf.com/mass-communication/",
    "https://www.veritas.flexisaf.com/medical-laboratory/",
    "https://www.veritas.flexisaf.com/medical-sciences/",
    "https://www.veritas.flexisaf.com/natural-applied-science/",
    "https://www.veritas.flexisaf.com/nursing/",
    "https://www.veritas.flexisaf.com/pharmaceutical-sciences/",
    "https://www.veritas.flexisaf.com/pharmacy/",
    "https://www.veritas.flexisaf.com/philosophy/",
    "https://www.veritas.flexisaf.com/political-science-and-diplomacy/",
    "https://www.veritas.flexisaf.com/public-administration/",
    "https://www.veritas.flexisaf.com/pure-and-applied-chemistry/",
    "https://www.veritas.flexisaf.com/pure-and-applied-physics/",
    "https://www.veritas.flexisaf.com/religious-studies/",
    "https://www.veritas.flexisaf.com/sacred-theology/",
    "https://www.veritas.flexisaf.com/science-education/",
    "https://www.veritas.flexisaf.com/veritas-students/",
    "https://www.veritas.flexisaf.com/veritas-university-journals-journals/",
]


web_text = """
    

Art and Social Science Education 


Overview of the Department/Our Philosophy
 
The philosophy of the Department is to pursue with vigour, the fundamental principles of training conscientious teachers for the secondary levels of the Nigerian educational system. To make the Philosophy functional, the Department strives to bring about the acquisition, development and inculcation of proper value-orientation for the survival of the individuals and society.


B.Ed. Business Education


B. Sc. (Marketing and Advertising)


B.Sc. Education Economics


B.Ed. Social Studies.


On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]

Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/art-and-social-science-education/', 'title': 'Art and Social Science Education – Veritas University', 'language': 'en-US'}
page_content='About US – Veritas University

About US 

VERITAS UNIVERSITY
Veritas University is a private university, located in Abuja. It was founded in March 2002 by the Catholic Church in Nigeria. The Institution received its provisional operation licence in 2007 from the National Universities Commission and commenced admission of students in October 2008, at its take-off campus in Obehie, Abia State, Nigeria.
HISTORY
Veritas University Abuja (VUA), also known as the Catholic University of Nigeria, was founded by the Catholic Bishops Conference of Nigeria through a resolution given at its March 2002 meeting in Abuja. The initiative was born by the collective desire of the attending Bishops’ for a University that would provide high quality tertiary education according to the tradition of the Catholic Church.
The Institution received its provisional operation licence in 2007 from the National Universities Commission and commenced admission of students in October 2008 at its take-off campus in Obehie, Abia State, Nigeria. In 2014, it moved to its permanent site with its campus now located in the Bwari Area council of the Federal Capital Territory, Abuja. Nigeria.
The University emphasizes moral values, self-reliance and the development of the students’ entrepreneurial capabilities for the social and economic benefit of the graduates and the Nigerian society.

OUR MISSION, VISION & FOCUSOUR MISSION


OUR FOCUS


OUR PHILOSOPHY


Vision


Other name:

The Catholic University of Nigeria


Motto:

Seeking the Truth


Type:

Private


Established:

2007; 15 years ago


Founder:

Catholic Church in Nigeria


Vice-Chancellor:

Prof. Ichoku Hyacinth


Address:

Bwari Area Council, FCT-Abuja, Abuja, Nigeria
9.28857708129,
7.41568800158


Campus:

Rural 49 acres (20 ha)


Email:

info@veritas.edu.ng


Website:

veritas.edu.ng
' metadata={'source': 'https://www.veritas.flexisaf.com/about-us/', 'title': 'About US – Veritas University', 'language': 'en-US'}
page_content='Accounting – Veritas University

Accounting 


Overview of the Department/Our Philosophy
The Department of Accounting is an offshoot of the defunct Department of Management Sciences, one of the six foundation departments of Veritas University Abuja (The Catholic University of Nigeria), which took off in the 2008/2009 academic session after the University was established in 2007. From its inception, the defunct Department of Management Sciences offered two undergraduate degree programmes, namely,


B. Sc. (Accounting)


B. Sc. (Marketing and Advertising)


In 2013, these programmes became independent departments.
The academic curricula of the Department is based on the Benchmark and Minimum Academic Standards (BMAS) as stipulated by the National Universities Commission (NUC) and the examination syllabi of the relevant professional bodies, such as the Institute of Chartered Accountants of Nigeria (ICAN), to which many of the undergraduate students aspire to belong.
The undergraduate programme of the Department has come as a private-sector Catholic university initiative to satisfy the needs of Nigerians and non-Nigerians for high quality education in Accounting.
This undergraduate programme leads to the award of Bachelor’s degree in Accounting with the following objectives:

 Producing graduates with strong moral character who are sufficiently trained in the humanities, social sciences, and management disciplines to prepare them for the variety of job opportunities that will be open to them after graduation.
 Preparing the graduates for the tasks that they may be confronted with in life and enable them to bring their training to bear in whatever roles they may be called upon to play in the cause of national development.
 Preparing the graduates to fit into varieties of job opportunities in teaching, research and development, and management positions in both the public and private sectors of the economy.
 Building strong capacity for developing entrepreneurial skills in the graduates for optimal utilization of their talents and professional, vocational, and skills training for self-employment so that they will become creators of jobs, rather than job-seekers.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Success Musa
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Matthias O. Ugwudioha
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Ioraver Nyenger Tsegba
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Uchenna Joseph Uwaleke
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Ngozi Eunice Okoroafor
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

Magnus Nkemjika Ogujiofor
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

AGGREH, Meshack
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

Eruse, Edirin Ufuoma
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

NNEDU, STANLEY CHINONSO
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Angela Chinenye Ibe
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

IZEGBU O. Ikechukwu
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

asd
asd
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through Unified Tertiary Matriculation Examination (UTME) into 100-level of any of the four-year programmes leading to the award of Bachelor of Science (B. Sc.) degree of the Department should possess a minimum of credit level passes in five (5) subjects at the Senior Secondary School Certificate Examinations (SSSCE) or its equivalents (GCE/WASCE/NECO) in not more than two (2) sittings to include English Language, Economics, Mathematics, and any other two subjects. Equivalent five-subject credits obtained in examinations conducted by the National Board for Technical Education (NABTEB) are also accepted.
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Business Management, or Economics;
Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.
Final stage of the Accounting Technician Scheme (ATS) ICAN examination

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/accounting/', 'title': 'Accounting – Veritas University', 'language': 'en-US'}
page_content='Art and Social Science Education – Veritas University

Art and Social Science Education 


Overview of the Department/Our Philosophy
 
The philosophy of the Department is to pursue with vigour, the fundamental principles of training conscientious teachers for the secondary levels of the Nigerian educational system. To make the Philosophy functional, the Department strives to bring about the acquisition, development and inculcation of proper value-orientation for the survival of the individuals and society.


B.Ed. Business Education


B. Sc. (Marketing and Advertising)


B.Sc. Education Economics


B.Ed. Social Studies.


On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/art-and-social-science-education/', 'title': 'Art and Social Science Education – Veritas University', 'language': 'en-US'}
page_content='Banking and Finance – Veritas University

Banking and Finance 


Overview of the Department/Our Philosophy
 
To develop and pursue excellent teaching and research through the provision of world-class facilities and opportunities for education, training and employment, to all those who are able to benefit without discrimination. To enhance human advancement, prosperity and welfare through effective and efficient teaching and research that encourage the application of knowledge, promote discipline, honesty and hard work, and to acquire and manage resources effectively to achieve these objectives.
Graduates of this programme would acquire and be able to apply banking and financial knowledge in the operation and management of banks, financial institutions and other organizations and be professionally qualified to practice the professions. For Competencies and Skills and Behavioural Attitudes as they relate to Attainment Levels, Resource Requirements for Teaching and Learning, refer to Section 1 of the Prospectus
The objectives of the programme include;

 To provide basic knowledge for understanding and analyzing problems relating to the management or administration of industrial, commercial, public and other human organizations, and particularly financial institutions.
 To equip the students with skills needed for recognizing and defining problems and taking appropriate decisions using scientific techniques and tools.
 To inculcate in students an awareness of and sensitivity to environmental factors and conditions and their impact on managerial administrative practice and decisions.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



ESTHER ALIBABA
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

DANIEL OGUCHE
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

BLESSING EJURA SUCCESS
LECTURER 11
Publications: [List publications with links, if available]
VIEW PROFILE

IDIH OGWU EMMANUEL
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

ISRAEL ODION IDEWELE
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
The B. Sc. (Banking and Finance) programme is structured as a four-year full-time course for candidates who possess five credits passes at SSCE/GCE/NECO “O” level or their equivalents in subjects that include Mathematics and English Language and any other three relevant subjects at not more than two sittings. Equivalent five-subject credits obtained in examinations conducted by the National Board for Technical Education (NABTEB) are also accepted. The University requires that candidates make an acceptable pass on the Unified Tertiary Matriculation Examinations (UTME) conducted by Joint Admission and Matriculation Board (JAMB). In addition, the University further screens all candidates for admission into its degree programmes.
Direct Entry

A National Diploma from approved universities or colleges of technology or polytechnics with a grade not lower than merit. In addition, the applicant must possess five credits at SSCE/GCE/NECO “O” level or its equivalent in subjects which include English Language, Mathematics, and Economics.
Two “A” Level passes in Economics, Accounting and additional subsidiary subjects. Candidates are expected to possess five credits at SSCE/GCE/NECO “O” level or their equivalent in subjects which include English Language and Mathematics. Results at “O” level must be attained at not more than two sittings.
HND in relevant discipline with at least lower credit in addition to five credit passes at SSCE/GCE/NECO “O” level or its equivalent in subjects which include English Language and Mathematics.
Final Certificate of relevant Professional Bodies in addition to five credit passes at SSCE/GCE/NECO “O” level or its equivalent in subjects which include English Language and Mathematics.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website

' metadata={'source': 'https://www.veritas.flexisaf.com/banking-and-finance/', 'title': 'Banking and Finance – Veritas University', 'language': 'en-US'}
page_content='Biochemistry – Veritas University

Biochemistry 


Overview of the Department/Our Philosophy
To be recognized as a center for excellence in Biochemistry that provides an atmosphere for acquiring skills in identifying the link between biological/molecular and human resources which can be transformed to enhance the quality of life.
The objectives of the Bachelor of Science, Computer Science programme include:

 To provide proper education in the field of Biochemistry; this will enable students acquire the techniques required by different production sectors of the economy including breweries, pharmaceutical industries, food industries, cosmetic industries, petrochemical industries, agricultural and research institutes.
 To provide a comprehensive training in theory and practice to students ofBiochemistry who having acquired the qualification can work as Graduate Assistant in Universities and other tertiary Institutions, or serve as biochemists in research institutes, industrial establishment or in service laboratories of hospitals.
 To employ in vitro and in vivo approaches in the science of biochemistry which will enable the students remain at the cutting edge of biochemical, biomedical and molecular research.
 To provide basic training in theoretical and practical Biochemistry that give students the necessary eligibility for post graduate studies leading to the award of MSc, MPhil or PhD degree in Biochemistry and related fields.
 To provide the students with necessary theoretical and practical background and tools needed for self-awareness, self-reliance and survival in the world of today
 To provide the students with necessary background that will enable them to discover new and relevant techniques in Biochemistry and related disciplines.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Veronica Folakemi Salau
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Dennis Amaechi Wesley
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Okwuchi Flora Ugoanyanwu
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Ini P. Ekpe
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Yisa Benjamin Nma
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Uchenna Blessing Alozieuwa
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Bukola Catherine Akin-Osanaiye
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
The course shall last for four years and the UTME entry requirements for the B.Sc. (Hons) degree programme in Biochemistry are five credits at ordinary level SSCE or School Certificate (SC)GCE, NECO/NABTEB which should include credit passes in the following subjects: Physics, Chemistry, Biology, Mathematics, English Language obtained at not more than two sittings.
Direct Entry
Direct candidates shall possess one of the following qualifications:

 Higher School Certificate*
 Interim Joint Matriculation Board (IJMB) Examination*
 Nigeria Certificate in Education (NCE)*
 National Diploma ( ND) Upper Credit in Computer Science or Related field*
 Higher National Diploma (HND) Lower Credit in Computer Science, Mathematics, Chemistry or Physics*

 


Transfer Candidates

**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

Partnerships & Collaborations
We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Internal Journals
Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/biochemistry/', 'title': 'Biochemistry – Veritas University', 'language': 'en-US'}
page_content='Biological Sciences – Veritas University

Biological Sciences 


Overview of the Department/Our Philosophy
Science and Technology has in the past few decades played very vital role in the transformation of some global once rural economies to great economic powers as seen in countries like Singapore, Malaysia, Taiwan, Brazil, China, South Korea, etc. The Department of Biological Sciences seeks therefore to educate and train men and women as the vanguards of a scientific and technological revolution that will make Nigeria one of the top twenty countries in the world come 2020. We are focused and our emphasis is not only on theory but also on practical aspects of Science.
The programme aims to produce graduates who will be useful in the following areas of the country’s needs:

 Hospitals, Agricultural and Forestry Establishments
 Ministries, Oil Companies and Foreign Services
 Research Institutions and Universities

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Eugene Ekpenyong- ene Itam
Chief Technologist
Publications: [List publications with links, if available]
VIEW PROFILE

OKEY-NDECHE, Ngozika Florence
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Ugwu Ozioma Lovelyn
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Precious Chimezie
Technologist II
Publications: [List publications with links, if available]
VIEW PROFILE

OLANIYI-OLUSHOLA THERESA
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

AMACHREE EVANGELINE UKACHI
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

OYEGUE ANTHONIA OSATO
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Ozoude Theresa Obiageli
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Oliver Okoi Enang-Effiom
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Obum-Nnadi Charity Ndidi
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

IBEH, Emmanuela Onyinye
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ADIKWU, Michael Umale
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

OJO, MICHAEL OLAWALE
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:
JAMB / UTME
Passing the Universities Matriculation Examination (UTME) after having obtained the Senior Secondary School Certificate with five credits which must include Biology, Chemistry and Mathematics or GCE ‘O’ Level credits in five subjects with a similar proviso. A credit level in SSCE English Language, or GCE ‘O’ Level English Language will be required and at least a pass in Physics may be mandatory together with credits in five other subjects including the science subjects listed above. Selection of candidates is done by the Joint Admission and Matriculation Board (JAMB).
Direct Entry
Direct candidates shall possess one of the following qualifications:
Admission to the Bachelors programme may be by direct entry to the three year standard programme upon obtaining O Level SSCE or GCE with credits in four subjects including Biology, Chemistry and Mathematics in addition to A/L GCE passes in Zoology (or Biology) and Chemistry. An A Level pass in Chemistry or Mathematics will be an advantage but A Level pass in Biology is mandatory. Candidates are selected by JAMB.

Transfer Candidates
Admissions requirements for Transfer candidates: Transfer fee of 200,000 naira for students who are considered for admission after screening. CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.



Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/biological-sciences/', 'title': 'Biological Sciences – Veritas University', 'language': 'en-US'}
page_content='Business Administration – Veritas University

Business Administration 


Overview of the Department/Our Philosophy
 
To promote academic excellence through committed teaching and research, to make the graduates become confident, innovative, productive and self-reliant and be useful to humanity.
The academic curriculum of the programme of the Department tailored the Benchmark and Minimum Academic Standards (BMAS) stipulated by the National Universities Commission (NUC) and the examination syllabi of the relevant professional bodies, such as the Nigerian Institute of Management – NIM – (Chartered), Chartered Institute of Administration (CIA), National Institute of Marketing of Nigeria – NIMN – Chartered, Advertising Practitioners Council of Nigeria – APCON, Nigerian Institute of Public Relations – NIPR – Chartered, Institute of Leadership Learning in Nigeria,
The undergraduate programmes of the Department have come as a private-sector Catholic University initiative to satisfy the needs of Nigerians and non-Nigerians for high quality education in management and business sciences. Specifically, the department aims to:

 Produce graduates with strong moral character who are sufficiently trained in the humanities, social sciences, and management disciplines to prepare them for the variety of job opportunities that will be open to them after graduation.
 Prepare the graduates for the tasks that they may be confronted with in life and enable them to bring their knowledge to bear in whatever roles they may be called upon to play in the cause of national development.
 Equip the graduates to enable them to fit into varieties of job opportunities in teaching, research and development, and management positions in both the public and private sectors of the economy.
 Expose students to training in professional areas, such as Management, Leadership, Marketing and Advertising, Public Relations, Administration, etc. to enable them pursue their desired career paths.
 Build strong capacity for developing entrepreneurial skills in the graduates for optimal utilization of their talents, professional, vocational, and skills for self-employment so that they will become creators of jobs, rather than job-seekers.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Dennis Amobi Ugwuja
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Oyenuga Michael
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ORIAKU CHRISTIAN CHINENYEM
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Solomon Jeresa
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

AHUNGWA AGNES IEMBER
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Mary Akhaine
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

ROMANUS NDUJI
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

OLADELE, Oyetunde Thomas
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through Unified Tertiary Matriculation Examination (UTME) into 100 level of any of the four-year programmes leading to the award of Bachelor of Science (B. Sc.) degree of the Department should possess a minimum of credit level passes in five (5) subjects at the Senior Secondary School Certificate Examinations (SSSCE) or its equivalents (GCE/WASCE/NECO) in not more than two (2) sittings. Specifically, for: B.Sc. Business Administration: English Language, Economics, Mathematics, and any other two subjects. B.Sc. Marketing and Advertising: English Language, Economics, Mathematics, and any other two subjects. Equivalent five-subject credits obtained in examinations conducted by the National Board for Technical Education (NABTEB) are also accepted. In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:

The Advanced Level GCE passes in at least two subjects specified as follows: Business Management, Accounting or Economics.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Intermediate Certificate of relevant Professional Bodies in addition to five credit passes as in (i) above

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

Partnerships & Collaborations
We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area] 



' metadata={'source': 'https://www.veritas.flexisaf.com/business-administration/', 'title': 'Business Administration – Veritas University', 'language': 'en-US'}
page_content='Computer Science – Veritas University

Computer Science 


Overview of the Department/Our Philosophy
In line with Veritas University’s philosophy the philosophy of the B. Sc programme in Computer Science is to search for the TRUTH scientifically by seeking to understand the computer, a product of man’s inquisitiveness and innovation, the complex processes that determine its working and its applications in science and technology that will enhance the integral and holistic formation of man in order to advance knowledge in the service of God and humanity.


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Enihe Raphael O
Asst LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Emmanuel Mkpojiogu
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

OMOPARIOLA Victor Adebola
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Okike Reuben
Laboratory Technologist II
Publications: [List publications with links, if available]
VIEW PROFILE

Joe Essien
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ABDULLAHI Monday Jubrin
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

IZEGBU O. Ikechukwu
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities
We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available: State-of-the-art laboratories equipped with [list equipment] Access to high-performance computing resources Specialized libraries with extensive collections in relevant fields


Eligibility Criteria
The following candidates are eligible to apply for our undergraduate programs: JAMB / UTME Pass at credit level in five subjects which include English Language, Mathematics, and Physics, and any two of, Agricultural Science, Biology, Chemistry and Economics (or any other Social Science subject) at the Ordinary Level SSCE (NECO, WASCE, and GCE). Direct Entry Possession of one the following qualifications Higher School Certificate* Interim Joint Matriculation Board (IJMB) Examination* Nigeria Certificate in Education (NCE)* National Diploma ( ND) Upper Credit in Computer Science or Related field* Higher National Diploma (HND) Lower Credit in Computer Science, Mathematics, Chemistry or Physics* First degree in a related area from a recognized University Plus Unified Tertiary Matriculation Examination (UTME) requirement *Two “A” Level Passes in Mathematics and Chemistry, or Physics
Transfer Candidates
**Admissions requirements for Transfer candidates:** Transfer fee of 200,000 naira for students who are considered for admission after screening. CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations
We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.


Internal Journals
Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students. For more information about our publications, please visit the department library website
' metadata={'source': 'https://www.veritas.flexisaf.com/computer-science/', 'title': 'Computer Science – Veritas University', 'language': 'en-US'}
page_content='Contact us – Veritas University

Contact us 

We welcome comments and enquiries about any of our activities and services. You can contact us in a number of ways.

Contact Us
   

Check our frequently asked questions to see if we can answer your query. Otherwise, take a look at who to contact below.



General study enquiries (not relating to a specific course or application)


Enquiries or concerns about our students


Request a prospectus


Accommodation information


Alumni enquiries


Media enquiries


Campus security


Jobs at the University


Conference facilities


People at the University


Documents, transcripts and award verification


Support services


General enquiries 



' metadata={'source': 'https://www.veritas.flexisaf.com/contact-us/', 'title': 'Contact us – Veritas University', 'language': 'en-US'}
page_content='E-NOTICE BOARD – Veritas University

E-NOTICE BOARD 

WELCOME TO OUR NOTICE BOARD
Parent Portal has been designed to improve home / University communication and to allow parents to take a more informed view of their ward’s progress in the University.

Here’s a space to stay connected & help us model your ward’s career, moral and spiritual life!

You can understand, monitor and participate in the education of your ward from home and elsewhere!

The statistics relate to your ward’s attendance, assessment, behaviour, timetable & other reports!

Our campus is as warm & vibrant as the sunny region we call home.


Campus Safety & Services
Our Mission
Our mission is to provide a safe and secure environment for our students, visitors, faculty and staff. Our goal is to reduce or eliminate crime and safety hazards on campus. We do this by partnering with you in upholding all university campus rules, regulations and all applicable laws and ordinances. This partnership allows for a safe and secure atmosphere where students and employees are able to pursue their life’s goals.


SAFETY AND SECURITY PATROL


Veritas is a private university. Therefore, all persons on the property should be able to demonstrate legitimate use of our facilities. Those unable to account for their presence on campus will be escorted off campus by Campus Public Safety personnel. Students, staff, and faculty should carry their ID cards always, and when practical, accompany their guests on the property. Campus Public Safety will secure all buildings after business hours and maintain a watch overnight to secure against unauthorized use or access of the buildings. Those working or studying in University offices or classrooms after normal business hours will be asked to identify themselves to ensure legitimate use of VUSC property and facilities. Each Department should construct and maintain a list of student workers or students given access to offices and classrooms after business hours and submit the list to the Campus Public Safety Department. Students not on the list will be asked to leave the building by the Campus Public Safety Officer. It is the responsibility of each Department to maintain the list for accuracy.CRIME REPORTING


SAFETY EQUIPMENT MONITORING


COOPERATION WITH LOCAL POLICE, AS NEEDED


OTHER SAFETY SERVICES


LOST AND FOUND
 



' metadata={'source': 'https://www.veritas.flexisaf.com/e-notice-board/', 'title': 'E-NOTICE BOARD – Veritas University', 'language': 'en-US'}
page_content='Ecclesiastical Philosophy – Veritas University

Ecclesiastical Philosophy 
' metadata={'source': 'https://www.veritas.flexisaf.com/ecclesiastical-philosophy/', 'title': 'Ecclesiastical Philosophy – Veritas University', 'language': 'en-US'}
page_content='Economics – Veritas University

Economics 


Overview of the Department/Our Philosophy
 
The philosophy of the economics programme in Veritas University is to produce graduates equipped with critical skills and abilities to abstract, using simplified models that identify the essence of a problem and reason deductively, marshal evidence, assimilate structures, analyze qualitative and quantitative data and communicate concisely the findings to the Nigerian Authority for better policy making and implementation.
Economics is one of the foundation courses of the College of Management and Social Sciences Studies (MAS) of Veritas University, Abuja. At inception in 2008, it was a programme of study in the Department of Management and Social Sciences. Following the split of the department in the 2013/14 academic session, the programme now domiciles in the Department of Economics.
The objectives of the Bachelor of Science, Economics programme are:

 To inculcate in the students a deep understanding and deep appreciation of the fundamentals and theories in Economics discipline.
 To ensure students with technical analytical tools for research and policy work in public and private sectors.
 To prepare students for rigorous post-graduate and academic pursuits in all areas of economics discipline.
 To ensure competitive positioning in the world of practical survival of the fittest for the graduates of this course,
 Provision of adequate and technical preparation in professional pursuits and careers in other related field as in Accounting, Banking, Finance, Marketing, Management, Planning and Counseling practice in any economy.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



OLUSHOLA OLUWATOSIN SOLOMON
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

OYINLOLA OLANIYI
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

OBANSA SUMAILA ADAVANI JOSEPH
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

IHUOMA, ANTHONY ADIEKPERECHI
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Chris AC-Ogbonna
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

MODESTUS CHIDI NSONWU
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Toluhi Kayode David
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Oguchi Chinweuba Benjamin
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Enitan Grace Wale-Odunaiya
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Samuel David
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Amarachi Doris Aligwara
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Credit passes in WASC, SSCE, NECO, or its nationally recognized equivalents in Economics, Mathematics, and English Language plus any other 2 subjects (in a maximum of two sittings).
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Direct candidates shall possess one of the following qualifications:
Minimum of B grades in Economics, Mathematics, and English in IJMB Examination, or minimum of 3.00 (out of a total of 5 points) in a University or Polytechnic diploma in Economics, Business Administration, or any other related field, obtained for a recognized institution.
Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/economics/', 'title': 'Economics – Veritas University', 'language': 'en-US'}
page_content='Educational Foundation – Veritas University

Educational Foundation 


Overview of the Department/Our Philosophy
 
The philosophy of the Department is to pursue the fundamental principles of training conscientious teachers, Educational Managers, Counsellors and Librarians, for the Educational Sector of Nigeria.


B.Ed. Educational Management


B.Ed. Guidance and Counselling


The establishment of post graduate programme of the Department was approved by the University Senate through a resolution passed on 78th meeting of Senate held on Thursday February 1, 2018, to run a Masters Degree in Educational Management programme. The Masters Degree programme in Educational Management took off in 2019/2020 session.
On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers, educational managers, counsellors and Librarians, with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.
 To provide teachers, managers, counsellors and Librarians with the intellectual and professional background, adequate for their alignment and to make them adaptable to any changing situation, not only in the life of their country but in the wide world.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Bakwaph, Peter Kanyip
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Chika Eucharia Eze
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

ANTHONY IGBOKWE AMADI
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Marcella Celestina Amaefule
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

UCHENNA EUCHARIA ENEM
Head of Department, Educational Foundations
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/educational-foundation/', 'title': 'Educational Foundation – Veritas University', 'language': 'en-US'}
page_content='Electronic and Computer Engineering – Veritas University

Electronic and Computer Engineering 


Overview of the Department/Our Philosophy
 
Given that Engineering is an applied science for efficient problem solving through design, modeling, simulation, analysis, and fabrication, which in effect translates to the production of key human products in response to the socio-economic and technological challenges of our time, the Programmes of the Department are designed to improve the quality of life of not only the immediate environment of the University, but also of Nigeria and the world at large.
The objectives of the Bachelor of Engineering, Electronic and Computer Engineering programme are:

 To train Engineers who will immediately upon graduation become problem solvers, designers or product Engineers, participate actively in the engineering process, and translate their knowledge into practical and meaningful products
 To apply the knowledge of mathematics, science and engineering principles for modeling, analyzing and solving problems in the domain of electronics and communication engineering.
 To design and develop practical solutions for real-life problems in the domain of electronics and communication engineering.
 Identify, formulate and analyze real-life problems in the domain of electronics and communication engineering using appropriate tools and standards
 To design and develop sophisticated equipment and experimental systems for conducting detailed investigations to solve multifaceted problems in the domain of electronics, communication and computer engineering
 To maintain lifelong learning process by participating in various professional activities and adapt to rapidly changing technologies.
 To demonstrate knowledge and understanding of project management, finance and apply these projects as individual, team member or leader

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Credit passes in WASC, SSCE, NECO, or its nationally recognized equivalents in Economics, Mathematics, and English Language plus any other 2 subjects (in a maximum of two sittings).
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Direct candidates shall possess one of the following qualifications:
Minimum of B grades in Economics, Mathematics, and English in IJMB Examination, or minimum of 3.00 (out of a total of 5 points) in a University or Polytechnic diploma in Economics, Business Administration, or any other related field, obtained for a recognized institution.
Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/electronic-and-computer-engineering/', 'title': 'Electronic and Computer Engineering – Veritas University', 'language': 'en-US'}
page_content='Engineering – Veritas University

Engineering 
' metadata={'source': 'https://www.veritas.flexisaf.com/engineering/', 'title': 'Engineering – Veritas University', 'language': 'en-US'}
page_content='English and Literary Studies – Veritas University

English and Literary Studies 


Overview of the Department/Our Philosophy
 
The overarching philosophy of the Department of English and Literary Studies is to promote scholarship in the humanistic studies as the foundation of knowledge and the aesthetic appreciation of all humanistic education and values for the holistic (intellectual, emotional and spiritual) development and advancement of humankind.
Specifically, the programme is anchored on the ultimate aim of producing highly literate graduates who will positively affect their environment and sustain socio-cultural, political, economic and moral progress of the Nigerian nation using language, literacy, and literary sensibilities as tools of engagement. The fundamental approach to the dispensation of and dialogue with knowledge in the programme of English and literary Studies is anchored on developing the competencies of learners using out-come based student-centred engagement, and employing the skills of critical thinking and inquiry through teaching, research, and service in order to propel personal and societal growth and development.
History of the Department
The Department of English and Literary Studies was established during the 2013/2014 Academic session. Prior to this time, it was one of the two programmes (English and Literary Studies, and History and International Relations) in the erstwhile Department of Arts and Theological Studies which is now a College. The defunct Department of Arts and Theological Studies was one of the two foundation Departments of the College of Management, Social Sciences, Arts and Theological Studies which took off in the 2008/2009 academic session when the University commenced academic activities. At inception, Dr Abimbola Shittu served as the Pioneer Acting Head of Department of Arts and Theological Studies for two sessions, 2008/2009 and 2009/2010. Dr. Gabriel B. Egbe was the second Acting Head of Department (2010-2012) during whose tenure the Department and the programme of English and Literary Studies earned full accreditation from the National Universities Commission (NUC). Dr Angela N. Dick was appointed Acting Head of Department (2012/2013) academic session. With the establishment of the Department of English and Literary Studies, Dr Gabriel B. Egbe was appointed as the pioneer Acting Head of Department with effect from the 2013/2014 academic session.
 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



GABRIEL BASSEY EGBE
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Arts (B.A.) degree in English and Literary Studies should possess a minimum of:

Five credit passes at the GCE/WAEC/NECO examinations, which must include English Language, Literature-in-English plus three other Arts and/or Social Science subjects
Grade 11 Teachers Certificate (TC11) with credit or merit passes in at least five subjects including English and Literature in English for English and literary Studies programme; and History or Government for History and International Relations programme.
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to the course and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In every case, the University requires that the candidate make an acceptable pass on the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admissions and Matriculation Board (JAMB). In addition, the University further screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level degree programme should possess, in addition to the minimum of five credit passes at the GCE/WAEC/NECO examinations any of the following:

Advanced Level GCE in two relevant subjects including Literature-in-English.
Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects excluding Education
National Diploma (ND) Upper Credit in subjects applied for or related field
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university

Results at ‘O’ level and ‘A’ level must be attained at not more than two sittings.
Candidates with two equivalent subjects at the Nigeria Certificate of Education (NCE) or a National Diploma (ND) certificate from an approved university, college of technology, or polytechnic with the minimum grade of MERIT may be accepted if they have satisfied all University Matriculation requirements.


Transfer Candidates

**Admissions requirements for Transfer candidates:**



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/english-and-literary-studies/', 'title': 'English and Literary Studies – Veritas University', 'language': 'en-US'}
page_content='Entrepreneurship – Veritas University

Entrepreneurship 


Overview of the Department/Our Philosophy
 
The Programme in Entrepreneurship was established as part of the second phase development strategy of the University which is among others, consolidation of existing programmes and creation of new ones in line with national needs. The Programme was therefore established to award a B.Sc. degree in Entrepreneurship as one of the programmes in the Department of Business Administration in the College of Management Sciences as approved by the University Senate through a resolution passed at the 32nd Meeting of the Senate of Veritas University, Abuja held on January 31, 2013. The department of Entrepreneurial Studies became a full-fledged department as approved by the University Senate through a resolution passed at the 59th Meeting of the Senate of Veritas University, Abuja held on31st March, 2016. In the new structure, the Department houses one undergraduate degree programme and a Centre:


B.Sc. Entrepreneurship


Entrepreneurship Development Centre


The academic curricula of the three programmes of the Department tailored the Benchmark and Minimum Academic Standards (BMAS) stipulated by the National Universities Commission (NUC) and the examination syllabi of the relevant professional bodies, and Institute of Entrepreneurs to which many of the undergraduate students aspire to belong.
The major objectives of the degree programme in entrepreneurship are as follows:

 To develop a group of competent professionals in the field of entrepreneurship who will be responsible for transforming the mindset of Nigerian youths towards enterprise and innovation.
 To increase the achievement motivation in our youths through the psychological empowerment obtainable from entrepreneurship training.
 To equip Nigerian youths with skills and competencies in venture opportunity identification, feasibility assessment, business plan development, venture creation and new venture management.
 To instill in our youths the capacity for independent thought, economic freedom and creativity.
 To imbibe in our younger generations a greater magnitude of the urge to achieve, excel and compete, through honest and meaningful ventures that add value to national and societal well-being.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



MARCUS GARVEY ORJI
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Bolaji Akeem JIMOH
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

KATE OBIANUJU CHIMA
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Babatunde Kizito Olaniyi
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Anyaegbunam Chinelo Caroline Esq.
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Chika E. Duru
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Anaeto-Ubah Uchechukwu Lydia
Experimental Officer 1
Publications: [List publications with links, if available]
VIEW PROFILE

Rebecca Remy Andem
Administrative Officer II
Publications: [List publications with links, if available]
VIEW PROFILE

CYRIL, OKECHUKWU FERDINAND
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Ige Grace Okwudilichi
Secretary II & Production Officer
Publications: [List publications with links, if available]
VIEW PROFILE

Kenneth Chukwujioke Agbim
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through Unified Tertiary Matriculation Examination (UTME) into 100-level of any of the four-year programmes leading to the award of Bachelor of Science (B. Sc.) degree of the Department should possess a minimum of credit level passes in five (5) subjects at the Senior Secondary School Certificate Examinations (SSSCE) or its equivalents (GCE/WASCE/NECO) in not more than two (2) sittings to include English Language, Economics or commerce, Mathematics, and any other two subjects. Equivalent five-subject credits obtained in examinations conducted by the National Board for Technical Education (NABTEB) are also accepted.
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:

The Advanced Level GCE passes in at least two subjects specified as follows: Entrepreneurship, Business Management, Accounting or Economics.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Intermediate Certificate of relevant Professional Bodies in addition to five credit passes as in (i) above Admission Requirement for a two-year Degree Programme
Five credit passes at the GCE/SSC/NECO or equivalent examinations.
Higher National Diploma in Entrepreneurship, Business Management, Administration, Accounting, Marketing, or any relevant field of a recognized polytechnic or college of technology.
National Certificate in Education –NCE – (Entrepreneurship Education option).

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Candidates wishing to transfer from another university into any of the Department’s academic programmes must obtain and fill the Inter-University Transfer form, from the University’s Academic Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme he or she has chosen. All inter-university transfer candidates will normally be admitted into 200 level of the receiving programme, and not to a higher level.

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/entrepreneurship/', 'title': 'Entrepreneurship – Veritas University', 'language': 'en-US'}
page_content='Faculties – Veritas University

Faculties 


Veritas University Abuja offers a diverse range of faculties catering to different academic interests and career paths. These faculties include Humanities, Social Sciences, Management Sciences, Natural Sciences, Law, Education, Engineering, and so on… Each faculty provides specialized education and training in its respective field, preparing students for various professions and equipping them with the knowledge and skills needed to make meaningful contributions to society.

' metadata={'source': 'https://www.veritas.flexisaf.com/faculties/', 'title': 'Faculties – Veritas University', 'language': 'en-US'}
page_content='Sacred Theology – Veritas University

Sacred Theology 


Overview of the Department/Our Philosophy
 
Theology is an objective study with over 2000 years of intellectual history. Unfortunately, in modern times, Theology ranks very low on the totem pole of academic status. At Veritas University, we seek to address and counter this trend. Theology goes beyond just knowing the faith. Theology seeks to deepen the student’s understanding and love of God, while helping them appreciate the beauty of his revelation in Jesus Christ and through his Holy Spirit. The program, will help the student experience a dynamic orthodoxy that illuminates God’s eternal truth and remains passionately faithful to Scripture, Tradition, and the Magisterium of the Catholic Church. The Theology Department at VERITAS University boasts an active faculty that is prolific in research and publishing and has a strong commitment to service. As an essential component of the core curriculum, Theology reinforces the Catholic Identity of the University. The discipline of Theology is indispensable for maintaining both the synthesis of knowledge and the dialogue of faith and reason that are the hallmarks of the Catholic Intellectual Tradition. If the University is the place where the Church does its thinking, then the Department of Theology should be the launching pad and the secondary Magisterium of the Local Church. At the end of the day, Theologians must strive be the conscience of the congregation.
Brief History
The Faculty of Theology at Veritas University Abuja, is one of the academic departments in the College of Humanities. The Faculty was established to comply with the wholistic Philosophy of Theological Studies as articulated by the BMAS (Benchmark of Minimum Academic Standards) which states that it shall “…cover all facets of religious phenomena as they affect the history, tradition, economic, social, political and ethics of man (human life).
Aims and Objectives of the Curriculum
The Plan and Programme of studies (curriculum) offered by the Faculty of Theology of Veritas University for the Baccalaureate is intended to profoundly study and systematically explain, according to the scientific method proper to it, Catholic doctrine, derived with the greatest care from divine revelation. It has the further aim of carefully seeking the solution to human problems in the light that same revelation.1 It also aims at solving the current human and environmental complex problems, to search for synthesis of knowledge and to have a dialogue between faith and reason, as well as incarnate the Gospel into cultures, Africa and Nigeria in particular (John 1:14). In fact, as stated in Ex Corde Ecclesiae, this Theology Programme serves all other disciplines in their search for meaning, not only helping them to investigate how their discoveries will affect individuals and society, but by bringing a perspective and an orientation not contained within their own methodologies. By this Faculty interacting with other Faculties and disciplines in Veritas University, and their discoveries enriching theology, offering it a better understanding of the world today, and making theological research more relevant to current needs in Africa and beyond. In order to achieve the above objectives, the Programme of studies, in the three Cycles, booklet in accordance with the documents of the Vatican II, Pope Francis’ Apostolic Constitution, Veritatis Gaudium, the 2016 Ratio Fundamentalis, Ex Corde Ecclesiae, Code of Canon Laws (cc.807- 821), the Post-Synodal Apostolic Exhortations, Ecclesia in Africa and Africae Manus, as well the pastoral directives of the Catholic Bishop’s Conference of Nigeria (CBCN). The Faculty of Theology Cycles in Veritas offers three successive Cycles of studies, each one terminating with the conferment of an academic degree: The Baccalaureate (STB), the Licentiate (STL) and the Doctorate (STD).
The Aims and Objectives of the B.S.T. in Theology Programme are as follows: –

 To initiate students into a global theological view of the Christian mystery, covering presentation of all the disciplines along with an introduction into scientific methodology;
 To present systematically in an organic exposition of the whole of the Catholic Doctrine found in Revelation and the living tradition in order to relate it to life situation (Sitz- im- Leben);
 To form men and women who will serve the Church in various ministries and leadership.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Barnabas Ishaku Sama’ila SHABAYANG
Head of Department
Publications: [List publications with links, if available]
VIEW PROFILE

Chibugo Ogechi Lebechi
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

GREGORY EKENE EZEOKEKE
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Michael Ufok Udoekpo
Faculty Dean
Publications: [List publications with links, if available]
VIEW PROFILE

Peter Hassan Kamai
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The minimum requirement for candidates seeking admission into the Bachelor of Sacred Theology degree programme of Veritas University, Abuja are as follows:

JAMB / UTME
The minimum requirement for candidates seeking admission into the B.A. (Theology) degree programme of Veritas University, Abuja are as follows:
Entry requirement
The Faculty of Theology is open to all qualified students, male and female, who can legally give testimony to leading a moral life and to have completed the previous studies appropriate to enrolling in the Faculty. Clerical and religious students shall need the permission of their Ordinary/Superior to join the Faculty. The lay students shall need a letter of recommendation from their Ordinary to join the Faculty.
Entry Requirement for First Cycle

Ordinary level, WASC/GCE with not less than 5 credits including English Language and Mathematics. That is to say, a secondary school (high school) diploma or certificate which would qualify the applicant for admission into a University in Nigeria.
A Cum Laude Baccalaureate in Philosophy or its equivalent
A successful completion of two years of university-level study in philosophy (Propaedeutic Courses), including courses in Logic, Epistemology, Philosophical Psychology (Philosophy of the Human Person, Philosophical Anthropology), Philosophy of Nature, Ethics (Moral Philosophy), Metaphysics, and the History of Philosophy.
A knowledge of the elements of form and syntax of Latin; And a sufficient knowledge of English Language.



 
Direct Entry
The University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
The University reserves the right to screen Direct Entry candidates before admission



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/sacred-theology/', 'title': 'Sacred Theology – Veritas University', 'language': 'en-US'}
page_content='Science Education – Veritas University

Science Education 


Overview of the Department/Our Philosophy
Coming soon
On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers, educational managers, counsellors and Librarians, with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.
 To provide teachers, managers, counsellors and Librarians with the intellectual and professional background, adequate for their alignment and to make them adaptable to any changing situation, not only in the life of their country but in the wide world.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Uzoechi Benneth Colman
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/science-education/', 'title': 'Science Education – Veritas University', 'language': 'en-US'}
page_content='Science Education – Veritas University

Science Education 


Overview of the Department/Our Philosophy
Coming soon
On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers, educational managers, counsellors and Librarians, with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.
 To provide teachers, managers, counsellors and Librarians with the intellectual and professional background, adequate for their alignment and to make them adaptable to any changing situation, not only in the life of their country but in the wide world.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Uzoechi Benneth Colman
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/science-education/', 'title': 'Science Education – Veritas University', 'language': 'en-US'}
page_content='Social Science – Veritas University

Social Science 
' metadata={'source': 'https://www.veritas.flexisaf.com/social-science/', 'title': 'Social Science – Veritas University', 'language': 'en-US'}
page_content='Theology – Veritas University

Theology 


Overview of the Department/Our Philosophy
 
The philosophy of the programme agrees with that of Veritas University, Abuja which exists to promote “the highest standards of teaching, research and community service whilst providing a balanced education for the acquisition of knowledge, practical skills and moral rectitude.” The programme offers a holistic learning and a solid formation of students who will become competent in the areas of scientific research and teaching and acquire the theological formation needed for an enlightened pastoral commitment. The academic and intellectual formation and mentoring in theological education propels, prepares and illumines the students with proper skill to engage in analytical, ontological, creative and revolutionary research. The B. A. programme is carefully designed to orient, challenge and task the student to develop a higher passion for seeking the Truth about God based on deposit of FAITH handed on from Apostolic tradition. By following the spirit, charism and passion that guided the Fathers of the Church, the Scholastics, the Reformation Theologians and the Fathers of the Second Vatican Council; all these are valuable and resource materials that reveal the deep philosophy of theological study. The philosophy of theological studies must seek to produce intellectuals that must create socio-cultural, politico-economic and psycho-spiritual change in human society in the twenty-first (21) century. Theology must lead humanity to “seek the Truth” about God for their final return to God, to attain salvation in God who is trinity – Father, Son and Holy Spirit.
The Aims and Objectives of the B.A. in Theology Programme are as follows: –

 To offer students the knowledge of contemporary theology solidly rooted in the Catholic tradition and open to contributions of other Christian and non-Christian traditions.
 To offer students adequate knowledge of the sources, methods, and the tools needed to continue the study of theology independently.
 To help students deepen their understanding of the content of the Christian faith and to offer prospective non-Christian students sound knowledge of the faith.
 To foster in the students the ability to perceive the relationship among the various areas of theology.
 To prepare students to be able to face challenges that they may encounter in living their faith in contemporary society.
 To help students grow in their Christian faith, strengthen their relationship with God and be able to disseminate the same.
 To equip students with the tenets of the Christian faith as foundation of their moral life.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The minimum requirement for candidates seeking admission into the B.A. (Theology) degree programme of Veritas University, Abuja are as follows:

JAMB / UTME
The minimum requirement for candidates seeking admission into the B.A. (Theology) degree programme of Veritas University, Abuja are as follows:
Advanced Level GCE in two relevant subjects (Results at ‘O’ level and ‘A’ level must be attained at not more than two sittings.

Five (5) Credits passes in relevant subjects including Mathematics and English Language either in SSCE (WAEC/NECO) OR GCE in a maximum of two (2) sittings.
Candidates must have a minimum of 180 score in the Unified Tertiary Matriculation Examination (UTME).
First degree in a related area of from a recognized University.

< h4>Direct EntryAdvanced Level GCE in two relevant subjects (Results at ‘O’ level and ‘A’ level must be attained at not more than two sittings.
First degree in a related area of from a recognized University.
All direct entry students must do all 200 level courses of their programme. They must also take 100 level courses of the programme which they did offer in their previous progamme.


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1: 5 for a four-point grading system or 1: 8 for a five-point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through Inter-University transfer will be considered only the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their in their former institution. Such students must take all 200 courses of their programme.
Furthermore, the University reserves the right to screen Direct Entry candidates before admission



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/theology/', 'title': 'Theology – Veritas University', 'language': 'en-US'}
page_content='Tuition and fees – Veritas University

Tuition and fees Please note that these fees are for the 2023/24 academic session only. Veritas University has not yet released tuition fees for the 2024/25 academic session.

ACCEPTANCE FEE for ALL NEW STUDENTS for all DEGREE PROGRAMS is N100,000
All students science-based students in 300 are to pay SIWES supervision fee of N10,000
All JUPEB Students are to make all their payments into POLARIS BANK ACC No 1771896020



Step-by-Step Guide to making payments on students’ portal: How to Make Payments

Access the Veritas admissions portal by visiting www.admissions.veritas.edu.ng.
If you are a new student, click on the ‘Applicant’ option. For continuing students, click on ‘Students’.
Provide your login credentials to access the portal.
Once logged in, navigate to the dashboard and click on the ‘Generate Remita’ option. This action will open the Remita interface.
In the Remita interface, select the specific payment option you require, that matches your faculty and hostel, from the payment drop-down menu.
After selecting your desired payment option, click on ‘Generate RRR’ to open the RRR interface.
To make an online payment, click on ‘Pay’. This will prompt you to input your card details securely.
Follow the instructions provided and click on ‘Continue’ to complete the payment process.
Alternatively, if you prefer to make the payment at a bank, you can copy the generated RRR number. Present this RRR number to the bank cashier during the payment process. Please inform the cashier that you are making a payment on Remita.

FACULTY OF MEDICINE AND SURGERY
FACULTY OF EDUCATION
MANAGEMENT SCINCES (EXLUDING ACCOUNTING)
MANAGEMENT SCIENCES: ACCOUNTING
FACULTIES OF HUMANITIES & SOC SCIENCES
FACULTY OF NATURAL SCIENCES
FACULTY OF ENGINEERING (INCLUDING SOFTWARE ENGINEERING)
FACULTY OF LAW
FACULTY OF PHARMACY
FACULTY OF HEALTH SCIENCES: NURSING
FACULTY OF HEALTH SCIENCES: MEDICAL LAB SCIENCE
ECCLESSIASTICAL FACULTIES OF PHILOSOPHY AND THEOLOGY
JOINT UNIVERSITIES PRELIMINARY EXAMINATION BOARD ( JUPEB) – NON-SCIENCE
JOINT UNIVERSITIES PRELIMINARY EXAMINATION BOARD ( JUPEB) – SCIENCE


Male (New Accomodation)
Female (New Accomodation)


Tuition Fees
3,500,000.00
3,500,000.00


Accomodation

₦ 300,000


₦ 300,000



Grand Total

₦ 3,800,000.00


₦ 3,800,000.00INSTRUCTION FOR FOREIGN STUDENTS


All foreign students and payments in foreign currencies are as follows:
S/N
FACULTIES
FEES (not including accommodation)


1
Faculties of Education, Humanities, Management, Social Sciences.
$1500


2
Faculties of Natural and Applied Sciences, and Engineering.
$1700


3
Faculties of Law, Pharmacy, Health Sciences of Medical Lab Science.
$2200


4
Ecclesiastical Faculties of Philosophy and Theology.
$650

Apart from tuition, the fees cover the under-listed items that are not charged separately.
Returning Students
New Students


Course Registration
Course Registration


Medical
Medical


Internet access
Internet access


Examinations
Examinations


Sports
Sports


Entrepreneurship
Entrepreneurship


Library Fee
Library Fee


Development Fee
Development Fee


Drug Test
Drug Test


Plagiarism Test
Matriculation Fee



ID Cards

The fees do not cover SRA Fee of N5000 Departmental fee (N3000) and Faculty Fee (N3000). These have to be paid to SRA, the Department and Faculty respectively.



FUNDS TRANSFER INSTRUCTION

VERITAS UNIVERSITY’S DOLLAR ACCOUNT
ACCOUNT NAME: VERITAS UNIVERSITY ABUJA
BANK: GUARANTEE TRUST BANK (GTB)
ACCOUNT NUMBER (USD): 0024642450


DOMICILLIARY ACCOUNT THROUGH CITIBANK NEW YORK
CORRESPONDENT BANK: CITIBANK, NEW YORK
SWIFT CODE: CITIUS33
ABA NO: 021000089
FOR CREDIT OF: GUARANTY TRUST BANK PLC, LAGOS NIGERIA
SWIFT CODE: GTBINGLA
ACCOUNT NUMBER: 36129295
FOR FINAL CREDIT OF :……………………………………( Beneficiary’s Name)
BENEFICIARY’S A/C NO: ………………………………… (With GTB)
ANY OTHER DETAIL: ………………………………………………………………… (E.g. Sender’s Name, Reference e.t.c)


DOMICILLIARY ACCOUNT THROUGH GTBANK LONDON
INTERMIDIARY BANK: HSBC NEW YORK
SWIFT CODE: MRMDUS33
Fed Wire Routing Code: 021001088
ACC WITH BANK: GUARANTY TRUST BANK (UK) LIMITED
SWIFT CODE: GTBIGB2L
ACCOUNT NUMBER: 000169307
BENEFICIARY NAME: GUARANTY TRUST BANK PLC NIGERIA
SWIFT CODE: GTBINGLA
GTB’S ACCT NO: 90110014250330 (With GTBANK London)
FOR FINAL CREDIT OF :……………………………………( Beneficiary’s Name)
BENEFICIARY’S A/C NO: ………………………………… (With GTB)
ANY OTHER DETAIL: ………………………………………………………………… (E.g. Sender’s Name, Reference e.t.c)


DOMICILLIARY ACCOUNT THROUGH CITIBANK LONDON
CORRESPONDENT BANK: CITIBANK, LONDON
SWIFT CODE: CITIGB2L
SORT CODE: 185008
FOR CREDIT OF: GUARANTY TRUST BANK PLC, LAGOS NIGERIA
SWIFT CODE: GTBINGLA
ACCOUNT NUMBER: 8315795
IBAN NUMBER: GB72 CITI 1850 0808 3157 95
FOR FINAL CREDIT OF :……………………………………( Beneficiary’s Name)
BENEFICIARY’S A/C NO: ………………………………… (With GTB)
ANY OTHER DETAIL: ………………………………………………………………… (E.g. Sender’s Name, Reference e.t.c) 



' metadata={'source': 'https://www.veritas.flexisaf.com/tuition-and-fees/', 'title': 'Tuition and fees – Veritas University', 'language': 'en-US'}
page_content='Undergraduate – Veritas University

Undergraduate 



Course and programme finder

UndergraduateTaught master’sPostgraduate research  

A-Z lists:

 Undergraduate courses
 Taught master’s courses
 Postgraduate research areas Undergraduate courses
 Taught master’s courses
 Postgraduate research areasEligibility Criteria
The following candidates are eligible to apply for our undergraduate programs:

Candidates who made Veritas University, Abuja their first or second choice in their current UTME application form and have scored a minimum of:

200 and above (for Nursing and Pharmacy)
220 and above (for Law)
170 and above for every other program in the last UTME


All other candidates interested in studying at Veritas University, even if Veritas University is not their choice in JAMB.
Direct entry and Transfer Candidates wishing to transfer from other Universities to Veritas University, Abuja.

Transfer Candidates
**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Fees & Financial Aid
We understand that financing your education is important. Here’s information on tuition fees and financial aid options available to undergraduate students:

**Tuition fees & payment options:** Find detailed information on tuition fees for different programs and available payment options.
**Scholarships and bursaries:** Explore our scholarship and bursary opportunities to help offset the cost of your education.
**Financial aid application process:** Learn about the financial aid application process and the steps involved in securing financial assistance.

' metadata={'source': 'https://www.veritas.flexisaf.com/undergraduate/', 'title': 'Undergraduate – Veritas University', 'language': 'en-US'}
page_content='Health Sciences – Veritas University

Health Sciences 
' metadata={'source': 'https://www.veritas.flexisaf.com/health-sciences/', 'title': 'Health Sciences – Veritas University', 'language': 'en-US'}
page_content='History and International Relations – Veritas University

History and International Relations 


Overview of the Department/Our Philosophy
 
The B.A (Hons) History and International relations programme reflects the belief that a proper understanding of history, apart from being indispensable to an educated individual, should embrace some perspectives from related disciplines in the humanities hence its combination with the field of International Relations. The programme also embraces other aspects of humanities, Social Sciences and the natural sciences. In tune with the philosophy of VUNA which is a faith-based institution, the department, in addition to emphasising the history and teachings of the church emphasises and adopt the multidisciplinary approach to the study of development of human society over time.
To achieve this therefore, students are exposed to the major areas of human development and international relations as well as social teachings and history of the church in their first and second year of the programme. In their third and fourth year, students are carefully exposed to much more specialised areas of history and international relations to guide them in making their choices of specialisation. In their final (fourth) year, students are encouraged to undertake small scale research in form of a long essay (project work). In addition, a number of specialised courses are offered in order allow them have a feel of contemporary issues in international arena and historical issues.
The objectives of the Bachelor of Arts, History and International Relations programme are:

 To give the students a thorough understanding of the history of Nigeria, Africa and contemporary issues in international relations.
 Help students acquire the skills to critically and rigorously analyse local and global historical movements that have shaped and continue to shape the lives of ordinary people in Nigeria Africa and the world over.
 Help students develop the analytical faculty to and balanced judgement in readiness for research, administrative and managerial responsibilities
 Help Students develop the awareness on how the realities of our contemporary world necessitate comparative study of other major areas of Europe and Asia and the new insights into the main political, social and economic forces that have shaped specific historical events and also how these historical events and other factors have enhanced or impeded world historical development.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Ombugadu Victor Attah
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Chinyere S. Ecoma
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Nwaneri M. Martinluther
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

BAZZA, Michael Boni
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Moses Tivlumun Korinya
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Boyi Solomon Sylvester
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

NJOKU Onwuka Ndukwe
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Adole John Owoicho
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Thadeus Blessing Iveren
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Felix Idongesit Oyosoro
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through Unified Tertiary Matriculation Examination (UTME) into 100-level of any of the four-year programmes leading to the award of Bachelor of Arts (B.A.) degrees of the Department should possess a minimum of:

Five credit passes at the GCE/WAEC/NECO examinations, which must include English Language, Geography, History or Government, and any other two subjects.
Grade 11 Teachers Certificate (TC11) with credit or merit passes in at least five subjects including; History or Government.
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to the course and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In every case, the University requires that the candidate make an acceptable pass on the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). In addition, the University further screens all candidates for admission into its degree programmes.
Direct Entry
Direct candidates shall possess one of the following qualifications:
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:

Advanced Level GCE in History or Government.
Nigeria Certificate in Education (NCE) in relevant subjects excluding Education
Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Candidates wishing to transfer from another university into any of the academic programmes of the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme he or she has chosen. All inter-university transfer candidates will normally be admitted into 200 (or lower) level of the receiving programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/history-and-international-relations/', 'title': 'History and International Relations – Veritas University', 'language': 'en-US'}
page_content='Veritas University
STUDENTS EXPERIENCE 



 The activities at Veritas University go beyond academics to include moral, psychological, and emotional experiences that mold our students into ideal professionals, that are perfectly prepared to change their world.  


Beware of Fraudsters 



1. We do NOT offer admissions through third parties.2. We do NOT accept payments through third parties.3. Do not interact with phone numbers that are NOT explicitly displayed on our Website; www.veritas.edu.ng.For admission related inquiries, please contact;Rev. Fr. Dr. Peter Bakwaph: 08039398830 (Chairman Admission Committee)Mr. Ilya Cephas: 07086858143Dr. Adidi Dokpesi: 08138605055 

                                        	                                            Read More                                        
 Apply > 
Undergraduate > 
Postgraduate > 
Short/Professional Courses > About Veritas > 
University Management > 
E-Notice Board > 
University Chplaincy > About Veritas University Abuja (VUA) 



A University built on moral, cultured & social standardsWe are a dynamic community of staff and students with Christian orientation and inspiration, who are motivated by the ideals of hard work, integrity, discipline, and creativity, and dedicated to Catholic principles, beliefs, and attitudes. We are working toward creating knowledgeable and skilled graduates who will fit in around the globe for the advancement of their environment and the Nigerian society. 

Read More  


 							Campus Tour						


 							Apply Admission						
 							FAQs- Frequently Asked Questions						

  



' metadata={'source': 'https://www.veritas.flexisaf.com/', 'title': 'Veritas University', 'language': 'en-US'}
page_content='Humanities – Veritas University

Humanities 
' metadata={'source': 'https://www.veritas.flexisaf.com/humanities/', 'title': 'Humanities – Veritas University', 'language': 'en-US'}
page_content='LAW – Veritas University

LAW 


Overview of the Department/Our Philosophy
Update Coming Soon


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria
Update coming soon
Transfer Candidates
Update coming soon


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/law/', 'title': 'LAW – Veritas University', 'language': 'en-US'}
page_content='Management Sciences – Veritas University

Management Sciences 
' metadata={'source': 'https://www.veritas.flexisaf.com/management-sciences/', 'title': 'Management Sciences – Veritas University', 'language': 'en-US'}
page_content='Mass Communication – Veritas University

Mass Communication 


Overview of the Department/Our Philosophy
 
The mass communication programme is primarily predicated on the provision of quality education in the areas of Radio, Television, Film and Newspaper and magazine content production and management, as well as advertising and public relations. Other emerging areas of communication are also considered. Aside from this, it will employ knowledge drawn from various segments of society into the proper foregrounding of related issues. In this regard, the sociology of the media and its intricate relationship to societal development would be very pivotal to the study of this discipline. The essential thread for appreciating this relationship is in the offerings that are provided by the various media.
Therefore, a concerted effort would be made to ensure that from training quality expected of our products (students), their output would be commensurate to industry standards in Nigeria and indeed elsewhere.
The objectives of the Bachelor of Science, Mass Communication programme are:

 To produce high quality graduates in mass communication to serve our society.
 To produce adequate manpower in the area of Radio and Television, Film, Public Relation, Advertising, Newspaper and Magazines, as well as other related areas of communication.
 To inculcate into its graduates, the ethics of the profession respect for truth and fairness doctrine.
 To enhance communication for development in the state and at the national level.
 To promote cooperation and understanding in the society.
 To ensure sound training in practice theory and research.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



John Sambe
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

TSEBEE ASOR KENNETH
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

KUSUGH TERNENGE
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Isaac Imo-Ter Nyam
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Okoh Samuel Ejime
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

EZE EMMANUEL OBUMNEME
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Member Solace Gbakighir
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ADAKOLE ONYEBI
Studio Demonstrator (Television)
Publications: [List publications with links, if available]
VIEW PROFILE

IWAMBE, SANDRA
Studio Demonstrator
Publications: [List publications with links, if available]
VIEW PROFILE

Onwunjiogu Valentine
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

NKECHI UWAKWE-ABUGU
SENIOR ASSISTANT REGISTRAR
Publications: [List publications with links, if available]
VIEW PROFILE

JAMES MUAZA SHEDRACK
ADMINISTRATIVE OFFICER II
Publications: [List publications with links, if available]
VIEW PROFILE

OBIEM A. SAMSON
Chief Clerical Officer
Publications: [List publications with links, if available]
VIEW PROFILE

Sunday E. Orbih
Photo Technologist
Publications: [List publications with links, if available]
VIEW PROFILE

AUGUSTINA NWAMAKA SORONNADI
PRINCIPAL EXECUTIVE OFFICER
Publications: [List publications with links, if available]
VIEW PROFILE

ASOLUKA CHRISTIAN ONYEWUCHI
AUDIO/VISUAL TECHNICIAN
Publications: [List publications with links, if available]
VIEW PROFILE

ROY EDACHE
MEDIA OPERATION MANAGER
Publications: [List publications with links, if available]
VIEW PROFILE

Usaku Robinson Wammanda
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

OLEH CYRIL ONYEMAECHI
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
A good UTME result; five (5) Ordinary Level credits including English Language and Mathematics, of not more than two sittings [Combined or separate; WASSEC, NECO, NABTECH, GCE, or any other legitimate equivalent]
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
JAMB Direct Entry application form along with a good IJMB examination result; five (5) Ordinary Level credits including English Language and Mathematics, of not more than two sittings [Combined or separate; WASSEC, NECO, NABTE, GCE, or any other legitimate equivalent]


Transfer Candidates

Transfer Candidates
**Admissions requirements for Transfer candidates:**
A good UTME result; JAMB Change of Institution/Course Form/Application; five (5) Ordinary Level credits including English Language and Mathematics, of not more than two sittings [Combined or separate; WASSEC, NECO, NABTECH, GCE, or any other legitimate equivalent]; university transcripts



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/mass-communication/', 'title': 'Mass Communication – Veritas University', 'language': 'en-US'}
page_content='Medical Laboratory – Veritas University

Medical Laboratory 


Overview of the Department/Our Philosophy
Update Coming Soon


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria
Update Coming Soon
Transfer Candidates
Update Coming Soon


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/medical-laboratory/', 'title': 'Medical Laboratory – Veritas University', 'language': 'en-US'}
page_content='Medical Sciences – Veritas University

Medical Sciences 
' metadata={'source': 'https://www.veritas.flexisaf.com/medical-sciences/', 'title': 'Medical Sciences – Veritas University', 'language': 'en-US'}
page_content='Natural & Applied Science – Veritas University

Natural & Applied Science 

Computer Science

Overview of the Department/Our Philosophy
In line with Veritas University’s philosophy the philosophy of the B. Sc programme in Computer Science is to search for the TRUTH scientifically by seeking to understand the computer, a product of man’s inquisitiveness and innovation, the complex processes that determine its working and its applications in science and technology that will enhance the integral and holistic formation of man in order to advance knowledge in the service of God and humanity.


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Enihe Raphael O
Asst LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Emmanuel Mkpojiogu
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

OMOPARIOLA Victor Adebola
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Okike Reuben
Laboratory Technologist II
Publications: [List publications with links, if available]
VIEW PROFILE

Joe Essien
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ABDULLAHI Monday Jubrin
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

IZEGBU O. Ikechukwu
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities
We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available: State-of-the-art laboratories equipped with [list equipment] Access to high-performance computing resources Specialized libraries with extensive collections in relevant fields


Eligibility Criteria
The following candidates are eligible to apply for our undergraduate programs: JAMB / UTME Pass at credit level in five subjects which include English Language, Mathematics, and Physics, and any two of, Agricultural Science, Biology, Chemistry and Economics (or any other Social Science subject) at the Ordinary Level SSCE (NECO, WASCE, and GCE). Direct Entry Possession of one the following qualifications Higher School Certificate* Interim Joint Matriculation Board (IJMB) Examination* Nigeria Certificate in Education (NCE)* National Diploma ( ND) Upper Credit in Computer Science or Related field* Higher National Diploma (HND) Lower Credit in Computer Science, Mathematics, Chemistry or Physics* First degree in a related area from a recognized University Plus Unified Tertiary Matriculation Examination (UTME) requirement *Two “A” Level Passes in Mathematics and Chemistry, or Physics
Transfer Candidates
**Admissions requirements for Transfer candidates:** Transfer fee of 200,000 naira for students who are considered for admission after screening. CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations
We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.


Internal Journals
Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students. For more information about our publications, please visit the department library website.



Biological Sciences

Overview of the Department/Our Philosophy
Science and Technology has in the past few decades played very vital role in the transformation of some global once rural economies to great economic powers as seen in countries like Singapore, Malaysia, Taiwan, Brazil, China, South Korea, etc. The Department of Biological Sciences seeks therefore to educate and train men and women as the vanguards of a scientific and technological revolution that will make Nigeria one of the top twenty countries in the world come 2020. We are focused and our emphasis is not only on theory but also on practical aspects of Science.
The programme aims to produce graduates who will be useful in the following areas of the country’s needs:

 Hospitals, Agricultural and Forestry Establishments
 Ministries, Oil Companies and Foreign Services
 Research Institutions and Universities

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Eugene Ekpenyong- ene Itam
Chief Technologist
Publications: [List publications with links, if available]
VIEW PROFILE

OKEY-NDECHE, Ngozika Florence
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Ugwu Ozioma Lovelyn
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Precious Chimezie
Technologist II
Publications: [List publications with links, if available]
VIEW PROFILE

OLANIYI-OLUSHOLA THERESA
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

AMACHREE EVANGELINE UKACHI
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

OYEGUE ANTHONIA OSATO
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Ozoude Theresa Obiageli
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Oliver Okoi Enang-Effiom
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Obum-Nnadi Charity Ndidi
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

IBEH, Emmanuela Onyinye
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ADIKWU, Michael Umale
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

OJO, MICHAEL OLAWALE
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:
JAMB / UTME
Passing the Universities Matriculation Examination (UTME) after having obtained the Senior Secondary School Certificate with five credits which must include Biology, Chemistry and Mathematics or GCE ‘O’ Level credits in five subjects with a similar proviso. A credit level in SSCE English Language, or GCE ‘O’ Level English Language will be required and at least a pass in Physics may be mandatory together with credits in five other subjects including the science subjects listed above. Selection of candidates is done by the Joint Admission and Matriculation Board (JAMB).
Direct Entry
Direct candidates shall possess one of the following qualifications:
Admission to the Bachelors programme may be by direct entry to the three year standard programme upon obtaining O Level SSCE or GCE with credits in four subjects including Biology, Chemistry and Mathematics in addition to A/L GCE passes in Zoology (or Biology) and Chemistry. An A Level pass in Chemistry or Mathematics will be an advantage but A Level pass in Biology is mandatory. Candidates are selected by JAMB.

Transfer Candidates
Admissions requirements for Transfer candidates: Transfer fee of 200,000 naira for students who are considered for admission after screening. CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.



Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website. 



' metadata={'source': 'https://www.veritas.flexisaf.com/natural-applied-science/', 'title': 'Natural & Applied Science – Veritas University', 'language': 'en-US'}
page_content='Nursing – Veritas University

Nursing 


Overview of the Department/Our Philosophy
Update Coming Soon


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria
Update Coming Soon
Transfer Candidates
Update Coming Soon


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/nursing/', 'title': 'Nursing – Veritas University', 'language': 'en-US'}
page_content='Pharmaceutical Sciences – Veritas University

Pharmaceutical Sciences 
' metadata={'source': 'https://www.veritas.flexisaf.com/pharmaceutical-sciences/', 'title': 'Pharmaceutical Sciences – Veritas University', 'language': 'en-US'}
page_content='Pharmacy – Veritas University

Pharmacy 


Overview of the Department/Our Philosophy
 
The programme is based on an internationally competitive curriculum. It is, therefore, expected to be able to increase the necessary knowledge that is required for achieving excellence in Pharmacy education and practice. The programme imparts such level of self and professional discipline that is required to mitigate the deplorable drug use (often abuse) situation in the country in both the short and long terms. The well-trained graduates and professionals will possess a wide range of scientific, professional and managerial competencies to best serve the needs of the community with sufficient adaptability in meeting the demands of a changing healthcare delivery system. With the opportunity to apply pharmaceutical and biomedical knowledge to problems of drug therapy in relation to patient care, the graduates of this programme should have broader experience of healthcare and the use of medicines, and be able to practicalise the concept of pharmaceutical care within the healthcare delivery system.
The overall objectives of the Pharm. D. programme are to:

 Provide students with a broad and balanced foundation in all the areas of pharmaceutical science.
 Develop in the students the ability to apply pharmaceutical knowledge in responding to changing environments in the healthcare delivery system.
 Provide students with professional knowledge and skills to identify and resolve drug-related problems.
 Impart to the students a comprehensive knowledge of pathophysiology, therapeutics, pharmacokinetics and toxicology.
 Guide the students in developing skilled understanding of the symptomatology of various disease states with emphasis on monitoring drug therapy.
 Establish and continually expand adequate database from patients, clients and other health professionals.
 Expand the students’ ability to independently use patients’ medication profile to evaluate and assess outcomes of drug therapy.
 Provide students with adequate knowledge base from which they can proceed for further studies in specialized areas of Pharmacy.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

In line with extant rules, all admissions into the Pharm. D. programme of Veritas University Abuja must be through the Joint Admissions and Matriculation Board (JAMB). Candidates seeking admission to the Pharm. D. programme must meet the general minimum admission requirements thus:

JAMB / UTME
Admission through University Tertiary Matriculation Examination (UTME)
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates with A-Level credits in the three science subjects of Chemistry, Physics/Mathematics and Zoology/Botany/Biology, in addition to the UTME admission requirements may be qualified.
Candidates with other qualifications, such as IJMB, JUPEB or similar certificates considered to be equivalent to A-Level may be eligible.
Candidates with a relevant Bachelor’s Degree, in addition to UTME requirements, may be admitted.
Candidates with acceptable Pharmacy Technician Diplomas from institutions accredited by the Pharmacists Council of Nigeria (PCN), in addition to Ordinary Level requirements of credits in Chemistry, Physics, Biology, Mathematics and English Language in the Senior Secondary School Certificate Examination (SSCE) may be considered.
Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

**Admissions requirements for Transfer candidates:**



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/pharmacy/', 'title': 'Pharmacy – Veritas University', 'language': 'en-US'}
page_content='Philosophy – Veritas University

Philosophy 


Overview of the Department/Our Philosophy
Update Coming soon!


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Anweting Kevin Ibok
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria
Update Coming soon!
Transfer Candidates
Update Coming soon!


How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/philosophy/', 'title': 'Philosophy – Veritas University', 'language': 'en-US'}
page_content='Political Science and Diplomacy – Veritas University

Political Science and Diplomacy 


Overview of the Department/Our Philosophy
 
To effectively structure the discipline in anticipation of the needs of the graduates, the government and the society at large; thereby enhance the political, socio-economic and moral development of the country, and scientific research to advance knowledge in the individual student.
Our Programs

B.Sc. Political Science
B.Sc. Peace and Conflict Studies

The study of Political Science and Diplomacy aims at building capacity and competences in contemporary national politics and international relations and practice.
The objectives of the Bachelor of Science, Political Science programme are:

 Graduates understand and are able to apply contemporary administrative and relational skill in managing public and private institutions in Nigeria and elsewhere.
 Graduates acquire capacity to operate successfully as administrators, journalists, and diplomats in multilateral organizations and international firms.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Jooji Innocent
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

ADEJOH SUNDAY
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

PHILIP TERZUNGWE VANDE
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

Okwara Emmanuel Chukwuma
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

Obodo Nneamaka Ijie
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Adagbo Onoja
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

ANYANWU CHRISTIANTUS IZUCHUKWU
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Kussah, Terwase Kimbir
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

Basil A. Ekot
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Samuel Onuh
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Otegwu Isaac Odu
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Onota Emmanuella
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

EBI LAWRENCE ALFRED
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Alfred-Igbokwe Nesochi
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
A minimum standard of five (5) credits at two sittings, including English Language. Candidates must have credit pass in Government or History and a pass in Mathematics. Basic knowledge of French or any other foreign language is an advantage.
In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:

 At least two ‘A’ level passes including Government or History. Candidates are expected to possess five credits at WASSCE/GCE/NECO ‘O’ Level or their equivalent in subjects that include English, Government or History and a Pass in Mathematics. Results at ‘O’ and ‘A’ level must be attained at not more than two sittings.
 A National Diploma certificate from an approved university, polytechnic or school of arts & science with a grade not lower than Merit. In addition, the applicant must possess credit passes at WASSCE/GCE/NECO ‘O’ level, or its equivalent, in five subjects, which must include English, Mathematics, Government or History.
 Any equivalent qualifications approved by the Senate of the University.
 Basic knowledge of French or any other foreign language is an advantage.

 


Transfer Candidates

**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/political-science-and-diplomacy/', 'title': 'Political Science and Diplomacy – Veritas University', 'language': 'en-US'}
page_content='Public Administration – Veritas University

Public Administration 


Overview of the Department/Our Philosophy
 
The philosophy of the programme spans from that of the University which states that all knowledge originates from God and is for the service of humanity, hence should be disseminated to all individuals without hindrance. In line with the above, the Department provides a holistic training which enables students to perform justly, skilfully and professionally in the economy.
The mission of The Veritas University Abuja is to provide students with an integral and holistic formation that combines academic and professional training with physical, moral, spiritual, social and cultural formation in line with the social teachings of the church. Specifically, the mission of the Department is to effectively structure the discipline to professionally equip her students with relevant skills needed to administer government and the society at large, thereby enhancing the political, socio- economic and moral development of the country.
The Department of Public Administration is poised to produce graduates with sound judgment, knowledgeableand with proficiency in the application of both theoretical and practical skills of administration; and to provide the nation with quality and adaptable manpower with dynamic ability to interpret and implement broad policies both in the public sector and other industrial set-ups. Therefore, the traditional role of the programme is to impact on students the knowledge and skills to be self-reliant and resourceful to themselves and Nigeria at large.
The specific objectives the programme are as follows;

 To expose undergraduates to the literary foundations and recent developments in the field of Public Administration and Management so as to prepare them for future managerial positions and higher degree programmes.
 To equip students with modern techniques for the practice of Public Administration and Management.
 To equip undergraduates with analytical skills needed for reorganizing, defining and solving problems as well as training in decision making.
 To equip students with administration/management tools for self-employment;
 To provide a forum for a better appreciation of the developmental problems of the Nigerian State.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Shimawua Dominic
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Moti Ukertor Gabriel
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Katuka Yaki
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Dahida Deewua Philip
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Nwekeaku Charles
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Ihuoma Anthony
SENIOR LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Uche Theophilus Okechukwu
LECTURER I
Publications: [List publications with links, if available]
VIEW PROFILE

Oigbochie Abel Ehizojie
ASSISTANT LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Iorhemen, Peter Iorchir
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Moses Atakpa
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Ayeh Roseline inikpi
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Akwen, Iorkegh Paul
Administrative Officer II
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the UTME must possess 5 credits at Ordinary Level in English Language, Mathematics, Government or History, Economics or Commerce and any other social sciences or art subjects in Senior Secondary Examination Certificate (SSCE) or National Examination Council (NECO), National Business and Technical Education Board (NABTEB) or its equivalent at a maximum of two (2) sittings. Such candidate must satisfy the University cut-off point at the UTME examination.
Direct Entry
Candidates for direct entry must:

Satisfy the above O level requirements
Obtain at least upper credit pass in National Diploma in relevant fields.
National Certificate of Education (NCE) with upper credit passes in relevant fields.
G. C. E. Advance Level Pass in which must include Government or History.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Intra-Departmental and intra-college transfers are permissible only in 100 and 200 levels of study if the student has satisfied the entry requirements of the receiving programme. However, request for intra-Departmental or intra-college transfer should be made through the University Registrar and if approved, effected at the beginning of the academic session.

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/public-administration/', 'title': 'Public Administration – Veritas University', 'language': 'en-US'}
page_content='Pure and Applied Chemistry – Veritas University

Pure and Applied Chemistry 


Overview of the Department/Our Philosophy
 
The philosophy of the Department of Pure and Applied Chemistry falls in line with that of the University: To search for the TRUTH scientifically by studying matter (science of chemistry), in order to provide knowledge for the understanding of the nature of matter and its applicability for the integral and holistic formation of man in order to advance knowledge in the service of God and humanity.
The Industrial Chemistry programme is designed to inculcate disciplined investigative character in the students to understand the science of chemistry in relation to other sciences and technology and its applicability in solving human problems in a non toxic environment. The graduates of industrial chemistry should be well balanced citizens who contribute meaningfully to the industrial, economic and political developments globally, and of their country in particular.
The objectives of the Bachelor of Science, Computer Science programme include:

 To create awareness in students of the vast natural resources endowed to man in our environment for exploitation chemically for man’s development
 To make the students know the nature : structure, composition, properties and uses of these resources and the laws governing their general characteristics.
 To produce skill graduates in industrial chemistry, who can manipulate natural products or create (synthesize) substances in the laboratory as well as in the industrial system.
 To produce skill workers in chemical industries.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



UDOURIOH, GODWIN AUGUSTINE
LECTURER II
Publications: [List publications with links, if available]
VIEW PROFILE

OJINNAKA CHUKWUNONYE MOSES
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Matthews-Amune, Omono Christiana
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Kingsley Igenepo JOHN
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

ONYENZE UGOCHUKWU
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

OGWUDA UCHECHUKWU ANTHONY
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Vitus Eze Agbazue
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

Ogbonnaya Ofor
Professor
Publications: [List publications with links, if available]
VIEW PROFILE

EBIEKPE, VICTOR E.
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Simon Koma Okwute
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria
p>The following candidates are eligible to apply for our undergraduate programs: 

JAMB / UTME
The entry requirements shall be at least credit level passes in five subjects including English Language, Mathematics, Physics and Chemistry to form the core subjects with credit in one other relevant science subject at the Senior Secondary School Certificate or its equivalent. In addition, an acceptable pass in the University Matriculation Examination (UME) into 100-level is required.
Direct Entry
Possession of one the following qualifications
Candidates with two A level passes (graded A-E) at the Advanced Level in one or more relevant subjects (Biology, Botany, Chemistry, Geography, Mathematics and Physics) may undertake the three year degree programme into 200-level.


Transfer Candidates

Transfer Candidates
**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

Partnerships & Collaborations
We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Internal Journals
Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/pure-and-applied-chemistry/', 'title': 'Pure and Applied Chemistry – Veritas University', 'language': 'en-US'}
page_content='Pure and Applied Physics – Veritas University

Pure and Applied Physics 


Overview of the Department/Our Philosophy
 
The philosophy of the Department of Pure and Applied Physics falls in line with that of the University: To search for the TRUTH scientifically by studying matter (science of Physic), in order to provide knowledge for the understanding of the nature of matter and its applicability for the integral and holistic formation of man in order to advance knowledge in the service of God and humanity.
The objectives of the Bachelor of Science, Physics with Electronics programme are:

 To provide students with a broad and balanced foundation of physics knowledge and practical skills.
 To instill in students a sense of enthusiasm for physics, and appreciation of its applications in different contexts.
 To involve the students in intellectually stimulating and satisfying experience of learning and studying.
 To develop in students the ability to apply their knowledge and skills in Physics to the solution of theoretical and practical problems.
 To develop in students through an education in Physics a range of transferable skills of value in physics and other areas.
 To provide students with a knowledge and skills base for further studies in physics or multi-disciplinary areas involving physics.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Dikedi P. N.
Lecturer I
Publications: [List publications with links, if available]
VIEW PROFILE

Uchechukwu Michael Opara
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Anthony Lordson Amana
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Martin Ogharandukun
Acting Head of Department Department of Pure and Applied Physics
Publications: [List publications with links, if available]
VIEW PROFILE

Francis Chidi UWAECHIA
Lecturer II
Publications: [List publications with links, if available]
VIEW PROFILE

Uko Ofe
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Bijimi, Ashia Gertrude
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Patrick Ovie AKUSU
Associate Professor
Publications: [List publications with links, if available]
VIEW PROFILE

ABENGA, Chivirter Raymond
Assistant Lecturer
Publications: [List publications with links, if available]
VIEW PROFILE

Oketa Patrick
Laboratory Technologist
Publications: [List publications with links, if available]
VIEW PROFILE

OGBE Thomas Adakole
Graduate Assistant
Publications: [List publications with links, if available]
VIEW PROFILE

Thomas I. Imalerio
Senior Lecturer
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Passing the Universities Matriculation Examination (UTME) after having obtained the Senior Secondary School Certificate with five credits which must include Biology, Chemistry and Mathematics or GCE ‘O’ Level credits in five subjects with a similar proviso. A credit level in SSCE English Language, or GCE ‘O’ Level English Language will be required and at least a pass in Physics may be mandatory together with credits in five other subjects including the science subjects listed above. Selection of candidates is done by the Joint Admission and Matriculation Board (JAMB).
Direct Entry
Possession of one the following qualifications
Admission to the Bachelors programme may be by direct entry to the three year standard programme upon obtaining O Level SSCE or GCE with credits in four subjects including Biology, Chemistry and Mathematics in addition to A/L GCE passes in Zoology (or Biology) and Chemistry. An A Level pass in Biology or Mathematics will be an advantage but A Level pass in Chemistry is mandatory. Candidates are selected by JAMB.


Transfer Candidates

**Admissions requirements for Transfer candidates:**

Transfer fee of 200,000 naira for students who are considered for admission after screening.
CGPA of 1.5 for other courses except the Health sciences who need 3.5 and above.How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/pure-and-applied-physics/', 'title': 'Pure and Applied Physics – Veritas University', 'language': 'en-US'}
page_content='Religious Studies – Veritas University

Religious Studies 


Overview of the Department/Our Philosophy
 
This program is designed to create a teaching and learning community, to impart appropriate skills, knowledge, behaviour and attitude to promote the pursuit and the advancement of truth; to advance the frontiers of knowledge that are relevant to national and global development; to engender a sense of selfless service in the public and socio-religious sectors in the Nigeria society; and to produce thorough-bred and disciplined students with excellent knowledge and expertise who shall be able to demonstrate competence in any area of endeavour they may choose to go into after graduation from Veritas University.
The vision of the Department is to contribute to an interdisciplinary and develop foster deeper knowledge of the academic study of Religion as a socio-cultural discipline that is pursued objectively and analytically with an aim to x-ray how religion shapes and is in-turn shaped by human cultures, societies and individuals
The objectives of the Bachelor of Arts, Religion and Intercultural Studies programme are:

 To expose the students to understand the general features of Religious Studies as proceeds of the socio-cultural phenomena and stimuli.
To acquaint students with the major contents of the popular religious traditions in Nigeria
 To equip our graduates with the cultural, moral and ethical know-how for launching into other related disciplines and professions such as Law and Morality, Policy Analysis, Critique of Religion, Public Administration, Corruption and Graft Agencies, Social Work, Conflict Resolution, Diplomacy, Human Resources Management, Public Relations, Intercultural and Ethnic Relations in Nigeria, Africa and World
 To enable students acquire critical skills about the implications of religion and culture in human society (Nigeria); especially on how religion and culture affect relationships across sub-ethnic cultures, ethnic communities and peoples

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.
Research Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through Unified Tertiary Matriculation Examination (UTME) into 100-level of any of the four-year programmes leading to the award of Bachelor of Arts (B.A.) degrees of the Department should possess a minimum of:

Five credit passes at the GCE/WAEC/NECO examinations, which must include English Language, Geography, History or Government, and any other two subjects.
Grade 11 Teachers Certificate (TC11) with credit or merit passes in at least five subjects including; History or Government.
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to the course and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In every case, the University requires that the candidate make an acceptable pass on the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). In addition, the University further screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:

Advanced Level GCE in History or Government.
Nigeria Certificate in Education (NCE) in relevant subjects excluding Education
Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Candidates wishing to transfer from another university into any of the academic programmes of the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme he or she has chosen. All inter-university transfer candidates will normally be admitted into 200 (or lower) level of the receiving programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website

' metadata={'source': 'https://www.veritas.flexisaf.com/religious-studies/', 'title': 'Religious Studies – Veritas University', 'language': 'en-US'}
page_content='Sacred Theology – Veritas University

Sacred Theology 


Overview of the Department/Our Philosophy
 
Theology is an objective study with over 2000 years of intellectual history. Unfortunately, in modern times, Theology ranks very low on the totem pole of academic status. At Veritas University, we seek to address and counter this trend. Theology goes beyond just knowing the faith. Theology seeks to deepen the student’s understanding and love of God, while helping them appreciate the beauty of his revelation in Jesus Christ and through his Holy Spirit. The program, will help the student experience a dynamic orthodoxy that illuminates God’s eternal truth and remains passionately faithful to Scripture, Tradition, and the Magisterium of the Catholic Church. The Theology Department at VERITAS University boasts an active faculty that is prolific in research and publishing and has a strong commitment to service. As an essential component of the core curriculum, Theology reinforces the Catholic Identity of the University. The discipline of Theology is indispensable for maintaining both the synthesis of knowledge and the dialogue of faith and reason that are the hallmarks of the Catholic Intellectual Tradition. If the University is the place where the Church does its thinking, then the Department of Theology should be the launching pad and the secondary Magisterium of the Local Church. At the end of the day, Theologians must strive be the conscience of the congregation.
Brief History
The Faculty of Theology at Veritas University Abuja, is one of the academic departments in the College of Humanities. The Faculty was established to comply with the wholistic Philosophy of Theological Studies as articulated by the BMAS (Benchmark of Minimum Academic Standards) which states that it shall “…cover all facets of religious phenomena as they affect the history, tradition, economic, social, political and ethics of man (human life).
Aims and Objectives of the Curriculum
The Plan and Programme of studies (curriculum) offered by the Faculty of Theology of Veritas University for the Baccalaureate is intended to profoundly study and systematically explain, according to the scientific method proper to it, Catholic doctrine, derived with the greatest care from divine revelation. It has the further aim of carefully seeking the solution to human problems in the light that same revelation.1 It also aims at solving the current human and environmental complex problems, to search for synthesis of knowledge and to have a dialogue between faith and reason, as well as incarnate the Gospel into cultures, Africa and Nigeria in particular (John 1:14). In fact, as stated in Ex Corde Ecclesiae, this Theology Programme serves all other disciplines in their search for meaning, not only helping them to investigate how their discoveries will affect individuals and society, but by bringing a perspective and an orientation not contained within their own methodologies. By this Faculty interacting with other Faculties and disciplines in Veritas University, and their discoveries enriching theology, offering it a better understanding of the world today, and making theological research more relevant to current needs in Africa and beyond. In order to achieve the above objectives, the Programme of studies, in the three Cycles, booklet in accordance with the documents of the Vatican II, Pope Francis’ Apostolic Constitution, Veritatis Gaudium, the 2016 Ratio Fundamentalis, Ex Corde Ecclesiae, Code of Canon Laws (cc.807- 821), the Post-Synodal Apostolic Exhortations, Ecclesia in Africa and Africae Manus, as well the pastoral directives of the Catholic Bishop’s Conference of Nigeria (CBCN). The Faculty of Theology Cycles in Veritas offers three successive Cycles of studies, each one terminating with the conferment of an academic degree: The Baccalaureate (STB), the Licentiate (STL) and the Doctorate (STD).
The Aims and Objectives of the B.S.T. in Theology Programme are as follows: –

 To initiate students into a global theological view of the Christian mystery, covering presentation of all the disciplines along with an introduction into scientific methodology;
 To present systematically in an organic exposition of the whole of the Catholic Doctrine found in Revelation and the living tradition in order to relate it to life situation (Sitz- im- Leben);
 To form men and women who will serve the Church in various ministries and leadership.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Barnabas Ishaku Sama’ila SHABAYANG
Head of Department
Publications: [List publications with links, if available]
VIEW PROFILE

Chibugo Ogechi Lebechi
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

GREGORY EKENE EZEOKEKE
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILE

Michael Ufok Udoekpo
Faculty Dean
Publications: [List publications with links, if available]
VIEW PROFILE

Peter Hassan Kamai
LECTURER
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The minimum requirement for candidates seeking admission into the Bachelor of Sacred Theology degree programme of Veritas University, Abuja are as follows:

JAMB / UTME
The minimum requirement for candidates seeking admission into the B.A. (Theology) degree programme of Veritas University, Abuja are as follows:
Entry requirement
The Faculty of Theology is open to all qualified students, male and female, who can legally give testimony to leading a moral life and to have completed the previous studies appropriate to enrolling in the Faculty. Clerical and religious students shall need the permission of their Ordinary/Superior to join the Faculty. The lay students shall need a letter of recommendation from their Ordinary to join the Faculty.
Entry Requirement for First Cycle

Ordinary level, WASC/GCE with not less than 5 credits including English Language and Mathematics. That is to say, a secondary school (high school) diploma or certificate which would qualify the applicant for admission into a University in Nigeria.
A Cum Laude Baccalaureate in Philosophy or its equivalent
A successful completion of two years of university-level study in philosophy (Propaedeutic Courses), including courses in Logic, Epistemology, Philosophical Psychology (Philosophy of the Human Person, Philosophical Anthropology), Philosophy of Nature, Ethics (Moral Philosophy), Metaphysics, and the History of Philosophy.
A knowledge of the elements of form and syntax of Latin; And a sufficient knowledge of English Language.



 
Direct Entry
The University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
The University reserves the right to screen Direct Entry candidates before admission



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/sacred-theology/', 'title': 'Sacred Theology – Veritas University', 'language': 'en-US'}
page_content='Science Education – Veritas University

Science Education 


Overview of the Department/Our Philosophy
Coming soon
On the basis of the above articulation, the Department of Arts and Social Science Education works towards achieving the following objectives:

 To produce prospective teachers, educational managers, counsellors and Librarians, with proper leadership qualities based on Catholic orientation.
 To produce teachers with the knowledge, skills and attitudes which will enable them to contribute to the growth and development of their communities in particular and their nation in general
 To produce teachers who have sound mastery of their subject areas and the ability to impart such knowledge to their students.
 To equip teachers with a mastery of problem solving skills and to enhance the skills of teachers in the use of new technologies.
 To produce highly committed, motivated, conscientious and efficient classroom teachers for our educational system.
 To produce teachers with strong moral values, self-reliance and entrepreneurial capabilities for the social and economic benefit of themselves and the Nigerian society.
 To help teachers to fit into the social life of the community and society at large and enhance their commitment to national objectives.
 To provide teachers, managers, counsellors and Librarians with the intellectual and professional background, adequate for their alignment and to make them adaptable to any changing situation, not only in the life of their country but in the wide world.

 


Staff Profiles
Meet our dedicated team of researchers who are passionate about advancing knowledge in their respective fields.



Uzoechi Benneth Colman
Professor
Publications: [List publications with links, if available]
VIEW PROFILEResearch Facilities

We provide cutting-edge facilities to support our research endeavors. Here are some of the key resources available:

State-of-the-art laboratories equipped with [list equipment]
Access to high-performance computing resources
Specialized libraries with extensive collections in relevant fieldsEligibility Criteria

The following candidates are eligible to apply for our undergraduate programs:

JAMB / UTME
Candidates seeking admission through the Unified Tertiary Matriculation Examination (UTME) into 100-level of the four-year programmes leading to the award of Bachelor of Education (B.Ed.), Bachelor of Arts Education (B.A. Ed.) or Bachelor of Science in Education (B.Sc. Ed.) should possess a minimum of:

Five credit passes in relevant subjects including Mathematics and English Language in the Senior Secondary Certificate Examination SSCE NECO/WAEC.
Grade II Teachers Certificate (TCII) with credit or merit passes in at least five subjects including Mathematics and English Language
National Teaching Certificate (NTC), National Business Certificate (NBC) with credit passes in five subjects relevant to their chosen programme and including Mathematics and English Language; and obtained at not more than two sittings. For NTC/NBC, a credit in any General Education subjects, trade related subjects and trade component subjects is equivalent to a credit in a subject.

In addition, the University requires that the candidate makes an acceptable pass in the Unified Tertiary Matriculation Examinations (UTME) conducted by the Joint Admission and Matriculation Board (JAMB). Furthermore, the University screens all candidates for admission into its degree programmes.
Direct Entry
Candidates seeking Direct Entry admission to the 200-level should possess, in addition to the minimum of five credit passes at the GCE/SSC/NECO examinations, any of the following qualifications:
The Advanced Level GCE passes in at least two subjects specified as follows:

Interim Joint Matriculation Board (IJMB) Examination in relevant subjects.
Nigeria Certificate in Education (NCE) in relevant subjects.
National Diploma (ND) Upper Credit or equivalent in the subject applied for or related field.
Higher National Diploma (HND) Lower Credit in related field.
First degree in a related area from a recognized university.

Furthermore, the University reserves the right to screen Direct Entry candidates before admission


Transfer Candidates

Transfer Candidates
Minimum requirement for transfer into the department is CGPA of 1.0 for a four point grading system or 1.50 for a five point grading system from previous institutions. Candidates wishing to transfer from another university into the Department must obtain and fill the Inter-University Transfer form from the University’s Admissions Office. An application for admission to the University through inter-university transfer will be considered only if the Department is satisfied that the candidate has met the minimum academic requirements for admission to the programme applied for. All inter-university transfer candidates will normally be admitted into 100 or 200 level irrespective of their attainment in their former institution. Such students must take all 200 level courses of their programme.



How to Apply
If you meet the eligibility criteria outlined above, click the button below to **APPLY NOW!**
APPLY NOWVeritas University offers a very flexible application process tailored to meet the needs of different categories of candidates.


Partnerships & Collaborations

We actively collaborate with various institutions and organizations to foster research excellence and broaden our impact.

Collaboration with [Name of institution/organization] on [Project name]
Joint research initiatives with [Name of institution/organization] in the field of [Field name]Internal Journals

Our department publishes high-quality, peer-reviewed journals showcasing the research of faculty and students.

[Journal name] – [Focus area]
[Journal name] – [Focus area]

For more information about our publications, please visit the department library website.

' metadata={'source': 'https://www.veritas.flexisaf.com/science-education/', 'title': 'Science Education – Veritas University', 'language': 'en-US'}
page_content='Veritas students – Veritas University

Veritas students 

Welcome Address by the President of the Student Representative Assembly
Esteemed Faculty Members, Honorable Guests, Fellow Students, It is with great pleasure and honor that I extend a warm welcome to each and every one of you on behalf of the Student Representative Assembly (SRA) at Veritas University, Abuja. As we gather here today, we stand united in our commitment to excellence, growth, and positive change within our esteemed institution. The role of the Student Representative Assembly is not merely administrative; it is a testament to the collective voice and aspirations of the student body. First and foremost, I would like to express my deepest gratitude to all the students who have entrusted me with the responsibility of serving as your President. It is a role that I do not take lightly, and I am fully dedicated to representing your interests, advocating for your needs, and fostering an environment conducive to learning, growth, and development. Our mission at the Student Representative Assembly is clear: to be the voice of the student body, to promote transparency, accountability, and inclusivity, and to work tirelessly to enhance the overall student experience at Veritas University. As we embark on this new academic year, we are faced with both challenges and opportunities. However, I am confident that together, as a united student body, we can overcome any obstacle and achieve greatness. I urge each and every one of you to actively engage with the Student Representative Assembly, to voice your concerns, ideas, and suggestions, and to participate in the various programs, events, and initiatives that we will be organizing throughout the year. Let us embrace diversity, cultivate a culture of mutual respect and understanding, and strive to make a positive impact not only within our university but also in the wider community. In closing, I would like to reaffirm my unwavering commitment to serving you, the students of Veritas University, to the best of my abilities. Together, let us embark on this journey with enthusiasm, determination, and a shared sense of purpose. Thank you, and welcome to Veritas University, where excellence thrives and dreams take flight. Warm regards, President, Student Representative Assembly Veritas University, Abuja
 IMPORTANT SCHEDULESFIRST SEMESTER
Resumption
OCTOBER 24TH 2023
Christmas Break
DECEMBER 16TH 2023
January Resumption
JANUARY 6TH 2024
Examination Starts
FEBRUARY 5TH 2024
First Semester Break
FEBRUARY 24TH 2024


SECOND SEMESTER
Resumption
MARCH 24TH 2023
Easter Break
APRIL 16TH 2023
Resumption
JANUARY 6TH 2024
Examination Starts
FEBRUARY 5TH 2024
Second Semester Break
FEBRUARY 24TH 2024



Matriculation, Convocation and other events may take place outside of these dates; check with this page frequently for updates and More.



Students
All NewsStudent Week
This is a brief description of the card. If the description is too long, it should be truncated with ellipsis.Cultural Competition
This is a brief description of the card. If the description is too long, it should be truncated with ellipsis.Sports Events
This is a brief description of the card. If the description is too
 



' metadata={'source': 'https://www.veritas.flexisaf.com/veritas-students/', 'title': 'Veritas students – Veritas University', 'language': 'en-US'}
page_content='Veritas University Journals JOURNALS – Veritas University

Veritas University Journals JOURNALS 



VUA Journals


Veritas Journal of Humanities
VERITAS JOURNAL OF HUMANITIES (VEJOH) is the journal of the Faculty of Humanities, Veritas University, Abuja, whose philosophy is predicated on the four cardinal pillars of Afroconstructivity, Humanity, Society and Development.
View
VUNA Journal of History and International Relations
VUNA Journal of History and International Relations is a unique addition to the realm of History and International Relations online publishing.
View



' metadata={'source': 'https://www.veritas.flexisaf.com/veritas-university-journals-journals/', 'title': 'Veritas University Journals JOURNALS – Veritas University', 'language': 'en-US'}

"""
