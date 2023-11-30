# TikTok - Short Video Sharing Platform

# Summary

A platform that enables users to create, share, and discover short music videos, primarily to showcase talent, creativity, and precious life moments.

# Introduction

This is a general system design for TikTok. The real-world architecture would delve deeper, considering things like real-time video processing, complex recommendation systems, global content delivery, and stringent content moderation.

## Background

Founded in 2016 by ByteDance, TikTok was originally released in China under the name Douyin. The international version, TikTok, was introduced in 2017. It skyrocketed to global prominence after merging with the lip-syncing app Musically.

## Scope

Design a short video sharing and discovery platform. The platform should support user registration, video creation/upload, browsing via a "For You" feed, engagement through likes/comments/shares, and following other users.

## Usage

TikTok is popular among teenagers and young adults, serving as a platform to showcase creativity, talents, comedic skits, dances, and challenges.

## Competitors

- Instagram Reels
- YouTube Shorts
- Triller
- Dubsmash
- Snapchat

## Prior experience

No prior experience

# Design

## User journey

1. **Creators**:

   - Register/Log in
   - Create or upload short videos.
   - Engage with viewers through comments.
   - Monetize content through brand collaborations.

2. **Viewers**:
   - Register/Log in.
   - Browse the "For You" feed or specific user profiles.
   - Engage with videos (like, comment, share).
   - Follow creators.

## Services / API's

1. User Service (Registration, Authentication, Profiles)
2. Video Service (Upload, Stream)
3. Discovery Service ("For You" Algorithm)
4. Engagement Service (Likes, Comments, Shares)
5. Monetization and Ad Service (Ads, Promotions)
6. Search and Recommendation Service

## Information model

| Entity         | Attributes (Key Attributes in Bold)                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| **User**       | **UserID**, Username, Email, ProfileImage, Bio, FollowersCount, FollowingCount                          |
| **Video**      | **VideoID**, UserID (FK to User), Caption, VideoFile, Timestamp, LikesCount, CommentsCount, SharesCount |
| **Comment**    | **CommentID**, VideoID (FK to Video), UserID (FK to User), Content, Timestamp                           |
| **Engagement** | **EngagementID**, Type (Like, Share), UserID (FK to User), VideoID (FK to Video), Timestamp             |

## Other

- **Sequence Diagrams**: Process of video creation and uploading.
- **System Model**: How video streaming is efficiently managed.
- **Code Examples**: How the "For You" algorithm could be structured.

# Architecture

## Front-end

- **Web**: Vue.js for a responsive web application.
- **Mobile**: Native apps (iOS - Swift, Android - Kotlin).

## Back-end

- **Web Server**: Node.js with Express.
- **Database**: PostgreSQL for relational data; Cassandra for scalable video metadata storage.

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into a data warehouse.
- **Analytics**: Tools like Tableau on data warehouse for insights about user growth and engagement.

## Infrastructure

- **Hosting**: AWS EC2 instances.
- **Storage**: AWS S3 for video storage.
- **CDN**: Akamai or Cloudflare for fast, global video delivery.
- **Load Balancer**: AWS ELB to handle traffic distribution.

## Other

- **Algorithms**: Personalized recommendation algorithms for the "For You" feed.
- **Security**: OAuth for user authentication, SSL/TLS for data encryption.
- **Protocols**: HLS for video streaming.
- **Deep Stack**: Use of machine learning for content moderation and recommendation.
- **Costs**: Cost associated with video storage and delivery would be significant.
- **Team Size**: Initial team of 200+, scaling as per growth.
