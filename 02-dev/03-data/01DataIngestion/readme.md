# Data ingestion

## Definition

- the process of importing, transferring, loading and processing data
- for immediate use or storage in a database.

We separate:

- Batch - chunks of data at periodic intervals
- Real-time ingestions - streaming data and ingesting it in real-time

## Overview

### Realtime

| Tool                       | Principle                                 | Underlying Technologies                | Strengths                                        | Weaknesses                                  |
| -------------------------- | ----------------------------------------- | -------------------------------------- | ------------------------------------------------ | ------------------------------------------- |
| **Apache NiFi**            | Automates flow of data                    | Java; Data routing, transformation     | Visual UI, data lineage, extensible              | Overkill for simple workflows; Needs JVM    |
| **Apache Kafka**           | Distributed streaming                     | Scala, Java; Publish-subscribe         | Scalable, fault-tolerant, low-latency            | Complex setup; Requires ecosystem knowledge |
| **Apache Flume**           | Collects, aggregates large log data       | Java; Designed for distributed systems | Scalable, fault-tolerant                         | Less flexible than NiFi; For Hadoop         |
| **Logstash**               | Data processing pipeline                  | Ruby; Input plugins                    | Works with Elasticsearch, large plugin ecosystem | JVM-based; Complex config                   |
| **Amazon Kinesis**         | Real-time data streaming                  | Cloud; AWS integration                 | Scalable, durable, real-time                     | AWS specific                                |
| **Google Cloud Pub/Sub**   | Real-time messaging                       | Cloud; GCP integration                 | Real-time data ingestion, scalable               | GCP specific                                |
| **Azure Stream Analytics** | Real-time data stream processing in cloud | Cloud; Azure integration               | Azure services integration, SQL-like querying    | Azure specific                              |

### Batch

| Tool                                  | Description                                                                               | Example Use Case                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Apache Hadoop (MapReduce)**         | Distributed processing framework for large datasets.                                      | Process and analyze web server logs.                   |
| **Apache Spark**                      | Distributed computing with batch and real-time processing; known for speed and libraries. | Large-scale data analytics or machine learning.        |
| **Apache Flink**                      | Real-time stream processing but also supports batch processing.                           | Analyze e-commerce transaction histories.              |
| **Apache Hive**                       | Data warehousing on Hadoop with SQL-like queries, optimized for batch.                    | Query large datasets in Hadoop using SQL-like queries. |
| **Apache Sqoop**                      | Tool to transfer data between Hadoop and relational databases.                            | Migrate relational database data into Hadoop.          |
| **Talend**                            | Data integration and management tool focusing on batch processing.                        | Integrate and transform data for a data warehouse.     |
| **Pentaho Data Integration (Kettle)** | Open-source ETL tool for batch data processing.                                           | Extract, transform, and load data into a database.     |

<br>

## Example data sets

### Small, medium and large

We will play with an order of magnitude with the data:

| Classification       | Size Range    | Characteristics                                                                                                              | Common Storage                              |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Small**            | Up to 10 GB   | - Can be processed on a single machine.<br> - Used in local development or prototyping.                                      | Flat files (CSV, JSON, Excel)               |
| **Medium**           | 10 GB to 1 TB | - Might require distributed storage but not always distributed processing.<br> - Advanced data processing tools can be used. | Relational databases, NoSQL databases, HDFS |
| **Large (Big Data)** | TBs to PBs    | - Requires distributed storage and processing.<br> - Processed with platforms like Hadoop, Spark.                            | HDFS, Cloud storage, Big data databases     |

### Small Dataset: Customers

| Customer ID | First Name | Last Name | Email Address          | Signup Date |
| ----------- | ---------- | --------- | ---------------------- | ----------- |
| 1           | John       | Doe       | john.doe@example.com   | 2023-01-15  |
| 2           | Jane       | Smith     | jane.smith@example.com | 2023-02-10  |

---

### Medium Dataset: Orders

| Order ID | Customer ID | Product Name | Quantity Ordered | Order Date | Total Amount |
| -------- | ----------- | ------------ | ---------------- | ---------- | ------------ |
| 1001     | 1           | Laptop       | 1                | 2023-02-01 | $1200        |
| 1002     | 2           | Mobile Phone | 1                | 2023-02-12 | $800         |
| 1003     | 1           | Keyboard     | 2                | 2023-02-15 | $100         |

---

### Large Dataset: Behavior (Website Activity)

| Behavior ID | Customer ID | Webpage Visited | Time Spent (s) | Activity Date & Time |
| ----------- | ----------- | --------------- | -------------- | -------------------- |
| 50001       | 1           | Homepage        | 30             | 2023-02-01 10:05:20  |
| 50002       | 1           | Product Page    | 120            | 2023-02-01 10:07:00  |
| 50003       | 2           | Checkout        | 300            | 2023-02-12 14:20:15  |
| 50004       | 2           | Payment Page    | 240            | 2023-02-12 14:25:20  |
| 50005       | 1           | FAQ Page        | 90             | 2023-02-15 11:12:10  |

<br>

## Batch processing

<br>

### 1. Small Dataset (Up to 10 GB)

**Tool**: Python with Pandas library

**Example**:

Given you have CSV files for `customers.csv`, `orders.csv`, and `behaviors.csv`, here's how you might load and preview them using Python and Pandas:

```python
import pandas as pd

# Load data
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
behaviors = pd.read_csv('behaviors.csv')

# Preview data
print(customers.head())
print(orders.head())
print(behaviors.head())
```

### 2. Medium Dataset (10 GB to 1 TB)

**Tool**: Apache Spark

Apache Spark can handle larger datasets while also providing distributed processing capabilities. Let's use PySpark to load the data:

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("mediumDataProcessing").getOrCreate()

# Load data
customers = spark.read.csv('customers.csv', header=True, inferSchema=True)
orders = spark.read.csv('orders.csv', header=True, inferSchema=True)
behaviors = spark.read.csv('behaviors.csv', header=True, inferSchema=True)

# Preview data
customers.show()
orders.show()
behaviors.show()
```

### 3. Large Dataset (TBs to PBs)

**Tool**: Apache Hadoop (with Hive)

Given the data's size, it's likely stored in a distributed file system like HDFS. Hive provides a SQL-like interface for querying large datasets stored in HDFS.

First, you'd set up Hive tables for your datasets:

```sql
-- Create tables
CREATE TABLE customers (id INT, first_name STRING, last_name STRING, email STRING, signup_date DATE)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

CREATE TABLE orders (order_id INT, customer_id INT, product_name STRING, quantity INT, order_date DATE, total_amount FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

CREATE TABLE behaviors (behavior_id INT, customer_id INT, webpage STRING, time_spent INT, activity_datetime TIMESTAMP)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

-- Load data from HDFS into Hive
LOAD DATA INPATH '/path_to_data/customers.csv' INTO TABLE customers;
LOAD DATA INPATH '/path_to_data/orders.csv' INTO TABLE orders;
LOAD DATA INPATH '/path_to_data/behaviors.csv' INTO TABLE behaviors;
```

You'd then use similar SQL queries to analyze the data within the Hive environment.

## Streaming processes

Streaming data processes handle data in real-time as it's generated, rather than in large batches. Here's how you might approach streaming data of different sizes using different technologies.

In these examples, the source of the streamed data would be your unstructured or structured datasets (like customer behaviors, orders, etc.) being generated in real-time.

### 1. Small Streaming Dataset

**Tool**: Python with `socket` for a simple TCP server-client setup.

This isn't a common production setup for streaming, but for small-scale data or testing purposes, Python's built-in libraries can set up a rudimentary stream.

```python
# Simple TCP Server to receive streamed data
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 9999))
server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024)
    print("Received:", data)
    client_socket.close()
```

### 2. Medium Streaming Dataset

**Tool**: Apache Kafka

Kafka is a distributed event streaming platform that can handle real-time data. Here's a very basic example using Python with the `confluent-kafka` library:

Producer (sending data):

```python
from confluent_kafka import Producer

conf = {'bootstrap.servers': 'YOUR_KAFKA_BROKER'}
producer = Producer(conf)

producer.produce('your_topic_name', key='key', value='value')
producer.flush()
```

Consumer (receiving data):

```python
from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'YOUR_KAFKA_BROKER',
    'group.id': 'your_group_id',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['your_topic_name'])

while True:
    message = consumer.poll(1.0)
    if message is None:
        continue
    if message.error():
        print("Consumer error: {}".format(message.error()))
    else:
        print("Received message: {}".format(message.value().decode('utf-8')))
```

### 3. Large Streaming Dataset

**Tool**: Apache Flink or Apache Spark Streaming

Both Apache Flink and Apache Spark Streaming can handle large-scale real-time data processing. They also support integration with Kafka, HDFS, and other big data tools. Here's a simple example using Spark Streaming with Kafka:

```python
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext("local[2]", "KafkaExample")
ssc = StreamingContext(sc, 1)  # 1 second window

kafkaStream = KafkaUtils.createStream(
    ssc,
    'YOUR_ZOOKEEPER_QUORUM',  # Zookeeper quorum location
    'your_group_name',
    {'your_topic_name': 1}
)

lines = kafkaStream.map(lambda x: x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()
```
