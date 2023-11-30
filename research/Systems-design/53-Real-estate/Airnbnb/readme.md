# Airbnb - Online Marketplace for Lodging

# Summary

An online platform that connects hosts who want to rent out their homes to guests looking for accommodations in those locales.

# Introduction

## Background

Founded in 2008 in San Francisco, Airbnb began as a simple idea to earn extra cash by renting out an air mattress on the floor. It has since transformed into a global marketplace for unique homes and experiences.

## Scope

Design an online platform for listing and booking lodgings. It should support user registration, listing creation, search, booking, payments, and reviews.

## Usage

Airbnb is used by travelers seeking short-term rentals and experiences, and hosts looking to monetize their spaces. They have 50 million users and 1 million listings.

## Competitors

- Booking.com
- Vrbo
- Expedia
- Hotels.com
- Couchsurfing

## Prior experience

Not really, this is a first attempt, based on exercises in AlgoExpert.

# Design

## User journey

1. **Guests**:

   - Register/Log in
   - Search listings by location, date, type, and price.
   - View listing details (photos, description, reviews).
   - Book a listing.
   - Complete the stay.
   - Review the host and listing.

2. **Hosts**:
   - Register/Log in.
   - Create a listing (add photos, set price, availability).
   - Receive booking requests or instant bookings.
   - Host the guests.
   - Review the guests.

## Services / API's

1. User Service (Registration, Authentication)
2. Listing Service (CRUD operations for listings)
3. Search Service (Find listings based on filters)
4. Booking Service (Handle reservations)
5. Payment Service (Manage transactions)
6. Review Service (Manage feedback and ratings)

## Information model

| Entity          | Attributes (Key Attributes in Bold)                                                               |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **User**        | **UserID**, Name, Email, Password, ProfileImage, UserType (Host, Guest)                           |
| **Listing**     | **ListingID**, Address, Price, Type, Description, Photos, Availability, HostID (FK to User)       |
| **Booking**     | **BookingID**, GuestID (FK to User), ListingID (FK to Listing), StartDate, EndDate, PaymentStatus |
| **Review**      | **ReviewID**, Content, Rating, ReviewerID (FK to User), ListingID (FK to Listing)                 |
| **Transaction** | **TransactionID**, Amount, Date, BookingID (FK to Booking), PayerID (FK to User)                  |

## Other

- **Sequence Diagrams**: Show interactions for the booking process.
- **System Model**: Outline how microservices communicate.
- **Code Examples**: CRUD operations for Listings.

# Architecture

## Front-end

- **Web**: ReactJS for a responsive web application.
- **Mobile**: Native apps (iOS - Swift, Android - Kotlin).

## Back-end

- **Web Server**: Node.js with Express.
- **Database**: PostgreSQL for relational data; MongoDB for unstructured data (reviews, user profiles).

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into a data warehouse.
- **Analytics**: Use Tableau or Looker on data warehouse to derive business insights.

## Infrastructure

- **Hosting**: AWS EC2 instances.
- **Storage**: AWS S3 for photos and static content.
- **Load Balancer**: AWS ELB to distribute incoming traffic.

## Other

- **Algorithms**: Search algorithms to provide the most relevant listings.
- **Security**: OAuth for user authentication, SSL/TLS for data encryption.
- **Protocols**: HTTP/HTTPS for web traffic.
- **Deep Stack**: Redis for caching frequently accessed data.
- **Costs**: Managed by the finance team; AWS provides cost breakdowns.
- **Team Size**: Initial team of 50, scalable as per growth.

---

This is a high-level system design for Airbnb. A real-world design would go much deeper, considering specifics like global scalability, disaster recovery, optimization strategies, and much more.
