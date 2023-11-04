# Data Processing/Transformation

| Data Storage          | Common Processing/Transformation Tools                                                 |
| --------------------- | -------------------------------------------------------------------------------------- |
| Relational Databases  | Talend, Apache Nifi, Informatica, SQL Scripts, AWS Glue, Azure Data Factory            |
| Data Warehouses       | dbt, Matillion, Apache Beam, Fivetran, Snowflake Data Pipelines, Google Cloud Dataflow |
| NoSQL Databases       | Apache Nifi, Talend, StreamSets, Apache Spark, MapReduce                               |
| Data Lakes            | Apache Spark, Apache Hive, Presto, Delta Lake, AWS Glue, Databricks                    |
| Time-series Databases | Native Query Tools, InfluxQL (for InfluxDB)                                            |
| Vector Databases      | Application-level transformations, Faiss                                               |
| Graph Databases       | Cypher (for Neo4j), Gremlin                                                            |
| Object Stores         | Apache Spark, Apache Hive, Presto, AWS Athena, Google Cloud Dataproc                   |
| Streaming Data        | Apache Kafka, Apache Flink, Apache Beam, Google Cloud Dataflow                         |

Special Mention:

- **Apache Airflow**: Often used for workflow orchestration rather than data transformation. It's great for scheduling and monitoring ETL tasks.
- **Databricks**: An analytics platform based on Apache Spark. Perfect for big data processing and ML.
- **Pandas**: A Python library for data manipulation and analysis. Ideal for small to medium-sized datasets.
- **Polars**: Similar to Pandas but written in Rust, it's designed to be faster and more memory efficient, suitable for medium datasets.

<br>

# Examples for each platform type

### 1. Relational Databases (RDBMS):

**Data Representation:**
Tables like `Customers`, `Orders`, `Behaviors`.

**SQL Code:**

```sql
SELECT c.name, b.action, o.product
FROM Customers c
JOIN Behaviors b ON c.customer_id = b.customer_id
JOIN Orders o ON c.customer_id = o.customer_id
WHERE b.timestamp < o.timestamp
ORDER BY b.timestamp;
```

### 2. Data Warehouses:

**Data Representation:**
Tables or views, similar to RDBMS but optimized for analytical queries.

**SQL Code (using BigQuery syntax as an example):**

```sql
SELECT c.name, b.action, o.product
FROM `project.dataset.Customers` c
JOIN `project.dataset.Behaviors` b ON c.customer_id = b.customer_id
JOIN `project.dataset.Orders` o ON c.customer_id = o.customer_id
WHERE TIMESTAMP_DIFF(b.timestamp, o.timestamp, SECOND) < 0
ORDER BY b.timestamp;
```

### 3. NoSQL Databases:

**Data Representation (for MongoDB):**
Collections like `customers`, `orders`, `behaviors`.

**MongoDB Query:**

```javascript
db.behaviors.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer_orders",
    },
  },
  {
    $unwind: "$customer_orders",
  },
  {
    $match: {
      timestamp: { $lt: "$customer_orders.timestamp" },
    },
  },
]);
```

### 4. Data Lakes:

**Data Representation:**
Files (like Parquet, JSON, or CSV) stored in folders named `customers`, `orders`, `behaviors`.

**Spark Code (using PySpark):**

```python
customers = spark.read.parquet("/datalake/customers")
behaviors = spark.read.parquet("/datalake/behaviors")
orders = spark.read.parquet("/datalake/orders")

result = customers.join(behaviors, "customer_id").join(orders, "customer_id").filter(behaviors.timestamp < orders.timestamp)
result.show()
```

### 5. Time-series Databases:

**Data Representation:**
Time-indexed series, for example: `customer_behaviors{customer_id="123", action="visited"}`.

**InfluxDB Query:**

```sql
SELECT "action", "product"
FROM "customer_behaviors", "orders"
WHERE "customer_id" = '123' AND "customer_behaviors".time < "orders".time;
```

### 6. Vector Databases:

**Data Representation:**
Vectors representing customer behaviors.

**Notes:**
Data retrieval would typically be more around similarity searches. Direct relational operations like the scenario described may not be common.

### 7. Graph Databases:

**Data Representation:**
Nodes representing `Customers`, `Orders`, and `Behaviors`, with edges like `MADE` (from Customers to Orders) and `DID` (from Customers to Behaviors).

**Cypher Query (for Neo4j):**

```cypher
MATCH (c:Customer)-[:DID]->(b:Behavior)
MATCH (c)-[:MADE]->(o:Order)
WHERE b.timestamp < o.timestamp
RETURN c.name, b.action, o.product
ORDER BY b.timestamp;
```

### 8. Object Stores:

**Data Representation:**
Similar to Data Lakes: Files (Parquet, JSON, CSV) stored in buckets or folders.

**Processing (using Spark with PySpark):**
This would be very similar to the Data Lake example using Spark.

### 9. Streaming Data:

**Data Representation:**
Continuous stream of records.

**Apache Kafka Streams Code:**

```java
KStream<String, Behavior> behaviors = ...;
KStream<String, Order> orders = ...;

behaviors.join(orders, (behavior, order) -> ...).filter((key, value) -> behavior.timestamp.before(order.timestamp));
```

This is a simplified view to fit the described scenario across various data storage paradigms. In real-world applications, additional considerations and configurations would come into play.

<br>

## Examples of outputs

Sure! Let's use the table data we discussed earlier as a basis:

```markdown
| Dataset   | Small (S) | Medium (M) | Large (L) |
| --------- | --------- | ---------- | --------- |
| Customers | 1,000     | 500,000    | 50M       |
| Orders    | 5,000     | 2.5M       | 250M      |
| Behavior  | 20,000    | 10M        | 1B        |
```

Given this data, and the scenario of understanding customer behavior before they make an order, the output might generally consist of:

- `customer_id` or `customer_name`
- the behavior or action they performed
- the order or product they purchased

Let's see what the outputs might look like for each example:

### 1. Relational Databases (RDBMS) & Data Warehouses:

Given their similar tabular structure, the output for both will look similar:

```markdown
| customer_name | behavior_action | order_product |
| ------------- | --------------- | ------------- |
| Alice         | Viewed Item     | Laptop        |
| Bob           | Clicked Ad      | Mobile Phone  |
| ...           | ...             | ...           |
```

### 2. NoSQL Databases (e.g., MongoDB):

The output might be represented as documents:

```json
{
    "customer_name": "Alice",
    "behaviors": [
        { "action": "Viewed Item", "timestamp": "..." },
        ...
    ],
    "orders": [
        { "product": "Laptop", "timestamp": "..." },
        ...
    ]
}
```

### 3. Data Lakes:

The output would be structured files (like Parquet, CSV), resembling:

```csv
customer_name,behavior_action,order_product
Alice,Viewed Item,Laptop
Bob,Clicked Ad,Mobile Phone
...
```

### 4. Time-series Databases:

Data will be in time-indexed format. The data display would be unique to the tool, but generally:

```markdown
| timestamp           | customer_name | behavior_action | order_product |
| ------------------- | ------------- | --------------- | ------------- |
| 2023-08-14 10:00:00 | Alice         | Viewed Item     | Laptop        |
| 2023-08-14 10:05:00 | Bob           | Clicked Ad      | Mobile Phone  |
```

### 5. Vector Databases:

Typically focused on similarity searches, direct outputs like our scenario might not be common. But if used, it might resemble a distance matrix indicating behavioral similarities.

### 6. Graph Databases:

Nodes and edges represent the data. Visualization tools would show a web of connections. In a tabular format, it might look similar to the relational databases output.

### 7. Object Stores:

Output will resemble the structured files in Data Lakes, for example:

```csv
customer_name,behavior_action,order_product
Alice,Viewed Item,Laptop
Bob,Clicked Ad,Mobile Phone
...
```

### 8. Streaming Data:

While the data is continuous, once processed, the output (for instance, when pushed to a sink or stored) might resemble:

```csv
customer_name,behavior_action,order_product
Alice,Viewed Item,Laptop
Bob,Clicked Ad,Mobile Phone
...
```
