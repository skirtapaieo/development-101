# Amazon e-commerce

## Clarifying questions

- From an e-commerce perspective - search, product catalog, inventory, recommendation engine, search results, cart, checkout, purchase history
- Nothing like prime, kindle, subscriptions, used items - no
- No country-specific solutions
- 300 million customers, 60,000 order/hour (20/second)
- US is 50% of the orders

## Other experiences

BDS - retail store system (B2C)
EIO - Online store (B2B)
Tele2, Comviq - buy goods and services, in several channels, order management, warehousing, order delivery, logistics, support,
DeLaval - buy digital services

# Summary

Amazon is a comprehensive online retail platform offering millions of products across numerous categories, coupled with services like Prime for faster delivery, streaming, and more.

# Introduction

## Background

Founded in 1994 by Jeff Bezos, Amazon began as an online bookstore but quickly expanded to various other categories, becoming the world's largest online marketplace.

## Scope

To design a digital ecosystem that allows users to browse, search, and purchase a wide array of products, while vendors can list and sell their items, and delivery logistics are optimized.

## Usage

Used by consumers worldwide for online shopping, vendors for selling, and Amazon's logistics for warehousing and delivery.

## Competitors

- eBay
- Walmart (online)
- Alibaba
- Target (online)

## Prior experience

Started as an online bookstore, and over time, expanded its services to incorporate nearly every possible e-commerce feature.

# Design

## User journey

1. **Consumers**:

   - Browse and search products.
   - Review products, see recommendations.
   - Add products to cart and checkout.
   - Track orders, make returns.

2. **Vendors**:

   - List and manage products.
   - Monitor sales and analytics.
   - Handle customer queries and returns.

3. **Logistics & Warehousing**:
   - Process incoming inventory.
   - Pack and ship orders.
   - Handle returns and restocking.

## Services / API's

1. Product Search and Listing Service
2. User Account Management Service
3. Cart and Checkout Service
4. Order Management and Tracking Service
5. Vendor Management Service
6. Inventory and Warehousing Service
7. Recommendation and Personalization Service

## Information model

| Entity      | Attributes (Key Attributes in Bold)                                    |
| ----------- | ---------------------------------------------------------------------- |
| **Product** | **ProductID**, Name, Description, Price, VendorID, StockCount, Rating  |
| **User**    | **UserID**, Username, Password, Email, Address, OrderHistory, Wishlist |
| **Vendor**  | **VendorID**, VendorName, ProductsListed, Rating, FinancialDetails     |
| **Order**   | **OrderID**, UserID, ProductIDs, TotalPrice, OrderStatus, TrackingInfo |

## Other

- **Sequence Diagrams**: Order placement and processing, inventory updates, user registration, and login.
- **System Model**: Interaction between front-end, back-end, payment gateways, warehousing systems, and vendor portals.

# Architecture

## Front-end

- **Web Portal**: Desktop site, optimized for various screen sizes.
- **Mobile App**: iOS and Android applications, streamlined for on-the-go shopping.

## Back-end

- **Web Server**: Backend server, perhaps using Node.js or Java Spring Boot.
- **Database**: SQL for structured data (like product details) and NoSQL (like Amazon DynamoDB) for user activity and cart sessions.

## Data Pipeline

- **ETL Process**: Extract data from various touchpoints (search, purchase, reviews), transform it for analytics, and load into data storage.
- **Analytics**: Use data for business insights, to improve product recommendations, and for targeted marketing.

## Infrastructure

- **Hosting**: AWS infrastructure (given Amazon owns AWS).
- **Storage**: Amazon S3 for storing product images, videos, and user-generated content.
- **Content Delivery Network (CDN)**: Using Amazon CloudFront for faster content delivery.

## Other

- **Algorithms**: Recommendation algorithms based on user behavior, search patterns, and purchase history.
- **Security**: Secure user data, ensure safe transactions through encryption, and protect against DDoS attacks.
- **Protocols**: HTTPS for secure data transmission, various payment gateway-specific protocols.
- **Deep Stack**: Machine learning and AI for advanced product recommendations, fraud detection, and chatbot customer support.
- **Costs**: Infrastructure costs, vendor onboarding, marketing, and advertising costs.
- **Team Size**: Given Amazon's size, multiple cross-functional teams spanning tech, business, operations, and logistics.
