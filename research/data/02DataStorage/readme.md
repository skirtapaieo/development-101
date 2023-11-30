# Data Storage

# Data Storage

| Data Storage Tool          | Example(s)                       | Principle & Technology                                 | Strengths                               | Weaknesses                                        |
| -------------------------- | -------------------------------- | ------------------------------------------------------ | --------------------------------------- | ------------------------------------------------- |
| RDBMS                      | PostgreSQL, MySQL, Oracle        | Tables, SQL                                            | ACID compliance, data integrity, mature | May not scale horizontally efficiently            |
| NoSQL Databases            | MongoDB, Cassandra, Redis, Neo4j | Various (based on type)                                | Scalable, flexible schema               | Lack of standardization, may lack full ACID       |
| Distributed File Systems   | HDFS, GlusterFS                  | Treat multiple machines as a single file system        | Scalable, fault-tolerant                | Complexity of setup and maintenance               |
| Object Storage             | Amazon S3, Google Cloud Storage  | Objects with ID, metadata, and blob data, RESTful APIs | Scalable, durable                       | Higher latency than block storage                 |
| Data Warehousing Solutions | Amazon Redshift, Google BigQuery | Analytics and reporting, SQL, columnar storage         | Fast querying, scalable                 | Can be expensive, not for transactional workloads |

# Mapping Data storage To Data Ingestion

| Data Storage Category      | Data Size & Type   | Recommended Solution(s)                                                     |
| -------------------------- | ------------------ | --------------------------------------------------------------------------- |
| RDBMS                      | Small - Batch      | SQLite, MySQL                                                               |
|                            | Small - Streaming  | MySQL with binlog streaming, PostgreSQL with logical replication            |
|                            | Medium - Batch     | PostgreSQL, Microsoft SQL Server                                            |
|                            | Medium - Streaming | PostgreSQL with logical replication, Amazon RDS with streaming extensions   |
|                            | Large - Batch      | Oracle, Amazon Aurora, Microsoft SQL Server Enterprise                      |
|                            | Large - Streaming  | Amazon Aurora with replication, Oracle GoldenGate                           |
| NoSQL Databases            | Small - Batch      | MongoDB, Redis                                                              |
|                            | Small - Streaming  | Redis Streams, MongoDB Change Streams                                       |
|                            | Medium - Batch     | Cassandra, MongoDB, Redis Cluster                                           |
|                            | Medium - Streaming | Cassandra with Kafka, MongoDB Change Streams                                |
|                            | Large - Batch      | Cassandra, MongoDB Atlas, Amazon DynamoDB                                   |
|                            | Large - Streaming  | Amazon DynamoDB Streams, Cassandra with Kafka                               |
| Distributed File Systems   | Small - Batch      | Not typically used for small datasets                                       |
|                            | Small - Streaming  | Not typically used for small datasets                                       |
|                            | Medium - Batch     | HDFS                                                                        |
|                            | Medium - Streaming | HDFS with Apache Kafka                                                      |
|                            | Large - Batch      | HDFS, GlusterFS                                                             |
|                            | Large - Streaming  | HDFS with Apache Kafka, Apache Flink                                        |
| Object Storage             | Small - Batch      | Amazon S3, Google Cloud Storage                                             |
|                            | Small - Streaming  | AWS Lambda triggered by S3 events, Google Cloud Functions triggered by GCS  |
|                            | Medium - Batch     | Amazon S3, Google Cloud Storage, Azure Blob Storage                         |
|                            | Medium - Streaming | Amazon Kinesis Firehose to S3, Google Pub/Sub to GCS                        |
|                            | Large - Batch      | Amazon S3, Google Cloud Storage, Azure Blob Storage                         |
|                            | Large - Streaming  | Amazon Kinesis Firehose to S3, Google Pub/Sub to GCS                        |
| Data Warehousing Solutions | Small - Batch      | Amazon Redshift, Google BigQuery                                            |
|                            | Small - Streaming  | Google BigQuery Streaming, Amazon Redshift with Kinesis                     |
|                            | Medium - Batch     | Amazon Redshift, Snowflake, Google BigQuery                                 |
|                            | Medium - Streaming | Snowflake Snowpipe, Google BigQuery Streaming                               |
|                            | Large - Batch      | Amazon Redshift Spectrum, Snowflake, Google BigQuery                        |
|                            | Large - Streaming  | Snowflake Snowpipe, Google BigQuery Streaming, Amazon Redshift with Kinesis |

# Examples - based on medium cases

Sure! Here are code examples for the "medium" case for various data storage categories, demonstrating basic operations related to customer, order, and behavior data:

### 1. RDBMS (using PostgreSQL as an example):

```sql
-- Creating tables for customer, order, and behavior data
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE order (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(id),
    product_name VARCHAR(100),
    order_date DATE
);

CREATE TABLE behavior (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(id),
    webpage_visited VARCHAR(255),
    timestamp TIMESTAMP
);

-- Inserting a sample customer, order, and behavior data
INSERT INTO customer (name, email) VALUES ('John Doe', 'john.doe@example.com');
INSERT INTO order (customer_id, product_name, order_date) VALUES (1, 'Laptop', '2023-08-10');
INSERT INTO behavior (customer_id, webpage_visited, timestamp) VALUES (1, 'homepage', '2023-08-10 10:00:00');
```

### 2. NoSQL Databases (using MongoDB as an example):

Using a MongoDB driver for Python:

```python
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Create/select a database
db = client['sampledb']

# Insert customer data
customer_data = {"name": "John Doe", "email": "john.doe@example.com"}
customer_id = db.customers.insert_one(customer_data).inserted_id

# Insert order data
order_data = {"customer_id": customer_id, "product_name": "Laptop", "order_date": "2023-08-10"}
db.orders.insert_one(order_data)

# Insert behavior data
behavior_data = {"customer_id": customer_id, "webpage_visited": "homepage", "timestamp": "2023-08-10 10:00:00"}
db.behaviors.insert_one(behavior_data)
```

### 3. Distributed File Systems (using HDFS with a hypothetical CSV file):

Assuming we have three CSV files: `customers.csv`, `orders.csv`, and `behaviors.csv`:

Command to put these files into HDFS:

```bash
hadoop fs -put /path/to/customers.csv /destination/on/hdfs/customers.csv
hadoop fs -put /path/to/orders.csv /destination/on/hdfs/orders.csv
hadoop fs -put /path/to/behaviors.csv /destination/on/hdfs/behaviors.csv
```

### 4. Object Storage (using Amazon S3 with Boto3, a Python SDK):

```python
import boto3

s3 = boto3.client('s3')

# Upload customer data
s3.upload_file('/path/to/customers.csv', 'mybucket', 'data/customers.csv')

# Upload order data
s3.upload_file('/path/to/orders.csv', 'mybucket', 'data/orders.csv')

# Upload behavior data
s3.upload_file('/path/to/behaviors.csv', 'mybucket', 'data/behaviors.csv')
```

### 5. Data Warehousing Solutions (using Google BigQuery):

Python code using the `google-cloud-bigquery` client:

```python
from google.cloud import bigquery

# Create a client object
client = bigquery.Client()

# Set dataset and table names
dataset_name = 'sample_dataset'
table_name = 'customers'

# Load data from a CSV file into BigQuery
dataset_ref = client.dataset(dataset_name)
table_ref = dataset_ref.table(table_name)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.autodetect = True

with open('/path/to/customers.csv', 'rb') as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    job.result()  # Wait for the job to complete
```

**Note**: The exact logic, error handling, configuration, and setup are skipped in these examples for simplicity. The real-world scenarios would demand more thorough implementations.
