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

## Amazon

## Exchanges - Stock Exchange

### Clarifying questions

- functional - like robinhood or etrade, buy/sell instruments, place a market order (buy/sell), not much else,
- non-functional - millions of customers, millions of trades (matched orders), high-availability, security, high-performance,

<br>

### Reflections

The design from front-end to back-end needs to be synchronized.

Driven by non-functional requirements to breaking down those first - to look for initial issues that might arise based on the millions of users and trades ...

Let's say that worst case there are 100,000 simultaneous users, that wants to follow some or a a lot of markets.

The majority of trades during the day is with 8 hours (8x3600 sec) with some peaks during the trading day - 2-3 trades/second - with peaks on 100s of orders per second.

It is easy to get into a situation where you over-optimize, but it is worth to consider a few of these things upfront.

And to go through the design end-to-end a few times before starting to iterate.

### Front-end

The initial thinking should be on rendering approach:

#### Rendering approaches

Sure, here's a comparison table of the different rendering approaches:

| Rendering Approach                        | Strengths                                                                                                                          | Weaknesses                                                                                                                                                                           |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Client-Side Rendering (CSR)**           | Smooth interaction after initial load. Flexible for dynamic content. Good for apps where SEO is not a priority.                    | Slow initial load. May impact SEO as crawlers may not execute or wait for JavaScript. Not optimal for low latency needs due to round-trip requirement for each interaction.          |
| **Server-Side Rendering (SSR)**           | Faster initial page load. Better SEO as the entire page's content is available to crawlers from the outset.                        | Increased server load. Page isn't interactive until all necessary JavaScript has loaded and run. May not be optimal for real-time updates as it requires a round trip to the server. |
| **Static Site Generation (SSG)**          | Fastest initial load time. Best SEO, as all content is available at load time. Low server load as pages are pre-generated.         | Not suitable for real-time updates or pages with content that changes frequently.                                                                                                    |
| **Incremental Static Regeneration (ISR)** | Benefits of SSG while also being able to serve dynamic content. Good SEO and performance.                                          | Only available with certain frameworks (like Next.js). Not ideal for extremely frequent updates.                                                                                     |
| **Hybrid Rendering**                      | Balances CSR and SSR to optimize for both performance and interactivity. Allows for real-time updates in certain parts of the app. | Complexity in implementation. Might still have slower initial load time compared to SSG or ISR.                                                                                      |

Given your requirement for low latency between the client and the trading systems to make the market as fair as possible, a hybrid rendering approach could be a good fit. This approach allows for real-time updates and interactions after the initial page load and reduces the need for frequent round trips to the server. You could also explore using WebSockets or Server-Sent Events (SSE) for pushing real-time updates from the server to the client, which could further reduce latency and enhance the user experience.

#### Efficient data handling

Implementing efficient data handling such as paginations, infinite scrolling, and lazy loading

##### Debouncing and throttling

If your application makes requests to the server as the user types into a field (for example, for autocomplete functionality), it can result in a large number of unnecessary requests. To avoid this, you can use debouncing or throttling.

Debouncing ensures that a function will not be executed until a certain amount of time has passed since it was last called. This can be useful for functions that react to user input, like search box autocomplete or form auto-saving features.

```JavaScript
let timer;
function debounce(func, delay) {
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => func.apply(this, args), delay);
  }
}

const debouncedSearch = debounce(searchFunc, 300);

input.addEventListener('input', debouncedSearch);
```

Throttling on the other hand ensures that a function is only called at most once in a specified period of time period.

```JavaScript
let allowFunction = true;
function throttle(func, limit) {
  return function(...args) {
    if (allowFunction) {
      func.apply(this, args);
      allowFunction = false;
      setTimeout(() => allowFunction = true, limit);
    }
  }
}

const throttledScroll = throttle(scrollFunc, 300);

window.addEventListener('scroll', throttledScroll);

```

##### Pagination and infinite scrolling

If the list a large, like a list of stocks:

```JavaScript
function getPage(pageNumber, pageSize) {
  fetch(`/api/stocks?page=${pageNumber}&size=${pageSize}`)
    .then(response => response.json())
    .then(data => displayData(data));
}
```

#### Caching

Client-side caching for data that doesn't change a lot

```JavaScript
const cache = {};

function getDataWithCaching(url) {
  if (cache[url]) {
    return Promise.resolve(cache[url]);
  } else {
    return fetch(url)
      .then(response => response.json())
      .then(data => {
        cache[url] = data;
        return data;
      });
  }
}
```

#### Offline

Using service workers

```JavaScript
const CACHE_NAME = 'my-cache';
const FILES_TO_CACHE = [
  '/',
  '/index.html',
  '/styles.css',
  '/script.js',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(FILES_TO_CACHE))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => response || fetch(event.request))
  );
});
```

<br>

### API/Communication protocol

Certainly, let's expand the comparison table to include security measures, low bandwidth measures, and real-time capabilities:

The communication protocol and data handling systems are crucial for a stock exchange. Here's why:

**Real-Time Updates:** Stock prices fluctuate constantly throughout a trading day. Real-time or near-real-time updates are essential for providing accurate data to users. The choice of communication protocol plays a crucial role in determining the speed and reliability of these updates.

**Scalability:** Stock exchanges can have millions of users and even more daily transactions. The chosen protocols and systems need to be able to scale to handle this load without impacting performance or reliability.

**Resilience:** Financial transactions are critical operations that require a high degree of reliability and data consistency. The systems and protocols used must be resilient to failures and provide guarantees about data consistency.

**Security:** Given the sensitive nature of financial data and transactions, security is paramount. The protocols and systems must provide strong security measures to protect against various types of attacks and unauthorized access.

**Latency:** In stock trading, even a few seconds of delay can make a huge difference. High-frequency trading, for instance, relies on extremely low latency. Protocols with less overhead and faster data transmission like gRPC, WebSockets, or even proprietary protocols might be preferred for such use cases.

**Bandwidth Usage:** Considering the volume of real-time data being transmitted, the protocol should also be efficient in terms of bandwidth usage. Protocols that support features like data compression and binary data transmission can help reduce bandwidth usage.

To sum up, the choice of communication protocols and data handling systems can greatly impact the performance, reliability, scalability, and security of a stock exchange. Therefore, these considerations are very important. However, the "best" choices depend on the specific requirements, constraints, and trade-offs of your application.

| Protocol/System          | Request/Response                                 | Server Push                     | Multiplexing | Binary Data               | Full Duplex            | Stream Processing | Security                          | Low Bandwidth                             | Real-Time |
| ------------------------ | ------------------------------------------------ | ------------------------------- | ------------ | ------------------------- | ---------------------- | ----------------- | --------------------------------- | ----------------------------------------- | --------- |
| REST                     | ✔️                                               | ❌                              | ❌           | ✔️(with additional setup) | ❌                     | ❌                | ✔️(with HTTPS)                    | ✔️(with compression)                      | ❌        |
| GraphQL                  | ✔️                                               | ✔️(with Subscriptions)          | ❌           | ❌                        | ✔️(with Subscriptions) | ❌                | ✔️(with HTTPS)                    | ✔️(clients specify data needs)            | ❌        |
| WebSockets               | ✔️                                               | ✔️                              | ✔️           | ✔️                        | ✔️                     | ✔️                | ✔️(with WSS)                      | ❌                                        | ✔️        |
| Server-Sent Events (SSE) | ❌                                               | ✔️                              | ❌           | ❌                        | ❌                     | ✔️                | ✔️(with HTTPS)                    | ❌                                        | ✔️        |
| gRPC                     | ✔️                                               | ✔️(with server streaming)       | ✔️           | ✔️                        | ✔️                     | ❌                | ✔️(with TLS)                      | ✔️(Protobuf is efficient)                 | ✔️        |
| RSocket                  | ✔️                                               | ✔️                              | ✔️           | ✔️                        | ✔️                     | ✔️                | ✔️(with Transport Layer Security) | ✔️(binary protocol)                       | ✔️        |
| SPDY                     | ✔️                                               | ✔️                              | ✔️           | ✔️                        | ✔️                     | ❌                | ✔️(with SSL)                      | ✔️(with compression)                      | ✔️        |
| QUIC                     | ✔️                                               | ✔️                              | ✔️           | ✔️                        | ✔️                     | ❌                | ✔️(Built-in encryption)           | ✔️(reduced connection establishment time) | ✔️        |
| Falcor                   | ✔️                                               | ❌                              | ❌           | ❌                        | ❌                     | ❌                | ✔️(with HTTPS)                    | ✔️(clients specify data needs)            | ❌        |
| Apache Kafka             | ✔️(in terms of producing and consuming messages) | ✔️(data is pushed to consumers) | ❌           | ✔️                        | ❌                     | ✔️                | ✔️(with SSL/TLS)                  | ❌                                        | ✔️        |

Again, keep in mind that this table is a simplification and might not capture all the subtleties of these protocols/systems. And just because a protocol supports a feature doesn't necessarily mean it's the best choice for that feature. Each of these protocols/systems has its own strengths and trade-offs, and you'll need to carefully evaluate them based on your specific needs and constraints.

#### Layer orientation

In an application such as a stock exchange platform with millions of customers and trades each day, the protocols that operate at the network and transport layers (Layer 3 and Layer 4 of the OSI model) play an essential role, even if it may not be directly apparent.

Layer 3 (Network Layer) protocols like IP (Internet Protocol) handle routing and transferring data from one network to another, which is crucial for the Internet to function.

Layer 4 (Transport Layer) protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) handle the transmission of data between systems, providing services like error-checking, data ordering, and flow control.

Without these layers, communication between your servers and your customers would not be possible. These layers form the bedrock upon which higher-level protocols like HTTP, WebSocket, or gRPC (which provide the functionality your application directly uses) are built.

That being said, from an application design perspective, you may not need to directly manage these lower-layer protocols. Your networking infrastructure and your chosen high-level protocol will handle these details for you. For example, when you decide to use HTTP/2, you're implicitly choosing to use TCP at the transport layer. Similarly, when you use QUIC (which HTTP/3 is based on), you're implicitly choosing to use UDP.

However, understanding these lower layers can help you make more informed decisions about your high-level protocol choice. For example, if you need ultra-low-latency communication, you might prefer a protocol that uses UDP (like QUIC) over one that uses TCP. But if reliable data delivery is more important, a protocol that uses TCP might be a better choice.

So, in short, even though you might not directly work with Layer 3 and Layer 4 protocols, they still play an important role in your application. Your main focus should likely be on selecting and implementing the right high-level protocol that best meets your specific requirements and constraints.

### Back-end considerations

Sure, here is a tabular view of some of the back-end considerations for designing a high-performance, scalable stock exchange system:

| Consideration                      | Description                                                                                                                                                                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System Architecture**            | Determine if a monolithic, microservices, or hybrid architecture best fits the application. Microservices can offer more flexibility and scalability but may be more complex to manage.                  |
| **Performance**                    | Choose a language and framework known for high performance, especially in terms of throughput and latency. Examples include C++, Rust, Java, and Go.                                                     |
| **Concurrency Model**              | Select a language that can handle a high volume of simultaneous connections efficiently. Languages with native support for async I/O or lightweight threads/coroutines could be beneficial.              |
| **Ecosystem**                      | Consider the libraries, frameworks, and tools available in the language's ecosystem, which can help accelerate development and ensure better code quality.                                               |
| **Development Speed**              | Higher-level languages like Python or Ruby might offer faster development cycles but may lack in raw performance. Consider a balance between development speed and performance.                          |
| **Maintainability**                | Choose a language that promotes a codebase easy to understand, modify, and maintain. Static typing can improve maintainability by catching many errors at compile time.                                  |
| **Scalability**                    | The language's runtime characteristics can impact the ease of scaling the system. Consider how the language handles multi-core processors, large memory handling, or a large number of open connections. |
| **Team Expertise**                 | Consider the team's familiarity and expertise with the language. Even the best language features can be useless if your team is not comfortable with the language.                                       |
| **Data Consistency**               | The system must provide strong consistency guarantees, avoiding race conditions or concurrency issues leading to data inconsistency.                                                                     |
| **Fault Tolerance and Resilience** | Design the system to handle failures gracefully, minimize downtime, and recover quickly. Use patterns like circuit breakers, retries, rate limiting, etc.                                                |
| **Security**                       | Implement best practices for security, including strong measures for authentication, authorization, encryption, and regular security audits.                                                             |
| **Database Optimization**          | Ensure your databases are optimized to handle high volumes of read and write operations, using techniques like indexing, sharding, and replication.                                                      |
| **Caching and CDN**                | Implement server-side caching and use a Content Delivery Network (CDN) to cache responses closer to the user, reducing latency and improving performance.                                                |

Remember, these are some of the considerations, and the specifics will depend on the exact requirements, constraints, and trade-offs of your project.

#### Language alternatives

Sure, here is how C, a lower-level language, could compare to Node.js and Go with regards to these considerations:

| Consideration                      | Description                                                                                  | Node.js                                                                                                                                                                      | Go                                                                                                                                                                                     | C                                                                                                                                                                                                   |
| ---------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System Architecture**            | Determines if a monolithic, microservices, or hybrid architecture best fits the application. | Node.js can support all types of architectures. However, it shines in microservices due to its event-driven nature and lightweight runtime.                                  | Go is also a great fit for microservices due to its simplicity, performance, and built-in support for concurrency.                                                                     | C doesn't naturally lend itself to the microservices architecture, but it's possible with proper abstractions and discipline.                                                                       |
| **Performance**                    | Raw speed and efficiency of the language.                                                    | Node.js is not the fastest language due to its interpreted nature, but its event-driven, non-blocking model can handle a large number of concurrent connections efficiently. | Go is a compiled language that is known for its high performance. It can handle CPU-intensive tasks much better than Node.js.                                                          | C is a lower-level language, and it can be extremely efficient in terms of raw speed. It's possible to optimize C code to a very high degree.                                                       |
| **Concurrency Model**              | Ability to handle simultaneous connections or tasks.                                         | Node.js has an event-driven model with asynchronous I/O, which can efficiently handle a large number of concurrent connections.                                              | Go has built-in support for lightweight threads (goroutines), which makes it excellent for tasks that require high concurrency.                                                        | C does not provide built-in support for concurrency, but it can be achieved using multi-threading with libraries such as Pthreads.                                                                  |
| **Ecosystem**                      | Libraries, frameworks, and tools available.                                                  | Node.js has a vast ecosystem with packages available for almost any task, thanks to npm. Express.js is a widely used framework for building web applications.                | Go's ecosystem is not as large as Node.js, but it's growing. For web development, there are frameworks like Gin and Echo.                                                              | C's ecosystem is vast and mature, but it lacks modern web development frameworks that Node.js and Go have.                                                                                          |
| **Development Speed**              | How quickly can we develop and iterate?                                                      | JavaScript is widely known and used, which can accelerate development. Also, Node.js has a shorter feedback loop due to its interpreted nature.                              | Go is easy to learn and use, which could lead to fast development. However, its compile-run cycle could be slower than Node.js.                                                        | C development can be slow due to its low-level nature. It requires manual memory management, and its compile-link-run cycle can be lengthy.                                                         |
| **Maintainability**                | Ease of maintaining and evolving code.                                                       | JavaScript is dynamically typed, which may lead to runtime errors. TypeScript, a superset of JavaScript, introduces static typing and can improve maintainability.           | Go is statically typed, which can reduce runtime errors and improve maintainability. Its syntax is simple and easy to read.                                                            | C code can be difficult to maintain due to its low-level nature. It lacks high-level abstractions and requires careful memory management.                                                           |
| **Scalability**                    | How does the language handle growth in data, traffic, or complexity?                         | Node.js can scale well, especially in I/O-bound tasks. However, CPU-bound tasks can block the Node.js event loop and degrade performance.                                    | Go is excellent for scalability. It performs well for both I/O-bound and CPU-bound tasks, and goroutines allow efficient use of multi-core processors.                                 | C can scale well in terms of performance, but it requires more manual work compared to Node.js or Go. It doesn't provide built-in support for I/O-bound scalability.                                |
| **Team Expertise**                 | Familiarity and expertise of the team with the language.                                     | JavaScript is one of the most popular languages and many developers have experience with it.                                                                                 | Go is less widely known compared to JavaScript, so your team might need to learn it, which could slow down initial development.                                                        | C is a classic language that many developers learn early on, but its low-level nature and complexity mean that it requires a higher level of expertise to use effectively in large applications.    |
| **Data Consistency**               | Ability to avoid race conditions or concurrency issues leading to data inconsistency.        | JavaScript is single-threaded, which eliminates many (but not all) concurrency-related issues. However, care must be taken to handle async operations properly.              | Go has built-in support for concurrent programming. However, ensuring data consistency requires careful handling of synchronization between goroutines.                                | C provides low-level mechanisms for managing concurrency, like mutexes, which can ensure data consistency. However, it requires a great deal of care and expertise to use correctly.                |
| **Fault Tolerance and Resilience** | Ability to handle and recover from errors and failures.                                      | Node.js does not have built-in features for this. Libraries like circuit-breaker-js can be used to implement these patterns.                                                 | Go's simplicity and strong static typing make it easier to write correct code. For more advanced fault tolerance, external libraries or patterns would need to be used.                | C lacks built-in features for fault tolerance and resilience. However, with its low-level access, developers can build custom solutions, albeit at a cost of increased complexity.                  |
| **Security**                       | Strength and ease of implementing secure applications.                                       | Node.js has well-known security modules like helmet and express-rate-limit. However, JavaScript's flexibility can also lead to security risks if not used carefully.         | Go is a statically-typed and compiled language, which reduces the risk of many common programmer mistakes. However, like any other language, secure coding practices must be followed. | C is powerful, but it's also easy to make serious security mistakes. Buffer overflows, underflows, and memory leaks are common security issues. Careful coding and extensive testing are necessary. |
| **Database Optimization**          | Language support for database operations and optimizations.                                  | Node.js supports a wide range of databases, both SQL and NoSQL, via ORMs like Sequelize or Mongoose.                                                                         | Go has several libraries for database access and supports SQL and NoSQL databases. However, ORMs are not as common in the Go ecosystem.                                                | C can interact with almost any database, but                                                                                                                                                        |

it usually requires writing low-level code or using a library. There is no standard ORM-like tool for C. |
| **Caching and CDN** | Ability to work with caching systems and CDNs. | Node.js can use in-memory data stores like Redis for caching and can interact with CDNs for static content delivery. | Go can also work with caching systems like Redis and CDNs. Its performance and concurrent processing capabilities make it a good fit for cache-heavy applications. | C can use caching systems and CDNs, but it usually requires lower-level, more complex code compared to Node.js or Go. |

Please note that the decision to use C should be considered very carefully due to its low-level nature, which can increase complexity and potential security risks. For many web applications, Node.js or Go (or other high-level languages) are more suitable. However, if maximum performance is crucial and the team has strong C expertise, it could be a viable choice.

<br>

#### Breaking points?

In a high-volume application like a stock exchange where there could be millions or tens of millions of trades each day, both the language choice and the infrastructure can be critical.

When comparing Node.js to Go in this scenario, there are some potential breaking points to consider:

1. **Concurrency**: Node.js uses a single-threaded event-driven architecture, which can handle a large number of concurrent connections. However, if there are CPU-bound tasks, they could potentially block the event loop and degrade performance. Go, on the other hand, has built-in support for lightweight threads (goroutines) and a strong concurrency model, making it capable of handling CPU-intensive tasks along with high concurrency requirements effectively.

2. **Performance**: Go, being a statically-typed compiled language, generally provides better performance than Node.js, especially for CPU-intensive operations. If your application requires a high level of computational tasks, Go may be a better choice.

3. **Scaling**: As the load increases, you might find that you need more instances of Node.js running to keep up with the demand, whereas you might need fewer instances of Go due to its better performance and efficiency.

However, language is just one part of the equation. The infrastructure also plays a significant role in how your application can scale and handle the load. Things like database design and optimization, load balancing, caching strategies, and how you distribute your microservices can greatly impact the system's overall performance and ability to handle large loads.

Cloud services, like AWS, Google Cloud, or Azure, provide tools and services that can help manage load, scale your application, and monitor performance, which can be just as important as your language choice. For example, using auto-scaling groups can help ensure that you have the right number of instances running to handle the current load. Similarly, using a load balancer can help distribute traffic evenly across your instances, preventing any single instance from becoming a bottleneck.

In conclusion, both Node.js and Go can be used to build a high-volume application like a stock exchange. The choice between them depends on your specific use case, the nature of the tasks your application performs, and your team's expertise. However, irrespective of the language you choose, proper infrastructure planning and optimization is crucial to handle the load efficiently and provide a smooth user experience.

### Data "pipeline"

Here is the table summarizing the considerations and the corresponding Google Cloud technologies for building a data pipeline:

| Data Pipeline Stage     | Considerations                                                           | Google Cloud Technologies                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Ingestion          | - Source of data <br> - Frequency of updates                             | - Google Cloud Pub/Sub <br> - Google Cloud Dataflow <br> - Google Cloud Functions <br> - Google Cloud Data Fusion                               |
| Data Storage            | - Data structure <br> - Data size <br> - Access patterns                 | - Google Cloud SQL <br> - Google Cloud Spanner <br> - Firestore <br> - Google Cloud Bigtable <br> - Google Cloud Storage <br> - Google BigQuery |
| Data Processing         | - Volume of data <br> - Real-time needs                                  | - Google Cloud Dataflow <br> - Google BigQuery                                                                                                  |
| Data Analysis           | - Business intelligence or machine learning needs                        | - Google Data Studio <br> - Google BigQuery ML <br> - Google Cloud AI and ML Platform                                                           |
| Data Security           | - Data security <br> - Access control <br> - Compliance with regulations | - Google Cloud IAM <br> - Google Cloud Security Command Center <br> - Google Cloud's Compliance offerings                                       |
| Monitoring and Alerting | - Monitoring data pipeline <br> - Alerting in case of issues             | - Google Cloud Operations Suite                                                                                                                 |

Please note that the exact services used can vary depending on the specific requirements of your data pipeline.

### Infrastructure

Sure, below is a table that describes a possible infrastructure setup on AWS, Azure, and Google Cloud Platform, including some useful Go-related tools and libraries. This is not exhaustive, but should provide a good starting point.

| Category                   | AWS                                                                                                   | Azure                                                                                             | Google Cloud Platform                                                                    | Go-related tools and libraries                                                      | Others                                                               |
| -------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Compute**                | Elastic Compute Cloud (EC2) for running Go services. Elastic Beanstalk for application orchestration. | Azure Virtual Machines for running Go services. Azure App Service for app deployment and scaling. | Compute Engine for running Go services. App Engine for automatic scaling and management. | Gorilla/mux for URL routing and handling. Negroni for HTTP middleware.              | Docker for containerization. Kubernetes for container orchestration. |
| **Storage**                | Simple Storage Service (S3) for object storage. Elastic Block Store (EBS) for block storage.          | Azure Blob Storage for object storage. Disk Storage for block storage.                            | Cloud Storage for object storage. Persistent Disk for block storage.                     | Go's standard library provides packages to interact with cloud storage services.    | -                                                                    |
| **Database**               | Relational Database Service (RDS) for SQL databases. DynamoDB for NoSQL.                              | Azure SQL Database. Cosmos DB for NoSQL.                                                          | Cloud SQL for MySQL and PostgreSQL. Firestore for NoSQL.                                 | sqlx for improved database interaction in Go.                                       | -                                                                    |
| **Caching**                | ElastiCache for in-memory caching.                                                                    | Azure Cache for Redis.                                                                            | Cloud Memorystore for Redis.                                                             | redigo or go-redis as Go clients for Redis.                                         | -                                                                    |
| **Load Balancing**         | Elastic Load Balancing (ELB).                                                                         | Azure Load Balancer.                                                                              | Cloud Load Balancing.                                                                    | -                                                                                   | -                                                                    |
| **Networking**             | Amazon VPC for networking. Direct Connect for dedicated network connection.                           | Azure Virtual Network. ExpressRoute for dedicated network connection.                             | Google Cloud VPC. Cloud Interconnect for dedicated network connection.                   | -                                                                                   | -                                                                    |
| **Messaging/Event-Driven** | Simple Notification Service (SNS). Simple Queue Service (SQS).                                        | Azure Service Bus. Event Grid.                                                                    | Pub/Sub for real-time messaging.                                                         | Go AWS SDK, Azure SDK, or Google Cloud SDK for interaction with messaging services. | -                                                                    |
| **Monitoring**             | CloudWatch for monitoring. X-Ray for tracing.                                                         | Azure Monitor. Application Insights for tracing.                                                  | Cloud Monitoring. Cloud Trace for tracing.                                               | Prometheus for metrics collection in Go. OpenTelemetry for tracing and metrics.     | Grafana for visualization of metrics.                                |
| **CI/CD**                  | AWS CodePipeline for CI/CD.                                                                           | Azure Pipelines for CI/CD.                                                                        | Cloud Build for CI/CD.                                                                   | -                                                                                   | Jenkins or CircleCI for CI/CD.                                       |
| **Security**               | Identity and Access Management (IAM). AWS Shield for DDoS protection.                                 | Azure Active Directory. Azure DDoS Protection.                                                    | Identity and Access Management (IAM). Google Cloud Armor for DDoS protection.            | -                                                                                   | HashiCorp Vault for secrets management.                              |

Remember, the choice of services will be driven by your specific use case, cost, team expertise, and preferences. The above are just recommendations and starting points.

#### Additional infrastructure due to API/communication protocols

Yes, depending on the API/communication protocols that you choose, there could be some additional considerations and services you might need to include:

1. **API Gateway**: If you're using REST or GraphQL over HTTP/HTTPS, you would need an API Gateway service to manage, secure, and throttle your APIs. In AWS, this could be the Amazon API Gateway; in Azure, it's the Azure API Management; and in Google Cloud, it's the Apigee API Platform.

2. **WebSocket support**: If you choose to use WebSocket, you'd need to make sure your load balancer and other networking components support WebSocket connections. AWS API Gateway and Application Load Balancer, Azure API Management and Application Gateway, and Google Cloud Load Balancer all support WebSocket connections.

3. **Serverless computing**: If you're planning on using Server-Sent Events (SSE), your infrastructure would need to support long-lived HTTP connections. This might influence your choice of compute service. For instance, AWS Lambda, a serverless computing service, has a maximum execution duration per request of 15 minutes as of my knowledge cutoff in September 2021, which could be a constraint for long-lived SSE connections.

4. **gRPC support**: If you're considering gRPC, you'll need to ensure your infrastructure supports HTTP/2, as gRPC is built on top of it. Google Cloud's load balancers and Cloud Endpoints support HTTP/2 and gRPC. Azure's Application Gateway and API Management recently added support for gRPC and HTTP/2 as well. In AWS, the Application Load Balancer and Network Load Balancer support HTTP/2, but as of my knowledge cutoff in September 2021, AWS's API Gateway does not natively support gRPC, though there are workarounds using AWS Lambda and a proxy server.

5. **Real-time updates**: If you require real-time updates (like price changes or trade confirmations) pushed to your clients, you might also need a real-time messaging service. AWS offers Simple Notification Service (SNS) and AppSync (for real-time GraphQL), Azure has Azure SignalR Service, and Google Cloud has Pub/Sub.

6. **Security**: Regardless of the protocols used, the security of your APIs is crucial. Consider using services like AWS WAF (Web Application Firewall), Azure Front Door (which includes WAF), or Google Cloud Armor to protect your APIs.

7. **Monitoring**: Monitoring the performance and usage of your APIs is also essential. Consider using API-specific monitoring and tracing tools like AWS X-Ray, Azure Application Insights, or Google Cloud Trace.

These additional components should integrate well with the previously mentioned infrastructure, enhancing your ability to create and maintain a secure, scalable, and efficient trading platform.

### Security layers

Security is an essential aspect of any application, especially when dealing with financial transactions and sensitive user data. There are various components of security you need to consider, including user authentication, data security, network security, and ensuring the application is resistant to common web vulnerabilities.

**Front-end (React/JavaScript)**

1. **User Authentication**: Implement secure user authentication. OAuth 2.0 is a standard protocol for authentication that's used by many providers, including Google. Libraries like Passport.js can help simplify this process.

2. **Input Validation**: Validate all user inputs to protect against issues like SQL injection and Cross-Site Scripting (XSS) attacks. React mitigates most XSS issues by default, as it escapes content in JSX before rendering.

3. **HTTPS**: Always use HTTPS, not HTTP, to prevent man-in-the-middle attacks.

4. **Secure data storage**: Avoid storing sensitive data in local storage or session storage. If a Cross-Site Scripting (XSS) attack occurs, the attacker could access this data.

5. **Content Security Policy (CSP)**: Implement a CSP to prevent certain types of attacks, like XSS and data injection attacks.

**API (Protocol Buffers)**

1. **Transport Layer Security (TLS)**: Use Transport Layer Security (TLS) for all communications to ensure the confidentiality and integrity of data in transit.

2. **Access Control**: Ensure that only authenticated and authorized users can access your APIs.

3. **Rate limiting**: Implement rate limiting to prevent abuse of your APIs.

4. **Input Validation**: Validate all inputs to your API to protect against attacks like SQL injection. If using Protocol Buffers, schema validation is done automatically, reducing the risk.

**Infrastructure (Google Cloud)**

1. **Identity and Access Management (IAM)**: Use Google Cloud's IAM for controlling access to your cloud resources. Implement the principle of least privilege—give a user or service account only those permissions necessary to perform their job.

2. **Firewall**: Configure firewalls to control who can access your systems. Google Cloud Armor provides DDOS protection and a web application firewall.

3. **Encryption**: Google Cloud encrypts customer data stored at rest by default, and offers options for customer-managed encryption keys.

4. **Audit Logs**: Use Google Cloud's audit logs to keep track of who did what, when, and where.

5. **Regular updates and patches**: Make sure all your services are up-to-date and apply patches regularly.

Remember, security is a vast and complex topic and these are just some of the considerations. It's always recommended to have a security expert involved when designing the architecture for an application dealing with sensitive user data and financial transactions.

### Regulatory compliance

Regulatory compliance is a critical aspect of building and maintaining a stock exchange platform. The specific requirements may vary depending on the jurisdiction your platform operates in, but some general strategies to achieve and maintain compliance are:

1. **Data Protection**: Understand the data protection laws and regulations in your jurisdiction. If your users are from the European Union, you will need to comply with the General Data Protection Regulation (GDPR). If they are from California in the US, you will need to comply with the California Consumer Privacy Act (CCPA). Implement necessary measures to ensure user data is protected and users are able to exercise their rights.

2. **Financial Regulations**: As a stock exchange platform, there will be specific financial regulations you must follow, like SEC regulations in the US. Compliance with these regulations can be complex and might involve aspects like reporting, transparency, fair trading practices, etc. It's advisable to work with a legal team that specializes in financial regulation.

3. **Security Standards**: Compliance with security standards like ISO 27001 or the Payment Card Industry Data Security Standard (PCI DSS) can also be important, depending on your business model. Compliance with these standards can help protect user data and reduce the risk of breaches.

4. **Auditability**: Ensure that your systems are designed to capture the necessary data and preserve it in a way that supports audit requirements. This often involves keeping detailed logs of activities and changes.

5. **Infrastructure Compliance**: If you're using Google Cloud Platform, ensure your infrastructure complies with the necessary standards and regulations. Google Cloud provides several compliance offerings including ISO/IEC 27001 for information security management, ISO/IEC 27017 for cloud security, ISO/IEC 27018 for privacy, SOC 2 for controls relevant to security, availability, and confidentiality, and more.

6. **Continuous Monitoring and Review**: Compliance isn't a one-time process. Regular monitoring and review of your systems and practices are needed to ensure ongoing compliance, particularly as laws and regulations evolve over time.

Please note that this advice is very general, and the specifics will depend on your situation and jurisdiction. Consult with a lawyer or compliance expert to make sure you're meeting all necessary legal and regulatory requirements.

### Analytics and reporting

See Data Pipeline

Sure, here's a table that aligns the data management, data pipeline, and analytics/reporting components, considering infrastructure, front-end, and back-end aspects.

| Component                   | Consideration            | Google Cloud Services                                                           | React/JavaScript                                                                | Go                                                                                  | Communication Protocol |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------- |
| **Data Management**         | Data Ingestion           | Pub/Sub (real-time event ingestion), Cloud Storage (large scale file ingestion) | Fetch API/Axios (for making HTTP requests to ingest data)                       | Use standard library for HTTP requests, Google Cloud client libraries for ingestion | HTTP/2, gRPC           |
|                             | Data Transformation      | Dataflow (both stream and batch processing), Cloud Dataprep (for data cleaning) | Data is usually transformed in the backend                                      | Use standard libraries or third-party packages for data transformation              | Protobuf, Avro         |
|                             | Data Storage             | BigQuery (Data Warehousing), Firestore or Cloud SQL (operational databases)     | Not directly interacting with these services, but can request data through APIs | Google Cloud client libraries for interaction with storage services                 | HTTP/2, gRPC           |
| **Data Pipeline**           | Real-time data handling  | Pub/Sub, Dataflow                                                               | WebSocket API for real-time data display                                        | gorilla/websocket for handling WebSocket connections                                | WebSocket, SSE         |
|                             | Batch data handling      | Dataflow, Dataproc (for Apache Spark and Hadoop)                                | Not directly interacting with these services, but can request data through APIs | Google Cloud client libraries for interaction                                       | HTTP/2, gRPC           |
| **Analytics and Reporting** | Data Analysis            | BigQuery (for big data analytics)                                               | Fetch API/Axios for requesting analytical data                                  | Google Cloud client libraries for interaction with BigQuery                         | HTTP/2, gRPC           |
|                             | Reporting/Visualizations | Data Studio, Looker                                                             | Use libraries like D3.js, Recharts, etc. for data visualization on the frontend | Primarily a front-end concern, Go will serve processed data for visualizations      | HTTP/2                 |
|                             | Real-time Analytics      | BigQuery (for real-time analytics), Pub/Sub, Dataflow                           | WebSocket API for real-time data display                                        | gorilla/websocket for handling WebSocket connections                                | WebSocket, SSE         |
|                             | Machine Learning         | AI Platform, AutoML, TensorFlow                                                 | TensorFlow.js for running machine learning models in the browser (if needed)    | Go has support for TensorFlow, but Python is generally more popular for ML tasks    | HTTP/2, gRPC           |

It's important to note that not every tool or service is used directly with every technology. For instance, front-end code in React may not interact directly with BigQuery or Dataflow, but would instead request data via APIs from a server application written in Go, which does interact with these services.

### Operations, monitoring and alerts (and support)

DevOps is a combination of practices and tools designed to increase an organization's ability to deliver applications and services at high velocity. Here are some key components of the DevOps lifecycle and the corresponding tools you might use with Google Cloud, React/JavaScript, and Go:

| DevOps Phase                     | Google Cloud                                                                                                                                                                                   | React/JavaScript                                                                        | Go                                                                                                                          |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Source Control**               | Cloud Source Repositories (hosting private Git repositories)                                                                                                                                   | Git (source control system)                                                             | Git                                                                                                                         |
| **Continuous Integration (CI)**  | Cloud Build (building, testing, and deploying in a CI/CD pipeline)                                                                                                                             | Jest (testing), ESLint (linting), Webpack (bundling and minifying)                      | Go test (testing), Go vet (static analysis), Go build (compiling)                                                           |
| **Continuous Deployment (CD)**   | Cloud Build, Cloud Functions (deploying serverless apps), Kubernetes Engine (deploying containerized apps)                                                                                     | CircleCI, Jenkins, or GitHub Actions (CI/CD tools)                                      | Docker (containerization), Kubernetes (container orchestration)                                                             |
| **Monitoring**                   | Cloud Monitoring (infrastructure and application monitoring), Cloud Logging (log management), Cloud Trace (distributed tracing), Cloud Profiler (continuous profiling of CPU and memory usage) | React DevTools, Redux DevTools (for debugging React and Redux apps)                     | Go's built-in pprof package (profiling)                                                                                     |
| **Security and Compliance**      | Cloud IAM (identity and access management), Cloud Security Command Center (security and data risk platform), Cloud Compliance (regulatory compliance)                                          | Helmet (security-related HTTP headers), npm audit (dependency vulnerability assessment) | Go's standard library and third-party packages (security features like cryptography, secure random number generation, etc.) |
| **Infrastructure as Code (IaC)** | Cloud Deployment Manager (automated management and deployment), Terraform (open-source tool that works with GCP)                                                                               | Not applicable (handled on the infrastructure side)                                     | Not applicable (handled on the infrastructure side)                                                                         |
| **Feature Toggles**              | Firebase Remote Config (managing feature toggles)                                                                                                                                              | React feature toggle libraries like `react-feature-toggles`                             | Go feature toggle libraries like `gofli`                                                                                    |

Each of these tools can play a key role in maintaining high velocity while keeping quality high. They support iterative development, automation, collaboration, and provide insight into the application and infrastructure, enabling teams to catch and resolve issues quickly.

### Testing

Testing is a critical aspect of any application lifecycle, including stock exchange systems. A well-structured testing strategy is important for ensuring the functionality, performance, and security of your application. Here are some key areas of testing and the corresponding tools you might use:

| Testing Area            | React/JavaScript                                                                                                   | Go                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Unit Testing**        | Jest (JavaScript testing framework), Enzyme (React testing library), React Testing Library (alternative to Enzyme) | Go's built-in testing package, Testify (third-party library providing additional features) |
| **Integration Testing** | Jest, Supertest (HTTP assertions), nock (HTTP server mocking)                                                      | Go's built-in testing and net/http/httptest packages                                       |
| **End-to-End Testing**  | Cypress (browser-based end-to-end testing), Puppeteer (headless browser for automated testing)                     | Agouti (Webdriver for Go)                                                                  |
| **Performance Testing** | Lighthouse (performance audits for web apps), Sitespeed.io (website speed testing)                                 | Vegeta (HTTP load testing), Go's built-in benchmarking support                             |
| **Security Testing**    | OWASP ZAP (automated security scanning), npm audit (checks for vulnerabilities in Node.js dependencies)            | GoSec (inspects Go source code for security problems)                                      |

For each of these testing stages, you'd define test cases that cover the different parts of your application, such as various user interactions, data processing, and data persistence.

In a DevOps or Continuous Integration/Continuous Deployment (CI/CD) environment, these tests would be run automatically in your pipeline to catch any issues before they reach production. Google Cloud's Cloud Build can be configured to run these tests at each stage of your pipeline.

<br>
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
