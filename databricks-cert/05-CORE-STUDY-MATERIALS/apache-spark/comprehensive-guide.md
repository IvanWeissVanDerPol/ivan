# Apache Spark - Comprehensive Study Guide for Databricks Certifications

## Overview
Apache Spark is at the heart of the Databricks Data Intelligence Platform and is the technology powering compute clusters and SQL warehouses. Databricks provides an optimized platform for Apache Spark that provides efficient and simple platform for running Spark workloads.

## Core Concepts

### What is Apache Spark?
- **Unified analytics engine** for large-scale data processing
- **In-memory computing** for faster processing
- **Lazy evaluation** - operations not executed until action is triggered
- **Distributed computing** across cluster of machines
- **Multi-language support** - Python (PySpark), Scala, SQL, R, Java

### Spark Architecture
```
┌─────────────────┐
│   Driver Node   │ ← Spark Context, coordinates tasks
└─────────────────┘
         │
┌─────────────────┐
│ Cluster Manager │ ← Manages resources
└─────────────────┘
         │
┌─────────────────┐
│ Worker Nodes    │ ← Execute tasks, store data
└─────────────────┘
```

## Core Data Structures

### 1. RDD (Resilient Distributed Dataset)
- **Low-level API** - most basic data structure
- **Immutable** - cannot be changed after creation
- **Fault-tolerant** - automatically recovers from node failures
- **Partitioned** - distributed across cluster

```python
# Create RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
text_rdd = spark.sparkContext.textFile("path/to/file.txt")

# Transformations
mapped_rdd = rdd.map(lambda x: x * 2)
filtered_rdd = rdd.filter(lambda x: x > 2)

# Actions
result = rdd.collect()
count = rdd.count()
```

### 2. DataFrames
- **High-level API** built on top of RDDs
- **Structured data** with schema
- **Catalyst optimizer** for query optimization
- **SQL interface** available

```python
# Create DataFrame
df = spark.read.format("parquet").load("path/to/file.parquet")
df = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])

# Operations
df.select("name").show()
df.filter(df.id > 1).show()
df.groupBy("name").count().show()

# SQL interface
df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE id > 1").show()
```

### 3. Datasets
- **Type-safe** version of DataFrames (Scala/Java)
- **Compile-time type checking**
- **Encoder** for serialization

```scala
// Scala example
case class Person(name: String, age: Int)
val ds = Seq(Person("Alice", 25), Person("Bob", 30)).toDS()
```

## Operations Types

### Transformations (Lazy)
Operations that create new RDDs/DataFrames without immediately computing results.

#### Narrow Transformations
- Data required for computation is available on single partition
- No data shuffling required
- Examples: `map()`, `filter()`, `flatMap()`

```python
# Examples of narrow transformations
df.select("column1")
df.filter(df.column1 > 100)
df.map(lambda row: row.column1 * 2)
```

#### Wide Transformations
- Data required for computation spans multiple partitions
- Requires data shuffling
- Examples: `groupBy()`, `join()`, `orderBy()`

```python
# Examples of wide transformations
df.groupBy("category").sum("amount")
df.join(other_df, "key")
df.orderBy("timestamp")
```

### Actions (Eager)
Operations that trigger computation and return results.

```python
# Common actions
df.collect()        # Return all rows to driver
df.count()          # Count rows
df.show()           # Display first 20 rows
df.take(5)          # Return first 5 rows
df.write.parquet()  # Write to storage
```

## Key Features on Databricks

### 1. Lazy Evaluation
- Operations are not executed immediately
- Spark builds a computation graph (DAG)
- Optimizes the entire plan before execution
- Only executes when action is called

### 2. Catalyst Optimizer
- **Query optimization engine**
- **Rule-based optimization** - predicate pushdown, column pruning
- **Cost-based optimization** - join reordering, statistics
- **Code generation** - generates Java bytecode

### 3. Photon Engine
- **Vectorized execution engine** by Databricks
- **C++ implementation** for performance
- **Automatic optimization** for SQL and DataFrame operations
- **Transparent integration** with Spark

## Data Sources and I/O

### Reading Data
```python
# Various formats
df = spark.read.format("json").load("path/to/file.json")
df = spark.read.format("csv").option("header", "true").load("path/to/file.csv")
df = spark.read.format("parquet").load("path/to/file.parquet")
df = spark.read.format("delta").load("path/to/delta-table")

# Database connections
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://host:port/database") \
    .option("dbtable", "table_name") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

### Writing Data
```python
# Save in various formats
df.write.format("parquet").mode("overwrite").save("path/to/output")
df.write.format("delta").mode("append").saveAsTable("my_table")

# Write modes
df.write.mode("overwrite")  # Replace existing data
df.write.mode("append")     # Add to existing data
df.write.mode("ignore")     # Skip if exists
df.write.mode("error")      # Fail if exists (default)
```

## Data Transformations

### Common DataFrame Operations

#### Selection and Projection
```python
# Select columns
df.select("col1", "col2")
df.select(df.col1, df.col2.alias("new_name"))

# Add/modify columns
from pyspark.sql.functions import col, lit, when
df.withColumn("new_col", col("existing_col") * 2)
df.withColumn("status", when(col("amount") > 1000, "high").otherwise("low"))
```

#### Filtering
```python
# Filter rows
df.filter(df.amount > 100)
df.filter("amount > 100")  # SQL-style
df.where(df.category == "electronics")
```

#### Aggregations
```python
# Group operations
df.groupBy("category").sum("amount")
df.groupBy("category").agg({"amount": "sum", "quantity": "avg"})

# Window functions
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

windowSpec = Window.partitionBy("category").orderBy("amount")
df.withColumn("rank", row_number().over(windowSpec))
```

#### Joins
```python
# Different join types
df1.join(df2, "key")                    # Inner join (default)
df1.join(df2, "key", "inner")           # Inner join
df1.join(df2, "key", "left")            # Left join
df1.join(df2, "key", "right")           # Right join
df1.join(df2, "key", "outer")           # Full outer join
df1.join(df2, "key", "left_anti")       # Left anti join

# Complex join conditions
df1.join(df2, (df1.key == df2.key) & (df1.date >= df2.start_date))
```

## Performance Optimization

### 1. Caching and Persistence
```python
# Cache DataFrame in memory
df.cache()
df.persist()

# Different storage levels
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.DISK_ONLY)

# Unpersist when done
df.unpersist()
```

### 2. Partitioning
```python
# Repartition data
df.repartition(4)                    # Specific number of partitions
df.repartition("column")             # Partition by column
df.coalesce(2)                       # Reduce partitions (no shuffle)

# Check partitions
df.rdd.getNumPartitions()
```

### 3. Bucketing
```python
# Write with bucketing
df.write \
  .bucketBy(10, "user_id") \
  .sortBy("timestamp") \
  .saveAsTable("bucketed_table")
```

### 4. Broadcast Joins
```python
from pyspark.sql.functions import broadcast

# Broadcast small table
large_df.join(broadcast(small_df), "key")
```

## Spark SQL

### Creating Views and Tables
```sql
-- Temporary view
CREATE OR REPLACE TEMPORARY VIEW my_view AS
SELECT * FROM my_table WHERE amount > 100;

-- Global temporary view
CREATE GLOBAL TEMPORARY VIEW global_view AS
SELECT * FROM my_table;

-- Permanent table
CREATE TABLE my_permanent_table
USING DELTA
AS SELECT * FROM my_view;
```

### Advanced SQL Operations
```sql
-- Window functions
SELECT 
    category,
    amount,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) as rank
FROM sales;

-- Common Table Expressions (CTEs)
WITH high_value AS (
    SELECT * FROM sales WHERE amount > 1000
)
SELECT category, COUNT(*) FROM high_value GROUP BY category;

-- Set operations
SELECT id FROM table1
UNION
SELECT id FROM table2;
```

## Streaming with Spark

### Structured Streaming
```python
# Read from stream source
stream_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "host:port") \
    .option("subscribe", "topic") \
    .load()

# Process streaming data
processed_df = stream_df \
    .selectExpr("CAST(value AS STRING) as message") \
    .select(get_json_object("message", "$.field").alias("field"))

# Write to stream sink
query = processed_df \
    .writeStream \
    .format("delta") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .trigger(processingTime='10 seconds') \
    .table("streaming_table")

query.awaitTermination()
```

### Stream Processing Concepts
- **Micro-batch processing** - default execution mode
- **Continuous processing** - low-latency mode
- **Watermarking** - handle late data
- **Checkpointing** - fault tolerance

## Configuration and Tuning

### Important Spark Configurations
```python
# Memory settings
spark.conf.set("spark.executor.memory", "4g")
spark.conf.set("spark.driver.memory", "2g")
spark.conf.set("spark.executor.cores", "2")

# Parallelism
spark.conf.set("spark.sql.shuffle.partitions", "200")
spark.conf.set("spark.default.parallelism", "100")

# Optimization settings
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

### Databricks-Specific Optimizations
```python
# Auto-optimize
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")

# Photon
spark.conf.set("spark.databricks.photon.enabled", "true")

# Predictive I/O
spark.conf.set("spark.databricks.io.cache.enabled", "true")
```

## Error Handling and Debugging

### Common Issues and Solutions

#### Out of Memory Errors
```python
# Increase driver/executor memory
# Optimize queries to reduce data shuffling
# Use efficient file formats (Parquet, Delta)
# Partition large datasets appropriately
```

#### Performance Issues
```python
# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Monitor Spark UI for bottlenecks
# Check partition sizes and distribution
# Use broadcast joins for small tables
```

#### Data Skew
```python
# Salting technique for skewed joins
from pyspark.sql.functions import rand, floor

salted_df = df.withColumn("salt", floor(rand() * 100))
# Join on composite key including salt
```

## Best Practices

### 1. Data Engineering
- Use appropriate file formats (Parquet for analytics)
- Implement proper partitioning strategy
- Monitor and optimize file sizes
- Use Delta Lake for ACID transactions

### 2. Performance
- Avoid unnecessary shuffles
- Use broadcast joins for small tables
- Cache frequently accessed data
- Enable adaptive query execution

### 3. Code Organization
- Use DataFrames over RDDs when possible
- Prefer built-in functions over UDFs
- Optimize SQL queries
- Use lazy evaluation effectively

### 4. Resource Management
- Right-size cluster configurations
- Use auto-scaling when appropriate
- Monitor resource utilization
- Implement proper error handling

## Certification Focus Areas

### For Data Engineer Associate/Professional
- DataFrame API operations
- Data ingestion and transformation patterns
- Performance optimization techniques
- Streaming data processing
- SQL query optimization

### For Data Analyst Associate
- SQL queries and analytics
- Data exploration with DataFrames
- Aggregations and window functions
- Data visualization preparation

### For Machine Learning Associate
- Data preparation for ML
- Feature engineering with Spark
- Model training data pipelines
- Integration with MLlib

## Quick Reference

### Essential Functions
```python
# Import common functions
from pyspark.sql.functions import *
from pyspark.sql.types import *

# DataFrame operations
df.show()                    # Display data
df.printSchema()             # Show schema
df.describe().show()         # Statistics
df.count()                   # Row count
df.columns                   # Column names

# Transformations
df.select()                  # Select columns
df.filter() / df.where()     # Filter rows
df.groupBy().agg()          # Aggregations
df.join()                    # Join tables
df.withColumn()             # Add/modify columns
df.drop()                   # Drop columns

# Actions
df.collect()                 # Get all data
df.take(n)                  # Get first n rows
df.show(n)                  # Display n rows
df.write.save()             # Save data
```

### SQL Commands
```sql
-- Basic queries
SELECT * FROM table_name;
SELECT col1, col2 FROM table_name WHERE condition;

-- Aggregations
SELECT category, COUNT(*), SUM(amount) 
FROM sales 
GROUP BY category 
HAVING COUNT(*) > 10;

-- Joins
SELECT a.*, b.name 
FROM orders a 
JOIN customers b ON a.customer_id = b.id;

-- Window functions
SELECT *, ROW_NUMBER() OVER (ORDER BY amount DESC) as rank
FROM sales;
```