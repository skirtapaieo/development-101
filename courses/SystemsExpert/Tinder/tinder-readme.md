# Tinder - dating app

<br>

# Summary

Tinder is a dating app that allows users to connect with other singles in their area based on their preferences and location.

**Features**

- Users can create a profile with photos, bio, and preferences (age range, gender, distance).
- Users can swipe right (like) or left (dislike) on other profiles. If two users like each other, it's a match.
- Once matched, users can chat with each other.
- Tinder also offers a variety of features, such as video calling, events, and group swiping/matching.

**Information Model**

The information model for Tinder is relatively simple, consisting of five entities: users, swipes, matches, messages, and feedback.

- **Users:** This entity represents a user of the Tinder app.
- **Swipes:** This entity represents a swipe that a user makes on another user's profile.
- **Matches:** This entity represents a match between two users.
- **Messages:** This entity represents a message that is sent between two users who are matched.
- **Feedback:** This entity represents feedback that a user provides about the Tinder app.

**Relationships**

The relationships between these entities are as follows:

- **User-Swipes:** One-to-many relationship. One user can have many swipes (either likes or dislikes), but each swipe is related to only one user.
- **User-Matches:** Many-to-many relationship. A user can have multiple matches, and each match can connect two different users.
- **Matches-Messages:** One-to-many relationship. A match (between two users) can produce many messages, but each message is tied to one match.
- **User-Feedback:** One-to-many relationship. One user can provide multiple pieces of feedback, but each feedback is tied to a specific user.

<br>

# Introduction

## Background

**Background of Tinder:**

Tinder was launched in 2012 by Sean Rad, Jonathan Badeen, Justin Mateen, Joe Munoz, Dinesh Moorjani, and Whitney Wolfe Herd. It originated within Hatch Labs, a startup incubator funded by IAC (InterActiveCorp). The idea behind Tinder was to leverage the smartphone's geolocation features to simplify and revolutionize the dating scene.

**Challenges Tinder Was Trying to Solve:**

1. **Complexity of Dating Sites**: Prior to Tinder, many dating platforms required filling out extensive profiles, answering a myriad of questions, or even paying upfront. This made the process of setting up an online dating profile cumbersome and discouraging for some. Tinder aimed to simplify this with a straightforward setup and a focus on images and brief profiles.

2. **Stigma Around Online Dating**: At the time, there was still some stigma around online dating. Many platforms felt formal, and there was a certain seriousness attached to them. Tinder, with its casual swiping mechanism, introduced a more laid-back approach, making online dating seem more like a game and less like a commitment.

3. **Safety and Mutual Consent**: One of the challenges in the online dating scene was the unsolicited messages many users, especially women, received from others. By ensuring a chat could only be initiated once a mutual match (both parties swiping right on each other) was established, Tinder introduced an additional layer of consent, helping to reduce unsolicited interactions.

4. **Local Connections**: Many dating platforms allowed users to connect with anyone from anywhere. Tinder's emphasis on local connections, showing profiles of people nearby, made the transition from online interaction to real-life meeting more feasible and spontaneous.

5. **Mobile-First Approach**: Tinder leveraged the rise of smartphones. While other platforms were adjusting to the mobile age, Tinder was designed with mobile in mind from the start, leveraging features like geolocation.

6. **Instant Gratification**: The traditional online dating process could be slow and filled with uncertainty. Tinder's swipe mechanism introduced immediate feedback. The euphoria of getting an instant match when someone you liked liked you back was a novel experience.

7. **Young Demographic**: Tinder specifically catered to the younger generation, mainly college students, at its inception. The platform's design, branding, and marketing catered to this demographic's desire for spontaneity, simplicity, and a fun experience.

In conclusion, Tinder's innovative approach to online dating transformed the landscape. By addressing several challenges that traditional dating platforms posed and by taking advantage of technological trends (like the ubiquity of smartphones), Tinder quickly became a sensation in the world of online dating.

## Scope

- Connect singles within a geographical radius, allowing them to like or pass
- Central to the matching is the user profiles, uploading profile pictures and adding a bio ...
- Adding preferences (age, gender, distance, etc)
- Links to social media, occupation, education, etc
- Profile verification through email and photo
- Matches and chat
- Adjusting preferences
- Boost
- Super like
- Learn preferences also
- In-app purchases, ads
- Safety/privacy
- In-app ratings
- bug reports, etc

## Usage

50 million users on Tinder

## Competitors

There are many competitors - Bumble, Hinge, Match, OkCupid, etc

## Prior experience

# Architecture

## Front-end - react native

## Back-end - node.js, express

## Real-time chat - Socket.io or similar

## Geo-location - Google Maps API

## Data Pipeline - various

## Infrastructure - cloud vendor

## Other

- Algorithms, security, protocols, algorithms, deep stack, costs, team size

# Design

## User journey

Absolutely. Here's a table that outlines the major steps in the core customer journey for a dating app, from registration to matching and chatting, with corresponding services/APIs for each step:

| **Steps in the Customer Journey**   | **Description**                                                                                     | **Services/APIs**                                                                                                   |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **1. Registration**                 | User signs up for the app.                                                                          | - User Management System<br>- OAuth (for social media sign-ups)                                                     |
| **2. Profile Creation**             | User sets up their profile, adding photos, bio, preferences, etc.                                   | - Image Storage (e.g., AWS S3)<br>- Database (e.g., PostgreSQL)                                                     |
| **3. Profile Verification**         | Verification of email, phone, or photos.                                                            | - Email Service (e.g., SendGrid)<br>- SMS API (e.g., Twilio)<br>- Image Recognition API (for photo verification)    |
| **4. Discover Matches**             | User views potential matches based on preferences & location.                                       | - Geolocation API (e.g., Google Maps)<br>- Recommendation Algorithm (e.g., TensorFlow for ML-based recommendations) |
| **5. Swiping & Matching**           | User swipes right (like) or left (dislike) on profiles. If two users like each other, it's a match. | - Real-time Data Processing (e.g., Kafka)<br>- Database for storing likes/dislikes/matches                          |
| **6. Chatting with Match**          | Once matched, users can start a conversation.                                                       | - Real-time Messaging API (e.g., Firebase, Socket.io)                                                               |
| **7. Video Calling** (if supported) | Some apps allow for virtual video dates.                                                            | - Video Calling API (e.g., Agora, Twilio Video)                                                                     |
| **8. Feedback & Reporting**         | Users can report inappropriate users or provide app feedback.                                       | - Feedback Submission System<br>- Reporting Mechanism                                                               |
| **9. Push Notifications**           | Notify users about matches, messages, or app updates.                                               | - Push Notification Service (e.g., Firebase Cloud Messaging, OneSignal)                                             |
| **10. Setting up a Real Date**      | Users decide to meet in person.                                                                     | - Calendar Integration (e.g., Google Calendar API)<br>- Restaurant/Event Booking API (if integrated)                |
| **11. Post-Date Feedback**          | Some apps allow users to provide feedback after a real date.                                        | - Feedback Submission System                                                                                        |

After matching and chatting, what happens next is largely up to the users. They might decide to:

- Continue chatting and get to know each other better.
- Set up virtual or in-person dates.
- Share contact information or connect on other social media platforms.
- Leave feedback or endorsements for each other (some platforms allow this to build trust).
- Or, they might decide they're not a good fit and either unmatch or just stop chatting.

The user journey can loop multiple times, as a user may not find a suitable match on their first try and will return to the discovery and swiping phase.

## Services/APIs

See above table

## Information model

Creating an information model involves identifying the major entities in our system and determining the relationships between them. For a dating app like Tinder, the model can get quite complex, but I'll sketch out a basic one for you.

### **Entities**:

1. **User**:

   - UserID (Primary Key)
   - Name
   - Email
   - Password (hashed)
   - DateOfBirth
   - Gender
   - Preferences (Age range, Gender, Distance)
   - ProfileImage
   - Bio
   - Location (Latitude, Longitude)
   - SocialLinks

2. **Swipes**:

   - SwipeID (Primary Key)
   - UserID (Foreign Key)
   - TargetUserID (The user who is swiped on)
   - SwipeType (Like, Dislike, SuperLike)
   - SwipeTime

3. **Matches**:

   - MatchID (Primary Key)
   - User1ID (Foreign Key)
   - User2ID (Foreign Key)
   - MatchTime

4. **Messages**:

   - MessageID (Primary Key)
   - SenderUserID (Foreign Key)
   - ReceiverUserID (Foreign Key)
   - MessageContent
   - MessageTime

5. **Feedback**:
   - FeedbackID (Primary Key)
   - UserID (Foreign Key)
   - FeedbackContent
   - FeedbackTime

### **Relationships**:

1. **User-Swipes**: One-to-many relationship. One user can have many swipes (either likes or dislikes), but each swipe is related to only one user.

2. **User-Matches**: Many-to-many relationship. A user can have multiple matches, and each match can connect two different users.

3. **Matches-Messages**: One-to-many relationship. A match (between two users) can produce many messages, but each message is tied to one match.

4. **User-Feedback**: One-to-many relationship. One user can provide multiple pieces of feedback, but each feedback is tied to a specific user.

### **Simplified Information Model**:

```
User <--- Swipes
  |      |
  |      |
  V      V
Matches ---> Messages
  |
  |
  V
Feedback
```

This is a basic representation and might need to be expanded based on additional features or nuanced business rules. For example, if you introduce features like video calls, events, or group swiping/matching, then more entities and relationships will be needed.

## Sequence diagrams

TBD

## System model

TBD
