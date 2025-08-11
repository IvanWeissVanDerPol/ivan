# Databricks Certification - Exam Day Quick Reference

## 🚀 Critical Commands Cheat Sheet

### Delta Lake Essentials
```sql
-- Create Delta table
CREATE TABLE catalog.schema.table USING DELTA AS SELECT ...

-- Time travel
SELECT * FROM table VERSION AS OF 10
SELECT * FROM table TIMESTAMP AS OF '2024-01-01'

-- Merge (Upsert)
MERGE INTO target USING source ON condition
WHEN MATCHED THEN UPDATE SET ...
WHEN NOT MATCHED THEN INSERT ...

-- Optimize and Vacuum
OPTIMIZE table_name ZORDER BY (col1, col2)
VACUUM table_name RETAIN 168 HOURS
```

### Spark DataFrame API
```python
# Core operations
df.select("col1", "col2")
df.filter(df.amount > 1000)
df.groupBy("category").sum("amount")
df.join(other_df, "key")

# Actions vs Transformations
df.collect()    # Action - triggers computation
df.show()       # Action - triggers computation
df.count()      # Action - triggers computation
df.select()     # Transformation - lazy
```

### MLflow Core
```python
# Experiment tracking
mlflow.set_experiment("/path/to/experiment")
with mlflow.start_run():
    mlflow.log_param("param", value)
    mlflow.log_metric("metric", value)
    mlflow.sklearn.log_model(model, "model")

# Model registry
mlflow.register_model("runs:/run-id/model", "model_name")
model = mlflow.pyfunc.load_model("models:/model_name/Production")
```

### Unity Catalog Essentials
```sql
-- Navigation
USE CATALOG catalog_name;
USE SCHEMA catalog.schema;

-- Permissions
GRANT SELECT ON TABLE catalog.schema.table TO `user@company.com`;
GRANT USE CATALOG ON CATALOG name TO `group-name`;

-- Three-part naming
SELECT * FROM catalog.schema.table;
```

## 📊 Key Concepts by Certification

### Data Engineer Associate/Professional
- **ETL Patterns**: Medallion architecture (Bronze→Silver→Gold)
- **Delta Lake**: ACID, time travel, merge operations
- **Spark**: DataFrames, partitioning, optimization
- **Scheduling**: Jobs, workflows, dependencies

### Data Analyst Associate  
- **SQL**: Window functions, CTEs, joins
- **Visualization**: Dashboards, charts, filters
- **Data Exploration**: Statistical functions, aggregations
- **Security**: Row/column level access control

### Machine Learning Associate/Professional
- **MLflow**: Tracking, registry, deployment
- **Feature Engineering**: Feature store, transformations
- **Model Lifecycle**: Training, validation, monitoring
- **AutoML**: Automated machine learning workflows

### Generative AI Engineer Associate
- **AI Agents**: LangChain, agent frameworks
- **Vector Databases**: Similarity search, embeddings  
- **LLM Integration**: Prompt engineering, fine-tuning
- **RAG Patterns**: Retrieval-augmented generation

## ⚡ Performance & Optimization

### Spark Optimization
```python
# Caching
df.cache()  # Memory
df.persist(StorageLevel.DISK_ONLY)

# Partitioning
df.repartition(4, "column")
df.coalesce(2)

# Broadcast joins
large_df.join(broadcast(small_df), "key")
```

### Delta Lake Performance
```sql
-- File optimization
OPTIMIZE table_name
OPTIMIZE table_name ZORDER BY (frequently_filtered_columns)

-- Cleanup
VACUUM table_name
VACUUM table_name RETAIN 7 DAYS

-- Statistics
ANALYZE TABLE table_name COMPUTE STATISTICS
```

## 🔐 Security Patterns

### Unity Catalog Security
```sql
-- Hierarchical permissions
GRANT USE CATALOG ON CATALOG name TO principal;  -- Inherits to all schemas
GRANT USE SCHEMA ON SCHEMA cat.schema TO principal;  -- Inherits to all tables

-- Dynamic views for row/column security
CREATE VIEW secure_view AS
SELECT 
  id,
  CASE WHEN is_member('admin') THEN salary ELSE NULL END as salary
FROM employees;
```

## 📈 Common Exam Question Types

### 1. Command Syntax (15-20%)
- SQL DDL/DML commands
- Python/Scala API usage
- Configuration settings

### 2. Concept Understanding (25-30%)
- When to use specific features
- Best practices
- Architecture patterns

### 3. Troubleshooting (15-20%)
- Error identification
- Performance issues
- Security problems

### 4. Scenario-Based (30-35%)
- Choose best approach
- Multi-step workflows
- Real-world applications

## 🎯 Last-Minute Review Checklist

### ✅ Delta Lake
- [ ] Time travel syntax (VERSION AS OF vs TIMESTAMP AS OF)
- [ ] MERGE operation syntax and use cases
- [ ] OPTIMIZE vs VACUUM differences
- [ ] Schema evolution and enforcement

### ✅ Spark
- [ ] Lazy evaluation concept
- [ ] Transformations vs Actions
- [ ] DataFrame API common operations
- [ ] Performance optimization techniques

### ✅ MLflow
- [ ] Experiment tracking workflow
- [ ] Model registry stages
- [ ] Artifact logging
- [ ] Model deployment patterns

### ✅ Unity Catalog
- [ ] Three-level hierarchy (catalog.schema.object)
- [ ] Permission inheritance
- [ ] External vs managed objects
- [ ] Storage credentials and external locations

## 🚨 Common Pitfalls to Avoid

### Syntax Errors
- Missing backticks for names with special characters
- Incorrect three-part naming format
- Wrong parameter names in API calls

### Conceptual Mistakes
- Confusing transformations with actions
- Mixing up schema evolution vs enforcement
- Incorrect understanding of permission inheritance

### Performance Anti-Patterns
- Unnecessary collect() operations
- Over-partitioning data
- Not using appropriate file formats

## 📝 Quick Formulas & Calculations

### Partition Sizing
- **Target partition size**: 1GB per partition
- **Max partitions**: 10,000 partitions per table
- **Calculation**: Total data size ÷ 1GB = optimal partitions

### Cache Memory
- **Default**: MEMORY_AND_DISK
- **Fast queries**: MEMORY_ONLY
- **Large datasets**: DISK_ONLY

### Retention Periods
- **Delta Log**: 30 days default
- **VACUUM**: 7 days default (can be shorter)
- **Time travel**: Limited by log retention

## 📊 File Format Comparison

| Format | Use Case | Performance | Schema Evolution |
|--------|----------|-------------|------------------|
| **Delta** | ACID transactions | Excellent | Yes |
| **Parquet** | Analytics | Good | Limited |
| **JSON** | Semi-structured | Fair | Flexible |
| **CSV** | Simple data | Poor | None |

## 🔍 Debugging Commands

### Spark
```python
# Check execution plan
df.explain(True)

# Monitor performance
spark.sparkContext.statusTracker()

# Cache information
spark.catalog.cacheTable("table_name")
```

### Delta Lake
```sql
-- Table history
DESCRIBE HISTORY table_name

-- Table details
DESCRIBE DETAIL table_name

-- Show properties
SHOW TBLPROPERTIES table_name
```

### Unity Catalog
```sql
-- Check permissions
SHOW GRANTS ON OBJECT object_name

-- Current user
SELECT current_user()

-- Group membership
SELECT is_member('group_name')
```

## ⏰ Time Management Tips

### Question Pacing (90-minute exam)
- **45 questions**: 2 minutes per question
- **60 questions**: 1.5 minutes per question
- **First pass**: 60-70 minutes (answer what you know)
- **Review pass**: 20-30 minutes (tackle difficult questions)

### Priority Strategy
1. **Quick wins**: Commands and syntax (30 seconds each)
2. **Concept questions**: Understanding-based (1-2 minutes each)  
3. **Scenarios**: Complex multi-step problems (3-4 minutes each)
4. **Review**: Double-check flagged questions

---

*Good luck on your exam! Remember: You've got this! 🌟*