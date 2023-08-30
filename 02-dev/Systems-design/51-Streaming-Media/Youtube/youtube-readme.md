---

# YouTube - Video Sharing & Streaming Platform

# Summary

A platform that allows users to upload, share, view, rate, comment on videos, and subscribe to other users.

# Introduction

This overview represents YouTube's system design at a high level. Given its immense user base, diverse content, and vast infrastructure, YouTube's actual architecture is highly complex and designed for scalability, performance, and resilience.

## Background

Launched in 2005 by Chad Hurley, Steve Chen, and Jawed Karim, YouTube was later acquired by Google in 2006. It revolutionized the way content is consumed, shared, and monetized on the internet.

## Scope

Design a platform to allow users to upload and stream videos, engage with content via likes, comments, and shares, and follow content creators.

## Usage

From vloggers to big media corporations, YouTube caters to a vast array of content creators and viewers. It serves as a platform for entertainment, education, advertising, news, and much more.

## Competitors

- Vimeo
- Dailymotion
- Twitch (for gaming and live streaming)
- TikTok (short-form content)

## Prior experience

YouTube has been pivotal in the rise of the influencer culture, democratizing content creation, and providing a platform for viral phenomena.

# Design

## User journey

1. **Creators**:

   - Register/Log in
   - Upload videos.
   - Engage with subscribers via comments, community posts.
   - Monetize content through ads, memberships, or merchandise.

2. **Viewers**:
   - Browse and search for content.
   - Engage with videos via likes, comments, and shares.
   - Subscribe to channels.
   - Use playlists, histories, or recommendations for content discovery.

## Services / API's

1. User Service (Registration, Authentication, Profiles)
2. Video Upload and Processing Service
3. Video Streaming Service
4. Engagement Service (Likes, Comments, Shares)
5. Subscription Service
6. Monetization Service (Ads, Super Chat, Memberships)
7. Search and Recommendation Service

## Information model

| Entity       | Attributes (Key Attributes in Bold)                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **User**     | **UserID**, Username, Email, ProfileImage, Bio, SubscribersCount, UploadedVideosCount                                        |
| **Video**    | **VideoID**, UserID (FK to User), Title, Description, Thumbnail, VideoFile, Timestamp, ViewsCount, LikesCount, CommentsCount |
| **Comment**  | **CommentID**, VideoID (FK to Video), UserID (FK to User), Content, Timestamp                                                |
| **Playlist** | **PlaylistID**, UserID (FK to User), Name, VideoIDs (List of VideoID)                                                        |

## Other

- **Sequence Diagrams**: Process of uploading, processing, and streaming videos.
- **System Model**: How the recommendation algorithms interact with user data.
- **Code Examples**: Techniques to optimize video streaming based on bandwidth.

# Architecture

## Front-end

- **Web**: Modern JavaScript frameworks such as React or Angular for dynamic UI.
- **Mobile**: Native apps (iOS - Swift, Android - Kotlin).

## Back-end

- **Web Server**: Python with Django or Java-based solutions (given Google's inclinations).
- **Database**: Bigtable (Google's NoSQL Big Data database service), MySQL or Spanner for structured data.

## Data Pipeline

- **ETL Process**: Extract from Bigtable, transform for analytics, and load into data warehouses like BigQuery.
- **Analytics**: Tools like Data Studio to analyze user engagement, views, and video spread.

## Infrastructure

- **Hosting**: Google Cloud Platform.
- **Storage**: Google Cloud Storage for video and media files.
- **CDN**: Google's own global CDN network for efficient video delivery.
- **Load Balancer**: Google's Load Balancers to handle global traffic distribution.

## Other

- **Algorithms**: Advanced recommendation systems using machine learning to suggest videos to users.
- **Security**: OAuth 2.0 for user authentication, DRM for copyrighted content.
- **Protocols**: DASH or HLS for adaptive video streaming.
- **Deep Stack**: Deep learning for video recommendations, content categorization, and more.
- **Costs**: High storage and bandwidth costs, given the video-focused nature of the platform.
- **Team Size**: Thousands, across product development, data science, marketing, and more.
