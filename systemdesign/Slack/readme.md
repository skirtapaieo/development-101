# Slack - Cloud-based team collaboration

# Summary

TBD

# Introduction

## Background

Slack was founded by Stewart Butterfield, Eric Costello, Cal Henderson, and Serguei Mourachov. Interestingly, Slack began as an internal communication tool for a different project led by Stewart Butterfield: a gaming company called Tiny Speck, which was working on a game named "Glitch". When "Glitch" was shut down in 2012 due to limited success, the team realized that the communication platform they'd built for themselves had potential as a standalone product.

The problems Slack is trying to solve is fragmented communication, email overload, real-time collaboration, integration with other tools, transparency and openness, remote and distributed teams, customization and scalability. Which Slack and its competitors have been quite successful with.

## Scope

Build on channels, direct messaging to channels and individuals, notifications, integrations with google drive, github and many more, and provide voice and video calls, also on the messages there are tools to save, pin, add emojis, writing code snippets and text blocks.

But we will focus on the core messaging functionality - notifications and synchronization - one on one and in group channels. Main focus is on the back-end.

## Usage

Slack has around 20 million users, as a comparison Microsoft teams have around 145 million (Jan-2023)

## Competitors

- Discord: open source
- Microsoft Teams: Targeted at businesses, offers chat, video conferencing, and integration with Microsoft Office products.
- Zoom Chat: While Zoom is more known for its video conferencing, it also has chat functionality.
- Trello (Butterfly): Although Trello is a project management tool, its newer chat functionality, Butterfly, puts it in competition with Slack.
- Mattermost: An open-source, self-hosted alternative to Slack.
- Rocket.Chat: Another open-source team chat software.

## Prior experience

I have made simple chats, message systems, in a galaxy far far away ... so this will be fun!

# Design

## The special thing

The special thing is that is can represent teams, make public and private, but you can also add larger groups like tribes/departments, within one common workspace, which creates a unit. It is also possible to add general channels, task forces and other kinds of communication groups. Channels is a very suitable foundation for this.

This is fully replicable in Microsoft Teams, but you have to, in both cases have "your tongue in the right place", and design the experience a little bit.

## Use cases

Certainly! For the "Technology Used" column, I'll provide a broad overview of the technologies or methods associated with each use case, though it's important to note that exact technologies might be proprietary to Slack or might have evolved since my last update in September 2021.

| Rank | Use Case                      | Associated Services/APIs                                                                                 | Technology Used                                                                                                                                |
| ---- | ----------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Channel Communication**     | - Public Channels<br>- Private Channels<br>- Multi-workspace Channels                                    | - WebSockets for real-time updates<br>- Backend services (likely in PHP & Java)<br>- Databases for storing messages                            |
| 2    | **Direct Messaging**          | - 1:1 Direct Messages<br>- Group Direct Messages (with multiple individuals)                             | - WebSockets for real-time communication<br>- Backend services<br>- Databases for message storage                                              |
| 3    | **Notifications**             | - Desktop Notifications<br>- Mobile Notifications<br>- Email Notifications<br>- Activity & Mentions Feed | - Push Notification Services<br>- Email Servers<br>- Client-side libraries for desktop notifications                                           |
| 4    | **Integrations**              | - Slack App Directory (for tools like Google Drive, GitHub, etc.)<br>- Webhooks<br>- Custom Bots         | - OAuth for authentication<br>- RESTful APIs & Webhooks<br>- Javascript for bots                                                               |
| 5    | **Voice and Video Calls**     | - Native Slack Calls (1:1 and group)<br>- Integration with Zoom, Microsoft Teams, etc.                   | - WebRTC for real-time communication<br>- Integration APIs for third-party services                                                            |
| 6    | **Message Tools**             | - Pinning Messages<br>- Saving Messages<br>- Emojis & Reactions<br>- Threads                             | - Client-side libraries for UI/UX<br>- Backend services for storing pinned/saved messages                                                      |
| 7    | **Rich Formatting & Sharing** | - Code Snippets<br>- Text Blocks<br>- File Upload & Sharing (e.g., Google Drive integration)             | - Markdown or similar formatting languages<br>- Cloud storage integrations (like Google Drive API)<br>- Syntax highlighting libraries for code |
| 8    | **Privacy & Security**        | - Two-factor Authentication<br>- Enterprise Key Management<br>- Data Encryption                          | - Authentication protocols (like OAuth)<br>- Encryption libraries and protocols<br>- Secure data storage methods                               |

This table provides a high-level overview, and the underlying technologies for each feature in Slack are likely more complex and multi-faceted.

## Services / API's

See above table

## Information model

Certainly, I'll create a tabular representation of the entities and their primary attributes based on the information model I've described:

| Entity                  | Attributes (Key Attributes in Bold)                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| **User**                | **UserID**, Name, Email, ProfileImage, Role (Admin, Member, Guest)                                     |
| **Channel**             | **ChannelID**, ChannelName, ChannelType (Public, Private), Topic, CreationDate                         |
| **Direct Message (DM)** | **DMID**, SenderID (Foreign Key to User), ReceiverID (Foreign Key to User), Content, Timestamp         |
| **Message**             | **MessageID**, Content, Timestamp, FileType (Text, Image, Video, etc.), SenderID (Foreign Key to User) |
| **Integration**         | **IntegrationID**, IntegrationName, Description, APIKey                                                |
| **Notification**        | **NotificationID**, Type (Message, Mention, etc.), Status (Read, Unread), User (Foreign Key to User)   |

The table gives a clear overview of each entity and its main attributes, simplifying the model for easier understanding. Remember, this is a basic representation, and Slack's actual data model would be far more intricate and detailed.

## Other

- Sequence diagrams, system model, code examples

# Architecture

## Front-end

## Back-end

## Data Pipeline

## Infrastructure

## Other

- Algorithms, security, protocols, algorithms, deep stack, costs, team size
