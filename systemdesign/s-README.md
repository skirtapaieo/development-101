# System Designs

- Exchanges - end-customers meet exchanges (betting and stocks and so on)
- Human Resources (employee perspective) - for developer interview preparation - Algoexpert platform (from Algoexpert exercise)
- Code - Code Deployment system (from Algoexpert exercise)
- Social - Feed-based system (from Algoexpert exercise)
- Streaming - Spotify (from Youtube/iGotanOffer)

- [Global and Fast Code Deployment system - from Algoexpert](#1-code-deployment-system)

## Twitch

## Airbnb

## Slack

## Tinder

## Uber

## Netflix

## Google Drive

## Reddit

/Reddit - post, comments, vote, awards

## Amazon (e-commerce)

/Amazon - e-commerce

## Exchanges - Stock Exchange

/Exchange - a lot of architecture, complexity in real-time protocol, and matching/settling order. Two cases, from iGaming, where we in one case use Cinnobers trading, one were we built it ourselves

<br>

## Algoexpert platform

### Clarifying questions

- Functional.
  - Are we designing the full platform or a part? (functionality/use cases) Only the core user flow where you end up at the website, going through questions, marking "questions" as complete or in progress, writing running code in various languages, the code will be tested and you either get ok or no
  - In the algoexpert part, there are content parts, but there is also an **engine of some kind that manages 9 languages**, test cases, etc, that seems to be the core of the platform.
  - It is a content platform, but How many changes/week? . A few every week, so not a large issue. Most likely the work on every course, the video content and so ...
- Non-functional
  - Load from users? 100,000 visits from users/week
  - Availability? not a big problem ...
  - performance? feel responsive ...

#### Additional questions

Sure, let's look at AlgoExpert's current design as of my knowledge cutoff in September 2021 to provide the best responses to these questions. Please note, the platform may have evolved since then, and my answers may no longer reflect the current state of the platform.

| Category                         | Questions                                                                                                                   | AlgoExpert's Current Implementation                                                                                                                                                                                  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User Requirements                | 1. Who exactly are we building this platform for?                                                                           | AlgoExpert is primarily targeted towards software engineering candidates preparing for technical interviews.                                                                                                         |
|                                  | 2. What kinds of content and features should the platform have?                                                             | AlgoExpert offers a comprehensive set of coding interview problems, video explanations, and text-based solutions.                                                                                                    |
|                                  | 3. What level of difficulty should the coding questions have?                                                               | AlgoExpert covers a wide range of difficulty levels, catering to users at different stages of their preparation.                                                                                                     |
|                                  | 4. What types of instructional materials should we include?                                                                 | AlgoExpert provides both video explanations and text-based solutions for each problem.                                                                                                                               |
|                                  | 5. Which programming languages should we support?                                                                           | As of September 2021, AlgoExpert supports several popular programming languages including Python, JavaScript, Java, C++, C#, and more.                                                                               |
|                                  | 11. Should the platform provide features to track a user's progress over time?                                              | AlgoExpert offers a progress tracker to help users keep track of their progress through the problem set.                                                                                                             |
|                                  | 12. How will the platform ensure accessibility and inclusivity for users of different backgrounds and with different needs? | AlgoExpert ensures accessibility by providing text-based solutions in addition to video explanations. Further details specific to inclusivity and accessibility initiatives were not available as of September 2021. |
| Product Design and Functionality | 6. What should the user interface look like?                                                                                | AlgoExpert has a user-friendly interface with a built-in code editor where users can write, test, and debug their code.                                                                                              |
|                                  | 7. How will users' solutions be evaluated?                                                                                  | AlgoExpert provides automated test cases that users can run against their code for immediate feedback.                                                                                                               |
|                                  | 8. Should the platform include features for users to collaborate with each other?                                           | As of September 2021, AlgoExpert does not include features for direct user collaboration such as forums or chat rooms.                                                                                               |
| Business Model                   | 9. What should the platform's subscription model be?                                                                        | AlgoExpert operates on a paid subscription model. They offer a one-time payment for lifetime access to their resources as of September 2021.                                                                         |
| Technical Requirements           | 10. How do we plan to scale the platform as the user base grows?                                                            | Specific details on AlgoExpert's scaling strategies are not publicly available. However, being a web-based platform, they likely use scalable cloud infrastructure.                                                  |
| Security and Privacy             | 13. What considerations should we make to ensure the platform is secure and respects user privacy?                          | AlgoExpert has a privacy policy in place that details how they collect, use, and protect user data. They likely follow industry standard security practices to protect their platform and user data.                 |

### The coding platform

| Feature                   | HackerRank's CodeChecker   | JDoodle        | Sphere Engine   | Glot.io       | CompileBox    | Remoteinterview.io  |
| ------------------------- | -------------------------- | -------------- | --------------- | ------------- | ------------- | ------------------- |
| Sandboxing                | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Multiple Languages        | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Resource Limitations      | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Input/Output Handling     | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Error Handling            | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Evaluation                | No\*                       | No\*           | No\*            | No\*          | No\*          | No\*                |
| Scalability               | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| ------------------------- | -------------------------- | -------------- | --------------- | ------------- | ------------- | ------------------- |
| Total 'Yes' Counts        | 6                          | 6              | 6               | 6             | 6             | 6                   |

\* While these services handle code execution, they typically do not perform evaluation of the solution against a set of test cases. That part usually needs to be managed by your platform - you would call their API to run the code and then evaluate the output yourself.

As for guessing which platform AlgoExpert is using, it's a tough call without insider knowledge. As an AI model trained by OpenAI, I don't have access to real-time or proprietary data.

As of my last training cut-off in September 2021, AlgoExpert hasn't publicly stated which method they use. It's plausible they could have developed their own in-house solution given their scale and specific requirements. The advantage of an in-house solution is that it allows for full control over the environment, including customization and scaling based on their particular needs.

If they're using a third-party service, it would likely be one that offers robust features and wide language support, but it's impossible to say definitively which one. Please reach out to AlgoExpert directly for the most accurate information.

### Description of the areas

A coding execution environment is the server-side component where the user-submitted code is actually executed and evaluated. It is also known as a code execution engine. Here's a more detailed look at the process and considerations involved in setting up this environment:

1. **Sandboxing:** One of the most critical aspects of the code execution environment is sandboxing, which is a security mechanism for separating running programs. It isolates the user-submitted code execution in a separate environment to ensure that any malicious code doesn't harm your system or access sensitive data.

2. **Supporting Multiple Languages:** The environment needs to support all the programming languages you plan to offer on your platform. This involves installing the required compilers or interpreters for each language on your server and creating a system that selects the correct one based on the user's chosen language.

3. **Resource Limitations:** User-submitted code can potentially consume a lot of system resources or even fall into an infinite loop. To prevent a single user from consuming all your server resources, you need to impose limitations on execution time, memory usage, and possibly other resources like disk usage or network access.

4. **Input and Output Handling:** The environment needs to provide the input data to the user's code and capture the output for evaluation. This might involve setting up a file system in the sandbox environment or redirecting the standard input/output streams of the code execution process.

5. **Error Handling:** If the user's code has an error, you need to capture this and provide helpful feedback. This involves capturing compiler/interpreter error messages and exceptions thrown during execution.

6. **Evaluation:** After running the code, you need to compare the output to the expected output to determine if the solution is correct. This might be as simple as a string comparison, or it might involve some more complex logic if there are multiple valid solutions.

7. **Scalability:** Depending on the number of users and the complexity of the problems, code execution could be a very resource-intensive task. You need to design your environment with scalability in mind. This could involve distributing the load across multiple servers, using cloud services that can auto-scale based on load, or queuing code execution tasks and processing them in the background.

If building such an environment sounds too complex or resource-intensive, there are third-party services like JDoodle, Sphere Engine, or HackerRank's CodeChecker that provide APIs for running code in multiple languages. These services handle all the complexities mentioned above and can save you a significant amount of development time and resources. However, they come with ongoing costs and the risk of relying on a third-party service.

Whether you choose to build your own environment or use a third-party service largely depends on your specific requirements, resources, and risk tolerance. Both options have their pros and cons and should be carefully considered.

### A list of platforms

1. [HackerRank's CodeChecker](https://www.hackerrank.com/)
2. [JDoodle](https://www.jdoodle.com/)
3. [Sphere Engine](https://www.sphere-engine.com/)
4. [Glot.io](https://glot.io/)
5. [CompileBox](https://github.com/remoteinterview/compilebox)
6. [RemoteInterview.io](https://www.remoteinterview.io/)

Platforms like Palm or GTP would be a supplement to these platforms.

## Spotify

Table of Contents/Index:

- [Product and UX perspective (out of scope)](#product-and-ux-perspective-out-of-scope)
- [Requirements/goals (start for it)](#requirementsgoals-start-for-it)
- [System components](#system-components)
- [Data "pipeline"](#data-pipeline)
- [Music streaming is central](#music-streaming-is-central)
- [Infrastructure (end-to-end)](#infrastructure-end-to-end)
- [IoT perspective](#iot-perspective)
- [Front-end perspective / microservices](#front-end-perspective--microservices)
- [Product requirements](#product-requirements)
- [UX](#ux)

#### Product and UX perspective (out of scope)

- User research
- Product requirements
- UX design principles
- Wireframing and prototyping
- User testing and iterations
- Implementation and evalution

--> focus is 1) finding and playing music

### Requirements/goals (start for it)

- Users: 1 billion
- Lists: 10 billion
- Songs: 100 million
- Artists: 1 million
- Albums: 10 million

- Search for the above
- Create, share, follow playlists
- System recommends songs/artists/lists

### System components

1. User management
2. Music metadata management
3. Music/Podcast audio management
4. Search service
5. Music streaming service
6. Recommendation service
7. Analytics service

### Data "pipeline"

Here's a table that outlines a possible data pipeline for Spotify using AWS services:

| Stage                              | AWS Service                                          | Purpose                                                                                                                                                                   |
| ---------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Ingestion                     | Amazon Kinesis Data Streams or Kinesis Firehose      | To handle the real-time streaming data from various sources such as user activities.                                                                                      |
| Operational Data Storage           | Amazon RDS / Amazon DynamoDB / Amazon S3             | RDS for structured data like user profiles, song metadata. DynamoDB for semi-structured data like playlists. S3 for storing music files.                                  |
| Analytical Data Storage            | Amazon Redshift                                      | A data warehouse service that is used for analytical processing, which is optimized for aggregation and read-heavy workloads.                                             |
| Batch Processing                   | Amazon EMR                                           | Managed Hadoop framework to process vast amounts of data across scalable Amazon EC2 instances.                                                                            |
| Stream Processing                  | Amazon Kinesis Data Analytics                        | To process and analyze streaming data in real-time.                                                                                                                       |
| ETL                                | AWS Glue                                             | Fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load data for analysis.                                                        |
| Data Analysis and Machine Learning | Amazon Athena / Amazon QuickSight / Amazon SageMaker | Athena for interactive query service. QuickSight for visualization. SageMaker for building, training, and deploying machine learning models.                              |
| Data Serving                       | AWS Lambda / Amazon API Gateway                      | Lambda for running your code (for example, to generate recommendations) without provisioning or managing servers. API Gateway for creating, deploying, and managing APIs. |

Note: This is a high-level overview and actual implementation may involve additional services based on the specific needs and constraints. Also, while AWS offers comprehensive services, other cloud providers like Google Cloud and Azure offer similar services and can also be used to implement the data pipeline.

### Music streaming is central

Music streaming is a critical feature for an application like Spotify, and it needs to be highly efficient to provide a smooth user experience. There are several aspects to consider:

1. **Audio File Compression:** The raw audio files are large, so they're compressed to make them more manageable for streaming. Spotify uses Ogg Vorbis and AAC for audio compression. The streaming quality can be adjusted based on the user's preference and network condition.

2. **Content Delivery Network (CDN):** Spotify uses a CDN to deliver music streams to users. A CDN is a network of servers distributed across various locations around the world. When a user requests a song, it is served from the nearest server in the CDN. This reduces the latency and improves the streaming experience. AWS CloudFront could be an example of a CDN in an AWS-based architecture.

3. **Caching:** Frequently accessed songs can be cached at various levels (CDN, Spotify backend servers, user's device) to reduce the load on the servers and decrease the latency.

4. **Adaptive Streaming:** The streaming quality can be dynamically adjusted based on the network condition. If the network is slow, the server can switch to a lower bitrate stream to avoid buffering. This requires encoding the song in multiple bitrates and switching between them as needed.

5. **Pre-fetching:** Spotify uses a technique called pre-fetching where it predicts the next song the user is likely to play (like the next song in the playlist) and starts buffering it in advance. This reduces the perceived latency when the song is actually played.

6. **Load Balancing:** Load balancers are used to distribute the network traffic evenly across multiple servers. This helps in efficiently handling large numbers of concurrent streaming requests.

7. **Fault Tolerance and Redundancy:** The system should be designed to be fault-tolerant and have redundancies in place. If one server or data center fails, the requests should automatically be routed to another healthy server or data center.

8. **Offline Playback:** Spotify also allows users to download songs for offline playback. This helps in situations where the network connection is slow or unavailable.

These are some of the techniques to manage highly efficient music streaming. It's a complex problem involving various trade-offs, and the actual implementation may vary based on the specific needs and constraints.

### Infrastructure (end-to end)

Building a global streaming service like Spotify involves careful planning and consideration of various infrastructure components. This requires a multi-region, globally distributed setup to ensure low latency and high availability. Let's discuss the various components and how they could be deployed using AWS:

1. **Front-End:** The front-end includes the client applications that users interact with. This could be the web app, desktop app (Windows, MacOS), and mobile apps (Android, iOS). These applications interact with the backend services over the internet, and users could be located anywhere in the world.

2. **Backend Services:** The backend services could be built as microservices, each responsible for a specific function (User Management, Music Streaming, Playlist Management, Search, Recommendation, etc.). These services can be deployed on AWS EC2 instances or use a serverless approach like AWS Lambda. To manage these services, you can use an orchestration service like AWS ECS or EKS.

3. **Global Load Balancer:** AWS Route 53 (DNS service) along with AWS Global Accelerator can help direct user requests to the nearest location with the lowest latency. These services route users to the nearest AWS edge location and from there, the traffic is routed via Amazon's backbone network to the backend services, ensuring low latency.

4. **Multi-region Deployment:** The backend services should be deployed in multiple AWS regions around the world. This ensures that the services are located closer to the users, reducing latency. Also, if one region fails, the traffic can be redirected to another region, ensuring high availability.

5. **Data Storage:** Data storage should also be multi-region. User data can be stored in Amazon RDS (relational data) and Amazon DynamoDB (NoSQL data), both of which support multi-region deployment. Music files can be stored in Amazon S3, which also supports cross-region replication.

6. **Data Pipeline:** For the data pipeline, you can use Amazon Kinesis for real-time data streaming, AWS Glue for ETL, Amazon Redshift for the data warehouse, and Amazon QuickSight for visualization. These services can be deployed in multiple regions as needed.

7. **Content Delivery Network (CDN):** Amazon CloudFront, a global CDN service, can be used to deliver music files to users. It caches the content at the edge locations closer to the users, reducing latency.

8. **Security:** Security is crucial when dealing with user data. AWS provides various services and features to help with this, like IAM for access control, Security Groups and NACLs for network security, KMS for encryption, etc.

9. **Monitoring and Logging:** Services like Amazon CloudWatch and AWS X-Ray can be used for monitoring the system and troubleshooting any issues.

This is a high-level overview of the end-to-end infrastructure for a global music streaming service like Spotify. The actual implementation could vary based on the specific needs and constraints. Remember, building such a system involves dealing with a lot of complexities and challenges like data consistency across regions, handling network partitions, dealing with regulatory and compliance requirements for storing user data, etc.

### IoT perspective

While Spotify itself isn't an Internet of Things (IoT) device, it does have integrations with various IoT devices. Here are a few examples:

1. **Smart Speakers:** Spotify can be streamed on smart speakers such as Amazon Echo, Google Home, Apple HomePod, and others. Users can control Spotify playback on these devices using voice commands.

2. **Smart TVs:** Many Smart TVs come with the Spotify app pre-installed or allow it to be installed. Users can listen to Spotify directly from their TV.

3. **Car Systems:** Spotify can be integrated with the infotainment systems in many cars. For example, Spotify is compatible with Apple's CarPlay and Google's Android Auto.

4. **Smart Watches:** Devices like the Apple Watch or certain models of Fitbit support Spotify, allowing users to control playback or even download music for offline listening directly from their wrist.

5. **Smart Displays:** Devices like the Google Nest Hub or Amazon Echo Show can display the Spotify interface and play music, controlled by voice or touch.

6. **Game Consoles:** Devices like Xbox and PlayStation have Spotify apps that allow users to stream music while they're playing games.

7. **Connected Home Devices:** Some connected home devices, like Samsung's Family Hub refrigerator, also support Spotify.

In each of these cases, Spotify isn't running the IoT side of things - they've simply created versions of their app that work on these different devices, or they've allowed these devices to control the Spotify app on a connected phone or computer. So, while Spotify isn't an IoT company per se, it's certainly part of the IoT ecosystem.

### Front-end perspective / microservices

1 - front-end platforms - Assumes there will be a a front-end, the organization is built to enable them to be autonomous, using fine-grained components

### Product requirements

2 - Music streaming

3 - Discoverabilty

4 - Playlists

5 - Social features

6 - Offline mode

7 - Multiple platforms

### UX

8 - Simplicity

9 - Consistency

10 - Personalization

11 - Feedback and error handling

12 - Accessibility

- Wireframing
- Prototyping
- User testing/iteration
- Implementation/evaluation

## News feed (facebook)

### Initial questions related

#### Key concepts?

- User-Generated Content (UGC): All these platforms rely heavily on content created and shared by their users.

- Algorithmic Content Delivery: They all use algorithms to decide what to show in a user's feed based on factors like past user behavior, network connections, user preferences, trending topics, etc.

- Social Interaction: Each of these platforms facilitates social interaction, allowing users to like, comment on, share, and interact with the content that they see.

- Real-time Updates: All of these platforms provide near-real-time updates, with new content appearing in the feed as it is posted.

- Customization: They all offer the ability for users to customize their feeds to some extent, based on who they follow or what topics they're interested in.

- Ad-based Revenue Model: They all generate revenue by showing targeted ads to users based on their behavior, interests, and demographics.

#### Example platforms

| Platform  | Content Focus                              | Unique Features                                                                                                                                  |
| --------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Spotify   | Music and podcasts                         | User follows artists, playlists, or friends to get updates and recommendations; "Discover Weekly" playlist.                                      |
| Facebook  | Mixed (text, photos, videos, links)        | Combines updates from friends, groups, pages; features for private messaging, groups, and events.                                                |
| Instagram | Photo and video                            | Aesthetic appeal; photo filters; Instagram Stories, IGTV, and Shopping.                                                                          |
| Twitter   | Text (also supports images, videos, links) | Character limit encourages concise messaging; real-time updates on current events; trending topics and hashtags.                                 |
| TikTok    | Short-form video                           | Users can create and share videos up to 60 seconds long; viral dance challenges; educational content; powerful content recommendation algorithm. |

#### Functionality needed?

- Account Management
- User Profile
- Posts an Content Sharing
- Feed and content discovery
- Social interactions
- Messaging
- Groups and pages
- Privacy and security
- Accessibility and usability
- Ad display

#### Main stakeholders

- End-users
- Advertiseras
- Content createors
- Employees and developers
- Regulatory authorities
- Partners
- Community and society at large

#### Initial services

- User Service: This handles user-related operations and stores user profiles, including the list of friends for each user.

- Feed Service: This is responsible for creating, storing, and retrieving feed data. Each user's feed is generated by pulling status updates from their friends and running them through a ranking algorithm.

- Real-Time Update Service: This service pushes real-time updates to users' feeds. When a user posts a status update, the Real-Time Update Service ensures that it's quickly propagated to their friends' feeds.

- Ranking Service: This service takes a list of relevant posts and ranks them to generate a user's news feed.

- Ads Service (optional): If ads are incorporated, this service will determine what ads to show to a user at any given time.

#### Sequence diagram - ver 1.0

![Feed sequence diagram](https://github.com/skirtapaieo/system-design-101/blob/main/feed-seq-diagram.png)

https://github.com/skirtapaieo/system-design-101/blob/main/feed-seq-diagram.png

´´´
@startuml
actor User
participant "User Service" as US
participant "Feed Service" as FS
participant "Ranking Service" as RS
participant "Real-Time Update Service" as RTUS

User -> US : Login
US -> FS : Request Feed
FS -> US : Get Friends
US -> FS : Return Friends
FS -> FS : Get Status Updates from Friends
FS -> RS : Rank Updates
RS -> FS : Return Ranked Updates
FS -> US : Return Feed
US -> User : Display Feed

User -> US : Post Status Update
US -> FS : Add Status Update
FS -> RTUS : Publish Update to Friends
RTUS -> FS : Update Friends' Feeds
@enduml
´´´

#### Non-functional requirements

- Scalability: Given the large number of users (100 million daily users, 1 million daily status updates), the system needs to be scalable. We could use a distributed database system and implement sharding and partitioning strategies to distribute data and load across multiple servers.

- Feed Generation/Refreshing: For feed generation, consider a pull model where feeds are generated when users log in or refresh their feeds. Given that we want new posts to show up quickly, it's important to optimize the feed refreshing process. Caching can also be used to improve feed load times.

- Data Persistence: To ensure that posts don't disappear, we need a robust data persistence strategy. This could involve database replication to protect against data loss if a single machine fails. Use of a distributed database with replication and failover mechanisms can help here.

- Real-Time Updates: Given the requirement for fast propagation of new posts, using a publish-subscribe model for real-time updates could be a good solution. When a user posts a status update, a message is published to a topic, and all of the user's friends who are subscribed to that topic receive the message.

- Global Audience: Given the global audience, latency and data locality should be considered. Users should be served from the nearest data center where possible. This can be achieved with a geo-distributed database and Content Delivery Network (CDN).

- Ads Integration (optional): If ads are incorporated, they could be treated as special types of posts that get inserted into the feed by the Ads Service and then ranked along with regular posts by the Ranking Service.

#### Sequence diagram ver 2 - with notes related to non-functional ideas

![Feed sequence diagram](https://github.com/skirtapaieo/system-design-101/blob/main/feed-seq-diagram-NFR.png)

https://github.com/skirtapaieo/system-design-101/blob/main/feed-seq-diagram-nfr.png

´´´
@startuml
actor User
participant "User Service" as US
participant "Feed Service" as FS
participant "Ranking Service" as RS
participant "Real-Time Update Service" as RTUS

User -> US : Login
US -> FS : Request Feed
note over FS : Scalability: Distributed database for user feeds
FS -> US : Get Friends
US -> FS : Return Friends
FS -> FS : Get Status Updates from Friends
FS -> RS : Rank Updates
RS -> FS : Return Ranked Updates
note over FS : Real-Time Updates: New posts propagate quickly
FS -> US : Return Feed
US -> User : Display Feed

User -> US : Post Status Update
note over US : Data Persistence: Status updates confirmed to user are reliably stored
US -> FS : Add Status Update
FS -> RTUS : Publish Update to Friends
RTUS -> FS : Update Friends' Feeds
@enduml

´´´

<br>

#### Requriements for each service

| Service                  | Description and Load                                                                                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User Service             | Handles user-related activities like authentication, profile edits, etc. Expected to handle millions of requests per day. Manages profile info and friend lists for 100M daily users.  |
| Feed Service             | Responsible for serving user feeds and processing status updates. Expected to handle billions of requests per day. Manages potentially 50B+ daily posts.                               |
| Ranking Service          | Handles the ranking of posts for user feeds. Expected to handle hundreds of millions to billions of ranking requests daily. Manages large amounts of metadata associated with ranking. |
| Real-Time Update Service | Responsible for processing and propagating real-time status updates to relevant user feeds. Expected to handle 500M update events daily. Manages large volumes of real-time data.      |

#### Requirements from post to ...

- ~10 KB per post
- ~1000 posts per news feed
- ~1 billion news feeds
- ~10 KB _ 1000 _ 1000^3 = 10 PB = 1000 \* 10 TB

#### Algoexpert system diagram

https://github.com/skirtapaieo/system-design-101/blob/main/facebook-system-diagram.svg

## Code-deployment system

design a code deployment system (part of exercise at Algoexpert/System design)

# Index

- [System design](#system-design)
- [The initial questions](#the-initial-questions)
- [Detailed system design questions](#detailed-system-design-questions)
  - [Scope and Scale](#scope-and-scale)
  - [Target Environments](#target-environments)
  - [Security Requirements](#security-requirements)
  - [Versioning and Rollbacks](#versioning-and-rollbacks)
  - [Deployment Workflow](#deployment-workflow)
  - [Monitoring and Logging](#monitoring-and-logging)
  - [Network and Infrastructure](#network-and-infrastructure)
  - [Compliance and Governance](#compliance-and-governance)
  - [Integration and Compatibility](#integration-and-compatibility)
  - [Team and Roles](#team-and-roles)
- [First pass of the system design](#first-pass-of-the-system-design)
  - [Global Deployment](#global-deployment)
  - [Deployment Frequency and Rollbacks](#deployment-frequency-and-rollbacks)
  - [Uptime and Performance](#uptime-and-performance)
  - [Integration with Code Reviews and Build Systems](#integration-with-code-reviews-and-build-systems)
  - [Automation and Orchestration](#automation-and-orchestration)
  - [Monitoring and Alerting](#monitoring-and-alerting)
  - [Security and Access Control](#security-and-access-control)
  - [Training and Documentation](#training-and-documentation)
- [The system overview](#the-system-overview)

# System design (result of below)

![Alt text of the image](https://github.com/skirtapaieo/codedeployment/blob/main/systemdesign.png)

# The initial questions

- The first questions is of course buy or build, but for the point of the exercise we will ask the questions needed for a design, and a later implementation.
- The second questions is whether this suits the company and the overall architecture and
- whether the resources are in place to, after the design, actually be able to build the system.

As shown later in the design phase, it is pretty complicated.

# Detailed system design questions

The following, and other questions will help us to understand the specific requirements and constraints of the code-deployment system, enabling you to design a solution the meets the needs of the organisation.

## Scope and Scale

- How many locations or regions will the system need to support globally?
- What is the expected number of deployments per day or per hour?
- Are there any specific performance or latency requirements?

## Target Environments

- What types of environments will the code be deployed to (e.g., cloud-based, on-premises, hybrid)?
- Are there any specific platforms, operating systems, or architectures that need to be supported?

## Security Requirements

- What security measures need to be in place to protect the code during deployment?
- Are there any specific authentication or authorization requirements?
- Is there a need for encryption or secure communication channels?

## Versioning and Rollbacks

- How should the system handle versioning of the deployed code?
- Is there a need for the ability to rollback to a previous version in case of issues or failures?

## Deployment Workflow

- What is the desired workflow for code deployment (e.g., continuous integration/continuous deployment, manual approval process)?
- Are there any specific pre-deployment or post-deployment tasks that need to be performed?

## Monitoring and Logging

- What metrics and logging information should be captured during deployment?
- Are there any specific monitoring or alerting requirements in case of deployment failures?

## Network and Infrastructure

- What are the available network bandwidth and infrastructure capabilities across different regions?
- Are there any limitations or considerations related to firewalls, load balancers, or other networking components?

## Compliance and Governance

- Are there any compliance requirements or industry-specific regulations that need to be considered during code deployment?

## Integration and Compatibility

- Does the code-deployment system need to integrate with any existing tools or systems (e.g., version control, configuration management)?
- Are there any dependencies or restrictions regarding the technologies or programming languages used in the code?

## Team and Roles

- Who will be responsible for managing and operating the code-deployment system?
- What are the roles and responsibilities of the individuals involved in the deployment process?

# First pass of the system design

- The system is supposed to exist in five different physical locations
- where binaries have to be deployed reliably and
- where the system have to be performance enought to do the deployment within a few minutes

## Global Deployment

- With around 5 locations, you need to ensure that the system can efficiently distribute deployments across these locations while maintaining consistent performance.
- Consider using a distributed architecture with local deployment servers in each location to minimize latency and network bottlenecks.

## Deployment Frequency and Rollbacks

- Supporting hundreds of deployments per day requires an automated and streamlined process.
- Implement a robust versioning system that allows easy rollback to previous versions if issues occur.
- Define a clear rollback strategy to handle failures, including a mechanism to roll forward quickly once the issue is resolved.

## Uptime and Performance

- To achieve 99.9% uptime, consider implementing redundancy and failover mechanisms across the deployment system.
- Optimize the deployment process to minimize downtime during deployments, aiming for a maximum build and deploy time of 30 minutes.
- Utilize load balancing and resource scaling techniques to handle increased demand during peak deployment periods.

## Integration with Code Reviews and Build Systems:

- Leverage the existing code review and build systems to ensure the quality and integrity of the code being deployed.
- Integrate the code-deployment system with the code review system to enforce checks and balances before allowing deployment.

## Automation and Orchestration

- Automation is crucial for managing a high volume of deployments.
- Implement a robust deployment pipeline that automates the steps from code submission to production deployment, including testing and verification.

## Monitoring and Alerting

- Set up comprehensive monitoring and logging capabilities to track the performance, health, and success of deployments.
- Implement real-time alerts to notify relevant teams or individuals in case of deployment failures or anomalies.

## Security and Access Control

- Ensure proper authentication and authorization mechanisms are in place to prevent unauthorized access to the deployment system.
- Consider using secure communication protocols (e.g., HTTPS) to protect sensitive data during code deployment.

## Training and Documentation:

- Provide training and documentation to users and stakeholders to ensure smooth adoption and understanding of the code-deployment system.
- Document best practices, guidelines, and troubleshooting procedures to assist users in case of issues.

By addressing these considerations, it is possible to design a global and fast code-deployment system that meets the specified requirements and supports efficient and reliable deployments across your organization.

# The system overview

Based on the description above we asked ChatGPT to generate a high-level sketch in PlantUML notation. _See Systemdesign.uml_
