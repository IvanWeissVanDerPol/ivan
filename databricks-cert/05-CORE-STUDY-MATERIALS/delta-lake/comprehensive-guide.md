# Delta Lake - Comprehensive Study Guide

## Overview
Delta Lake is the optimized storage layer that provides the foundation for tables in a lakehouse on Databricks. It extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling.

## Key Concepts

### What is Delta Lake?
- **Open source software** that extends Parquet data files
- **File-based transaction log** for ACID transactions
- **Default format** for all operations on Databricks
- **Fully compatible** with Apache Spark APIs
- **Developed for tight integration** with Structured Streaming

### Core Benefits
1. **ACID Transactions**: Ensures data consistency
2. **Schema Enforcement**: Validates data on write
3. **Time Travel**: Query previous versions of tables
4. **Scalable Metadata Handling**: Efficiently manages table metadata
5. **Unified Batch and Streaming**: Single copy of data for both operations

## Getting Started with Delta Lake

### Basic Operations
All tables on Databricks are Delta tables by default. You get Delta Lake benefits automatically when saving data with default settings.

#### Creating Tables
```sql
-- Create Delta table
CREATE TABLE my_table (
    id INT,
    name STRING,
    created_at TIMESTAMP
) USING DELTA

-- Create table from DataFrame
df.write.format("delta").saveAsTable("my_table")
```

#### Reading Data
```sql
-- Simple SELECT
SELECT * FROM my_table

-- Time travel query
SELECT * FROM my_table VERSION AS OF 10
SELECT * FROM my_table TIMESTAMP AS OF '2024-01-01'
```

#### Writing Data
```python
# Write DataFrame to Delta table
df.write.format("delta").mode("overwrite").saveAsTable("my_table")

# Append data
df.write.format("delta").mode("append").saveAsTable("my_table")
```

#### Updating Data
```sql
-- Update records
UPDATE my_table SET name = 'Updated Name' WHERE id = 1

-- Upsert using MERGE
MERGE INTO target_table t
USING source_table s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.name = s.name
WHEN NOT MATCHED THEN INSERT (id, name) VALUES (s.id, s.name)
```

## Data Ingestion Methods

### 1. Lakeflow Declarative Pipelines
- Simplified ETL workloads
- Optimized execution
- Automated infrastructure deployment

### 2. COPY INTO
```sql
COPY INTO my_table
FROM '/path/to/files/'
FILEFORMAT = PARQUET
```

### 3. Auto Loader
```python
df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .load("/path/to/files/")
```

### 4. Streaming Tables
```python
# Streaming write
df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .table("my_table")
```

## Schema Management

### Schema Enforcement
- Delta Lake validates schema on write
- Ensures data quality and consistency
- Prevents incompatible data from being written

### Schema Evolution
```sql
-- Add column
ALTER TABLE my_table ADD COLUMN new_column STRING

-- Enable automatic schema merging
SET spark.databricks.delta.schema.autoMerge.enabled = true
```

### Column Mapping
```sql
-- Enable column mapping
ALTER TABLE my_table SET TBLPROPERTIES (
    'delta.columnMapping.mode' = 'name'
)

-- Rename column
ALTER TABLE my_table RENAME COLUMN old_name TO new_name
```

## Table Operations

### Merge (Upsert)
```sql
MERGE INTO target t
USING source s ON t.key = s.key
WHEN MATCHED AND s.flag = 'update' THEN
    UPDATE SET t.value = s.value
WHEN MATCHED AND s.flag = 'delete' THEN
    DELETE
WHEN NOT MATCHED AND s.flag = 'insert' THEN
    INSERT (key, value) VALUES (s.key, s.value)
```

### Selective Overwrite
```sql
-- Overwrite specific partitions
INSERT OVERWRITE my_table
SELECT * FROM source_table
WHERE partition_date = '2024-01-01'
```

### Delete
```sql
DELETE FROM my_table WHERE condition = 'value'
```

## Time Travel and Versioning

### Query Previous Versions
```sql
-- By version number
SELECT * FROM my_table VERSION AS OF 5

-- By timestamp
SELECT * FROM my_table TIMESTAMP AS OF '2024-01-01 12:00:00'

-- Using @ syntax
SELECT * FROM my_table@v5
```

### Table History
```sql
-- View table history
DESCRIBE HISTORY my_table

-- Restore to previous version
RESTORE TABLE my_table TO VERSION AS OF 5
```

## Performance Optimization

### Optimize Command
```sql
-- Optimize small files
OPTIMIZE my_table

-- Z-order optimization
OPTIMIZE my_table ZORDER BY (col1, col2)
```

### Liquid Clustering
```sql
-- Create table with liquid clustering
CREATE TABLE my_table (
    id INT,
    category STRING,
    date DATE
) USING DELTA
CLUSTER BY (category, date)
```

### Data Skipping
- Automatic feature that uses min/max statistics
- Reduces files scanned during queries
- Works with partition pruning

### Vacuum
```sql
-- Remove old data files
VACUUM my_table

-- Specify retention period
VACUUM my_table RETAIN 168 HOURS
```

## Streaming with Delta Lake

### Change Data Feed
```sql
-- Enable change data feed
ALTER TABLE my_table SET TBLPROPERTIES (
    delta.enableChangeDataFeed = true
)

-- Read change feed
SELECT * FROM table_changes('my_table', 2, 5)
```

### Structured Streaming
```python
# Read stream from Delta table
df = spark.readStream \
    .format("delta") \
    .table("source_table")

# Write stream to Delta table
df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .trigger(processingTime='10 seconds') \
    .table("target_table")
```

## Configuration and Properties

### Important Table Properties
```sql
-- Set table properties
ALTER TABLE my_table SET TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = 'true',
    'delta.autoOptimize.autoCompact' = 'true',
    'delta.deletedFileRetentionDuration' = '168 hours',
    'delta.enableChangeDataFeed' = 'true'
)
```

### Spark Configurations
```python
# Enable optimizations
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")
```

## Best Practices

### 1. File Size Management
- Target 1GB files for optimal performance
- Use Auto Optimize for automatic file management
- Run OPTIMIZE regularly for better query performance

### 2. Partitioning Strategy
- Partition by commonly filtered columns
- Avoid over-partitioning (too many small partitions)
- Consider liquid clustering for modern workloads

### 3. Schema Design
- Define appropriate data types
- Use constraints for data quality
- Plan for schema evolution

### 4. Performance Tuning
- Use Z-ORDER for frequently queried columns
- Enable data skipping
- Monitor and optimize based on query patterns

### 5. Data Lifecycle Management
- Set appropriate retention periods
- Regular VACUUM operations
- Monitor storage costs

## Error Handling and Troubleshooting

### Common Issues
1. **Schema mismatch errors**: Enable schema merging or fix schema
2. **File not found errors**: Check table location and permissions
3. **Concurrent write conflicts**: Implement retry logic

### Monitoring
```sql
-- Check table details
DESCRIBE DETAIL my_table

-- View table properties
SHOW TBLPROPERTIES my_table
```

## Integration with Other Services

### Unity Catalog
- Centralized governance
- Fine-grained access control
- Lineage tracking

### MLflow
- Model registry integration
- Feature store compatibility
- Experiment tracking

### Power BI / Tableau
- Direct connectivity
- Real-time dashboards
- Optimized for analytics

## Certification Focus Areas

### For Data Engineer Associate
- Basic Delta Lake operations
- Schema management
- Data ingestion patterns
- Performance optimization basics

### For Data Engineer Professional
- Advanced optimization techniques
- Complex streaming scenarios
- Multi-table transactions
- Advanced troubleshooting

### For Data Analyst Associate
- Querying Delta tables
- Time travel features
- Basic data exploration
- Working with streaming data

### For Machine Learning Associate
- Feature store integration
- Model training data preparation
- Streaming ML pipelines
- Data versioning for ML

## Sample Exam Questions Focus

1. **MERGE operations** - Syntax and use cases
2. **Time travel queries** - VERSION AS OF vs TIMESTAMP AS OF
3. **Schema evolution** - When and how to enable
4. **Optimization** - OPTIMIZE vs VACUUM differences
5. **Streaming** - Change data feed applications
6. **Performance** - Z-ORDER vs liquid clustering
7. **Data ingestion** - COPY INTO vs Auto Loader
8. **Troubleshooting** - Common error scenarios

## Quick Reference Commands

```sql
-- Create table
CREATE TABLE table_name USING DELTA AS SELECT ...

-- Time travel
SELECT * FROM table_name VERSION AS OF version_number
SELECT * FROM table_name TIMESTAMP AS OF timestamp

-- Optimize
OPTIMIZE table_name
OPTIMIZE table_name ZORDER BY (col1, col2)

-- Vacuum
VACUUM table_name
VACUUM table_name RETAIN hours

-- Merge
MERGE INTO target USING source ON condition
WHEN MATCHED THEN UPDATE SET ...
WHEN NOT MATCHED THEN INSERT ...

-- History
DESCRIBE HISTORY table_name
RESTORE TABLE table_name TO VERSION AS OF version
```