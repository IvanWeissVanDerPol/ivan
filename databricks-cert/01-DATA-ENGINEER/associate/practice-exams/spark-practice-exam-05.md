# Apache Spark Developer Associate - Practice Exam 05
## Focus: Performance Optimization (Caching, Broadcasting, Resource Tuning)
**Difficulty Level:** Intermediate to Advanced  
**Time Limit:** 90 minutes  
**Questions:** 65

---

### Question 1
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize caching strategies

Which storage level provides the best balance of performance and fault tolerance for frequently accessed DataFrames?

A. MEMORY_ONLY  
B. MEMORY_AND_DISK  
C. MEMORY_AND_DISK_SER  
D. DISK_ONLY

**Correct Answer:** B  
**Explanation:** MEMORY_AND_DISK provides good performance with memory caching and fault tolerance by spilling to disk when memory is insufficient.

---

### Question 2
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply broadcast optimization strategies

When should you use broadcast joins?

A. When both DataFrames are large  
B. When one DataFrame is small enough to fit in driver memory  
C. When joining on multiple columns  
D. Always, as they are faster than other join types

**Correct Answer:** B  
**Explanation:** Broadcast joins are effective when one DataFrame is small enough (typically < 10MB by default) to be broadcast to all nodes.

---

### Question 3
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark partitioning

What is the recommended partition size for optimal performance?

A. 64 MB  
B. 128 MB  
C. 256 MB  
D. 512 MB

**Correct Answer:** B  
**Explanation:** 128 MB is generally recommended as it balances parallelism with overhead. Too small partitions create overhead, too large partitions reduce parallelism.

---

### Question 4
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize memory usage

Which configuration parameter controls the fraction of heap space used for caching?

A. `spark.storage.memoryFraction`  
B. `spark.memory.fraction`  
C. `spark.cache.memoryFraction`  
D. `spark.executor.memoryFraction`

**Correct Answer:** B  
**Explanation:** `spark.memory.fraction` (default 0.6) controls the fraction of heap space used for execution and caching combined.

---

### Question 5
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply adaptive query execution

Which AQE feature automatically optimizes join strategies based on runtime statistics?

A. Dynamic coalescing  
B. Dynamic join selection  
C. Dynamic partition pruning  
D. Dynamic filter pushdown

**Correct Answer:** B  
**Explanation:** Dynamic join selection in AQE can switch from sort-merge to broadcast joins based on actual data sizes observed at runtime.

---

### Question 6
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure executor resources

What happens when you set too few executor cores?

A. Memory usage increases  
B. Parallelism decreases  
C. Network I/O increases  
D. Storage requirements increase

**Correct Answer:** B  
**Explanation:** Too few executor cores reduces parallelism, leading to underutilization of cluster resources and longer execution times.

---

### Question 7
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize data serialization

Which serialization format is recommended for better performance?

A. Java serialization  
B. Kryo serialization  
C. Avro serialization  
D. JSON serialization

**Correct Answer:** B  
**Explanation:** Kryo serialization is faster and more compact than Java's default serialization, improving shuffle performance.

---

### Question 8
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply caching best practices

Which DataFrame operation benefits most from caching?

A. DataFrames used once  
B. DataFrames used multiple times in the same action  
C. DataFrames used multiple times across different actions  
D. Large DataFrames regardless of usage

**Correct Answer:** C  
**Explanation:** Caching is most beneficial for DataFrames used multiple times across different actions, as it avoids recomputation.

---

### Question 9
**Section:** Apache Spark Architecture and Components  
**Objective:** Optimize shuffle operations

Which configuration reduces shuffle overhead?

A. Increasing partition count  
B. Enabling adaptive query execution  
C. Using broadcast variables  
D. All of the above

**Correct Answer:** D  
**Explanation:** All options can reduce shuffle overhead: proper partitioning, AQE optimizations, and broadcast variables for small datasets.

---

### Question 10
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Monitor and tune garbage collection

Which JVM flag is commonly used to optimize GC for Spark workloads?

A. `-XX:+UseG1GC`  
B. `-XX:+UseParallelGC`  
C. `-XX:+UseSerialGC`  
D. `-XX:+UseConcMarkSweepGC`

**Correct Answer:** A  
**Explanation:** G1GC is often preferred for Spark because it provides predictable pause times and handles large heaps well.

---

### Question 11
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize broadcast variables

What is the maximum recommended size for broadcast variables?

A. 1 MB  
B. 10 MB  
C. 100 MB  
D. 1 GB

**Correct Answer:** C  
**Explanation:** Broadcast variables should typically be under 100 MB to avoid network overhead and driver memory issues.

---

### Question 12
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure dynamic allocation

Which setting enables dynamic allocation of executors?

A. `spark.dynamicAllocation.enabled = true`  
B. `spark.executor.dynamicAllocation = true`  
C. `spark.cluster.dynamicAllocation = true`  
D. `spark.adaptive.dynamicAllocation = true`

**Correct Answer:** A  
**Explanation:** `spark.dynamicAllocation.enabled` controls whether Spark can dynamically add or remove executors based on workload.

---

### Question 13
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply data skew handling

Which technique helps handle data skew in joins?

A. Salting keys  
B. Broadcast joins  
C. Bucketing  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques can help with data skew: salting distributes skewed keys, broadcast joins avoid shuffles, and bucketing pre-distributes data.

---

### Question 14
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize storage levels

When should you use MEMORY_ONLY_SER storage level?

A. When memory is abundant  
B. When memory is limited but CPU is available  
C. When data is accessed infrequently  
D. Never, it's deprecated

**Correct Answer:** B  
**Explanation:** MEMORY_ONLY_SER saves memory through serialization at the cost of CPU overhead for deserialization, useful when memory is constrained.

---

### Question 15
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure cluster resources

What is the relationship between executor cores and concurrent tasks?

A. One task per executor regardless of cores  
B. Multiple tasks can run per executor based on core count  
C. Tasks run sequentially within an executor  
D. Core count doesn't affect task parallelism

**Correct Answer:** B  
**Explanation:** Each executor can run multiple tasks concurrently, with the number of concurrent tasks typically equal to the number of cores.

---

### Question 16
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply performance monitoring techniques

Which Spark UI tab provides information about storage and caching?

A. Jobs tab  
B. Stages tab  
C. Storage tab  
D. Executors tab

**Correct Answer:** C  
**Explanation:** The Storage tab shows cached RDDs and DataFrames, their storage levels, memory usage, and cache hit rates.

---

### Question 17
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize join operations

Which join hint forces a broadcast join?

A. `/*+ BROADCAST(table) */`  
B. `/*+ MERGE(table) */`  
C. `/*+ SHUFFLE_HASH(table) */`  
D. `/*+ SORT_MERGE(table) */`

**Correct Answer:** A  
**Explanation:** The `/*+ BROADCAST(table) */` hint forces Spark to use broadcast join for the specified table.

---

### Question 18
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure shuffle behavior

Which configuration controls the number of partitions in shuffle operations?

A. `spark.sql.shuffle.partitions`  
B. `spark.shuffle.partitions`  
C. `spark.default.parallelism`  
D. `spark.executor.cores`

**Correct Answer:** A  
**Explanation:** `spark.sql.shuffle.partitions` (default 200) controls the number of partitions used in shuffles for DataFrame operations.

---

### Question 19
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply columnar storage optimizations

Which file format provides the best compression and query performance?

A. JSON  
B. CSV  
C. Parquet  
D. Text

**Correct Answer:** C  
**Explanation:** Parquet provides columnar storage with excellent compression ratios and supports predicate pushdown for optimal query performance.

---

### Question 20
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize memory management

What indicates that an application might benefit from increasing executor memory?

A. High GC time in Spark UI  
B. Frequent disk spills  
C. OutOfMemoryError exceptions  
D. All of the above

**Correct Answer:** D  
**Explanation:** All symptoms indicate memory pressure that could benefit from increased executor memory allocation.

---

### Question 21
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark session settings

Which configuration enables cost-based optimization?

A. `spark.sql.cbo.enabled = true`  
B. `spark.sql.adaptive.enabled = true`  
C. `spark.sql.optimizer.enabled = true`  
D. `spark.sql.cbo.joinReorder.enabled = true`

**Correct Answer:** A  
**Explanation:** `spark.sql.cbo.enabled` enables cost-based optimization, which uses table statistics to optimize query plans.

---

### Question 22
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply predicate pushdown optimizations

Which operation benefits from predicate pushdown?

A. Filtering data early in the query plan  
B. Joining large datasets  
C. Aggregating data  
D. Sorting data

**Correct Answer:** A  
**Explanation:** Predicate pushdown moves filter conditions down to the data source level, reducing the amount of data read and processed.

---

### Question 23
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize checkpointing

When should you use checkpointing?

A. After every transformation  
B. For long RDD lineages or iterative algorithms  
C. Only in streaming applications  
D. Never, it slows down processing

**Correct Answer:** B  
**Explanation:** Checkpointing breaks long lineages and is beneficial for iterative algorithms where recomputation would be expensive.

---

### Question 24
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure network optimizations

Which setting improves performance for shuffle-intensive workloads?

A. Increasing `spark.reducer.maxSizeInFlight`  
B. Enabling `spark.shuffle.service.enabled`  
C. Tuning `spark.shuffle.file.buffer`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All settings can improve shuffle performance: larger fetch sizes, external shuffle service, and optimized buffer sizes.

---

### Question 25
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply lazy evaluation optimizations

Which transformation is eager (executes immediately)?

A. `filter()`  
B. `map()`  
C. `cache()`  
D. None of the above

**Correct Answer:** D  
**Explanation:** All DataFrame/RDD transformations including `cache()` are lazy and don't execute until an action is called.

---

### Question 26
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize resource allocation

What's the recommended ratio of executor memory to cores?

A. 1 GB per core  
B. 2-5 GB per core  
C. 10 GB per core  
D. Memory and cores are independent

**Correct Answer:** B  
**Explanation:** A ratio of 2-5 GB memory per core is generally recommended, depending on the workload and data characteristics.

---

### Question 27
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure Spark streaming optimizations

Which configuration improves streaming performance?

A. `spark.streaming.backpressure.enabled`  
B. `spark.streaming.receiver.writeAheadLog.enable`  
C. `spark.streaming.kafka.consumer.cache.enabled`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All configurations can improve streaming performance through backpressure control, fault tolerance, and consumer optimization.

---

### Question 28
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply partition pruning

Which scenario benefits most from partition pruning?

A. Reading entire datasets  
B. Filtering on partition columns  
C. Joining unpartitioned data  
D. Random data access

**Correct Answer:** B  
**Explanation:** Partition pruning is most effective when filtering on partition columns, as entire partitions can be skipped.

---

### Question 29
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize batch size tuning

Which factor determines optimal batch size in streaming?

A. Available memory only  
B. Processing time and latency requirements  
C. Number of cores only  
D. Network bandwidth only

**Correct Answer:** B  
**Explanation:** Optimal batch size balances processing time (must be less than batch interval) with latency requirements and resource utilization.

---

### Question 30
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure task scheduling

What does `spark.task.cpus` control?

A. Number of CPUs per executor  
B. Number of CPUs per task  
C. Total CPUs in cluster  
D. CPU allocation algorithm

**Correct Answer:** B  
**Explanation:** `spark.task.cpus` specifies how many CPU cores each task requires, affecting task parallelism within executors.

---

### Question 31
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply compression optimizations

Which compression codec provides the best balance of compression ratio and speed?

A. GZIP  
B. Snappy  
C. LZ4  
D. BZIP2

**Correct Answer:** B  
**Explanation:** Snappy provides a good balance of compression ratio and speed, making it popular for big data workloads.

---

### Question 32
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize join strategies

When does Spark automatically choose broadcast join?

A. When one side is smaller than `spark.sql.autoBroadcastJoinThreshold`  
B. When both sides are small  
C. When explicitly hinted  
D. Both A and C

**Correct Answer:** D  
**Explanation:** Spark chooses broadcast joins automatically based on size threshold or when explicitly hinted with broadcast join hints.

---

### Question 33
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure garbage collection optimization

Which GC strategy is best for large executor heaps?

A. Parallel GC  
B. G1GC  
C. Serial GC  
D. CMS GC

**Correct Answer:** B  
**Explanation:** G1GC handles large heaps better with more predictable pause times compared to other garbage collectors.

---

### Question 34
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply data locality optimizations

What does PROCESS_LOCAL data locality mean?

A. Data is on the same node  
B. Data is in the same JVM process  
C. Data is in the same rack  
D. Data is remote

**Correct Answer:** B  
**Explanation:** PROCESS_LOCAL means data and computation are in the same JVM process, providing the best data locality.

---

### Question 35
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize storage format selection

Which storage format supports schema evolution best?

A. CSV  
B. JSON  
C. Parquet  
D. Avro

**Correct Answer:** C  
**Explanation:** Parquet supports schema evolution well, allowing addition of columns and some type changes while maintaining compatibility.

---

### Question 36
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure executor lifetime management

What does `spark.dynamicAllocation.maxExecutors` control?

A. Maximum executors that can be allocated  
B. Initial number of executors  
C. Executors per node  
D. Executor core count

**Correct Answer:** A  
**Explanation:** `spark.dynamicAllocation.maxExecutors` sets the upper bound on the number of executors that can be dynamically allocated.

---

### Question 37
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply bucketing optimizations

How does bucketing improve join performance?

A. Reduces data size  
B. Pre-distributes data to avoid shuffles  
C. Enables compression  
D. Improves serialization

**Correct Answer:** B  
**Explanation:** Bucketing pre-distributes data based on join keys, allowing joins to avoid expensive shuffle operations.

---

### Question 38
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize cache eviction policies

Which storage level allows Spark to evict cached data when memory is needed?

A. MEMORY_ONLY  
B. MEMORY_AND_DISK  
C. DISK_ONLY  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both MEMORY_ONLY and MEMORY_AND_DISK allow eviction. MEMORY_ONLY recomputes evicted data, while MEMORY_AND_DISK spills to disk.

---

### Question 39
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure shuffle compression

Which setting enables shuffle compression?

A. `spark.shuffle.compress = true`  
B. `spark.io.compression.codec`  
C. Both A and B work together  
D. Shuffle compression is automatic

**Correct Answer:** C  
**Explanation:** `spark.shuffle.compress` enables compression, and `spark.io.compression.codec` specifies which codec to use.

---

### Question 40
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply adaptive query execution features

Which AQE feature combines small partitions after shuffles?

A. Dynamic join selection  
B. Dynamic coalescing  
C. Dynamic partition pruning  
D. Dynamic broadcasting

**Correct Answer:** B  
**Explanation:** Dynamic coalescing in AQE automatically combines small partitions after shuffle operations to improve performance.

---

### Question 41
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize resource utilization monitoring

Which metric indicates inefficient resource utilization?

A. High CPU usage  
B. Low task completion rate  
C. Many idle executors  
D. High memory usage

**Correct Answer:** C  
**Explanation:** Many idle executors indicate inefficient resource utilization, suggesting over-allocation or workload imbalance.

---

### Question 42
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure speculation settings

When should task speculation be enabled?

A. In homogeneous clusters  
B. In heterogeneous clusters with varying performance  
C. Only for batch processing  
D. Never, it wastes resources

**Correct Answer:** B  
**Explanation:** Task speculation helps in heterogeneous clusters where some nodes might be slower, by running backup tasks.

---

### Question 43
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply memory-efficient algorithms

Which operation is most memory-efficient for large datasets?

A. `collect()`  
B. `take(1000)`  
C. `foreach()`  
D. `count()`

**Correct Answer:** C  
**Explanation:** `foreach()` processes data without collecting results to the driver, making it memory-efficient for large datasets.

---

### Question 44
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize disk I/O performance

Which technique reduces disk I/O overhead?

A. Using SSD storage  
B. Enabling data compression  
C. Columnar storage formats  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques reduce I/O overhead: SSDs are faster, compression reduces data size, and columnar formats enable efficient reads.

---

### Question 45
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure cluster mode optimizations

Which deployment mode typically provides better resource utilization?

A. Client mode  
B. Cluster mode  
C. Local mode  
D. All are equivalent

**Correct Answer:** B  
**Explanation:** Cluster mode typically provides better resource utilization as the driver runs on the cluster, reducing network overhead.

---

### Question 46
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply query optimization techniques

Which technique helps optimize complex queries?

A. Breaking queries into smaller parts  
B. Using appropriate join orders  
C. Enabling cost-based optimization  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques help: breaking queries reduces complexity, join order affects performance, and CBO makes optimal decisions.

---

### Question 47
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize aggregation performance

Which aggregation strategy is most efficient for high-cardinality grouping?

A. Hash aggregation  
B. Sort-based aggregation  
C. Tree aggregation  
D. Map-side aggregation

**Correct Answer:** A  
**Explanation:** Hash aggregation is typically more efficient for high-cardinality grouping as it doesn't require sorting.

---

### Question 48
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure off-heap memory

What is the benefit of using off-heap memory?

A. Reduced GC pressure  
B. Better memory utilization  
C. Fault tolerance  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Off-heap memory reduces GC pressure and often provides better memory utilization patterns for certain workloads.

---

### Question 49
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply workload-specific optimizations

Which optimization is most important for iterative algorithms?

A. Caching intermediate results  
B. Increasing partition count  
C. Using broadcast variables  
D. Enabling checkpointing

**Correct Answer:** A  
**Explanation:** Caching intermediate results prevents recomputation in iterative algorithms, providing significant performance improvements.

---

### Question 50
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize network performance

Which technique reduces network overhead in Spark jobs?

A. Data locality optimization  
B. Broadcast variables for lookup tables  
C. Efficient serialization  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques reduce network overhead: locality reduces data movement, broadcasting avoids shuffles, and efficient serialization reduces transfer sizes.

---

### Question 51
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure task parallelism

What determines the maximum parallelism in a Spark job?

A. Number of executors  
B. Total number of cores  
C. Number of partitions  
D. Both B and C (minimum of the two)

**Correct Answer:** D  
**Explanation:** Maximum parallelism is limited by both the total cores available and the number of partitions (whichever is smaller).

---

### Question 52
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply statistics-based optimizations

How do table statistics improve query performance?

A. Enable cost-based optimization  
B. Help choose optimal join strategies  
C. Enable partition pruning  
D. All of the above

**Correct Answer:** D  
**Explanation:** Statistics enable CBO, help choose join strategies, and can improve partition pruning decisions.

---

### Question 53
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize driver program performance

Which operation should be avoided in the driver program?

A. Creating SparkContext  
B. Collecting large datasets  
C. Defining transformations  
D. Configuring Spark settings

**Correct Answer:** B  
**Explanation:** Collecting large datasets to the driver can cause memory issues and should be avoided. Use sampling or aggregation instead.

---

### Question 54
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure resource scaling

When does dynamic allocation add more executors?

A. When pending tasks exist  
B. When CPU usage is high  
C. When memory usage is high  
D. At fixed time intervals

**Correct Answer:** A  
**Explanation:** Dynamic allocation adds executors based on pending task backlog, not just resource utilization metrics.

---

### Question 55
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply memory tuning strategies

Which memory pool is used for shuffle operations?

A. Storage memory  
B. Execution memory  
C. Off-heap memory  
D. System memory

**Correct Answer:** B  
**Explanation:** Execution memory is used for shuffle operations, joins, sorts, and aggregations, separate from storage memory used for caching.

---

### Question 56
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize data loading performance

Which technique improves performance when reading many small files?

A. Increasing executor memory  
B. Using `coalesce()` or `repartition()` after reading  
C. Reading files in parallel  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both techniques help: reading in parallel utilizes cluster resources, and coalescing/repartitioning optimizes processing of many small partitions.

---

### Question 57
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure executor placement

Which factor affects executor placement in a cluster?

A. Data locality preferences  
B. Available resources on nodes  
C. Rack topology  
D. All of the above

**Correct Answer:** D  
**Explanation:** Executor placement considers data locality, resource availability, and network topology to optimize performance.

---

### Question 58
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply persistent storage optimizations

When should you unpersist cached DataFrames?

A. Never, caching is always beneficial  
B. When they're no longer needed  
C. After every action  
D. Only when memory is full

**Correct Answer:** B  
**Explanation:** Unpersisting cached DataFrames when they're no longer needed frees up memory for other operations.

---

### Question 59
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize join performance tuning

Which join algorithm is most efficient for joining very large datasets?

A. Broadcast join  
B. Shuffle hash join  
C. Sort-merge join  
D. Cartesian join

**Correct Answer:** C  
**Explanation:** Sort-merge join is typically most efficient for large-large joins as it sorts data once and then merges, avoiding the need to build hash tables.

---

### Question 60
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure serialization optimization

Which serialization setting improves performance for UDFs?

A. `spark.serializer = org.apache.spark.serializer.KryoSerializer`  
B. `spark.kryo.registrationRequired = true`  
C. Registering classes with Kryo  
D. All of the above

**Correct Answer:** D  
**Explanation:** All settings improve serialization performance: using Kryo, requiring registration for optimization, and pre-registering frequently used classes.

---

### Question 61
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply resource monitoring best practices

Which metric indicates a well-balanced workload?

A. Equal task durations across executors  
B. High CPU utilization  
C. Low GC time  
D. All of the above

**Correct Answer:** D  
**Explanation:** A balanced workload shows equal task durations, high CPU utilization, and low GC overhead, indicating efficient resource use.

---

### Question 62
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Optimize cluster resource allocation

What's the typical recommendation for executor size?

A. Few large executors  
B. Many small executors  
C. Medium-sized executors (2-5 cores, 4-20 GB memory)  
D. Size doesn't matter

**Correct Answer:** C  
**Explanation:** Medium-sized executors provide good balance of parallelism and resource efficiency, avoiding issues with very large or very small executors.

---

### Question 63
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure fault tolerance optimizations

Which setting improves fault tolerance without significant performance impact?

A. Frequent checkpointing  
B. Using external shuffle service  
C. Increasing replication factor  
D. Disabling speculation

**Correct Answer:** B  
**Explanation:** External shuffle service improves fault tolerance by preserving shuffle files even if executors fail, without significant performance overhead.

---

### Question 64
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Apply advanced optimization techniques

Which advanced technique can optimize joins with skewed data?

A. Salting join keys  
B. Using range partitioning  
C. Broadcast join with filtering  
D. All of the above

**Correct Answer:** D  
**Explanation:** All techniques help with skewed data: salting distributes load, range partitioning can isolate skewed keys, and selective broadcasting can handle partial skew.

---

### Question 65
**Section:** Troubleshooting and Tuning Apache Spark Applications  
**Objective:** Implement comprehensive performance strategies

Which approach provides the most comprehensive performance optimization?

A. Focus only on memory tuning  
B. Combine multiple optimization techniques based on workload analysis  
C. Use default settings  
D. Maximize resource allocation

**Correct Answer:** B  
**Explanation:** Comprehensive performance optimization requires analyzing the specific workload and applying multiple appropriate techniques rather than using a one-size-fits-all approach.

---

## Answer Key Summary

1. B  2. B  3. B  4. B  5. B  6. B  7. B  8. C  9. D  10. A
11. C  12. A  13. D  14. B  15. B  16. C  17. A  18. A  19. C  20. D
21. A  22. A  23. B  24. D  25. D  26. B  27. D  28. B  29. B  30. B
31. B  32. D  33. B  34. B  35. C  36. A  37. B  38. D  39. C  40. B
41. C  42. B  43. C  44. D  45. B  46. D  47. A  48. D  49. A  50. D
51. D  52. D  53. B  54. A  55. B  56. D  57. D  58. B  59. C  60. D
61. D  62. C  63. B  64. D  65. B

## Score Interpretation
- **90-100% (59-65 correct):** Excellent! Performance optimization expert
- **80-89% (52-58 correct):** Good preparation, review advanced tuning techniques
- **70-79% (46-51 correct):** Fair understanding, focus on resource management and caching
- **Below 70% (<46 correct):** More study needed on performance fundamentals

## Next Steps
- Review explanations for incorrect answers
- Practice with Spark UI analysis and performance monitoring
- Study advanced optimization techniques for specific workload patterns
- Focus on production performance tuning scenarios