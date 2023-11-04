# Data Quality

| Stage                     | Data Solution Size | Data Quality Task                                       | Tool Examples                                                                            |
| ------------------------- | ------------------ | ------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Ingestion                 | Small              | Format checks, mandatory field checks                   | Excel, Google Sheets, Python (with Pandas)                                               |
|                           | Medium             | Schema validation, basic anomaly detection              | Talend, Apache Nifi, Logstash                                                            |
|                           | Large              | Streaming data validation, bulk data consistency checks | Apache Kafka with validation plugins, StreamSets                                         |
| Storage                   | Small              | Data audits, consistency checks                         | SQLite, PostgreSQL with data quality extensions                                          |
|                           | Medium             | Regular data integrity checks, relevancy audits         | MySQL, MongoDB with built-in validation                                                  |
|                           | Large              | Distributed system data integrity, data snapshots       | Hadoop HDFS with data validation jobs, Amazon S3 with AWS Lambda triggers for validation |
| Processing/Transformation | Small              | Duplicate removal, missing value imputation             | Python (Pandas), Excel                                                                   |
|                           | Medium             | Data normalization, outlier detection                   | Apache Spark, Trifacta, OpenRefine                                                       |
|                           | Large              | Large-scale data wrangling, distributed data cleaning   | Apache Spark with PySpark, DBT, Talend Big Data platform                                 |
