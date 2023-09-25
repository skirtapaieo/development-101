# Uber - ride-sharing service etc

**Summary**

**Introdution**

- [Background](#background)
- [Scope](#scope)
- [Competitors](#competitors)
- [Riders and Drivers](#riders-and-drivers)
- [Prior Experiences](#prior-experiences)

**Design**

- [Use Cases](#use-cases)
- [Interactions, Services/API's and Description](#interactions-servicesapis-and-description)
- [Information Model](#information-model)
- [The Tricky Parts of the Service](#the-tricky-parts-of-the-service)
  - [Rider and Driver Tracking](#rider-and-driver-tracking)
    - [Area 1 - Proximity Matching](#area-1---proximity-matching)
      - [Roads are networks](#roads-are-networks)
      - [Tools available](#tools-available)
      - [For ride hailing (or other types of matching)](#for-ride-hailing-or-other-types-of-matching)
    - [Area 2 - Concurrent requests](#area-2---concurrent-requests)
      - [Geospatial Data Structures](#geospatial-data-structures)
      - [Time-to-arrival (ETA) Estimation](#time-to-arrival-eta-estimation)
      - [Stale Data](#stale-data)
      - [Fairness](#fairness)

** Architecture**

# Summary

In this document, we have discussed the design of a ride-sharing service like Uber. We have identified the key use cases, interactions, and services that are required to implement such a system. We have also discussed some of the challenges that need to be addressed in order to build a reliable and scalable ride-sharing service.

The design presented in this document is just a starting point. There are many other factors that need to be considered when building a real-world ride-sharing service. However, the concepts discussed in this document provide a good foundation for understanding the challenges and opportunities of building such a system.

Here are some of the key takeaways from this document:

- Ride-sharing services are complex systems that require a variety of services and APIs to function.
- The design of a ride-sharing service needs to take into account the rider and driver experience, as well as the efficiency of the system (the central parts)
- There are a number of challenges that need to be addressed in order to build a reliable and scalable ride-sharing service, such as rider and driver tracking, proximity matching, and time-to-arrival estimation.

# Introduction

## Background

- Ubers first ride was in 2009
- Have had problems with traditional Taxi regulations
- Does not employ the drivers - been criticized for that
- Problems being addressed - availability, reliabiltiy, transparency, easy to pay, rating system, marketplace flexibility, cost, economic opportunities for car owners, safety features

## Scope

Uber have a lot of variations in their services: X, XL, Pool, Black, SUV, Comfort, Green, depending on the cars in their fleet. Also Eats, Freight, Air.

The core though passenger-facing and driver-facing services, which we will redesign.

## Competitors et misc

They have many competitors, like Bolt (Europe), Lyft (US), DiDi (China), Ola (India), Grab (south-east asia), Yandex (Russia).

Voi is a swedish electric scooter company, it has a slightly simpler, but similar service. Tipptapp is also a service similar to this.

## Riders and Drivers

Uber has 5 million active drivers - and 100 million monthly active riders - and in 2022 Uber completed over 10 billion rides. So each driver make 2 000 rides/year, or 5 per day.

The fleet includes over 40 different vehicle types, ranging from sedans to luxury vehicles.

## Prior experiences

I started a side project on boats otherwise nothing but this exercise, which will help me with the boat side-project.

# Design

## Use cases

- a user/passenger hails a ride from A to B, it is possible to cancel
- they ask for a certain type of ride (depends on drivers available
- drivers, being tracked and active, address their interest to take the drive
- a match is made with the best match driver
- driver can be tracked,
- the position of the passenger is known for the driver
- a pickup is made
- drive is performed
- target route should be followed? Or else?
- drive is done
- payment is done
- payment is managed
- rating is performed by user

## Interactions, services/API's and description

The central use case of hailing a ride in the Uber system can be broken down into a series of interactions between the rider, driver, and Uber's central systems.

| #   | Interaction                             | Actor        | Service/API                       | Description                                                                           |
| --- | --------------------------------------- | ------------ | --------------------------------- | ------------------------------------------------------------------------------------- |
| 1   | Request a ride                          | Rider        | `RideRequestService`              | Allows rider to input destination, choose car type, and view estimated fare.          |
| 2   | Cancel a ride (if needed)               | Rider        | `RideCancellationService`         | Gives rider the option to cancel a requested ride within a stipulated time.           |
| 3   | Broadcast ride request                  | Uber Central | `RideBroadcastService`            | Notifies available drivers about a new ride request based on criteria like proximity. |
| 4   | Show available rides                    | Driver       | `AvailableRidesService`           | Drivers can view details of rides nearby and choose to accept or decline.             |
| 5   | Accept the ride request                 | Driver       | `RideAcceptanceService`           | Driver signals intention to pick up the passenger.                                    |
| 6   | Match driver with rider                 | Uber Central | `RideMatchingService`             | Chooses the best match driver for the rider based on various criteria.                |
| 7   | Notify rider of matched driver          | Rider        | `RideNotificationService`         | Rider gets details of the driver, car, and estimated time of arrival.                 |
| 8   | Track driver's location                 | Rider/Uber   | `DriverLocationTrackingService`   | Displays the real-time location of the driver to the rider and Uber Central.          |
| 9   | Share rider's location                  | Driver       | `RiderLocationService`            | Provides the driver with the rider's current location for pickup.                     |
| 10  | Pickup rider                            | Driver       | ---                               | Physical action, no direct API interaction.                                           |
| 11  | Suggest optimal route                   | Driver/Uber  | `RouteSuggestionService`          | Gives the driver the best route based on traffic, distance, etc.                      |
| 12  | Monitor route deviation (if any)        | Uber Central | `RouteDeviationMonitoringService` | Checks if the driver is following the suggested route or deviating for valid reasons. |
| 13  | Complete the ride                       | Driver       | `RideCompletionService`           | Marks the ride as completed upon reaching the destination.                            |
| 14  | Calculate and process payment           | Rider/Uber   | `PaymentProcessingService`        | Automatically charges the rider based on the fare and distance traveled.              |
| 15  | Rate the driver                         | Rider        | `DriverRatingService`             | Allows the rider to give feedback and rate the driver post-ride.                      |
| 16  | Rate the rider (if the platform allows) | Driver       | `RiderRatingService`              | Allows the driver to rate the rider, which can influence rider behavior.              |

This table gives a high-level view of the interactions and associated services/APIs. Each service can further have multiple methods, and the actual implementations might involve more granularity and detail.

## Information model

this is simplified and meant to give a visual depiction of the entities and their attributes. In real-world scenarios, data normalization and other best practices would be applied for efficient database design.

### Rider Table:

| riderID | name     | email             | phone      | paymentMethod        | rating |
| ------- | -------- | ----------------- | ---------- | -------------------- | ------ |
| 1001    | John Doe | johnd@example.com | 1234567890 | Credit Card \*\*\*\* | 4.7    |

### Driver Table:

| driverID | name        | email             | phone      | carDetails             | rating |
| -------- | ----------- | ----------------- | ---------- | ---------------------- | ------ |
| 5001     | Alice Smith | alice@example.com | 9876543210 | Toyota Camry '20 - XYZ | 4.9    |

### Ride Table:

| rideID | riderID | driverID | startLocation | endLocation | startTime      | endTime         | fare | route     |
| ------ | ------- | -------- | ------------- | ----------- | -------------- | --------------- | ---- | --------- |
| 8001   | 1001    | 5001     | Point A       | Point B     | 2023-08-09 9AM | 2023-08-09 10AM | $15  | A > X > B |

### Payment Table:

| paymentID | riderID | rideID | amount | paymentMethod        | timestamp       |
| --------- | ------- | ------ | ------ | -------------------- | --------------- |
| 9001      | 1001    | 8001   | $15    | Credit Card \*\*\*\* | 2023-08-09 10AM |

### Rating Table:

| ratingID | riderID | driverID | rideID | score | feedback                    |
| -------- | ------- | -------- | ------ | ----- | --------------------------- |
| 7001     | 1001    | -        | 8001   | 5     | Great and smooth drive!     |
| 7002     | -       | 5001     | 8001   | 4     | Rider was polite and quiet. |

For simplification, the '-' denotes missing or non-applicable data in the tables. In an actual database, you'd want to use NULL or another appropriate representation.

## The big challenges

### A - Rider and Driver tracking

These are tightly related and they deal with real-time location tracking and sharing.

- Real-time updates
- Accuracy
- Privacy concerns
- Network & battery efficiency

### B - Ride Matching Service

#### Area 1 - Proximity Matching

##### Roads are networks

Finding the nearest driver is not a simple make a line from A to B.

- The roads are networks- with nodes, edges, properties/weights and so on
- Algorithms such as Dijkstras algorithm or A\* can help finding shortest path
- Reality adds complexity - overpasses/underpasses, tunnels, closed for maintenance, temporarily blocked due to incidents, traffic conditions
- Dynamic updates - mapping system try to incorporate real-time data to match models with reality

Finding the nearest driver assumes a good underlying mapping system, for routing, estimating time to arrival between A and B.

##### Tools available

There are tools available such as

- OpenStreetMap (OSM) and OSRM (OpenStreetMap Routing Machine) that is an open source collaborative project
- Graphhopper - uses OSM to calculate routes
- MAP APIs - major map providers like Google Maps, Bing and Mapbox provide API för distance and routing calculations and can be used for proximity matching

##### For ride hailing (or other types of matching)

- Use above tools as a start
- Update drivers locations - and recalculate ETA
- On ride requests - find potential matches, sort by driver rating, vehicle type, etc
- Do on the fly computation for matching, which might be more resous intensive, but will use most up-to-date data
- Doing a straightline calculation followed by other more intricated calculations if needed

#### Area 2 - Concurrent requests

There are many aspects to matching concurrently, in ride hailing ...

Matching in high-demand, active zones for ride-hailing services like Uber or Lyft the matching problem involves spatial factors, driver availability, rider preferences, time, traffic conditions, and more. Here are some approaches and considerations:

1. **Geospatial Data Structures**: Data structures like KD-trees, Quad-trees, or Geohash can help in efficiently querying drivers that are nearby to a rider.

2. **Priority Queue**: For each ride request, a priority queue can be set up where drivers are prioritized based on factors like proximity, ratings, or vehicle type. The top driver in the queue gets the ride request first.

3. **Dynamic Matching**: Especially in busy zones, it might be beneficial to have a dynamic matching system. As conditions change (e.g., a driver becomes occupied), the system can reevaluate and reshuffle matches.

4. **Supply-Demand Balancing**: During high demand, surge pricing or other incentives can be introduced to balance the demand with the available supply of drivers.

5. **Batch Processing**: If there are multiple requests and drivers available concurrently, the system might batch these together and solve the matching problem for the entire batch, ensuring overall efficiency. This resembles stock exchange mechanisms.

6. **Stable Matching** using algorithms like the **Gale-Shapley Algorithm**: This is used to solve the Stable Marriage Problem but can be adapted for scenarios where you want to ensure that once a rider is matched with a driver, the match remains stable, i.e., another rider cannot take away that driver unless the first rider cancels.

7. **Learning-based Approaches**: Machine learning models can predict demand in various zones and direct drivers to position themselves optimally, aiding in quicker matches when requests come in.

8. **Real-time Adjustments**: The system can also monitor accepted vs. rejected requests in real-time. If many requests are being rejected by drivers in a zone, the system can adjust parameters or introduce incentives.

### C - Pricing, fare adjustments and payments

Uber's fare system is built around dynamic pricing, and there can be several reasons for fare adjustments. While I don't have an exact number for how many fare adjustments Uber processes (as this would depend on numerous factors and can vary across regions and time), the reasons for fare adjustments generally fall into several categories:

1. **Technical Issues**: Sometimes, there might be glitches or errors in the app that cause discrepancies in the fare. This could be due to GPS inaccuracies, server issues, or other technical glitches.

2. **Rider Complaints**: If a rider feels they were charged unfairly, perhaps due to a longer route taken by the driver or other reasons, they can file a complaint. If Uber finds the claim valid, they might adjust the fare.

3. **Driver Reports**: Similar to riders, drivers can also report issues. For instance, if a rider made a stop during the trip that was not accounted for in the fare, the driver can report it, leading to a fare adjustment.

4. **Promotions & Refunds**: Sometimes, Uber provides promotions, discounts, or special offers. If a rider was eligible for a promotion but it wasn't applied during billing, a fare adjustment might be done retroactively.

5. **Surge Pricing Adjustment**: Uber's dynamic pricing model, often referred to as "surge pricing", adjusts fares based on the demand for rides in a specific area. If there's an issue or miscalculation related to surge pricing, adjustments might be needed.

6. **Safety Issues**: If there was a safety incident or a severe violation of Uber's community guidelines during a ride, it could lead to a fare being adjusted or even fully refunded.

7. **External Factors**: Events outside of Uber's control, like road closures, extreme weather conditions, or significant public events, can sometimes cause unexpected detours or delays. If these result in a significantly higher fare, adjustments might be considered.

8. **Incomplete Trips**: If a trip is cut short for any reason – maybe the rider chose to get off earlier than the destination or there was an issue with the vehicle – a fare adjustment might be needed.

Riders and drivers can report fare discrepancies through the app, and Uber typically reviews these reports to determine if an adjustment is warranted. Given the millions of rides Uber processes, it's reasonable to assume that a small percentage of them might need fare adjustments.

### System model

TBD

## Architecture

TBD - focus was on design

- Front-end - passenger app and driver app
- Back-end -
- Data -
- Infrastructure -
- Other - security, protocols, algorithms, deep stack, costs, team size,etc
