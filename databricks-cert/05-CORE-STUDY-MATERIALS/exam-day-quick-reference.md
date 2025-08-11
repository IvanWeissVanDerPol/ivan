# Databricks Certification Exam Day Quick Reference

## Pre-Exam Checklist
- [ ] Government-issued ID ready
- [ ] Quiet, private room
- [ ] Stable internet connection
- [ ] Computer camera working
- [ ] Close all applications
- [ ] Clear desk area
- [ ] No second monitors

## Key Formulas & Syntax

### Delta Lake Time Travel
```sql
-- By version
SELECT * FROM table VERSION AS OF 5
SELECT * FROM table@v5

-- By timestamp  
SELECT * FROM table TIMESTAMP AS OF '2024-01-01'
SELECT * FROM table AS OF '2024-01-01'
```

### Window Functions
```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY col2)
RANK() OVER (PARTITION BY col ORDER BY col2 DESC)
LAG(column, 1) OVER (ORDER BY date)
SUM(amount) OVER (PARTITION BY customer ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

### MERGE Statement
```sql
MERGE INTO target USING source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
WHEN MATCHED AND condition THEN DELETE
```

### Common PySpark Operations
```python
# Read data
df = spark.read.format("delta").load(path)
df = spark.read.option("header", "true").csv(path)

# Transformations
df.filter(col("age") > 21)
df.select("col1", "col2", F.col("col3").alias("new_name"))
df.groupBy("category").agg(F.sum("amount"), F.count("*"))
df.join(other_df, ["key_col"], "left")

# Write data
df.write.mode("overwrite").format("delta").save(path)
df.write.mode("append").option("mergeSchema", "true").saveAsTable("table")
```

### MLflow Quick Commands
```python
# Basic tracking
with mlflow.start_run():
    mlflow.log_param("alpha", 0.5)
    mlflow.log_metric("rmse", 0.876)
    mlflow.sklearn.log_model(model, "model")

# Model registry
mlflow.register_model("runs:/run_id/model", "model_name")
```

### Performance Optimization
```python
# Caching
df.cache()
df.persist(StorageLevel.MEMORY_AND_DISK)

# Repartitioning
df.repartition(200)  # Increase partitions
df.coalesce(10)     # Reduce partitions

# Broadcast join
from pyspark.sql.functions import broadcast
df1.join(broadcast(small_df), "key")

# Adaptive Query Execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
```

## Quick Decision Trees

### Choosing Cluster Type
- **Job Cluster**: Scheduled/automated workloads
- **All-Purpose Cluster**: Interactive development
- **High Concurrency**: Multiple users
- **Single Node**: Small data, testing

### Choosing File Format
- **Delta**: Default choice, ACID, time travel
- **Parquet**: Interoperability, columnar storage
- **JSON**: Semi-structured, nested data
- **CSV**: Human readable, compatibility

### Memory Issues
1. Increase cluster memory
2. Repartition data
3. Use broadcast joins for small tables
4. Cache only what's needed
5. Use appropriate storage levels

### Performance Issues
1. Check execution plan with .explain()
2. Reduce shuffles
3. Use appropriate partitioning
4. Enable AQE
5. Consider Z-ordering for Delta

## Common Gotchas

### Syntax Reminders
- Python: `col("column_name")` not `"column_name"`
- SQL: Use backticks for spaces in names: `column name`
- Case sensitivity matters in Python
- Default join is INNER

### Delta Lake
- VACUUM removes old files (can't time travel past retention)
- OPTIMIZE compacts small files
- Z-ORDER improves query performance
- Schema evolution requires mergeSchema option

### MLflow
- Models must be logged within run context
- Feature store requires Delta tables
- Model serving needs registered models
- Experiments organize runs

## Time Management
- 90 minutes for ~45 questions = 2 minutes per question
- Flag difficult questions for later review
- Don't spend more than 3 minutes on any single question
- Save 10 minutes at the end for review

## Answer Strategy
- Eliminate obviously wrong answers first
- Look for exact syntax matches
- Consider Databricks-specific best practices
- When in doubt, choose the most explicit/clear option
- Watch for words like "BEST", "MOST", "NOT", "EXCEPT"