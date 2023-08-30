# Twitch - Live-Streaming Platform for Gamers

# Summary

A platform that allows users to stream live gameplay, engage with viewers in real-time, and monetize their streams through ads, donations, and subscriptions.

# Introduction

## Background

Founded in 2011, Twitch was initially a spin-off of the streaming platform Justin.tv. It mainly focuses on video game live streaming, including broadcasts of eSports competitions. Amazon later acquired it in 2014.

## Scope

Design a live-streaming platform where users can watch or broadcast live video streams, especially centered around gaming. The platform should support user registration, live-streaming, chat interactions, channel subscriptions, and advertisements.

## Usage

Twitch is utilized by gamers for live-streaming gameplay, eSports enthusiasts watching tournaments, and other content creators in categories like music, art, and chat shows.

## Competitors

- YouTube Gaming
- Facebook Gaming
- Mixer (defunct as of 2020)
- Caffeine

## Prior experience

Twitch has become the go-to platform for game streaming, with deep integrations into gaming platforms and exclusive broadcasting deals for major eSports tournaments.

# Design

## User journey

1. **Viewers**:

   - Register/Log in
   - Browse or search for live streams.
   - Watch streams and engage via chat.
   - Subscribe to channels or donate to streamers.
   - Watch ads or use bits for interactions.

2. **Streamers**:
   - Register/Log in.
   - Set up their streaming software (e.g., OBS).
   - Start a live stream.
   - Engage with viewers via chat.
   - Monetize streams through ads, donations, subscriptions.

## Services / API's

1. User Service (Registration, Authentication)
2. Streaming Service (Manage live streams)
3. Chat Service (Real-time interactions)
4. Monetization Service (Handle donations, ads, subscriptions)
5. Search and Recommendation Service
6. Analytics Service (Viewer count, engagement metrics)

## Information model

| Entity           | Attributes (Key Attributes in Bold)                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| **User**         | **UserID**, Username, Email, Password, ProfileImage, UserType (Streamer, Viewer)               |
| **Stream**       | **StreamID**, StreamerID (FK to User), Title, Category, LiveStatus, ViewerCount                |
| **ChatMessage**  | **MessageID**, StreamID (FK to Stream), UserID (FK to User), Content, Timestamp                |
| **Subscription** | **SubscriptionID**, SubscriberID (FK to User), StreamerID (FK to User), StartDate, RenewalDate |
| **Donation**     | **DonationID**, DonorID (FK to User), StreamerID (FK to User), Amount, Message, Date           |

## Other

- **Sequence Diagrams**: Show the process of starting a live stream.
- **System Model**: Depict how different services (chat, stream, etc.) interact.
- **Code Examples**: How to set up and manage chat interactions.

# Architecture

## Front-end

- **Web**: ReactJS for a responsive web application.
- **Mobile**: Native apps (iOS - Swift, Android - Kotlin).

## Back-end

- **Web Server**: Node.js with Express.
- **Database**: PostgreSQL for relational data; Redis for real-time chat data.

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into a data warehouse.
- **Analytics**: Use tools like Looker on the data warehouse for business insights.

## Infrastructure

- **Hosting**: AWS EC2 instances.
- **Storage**: AWS S3 for video storage and VODs.
- **CDN**: AWS CloudFront or Akamai for video delivery.
- **Load Balancer**: AWS ELB for traffic distribution.

## Other

- **Algorithms**: Recommendation algorithms to suggest streams.
- **Security**: OAuth for user authentication; SSL/TLS for data encryption; DDoS protection.
- **Protocols**: RTMP for video streaming; WebSocket for real-time chat.
- **Deep Stack**: Elasticsearch for efficient search capabilities.
- **Costs**: Managed by finance; AWS provides a detailed breakdown.
- **Team Size**: Initial team of 100+, scalable as per growth.

---

This design offers a holistic view of Twitch's system. However, in reality, the design would be more intricate, considering global scalability, content delivery nuances, and multiple other intricate factors.
