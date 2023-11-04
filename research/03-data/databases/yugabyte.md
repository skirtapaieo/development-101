
# Yugabyte

[Site URL](https://www.yugabyte.com/)
[Tutorial URL](https://learn.yugabyte.com/)

## Why should I care of Yugabyte?

Yugabyte is a high-performance, cloud-native distributed SQL database. It is PostgreSQL-compatible and is designed for resilience and linear scalability.

## Who created Yugabyte?

Yugabyte was founded by former Facebook engineers Kannan Muthukkaruppan, Karthik Ranganathan, and Mikhail Bautin.

## Why the name Yugabyte?

"Yuga" in Sanskrit means an era or an epoch, and "byte" pertains to data. Together, they signify a new era of data storage solutions.

## Why Yugabyte was created?

Yugabyte was created to offer a cloud-native, distributed SQL database that combines the scalability of NoSQL with the ACID guarantees of traditional databases.

## How and when was Yugabyte started?

Yugabyte was founded in 2016.

## Who uses Yugabyte?

Companies requiring high-performance, resilient, and easily scalable databases often choose Yugabyte, especially those in the financial, retail, and telecommunications sectors.

## What are the things that people say Yugabyte needs to improve?

- Complexity in managing and maintaining the system.
- Requires more robust monitoring and debugging tools.

## What are the main alternatives to Yugabyte (include URLs)?

- CockroachDB ([CockroachDB](https://www.cockroachlabs.com/))
- Google Cloud Spanner ([Cloud Spanner](https://cloud.google.com/spanner))
- Amazon Aurora ([Amazon Aurora](https://aws.amazon.com/aurora/))

## Overview of the Yugabyte stack

Yugabyte is based on a sharded, strongly consistent, and highly available document store. It offers YSQL and YCQL APIs for SQL and semi-structured data respectively.

# Using the tool Yugabyte

## How to install Yugabyte using CLI

```bash
./bin/yb-ctl create
```

## How to configure Yugabyte

\`\`\`bash
./bin/yb-ctl --data_dir /my_data add_node
\`\`\`

## Give a simple example of how to use Yugabyte

\`\`\`sql
CREATE TABLE employees (id INT PRIMARY KEY, name TEXT, age INT);
\`\`\`

## Give a more complex and full example of what you can do with Yugabyte

\`\`\`sql
CREATE TABLE orders (id INT PRIMARY KEY, user_id INT, total_amount DECIMAL, created_at TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(id));
INSERT INTO orders VALUES (1, 1, 19.99, NOW());
\`\`\`
