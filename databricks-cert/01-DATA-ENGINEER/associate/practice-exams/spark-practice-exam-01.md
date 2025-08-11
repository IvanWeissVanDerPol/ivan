# Apache Spark Developer Associate - Practice Exam 01
## Focus: Spark Core Fundamentals (RDDs, DataFrames, Basic Transformations)
**Difficulty Level:** Beginner to Intermediate  
**Time Limit:** 90 minutes  
**Questions:** 60

---

### Question 1
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the role of core components of Apache Spark's Architecture

Which component in the Spark cluster is responsible for coordinating tasks and managing the overall execution of a Spark application?

A. Worker Node  
B. Executor  
C. Driver Node  
D. Cluster Manager

**Correct Answer:** C  
**Explanation:** The Driver Node runs the main() function of the application and creates the SparkContext. It coordinates the execution of tasks across the cluster and manages the overall workflow.

---

### Question 2
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the execution patterns of Apache Spark engine

Which of the following statements about lazy evaluation in Apache Spark is TRUE?

A. All operations are executed immediately when called  
B. Only actions trigger the execution of transformations  
C. Lazy evaluation only applies to RDDs, not DataFrames  
D. Caching prevents lazy evaluation from working

**Correct Answer:** B  
**Explanation:** Spark uses lazy evaluation, meaning transformations are not executed until an action is called. This allows Spark to optimize the execution plan.

---

### Question 3
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Given a DataFrame `df` with columns `name`, `age`, and `salary`, which code correctly adds a new column `bonus` that is 10% of the salary?

A. `df.withColumn("bonus", col("salary") * 0.1)`  
B. `df.addColumn("bonus", col("salary") * 0.1)`  
C. `df.select("*", col("salary") * 0.1 as "bonus")`  
D. Both A and C are correct

**Correct Answer:** D  
**Explanation:** Both `withColumn()` and `select()` with all columns can add a new calculated column. However, `addColumn()` is not a valid DataFrame method.

---

### Question 4
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as filtering

Which of the following filtering operations are equivalent? Select all that apply.

A. `df.filter(col("age") > 21)`  
B. `df.where(col("age") > 21)`  
C. `df.filter("age > 21")`  
D. `df.where("age > 21")`

**Correct Answer:** A, B, C, D  
**Explanation:** All four options are valid and equivalent. `filter()` and `where()` are aliases, and both accept Column expressions or SQL string expressions.

---

### Question 5
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the features of Apache Spark Modules

Which Spark module is primarily used for structured data processing with optimized execution plans?

A. Spark Core  
B. Spark SQL  
C. Spark Streaming  
D. MLlib

**Correct Answer:** B  
**Explanation:** Spark SQL provides the DataFrame and Dataset APIs with the Catalyst optimizer for structured data processing.

---

### Question 6
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

Which import statement is required to use built-in functions like `upper()`, `lower()`, and `length()` in PySpark?

A. `from pyspark.sql import functions`  
B. `from pyspark.sql.functions import *`  
C. `import pyspark.sql.functions as F`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three import patterns are valid ways to access Spark SQL functions. The choice depends on coding style preferences.

---

### Question 7
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the architecture of Apache Spark

What is the default storage level when you call `.cache()` on a DataFrame?

A. MEMORY_ONLY  
B. MEMORY_AND_DISK  
C. DISK_ONLY  
D. MEMORY_ONLY_SER

**Correct Answer:** B  
**Explanation:** The default cache() operation uses MEMORY_AND_DISK storage level, which stores data in memory if possible, otherwise spills to disk.

---

### Question 8
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as sorting

Which of the following correctly sorts a DataFrame by the `age` column in descending order?

A. `df.sort(desc("age"))`  
B. `df.orderBy(desc("age"))`  
C. `df.sort(col("age").desc())`  
D. All of the above

**Correct Answer:** D  
**Explanation:** `sort()` and `orderBy()` are aliases. Both `desc("age")` and `col("age").desc()` create descending order specifications.

---

### Question 9
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

When reading a large CSV file, which parameter controls the number of partitions created?

A. `spark.sql.adaptive.enabled`  
B. `spark.sql.files.maxPartitionBytes`  
C. `spark.serializer`  
D. `spark.sql.adaptive.coalescePartitions.enabled`

**Correct Answer:** B  
**Explanation:** The `spark.sql.files.maxPartitionBytes` configuration determines the maximum number of bytes to pack into a single partition when reading files.

---

### Question 10
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

Which method removes duplicate rows from a DataFrame based on all columns?

A. `df.distinct()`  
B. `df.dropDuplicates()`  
C. `df.unique()`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `distinct()` and `dropDuplicates()` without parameters remove duplicate rows based on all columns.

---

### Question 11
**Section:** Apache Spark Architecture and Components  
**Objective:** Explain the Apache Spark Architecture execution hierarchy

In the Spark execution hierarchy, what is the relationship between Jobs, Stages, and Tasks?

A. Job → Task → Stage  
B. Stage → Job → Task  
C. Job → Stage → Task  
D. Task → Stage → Job

**Correct Answer:** C  
**Explanation:** Each Action creates a Job. Jobs are divided into Stages at shuffle boundaries. Each Stage contains multiple Tasks that run in parallel.

---

### Question 12
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

Which function extracts the year from a date column?

A. `year(col("date_column"))`  
B. `date_part("year", col("date_column"))`  
C. `extract(year from col("date_column"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `year()` and `date_part("year", ...)` extract the year from a date column. Option C is SQL syntax, not PySpark.

---

### Question 13
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify advantages and challenges of implementing Spark

Which of the following is an advantage of Apache Spark's in-memory processing?

A. Reduces disk I/O operations  
B. Enables faster iterative algorithms  
C. Improves performance for machine learning workloads  
D. All of the above

**Correct Answer:** D  
**Explanation:** In-memory processing reduces disk I/O, speeds up iterative algorithms, and significantly improves ML workload performance.

---

### Question 14
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as conversion between formats

How do you convert a DataFrame to a Pandas DataFrame in PySpark?

A. `df.toPandas()`  
B. `df.to_pandas()`  
C. `df.convertToPandas()`  
D. `pandas.DataFrame(df)`

**Correct Answer:** A  
**Explanation:** The `toPandas()` method converts a Spark DataFrame to a Pandas DataFrame, collecting all data to the driver.

---

### Question 15
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe different types of variables in Spark

What is the primary purpose of broadcast variables in Spark?

A. To share large read-only data across all nodes efficiently  
B. To accumulate values across multiple tasks  
C. To partition data across the cluster  
D. To cache intermediate results

**Correct Answer:** A  
**Explanation:** Broadcast variables efficiently distribute large read-only data to all worker nodes, avoiding the need to send it with each task.

---

### Question 16
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which code correctly calculates the average salary by department?

A. `df.groupBy("department").avg("salary")`  
B. `df.groupBy("department").mean("salary")`  
C. `df.groupBy("department").agg(avg("salary"))`  
D. All of the above

**Correct Answer:** D  
**Explanation:** `avg()` and `mean()` are equivalent methods. The `agg()` method with `avg()` function is also correct.

---

### Question 17
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the execution patterns of Apache Spark engine

Which of the following are transformations? Select all that apply.

A. `select()`  
B. `show()`  
C. `filter()`  
D. `collect()`  
E. `map()`

**Correct Answer:** A, C, E  
**Explanation:** `select()`, `filter()`, and `map()` are transformations (lazy). `show()` and `collect()` are actions (trigger execution).

---

### Question 18
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage input and output operations

When writing a DataFrame to Parquet format, which mode overwrites existing data?

A. `df.write.mode("overwrite").parquet("path")`  
B. `df.write.mode("replace").parquet("path")`  
C. `df.write.overwrite().parquet("path")`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** The correct mode is "overwrite". "replace" is not a valid mode, and `overwrite()` is not a method.

---

### Question 19
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

What happens when you call `repartition(10)` on a DataFrame?

A. The DataFrame is redistributed into exactly 10 partitions  
B. The DataFrame is coalesced to at most 10 partitions  
C. An error occurs if the DataFrame has fewer than 10 partitions  
D. The operation is ignored if the DataFrame already has 10 partitions

**Correct Answer:** A  
**Explanation:** `repartition()` performs a full shuffle to create exactly the specified number of partitions, regardless of the current partition count.

---

### Question 20
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Which method removes a column from a DataFrame?

A. `df.drop("column_name")`  
B. `df.remove("column_name")`  
C. `df.delete("column_name")`  
D. `df.dropColumn("column_name")`

**Correct Answer:** A  
**Explanation:** The `drop()` method removes columns from a DataFrame. The other methods don't exist in the DataFrame API.

---

### Question 21
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the role of core components of Apache Spark's Architecture

How many CPU cores does each executor use by default?

A. 1  
B. 2  
C. All available cores  
D. It depends on the cluster manager

**Correct Answer:** A  
**Explanation:** By default, each executor uses 1 CPU core (`spark.executor.cores = 1`).

---

### Question 22
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

Which import is needed to create a UDF in PySpark?

A. `from pyspark.sql.functions import udf`  
B. `from pyspark.sql.types import *`  
C. `from pyspark.sql import SparkSession`  
D. Only A is required

**Correct Answer:** D  
**Explanation:** To create a UDF, you only need to import the `udf` function from `pyspark.sql.functions`.

---

### Question 23
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the architecture of Apache Spark

What is the difference between persist() and cache()?

A. persist() allows specifying storage level, cache() uses default  
B. cache() is faster than persist()  
C. persist() writes to disk, cache() keeps in memory  
D. There is no difference

**Correct Answer:** A  
**Explanation:** `persist()` allows specifying a storage level, while `cache()` uses the default MEMORY_AND_DISK storage level.

---

### Question 24
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as iterating

Which method returns the first row of a DataFrame?

A. `df.first()`  
B. `df.head()`  
C. `df.take(1)[0]`  
D. All of the above

**Correct Answer:** D  
**Explanation:** `first()`, `head()`, and `take(1)[0]` all return the first row, though they have slightly different return types and behaviors.

---

### Question 25
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

What's the difference between `repartition()` and `coalesce()`?

A. repartition() can increase partitions, coalesce() can only decrease  
B. repartition() involves a shuffle, coalesce() avoids shuffling when possible  
C. repartition() redistributes data evenly, coalesce() may create uneven partitions  
D. All of the above

**Correct Answer:** D  
**Explanation:** All statements are correct. `repartition()` can increase/decrease with shuffle, while `coalesce()` is optimized for decreasing partitions.

---

### Question 26
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you rename multiple columns at once?

A. `df.withColumnRenamed("old1", "new1").withColumnRenamed("old2", "new2")`  
B. `df.select(col("old1").alias("new1"), col("old2").alias("new2"))`  
C. `df.toDF("new1", "new2", ...)`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three approaches can rename multiple columns, though they have different use cases and requirements.

---

### Question 27
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the features of Apache Spark Modules

Which statement about RDDs is FALSE?

A. RDDs are immutable  
B. RDDs are fault-tolerant  
C. RDDs provide automatic query optimization  
D. RDDs can be cached in memory

**Correct Answer:** C  
**Explanation:** RDDs don't have automatic query optimization. That's a feature of DataFrames and Datasets with the Catalyst optimizer.

---

### Question 28
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which aggregation function calculates the number of distinct values?

A. `countDistinct()`  
B. `count_distinct()`  
C. `distinct().count()`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** `countDistinct()` directly counts distinct values, while `distinct().count()` first gets distinct rows then counts them.

---

### Question 29
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe different types of variables in Spark

Which type of variable is used to implement counters and sums across tasks?

A. Broadcast variables  
B. Accumulators  
C. Local variables  
D. Shared variables

**Correct Answer:** B  
**Explanation:** Accumulators are used for implementing counters and sums that can be safely updated from parallel tasks.

---

### Question 30
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you select all columns except one from a DataFrame?

A. `df.select("*").drop("unwanted_column")`  
B. `df.drop("unwanted_column")`  
C. `df.select(*[c for c in df.columns if c != "unwanted_column"])`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** `drop()` removes specified columns. List comprehension with `select()` explicitly selects all except unwanted columns.

---

### Question 31
**Section:** Apache Spark Architecture and Components  
**Objective:** Explain the Apache Spark Architecture execution hierarchy

At which boundary are stages divided in Spark?

A. Action boundaries  
B. Transformation boundaries  
C. Shuffle boundaries  
D. Partition boundaries

**Correct Answer:** C  
**Explanation:** Stages are divided at shuffle boundaries, where data needs to be redistributed across the cluster.

---

### Question 32
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

How do you remove duplicates based on specific columns?

A. `df.dropDuplicates(["col1", "col2"])`  
B. `df.distinct(["col1", "col2"])`  
C. `df.dedupe(["col1", "col2"])`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** `dropDuplicates()` accepts a list of column names. `distinct()` without parameters removes duplicates based on all columns.

---

### Question 33
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the architecture of Apache Spark

What is the SparkSession lifecycle?

A. Created → Configured → Used → Stopped  
B. Started → Initialized → Executed → Destroyed  
C. Built → Active → Inactive → Garbage Collected  
D. Created → Active → Stopped

**Correct Answer:** A  
**Explanation:** SparkSession is typically created, configured with settings, used for operations, and then stopped to release resources.

---

### Question 34
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage input and output operations

Which method is used to infer schema when reading JSON files?

A. Schema is always inferred automatically  
B. `spark.read.option("inferSchema", "true").json(path)`  
C. `spark.read.schema(inferred_schema).json(path)`  
D. Schema inference is not possible with JSON

**Correct Answer:** A  
**Explanation:** When reading JSON files, Spark automatically infers the schema by scanning the file, unlike CSV files where it needs to be explicitly enabled.

---

### Question 35
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

What determines the number of partitions when creating an RDD from a collection?

A. The size of the collection  
B. The `spark.default.parallelism` setting  
C. The number of CPU cores  
D. The cluster size

**Correct Answer:** B  
**Explanation:** When creating RDDs from collections, `spark.default.parallelism` determines the default number of partitions.

---

### Question 36
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as printing schema

Which method displays the structure of a DataFrame?

A. `df.schema`  
B. `df.printSchema()`  
C. `df.dtypes`  
D. All of the above

**Correct Answer:** D  
**Explanation:** `schema` returns the StructType, `printSchema()` prints it formatted, and `dtypes` returns column names with types as a list.

---

### Question 37
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify advantages and challenges of implementing Spark

Which scenario would NOT benefit from using Apache Spark?

A. Processing small datasets (< 1GB) on a single machine  
B. Iterative machine learning algorithms  
C. Real-time stream processing  
D. Large-scale ETL operations

**Correct Answer:** A  
**Explanation:** Spark's distributed processing overhead may not be justified for small datasets that can be processed efficiently on a single machine.

---

### Question 38
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the correct way to register a Python UDF?

```python
def square(x):
    return x * x
```

A. `spark.udf.register("square_udf", square, IntegerType())`  
B. `square_udf = udf(square, IntegerType())`  
C. `@udf(returnType=IntegerType())`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three are valid ways to create UDFs. Method A registers for SQL use, B creates for DataFrame API, C uses decorator syntax.

---

### Question 39
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the execution patterns of Apache Spark engine

Which statement about lazy evaluation is TRUE?

A. It allows Spark to optimize the entire query plan  
B. It reduces memory usage by avoiding intermediate results  
C. It enables fault recovery by re-executing from the beginning  
D. All of the above

**Correct Answer:** D  
**Explanation:** Lazy evaluation enables query optimization, reduces memory usage, and supports fault tolerance through lineage.

---

### Question 40
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you add 30 days to a date column?

A. `date_add(col("date_column"), 30)`  
B. `col("date_column") + 30`  
C. `add_days(col("date_column"), 30)`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** `date_add()` is the correct function to add days to a date. Simple arithmetic operators don't work with date columns.

---

### Question 41
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the role of core components of Apache Spark's Architecture

What runs inside each executor?

A. Driver program  
B. Tasks  
C. SparkContext  
D. Cluster manager

**Correct Answer:** B  
**Explanation:** Executors run tasks that are sent by the driver. The driver and cluster manager run separately.

---

### Question 42
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which aggregation produces a summary with count, mean, stddev, min, and max?

A. `df.describe()`  
B. `df.summary()`  
C. `df.agg(count("*"), mean("col"), stddev("col"), min("col"), max("col"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `describe()` and `summary()` produce statistical summaries, though `summary()` provides more percentiles.

---

### Question 43
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

How do you check the number of partitions in a DataFrame?

A. `df.rdd.getNumPartitions()`  
B. `df.partitions.count()`  
C. `df.getPartitionCount()`  
D. `len(df.partitions)`

**Correct Answer:** A  
**Explanation:** You need to access the underlying RDD to get partition count using `getNumPartitions()`.

---

### Question 44
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

What's the difference between `union()` and `unionAll()`?

A. union() removes duplicates, unionAll() keeps them  
B. unionAll() is deprecated, use union() instead  
C. union() requires same schema, unionAll() doesn't  
D. No difference in current Spark versions

**Correct Answer:** D  
**Explanation:** In current Spark versions, `union()` and `unionAll()` behave the same way - they don't remove duplicates. Use `union().distinct()` to remove duplicates.

---

### Question 45
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the architecture of Apache Spark

What happens when an executor fails during job execution?

A. The entire job fails  
B. The stage is recomputed on another executor  
C. Only the failed tasks are retried  
D. The application shuts down

**Correct Answer:** C  
**Explanation:** Spark automatically retries failed tasks on other executors using the RDD lineage information.

---

### Question 46
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you explode an array column into multiple rows?

A. `df.select("*", explode(col("array_column")).alias("item"))`  
B. `df.withColumn("item", explode(col("array_column")))`  
C. `df.explode("array_column")`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** `explode()` must be used with `select()`. Using it with `withColumn()` would try to add the exploded values as a new column, which isn't valid.

---

### Question 47
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe different types of variables in Spark

When should you use broadcast variables?

A. When sharing large read-only lookup tables  
B. When the data is larger than available memory  
C. When data changes frequently during execution  
D. When implementing counters across tasks

**Correct Answer:** A  
**Explanation:** Broadcast variables are ideal for sharing large read-only data (like lookup tables) efficiently across all nodes.

---

### Question 48
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as sorting

Which sorting operation is more efficient for large datasets?

A. `df.sort("column")`  
B. `df.orderBy("column")`  
C. Both are equivalent  
D. It depends on the data distribution

**Correct Answer:** C  
**Explanation:** `sort()` and `orderBy()` are aliases and perform identical operations with the same efficiency.

---

### Question 49
**Section:** Apache Spark Architecture and Components  
**Objective:** Explain the Apache Spark Architecture execution hierarchy

What triggers the creation of a new job in Spark?

A. Any transformation  
B. Any action  
C. Creating a new DataFrame  
D. Calling cache()

**Correct Answer:** B  
**Explanation:** Each action (like `collect()`, `show()`, `save()`) triggers the creation of a new job in Spark.

---

### Question 50
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage input and output operations

Which format preserves the exact schema when writing and reading data?

A. CSV  
B. JSON  
C. Parquet  
D. Text

**Correct Answer:** C  
**Explanation:** Parquet is a columnar format that preserves schema information, data types, and provides efficient compression.

---

### Question 51
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the features of Apache Spark Modules

Which module provides the Dataset API?

A. Spark Core  
B. Spark SQL  
C. Spark MLlib  
D. Spark Streaming

**Correct Answer:** B  
**Explanation:** The Dataset API is part of Spark SQL module, along with DataFrames and the Catalyst optimizer.

---

### Question 52
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data validation operations on DataFrames

How do you check if a DataFrame is empty?

A. `df.count() == 0`  
B. `df.isEmpty()`  
C. `len(df) == 0`  
D. `df.rdd.isEmpty()`

**Correct Answer:** D  
**Explanation:** `df.rdd.isEmpty()` is the most efficient way as it doesn't require counting all records like `count() == 0`.

---

### Question 53
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

What's the recommended partition size for optimal performance?

A. 64MB - 256MB  
B. 1MB - 64MB  
C. 256MB - 1GB  
D. It varies by use case

**Correct Answer:** A  
**Explanation:** The general recommendation is 64MB to 256MB per partition for optimal performance, balancing parallelism and overhead.

---

### Question 54
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Which function splits a string column into an array?

A. `split(col("column"), delimiter)`  
B. `explode(col("column"))`  
C. `array_split(col("column"), delimiter)`  
D. `tokenize(col("column"), delimiter)`

**Correct Answer:** A  
**Explanation:** The `split()` function splits a string column into an array using a delimiter pattern.

---

### Question 55
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe the architecture of Apache Spark

What is the purpose of the Catalyst optimizer?

A. Optimize RDD operations  
B. Optimize DataFrame and SQL operations  
C. Manage memory allocation  
D. Handle fault tolerance

**Correct Answer:** B  
**Explanation:** The Catalyst optimizer optimizes DataFrame and SQL operations through rule-based and cost-based optimization.

---

### Question 56
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate multiple aggregations in one operation?

A. `df.groupBy("category").agg(sum("amount"), avg("price"), count("*"))`  
B. `df.groupBy("category").sum("amount").avg("price").count()`  
C. Multiple calls to different aggregation functions  
D. Only A is correct

**Correct Answer:** D  
**Explanation:** The `agg()` method allows multiple aggregations in a single operation, which is more efficient than chaining.

---

### Question 57
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify advantages and challenges of implementing Spark

What is a potential challenge when using Spark?

A. Memory requirements can be high  
B. Complex operations may require multiple stages  
C. Cluster management overhead  
D. All of the above

**Correct Answer:** D  
**Explanation:** All listed items are potential challenges: high memory usage, complex query plans, and distributed system management complexity.

---

### Question 58
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the performance difference between UDFs and built-in functions?

A. UDFs are faster  
B. Built-in functions are faster  
C. No significant difference  
D. It depends on the function complexity

**Correct Answer:** B  
**Explanation:** Built-in functions are optimized and run in the JVM, while UDFs (especially Python UDFs) have serialization overhead.

---

### Question 59
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning in distributed data processing

When does a shuffle operation occur?

A. When using `join()` operations  
B. When using `groupBy()` operations  
C. When using `repartition()` operations  
D. All of the above

**Correct Answer:** D  
**Explanation:** Shuffles occur during joins, group operations, and explicit repartitioning, as data needs to be redistributed across partitions.

---

### Question 60
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage input and output operations

Which save mode appends data to existing files?

A. `"append"`  
B. `"overwrite"`  
C. `"ignore"`  
D. `"error"`

**Correct Answer:** A  
**Explanation:** The "append" save mode adds new data to existing files without overwriting them.

---

## Answer Key Summary

1. C  2. B  3. D  4. A,B,C,D  5. B  6. D  7. B  8. D  9. B  10. D
11. C  12. D  13. D  14. A  15. A  16. D  17. A,C,E  18. A  19. A  20. A
21. A  22. D  23. A  24. D  25. D  26. D  27. C  28. D  29. B  30. D
31. C  32. A  33. A  34. A  35. B  36. D  37. A  38. D  39. D  40. A
41. B  42. D  43. A  44. D  45. C  46. A  47. A  48. C  49. B  50. C
51. B  52. D  53. A  54. A  55. B  56. D  57. D  58. B  59. D  60. A

## Score Interpretation
- **90-100% (54-60 correct):** Excellent! Ready for certification
- **80-89% (48-53 correct):** Good preparation, review weak areas
- **70-79% (42-47 correct):** Fair understanding, more study needed
- **Below 70% (<42 correct):** Significant preparation required

## Next Steps
- Review explanations for incorrect answers
- Focus on weak topic areas
- Practice with additional exams
- Study the comprehensive guide materials