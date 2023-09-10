# System Designs

<br>

## Course: Algoexpert Systems Design

## Made a set of systems design with a few areas:

##

- Exchanges - end-customers meet exchanges (betting and stocks and so on)
- Human Resources (employee perspective) - for developer interview preparation - Algoexpert platform (from Algoexpert exercise)
- Code - Code Deployment system (from Algoexpert exercise)
- Social - Feed-based system (from Algoexpert exercise)
- Streaming - Spotify (from Youtube/iGotanOffer)

- [Global and Fast Code Deployment system - from Algoexpert](#1-code-deployment-system)

## Twitch

## Airbnb

## Slack

## Tinder

## Uber

## Netflix

/Netflix

## Google Drive

## Reddit

/Reddit - post, comments, vote, awards

## Amazon (e-commerce)

/Amazon - e-commerce

## Exchanges - Stock Exchange

/Exchange - a lot of architecture, complexity in real-time protocol, and matching/settling order. Two cases, from iGaming, where we in one case use Cinnobers trading, one were we built it ourselves

<br>

## Code-deployment system

design a code deployment system (part of exercise at Algoexpert/System design)

# Index

- [System design](#system-design)
- [The initial questions](#the-initial-questions)
- [Detailed system design questions](#detailed-system-design-questions)
  - [Scope and Scale](#scope-and-scale)
  - [Target Environments](#target-environments)
  - [Security Requirements](#security-requirements)
  - [Versioning and Rollbacks](#versioning-and-rollbacks)
  - [Deployment Workflow](#deployment-workflow)
  - [Monitoring and Logging](#monitoring-and-logging)
  - [Network and Infrastructure](#network-and-infrastructure)
  - [Compliance and Governance](#compliance-and-governance)
  - [Integration and Compatibility](#integration-and-compatibility)
  - [Team and Roles](#team-and-roles)
- [First pass of the system design](#first-pass-of-the-system-design)
  - [Global Deployment](#global-deployment)
  - [Deployment Frequency and Rollbacks](#deployment-frequency-and-rollbacks)
  - [Uptime and Performance](#uptime-and-performance)
  - [Integration with Code Reviews and Build Systems](#integration-with-code-reviews-and-build-systems)
  - [Automation and Orchestration](#automation-and-orchestration)
  - [Monitoring and Alerting](#monitoring-and-alerting)
  - [Security and Access Control](#security-and-access-control)
  - [Training and Documentation](#training-and-documentation)
- [The system overview](#the-system-overview)

# System design (result of below)

![Alt text of the image](https://github.com/skirtapaieo/codedeployment/blob/main/systemdesign.png)

# The initial questions

- The first questions is of course buy or build, but for the point of the exercise we will ask the questions needed for a design, and a later implementation.
- The second questions is whether this suits the company and the overall architecture and
- whether the resources are in place to, after the design, actually be able to build the system.

As shown later in the design phase, it is pretty complicated.

# Detailed system design questions

The following, and other questions will help us to understand the specific requirements and constraints of the code-deployment system, enabling you to design a solution the meets the needs of the organisation.

## Scope and Scale

- How many locations or regions will the system need to support globally?
- What is the expected number of deployments per day or per hour?
- Are there any specific performance or latency requirements?

## Target Environments

- What types of environments will the code be deployed to (e.g., cloud-based, on-premises, hybrid)?
- Are there any specific platforms, operating systems, or architectures that need to be supported?

## Security Requirements

- What security measures need to be in place to protect the code during deployment?
- Are there any specific authentication or authorization requirements?
- Is there a need for encryption or secure communication channels?

## Versioning and Rollbacks

- How should the system handle versioning of the deployed code?
- Is there a need for the ability to rollback to a previous version in case of issues or failures?

## Deployment Workflow

- What is the desired workflow for code deployment (e.g., continuous integration/continuous deployment, manual approval process)?
- Are there any specific pre-deployment or post-deployment tasks that need to be performed?

## Monitoring and Logging

- What metrics and logging information should be captured during deployment?
- Are there any specific monitoring or alerting requirements in case of deployment failures?

## Network and Infrastructure

- What are the available network bandwidth and infrastructure capabilities across different regions?
- Are there any limitations or considerations related to firewalls, load balancers, or other networking components?

## Compliance and Governance

- Are there any compliance requirements or industry-specific regulations that need to be considered during code deployment?

## Integration and Compatibility

- Does the code-deployment system need to integrate with any existing tools or systems (e.g., version control, configuration management)?
- Are there any dependencies or restrictions regarding the technologies or programming languages used in the code?

## Team and Roles

- Who will be responsible for managing and operating the code-deployment system?
- What are the roles and responsibilities of the individuals involved in the deployment process?

# First pass of the system design

- The system is supposed to exist in five different physical locations
- where binaries have to be deployed reliably and
- where the system have to be performance enought to do the deployment within a few minutes

## Global Deployment

- With around 5 locations, you need to ensure that the system can efficiently distribute deployments across these locations while maintaining consistent performance.
- Consider using a distributed architecture with local deployment servers in each location to minimize latency and network bottlenecks.

## Deployment Frequency and Rollbacks

- Supporting hundreds of deployments per day requires an automated and streamlined process.
- Implement a robust versioning system that allows easy rollback to previous versions if issues occur.
- Define a clear rollback strategy to handle failures, including a mechanism to roll forward quickly once the issue is resolved.

## Uptime and Performance

- To achieve 99.9% uptime, consider implementing redundancy and failover mechanisms across the deployment system.
- Optimize the deployment process to minimize downtime during deployments, aiming for a maximum build and deploy time of 30 minutes.
- Utilize load balancing and resource scaling techniques to handle increased demand during peak deployment periods.

## Integration with Code Reviews and Build Systems:

- Leverage the existing code review and build systems to ensure the quality and integrity of the code being deployed.
- Integrate the code-deployment system with the code review system to enforce checks and balances before allowing deployment.

## Automation and Orchestration

- Automation is crucial for managing a high volume of deployments.
- Implement a robust deployment pipeline that automates the steps from code submission to production deployment, including testing and verification.

## Monitoring and Alerting

- Set up comprehensive monitoring and logging capabilities to track the performance, health, and success of deployments.
- Implement real-time alerts to notify relevant teams or individuals in case of deployment failures or anomalies.

## Security and Access Control

- Ensure proper authentication and authorization mechanisms are in place to prevent unauthorized access to the deployment system.
- Consider using secure communication protocols (e.g., HTTPS) to protect sensitive data during code deployment.

## Training and Documentation:

- Provide training and documentation to users and stakeholders to ensure smooth adoption and understanding of the code-deployment system.
- Document best practices, guidelines, and troubleshooting procedures to assist users in case of issues.

By addressing these considerations, it is possible to design a global and fast code-deployment system that meets the specified requirements and supports efficient and reliable deployments across your organization.

# The system overview

Based on the description above we asked ChatGPT to generate a high-level sketch in PlantUML notation. _See Systemdesign.uml_
