# Twitter - Microblogging & Social Network

# Summary

A platform that allows users to send, read, and interact with brief messages called "tweets." Tweets are limited to a specific number of characters, fostering concise communication.

# Introduction

This is a high-level system design for Twitter. The actual architecture of Twitter is complex and optimized for real-time delivery, scalability, and resilience.

## Background

Launched in 2006 by Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams, Twitter rapidly became a new standard for real-time communication and news dissemination.

## Scope

Design a platform for users to post short messages, follow others, retweet, like, and reply to tweets, and direct message for private conversations.

## Usage

Twitter is popular among a wide demographic, including celebrities, politicians, journalists, businesses, and everyday users for personal sharing, news reporting, brand promotion, and real-time discussions.

## Competitors

- Facebook
- Instagram
- Mastodon (open-source alternative)
- Tumblr

## Prior experience

Twitter has played a crucial role in various global events, from political movements to the live reporting of events. The "hashtag" (#) phenomenon started here.

# Design

## User journey

1. **Tweeters**:

   - Register/Log in
   - Compose and post tweets.
   - Retweet, like, and reply to tweets.
   - Engage with followers through comments and mentions.
   - Direct message for private conversations.

2. **Followers**:
   - Register/Log in.
   - Follow other users.
   - Browse the timeline and engage with tweets.
   - Use Direct Messages for private conversations.

## Services / API's

1. User Service (Registration, Authentication, Profiles)
2. Tweet Service (Posting, Retweeting)
3. Engagement Service (Likes, Replies)
4. Follow Service (Follow/Unfollow Users)
5. Direct Messaging Service
6. Trending Service (Hashtags and Trends)

## Information model

| Entity            | Attributes (Key Attributes in Bold)                                                         |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **User**          | **UserID**, Handle, Email, ProfileImage, Bio, FollowersCount, FollowingCount, TweetCount    |
| **Tweet**         | **TweetID**, UserID (FK to User), Content, Timestamp, RetweetsCount, LikesCount, ReplyCount |
| **DirectMessage** | **MessageID**, SenderID (FK to User), ReceiverID (FK to User), Content, Timestamp           |
| **Trend**         | **TrendID**, Name (e.g., Hashtag), Description, TweetCount                                  |

## Other

- **Sequence Diagrams**: Lifecycle of a tweet from creation to dissemination.
- **System Model**: Interactions between services, especially the real-time nature of tweets.
- **Code Examples**: How trends are computed from tweet data.

# Architecture

## Front-end

- **Web**: JavaScript frameworks like React or Angular for a dynamic web interface.
- **Mobile**: Native apps (iOS - Swift, Android - Kotlin).

## Back-end

- **Web Server**: Scala with Finagle (Twitter's historically known stack).
- **Database**: MySQL for structured data; Manhattan (Twitter's real-time, multi-tenant distributed storage) for tweets and user data.

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into Twitter's analytics platform.
- **Analytics**: Internal tools to monitor user growth, engagement, and content spread.

## Infrastructure

- **Hosting**: Twitter uses a combination of in-house data centers and cloud services.
- **Storage**: Manhattan, Blobstore for media like images and videos.
- **CDN**: Use of external CDNs like Akamai for content delivery.
- **Load Balancer**: In-house solutions for distributing incoming traffic.

## Other

- **Algorithms**: Algorithms to compute trending topics based on tweet volume and engagement.
- **Security**: OAuth for user authentication, encryption for data at rest and in transit.
- **Protocols**: User Streaming for real-time tweet delivery.
- **Deep Stack**: Machine learning for tweet recommendations and ad targeting.
- **Costs**: Infrastructure costs especially due to the real-time nature of the platform.
- **Team Size**: Thousands, encompassing development, operations, data science, and more.
