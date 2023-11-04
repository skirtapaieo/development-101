# Cockroach

[Site URL](https://www.cockroachlabs.com/)
[Tutorial URL](https://www.cockroachlabs.com/docs/stable/cockroach-quickstart.html)

## Why should I care of Cockroach?

Cockroach is a cloud-native, distributed SQL database that is designed for horizontal scalability and high availability.

## Who created Cockroach?

Cockroach Labs, the company behind CockroachDB, was founded by three ex-Google engineers: Spencer Kimball, Peter Mattis, and Ben Darnell.

## Why the name Cockroach?

The name "Cockroach" is indicative of the database's resilience and ability to survive failures.

## Why Cockroach was created?

CockroachDB was created to bring together the best aspects of SQL databases with the scalability and resilience of NoSQL databases.

## How and when was Cockroach started?

Cockroach Labs was founded in 2015.

## Who uses Cockroach?

Organizations requiring a scalable and resilient database solution, especially in industries like finance, retail, and healthcare, use CockroachDB.

## What are the things that people say Cockroach needs to improve?

- Complexity in setup and maintenance.
- Higher operational costs compared to traditional databases.

## What are the main alternatives to Cockroach (include URLs)?

- Google Cloud Spanner ([Cloud Spanner](https://cloud.google.com/spanner))
- Yugabyte ([Yugabyte](https://www.yugabyte.com/))

## Overview of the Cockroach stack

CockroachDB uses a distributed SQL engine and is built on a transactional and strongly-consistent key-value store.

# Using the tool Cockroach

## How to install Cockroach using CLI

\`\`\`bash
wget -qO- https://binaries.cockroachdb.com/cockroach-v21.1.0.linux-amd64.tgz | tar  xvz
\`\`\`

## How to configure Cockroach

\`\`\`bash
cockroach start --insecure --store=node1 --listen-addr=localhost:26257
\`\`\`

## Give a simple example of how to use Cockroach

\`\`\`sql
CREATE DATABASE my_db;
\`\`\`

## Give a more complex and full example of what you can do with Cockroach

\`\`\`sql
BEGIN;
INSERT INTO accounts VALUES (1, 1000), (2, 250);
COMMIT;
\`\`\`

