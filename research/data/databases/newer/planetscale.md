# Planetscale

[Site URL](https://planetscale.com/)
[Tutorial URL](https://docs.planetscale.com/tutorials)

## Why should I care of Planetscale?

Planetscale is a scalable, MySQL-compatible relational database built on Vitess. It offers seamless scaling without manual sharding, making it easier to manage large-scale data.

## Who created Planetscale?

PlanetScale was founded by Jiten Vaidya and Sugu Sougoumarane, who are ex-YouTube and Google engineers.

## Why the name Planetscale?

The name "PlanetScale" signifies the platform's ability to scale databases across the globe.

## Why Planetscale was created?

Planetscale was created to provide an easy-to-manage, scalable, and secure database solution that is compatible with MySQL.

## How and when was Planetscale started?

PlanetScale was founded in 2018 and is built on Vitess, an open-source clustering system for horizontal scaling of MySQL.

## Who uses Planetscale?

Developers and companies that need a MySQL-compatible, scalable, and easy-to-manage database service use PlanetScale.

## What are the things that people say Planetscale needs to improve?

- Cost can be a concern for small startups.
- Some users would like more geographically distributed data centers.

## What are the main alternatives to Planetscale (include URLs)?

- AWS RDS ([AWS RDS](https://aws.amazon.com/rds/))
- Google Cloud SQL ([Cloud SQL](https://cloud.google.com/sql))
- CockroachDB ([CockroachDB](https://www.cockroachlabs.com/))

## Overview of the Planetscale stack

PlanetScale uses Vitess as its primary database clustering technology. It supports MySQL and offers a range of APIs and client libraries.

# Using the tool Planetscale

## How to install Planetscale using CLI

\`\`\`bash
npm install -g planetscale
\`\`\`

## How to configure Planetscale

\`\`\`bash
pscale auth login
pscale database create my-database
\`\`\`

## Give a simple example of how to use Planetscale

\`\`\`bash
pscale connect my-database main
\`\`\`

## Give a more complex and full example of what you can do with Planetscale

\`\`\`bash
pscale database create my-database
pscale branch create my-database my-branch
pscale connect my-database my-branch
\`\`\`
