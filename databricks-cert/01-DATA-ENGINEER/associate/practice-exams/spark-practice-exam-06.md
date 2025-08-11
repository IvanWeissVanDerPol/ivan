# Apache Spark Developer Associate - Practice Exam 06
## Focus: Data Sources & Formats (File Formats, I/O Operations, Schema Evolution)
**Difficulty Level:** Intermediate to Advanced  
**Time Limit:** 90 minutes  
**Questions:** 60

---

### Question 1
**Section:** Using Spark SQL  
**Objective:** Read and write data from external data sources

Which file format provides the best compression ratio for analytical workloads?

A. JSON  
B. CSV  
C. Parquet  
D. Avro

**Correct Answer:** C  
**Explanation:** Parquet provides excellent compression ratios for analytical workloads due to its columnar storage format and built-in compression algorithms.

---

### Question 2
**Section:** Using Spark SQL  
**Objective:** Configure external data source connections

Which JDBC option controls the number of partitions when reading from a database?

A. `numPartitions`  
B. `partitionColumn`  
C. `lowerBound` and `upperBound`  
D. All of the above work together

**Correct Answer:** D  
**Explanation:** All options work together: `numPartitions` sets the count, `partitionColumn` specifies which column to partition on, and `lowerBound`/`upperBound` define the range.

---

### Question 3
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Read data from various file formats

When reading CSV files with headers, which option correctly configures the reader?

A. `.option("header", "true")`  
B. `.option("inferSchema", "true")`  
C. `.option("delimiter", ",")`  
D. All of the above are valid options

**Correct Answer:** D  
**Explanation:** All options are valid for CSV reading: `header` treats first row as column names, `inferSchema` automatically detects types, and `delimiter` specifies the separator.

---

### Question 4
**Section:** Using Spark SQL  
**Objective:** Handle schema evolution in data formats

What happens when you write data with additional columns to an existing Parquet file?

A. The write operation fails  
B. Additional columns are ignored  
C. Schema evolution occurs automatically  
D. Depends on write mode and schema merge settings

**Correct Answer:** D  
**Explanation:** Behavior depends on write mode (append, overwrite) and whether schema merging is enabled (`spark.sql.parquet.mergeSchema`).

---

### Question 5
**Section:** Using Spark SQL  
**Objective:** Optimize data source performance

Which technique improves performance when reading many small files?

A. Using `coalesce()` after reading  
B. Enabling file coalescing in the data source  
C. Using appropriate file formats like Parquet  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques help: coalescing reduces partition count, some sources support file coalescing, and efficient formats reduce I/O overhead.

---

### Question 6
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with JSON data sources

Which mode handles malformed JSON records gracefully?

A. `PERMISSIVE`  
B. `DROPMALFORMED`  
C. `FAILFAST`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `PERMISSIVE` (puts malformed records in a special column) and `DROPMALFORMED` (ignores bad records) handle malformed data gracefully.

---

### Question 7
**Section:** Using Spark SQL  
**Objective:** Configure data source partitioning

When writing partitioned data, which method creates partition directories?

A. `.partitionBy("column")`  
B. `.bucketBy(n, "column")`  
C. `.sortBy("column")`  
D. `.clusterBy("column")`

**Correct Answer:** A  
**Explanation:** `.partitionBy()` creates physical directory partitions based on column values, enabling partition pruning during reads.

---

### Question 8
**Section:** Using Spark SQL  
**Objective:** Handle data source formats and compression

Which compression codec is best for write-once, read-many scenarios?

A. Snappy (fast compression/decompression)  
B. GZIP (high compression ratio)  
C. LZ4 (very fast)  
D. Depends on the priority: speed vs. space

**Correct Answer:** D  
**Explanation:** Choice depends on priorities: Snappy balances speed and compression, GZIP maximizes space savings, LZ4 prioritizes speed.

---

### Question 9
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Read from streaming data sources

Which data source is commonly used for real-time streaming?

A. HDFS files  
B. Kafka  
C. JDBC databases  
D. Local files

**Correct Answer:** B  
**Explanation:** Kafka is the most common streaming data source, designed for real-time data ingestion and processing.

---

### Question 10
**Section:** Using Spark SQL  
**Objective:** Apply predicate pushdown optimizations

Which file format supports predicate pushdown to the storage layer?

A. CSV  
B. JSON  
C. Parquet  
D. Text files

**Correct Answer:** C  
**Explanation:** Parquet supports predicate pushdown, allowing filters to be applied at the storage level, reducing data read.

---

### Question 11
**Section:** Using Spark SQL  
**Objective:** Configure save modes for data writes

What does `SaveMode.Append` do when the target already exists?

A. Overwrites existing data  
B. Adds new data to existing data  
C. Fails with an error  
D. Ignores the write operation

**Correct Answer:** B  
**Explanation:** `SaveMode.Append` adds new data to existing data without overwriting the existing content.

---

### Question 12
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source authentication

How do you pass authentication credentials when reading from JDBC?

A. In the JDBC URL  
B. Using `.option("user", "username")` and `.option("password", "password")`  
C. Through connection properties  
D. All of the above methods work

**Correct Answer:** D  
**Explanation:** Credentials can be passed via URL, as options, or through connection properties, depending on security requirements.

---

### Question 13
**Section:** Using Spark SQL  
**Objective:** Work with Delta Lake format

What is the main advantage of Delta Lake over Parquet?

A. Better compression  
B. ACID transactions and time travel  
C. Faster writes  
D. Smaller file sizes

**Correct Answer:** B  
**Explanation:** Delta Lake provides ACID transactions, time travel, and schema evolution on top of Parquet, enabling reliable data lake operations.

---

### Question 14
**Section:** Using Spark SQL  
**Objective:** Configure data source batch sizes

Which JDBC option controls how many rows are fetched in each batch?

A. `batchSize`  
B. `fetchSize`  
C. `batchsize`  
D. `fetchsize`

**Correct Answer:** B  
**Explanation:** `fetchSize` controls how many rows the JDBC driver fetches in each round trip to the database.

---

### Question 15
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle schema inference optimization

When is explicit schema definition preferred over schema inference?

A. For small datasets  
B. For one-time exploratory analysis  
C. For production jobs with stable schemas  
D. Schema definition is never preferred

**Correct Answer:** C  
**Explanation:** Explicit schemas are preferred in production for better performance, type safety, and avoiding inference overhead.

---

### Question 16
**Section:** Using Spark SQL  
**Objective:** Work with complex file structures

How do you read nested directories with different schemas?

A. Enable schema merging  
B. Use a union of DataFrames  
C. Define a common schema  
D. All approaches can work

**Correct Answer:** D  
**Explanation:** All approaches work: schema merging handles variations, unions combine different structures, and common schemas enforce consistency.

---

### Question 17
**Section:** Using Spark SQL  
**Objective:** Optimize write operations

Which technique improves write performance for large datasets?

A. Partitioning data appropriately  
B. Using optimal file sizes (128MB-1GB)  
C. Choosing efficient compression  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques improve write performance: partitioning enables parallel writes, optimal file sizes balance parallelism and overhead, and compression reduces I/O.

---

### Question 18
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source errors

What happens when reading fails for some files in a directory?

A. The entire operation fails  
B. Successful files are processed, failed files are skipped  
C. Depends on the `ignoreCorruptFiles` setting  
D. Failed files are retried automatically

**Correct Answer:** C  
**Explanation:** With `spark.sql.files.ignoreCorruptFiles=true`, corrupt files are skipped; otherwise, the operation fails.

---

### Question 19
**Section:** Using Spark SQL  
**Objective:** Configure data source caching

Which data sources benefit most from caching?

A. Data sources read multiple times  
B. Expensive-to-compute derived datasets  
C. Frequently accessed lookup tables  
D. All of the above

**Correct Answer:** D  
**Explanation:** All scenarios benefit from caching: repeated reads, expensive computations, and frequent lookups all see performance improvements.

---

### Question 20
**Section:** Using Spark SQL  
**Objective:** Work with external table management

What's the difference between managed and external tables?

A. Managed tables are faster  
B. Managed tables' data is managed by Spark, external tables point to existing data  
C. External tables support more formats  
D. No difference in functionality

**Correct Answer:** B  
**Explanation:** Managed tables have their data lifecycle controlled by Spark (dropped with table), while external tables reference existing data locations.

---

### Question 21
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source transformations during read

Which transformation can be applied during the read operation?

A. Column selection (projection)  
B. Row filtering (predicate pushdown)  
C. Data type conversion  
D. All of the above

**Correct Answer:** D  
**Explanation:** Modern data sources support pushdown optimizations including projection, filtering, and some type conversions at the source level.

---

### Question 22
**Section:** Using Spark SQL  
**Objective:** Configure connection pooling

How can you optimize JDBC connection usage?

A. Use connection pooling  
B. Reuse connections across partitions  
C. Configure appropriate fetch sizes  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques optimize JDBC usage: pooling reduces connection overhead, reuse minimizes setup costs, and proper fetch sizes improve throughput.

---

### Question 23
**Section:** Using Spark SQL  
**Objective:** Handle large object data types

Which approach handles BLOB data effectively in Spark?

A. Read as binary data type  
B. Convert to base64 strings  
C. Use external storage with references  
D. All approaches have trade-offs

**Correct Answer:** D  
**Explanation:** Each approach has trade-offs: binary type for direct processing, base64 for text compatibility, external storage for very large objects.

---

### Question 24
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with time-partitioned data

Which pattern is most efficient for reading time-series data?

A. Read all data and filter by date  
B. Use partition pruning with date-based partitions  
C. Read data in small batches  
D. Use streaming reads

**Correct Answer:** B  
**Explanation:** Date-based partitioning with partition pruning reads only relevant partitions, minimizing data scanning.

---

### Question 25
**Section:** Using Spark SQL  
**Objective:** Configure data format specific options

Which Parquet-specific optimization improves query performance?

A. Column pruning  
B. Predicate pushdown  
C. Dictionary encoding  
D. All of the above

**Correct Answer:** D  
**Explanation:** Parquet supports all optimizations: column pruning reads only needed columns, predicate pushdown filters at storage level, and dictionary encoding improves compression and filtering.

---

### Question 26
**Section:** Using Spark SQL  
**Objective:** Handle data source failover

Which strategy provides resilience when primary data source fails?

A. Retry mechanism with exponential backoff  
B. Multiple data source locations  
C. Circuit breaker pattern  
D. All strategies can be combined

**Correct Answer:** D  
**Explanation:** Comprehensive resilience combines retries, multiple sources, and circuit breakers to handle different failure scenarios.

---

### Question 27
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize schema operations

When reading Avro files, how is schema handled?

A. Schema is embedded in the file  
B. Schema must be provided separately  
C. Schema is inferred automatically  
D. Avro doesn't support schemas

**Correct Answer:** A  
**Explanation:** Avro files embed schema information, making them self-describing and enabling schema evolution.

---

### Question 28
**Section:** Using Spark SQL  
**Objective:** Configure write optimization

Which technique prevents small file problems when writing?

A. Using appropriate `maxRecordsPerFile`  
B. Coalescing before writing  
C. Using bucketing  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques help: `maxRecordsPerFile` limits file size, coalescing reduces partition count, and bucketing controls file distribution.

---

### Question 29
**Section:** Using Spark SQL  
**Objective:** Work with nested data structures

Which format handles deeply nested data most efficiently?

A. CSV (flattened)  
B. JSON  
C. Parquet with nested types  
D. Avro

**Correct Answer:** C  
**Explanation:** Parquet with nested types provides columnar efficiency even for nested structures, offering better query performance than other formats.

---

### Question 30
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source metadata

How can you access file metadata (path, modification time) when reading?

A. Enable `pathGlobFilter`  
B. Add `input_file_name()` and `input_file_block_start()` functions  
C. Use `modifiedBefore` and `modifiedAfter` options  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Input functions provide file metadata during processing, while modified time options filter files based on timestamps.

---

### Question 31
**Section:** Using Spark SQL  
**Objective:** Configure data source security

Which approach secures sensitive data in configuration?

A. Hardcode credentials in code  
B. Use environment variables  
C. Use external credential providers  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both environment variables and external credential providers avoid hardcoding sensitive information, with external providers offering more advanced security features.

---

### Question 32
**Section:** Using Spark SQL  
**Objective:** Handle data source versioning

How do you handle backward compatibility when data format changes?

A. Always use the latest format version  
B. Maintain multiple readers for different versions  
C. Use formats that support schema evolution  
D. Convert old data to new format

**Correct Answer:** C  
**Explanation:** Using formats that support schema evolution (like Parquet, Avro, Delta Lake) provides the most maintainable approach to format changes.

---

### Question 33
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize data source parallelism

How does Spark determine the number of partitions when reading files?

A. One partition per file  
B. Based on total file size and target partition size  
C. Fixed number based on cluster size  
D. User must specify explicitly

**Correct Answer:** B  
**Explanation:** Spark calculates partitions based on total input size divided by target partition size (default ~128MB), ensuring balanced partitions.

---

### Question 34
**Section:** Using Spark SQL  
**Objective:** Work with data source statistics

How do column statistics improve query performance?

A. Enable cost-based optimization  
B. Improve join strategy selection  
C. Enable better predicate pushdown  
D. All of the above

**Correct Answer:** D  
**Explanation:** Column statistics enable CBO for better query plans, help choose optimal join strategies, and improve pushdown optimizations.

---

### Question 35
**Section:** Using Spark SQL  
**Objective:** Configure data source timeouts

Which setting controls timeout for JDBC connections?

A. `connectTimeout`  
B. `socketTimeout`  
C. `queryTimeout`  
D. All are relevant timeout settings

**Correct Answer:** D  
**Explanation:** Different timeout settings control different aspects: connection establishment, socket operations, and query execution.

---

### Question 36
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source transactions

Which data source supports transactional writes natively?

A. Parquet  
B. Delta Lake  
C. JSON  
D. CSV

**Correct Answer:** B  
**Explanation:** Delta Lake provides ACID transaction support, while other formats don't guarantee atomic writes at the table level.

---

### Question 37
**Section:** Using Spark SQL  
**Objective:** Optimize data source reads

Which technique reduces data read during aggregations?

A. Column pruning  
B. Predicate pushdown  
C. Partition pruning  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques reduce data read: column pruning reads only needed columns, predicate pushdown filters early, and partition pruning skips irrelevant partitions.

---

### Question 38
**Section:** Using Spark SQL  
**Objective:** Handle data source consistency

How do you ensure data consistency when reading from eventually consistent storage?

A. Use strong consistency settings  
B. Implement retry logic  
C. Read from replicated sources  
D. All strategies may be needed

**Correct Answer:** D  
**Explanation:** Different strategies address different consistency challenges: strong consistency when available, retries for transient issues, and replication for availability.

---

### Question 39
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with data source catalogs

What is the advantage of using data catalogs?

A. Centralized metadata management  
B. Schema discovery and evolution tracking  
C. Access control integration  
D. All of the above

**Correct Answer:** D  
**Explanation:** Data catalogs provide comprehensive metadata management, schema tracking, and security integration for enterprise data management.

---

### Question 40
**Section:** Using Spark SQL  
**Objective:** Configure data source monitoring

Which metrics help monitor data source performance?

A. Read/write throughput  
B. Connection pool utilization  
C. Error rates and latency  
D. All of the above

**Correct Answer:** D  
**Explanation:** Comprehensive monitoring includes throughput metrics, resource utilization, and error tracking to identify performance issues.

---

### Question 41
**Section:** Using Spark SQL  
**Objective:** Handle data source encoding

Which encoding issue commonly occurs when reading text files?

A. Character set mismatches  
B. Line ending differences  
C. Byte order marks (BOM)  
D. All of the above

**Correct Answer:** D  
**Explanation:** All encoding issues can occur: character set mismatches cause garbled text, line endings affect parsing, and BOMs can appear as extra characters.

---

### Question 42
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize data source writes

Which write strategy minimizes impact on concurrent readers?

A. Write to temporary location then atomic move  
B. Write directly to final location  
C. Write with overwrite mode  
D. Write to multiple locations simultaneously

**Correct Answer:** A  
**Explanation:** Writing to temporary location then atomic move ensures readers see complete data and prevents reading partial writes.

---

### Question 43
**Section:** Using Spark SQL  
**Objective:** Work with data source compression

Which compression algorithm provides the best query performance?

A. GZIP (high compression)  
B. Snappy (balanced performance)  
C. LZ4 (fast decompression)  
D. Depends on workload characteristics

**Correct Answer:** D  
**Explanation:** Optimal compression depends on workload: CPU-bound workloads may prefer less compression, I/O-bound workloads benefit from higher compression ratios.

---

### Question 44
**Section:** Using Spark SQL  
**Objective:** Handle data source evolution

Which approach manages schema changes in production pipelines?

A. Version control for schemas  
B. Schema registry integration  
C. Backward compatibility testing  
D. All approaches are recommended

**Correct Answer:** D  
**Explanation:** Production schema management requires versioning, registries for sharing schemas, and compatibility testing to prevent breaking changes.

---

### Question 45
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Configure data source batching

How does batch size affect JDBC read performance?

A. Larger batches always perform better  
B. Optimal batch size depends on network and memory  
C. Batch size doesn't affect performance  
D. Smaller batches reduce memory usage only

**Correct Answer:** B  
**Explanation:** Optimal batch size balances network round trips (favor larger batches) with memory usage and processing latency (favor smaller batches).

---

### Question 46
**Section:** Using Spark SQL  
**Objective:** Work with data source partitioning strategies

Which partitioning strategy is best for time-series data?

A. Hash partitioning on timestamp  
B. Range partitioning by date  
C. Random partitioning  
D. No partitioning

**Correct Answer:** B  
**Explanation:** Range partitioning by date enables efficient time-based queries through partition pruning, which is common for time-series analytics.

---

### Question 47
**Section:** Using Spark SQL  
**Objective:** Handle data source conflicts

What happens when writing with SaveMode.ErrorIfExists and target exists?

A. Data is appended  
B. Data is overwritten  
C. An exception is thrown  
D. Write operation is ignored

**Correct Answer:** C  
**Explanation:** SaveMode.ErrorIfExists throws an exception if the target already exists, preventing accidental data overwrites.

---

### Question 48
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize data source memory usage

Which technique reduces memory usage when reading large files?

A. Streaming reads  
B. Appropriate partition sizing  
C. Column pruning  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques reduce memory usage: streaming processes incrementally, proper partitioning controls memory per partition, and column pruning reduces data volume.

---

### Question 49
**Section:** Using Spark SQL  
**Objective:** Configure data source reliability

Which pattern improves reliability for critical data operations?

A. Idempotent writes  
B. Checkpointing intermediate results  
C. Multi-location backups  
D. All patterns improve reliability

**Correct Answer:** D  
**Explanation:** All patterns contribute to reliability: idempotent operations can be safely retried, checkpointing prevents data loss, and backups provide recovery options.

---

### Question 50
**Section:** Using Spark SQL  
**Objective:** Work with data source performance optimization

Which technique provides the best performance for analytical queries?

A. Row-based formats like CSV  
B. Columnar formats like Parquet  
C. Document formats like JSON  
D. Format doesn't affect performance

**Correct Answer:** B  
**Explanation:** Columnar formats like Parquet provide superior performance for analytical queries through column pruning, compression, and encoding optimizations.

---

### Question 51
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source validation

How can you validate data quality during reads?

A. Schema enforcement  
B. Custom validation UDFs  
C. Data profiling and statistics  
D. All approaches can be used

**Correct Answer:** D  
**Explanation:** Comprehensive data validation combines schema enforcement for structure, UDFs for business rules, and profiling for data quality assessment.

---

### Question 52
**Section:** Using Spark SQL  
**Objective:** Configure data source networking

Which network optimization improves data source performance?

A. Connection pooling  
B. Compression for network transfers  
C. Parallel connections  
D. All optimizations help

**Correct Answer:** D  
**Explanation:** All network optimizations contribute: pooling reduces connection overhead, compression reduces transfer size, and parallelism improves throughput.

---

### Question 53
**Section:** Using Spark SQL  
**Objective:** Handle data source formats compatibility

Which format provides the best cross-platform compatibility?

A. Parquet  
B. Avro  
C. ORC  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both Parquet and Avro provide excellent cross-platform compatibility and are supported by most big data tools, while ORC is more Hive-centric.

---

### Question 54
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize data source integration

Which approach facilitates integration with external systems?

A. Standard APIs and protocols  
B. Custom connectors  
C. Data format standardization  
D. All approaches help integration

**Correct Answer:** D  
**Explanation:** Integration benefits from standard APIs for compatibility, custom connectors for specific systems, and format standards for interoperability.

---

### Question 55
**Section:** Using Spark SQL  
**Objective:** Work with data source lineage

How can you track data lineage across different sources?

A. Metadata management systems  
B. Custom logging and tracking  
C. Built-in Spark lineage features  
D. All methods can track lineage

**Correct Answer:** D  
**Explanation:** Data lineage can be tracked through dedicated systems, custom implementations, or leveraging Spark's built-in capabilities, depending on requirements.

---

### Question 56
**Section:** Using Spark SQL  
**Objective:** Configure data source scalability

Which factor most impacts data source scalability?

A. Parallelism and partitioning strategy  
B. Network bandwidth  
C. Storage system performance  
D. All factors affect scalability

**Correct Answer:** D  
**Explanation:** Scalability depends on all factors: proper parallelism utilizes resources, network bandwidth affects data transfer, and storage performance limits throughput.

---

### Question 57
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data source migration

Which strategy minimizes downtime during data source migration?

A. Blue-green deployment pattern  
B. Gradual migration with dual writes  
C. Snapshot and restore approach  
D. All strategies can minimize downtime

**Correct Answer:** D  
**Explanation:** Different strategies suit different scenarios: blue-green for complete switches, dual writes for gradual migration, and snapshots for consistency requirements.

---

### Question 58
**Section:** Using Spark SQL  
**Objective:** Optimize data source costs

Which approach optimizes cloud storage costs?

A. Lifecycle management policies  
B. Compression and efficient formats  
C. Intelligent tiering  
D. All approaches reduce costs

**Correct Answer:** D  
**Explanation:** Cost optimization combines lifecycle policies for automated management, efficient formats to reduce storage needs, and tiering for cost-appropriate access patterns.

---

### Question 59
**Section:** Using Spark SQL  
**Objective:** Work with data source governance

Which practice supports data governance requirements?

A. Access control and audit logging  
B. Data classification and tagging  
C. Retention policy enforcement  
D. All practices support governance

**Correct Answer:** D  
**Explanation:** Comprehensive governance requires access controls for security, classification for appropriate handling, and retention policies for compliance.

---

### Question 60
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement comprehensive data source strategies

Which approach provides the most robust data source architecture?

A. Single source of truth with caching  
B. Multi-source federation with consistency checks  
C. Event-driven architecture with real-time sync  
D. The best approach depends on requirements

**Correct Answer:** D  
**Explanation:** Optimal architecture depends on specific requirements: single source for simplicity, federation for flexibility, or event-driven for real-time needs.

---

## Answer Key Summary

1. C  2. D  3. D  4. D  5. D  6. D  7. A  8. D  9. B  10. C
11. B  12. D  13. B  14. B  15. C  16. D  17. D  18. C  19. D  20. B
21. D  22. D  23. D  24. B  25. D  26. D  27. A  28. D  29. C  30. D
31. D  32. C  33. B  34. D  35. D  36. B  37. D  38. D  39. D  40. D
41. D  42. A  43. D  44. D  45. B  46. B  47. C  48. D  49. D  50. B
51. D  52. D  53. D  54. D  55. D  56. D  57. D  58. D  59. D  60. D

## Score Interpretation
- **90-100% (54-60 correct):** Excellent! Data sources and formats expert
- **80-89% (48-53 correct):** Good preparation, review advanced I/O optimization
- **70-79% (42-47 correct):** Fair understanding, focus on file formats and data source configuration
- **Below 70% (<42 correct):** More study needed on data sources and I/O operations

## Next Steps
- Review explanations for incorrect answers
- Practice with different file formats and their optimization techniques
- Study data source security and governance practices
- Focus on production data pipeline patterns