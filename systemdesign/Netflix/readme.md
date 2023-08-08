# Netflix - streaming services

# Initial questions/thoughts

## Scope

- Score/core: Go to the platform, profile will be presented with movies and shows, and watch them, and it uses your history to make recommendations
- Out of scope/not Core: No major thoughts on auxiliary things like authentication and payments ...

## Users

- 200 million users
-

# Prior experiences

- Spotify design (reusable?)
- Digital TV broadcast (STB-applications)
- Codeta (streamed videos in the CMS - and the design)

# Core design

- Use cases
- Information model
- Services/APIs
- Examples
- Sequence diagrams
- System diagram

## Use Cases

1. User Registration & Management
2. Content Browsing & Search
3. Content Streaming
4. Content Recommendation
5. Account & Subscription Management
6. User Feedback & Ratings

| **Use Case**                         | **Core Service**       | **API(s)**                                                                                                      | **Information Model**                                                              |
| ------------------------------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1. User Registration & Management    | User Service           | `registerUser`, `login`, `logout`, `updateUserProfile`, `deleteUser`                                            | `User {userID, email, password, name, DOB, country}`                               |
| 2. Content Browsing & Search         | Content Service        | `browseContent`, `searchContent`, `getContentDetails`, `getGenres`, `getTrending`                               | `Content {contentID, title, genre, releaseDate, duration, synopsis, cast, rating}` |
| 3. Content Streaming                 | Streaming Service      | `streamContent`, `pauseStream`, `resumeStream`, `stopStream`                                                    | `Stream {userID, contentID, timestamp, currentProgress, bitrate, resolution}`      |
| 4. Content Recommendation            | Recommendation Service | `getRecommendationsForUser`, `getSimilarContent`                                                                | `Recommendation {userID, recommendedContentID[]}`                                  |
| 5. Account & Subscription Management | Account Service        | `createSubscription`, `updateSubscription`, `cancelSubscription`, `getSubscriptionDetails`, `getBillingHistory` | `Subscription {userID, planType, startDate, endDate, billingAmount, billingCycle}` |
| 6. User Feedback & Ratings           | Feedback Service       | `rateContent`, `submitFeedback`, `getContentRatings`, `getUserRatings`                                          | `Rating {userID, contentID, ratingValue, feedbackText}`                            |

This table provides a structured way of thinking about how the various components of a service like Netflix might interact. In reality, Netflix has a much more intricate system with dozens of microservices handling various functionalities. This is a simplified and representative structure for design interview purposes.

## The ranking of these features - user, technical and business

Certainly. I'll add the scoring for each ranking criteria explicitly to the table:

| **Rank** | **Use Case**                      | **Core Service**       | **User Value** | **Technical Complexity** | **Business Significance** | **Overall Motivation**                                                                                                                                                                          |
| -------- | --------------------------------- | ---------------------- | -------------- | ------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Content Streaming                 | Streaming Service      | 10/10          | 9/10                     | 10/10                     | The primary value proposition of Netflix is streaming. Technical challenges include handling adaptive bitrate streaming, optimizing for various devices and networks, and ensuring low latency. |
| 2        | Content Recommendation            | Recommendation Service | 9/10           | 10/10                    | 9/10                      | Crucial for user retention and engagement. Technically challenging due to the need for real-time analysis, machine learning models, and personalization at scale.                               |
| 3        | User Registration & Management    | User Service           | 8/10           | 8/10                     | 9/10                      | Without user management, no other service can be personalized. The challenge lies in security, scalability, and global distribution of user data.                                               |
| 4        | Content Browsing & Search         | Content Service        | 8/10           | 8/10                     | 8/10                      | Core to the user experience. Search algorithms, metadata management, and real-time updates are challenging.                                                                                     |
| 5        | Account & Subscription Management | Account Service        | 7/10           | 8/10                     | 10/10                     | Directly linked to revenue. Challenges include secure handling of payment data, integrations with payment gateways, and managing subscription lifecycles.                                       |
| 6        | User Feedback & Ratings           | Feedback Service       | 7/10           | 7/10                     | 7/10                      | Important for content curation and user engagement. The primary challenge is gathering, storing, and analyzing large amounts of feedback data efficiently.                                      |

The scores are subjective and are meant to illustrate the potential significance of each service based on the criteria. Each criterion is rated out of 10, where 10 indicates the highest importance or challenge.

## From Spotify design

### Services

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

# Architecture

## Front-end

## Back-end

## Data (pipeline)

## Infrastructure

## Additional

- Security
- Protocols
- Algorithms
