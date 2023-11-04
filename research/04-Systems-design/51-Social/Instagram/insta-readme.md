# Instagram - Photo & Video Sharing Social Network

# Summary

A platform that empowers users to capture, edit, share photos and videos, and interact with others through likes, comments, and direct messages.

# Introduction

## Background

Launched in 2010 by Kevin Systrom and Mike Krieger, Instagram was originally a photo-sharing platform. It quickly gained popularity and was acquired by Facebook in 2012. Over time, it integrated video sharing, stories, IGTV, and more.

## Scope

Design a platform to allow users to share photos and videos, discover content through a feed, engage via comments and likes, and communicate through direct messages.

## Usage

Instagram is popular among a diverse audience, from teenagers to businesses. It's used for personal sharing, brand promotion, content creation, and e-commerce through shoppable posts.

## Competitors

- TikTok
- Snapchat
- Pinterest
- Twitter
- Facebook

## Prior experience

No earlier experience

# Design

## User journey

1. **Creators**:

   - Register/Log in
   - Capture or upload photos/videos.
   - Edit using filters/tools.
   - Share on feed, stories, or IGTV.
   - Engage with followers through comments, likes.
   - Use Instagram Shop or monetize through brand collaborations.

2. **Viewers**:
   - Register/Log in.
   - Browse feed, discover content through Explore.
   - Engage with content.
   - Use Direct Messages for private chats.
   - Shop through shoppable posts.

## Services / API's

1. User Service (Registration, Authentication, Profiles)
2. Media Service (Photo, Video Upload, and Streaming)
3. Engagement Service (Likes, Comments, Saves)
4. Messaging Service (Direct Messages)
5. Discover Service (Explore, Recommendations)
6. E-commerce Service (Instagram Shop)

## Information model

| Entity            | Attributes (Key Attributes in Bold)                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **User**          | **UserID**, Username, Email, ProfileImage, Bio, FollowersCount, FollowingCount, PostsCount               |
| **Media**         | **MediaID**, UserID (FK to User), Caption, MediaFile (Photo/Video), Timestamp, LikesCount, CommentsCount |
| **Comment**       | **CommentID**, MediaID (FK to Media), UserID (FK to User), Content, Timestamp                            |
| **DirectMessage** | **MessageID**, SenderID (FK to User), ReceiverID (FK to User), Content, Timestamp                        |

## Other

- **Sequence Diagrams**: Process of capturing, editing, and sharing photos/videos.
- **System Model**: Interactions between different services.
- **Code Examples**: Techniques for the Explore page algorithm.

# Architecture

## Front-end

- **Web**: ReactJS for a responsive web experience.
- **Mobile**: Native apps (iOS - Objective-C/Swift, Android - Java/Kotlin).

## Back-end

- **Web Server**: Python with Django (originally, now possibly diversified).
- **Database**: PostgreSQL for relational data; Cassandra for scalable post metadata storage.

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into a data warehouse.
- **Analytics**: Tools such as Tableau or PowerBI to analyze user engagement and growth.

## Infrastructure

- **Hosting**: Facebook's infrastructure, given the acquisition.
- **Storage**: Distributed storage for media files.
- **CDN**: Use of multiple CDNs for faster global content delivery.
- **Load Balancer**: Facebook's proprietary systems for handling traffic distribution.

## Other

- **Algorithms**: Personalized recommendation algorithms for the Explore page.
- **Security**: OAuth for user authentication, end-to-end encryption for direct messages.
- **Protocols**: Multiple, considering the range of services, including video streaming protocols.
- **Deep Stack**: Advanced AI for content recommendation and moderation.
- **Costs**: Major costs associated with storage, delivery, and AI computations.
- **Team Size**: Large, encompassing a range of roles, from product development to data science.

---

This provides an overview of Instagram's system design. Given its vast user base, myriad features, and continual evolution, the platform's architecture is complex and highly optimized for scale and performance.
