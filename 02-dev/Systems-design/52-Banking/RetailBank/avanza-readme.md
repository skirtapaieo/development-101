# Avanza - Retail Banking & Trading Platform

# Summary

A leading platform in Sweden that offers a comprehensive suite of banking and trading services, including stock trading on domestic and international markets, savings accounts, loans, and more.

# Introduction

This is a high-level system design for Avanza. The specifics of Avanza's actual architecture would be proprietary and complex, tailored to the requirements of the financial industry and the regulatory landscape of Sweden.

## Background

Established in 1999, Avanza has grown to be one of Sweden's most popular platforms for investments and savings, priding itself on low fees and an extensive range of financial products.

## Scope

Design a system that provides users with banking services, the ability to trade on multiple stock exchanges, access to financial information and analytics, and more.

## Usage

Used by both individual retail investors and institutions for banking and investment purposes in Sweden.

## Competitors

- Nordnet
- SEB
- Swedbank
- Handelsbanken

## Prior experience

Known for its user-friendly interface, competitive fees, and comprehensive financial offerings.

# Design

## User journey

1. **Retail Customers**:

   - Register/Log in.
   - View account balance and portfolio.
   - Trade stocks, bonds, and other financial products.
   - Access financial analytics and news.
   - Use banking services like transferring money, setting up savings accounts, etc.

2. **Institutional Clients**:
   - Similar functionalities as retail but with additional features like bulk trading, advanced analytics, etc.

## Services / API's

1. User Service (Registration, Authentication, Profiles)
2. Trading Service (Order execution, Trade history)
3. Banking Service (Account management, Transfers)
4. Analytics and Financial Information Service
5. Portfolio Management Service
6. Notifications and Alerts Service
7. Market Connectivity Service (to connect with exchanges)

## Information model

| Entity          | Attributes (Key Attributes in Bold)                                                |
| --------------- | ---------------------------------------------------------------------------------- |
| **User**        | **UserID**, Username, Email, ProfileImage, TotalPortfolioValue, AccountBalance     |
| **Trade**       | **TradeID**, UserID (FK to User), StockSymbol, Amount, Price, Timestamp            |
| **BankAccount** | **AccountID**, UserID (FK to User), AccountType (e.g., Savings, Checking), Balance |
| **StockInfo**   | **StockSymbol**, CurrentPrice, DailyHigh, DailyLow, Volume, MarketCap              |

## Other

- **Sequence Diagrams**: Order placing, execution, and settlement process.
- **System Model**: Interaction between trading, analytics, and banking services.
- **Code Examples**: Calculation of portfolio value, risk assessments, etc.

# Architecture

## Front-end

- **Web**: Modern frameworks for a responsive and dynamic interface.
- **Mobile**: Native apps for iOS and Android with real-time trading capabilities and notifications.

## Back-end

- **Web Server**: Could be Java-based solutions, popular in the financial industry for performance.
- **Database**: Relational databases like PostgreSQL or Oracle for structured financial data.

## Data Pipeline

- **ETL Process**: Extract from databases, transform for analysis, and load into analytical tools.
- **Analytics**: Custom-built tools or third-party solutions for financial analytics and forecasting.

## Infrastructure

- **Hosting**: Data centers with high security given the financial data's sensitivity.
- **Storage**: High-performance storage solutions given the real-time nature of trading data.
- **CDN**: For efficient delivery of financial news, stock updates, and other real-time information.
- **Load Balancer**: To handle traffic, especially during peak trading hours.

## Other

- **Algorithms**: Algorithms for risk assessment, stock predictions based on historical data.
- **Security**: High focus on security given the sensitivity of financial data. Might include multi-factor authentication, encrypted communication, regular audits.
- **Protocols**: FIX (Financial Information eXchange) for communication with stock exchanges.
- **Deep Stack**: Machine learning for predicting stock movements, analyzing trading patterns.
- **Costs**: High costs associated with real-time trading, data security, and market connectivity.
- **Team Size**: Given the vast array of services, a substantial team across development, finance, security, and operations.
