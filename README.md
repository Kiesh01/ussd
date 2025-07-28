**A STUDY OF A TICKETING MECHANISM FOR KENYA AGRICULTURAL LIVESTOCK RESEARCH ORGANIZATION (KARLO) FARMERS.**






AUTHOR:  KIERU GITAU
REG NO: SCT221-0520/2021
SUPERVISOR: Dr. DENNIS KABURU







A proposal/ research project submitted to the Department of Information Technology in the School of Information Technology in partial fulfillment of the requirement for the award of the degree of Information Technology,                            Jomo Kenyatta University of Agriculture and Technology.


2025

DECLARATION

This proposal/research project is my original work and has not been presented for a degree in any other University


......................                                                                     .....................
Signature                                                                           Date


This proposal/research project has been submitted for examination with my approval as University Supervisor


..................                                                                            ...................
Signature                                                                               Date













**ABSTRACT**

When attempting to access government services, farmers frequently experience communication breakdowns, which causes delays and inefficiencies that impede their farming operations. The absence of an efficient platform to communicate with government agencies has made it more difficult for farmers to get timely resources, technical assistance, and agricultural help. By investigating the nexus between agricultural service delivery and technology, this study seeks to address this issue and offers a solution that entails the creation of a centralised ticketing system. 
With the use of this system, farmers will be able to track their requests, make enquiries, and get prompt answers from government officials—improving both service accessibility and general productivity. A requirements assessment of farmers is the first step in the technique, which also include creating a user-friendly system that can be accessed through mobile platforms and testing its operation and efficacy through a pilot program. The anticipated consequence is a notable increase in the effectiveness of farmer-government agency communication, which will lead to improved farming practices, more access to services, and higher agricultural productivity. Data from the initiative will also be used to inform future policy changes.








Contents
DECLARATION	ii
ABSTRACT	iii
CHAPTER ONE:	1
1.0 INTRODUCTION.	1
1.2 PROJECT OVERVIEW.	2
1.3 STATE OF THE PROBLEM.	3
1.4 PROPOSED SOLUTION.	5
1.5 OBJECTIVES.	6
1.6 RESEARCH QUESTIONS.	7
1.7 JUSTIFICATION.	8
1.8	METHODOLOGY.	9
1.9	SCOPE.	11
Appendices	12
A.	Project Resources.	12
B.	Budget	13
C.	Project Duration	14
CHAPTER TWO	15
2.1 INTRODUCTION.	15
2.2 THEORETICAL REVIEW.	16
2.4 CASE STUDY REVIEW.	18
1. eKilimo Platform (Kenya)	18
2. M-Farm (Kenya)	18
3. Digital Green (Global, with Pilots in Kenya)	19
4. Safaricom's DigiFarm (Kenya)	20
2.5 INTERGRATION AND ARCHITECTURE.	21
2.6 SUMMARY.	24
2.7 RESEARCH GAPS.	25
References	26
Cases
KALRO: Kenya Agricultural and Livestock Research Organization	1
USSD: Unstructured Supplementary Service Data	6
SMS: Short Message Service	6
API: Application programming interface	19
IDE: Intergrated Development Environment	19
UI: User Interaction	19
UX: User Experience	19

Figure 1 Communication Gaps	4
Figure 2 Agile Planning	10
Figure 3 Microservice Architecture	19

Table 1 Budget	13
Table 2 Gantt chart	14
Table 3 Communication model	16
Table 4 Microservices Intergration	21




















 

**CHAPTER ONE:**
**1.0 INTRODUCTION**.

Effective communication is crucial for timely access to services, resources, and technical advice between farmers and agricultural support institutions worldwide. Governments in a number of nations have set up platforms to facilitate communication between service providers and farmers by utilising technology. When requesting government services to support their farming operations, Kenyan farmers who are registered with the Kenya Agricultural and Livestock Research Organisation (KALRO) still face substantial communication obstacles. 

In spite of the critical role that KALRO plays in agricultural innovation and research, delays, misunderstandings, and restricted access to resources that farmers require to maximise their farming methods have been caused by the lack of an organised, responsive communication platform. These difficulties are more severe in rural locations where farmers may have less access to the internet, making it more difficult for them to get help from government organisations. The current disjointed and decentralised communication channels are the root of the issue, as they make it challenging for KARLO and government agencies to effectively meet the demands of farmers. As a result, Kenya's agriculture is in dire need of a more efficient and effective communication infrastructure to help it flourish and last.




**1.2 PROJECT OVERVIEW.**

The project focuses on addressing communication challenges faced by farmers registered under the Kenya Agricultural and Livestock Research Organization (KALRO) when seeking services and support from the government. Globally, farmers and government organisations are communicating more easily thanks to the growing use of technology, which makes it possible for them to efficiently access resources, services, and advice related to agriculture. Ticketing methods and digital platforms have been effectively employed in industrialised nations to handle farmer enquiries, guaranteeing prompt responses and efficient service delivery.

 However, a lack of internet connectivity, fragmented communication channels, and unpredictable service response times pose serious challenges for many Kenyan farmers, especially those in remote areas. The goal of this project is to create a centralised ticketing system, a solution based on database administration, task automation, and user-friendly interface design. Through friendly platforms , such a system will enable farmers to submit, track, and manage their service requests, assuring inclusion for those with limited digital access. In order to support the long-term viability of Kenya's agriculture industry, the initiative seeks to increase overall agricultural productivity, improve communication efficiency, and respond promptly.





**1.3 STATE OF THE PROBLEM.**

In the agricultural sector, efficient communication is a critical backbone for service delivery, especially for institutions such as the Kenya Agricultural and Livestock Research Organization (KARLO) that support farmers through microservices like transport, fertilizer distribution, seed distribution, and produce marketing. However, KARLO currently faces a significant communication breakdown across these services, hampering effective coordination, timely service delivery, and ultimately affecting farmers' productivity and incomes.
Research indicates that in Kenya, up to 40% of agricultural produce is lost post-harvest due to delays in transportation and poor market access (Kenya National Bureau of Statistics, 2023). Additionally, fertilizer and seed distribution inefficiencies have led to a 20% drop in expected yields among smallholder farmers annually (FAO Report, 2023). Interviews with KARLO service managers reveal that one major contributing factor to these inefficiencies is fragmented, slow, and unreliable communication between service providers and farmers. Many communications are still reliant on basic SMS alerts, physical notices at service centers, and sporadic in-person visits, which are neither scalable nor sufficient for the demands of modern agriculture.
The communication problem has been further exacerbated by the increasing adoption of smartphones, mobile money, and digital marketplaces among farmers, creating a digital divide between what farmers expect and the outdated methods used by KARLO. While digital solutions are available, KARLO’s current communication systems have not evolved to match these trends, resulting in missed opportunities, farmer dissatisfaction, and overall reduced impact of KARLO’s farmer support initiatives.
The magnitude of this problem is seen in logistical mismatches—farmers receiving late input deliveries, produce rotting before reaching the market, and farmers being unaware of transport schedules or market opportunities. This not only increases operational costs for KARLO but also directly reduces the farmers’ earning potential and trust in the services provided.
 
Figure 1 Communication Gaps
<img width="975" height="754" alt="image" src="https://github.com/user-attachments/assets/64427931-52d1-4cd7-ba5e-b37622718239" />







**1.4 PROPOSED SOLUTION.**

The goal of this project is to create a reliable, centralised ticketing system that is especially made to help farmers who are enrolled under KALRO communicate with government organisations more effectively. The study will investigate cutting-edge communication models and assess the efficacy of ticketing systems put in place in various agricultural contexts across the world, including Brazil and India, where comparable solutions have enhanced agricultural productivity and service delivery. To accommodate farmers in distant locations with limited internet connection, the proposed system will include mobile-based technologies such as SMS, USSD and Web applications going beyond simple digitisation. The system's primary features will allow farmers to submit targeted service requests, monitor the real-time progress of their queries, and get fast replies from the appropriate government agencies. 

To ensure that requests are sent to the right authorities and handled quickly, the system will include clever routing algorithms. This will reduce delays and speed up government response times. Furthermore, the system will make use of data analytics to pinpoint typical problems that farmers encounter, enabling KALRO to decide on resource allocation and policy enhancements with knowledge. In order to ensure sustained and significant results for farmers, the research will concentrate on creating a scalable, user-friendly system that complies with international best practices and caters to the particular requirements of Kenya's agricultural industry.





**1.5 OBJECTIVES.**

General Objective.
1.	To provide a centralised, effective ticketing system that enhances communication between government organisations and farmers who have registered with KALRO, enabling prompt access to agricultural services and assistance.

Specific Objectives.
1.	To investigate and examine regional and international agricultural communication system models in order to determine the most effective approaches and technological advancements that may be applied to Kenya.

2.	To create and implement an intuitive ticketing system that allows farmers to submit, monitor, and get service request responses using SMS and USSD mobile platforms.

3.	To implement the ticketing system, ensuring integration with KALRO and government service workflows, and test its functionality and usability with a pilot group of farmers.

4.	To assess the system's effectiveness using input from farmers and governmental organisations, and to maximise its responsiveness and efficiency using data from actual usage in real time.



**1.6 RESEARCH QUESTIONS.**

1. What are the global and regional best practices in agricultural communication systems, and how can these be adapted to address the specific communication challenges faced by KALRO-registered farmers in Kenya?
2. How can existing ticketing systems be customized to cater to the diverse needs of Kenyan farmers, particularly in terms of accessibility via mobile platforms like USSD and SMS?
3. What are the most critical design considerations for developing an inclusive and user-friendly ticketing system that enhances communication between farmers and government agencies?
4. How can the proposed ticketing system be effectively integrated with existing KARLO and government service workflows to ensure smooth operations and timely response to farmer inquiries?
5. What are the most appropriate methods for testing the functionality, usability, and reliability of the ticketing system during a pilot phase with KALRO-registered farmers?
6. What impact does the use of a centralized ticketing system have on the efficiency of government response times and the overall satisfaction of farmers in accessing agricultural services?
7. How can feedback from farmers and government agencies be used to continuously optimize and improve the performance and responsiveness of the ticketing system over time?


**1.7 JUSTIFICATION.**

The pressing need to remove the communication obstacles preventing KALRO-registered farmers from receiving crucial government services and assistance for their farming operations serves as the rationale for this study. More than 70% of Kenyans rely on agriculture as their primary source of income, making it imperative for farmers to be able to interact with government organisations in an efficient and effective manner in order to boost sustainability and production. Through the creation of a centralised ticketing system that will expedite communication and allow farmers to receive prompt answers to their questions and service requests, this research aims to assist both government agencies and farmers. 

The suggested approach offers a better organised, responsive, and accessible platform that can accommodate farmers with restricted internet connectivity, directly addressing the fragmentation and inefficiencies in the current system. This project will help close the gap between farmers and agricultural services by providing a new technological approach that is specifically tailored to the needs of rural farmers. This will ultimately improve service delivery, enhance agricultural productivity, and support Kenya's larger goal of food security. The rising reliance on technology worldwide to optimise agricultural practices makes this research more relevant, and it offers a timely answer that is in line with Kenya's agriculture sector's digital transition.





**1.8	METHODOLOGY.**

Agile methodology will be used in the planned study and system development to address communication problems that farmers registered under KALRO encounter when corresponding with the government. Through constant feedback from farmers and government stakeholders, the ticketing system will be built gradually thanks to this iterative process, which will also enable system requirements to be refined. The development process will start with a comprehensive needs study that makes use of surveys, interviews, and an examination of current communication techniques. Tools like Sublime as an IDE, Mindview for project tracking, and Microsoft Teams or Slack for communication will be used in the system's construction. Key features including ticket creation, categorisation, and communication channels will be developed with each sprint. User testing and feedback loops will then be conducted. Agile is preferred for projects involving a variety of stakeholders, such as farmers and government officials, because of its adaptability to changing requirements. The research will make sure the system satisfies end users' practical needs by including them in every step of the process. Problem identification will be the first step in the study life cycle. Next comes planning, system design, development, testing, deployment, and iterative improvements based on user input.
                               

 
Figure 2 Agile Planning



<img width="938" height="698" alt="image" src="https://github.com/user-attachments/assets/0306dba0-0897-4bee-a0e3-bc19bdb4d479" />









**1.9	SCOPE.**

The purpose of this project is to solve the communication difficulties that farmers who are registered with the Kenya Agricultural and Livestock Research Organisation (KALRO) encounter when attempting to obtain government services that facilitate their farming operations. The project's geographic scope is restricted to Kenyan farmers, especially those in rural areas who depend on KALRO's services yet encounter difficulties getting support because of ineffective communication routes. A ticketing system, which is the suggested remedy, will enable organised contact between farmers and the government. This study does, however, recognise certain possible drawbacks, including the lack of complete or accurate data regarding farmer demands, the difficulty of accessing dependable technology in rural areas, and resource limitations that might prevent the full deployment of advanced system features. The project will not focus on advanced integrations or long-term system scalability; instead, it will limit itself to the design, development, and initial implementation of a basic ticketing system that enables farmers to submit, track, and get responses to service requests.











Appendices
A.	Project Resources.
The success of the intelligent ticketing system for KALRO farmers will require the following resources:
Human Resources:
Project Manager: Oversees the entire project, ensuring deadlines are met.
Software Developers: Responsible for designing, developing, and testing the ticketing system.
Database Administrator: Manages the database that stores farmer requests and ticket data.
UI/UX Designer: Develops an easy-to-use interface for farmers, considering mobile accessibility.
System Tester: Conducts tests to identify bugs and ensure the system meets user needs.
Field Agents: Assist farmers in adopting the system, provide support and training.
Technical Support Staff: Available to address any technical issues after the system is deployed.
Technological Resources:
Cloud Infrastructure: For hosting the ticketing system, ensuring scalability and data security.
Mobile Integration Platform: To support SMS and mobile app access for farmers with limited internet.
Development Software: Tools such as Git for version control, Jira for project management, and integrated development environments (IDEs) for coding.
API Integration Tools: To connect the ticketing system with existing government services.
Other Resources:
Training Material: Documentation and videos to train farmers and support staff.
Community Outreach: Posters, brochures, and training sessions to introduce the system to KARLO farmers.




B.	Budget

Item	Cost
Human Resources	
Project Manager (6 months)	KShs600,000
Software Developers (2 x 6 months)	KShs2,400,000
Database Administrator (6 months)	KShs5,00000
UI/UX Designer (3 months)	KShs450,000
System Tester (3 months)	KShs350,000
Field Agents (5 agents, 6 months)	KShs1,000,000
Technical Support Staff (6 months)	KShs400,000
Technology and Infrastructure	
Cloud Hosting (6 months)	KShs600,000
SMS/Mobile Integration Costs	KShs4,000,000
Development Software and Tools	KShs300,000
API Integration	KShs250,000
Training and Support	
Training Material (Manuals, Videos)	Kshs150,000
Community Outreach (Posters, Brochures)	KShs200,000
Miscellaneous	KShs250,000
Total Estimated Budget	KShs7,850,000
Table 1 Budget

C.	Project Duration

Project Phase	Duration	Start Date	End Date	Actual Start Date	Actual End Date
Phase 1: Project Planning	2 weeks	Feb 9, 2025	Feb 24, 2025		
Resource Allocation & Team Setup	1 week	Feb 25, 2025	Feb 28, 2025		
Requirements Gathering	1 week	March 3, 2025	March 7, 2025		
Phase 2: System Design	3 weeks	March 10, 2025	March 31, 2025		
UI/UX Design	2 weeks	April 1, 2025	April 14, 2025		
Database and System Architecture	3 weeks	April 15, 2025	April 29, 2025		
Phase 3: Development	8 weeks	April 30, 2025	Aug 4, 2025		
Core Ticketing System Development	5 weeks	Aug 5, 2025	Sep 8 , 2025		
Mobile and SMS Integration	3 weeks	Sep 9, 2025	Sep 30, 2025		
Phase 4: Testing & Refinement	4 weeks	Oct 6, 2025	Nov 3, 2025		
System Testing & Bug Fixes	3 weeks	Nov 4, 2025	Dec 1, 2025		
User Testing and Feedback	1 week	Dec 2, 2025	Dec 9, 2025		
Phase 5: Deployment & Training	4 weeks	Dec 15, 2025	Jan 19 , 2026		
System Deployment	1 week	Jan 10, 2026	Jan 27, 2026		
Farmer Training Sessions	3 weeks	Jan 28, 2026	Feb 25, 2026		
Phase 6: Monitoring & Support	Ongoing (6 months)	March 1, 2026	Sept 1, 2026		
Table 2 Gantt chart

**CHAPTER TWO**
**2.1 INTRODUCTION.**

This chapter reviews existing literature relevant to addressing communication challenges between farmers and government institutions, focusing on the development of a ticketing system for farmers registered under the Kenya Agricultural and Livestock Research Organization (KALRO). For farmers to receive services like subsidies, technical assistance, and market information on time, there must be effective communication between government agencies and farmers. However, many farmers encounter difficulties in navigating these procedures. In order to improve service delivery and streamline communication, industries like customer service, healthcare, and education have been using ticketing systems and other technological solutions more and more in recent years. With a particular emphasis on the function of digital platforms in promoting contacts between farmers and the government. With a particular emphasis on the function of digital platforms in promoting contacts between farmers and the government, this literature review attempts. This literature review aims to explore the current state of communication technology in agricultural settings, focusing on the role of digital platforms in facilitating farmer-government interactions. The goals are to pinpoint areas where current solutions fall short, evaluate whether a ticketing system can fill these gaps, and offer advice that will direct the creation and execution of the suggested system.




**2.2 THEORETICAL REVIEW.**
This project’s theoretical review focuses on key concepts related to communication technology, service delivery systems, and ticketing systems within a microservices architecture framework, aimed at bridging the communication gap between farmers and government institutions such as KALRO. Critical variables in this context include digital communication platforms, ticket management systems, user engagement models, and service response frameworks, all adapted to operate in a modular and distributed microservices environment.
Ticketing systems, commonly used in customer service and IT service management, are engineered to optimize the submission, tracking, and resolution of service requests. When reimagined through a microservices lens, ticketing systems can be broken into independent, specialized services — each responsible for a specific aspect of ticket lifecycle management (e.g., submission, categorization, routing, resolution, and feedback collection). This modular approach aligns well with the needs of agriculture-focused institutions like KALRO, ensuring scalability, flexibility, and resilience in service delivery.
The project will investigate several theoretical communication models relevant to microservices-based systems:
Communication Model	Microservices Interpretation
Centralized Service Systems	A master ticket orchestration service manages all ticket submissions and service routing, ensuring consistent workflows.
Decentralized Peer-to-Peer Communication	Individual microservices (e.g., Transport, Seed Distribution) communicate directly with farmers and with each other through well-defined APIs, minimizing central control.
Automated Response Systems	Microservices integrate AI modules for automated triage, initial responses, and basic problem resolution, especially for frequent or low-complexity enquiries.
Table 3 Communication model
Each approach has foundational assumptions and distinct implications in a microservices context:
•	Centralized orchestration offers strong control, consistency, and policy enforcement but can introduce bottlenecks and reduce system agility.
•	Decentralized service interactions improve responsiveness and scalability but require robust API governance to prevent disorganized service behavior.
•	AI-driven automation boosts efficiency and allows microservices to manage high volumes of standard queries; however, it may lack the nuance necessary for complex, context-specific farmer support cases.
In a microservices-based ticketing and communication system, careful design of service boundaries, clear API contracts, and strong integration layers are necessary to maximize the benefits while minimizing risks of fragmentation or inefficiency. By leveraging microservices theory, the project aims to build a dynamic, resilient, and farmer-centric communication platform capable of adapting to the evolving needs of agricultural service delivery in Kenya.
. 







**2.4 CASE STUDY REVIEW.**
Effective communication systems have been successfully deployed in agricultural sectors globally to address logistics and service delivery issues. In the Kenyan context, particularly within institutions similar to the Kenya Agriculture and Livestock Research Organization (KARLO), there have been notable applications of digital technologies to bridge communication gaps between service providers and farmers.
1. eKilimo Platform (Kenya)
Application:
eKilimo is a mobile and web-based platform that connects farmers to agricultural extension services, markets, and input suppliers. It offers updates on weather, market prices, and agricultural best practices.
Successes:
•	Provided real-time access to critical information, leading to better farming decisions.
•	Increased market access by connecting farmers directly to buyers.
•	Enabled digital record-keeping and farmer profiling.
Misses:
•	Limited penetration in remote areas with low internet access.
•	Language barriers since much of the content was initially in English.
•	Communication was more informational than interactive, lacking real-time service scheduling and feedback loops essential for microservices like transportation logistics
2. M-Farm (Kenya)
Application:
M-Farm is a mobile service that allows farmers to receive real-time market prices, connect to buyers, and find affordable inputs.
Successes:
•	Empowered farmers with bargaining power by providing transparency on market prices.
•	Reduced exploitation by middlemen.
•	Mobile-based communication suited Kenyan rural areas with high mobile phone penetration.
Misses:
•	Limited integration with logistics services like fertilizer or seed distribution.
•	Focused more on produce marketing and not holistic service delivery (transport, input distribution).
•	Not designed specifically for institutional service coordination like KARLO’s internal needs.

3. Digital Green (Global, with Pilots in Kenya)
Application:
Digital Green uses video-based agricultural extension services and community-led communication methods to train farmers and inform them about best practices.
Successes:
•	High farmer engagement due to localized language and context.
•	Scalable model for information dissemination.
•	Built trust within farming communities.
Misses:
•	Lacked a two-way communication feature necessary for dynamic services like transport scheduling.
•	Not linked directly to input supply chain management (e.g., fertilizer or seed distribution).

4. Safaricom's DigiFarm (Kenya)
Application:
DigiFarm is a mobile platform providing farmers access to inputs, loans, insurance, and advisory services via USSD codes and smartphone apps.
Successes:
•	Wide reach due to partnership with Safaricom, Kenya’s leading mobile network operator.
•	Integrated value chain from input purchase to sales, improving service delivery.
•	Affordable and accessible even for smallholder farmers.
Misses:
•	Limited customization for specific institutional microservices like KARLO’s segmented transport and distribution services.
•	Data privacy concerns and reluctance among older farmers to fully engage digitally.
These case studies show that while Kenya has seen impressive advances in digital agriculture communication platforms, none fully address the comprehensive, real-time, two-way communication needs for service-oriented microservices (transport, fertilizer and seed distribution, market access) within an institution like KARLO. Current solutions either focus on information dissemination or market pricing but rarely integrate full logistics coordination or dynamic service feedback, which are essential for efficient operation of KARLO’s services.
Therefore, there is a clear opportunity to design a solution that provides real-time, interactive, farmer-institution communication — customized specifically for logistical and service needs within KARLO's operations.

**2.5 INTERGRATION AND ARCHITECTURE.**

For KALRO farmers, the architecture and integration of a Service Enquiry Ticket System must be carefully designed to guarantee seamless implementation and full compatibility with existing agricultural support systems. A central integration strategy involves linking the ticketing system with government service portals and KALRO’s existing database of registered farmers, enabling smooth information flow between farmers, KALRO officers, and external service providers.
To ensure inclusivity and accessibility, especially for farmers in remote areas with limited internet access, the system will integrate with SMS gateways and mobile applications, offering both offline and online access modes. Farmers will be able to create and track service enquiries via simple USSD codes, SMS, mobile apps, or a web portal. In addition, API-driven integration will enable real-time synchronization with government platforms, such as agricultural subsidy programs and technical advisory services, ensuring up-to-date service tracking and status reporting.
In terms of system design, the solution will adopt a cloud-based microservices architecture. Each agricultural microservice and platform function will operate independently but integrate through secure APIs to enable seamless coordination. Below is a table showing the proposed microservices:

Microservice	Description
Transport Microservice	Manages logistics scheduling, transport booking, and produce movement tracking.
Fertilizer Distribution Microservice	Handles fertilizer order placement, distribution tracking, and stock management.
Seed Distribution Microservice	Facilitates seed order requests, delivery tracking, and quality assurance updates.
Produce Marketing Microservice	Connects farmers to buyers, manages market listings, and tracks sale outcomes.
Table 4 Microservices Intergration
Each of these core agricultural services will operate as an independent microservice component, allowing for modular development, deployment, and scaling without disrupting the operation of the entire platform. For example:
•	A Ticket Submission Service will manage farmer enquiries across transport, seeds, fertilizers, and marketing.
•	A Response Management Service will assign and track agent responses based on ticket type and urgency.
•	An Alerts and Notifications Service will handle automated updates via SMS, email, or mobile push notifications based on ticket progress.
•	A Farmer Profile and Data Service will securely manage farmer records, past ticket histories, and service preferences.

Security will be enforced through:
•	Role-Based Access Control (RBAC)
•	Secure API Gateways
•	End-to-End Encryption
•	Audit Trails for service requests and responses.
This microservices approach ensures that KALRO can deliver real-time, efficient, farmer-centric service communication, positioning the platform for future expansion and integration with emerging agricultural technologies.



 
Figure 3 Microservice Architecture


<img width="973" height="410" alt="image" src="https://github.com/user-attachments/assets/c6af79b4-cd7f-4d04-bd41-77fde44c0f6c" />

















**2.6 SUMMARY.**

The literature analysis concludes by emphasizing the role that digital communication platforms—like ticketing systems—play in enhancing service delivery and filling in communication gaps across a range of industries, including agriculture. The evaluation highlights how a service enquiry ticket system, which centralizes requests, tracks responses, and improves transparency, can expedite interactions between KALRO farmers and government services. Case studies from the agricultural and other industries show how successful similar systems may be in increasing productivity, but issues with digital literacy, technology accessibility, and system responsiveness still exist. Possible architectural frameworks are revealed by theoretical models of automated, decentralized, and centralized systems; a microservices-based, cloud-integrated architecture emerges as a versatile and scalable option. This assessment highlights potential implementation-related issues and lays the groundwork for creating a ticketing system that is safe, easily accessible, and customized to meet the specific requirements of rural farmers.













**2.7 RESEARCH GAPS.**

Many research gaps exist in the application of digital communication systems, especially for rural agricultural communities like KALRO farmers, as the literature study makes clear. There is little research on the use of ticketing systems in agriculture, particularly in low-resource settings with limited access to digital literacy and technological infrastructure, despite the fact that they have been extensively studied and used in customer service and other industries. Furthermore, the majority of current solutions fall short in addressing the particular requirements of rural farmers, namely support in their native tongues and access through simple mobile phones. In order to guarantee effective and timely service delivery, there is also a dearth of attention paid to the integration of government agriculture services with these systems. By creating a ticketing system specifically suited to the requirements of KALRO farmers, this research aims to close these gaps. It emphasises accessibility via smartphone integration, user-friendly design, and language support. Furthermore, in order to guarantee a seamless exchange of information and services, the project will investigate methods for integrating the system with currently in use government platforms. The goal of this project is to close these gaps and provide a workable, scalable solution that improves farmer-government relations in the provision of agricultural services.







References

Eremina, I., Yudin, A., Tarabukina, T., & Oblizov, A. (2022). The Use of Digital Technologies to Improve the Information Support of Agricultural Enterprises. International Journal of Technology, 13(7), 1393-1402.
Ntaliani, M., Costopoulou, C., & Karetsos, S. (2008). Mobile government: A challenge for agriculture. Government Information Quarterly, 25(4), 699-716.
Hillstrom, K., & Hillstrom, L. C. (Eds.). (2007). The Industrial Revolution in America: Communications, Agriculture and Meatpacking, Overview/Comparison [3 volumes]. 
Bloomsbury Publishing USA. 
Kumar Jaiswal, P. (2011). SMS Based Information Systems. University of Eastern Finland School of Computing.
Ault, A. C., Krogmeier, J. V., & Buckmaster, D. (2013). Mobile, cloud-based farm management: a case study with trello on my farm. In 2013 Kansas City, Missouri, July 21-July 24, 2013 (p. 1). American Society of Agricultural and Biological Engineers.
Mao, X., Huang, Q., Pan, J., Yan, Z., & Liu, W. (2021). Research on New Ticket System Architecture Based on Middle Platform. In Advances in Smart Vehicular Technology, Transportation, Communication and Applications: Proceeding of the Third International Conference on VTCA, 15–18 October 2019, Arad, Romania (pp. 237-248). Springer Singapore.
Christou, E., Avdimiotis, S., Kassianidis, P., & Sigala, M. (2004, January). Examining the factors influencing the adoption of web-based ticketing: Etix and its adopters. 
In ENTER (pp. 129-138).
Singh, P., Kansal, M., Tyagi, G., Tanwar, K., Singh, A. P., & Yadav, R. K. (2024). Empowering Farmers: An AI-Based Solution for Agricultural Challenges. In Computational Intelligence in Internet of Agricultural Things (Pp. 401-417). Cham: Springer Nature Switzerland.
Fachri, B. (2023). Ticket reporting information system using a web based waterfall method. Prosiding universitas dharmawangsa, 3(1), 282-290.
Burbi, S., & Hartless Rose, K. (2016). The role of internet and social media in the diffusion of knowledge and innovation among farmers.




**CHAPTER 3: SYSTEM ANALYSIS AND DESIGN**
**3.1 Introduction**
This chapter provides a comprehensive analysis and design overview of the proposed USSD-based agricultural platform developed for the Kenya Agricultural and Livestock Research Organization (KALRO). The system was designed to provide rural and peri-urban farmers with seamless access to agricultural services and digital payment capabilities through a simple, accessible USSD interface. It specifically aims to support services such as product registration, produce selling and buying, seed and fertilizer offers, and transport requests—integrated with Safaricom’s Daraja API for STK Push mobile payments.
To ensure that the system meets user expectations and technical standards, this chapter outlines the methodologies used in its development, starting from requirement gathering to logical system design. A user-centered and iterative approach was adopted to ensure both functionality and usability.

**3.2 Systems Development Methodology**
In the development of the KALRO USSD application, an Agile Software Development Methodology was adopted. This methodology emphasizes iterative development, close stakeholder collaboration, and continuous feedback—key factors when building systems meant to be both user-centric and responsive to changing agricultural service needs.
Agile was chosen due to its suitability for projects where requirements are expected to evolve. Since the KALRO USSD app serves a wide demographic with varying literacy and technology exposure, iterative prototyping and constant user feedback loops were crucial in ensuring the final product was simple, functional, and effective.
The Agile process followed these phases:
1.	Planning and Requirement Gathering: Initial meetings with KALRO stakeholders were conducted to define the scope, major features, and target user groups of the system. This phase also involved outlining key deliverables like produce buying/selling, transport requests, and seed offers.
2.	Design Iterations: The USSD menu structure and backend logic were designed incrementally. After each iteration, feedback was gathered from mock users and KALRO personnel to refine menu flows, improve confirmation steps, and ensure logical navigation.
3.	Incremental Development: Using Flask for the backend and MongoDB for storage, features such as user registration, STK Push payment handling via Daraja, and purchase/sales data recording were implemented one at a time in weekly sprints. Each module was tested independently.
4.	Testing and Integration: Modules were integrated and tested as they were completed. Emphasis was placed on Daraja callback handling and maintaining seamless session states in USSD, especially during multi-step processes like payments and confirmations.
5.	Deployment and Feedback: The application was deployed in a testing environment for user trials. Feedback led to improvements in menu clarity, database schema adjustments, and the addition of features like transport requests.
The flexibility of Agile allowed the system to remain adaptable and responsive, especially when KALRO requested enhancements to menu flows or changes in pricing structures for different produce items. It also ensured that stakeholder input was incorporated continuously throughout development, increasing the likelihood of adoption and usability among rural farmers.

**3.3 Feasibility Study**
The feasibility study was conducted to assess whether the development and deployment of the KALRO USSD-based platform was viable and sustainable. This involved examining the project from several dimensions: technical, operational, economic, and legal. The goal was to ensure that the system could be developed with the available resources and would deliver value to farmers, KALRO officers, and other agricultural stakeholders.
3.3.1 Technical Feasibility
The proposed system is technically feasible. The application leverages proven technologies including:
•	USSD Gateway integration to facilitate interactions over feature phones.
•	Flask, a lightweight and efficient Python web framework, for building the backend logic.
•	MongoDB, a NoSQL database suited for flexible data models such as user sessions, transactions, and dynamic product catalogs.
•	Daraja API for initiating and handling mobile money payments via STK Push.
•	Hosting on cloud platforms or local servers using minimal infrastructure.
All these tools are open-source or available via freemium plans, making them cost-effective and suitable for scalable deployment across various regions in Kenya.
3.3.2 Operational Feasibility
The system is operationally feasible for both farmers and KALRO staff:
•	The USSD interface ensures accessibility to users with basic mobile phones and without internet access.
•	The menu-driven design is simple, with short and clear steps.
•	Payment confirmations via STK Push (Daraja) are familiar to most Kenyan mobile users, improving ease of use.
•	KALRO agents can access purchase and transport data through a simple admin dashboard, aiding in logistics coordination and recordkeeping.
Training needs are minimal due to the straightforward interface and language used in prompts.
3.3.3 Economic Feasibility
From a financial standpoint, the system is economically viable:
•	Development costs were kept low by using open-source technologies (Flask, MongoDB).
•	The USSD service can be provisioned using shortcodes through partnerships with mobile operators or aggregators.
•	Ongoing costs are minimal and include server hosting, USSD gateway fees, and optional cloud database services.
The expected economic benefits—improved market access for farmers, reduced losses from unsold produce, and more efficient agricultural input distribution—outweigh the development and operational expenses.
3.3.4 Legal Feasibility
The system complies with the relevant legal and regulatory frameworks in Kenya:
•	Data privacy: User information, including phone numbers and transaction data, is securely stored and not shared with third parties without consent.
•	Payment regulations: The Daraja API integration aligns with Safaricom’s standards and is legally compliant with Central Bank of Kenya (CBK) mobile transaction policies.
•	USSD licensing: Collaboration with licensed mobile service providers ensures the system’s USSD access is lawfully provisioned.
With proper data management and adherence to Kenya’s Data Protection Act (2019), the application meets all key legal requirements.

**3.4 Requirements Elicitation**
Requirements elicitation is a critical phase in the system development process that involves gathering, analyzing, and validating the needs of stakeholders to guide system design and implementation. For the KALRO USSD application, a combination of qualitative techniques was employed to obtain accurate, comprehensive, and user-centered system requirements.
3.4.1 Stakeholder Identification
The primary stakeholders involved in the system include:
•	Smallholder farmers: The end users who interact with the USSD system to buy/sell farm produce, access seed and fertilizer offers, and request transportation services.
•	KALRO officers: Agricultural officers responsible for monitoring transactions, managing logistics, and analyzing usage data from the admin dashboard.
•	Agricultural input suppliers: Entities offering seeds, fertilizers, and other inputs to farmers.
•	Mobile network service providers: Facilitators of USSD and mobile money infrastructure (e.g., Safaricom via the Daraja API).
3.4.2 Techniques Used
To ensure the requirements reflect the actual needs of users and the operating environment, the following elicitation techniques were used:
•	Interviews: Informal discussions were conducted with KALRO staff and selected farmers to understand daily challenges, how they interact with agricultural systems, and their preferred workflows.
•	Observation: Field visits helped understand the digital literacy level of target users and confirmed that many use basic phones without internet connectivity, reinforcing the need for a USSD interface.
•	Document Review: Analysis of KALRO reports and existing agricultural service workflows provided insights into logistical issues such as delayed input delivery, unpredictable market prices, and poor record-keeping.
•	Brainstorming and Feedback Loops: Development was carried out iteratively, with each feature (e.g., transport request or produce sales) being reviewed and refined based on stakeholder feedback.
3.4.3 Key Requirements Identified
From the elicitation process, the following functional and non-functional requirements were established:
Functional Requirements:
•	Users should be able to register using their phone number, location, and PIN.
•	The USSD system must allow users to:
o	Browse and purchase available farm produce.
o	Sell their own produce (e.g., tomatoes, sukumawiki, onions).
o	Access current offers on seeds and fertilizers.
o	Request transportation for farm goods.
•	Payment should be confirmed via Safaricom STK Push using Daraja API.
•	Admins should have access to purchase and transport data, filtered by location.
Non-Functional Requirements:
•	The system must support session persistence across multiple steps.
•	Menus must be short, intuitive, and easily navigable using a feature phone keypad.
•	Responses must be fast (typically under 5 seconds) to prevent USSD timeouts.
•	Data must be securely stored and protected in compliance with data protection laws.
•	The system must be scalable to accommodate additional produce categories and features in future updates.
These requirements guided the modeling and design phases and ensured the resulting system aligns with real-world usage and constraints.

**3.5 Data Analysis**
Data analysis plays a critical role in transforming raw user inputs, requirements, and stakeholder feedback into a structured framework for system development. For the KALRO USSD-based platform, data analysis focused on identifying patterns, refining workflows, and segmenting core functionalities that would support effective service delivery to farmers.
The analysis was performed on the data collected during the requirements elicitation phase, field observations, and prototype feedback from test users. The aim was to ensure the system structure directly addresses real user needs while maintaining technical feasibility.
3.5.1 User Behavior Patterns
The analysis revealed the following behavioral insights that significantly influenced the system design:
•	Most farmers use feature phones, making USSD the most practical communication interface.
•	Users prefer direct navigation paths: Farmers favored short, menu-driven options with minimal steps, e.g., selecting produce by number rather than typing full names.
•	Pricing sensitivity: Many users compare prices before committing to a purchase or sale, prompting the inclusion of price previews and confirmation steps.
•	Reliance on mobile payments: Most users already use M-PESA, which validated the integration of STK Push via the Daraja API for secure and familiar payments.
3.5.2 Functional Grouping
From the data, system functionalities were grouped into the following modules:
•	User Management: Registration, login with PIN, and user session tracking.
•	Product Marketplace:
o	Buy Produce: View available farm products, select quantity, and make payments.
o	Sell Produce: Select produce, enter quantity for sale, and confirm submission.
•	Inputs Offers: View available fertilizer offers by category.
•	Transport Requests: Request transportation services for sold produce, with linked location data.
•	Admin Dashboard Access: View filtered transactional data based on the admin’s assigned location and status.
3.5.3 Data Entities and Attributes
Key data elements were identified for database modeling. These include:
Entity	Attributes
User	Phone number, Name, PIN, Location ID, Date of Registration
Produce Item	Name, Grades/Weight Categories, Price per unit, Available Stock
Purchase	User ID, Produce Name, Quantity, Total Price, Payment Status, Timestamp
Sale	User ID, Produce Type, Quantity, Selling Price, Status, Timestamp
Transport Request	User ID, Purchase/Sale ID, Pickup Location, Status, Request Time
Admin	Name, Email, Password, Assigned Location ID
These entities were further used to define MongoDB collections such as users, purchased, sales, and admins.
3.5.4 Workflow Insights
•	Sequential menu navigation was preferred over branching to reduce confusion.
•	Users often abandon sessions if required to enter long text, favoring numeric options.
•	Confirmation prompts reduced transaction errors and improved user trust.
The insights gained during data analysis provided the basis for modeling the system’s flow, database structure, and interface logic, all tailored for efficiency and usability.

**3.6 System Specification**
The system specification defines both the functional and non-functional requirements of the KALRO USSD-based agricultural platform. These specifications provide a clear blueprint for what the system must accomplish and how it should behave under various conditions. They serve as the foundation for system modeling, design, and implementation.
3.6.1 Functional Requirements
These are the specific operations and tasks the system must perform to meet user and stakeholder needs:
1.	User Registration
o	New users must register with their phone number, full name, location, and create a 4-digit PIN.
o	Registered users must be stored in the users MongoDB collection with a unique identifier.
2.	User Login and Session Management
o	Existing users must log in using their phone number and PIN.
o	The system must maintain session state throughout the USSD interaction.
3.	Buy Farm Produce
o	Users should browse produce options (e.g., Tomatoes, Cabbages, Sukumawiki).
o	Upon selecting a product and weight, the system should display the price.
o	Payment is handled via Daraja STK Push and must confirm success before finalizing the transaction.
o	The transaction is saved in the purchased collection.
4.	Sell Farm Produce
o	Farmers can list produce for sale by selecting item type and weight category.
o	Selling prices are automatically calculated and shown before submission.
o	Sales are recorded in the sales collection.
5.	Access Seed and Fertilizer Offers
o	Users can view available offers grouped by input type.
o	Offers are static but updatable from the admin side.
6.	Transport Request
o	Users can request transport for a purchased item whose transport_checkout_status is currently marked as "declined".
o	The system retrieves such entries from the purchased collection and displays them to the user.
o	Upon selection, the system updates the transport_checkout_status from "declined" to "included" to indicate that the user now wants transport to be arranged.
o	No new collection is created; all transport-related updates are managed within the existing purchased documents.
o	The update is timestamped and available for admin review in the dashboard.
7.	Admin Dashboard Access
o	Admins log in via a web interface using secure credentials.
o	The dashboard filters transactions and transport requests based on the admin’s assigned location.
o	Only completed purchases with included or completed transport status are displayed.
8.	Daraja Callback Handling
o	The system receives payment callbacks and updates payment_status to completed or failed.
o	Upon success, the user receives a confirmation USSD message and the transaction is finalized.
3.6.2 Non-Functional Requirements
These define the quality attributes the system must uphold for performance, security, and reliability.
Requirement	Description
Performance	All USSD responses must be returned within 5 seconds to prevent timeout.
Availability	The system must be accessible 24/7 with minimal downtime.
Scalability	The system must support additional produce types, input offers, and users.
Security	User data and PINs must be securely stored using access controls.
Data Integrity	Transactions must be atomic, especially around payment and confirmation steps.
Usability	Menus must be clear, short, and intuitive to users with low digital literacy.
Compliance	The system must adhere to Kenya’s Data Protection Act and M-PESA transaction laws.
Localization	he system should support multilingual options in future updates.

The above specifications ensure that the KALRO USSD system meets the intended goals of accessibility, reliability, and ease of use for farmers, while remaining manageable and insightful for KALRO administrators.




**3.7 Requirements Analysis and Modeling**
After gathering and specifying the system requirements, the next step involves analyzing them to identify relationships, dependencies, and potential conflicts, and structuring them into a coherent design. This ensures that the final system aligns with stakeholder needs and behaves predictably in real-world usage.
This section outlines the analysis process, highlights how the requirements were structured into components, and presents key modeling diagrams used to visualize system behavior and interactions.
3.7.1 Requirements Dependency and Conflict Analysis
The requirements were carefully reviewed to identify logical dependencies and possible conflicts:
•	Dependencies:
o	STK Push payments depend on successful user authentication and product selection.
o	Transport requests depend on the existence of a completed purchase with a transport_checkout_status of "declined".
o	Admin dashboard filters depend on accurate location_id mapping during registration.
•	Potential Conflicts and Solutions:
o	Conflict: Payment confirmation and session timeout can cause data loss.
	Solution: Implement asynchronous Daraja callback handling to update payment status independently of session flow.
o	Conflict: Multiple transactions by a user in rapid succession may cause confusion in transport requests.
	Solution: Allow selection from a list of previously completed purchases where transport was declined.
3.7.2 Functional Structuring of Requirements
Requirements were grouped into modular functionalities, each handled by specific components:
Module	Functionality
Produce Marketplace	Buying and Selling of Farm Produce
Payment Processing	STK Push Initiation, Callback Handling
Input Offers	Viewing seed and fertilizer offers
Transport Request	Updating transport status for prior declined purchases
Admin Dashboard	Viewing filtered records of purchases and transport statuses by location
User Management	Registration, Login, Session Tracking

Each module is implemented as a Flask route (or endpoint) and interacts with MongoDB collections like users and purchased.
3.7.3 Modeling Diagrams
To further clarify and visualize system behavior, several modeling diagrams were used:
A. Use Case Diagram
 


<img width="675" height="654" alt="image" src="https://github.com/user-attachments/assets/e78cbade-d687-4aba-a3d4-0d5471727717" />











B. Data Flow Diagram (DFD) 

 <img width="923" height="1209" alt="image" src="https://github.com/user-attachments/assets/789a67e1-fdf8-467c-9b8d-a42ecb790418" />


C. Conceptual Class Diagram 
<img width="975" height="933" alt="image" src="https://github.com/user-attachments/assets/af86bcbc-8123-4d06-b1d7-a2a85120e4e1" />

 
These diagrams and the modular structure ensured that the development team could clearly understand the expected system functionality and interactions. They also served as documentation references during testing, debugging, and stakeholder reviews.


**3.8 Logical Design**
This section outlines the logical design of the KALRO USSD Application. It captures the core structure, behavior, and functionality of the system using high-level architectural and flow models. The logical design serves as a blueprint for the implementation phase.
3.8.1 System Architecture
The KALRO USSD Application adopts a client-server architecture, where the mobile user acts as the client, and the back-end system (server) processes requests and returns appropriate responses.
Major Components:
•	USSD Client Interface
Interacts with users through shortcodes via mobile phones.
•	USSD Gateway (Middleware)
Facilitates communication between the mobile network and the application server.
•	Application Server (Backend)
o	Handles session logic, menu navigation, and user interactions.
o	Processes transactions such as purchases, registrations, and submissions.
•	Database (MongoDB)
Stores:
o	User records (e.g., farmer profiles)
o	Transactions (e.g., fertilizer purchases)
o	Produce listings
o	Research queries
•	MPesa STK Push API
Integrates mobile money for payment handling.


Client-Server
<img width="558" height="506" alt="image" src="https://github.com/user-attachments/assets/b4a2deae-65db-4b06-a043-c38acd1a8acb" />

 
3.8.2 Control Flow and Process Design
Control flow refers to how users navigate the system and how the server handles those interactions. Each menu option triggers a route which processes the request, performs validations, interacts with the database, and returns a USSD response.
Key Process Flows:
1.	User Registration/Login
o	User inputs details via USSD.
o	System stores in users collection.
2.	Purchase Produce
o	User selects item and quantity.
o	System calculates price and initiates STK Push.
o	Upon Daraja callback success, record saved in purchased with payment_status = completed.
3.	Sell Produce
o	User selects produce and enters quantity.
o	Price is calculated and saved in sales collection.
4.	Request Transport
o	System fetches declined purchases.
o	User selects one and confirms STK Push for transport.
o	On success, system updates transport_checkout_status to "included".
Sequence Diagram (Textual):
<img width="678" height="1017" alt="image" src="https://github.com/user-attachments/assets/8b26cf52-66c3-4454-97a0-5d63dbab672e" />

 
Activity Flow
Example – Fertilizer Purchase with Transport:
1.	User selects "Fertilizer Offers"
2.	List shown → User selects an item
3.	System asks: "Do you want to buy?"
4.	If Yes → Ask "Do you want transport?"
5.	If Yes → Add Ksh 350 to price
6.	Show total + confirmation
7.	If confirmed → Trigger STK Push
8.	Record transaction
 <img width="716" height="1350" alt="image" src="https://github.com/user-attachments/assets/23bc4c62-10f6-4852-9c45-861ce38a87b1" />

Pseudo-code 

if purchase['transport_checkout_status'] == 'declined':
    initiate_stk_push(user_phone, transport_fee)
    if payment_success:
        update purchase set transport_checkout_status = 'included'



3.8.3 Design for Non-Functional Requirements
Security Strategies:
•	Input validation on all entries (e.g., numeric enforcement for ID, menu options)
•	STK Push via MPesa ensures secure payment flow without exposing user credentials.
•	Database access is restricted and encrypted via environment credentials.
Error and Exception Handling:
•	Graceful fallback on invalid inputs (e.g., “Invalid option. Try again.”)
•	Session timeout handling after 180 seconds of inactivity.
•	Transaction rollback on payment failure.
Efficiency, Effectiveness & Appeal:
•	Fast-loading text-based menus optimized for low-end phones and 2G networks.
•	Simple and clear wording tailored to target farmers in rural areas.
•	Transport cost calculation automated to enhance decision-making.
•	Session memory logic helps return users where they left off if interrupted.

**3.9 Physical Design**
This section presents the physical design of the KALRO USSD application. It includes decisions and specifications regarding the actual technologies and platforms used, with emphasis on the database, user interfaces, and system integration components.
3.9.1 Database Design
Database Management System (DBMS):
•	MongoDB (NoSQL) – chosen for its flexibility, scalability, and ability to store semi-structured data.
Database Schema (Collections & Fields):
Collection	Fields
users	_id, name, location, category, phone_number, registered_at
purchased	_id, user_id, item_name, item_type, price, quantity, transport_checkout_status, total_price, payment_status, purchased_at
sales	_id, user_id, produce_type, quantity, price_per_unit, status, date
admins	_id, username, password

Design Features:
•	Data Integrity: Validations for phone numbers and numeric entries.
•	Security:
o	Passwords implementation in admins collection.
o	Access to CRUD operations controlled via role-based privileges.
•	Indexing:
o	Indexes on user_id, purchased_at, and date to improve filtering and reporting.
•	Optimization:
o	Light-weight documents for low latency and fast query response in USSD environment.
•	Storage Format:
o	All data stored in JSON-like BSON format native to MongoDB.
3.9.2 User Interface Design
Though the system operates via a USSD interface (text-based), design considerations were applied to ensure usability, clarity, and logical flow across interactions.
Application Programming Interfaces:
•	USSD Gateway ↔ Application Server
o	Handles session initiation, input capture, and response rendering.
•	Application Server ↔ MongoDB
o	CRUD operations for user data, offers, transactions, etc.
•	Application Server ↔ MPesa API
o	Sends STK Push requests and processes callbacks.
Input and Output Forms
Function
	Input (User Entry)	Output (System Response)
User Registration	
Name, Phone number, Location,
	"You have been registered successfully as a Farmer in [County]."
Fertilizer Purchase	Selection of fertilizer, transport option (Yes/No), quantity confirmation	Displays total price, transport fee if applicable, asks to pay
Transport Option	"Do you want transport?" (1 for Yes, 2 for No)	Shows delivery fee (Ksh 350) added to total, displays final cost
Payment Confirmation	"Pay Now?" (1 for Yes, 2 for Cancel)	
STK Push triggered or "Transaction Cancelled."

Sell Farm Produce	Produce type, quantity, price per unit	"Your produce has been listed for sale."
Login	Pin	"Welcome, [User]!" or error message if not found


Wireframe (USSD Flow Sketch):
Due to the nature of USSD, wireframes are linear. Below is a text-based wireframe example for Fertilizer Offers flow:
[Main Menu]
1. Fertilizer Offers
2. Buy Farm Produce
3. Sell Farm Produce
4. Research Help
5. Exit

[Fertilizer Menu]
1. NPK 23-23-0 @ Ksh 3,000
2. CAN @ Ksh 2,700
00. More     00. Back

[Confirm Buy]
Do you want to buy NPK 23-23-0?
1. Yes
2. No




[Transport Option]
Need transport? (Add Ksh 350)
1. Yes
2. No

[Payment]
Total: Ksh 3,350
Pay Now?
1. Yes
2. Cancel

                 


<img width="566" height="848" alt="image" src="https://github.com/user-attachments/assets/6cd421fc-3d50-40e4-a2c0-0cac445a2012" />



**CHAPTER 4: SYSTEM IMPLEMENTATION AND TESTING,
CONCLUSIONS AND RECOMMENDATIONS**

**4.1 Introduction**
This chapter describes the implementation environment, tools used, and testing processes for the KALRO USSD application. It also presents conclusions and recommendations drawn from the system development lifecycle.
The goal of the system is to provide an accessible mobile-based platform for farmers, agro-dealers, and researchers to interact with KALRO services via USSD, even in low-bandwidth regions. A layered architecture was adopted, encompassing the backend logic, middleware (USSD gateway), and a cloud-hosted NoSQL database.
**4.2 Environment and Tools**
The system was developed in a modular, multi-layered environment comprising the backend server, USSD gateway middleware, and a cloud-hosted database. The tools and technologies were selected based on reliability, ease of integration, and scalability.
4.2.1 Backend (Server-Side Logic)
The backend was developed using Python with the Flask framework. It handles session management, menu navigation, transaction processing, and communication with the database and payment system.
•	Programming Language: Python 3
•	Framework: Flask (lightweight and suitable for RESTful APIs)
•	Core Libraries:
o	pymongo – for MongoDB integration
o	requests – for API communication with M-Pesa
o	python-dotenv – for environment variable management

4.2.2 Middleware (USSD Gateway Integration)
The USSD layer is integrated using Africa’s Talking, a platform that provides programmable USSD shortcodes and handles session routing.
•	Integration Platform: Africa’s Talking (AT)
•	Implementation Details:
o	USSD requests are received via AT
o	AT forwards user inputs to the Flask backend through POST requests
o	The backend responds with the next menu or action
4.2.3 Database
The application uses MongoDB as its primary data storage system due to its flexibility and support for dynamic schema designs. Data is stored in collections rather than relational tables.
•	Database Type: NoSQL
•	Database Engine: MongoDB (hosted on MongoDB Atlas)
•	Main Collections:
o	users – stores user registration details
o	purchased – stores fertilizer and produce purchase transactions
o	sales – stores data on listed farm produce
o	admins – stores admin login credentials
•	Security Features:
o	Encrypted connections via TLS
o	Admin credentials hashed before storage
o	IP-based access control (whitelisting enabled)
4.2.4 Deployment Environment
Development and testing were performed locally using Ngrok to expose the backend server to the internet. This allowed seamless integration with Africa's Talking USSD gateway during the development phase.
•	Development OS: Windows 10
•	Editor: Visual Studio Code (VS Code)
•	Local Hosting Tool: Ngrok – used to tunnel the Flask server over a public URL
•	Testing Devices: Safaricom-enabled GSM phones for USSD and MPesa STK Push verification
**4.3 System Code Generation**
The code generation process for the KALRO USSD application involved translating the system’s logical design into working modules that handle user registration, menu navigation, fertilizer purchases, produce sales, and MPesa payment integration. The backend was built using Python with the Flask framework, while Ngrok was used to expose the localhost endpoint to Africa's Talking for testing.
The code is structured around endpoints that respond to incoming POST requests from Africa’s Talking’s USSD gateway. Each session progresses by checking the user's input (text) and returning the appropriate menu or action.
4.3.1 Key Process: USSD Entry Point
This route handles incoming requests from Africa’s Talking and determines the next screen to show based on user input.
@daraja_callback_bp.route("/daraja/callback", methods=["POST"])
def daraja_callback():
    data = request.get_json(force=True)
    print("Headers:", request.headers)
    print("Content-Type:", request.content_type)
    print("Callback received:", data)

    try:
        callback = data['Body']['stkCallback']
        result_code = callback['ResultCode']
        checkout_request_id = callback['CheckoutRequestID']
        result_desc = callback['ResultDesc']

        # Update the matching purchase
        update_result = purchased.update_one(
            {"mpesa_checkout_request_id": checkout_request_id},
            {
                "$set": {
                    "status": "completed" if result_code == 0 else "failed",
                    "result_code": result_code,
                    "result_desc": result_desc,
                    "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )

        print(f"Update matched {update_result.matched_count} document(s).")

    except Exception as e:
        print("Error processing callback:", str(e))

4.3.2 Key Process: Registration
When a new user accesses the system, they’re guided through a step-by-step registration process.
elif not is_registered:
        if user_responses[0] == "1":  # Register flow
            if level == 1:
                response = "CON Enter your name:"
            elif level == 2:
                response = "CON Select your location:\n" + "\n".join([f"{k}. {v}" for k, v in locations.items()])
            elif level == 3:
                if user_responses[2] in locations:
                    response = "CON Create a 4-digit PIN:"
                else:
                    response = "END Invalid location."
            elif level == 4:
                name, location_key, pin = user_responses[1], user_responses[2], user_responses[3]
                if location_key in locations:
                    users.insert_one({
                        "phone": phone_number,
                        "name": name,
                        "location": locations[location_key],
                        "pin": pin
                    })
                    response = f"END Registration successful. Welcome, {name}!"
                else:
                    response = "END Invalid location."
        else:
            response = "END Thank you for visiting KALRO."

    else:
        response = "END Invalid input."

    return Response(response, mimetype="text/plain")


4.3.3 Key Process: Fertilizer Purchase with Transport Option
This section allows users to view fertilizer options, select one, and choose whether they want transport
 if option == "1":
                # Level 3 -> display main offers menu
                if level == 3:
                    response = (
                        "CON Select an input:\n"
                        "1. DAP 18:46:00 10Kg - 160\n"
                        "2. NPK 23:23:00 10Kg - 660\n"
                        "3. CAN 26%N 10Kg - 980\n"
                        "4. CAN 26%N 25Kg - 2200\n"
                        "5. CAN 26%N 50Kg - 3850\n"
                        "00. More"
                    )
                elif level == 4:
                    choice = user_responses[3]
                    if choice == "00":
                        response = (
                            "CON More Offers:\n"
                            "6. DAP 18:46:00 50Kg - 6500\n"
                            "7. NPK 17:17:17 50Kg - 6700\n"
                            "00. Back"
                        )
                    elif choice in offers:
                        item = offers[choice]
                        response = (
                            f"CON You selected {item['name']} @ Ksh {item['price']}.\n"
                            "Would you like delivery for KES 350?\n"
                            "1. Yes\n"
                            "2. No"
                        )
                    else:
                        response = "END Invalid selection."
                elif level == 5 and user_responses[3]=="00":
                    # More offers selection
                    choice = user_responses[4]
                    if choice =="00":
                        #Go back to main main

                        response = (
                            "CON Select an input:\n"
                            "1. DAP 18:46:00 10Kg - 160\n"
                            "2. NPK 23:23:00 10kG - 660\n"
                            "3. CAN 26%N 10Kg - 980\n"
                            "4. CAN 26%N 25Kg - 2200\n"
                            "5. CAN 26%N 50Kg - 3850\n"
                            "00. More"
                        )
                    elif choice in offers:
                        item = offers[choice]
                        response = (

                            f"CON You selected {item['name']} @ Ksh {item['price']}.\n"
                            "Would you like delivery for KES 350?\n"
                            "1. Yes\n"
                            "2. No"
                        )
                    else:
                        response = "END Invalid selection."

4.3.4 Key Process: MPesa STK Push Integration
If the user agrees to pay, the system initiates an STK Push via MPesa.
def lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc,callback):
    access_token = get_access_token()

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = MPESA_SHORTCODE + MPESA_PASSKEY + timestamp
    encoded_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

    stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
   
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        
    }

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": encoded_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": '254708374149',
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": callback,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
        
    }

    response = requests.post(stk_push_url, json=payload, headers=headers)
    data = response.json()

    print("MPESA STK Push Response:", data)

4.3.5 Key Process: Produce Sale Listing
Users can list their farm produce for sale with quantity and price.
        elif option == "3":
                if level == 3:
                    response = (
                        "CON Select produce to sell:\n"
                        "1. Tomatoes\n2. Cabbage\n3. Onions\n4. Sukumawiki\n5. Spinach\n6. Rice"
                    )

                elif level == 4:
                    prod_id = user_responses[3]
                    if prod_id in sell_options:
                        options = sell_options[prod_id]
                        response = "CON Select quantity:\n" + "\n".join(
                            [f"{k}. {v['qty']} - Ksh {v['price']}" for k, v in options.items()]
                        )
                    else:
                        response = "END Invalid produce selection."

                elif level == 5:
                    prod_id, qty_id = user_responses[3], user_responses[4]
                    produce_map = {
                        "1": "Tomatoes", "2": "Cabbage", "3": "Onions",
                        "4": "Sukumawiki", "5": "Spinach", "6": "Rice"
                    }

                    if prod_id in sell_options and qty_id in sell_options[prod_id]:
                        item = sell_options[prod_id][qty_id]
                        name = produce_map.get(prod_id, "Produce")
                        response = (
                            f"CON Confirm sale:\n{name} - {item['qty']} for Ksh {item['price']}\n"
                            "1. Confirm\n2. Cancel"
                        )
                    else:
                        response = "END Invalid selection."

                elif level == 6:
                    confirm = user_responses[5]
                    prod_id, qty_id = user_responses[3], user_responses[4]
                    item = sell_options.get(prod_id, {}).get(qty_id)
                    produce_map = {
                        "1": "Tomatoes", "2": "Cabbage", "3": "Onions",
                        "4": "Sukumawiki", "5": "Spinach", "6": "Rice"
                    }
                    name = produce_map.get(prod_id, "Produce")

                    if confirm == "1" and item:
                        sales.insert_one({
                            "phone": phone_number,
                            "produce": name,
                            "quantity": item["qty"],
                            "expected_price": item["price"],
                            "status": "available",
                            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        response = f"END Sale recorded for {item['qty']} {name} at Ksh {item['price']}."
                    else:
                        response = "END Sale cancelled.

**4.4 Testing**
Testing was a crucial phase in the development of the KALRO USSD application, ensuring that all system functions met the expected requirements. A structured testing strategy was adopted, involving both functional and non-functional tests.
4.4.1 Testing Strategy
The system was subjected to the following testing strategy.
1. Unit Testing
•	Tested individual functions in the backend such as:
o	Menu rendering
o	User registration steps
o	Transport price calculation
o	Database insertion logic
2. Integration Testing
•	Verified communication between:
o	Flask backend and MongoDB
o	Backend and Africa's Talking USSD gateway
o	Backend and MPesa STK Push API
3. End-to-End (E2E) Testing
•	Simulated real user sessions using mobile phones and Ngrok URLs
•	Performed real-time registration, buying, and selling processes
•	Verified payment flow via Safaricom’s STK Push
4. Validation Testing
•	Ensured correct handling of:
o	Invalid menu selections
o	Missing input values
o	Session timeouts and retry behavior
4.4.2 Testing Suite and Tools

Test Type	Tool/Platform	Description
Unit Tests	
Manual Python testing (VS Code)	Checked function outputs
API Integration	Postman / Curl	Simulated POST requests to /ussd route
USSD Simulation


	Africa's Talking sandbox & live USSD	Simulated USSD flow via mobile device
Tunnel Testing


	Ngrok	Exposed localhost to public USSD gateway
Payment Testing	Safaricom Daraja Sandbox	Triggered STK Push flows to verify payment interaction

4.4.3 Sample Test Cases and Results
Test Case	
	Expected Result
	Actual Result	Pass/Fail

User Registration with valid input	User Registration with valid input	Success	Success
Invalid menu input	Return “Invalid option. Try again.”	Error handled	Pass
Fertilizer selected + transport = total	Total price includes Ksh 350 transport	Accurate total	Pass
STK Push on "Pay Now"	Phone receives payment prompt	Prompt received	Pass
Selling produce with quantity and price	Produce listed in sales collection	Recorded	Pass
Transport skipped	Total shown without transport fee	Correct total	Pass


4.4.4 Screenshots of Tests 

**4.5 User Guide**
This section provides step-by-step instructions on how users interact with the KALRO USSD system. It covers registration, login, buying and selling produce, accessing offers, and making transport requests.
1. Accessing the System
•	Dial the USSD code (e.g., *123#) on any mobile phone.
•	The system checks if the user is registered.
2. Registration (First-Time Users)
•	Unregistered users are prompted to enter:
o	Full Name
o	Phone Number (auto-detected)
o	Location
o	4-digit PIN
•	Upon successful registration, the user proceeds to the main menu.
3. Login (Returning Users)
•	Enter your registered phone number and 4-digit PIN.
•	If authentication is successful, the system displays the main menu.
4. Main Menu Options
Upon login, users are presented with the following options:
1.	Fertilizer Request
2.	Buy Farm Produce
3.	Sell Farm Produce
4.	Request Transport
5. Buying Farm Produce
•	Select Buy Farm Produce.
•	Choose the produce type (e.g., Tomatoes, Cabbages).
•	Choose the weight or quantity.
•	The system displays the total price.
•	You confirm the order.
•	An M-PESA STK Push is initiated.
•	Upon successful payment, a confirmation is displayed and the purchase is saved.
6. Selling Farm Produce
•	Select Sell Farm Produce.
•	Choose the produce type.
•	Choose weight or quantity category.
•	The system displays the calculated selling price.
•	Upon confirmation, the sale is saved.
7. Viewing Seed and Fertilizer Offers
•	Select Fertilizer Offers.
•	Fertilizer offers are displayed by type.
•	Choose the weight or quantity.
•	The system displays the total price.
•	You confirm the order.
•	An M-PESA STK Push is initiated.
•	Upon successful payment, a confirmation is displayed and the purchase is saved.
8. Requesting Transport for Purchased Produce
•	Select Request Transport from the main menu.
•	The system retrieves all completed purchases where transport_checkout_status = "declined".
•	Choose the item you want transport for.
•	The system displays the transport fee.
•	Upon confirmation, an M-PESA STK Push is triggered for the transport cost.
•	On successful payment:
o	The purchase record is updated.
o	transport_checkout_status is changed to "included".
o	A confirmation is displayed to the user.

**4.6 Conclusions**
The development and implementation of the KALRO USSD-based agricultural platform successfully addressed the core needs identified by the client—primarily providing a simple, accessible, and reliable tool for farmers to engage with agricultural markets using basic mobile phones.
Problem Solved
The client’s challenge was to offer farmers—particularly those in rural areas without smartphones or internet—an effective platform to:
•	Register and manage their farm produce sales and purchases,
•	Access seed and fertilizer offers,
•	Receive transport support for purchased goods,
•	Make secure payments via M-PESA (Daraja API).
The system delivered on all these objectives. The USSD menu is intuitive and fast, allowing users to perform key tasks with minimal steps. Payment integration via Safaricom’s STK Push ensured transactions were seamless and trustworthy. Furthermore, the admin dashboard enables KALRO staff to track activity based on location and transport status, giving them visibility into field operations.
Significant Accomplishments
•	Fully functional USSD Application built with Flask and MongoDB, tailored for low-end mobile phone users.
•	Integrated STK Push (Daraja API) for payments, both for product purchases and transport requests.
•	Role-based System Access with farmer USSD interactions and admin dashboard filtering by location and transaction status.
•	Dynamic Transport Request Handling that updates purchased records based on user-initiated payment.
•	Scalable Data Models built around MongoDB for handling real-time transactions.
•	Improved Farmer Reach by removing the barrier of smartphones and internet access.
Limitations
Despite the successful implementation, some limitations were encountered:
•	Skills Gaps: Advanced UI/UX optimization for the admin dashboard and performance tuning for MongoDB required more expertise than initially available.
•	Budget Constraints: Some planned features like multilingual USSD support and SMS notifications were not implemented due to limited financial resources.
•	Tooling Constraints: Hosting and deploying a fully scalable USSD platform with production-grade testing (e.g., with shortcodes and Telco environments) required expensive third-party platforms and licenses.
Challenges Faced
•	Technical Complexity of Daraja Integration: While documentation exists, handling asynchronous callbacks and ensuring payment verification accuracy was challenging.
•	USSD Testing: Real-world testing required coordination with mobile carriers or simulators, which were not always reliable or easy to access.
•	Data Modeling Iterations: Evolving features like transport requests required frequent restructuring of MongoDB documents to maintain flexibility.
•	Limited Access to Devices for Field Testing: The team could not conduct large-scale live tests on actual feature phones, relying instead on sandbox environments.
Despite these challenges, the system achieved its primary goals and laid a foundation for future scalability, localization, and integration with more agricultural services.

**4.7 Recommendations**
Based on the conclusions drawn from the implementation of the KALRO USSD agricultural system, several improvements are recommended to enhance system performance, user experience, and scalability. First, the system should support multiple local languages such as Kiswahili to ensure that farmers from various regions can comfortably use the platform. Integrating SMS notifications for successful transactions and transport confirmations would also improve transparency and user confidence. The transport request feature could be expanded to include delivery timelines, driver information, or tracking capabilities to improve accountability. Additionally, the admin dashboard should be enhanced with features like report exporting, role-based access, and real-time notifications. Security and performance can be improved by implementing rate limiting, session logging, and USSD shortcode whitelisting. It is also recommended that the system be migrated to a dedicated, production-grade USSD gateway to ensure scalability and carrier compatibility. Further, automated handling and monitoring of STK Push failures should be implemented to maintain transactional reliability. Finally, piloting the system with real farmers and KALRO officers in a selected region before full-scale rollout will help refine the application based on real-world feedback.





