A TICKETING MECHANISM FOR KENYA AGRICULTURAL LIVESTOCK RESEARCH ORGANIZATION (KALRO) FARMERS.






AUTHOR:  KIERU GITAU

REG NO: SCT221-0520/2021

SUPERVISOR: Dr. DENNIS KABURU




















A proposal/ research project submitted to the Department of Information Technology in the School of Information Technology in partial fulfillment of the requirement for the award of the degree of Information Technology,Jomo Kenyatta University of Agriculture and Technology.


2025




DECLARATION

This proposal/research project is my original work and has not been presented for a degree in any other University


......................                                                                     .....................
Signature                                                                           Date


This proposal/research project has been submitted for examination with my approval as University Supervisor


..................                                                                            ...................
Signature                                                                               Date






















ABSTRACT

This project applies microservices architecture to address persistent communication challenges between farmers and the Kenya Agricultural and Livestock Research Organisation (KALRO). Farmers often experience delays, fragmented responses, and limited access to vital agricultural services due to the lack of a structured, responsive communication platform. The proposed solution is a centralized ticketing system built on microservices principles, where each core function—such as request submission, enquiry tracking, notification delivery, and analytics—is developed as an independent, interoperable service. This design ensures scalability, resilience, and adaptability to varying connectivity conditions, particularly in rural areas. The system will be accessible through mobile platforms, enabling farmers to log requests, receive timely updates, and track resolutions in real time. A pilot implementation will evaluate usability, response efficiency, and service delivery impact. The expected outcome is improved farmer–government engagement, greater service accessibility, and data-driven insights to inform future agricultural policies and operational improvements






















Contents:

A TICKETING MECHANISM FOR KENYA AGRICULTURAL LIVESTOCK RESEARCH ORGANIZATION (KARLO) FARMERS.	     i.

DECLARATION. 	     ii.

ABSTRACT.	        iii.



CHAPTER ONE:	1

1.0 INTRODUCTION.	1

1.2 PROJECT OVERVIEW.	1

1.3 STATE OF THE PROBLEM.	2

1.4 PROPOSED SOLUTION.	4

1.5 OBJECTIVES.	5

1.6 RESEARCH QUESTIONS.	6

1.7 JUSTIFICATION.	7

1.8 METHODOLOGY	7

1.9 SCOPE.	11

Appendices	13

A.	Project Resources.	13

B.	Budget	14

C.	Project Duration	15

CHAPTER TWO	16

2.1 INTRODUCTION.	16

2.2 THEORETICAL REVIEW.	17

2.3 CASE STUDY REVIEW.	19

2.4 INTERGRATION AND ARCHITECTURE.	20

2.4.1 Architectural Overview	20

2.4.2 Integration Workflow	21

2.4.3 Benefits of the Technology Stack	22

2.5 SUMMARY.	23

2.6 RESEARCH GAPS.	23

References	25

CHAPTER 3: SYSTEM ANALYSIS AND DESIGN	26

3.1 INTRODUCTION	26

3.2 SYSTEMS DEVELOPMENT METHODOLOGY	27

3.3 FEASIBILITY STUDY	28

3.3.1 Technical Feasibility	28

3.3.2 Operational Feasibility	28

3.3.3 Economic Feasibility	29

3.3.4 Legal Feasibility	29

3.4 REQUIREMENTS ELICITATION	30

3.4.1 Stakeholder Identification	30

3.4.2 Techniques Used	30

3.4.3 Key Requirements Identified	31

3.5 DATA ANALYSIS	32

3.5.1 User Behavior Patterns	32

3.5.2 Functional Grouping	32

3.5.3 Data Entities and Attributes	33

3.5.4 Workflow Insights	33

3.6 SYSTEM SPECIFICATION	33

3.6.1 Functional Requirements	34

3.6.2 Non-Functional Requirements	35

3.7 REQUIREMENTS ANALYSIS AND MODELING	36

3.7.1 Requirements Dependency and Conflict Analysis	36

3.7.2 Functional Structuring of Requirements	37

3.7.3 Modeling Diagrams	38

3.8 LOGICAL DESIGN	41
3.8.1 System Architecture	41

The Server	41

The Interaction Flow	41

3.8.2 Control Flow and Process Design	44

3.8.3 Design for Non-Functional Requirements	48

3.9 PHYSICAL DESIGN	48

3.9.1 Database Design	48

3.9.2 User Interface Design	49

CHAPTER 4: SYSTEM IMPLEMENTATION AND TESTING,	53

CONCLUSIONS AND RECOMMENDATIONS	53

4.1 INTRODUCTION	53

4.2 ENVIRONMENT AND TOOLS	53

4.2.1 Backend (Server-Side Logic)	53

4.2.2 Middleware (USSD Gateway Integration)	54

4.2.3 Database	54

4.2.4 Deployment Environment	54

4.3 SYSTEM CODE GENERATION	55

4.3.1 Key Process: USSD Entry Point	55

4.3.2 Key Process: Registration	56

4.3.3 Key Process: Fertilizer Purchase with Transport Option	57

4.3.4 Key Process: MPesa STK Push Integration	58

4.3.5 Key Process: Produce Sale Listing	59

4.4 TESTING	61

4.4.1 Testing Strategy	61

4.4.2 Testing Suite and Tools	62

4.4.3 Sample Test Cases and Results	63

4.4.4 Screenshots of Tests	64

4.5 USER GUIDE	65

4.6 CONCLUSIONS	67

4.7 RECOMMENDATIONS	69

Cases
KALRO: Kenya Agricultural and Livestock Research Organization	1

USSD: Unstructured Supplementary Service Data	6

SMS: Short Message Service	6

API: Application programming interface	19

IDE: Intergrated Development Environment	19

UI: User Interaction	19

UX: User Experience	19

Figure 1 Communication Gaps	3

Figure 2 Agile Planning	10

Figure 3 Microservice Architecture	22

Figure 4 Use Case	38

Figure 5 Data Flow Diagram	39

Figure 6 Class Diagram	40

Figure 7 Client-Server	43

Figure 8 Sequence Diagram	45

Figure 9 Activity Diagram	47

Figure 10 Wireframe	52

Figure 11 Screenshots	64

Table 1 Budget	15

Table 2 Gantt chart	16

Table 3 Data Entities and Attributes	33

Table 4 Non-Functional Requirements	36

Table 5 Modules	37

Table 6 Database Schema	49

Table 7 Input and Output forms	50

Table 8 Test Suite and Tools	62

Table 9 Test Results	63


















 

CHAPTER ONE:
1.0 INTRODUCTION.

Microservices architecture has emerged as a modern approach to building scalable, modular, and resilient systems, enabling organisations to break down complex applications into smaller, independently deployable services. This approach enhances maintainability, scalability, and flexibility, making it well-suited for solving sector-specific challenges that require efficient, adaptive solutions.
In Kenya’s agricultural sector, particularly within the Kenya Agricultural and Livestock Research Organisation (KALRO), farmers face persistent communication barriers when seeking government support, technical advice, and resources. The absence of a centralised, responsive platform has led to delays, miscommunication, and reduced access to vital agricultural services—issues compounded in rural areas with limited internet connectivity. Current communication channels are fragmented and inefficient, making it difficult for KALRO to deliver timely and targeted support.
This project applies microservices architecture to address these communication gaps by developing a centralized ticketing system tailored for KALRO’s operations. Core functions—such as request handling, enquiry tracking, notifications, and analytics—are implemented as independent, interoperable services. By enabling real-time request tracking, quick responses from officials, and seamless integration with other agricultural systems, the proposed solution aims to enhance farmer–government interactions, improve service accessibility, and support sustainable agricultural productivity.
1.2 PROJECT OVERVIEW.

Microservices architecture, while offering scalability, flexibility, and modularity, also presents unique challenges in implementation—particularly in environments where systems must operate under constraints such as unreliable connectivity, diverse user needs, and high demand for service responsiveness. The problem lies in designing a microservices-based solution that maintains efficient communication, ensures interoperability between services, and remains reliable even in resource-limited settings.
This project addresses that broader microservices communication challenge through a case study in Kenya’s agricultural sector. Within the Kenya Agricultural and Livestock Research Organisation (KALRO), farmers face delays, fragmented responses, and limited access to services due to disjointed communication channels. By applying microservices principles to this scenario, the project explores how independent services—such as request handling, notification delivery, and data analytics—can be orchestrated to create a coherent, responsive platform that overcomes both technical and operational barriers.
The KALRO case provides a real-world context to examine microservices-related issues such as service discovery, API communication reliability, fault tolerance, and deployment in low-bandwidth environments. The findings from this implementation aim to contribute to microservices best practices, offering insights into how such architectures can be optimised for sectors where timely information exchange directly impacts productivity and livelihoods.

1.3 STATE OF THE PROBLEM.

While microservices architecture offers significant advantages—such as scalability, independent deployment, and ease of integration—it also introduces critical challenges in maintaining seamless communication and service coordination. In distributed microservices environments, ensuring that independent services exchange information reliably, maintain data consistency, and respond in a timely manner can be complex. Issues such as network latency, service discovery failures, message loss, and inconsistent error handling often degrade system performance. These challenges are magnified in settings with unreliable connectivity, high request volumes, or diverse end-user access points.
The Kenya Agricultural and Livestock Research Organisation (KALRO) provides a real-world context where these microservices communication challenges are highly relevant. Farmers seeking government services through KALRO face delays, fragmented feedback, and inconsistent responses—symptoms that parallel common microservices communication breakdowns. In rural areas, poor internet access further compounds the problem, as message delivery between services can fail or be delayed, leading to incomplete or inaccurate transaction processing.
This situation underscores a broader microservices problem: how to design and implement a distributed system that ensures reliable, low-latency communication between services in environments where infrastructure constraints and user diversity are significant. Addressing this problem is essential not only for improving KALRO’s farmer–government interactions but also for contributing to microservices design strategies that perform effectively in similar high-demand, low-resource contexts.

 <img width="1950" height="1508" alt="image" src="https://github.com/user-attachments/assets/ab635227-2944-41f8-833f-f016198da36d" />

Figure 1 Communication Gaps

1.4 PROPOSED SOLUTION.

To address the challenge of maintaining reliable, efficient communication in a microservices environment, this project proposes a fault-tolerant, event-driven microservices architecture designed to ensure seamless interaction between distributed services even in low-resource conditions. The solution leverages asynchronous communication using lightweight message queues to minimise latency, prevent message loss, and enable services to operate independently without blocking requests.
In the case study context of the Kenya Agricultural and Livestock Research Organisation (KALRO), the architecture decomposes the centralized ticketing platform into modular services—such as request management, notification delivery, authentication, analytics, and reporting—each with its own database and API. A service discovery mechanism ensures that services can dynamically locate and communicate with each other, while circuit breakers and retry strategies handle failures gracefully.
The system will be deployed with container orchestration tools to manage scaling, load balancing, and failover, ensuring high availability even under fluctuating request volumes. API gateways will be used to standardize external communication, enforce security, and aggregate responses from multiple services for end-users.
By applying these microservices design patterns, the proposed solution aims to eliminate the communication breakdowns typical in distributed systems, while ensuring that KALRO farmers can submit requests, receive timely feedback, and access agricultural support seamlessly. The approach is adaptable and can be replicated in other sectors that require robust microservices communication in constrained environments.



1.5 OBJECTIVES.

General Objective.

1.	To design and implement a reliable, scalable, and fault-tolerant microservices architecture that addresses communication inefficiencies in distributed systems, using the Kenya Agricultural and Livestock Research Organisation (KALRO) as a case study.

Specific Objectives.
1.	To analyse the communication and coordination challenges inherent in microservices architectures, particularly in resource-constrained environments.

2.	To investigate the existing communication gaps between farmers and KALRO as a practical scenario for applying microservices principles.

3.	To design a microservices-based architecture incorporating service discovery, asynchronous communication, and fault-tolerance mechanisms to ensure reliable service interaction.

4.	To implement a case-specific microservices solution enabling farmers to submit requests, track progress, and receive timely updates via mobile platforms.

5.	To evaluate the performance, scalability, and resilience of the proposed architecture under varying connectivity and load conditions.

6.	To generate insights and best practices for applying microservices in similar high-demand, low-resource contexts beyond agriculture.




1.6 RESEARCH QUESTIONS.

1. What global and regional agricultural communication practices can inform the design of USSD-based systems for feature phone users in Kenya?
2. What are the most critical design considerations—such as menu simplicity and confirmation prompts—for creating an inclusive USSD system for farmers? 
3. How can admin-specific dashboards and localized data filters support the integration of the USSD system into KALRO’s operational workflows?  
4. What testing methods best validate usability, trust, and transaction accuracy in USSD applications during pilot programs with KALRO-registered farmers?  
5.  What impact does a centralized support and transaction tracking system have on government responsiveness and farmer satisfaction in agricultural service delivery?  
6. How can transaction data, user flow behaviour, and farmer feedback be used to iteratively improve the system’s navigation, pricing clarity, and feature relevance? Which of the following feedback sources should be used for improving the system?











1.7 JUSTIFICATION.

The adoption of microservices architecture in modern software development has transformed how complex systems are built, deployed, and maintained. However, the distributed nature of microservices introduces significant communication and coordination challenges, particularly in environments with limited infrastructure, fluctuating network reliability, and diverse user access points. Addressing these challenges is essential to unlocking the full potential of microservices in critical service delivery contexts.
The Kenya Agricultural and Livestock Research Organisation (KALRO) presents an ideal case study for this problem. Farmers relying on KALRO’s services often face delays, fragmented responses, and restricted access to essential agricultural support due to disjointed communication channels. These issues mirror common pain points in microservices communication, such as message loss, service discovery failures, and inconsistent data propagation—especially in rural areas with unstable connectivity.
By designing and implementing a microservices architecture that is fault-tolerant, scalable, and adaptable to low-resource conditions, this project not only aims to solve KALRO’s communication inefficiencies but also to contribute to best practices in microservices design. The solution’s relevance extends beyond agriculture, offering a framework that can be adapted to other sectors where reliable service interaction is critical for operational efficiency and stakeholder satisfaction.

1.8 METHODOLOGY

This project adopts the Agile Software Development Methodology to design, implement, and evaluate a microservices architecture aimed at solving distributed communication challenges, using the Kenya Agricultural and Livestock Research Organisation (KALRO) as a case study. Agile is selected due to its iterative approach, flexibility in accommodating changes, and suitability for modular development, which aligns with the principles of microservices.
1.	Agile Framework Selection
•	Scrum is chosen as the framework to guide development, with work divided into short iterations (sprints) of 2–3 weeks.
•	Core roles:
o	Product Owner – Represents stakeholders (KALRO and farmers) and prioritizes backlog items.
o	Scrum Master – Facilitates Agile practices and removes development impediments.
o	Development Team – Designs, codes, tests, and deploys microservices.
2.	Project Initiation & Backlog Creation
•	Identify high-level requirements through stakeholder workshops and interviews with KALRO staff and farmers.
•	Translate requirements into user stories (e.g., “As a farmer, I want to track my request so that I know its progress”).
•	Populate the Product Backlog with features mapped to individual microservices such as Request Management, Notification Service, Analytics, and Authentication.
3.	Sprint Planning & Execution
•	Break down backlog items into Sprint Backlog tasks for implementation within each sprint.
•	Prioritize tasks addressing core communication reliability issues in microservices, such as service discovery, fault tolerance, and message queuing.
•	Each sprint delivers a functional increment, such as a working version of a microservice or a tested API endpoint.
4.	Development Approach
•	Apply Test-Driven Development (TDD) to ensure each microservice meets its acceptance criteria before integration.
•	Implement services as independently deployable containers, enabling parallel development and faster iteration.
•	Use asynchronous messaging and API Gateway integration in early sprints to mitigate communication breakdowns.
5.	Review & Feedback
•	Conduct Sprint Reviews to demonstrate completed features to KALRO representatives and gather feedback.
•	Hold Retrospectives to identify process improvements for the next sprint.
6.	 Integration & Continuous Delivery
•	Integrate microservices gradually, validating communication reliability after each integration step.
•	Use Continuous Integration/Continuous Deployment (CI/CD) pipelines for automated builds, testing, and deployment.
7.	Pilot Testing & Iteration
•	Deploy the system in a small KALRO operational region for real-world testing.
•	Collect feedback from farmers and staff to refine service communication handling, fault tolerance, and user experience.
•	Iterate improvements in subsequent sprints until performance, reliability, and usability meet the acceptance criteria.
8.	Final Deployment & Knowledge Transfer
•	Roll out the fully integrated microservices system to all targeted KALRO regions.
•	Provide training to KALRO staff and documentation for system operation and maintenance.
                               

     <img width="1800" height="2492" alt="image" src="https://github.com/user-attachments/assets/569a718a-96d6-46ca-9f22-2833809352f1" />
  
Figure 2 Agile Planning


1.9 SCOPE.

This project is limited to the design, implementation, and evaluation of a microservices architecture aimed at addressing communication and coordination challenges in distributed systems, with the Kenya Agricultural and Livestock Research Organisation (KALRO) serving as the case study. The primary focus is on solving technical issues common in microservices—such as service discovery, message delivery reliability, fault tolerance, and scalability—rather than on general system digitization or organizational restructuring.
The system to be developed will consist of independent, loosely coupled services for request handling, enquiry tracking, notification delivery, authentication, and analytics. It will be accessible via mobile platforms, with provisions for low-connectivity areas through USSD/SMS integration. The project will cover:

•	Analysis of microservices communication challenges in the context of KALRO’s farmer–government interactions.

•	Design of a modular, fault-tolerant architecture incorporating asynchronous communication and resilience patterns.

•	Implementation of core services sufficient to demonstrate reliable inter-service communication and user request handling.

•	Testing under varied connectivity and load conditions to assess system reliability, scalability, and responsiveness.

•	Pilot deployment in a selected operational region for real-world evaluation.

The project will not cover:

•	Replacement or overhaul of KALRO’s existing back-office systems.

•	Development of unrelated agricultural management tools beyond the communication-focused microservices.

•	Large-scale deployment to all regions during the initial project phase.

The outcomes are intended to provide both a functional case-specific solution for KALRO and generalizable insights into deploying microservices effectively in low-resource, high-demand environments.





































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

<img width="468" height="551" alt="image" src="https://github.com/user-attachments/assets/b74bd0fa-7395-4956-afa9-9f07308b24f5" />

Table 1 Budget


C.	Project Duration

		
<img width="468" height="629" alt="image" src="https://github.com/user-attachments/assets/fd3e9d3d-d7b2-4187-a52d-c0437bb00ed7" />
	
Table 2 Gantt chart






























CHAPTER TWO

2.1 INTRODUCTION.

This chapter reviews existing literature relevant to the application of microservices architecture in solving communication and coordination challenges in distributed systems, with a focus on its potential use in improving agricultural service delivery. The review examines the conceptual foundations of microservices, the common technical issues associated with their implementation, and the strategies developed to address these challenges. It also considers the role of technology in enhancing farmer–government interactions, drawing on both global and Kenyan case studies to highlight practical lessons and gaps in current approaches.
The chapter is organised into thematic sections covering the evolution of software architectures from monolithic to microservices, key characteristics and advantages of microservices, common communication problems in distributed environments, and patterns or frameworks for achieving reliable inter-service communication. It further reviews existing IT solutions in agriculture, identifying where they succeed and where they fail in ensuring timely, reliable, and accessible communication for end-users. By synthesising these insights, this chapter provides the theoretical and practical grounding for designing the proposed microservices-based solution in the KALRO case study.

2.2 THEORETICAL REVIEW.

Microservices architecture is a software design paradigm in which an application is divided into multiple, small, independently deployable services that work together to form a complete system (Newman, 2015). Unlike monolithic architectures—where all functionalities are bundled into a single deployable unit—microservices allow each component to be built, deployed, and scaled independently. This project specifically focuses on asynchronous, event-driven microservices, which communicate through message queues or event streams rather than direct synchronous calls.
The theoretical foundation of microservices lies in the principle of modularity—a concept proposed by Parnas (1972)—which advocates breaking complex systems into smaller, more manageable modules with clear interfaces. In the microservices context, each module (service) is responsible for a specific business capability. This modularity supports faster development, independent scaling, and easier maintenance (Fowler & Lewis, 2014).
Asynchronous, event-driven microservices operate on the principle of loose coupling (Erl, 2005), where services interact indirectly through events or messages rather than direct API calls. This architecture enhances resilience and fault tolerance because the failure of one service does not immediately halt the functioning of others. Chappell (2009) describes this as event-driven architecture (EDA)—a pattern in which services publish events when something happens and other services subscribe to those events to act accordingly.
However, distributed communication in microservices introduces new challenges. According to Tanenbaum and Van Steen (2017), network-based interactions face latency, message loss, and partial failures. In the agricultural sector—particularly in rural areas with poor network stability—these issues can severely disrupt real-time communication. For instance, in the Kenya Agricultural and Livestock Research Organisation (KALRO) farming sector, delays or failures in message delivery between farmer-facing services and backend services can result in missed updates, delayed responses, and reduced trust in the system.
By applying asynchronous, event-driven microservices, the proposed approach aims to address these communication challenges by enabling non-blocking service interactions, ensuring that farmer queries, notifications, and updates are transmitted reliably, even under unstable connectivity conditions. This aligns with the broader theoretical goal of microservices: to build scalable, resilient, and loosely coupled systems that support complex organisational processes while maintaining flexibility.
. 




2.3 CASE STUDY REVIEW.

The Kenya Agricultural and Livestock Research Organisation (KALRO) operates a nationwide network that provides farmers with research findings, agricultural advice, and market information. However, the current communication systems within KALRO’s farming information services are largely centralised and partially monolithic, leading to delays in information dissemination, limited real-time interaction, and difficulties in scaling services for different regions.
Field assessments reveal that KALRO’s digital platforms—such as USSD services, SMS notifications, and web portals—often face challenges when processing and delivering updates to farmers simultaneously across multiple regions. These challenges stem from:
•	Synchronous dependency between modules, where a failure or delay in one service halts the entire communication process.
•	Limited scalability, making it hard to handle high message volumes during peak farming seasons (e.g., planting or harvesting).
•	Network instability in rural areas, which disrupts direct API calls between services.
Globally, similar agricultural organisations have adopted asynchronous, event-driven microservices to address such issues. For instance, the Indian Council of Agricultural Research (ICAR) implemented an event-based messaging platform that decouples the farmer communication interface from backend processing services. This allowed farmer queries to be queued and processed even during connectivity downtimes, improving reliability and trust.
In East Africa, the Uganda National Agricultural Advisory Services (NAADS) tested a message broker-based microservice approach to handle farmer queries. The system relied on event queues to store messages when connectivity was low, delivering them once a stable connection was available. This reduced communication delays by over 40% (NAADS Report, 2021).
For KALRO, adopting a similar asynchronous microservice architecture could ensure that messages between farmers, researchers, and support teams are delivered reliably and promptly. In practice, this would involve decoupling core modules (e.g., Farmer Query Service, Research Data Service, Notification Service) and integrating them via an event broker such as Apache Kafka or RabbitMQ. By doing so, the system would be resilient to partial failures and adaptable to Kenya’s variable network conditions, directly addressing the communication gap problem identified in the study.

2.4 INTERGRATION AND ARCHITECTURE.

The proposed system for improving farmer–KALRO communication leverages an asynchronous microservice architecture, integrating Africa’s Talking, Daraja API, MongoDB, and a Python-based server to ensure seamless, reliable, and scalable operations. The design addresses the communication gap by decoupling core services and enabling event-driven message handling.

2.4.1 Architectural Overview

The architecture consists of independent services that interact via a central message/event broker pattern implemented in Python. Each service is deployed as a standalone unit but integrated through the publish/subscribe approach.
Key Microservices:
1.	USSD/SMS Communication Service (Africa’s Talking)
o	Receives farmer requests and inputs via USSD or SMS.
o	Forwards requests as events to the Message Broker for processing.
o	Uses Africa’s Talking APIs to ensure compatibility with feature phones, making it accessible in rural areas.
2.	Payment Verification Service (Daraja API)
o	Integrates Safaricom’s M-Pesa for payment handling.
o	Operates independently from other services.
o	Publishes payment confirmation events to the broker, triggering order fulfilment or service access.
3.	Data Management Service (MongoDB)
o	Stores farmer profiles, KALRO research data, transaction logs, and communication records.
o	Subscribes to data update events and writes changes asynchronously.
o	Enables retrieval of historical interaction data for analytics.
4.	Notification Service
o	Listens for updates from other services (e.g., payment success, research advice ready).
o	Sends outbound messages to farmers via Africa’s Talking SMS API.
5.	Python Server (Backend Event Controller)
o	Acts as the orchestration layer managing event flow between services.
o	Implements the publish/subscribe and message queue logic.
o	Integrates with MongoDB, Daraja API, and Africa’s Talking simultaneously without creating direct service dependencies.

2.4.2 Integration Workflow

1.	Farmer Request Stage
o	A farmer dials the USSD code or sends an SMS.
o	Africa’s Talking forwards the request to the Communication Service in the Python backend.
2.	Processing Stage
o	The backend publishes the request as an event to the Message Broker.
o	Relevant services (e.g., Research Data Service, Payment Service) subscribe and process the request independently.
3.	Payment Handling
o	If payment is needed, the Payment Service triggers the Daraja API for M-Pesa checkout.
o	Upon success, it publishes a "payment confirmed" event.
4.	Response Stage
o	The Notification Service consumes the final output event and sends the response back via Africa’s Talking.
o	MongoDB logs the entire interaction for records.
2.4.3 Benefits of the Technology Stack
•	Africa’s Talking – Ensures farmers in rural areas can access the system without internet via USSD/SMS.
•	Daraja API – Provides secure, automated mobile money transactions without requiring manual processing.
•	MongoDB – Offers a flexible NoSQL database for storing diverse agricultural and communication data in real-time.
•	Python Server – Supports asynchronous event processing, making the system resilient to slow network conditions and individual service failures.
 <img width="1592" height="1592" alt="image" src="https://github.com/user-attachments/assets/ebd4ed97-3cc7-4e25-bc81-19edff2a1884" />

Figure 3 Microservice Architecture


2.5 SUMMARY.

This case study focuses on addressing microservice-specific challenges in farmer service platforms, particularly issues of service communication, fault tolerance, data consistency, and performance monitoring. While a microservices approach offers clear benefits such as scalability, flexibility, and easier integration with emerging technologies, it also brings significant complexities in coordinating distributed services, ensuring consistent data flow, and maintaining optimal system performance under varying loads. The proposed solution adopts a loosely coupled, resilient microservice architecture featuring an API Gateway for unified access, a Service Registry for dynamic service discovery, a Message Broker for asynchronous communication, containerization for deployment consistency, and robust monitoring tools to track performance and detect failures early. These design choices aim to enable independent service deployment, minimize downtime, improve fault isolation, and ensure the platform can evolve without major disruptions. Development follows the Agile methodology, emphasizing iterative sprints, continuous integration and deployment (CI/CD), and close stakeholder collaboration, ensuring rapid delivery of functional components, faster issue resolution, and long-term maintainability.

2.6 RESEARCH GAPS.

Optimized Communication Models – Limited research on low-latency, high-reliability communication frameworks tailored for microservices in resource-constrained or rural network environments.
Fault Tolerance in Agricultural Systems – Few studies address how microservices can recover from failures in farmer service platforms without disrupting ongoing transactions.
Data Consistency Across Distributed Services – Insufficient solutions for maintaining strong or eventual consistency when services span different databases and geographic regions.
Monitoring and Predictive Maintenance – Lack of predictive monitoring models that can proactively detect and resolve service degradation before it impacts end-users.
Cost-Efficient Scaling – Minimal exploration of scaling strategies that balance performance and operational costs, especially for systems with seasonal usage spikes.
Security and Compliance – Limited frameworks addressing microservice security in sensitive agricultural data handling, particularly in line with local regulations.






































References

Chappell, D. (2009). Enterprise Service Bus. O’Reilly Media.

Dragoni, N., Giallorenzo, S., Lafuente, A. L., Mazzara, M., Montesi, F., Mustafin, R., & Safina, L. (2017). Microservices: Yesterday, today, and tomorrow. Present and Ulterior Software Engineering, 195–216.

Erl, T. (2005). Service-Oriented Architecture: Concepts, Technology, and Design. Prentice Hall.

Fowler, M., & Lewis, J. (2014). Microservices. ThoughtWorks.

Newman, S. (2015). Building Microservices: Designing Fine-Grained Systems. O’Reilly Media.

Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. Communications of the ACM, 15(12), 1053–1058.

Tanenbaum, A. S., & Van Steen, M. (2017). Distributed Systems: Principles and Paradigms. Pearson.
.












CHAPTER 3: SYSTEM ANALYSIS AND DESIGN

3.1 INTRODUCTION

This chapter transitions from the theoretical discussion of the communication gap in microservices to the practical analysis and design of a tangible solution. Using the Kenya Agricultural and Livestock Research Organization (KALRO) farmer communication platform as a case study, this section outlines the architectural blueprint of the proposed system. The primary objective is to detail the methodologies and design principles employed to create a robust, scalable, and decoupled system that effectively bridges the communication challenges inherent in distributed architectures.
The core of the proposed solution is a microservices architecture where independent services communicate asynchronously. To address the central problem of inter-service communication, an event-driven, publish/subscribe model was selected. This approach, orchestrated by a central message broker, ensures that services remain loosely coupled, improving resilience and maintainability.
This chapter will systematically break down the system's design. It will begin by defining the functional and non-functional requirements derived from the case study's needs. Subsequently, it will present the high-level system architecture, detailing each microservice's role and responsibilities. The discussion will cover the design of the:

•	USSD/SMS Communication Service

•	Payment Verification Service

•	Data Management Service

•	Notification Service

Finally, the chapter will detail the data models, integration workflows, and the specific technologies chosen to implement this architecture. The following sections will provide a comprehensive overview of the system's design, beginning with the analysis of its core requirements.

 3.2 SYSTEMS DEVELOPMENT METHODOLOGY
 
In the development of the KALRO USSD application, an Agile Software Development Methodology was adopted. This methodology emphasizes iterative development, close stakeholder collaboration, and continuous feedback—key factors when building systems meant to be both user-centric and responsive to changing agricultural service needs.
Agile was chosen due to its suitability for projects where requirements are expected to evolve. Since the KALRO USSD app serves a wide demographic with varying literacy and technology exposure, iterative prototyping and constant user feedback loops were crucial in ensuring the final product was simple, functional, and effective.
The Agile process followed these phases:

1.	Planning and Requirement Gathering: Initial meetings with KALRO stakeholders were conducted to define the scope, major features, and target user groups of the system. This phase also involved outlining key deliverables like produce buying/selling, transport requests, and seed offers.
2.	Design Iterations: The USSD menu structure and backend logic were designed incrementally. After each iteration, feedback was gathered from mock users and KALRO personnel to refine menu flows, improve confirmation steps, and ensure logical navigation.
3.	Incremental Development: Using Flask for the backend and MongoDB for storage, features such as user registration, STK Push payment handling via Daraja, and purchase/sales data recording were implemented one at a time in weekly sprints. Each module was tested independently.
4.	Testing and Integration: Modules were integrated and tested as they were completed. Emphasis was placed on Daraja callback handling and maintaining seamless session states in USSD, especially during multi-step processes like payments and confirmations.
5.	Deployment and Feedback: The application was deployed in a testing environment for user trials. Feedback led to improvements in menu clarity, database schema adjustments, and the addition of features like transport requests.
The flexibility of Agile allowed the system to remain adaptable and responsive, especially when KALRO requested enhancements to menu flows or changes in pricing structures for different produce items. It also ensured that stakeholder input was incorporated continuously throughout development, increasing the likelihood of adoption and usability among rural farmers.

3.3 FEASIBILITY STUDY

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

3.4 REQUIREMENTS ELICITATION

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

3.5 DATA ANALYSIS
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


<img width="468" height="197" alt="image" src="https://github.com/user-attachments/assets/908a05b2-4663-4d90-b2f4-47f37dc12675" />


Table 3 Data Entities and Attributes
These entities were further used to define MongoDB collections such as users, purchased, sales, and admins.

3.5.4 Workflow Insights

•	Sequential menu navigation was preferred over branching to reduce confusion.

•	Users often abandon sessions if required to enter long text, favoring numeric options.

•	Confirmation prompts reduced transaction errors and improved user trust.

The insights gained during data analysis provided the basis for modeling the system’s flow, database structure, and interface logic, all tailored for efficiency and usability.

3.6 SYSTEM SPECIFICATION

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

<img width="468" height="371" alt="image" src="https://github.com/user-attachments/assets/8665cbfe-e60f-4f27-adc2-585ddb09417f" />


Table 4 Non-Functional Requirements
The above specifications ensure that the KALRO USSD system meets the intended goals of accessibility, reliability, and ease of use for farmers, while remaining manageable and insightful for KALRO administrators.

3.7 REQUIREMENTS ANALYSIS AND MODELING

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

<img width="468" height="204" alt="image" src="https://github.com/user-attachments/assets/7b996a8c-6052-4feb-b802-df22798fb5a7" />


Table 5 Modules
Each module is implemented as a Flask route (or endpoint) and interacts with MongoDB collections like users and purchased.

3.7.3 Modeling Diagrams

To further clarify and visualize system behavior, several modeling diagrams were used:

A. Use Case Diagram
 <img width="1950" height="1950" alt="image" src="https://github.com/user-attachments/assets/a382a48c-fecf-4bc7-ac81-10a2778dedff" />

Figure 4 Use Case














B. Data Flow Diagram (DFD) 

 <img width="1950" height="1950" alt="image" src="https://github.com/user-attachments/assets/98cf9cf3-941b-424a-aeff-715d634ffea7" />
Figure 5 Data Flow Diagram





C. Conceptual Class Diagram 

 <img width="1950" height="1866" alt="image" src="https://github.com/user-attachments/assets/b734b5ff-4c2e-48bf-b5f3-6427dbb4002e" />

Figure 6 Class Diagram
	These diagrams and the modular structure ensured that the development team could clearly understand the expected system functionality and interactions. They also served as documentation references during testing, debugging, and stakeholder reviews.


3.8 LOGICAL DESIGN

This section outlines the logical design of the KALRO USSD Application. It captures the core structure, behavior, and functionality of the system using high-level architectural and flow models. The logical design serves as a blueprint for the implementation phase.

3.8.1 System Architecture

The KALRO USSD Application adopts a client-server architecture, where the mobile user acts as the client, and the back-end system (server) processes requests and returns appropriate responses.
The client is the farmer's feature phone. It is the device that initiates a request, either by dialing a USSD code or sending an SMS. The client's role is to send data to the server and display the response it receives. It acts as the entry point for all farmer interactions.
The Server
The server is the entire microservices architecture that resides in the backend. It's not a single machine but a distributed system of interconnected services. The server's role is to receive the client's request, process it, and generate an appropriate response. This is where all the business logic, payment handling, data storage, and notification management takes place.
The Interaction Flow
The client-server interaction is a simple request-response cycle:

1.	Request: A farmer sends a request from their phone (the client).
2.	Processing: The request is received by the USSD/SMS Communication Service (part of the server), which then triggers the event-driven workflow you designed.
3.	Response: The Notification Service (also part of the server) sends the final output back to the farmer's phone (the client) as an SMS or USSD session response.

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

<img width="1950" height="1950" alt="image" src="https://github.com/user-attachments/assets/23059349-5fa6-463b-81a1-c58e38586c54" />
 
Figure 7 Client-Server

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

 <img width="1356" height="2034" alt="image" src="https://github.com/user-attachments/assets/32e0ddfa-dd19-4764-8ffd-ee6fc4d1762b" />

Figure 8 Sequence Diagram



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
 <img width="1372" height="2588" alt="image" src="https://github.com/user-attachments/assets/f0dba2df-689f-4091-9ea2-b4ce841c2c51" />

Figure 9 Activity Diagram
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

3.9 PHYSICAL DESIGN

This section presents the physical design of the KALRO USSD application. It includes decisions and specifications regarding the actual technologies and platforms used, with emphasis on the database, user interfaces, and system integration components.

3.9.1 Database Design

Database Management System (DBMS):
•	MongoDB (NoSQL) – chosen for its flexibility, scalability, and ability to store semi-structured data.
Database Schema (Collections & Fields):

Collection	Fields

<img width="468" height="143" alt="image" src="https://github.com/user-attachments/assets/8b8fc954-5a91-45ab-8df0-50d682987fd9" />


Table 6 Database Schema

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

<img width="468" height="408" alt="image" src="https://github.com/user-attachments/assets/a73ac6cf-f0d1-4780-b7e0-f326e2be43fc" />

Table 7 Input and Output forms

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

     <img width="1131" height="1697" alt="image" src="https://github.com/user-attachments/assets/5d49bfae-2df4-457d-b0ff-40094b4e73e8" />
            
Figure 10 Wireframe







CHAPTER 4: SYSTEM IMPLEMENTATION AND TESTING,
CONCLUSIONS AND RECOMMENDATIONS

4.1 INTRODUCTION

This chapter describes the implementation environment, tools used, and testing processes for the KALRO USSD application. It also presents conclusions and recommendations drawn from the system development lifecycle.
The goal of the system is to provide an accessible mobile-based platform for farmers, agro-dealers, and researchers to interact with KALRO services via USSD, even in low-bandwidth regions. A layered architecture was adopted, encompassing the backend logic, middleware (USSD gateway), and a cloud-hosted NoSQL database.

4.2 ENVIRONMENT AND TOOLS

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

4.3 SYSTEM CODE GENERATION

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

4.4 TESTING

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

<img width="468" height="242" alt="image" src="https://github.com/user-attachments/assets/e35d1592-da54-4d0f-84a6-eab6aa5f4a43" />


Table 8 Test Suite and Tools














4.4.3 Sample Test Cases and Results


<img width="468" height="308" alt="image" src="https://github.com/user-attachments/assets/7c2b0c4d-8cef-4dc3-b8c9-487e5a673205" />


Table 9 Test Results

4.4.4 Screenshots of Tests 
    <img width="579" height="1018" alt="image" src="https://github.com/user-attachments/assets/cb460ae2-2d00-45a4-ab49-edae0f13757a" />
    <img width="605" height="1029" alt="image" src="https://github.com/user-attachments/assets/ff02a80b-1fa7-4c37-b49d-e50bc17ba456" />
    <img width="608" height="1034" alt="image" src="https://github.com/user-attachments/assets/867fe927-2600-401c-a08c-59f544f62b67" />
    <img width="633" height="1054" alt="image" src="https://github.com/user-attachments/assets/9af95b71-e868-4623-b8b5-3befedbdcc75" />
    <img width="619" height="1030" alt="image" src="https://github.com/user-attachments/assets/55aab177-d771-47ee-814a-964f977ce4db" />
    <img width="523" height="930" alt="image" src="https://github.com/user-attachments/assets/bb78d177-4acd-4d97-90eb-4d3c34ade84c" />

Figure 11 Screenshots
   

4.5 USER GUIDE
This section provides step-by-step instructions on how users interact with the KALRO USSD system. It covers registration, login, buying and selling produce, accessing offers, and making transport requests.

1. Accessing the System
•	Dial the USSD code *384*79300# on any mobile phone.
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

4.6 CONCLUSIONS

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

4.7 RECOMMENDATIONS

Improvements for the Microservices Architecture:
Decoupled Language Support: Instead of modifying the existing USSD/SMS Communication Service to handle multilingual text, a new, dedicated Translation Microservice should be implemented. This service would subscribe to incoming events, translate relevant text, and publish a new event with the localized content. This keeps the core communication service lean and allows the system to easily add more languages in the future without redeploying other services.

Specialized Transport Service: To expand the transport features (timelines, driver information, tracking), a new, dedicated Transport Management Service should be created. This service would be responsible for all logistics. It would subscribe to "order_fulfilled" events, manage the transport details, and then publish "transport_assigned" or "delivery_scheduled" events. The Notification Service would then subscribe to these new events to send the appropriate updates to the farmer, maintaining the principle of single responsibility.

Dedicated Analytics and Security Microservices: The enhanced admin dashboard features should be powered by new, independent services. An Analytics and Reporting Service would subscribe to all relevant events from the Message Broker and process them to provide data for the dashboard. This offloads resource-intensive reporting queries from the primary Data Management Service. Similarly, features like rate limiting and security logging should be managed by a dedicated API Gateway and a Logging Service, which can protect the core services and provide centralized security monitoring without adding complexity to the business logic of each service.

Transaction Reliability: The automated handling and monitoring of STK Push failures should be handled internally by the Payment Verification Service. This service would be enhanced to listen for failure events from the Daraja API. When a failure is detected, the service would publish a specific "payment_failure" event to the Message Broker. The Notification Service would then subscribe to this event and send an appropriate message to the farmer, ensuring transactional reliability is managed within the responsible service.
Infrastructure for Scalability: The recommendation to migrate to a production-grade USSD gateway is an architectural improvement focused on the USSD/SMS Communication Service. The core logic of the microservice would remain the same, but the integration layer would be upgraded to ensure it can handle increased traffic and maintain compatibility across different carriers, which is crucial for scalability in a microservices environment.

