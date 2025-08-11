# Apache Spark Developer Associate - Practice Exam 03
## Focus: RDD Operations and Low-Level APIs
**Difficulty Level:** Intermediate to Advanced  
**Time Limit:** 90 minutes  
**Questions:** 60

---

### Question 1
**Section:** Apache Spark Architecture and Components  
**Objective:** Understand RDD operations and transformations

What is the fundamental difference between RDD transformations and actions?

A. Transformations are executed immediately, actions are lazy  
B. Transformations are lazy, actions trigger execution  
C. Transformations modify data, actions just read it  
D. There is no difference

**Correct Answer:** B  
**Explanation:** Transformations (map, filter, etc.) are lazy and build a DAG. Actions (collect, save, etc.) trigger the actual computation.

---

### Question 2
**Section:** Apache Spark Architecture and Components  
**Objective:** Identify the features of RDD operations

Which RDD transformation performs a one-to-many mapping?

A. `map()`  
B. `filter()`  
C. `flatMap()`  
D. `reduce()`

**Correct Answer:** C  
**Explanation:** `flatMap()` can produce zero, one, or multiple output elements for each input element, unlike `map()` which is one-to-one.

---

### Question 3
**Section:** Apache Spark Architecture and Components  
**Objective:** Describe RDD lineage and fault tolerance

What information does RDD lineage contain?

A. The sequence of transformations that created the RDD  
B. The partitioning information  
C. The dependencies between RDDs  
D. All of the above

**Correct Answer:** D  
**Explanation:** RDD lineage tracks transformations, partitioning, and dependencies, enabling fault recovery by recomputing lost partitions.

---

### Question 4
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with RDD operations

Given an RDD of numbers, which code correctly calculates the sum?

```python
numbers_rdd = sc.parallelize([1, 2, 3, 4, 5])
```

A. `numbers_rdd.sum()`  
B. `numbers_rdd.reduce(lambda a, b: a + b)`  
C. `numbers_rdd.fold(0, lambda a, b: a + b)`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** `reduce()` and `fold()` can both sum elements. RDDs don't have a `sum()` method (that's for DataFrames).

---

### Question 5
**Section:** Apache Spark Architecture and Components  
**Objective:** Configure RDD partitioning

How do you create an RDD with a specific number of partitions?

A. `sc.parallelize(data, numSlices=4)`  
B. `sc.parallelize(data).repartition(4)`  
C. `sc.parallelize(data, 4)`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three approaches create RDDs with specific partition counts, though with different methods.

---

### Question 6
**Section:** Apache Spark Architecture and Components  
**Objective:** Understand RDD persistence and caching

What happens when you call `cache()` on an RDD?

A. Data is immediately stored in memory  
B. The RDD is marked for caching on first action  
C. Data is written to disk  
D. Nothing happens until an action is called

**Correct Answer:** B  
**Explanation:** `cache()` marks the RDD for caching but doesn't store data until the first action triggers computation.

---

### Question 7
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD key-value operations

Which operation is used to group elements by key in a pair RDD?

A. `groupBy()`  
B. `groupByKey()`  
C. `groupByValues()`  
D. `partitionBy()`

**Correct Answer:** B  
**Explanation:** `groupByKey()` groups values by key in pair RDDs (RDD[(K, V)] → RDD[(K, Iterable[V])]).

---

### Question 8
**Section:** Apache Spark Architecture and Components  
**Objective:** Understand shuffle operations

Which RDD operation typically causes a shuffle?

A. `map()`  
B. `filter()`  
C. `reduceByKey()`  
D. `mapPartitions()`

**Correct Answer:** C  
**Explanation:** `reduceByKey()` requires shuffling data to group all values with the same key together across partitions.

---

### Question 9
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD transformations and actions

What's the difference between `reduce()` and `fold()` operations?

A. `reduce()` requires an identity element, `fold()` doesn't  
B. `fold()` requires an identity element, `reduce()` doesn't  
C. They are identical operations  
D. `fold()` works only on numeric data

**Correct Answer:** B  
**Explanation:** `fold()` takes an identity/zero value as the first parameter, while `reduce()` doesn't require one.

---

### Question 10
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD creation and data sources

Which method creates an RDD from a text file?

A. `sc.textFile("path")`  
B. `sc.readTextFile("path")`  
C. `sc.loadFile("path")`  
D. `sc.fromFile("path")`

**Correct Answer:** A  
**Explanation:** `sc.textFile()` is the standard method to create an RDD from text files in HDFS or local filesystem.

---

### Question 11
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD pair operations

How do you perform an inner join on two pair RDDs?

```python
rdd1 = sc.parallelize([(1, "a"), (2, "b"), (3, "c")])
rdd2 = sc.parallelize([(1, "x"), (2, "y"), (4, "z")])
```

A. `rdd1.join(rdd2)`  
B. `rdd1.innerJoin(rdd2)`  
C. `rdd1.merge(rdd2)`  
D. `rdd1.combine(rdd2)`

**Correct Answer:** A  
**Explanation:** The `join()` method performs an inner join by default on pair RDDs, matching on keys.

---

### Question 12
**Section:** Apache Spark Architecture and Components  
**Objective:** Understand RDD operations performance

Why is `reduceByKey()` preferred over `groupByKey()` followed by reduce?

A. `reduceByKey()` performs local reduction before shuffling  
B. `groupByKey()` shuffles all values across the network  
C. `reduceByKey()` is more memory efficient  
D. All of the above

**Correct Answer:** D  
**Explanation:** `reduceByKey()` performs local pre-aggregation, reducing network traffic and memory usage compared to `groupByKey()`.

---

### Question 13
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD transformations

What does the `mapPartitions()` transformation do?

A. Maps each element individually  
B. Maps each partition as a whole  
C. Filters partitions based on criteria  
D. Repartitions the RDD

**Correct Answer:** B  
**Explanation:** `mapPartitions()` applies a function to each partition's iterator, allowing batch processing of partition data.

---

### Question 14
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD persistence storage levels

Which storage level keeps RDD data in memory and falls back to disk?

A. `MEMORY_ONLY`  
B. `MEMORY_AND_DISK`  
C. `DISK_ONLY`  
D. `MEMORY_ONLY_SER`

**Correct Answer:** B  
**Explanation:** `MEMORY_AND_DISK` storage level caches in memory first, spilling to disk when memory is insufficient.

---

### Question 15
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD actions and collections

Which action returns the first n elements of an RDD?

A. `first(n)`  
B. `take(n)`  
C. `head(n)`  
D. `limit(n)`

**Correct Answer:** B  
**Explanation:** `take(n)` returns the first n elements as a Python list. `first()` returns only the first element.

---

### Question 16
**Section:** Apache Spark Architecture and Components  
**Objective:** Custom partitioning

How do you implement custom partitioning for an RDD?

A. Create a custom Partitioner class  
B. Use `partitionBy()` with a custom function  
C. Override the `getPartition()` method  
D. Both A and B

**Correct Answer:** D  
**Explanation:** You can create a custom Partitioner class or use `partitionBy()` with a partitioning function.

---

### Question 17
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD set operations

Which operation finds elements in RDD1 but not in RDD2?

A. `rdd1.subtract(rdd2)`  
B. `rdd1.difference(rdd2)`  
C. `rdd1.except(rdd2)`  
D. `rdd1.minus(rdd2)`

**Correct Answer:** A  
**Explanation:** `subtract()` returns elements in the first RDD that are not in the second RDD.

---

### Question 18
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD narrow vs wide transformations

Which of these is a narrow transformation?

A. `map()`  
B. `filter()`  
C. `union()`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All are narrow transformations because each input partition contributes to only one output partition.

---

### Question 19
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD aggregations

How do you implement a custom aggregation using `aggregate()`?

```python
# Calculate sum and count in one pass
```

A. `rdd.aggregate((0, 0), lambda acc, x: (acc[0] + x, acc[1] + 1), lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]))`  
B. `rdd.reduce(lambda a, b: (a[0] + b, a[1] + 1))`  
C. `rdd.fold((0, 0), lambda acc, x: (acc[0] + x, acc[1] + 1))`  
D. Only A is correct

**Correct Answer:** D  
**Explanation:** `aggregate()` requires zero value, sequence operation (within partition), and combination operation (across partitions).

---

### Question 20
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD checkpointing

What is the purpose of RDD checkpointing?

A. Save computation results to disk  
B. Break long lineage chains  
C. Enable faster recovery from failures  
D. All of the above

**Correct Answer:** D  
**Explanation:** Checkpointing saves RDD to disk, truncates lineage, and provides faster recovery than recomputing from the beginning.

---

### Question 21
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD sampling

How do you take a random sample from an RDD?

A. `rdd.sample(withReplacement=False, fraction=0.1, seed=42)`  
B. `rdd.takeSample(withReplacement=False, num=100, seed=42)`  
C. `rdd.randomSample(0.1)`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `sample()` returns a sampled RDD with given fraction, `takeSample()` returns exact number of samples to driver.

---

### Question 22
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD transformations vs actions

Which operation is an action?

A. `map()`  
B. `filter()`  
C. `foreach()`  
D. `flatMap()`

**Correct Answer:** C  
**Explanation:** `foreach()` is an action that applies a function to each element but doesn't return a value, triggering computation.

---

### Question 23
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD key-value operations

What does `combineByKey()` do?

A. Combines values with the same key using custom functions  
B. Combines multiple RDDs by key  
C. Combines partitions by key  
D. Combines keys into a single value

**Correct Answer:** A  
**Explanation:** `combineByKey()` is the most general aggregation function, allowing custom create, merge, and combine operations.

---

### Question 24
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD partitioning strategies

When should you use hash partitioning?

A. When keys are evenly distributed  
B. When you need range-based queries  
C. When doing multiple operations by key  
D. Both A and C

**Correct Answer:** D  
**Explanation:** Hash partitioning works well with evenly distributed keys and benefits operations that process data by key.

---

### Question 25
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD operations efficiency

Which approach is more efficient for word count?

A. `rdd.map(lambda line: line.split()).flatMap(lambda words: [(w, 1) for w in words]).reduceByKey(lambda a, b: a + b)`  
B. `rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)`  
C. `rdd.flatMap(lambda line: [(w, 1) for w in line.split()]).reduceByKey(lambda a, b: a + b)`  
D. All are equally efficient

**Correct Answer:** B  
**Explanation:** Option B is most efficient: split lines, create pairs, then reduce. It minimizes intermediate collections.

---

### Question 26
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD persistence patterns

When should you persist an RDD?

A. When the RDD is used multiple times  
B. When the RDD is expensive to compute  
C. When the RDD is small enough to fit in memory  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Persist RDDs that are reused or expensive to recompute. Size considerations depend on available memory.

---

### Question 27
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD creation patterns

How do you create an RDD from a Python collection with custom parallelism?

A. `sc.parallelize(collection, numSlices=8)`  
B. `sc.makeRDD(collection, 8)`  
C. `sc.distribute(collection, partitions=8)`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `parallelize()` and `makeRDD()` (alias) can create RDDs with specified partition counts.

---

### Question 28
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD DAG and execution

What triggers the creation of a DAG (Directed Acyclic Graph)?

A. Creating an RDD  
B. Applying transformations  
C. Calling an action  
D. Both A and B

**Correct Answer:** D  
**Explanation:** The DAG is built as RDDs are created and transformations applied, representing the computation lineage.

---

### Question 29
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD cogroup operations

What does `cogroup()` return when applied to two pair RDDs?

A. `RDD[(K, (Iterable[V1], Iterable[V2]))]`  
B. `RDD[(K, V1, V2)]`  
C. `RDD[(K, List[V1, V2])]`  
D. `RDD[K, (V1, V2)]`

**Correct Answer:** A  
**Explanation:** `cogroup()` groups values from both RDDs by key, returning iterables of values for each key from both RDDs.

---

### Question 30
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD broadcast and accumulator usage

How do you use a broadcast variable in RDD operations?

```python
broadcast_var = sc.broadcast(large_dict)
```

A. `rdd.map(lambda x: broadcast_var[x])`  
B. `rdd.map(lambda x: broadcast_var.value[x])`  
C. `rdd.map(lambda x: broadcast_var.get(x))`  
D. Both A and B

**Correct Answer:** B  
**Explanation:** Access broadcast variable content using `.value` property to get the actual broadcasted object.

---

### Question 31
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD advanced transformations

What's the difference between `map()` and `mapPartitions()`?

A. `map()` processes individual elements, `mapPartitions()` processes entire partitions  
B. `mapPartitions()` is always more memory efficient  
C. `map()` can change the number of elements, `mapPartitions()` cannot  
D. No significant difference

**Correct Answer:** A  
**Explanation:** `map()` applies function element by element, `mapPartitions()` processes partition iterators, enabling batch operations.

---

### Question 32
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD fault tolerance mechanisms

How does Spark recover from executor failure?

A. Restart the entire job  
B. Recompute lost RDD partitions using lineage  
C. Restore from checkpoint  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Spark can recover by recomputing lost partitions using lineage information or restoring from checkpoints if available.

---

### Question 33
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD sorting operations

How do you sort an RDD by key?

```python
pair_rdd = sc.parallelize([(3, "c"), (1, "a"), (2, "b")])
```

A. `pair_rdd.sortByKey()`  
B. `pair_rdd.sort()`  
C. `pair_rdd.orderBy(lambda x: x[0])`  
D. `pair_rdd.sortBy(lambda x: x[0])`

**Correct Answer:** A  
**Explanation:** `sortByKey()` is the standard method for sorting pair RDDs by their keys.

---

### Question 34
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD memory management

What happens when an RDD doesn't fit in memory during caching?

A. Spark throws an out-of-memory error  
B. Spark spills to disk based on storage level  
C. Spark evicts least recently used partitions  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Depending on storage level, Spark may spill to disk or evict partitions using LRU (Least Recently Used) strategy.

---

### Question 35
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD zip operations

What does `zip()` do with two RDDs?

A. Combines RDDs element by element  
B. Creates pairs from corresponding elements  
C. Requires RDDs to have same number of partitions and elements  
D. All of the above

**Correct Answer:** D  
**Explanation:** `zip()` pairs up elements from two RDDs by position, requiring identical partition and element counts.

---

### Question 36
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD lineage optimization

How does Spark optimize RDD lineage?

A. Combines consecutive map operations  
B. Pushes filters as early as possible  
C. Eliminates unused columns  
D. These optimizations apply to DataFrames, not RDDs

**Correct Answer:** D  
**Explanation:** RDDs don't have automatic query optimization. These optimizations are performed by the Catalyst optimizer for DataFrames.

---

### Question 37
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD custom functions

How do you implement a custom function that works on RDD partitions?

```python
def process_partition(iterator):
    # Process all elements in partition
    result = []
    for element in iterator:
        # Custom processing
        result.append(transform(element))
    return iter(result)
```

A. `rdd.map(process_partition)`  
B. `rdd.mapPartitions(process_partition)`  
C. `rdd.foreachPartition(process_partition)`  
D. `rdd.transform(process_partition)`

**Correct Answer:** B  
**Explanation:** `mapPartitions()` applies a function to each partition's iterator, perfect for custom partition-level processing.

---

### Question 38
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD serialization

Which serialization format is recommended for RDD operations?

A. Java serialization  
B. Kryo serialization  
C. JSON serialization  
D. Avro serialization

**Correct Answer:** B  
**Explanation:** Kryo serialization is faster and more compact than Java serialization for RDD operations.

---

### Question 39
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD statistics

How do you calculate basic statistics for an RDD of numbers?

A. `rdd.stats()`  
B. `rdd.describe()`  
C. Manual calculation using `mean()`, `stdev()`, etc.  
D. Convert to DataFrame first

**Correct Answer:** C  
**Explanation:** RDDs don't have built-in statistics methods. You need to calculate manually or convert to DataFrame for `describe()`.

---

### Question 40
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD glom operation

What does the `glom()` transformation do?

A. Flattens nested structures  
B. Groups elements by key  
C. Converts each partition into a list  
D. Removes duplicates

**Correct Answer:** C  
**Explanation:** `glom()` transforms each partition into a single list element, useful for debugging partition contents.

---

### Question 41
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD pipe operations

What is the purpose of the `pipe()` operation?

A. Connect RDDs together  
B. Pass RDD data through external scripts  
C. Create data pipelines  
D. Stream data to output

**Correct Answer:** B  
**Explanation:** `pipe()` allows passing RDD data through external command-line programs or scripts.

---

### Question 42
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD repartitioning strategies

When should you use `coalesce()` instead of `repartition()`?

A. When reducing the number of partitions  
B. When you want to avoid shuffling  
C. When working with small datasets  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `coalesce()` is preferred when reducing partitions as it minimizes shuffling, while `repartition()` always shuffles.

---

### Question 43
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD intersection operations

How do you find common elements between two RDDs?

A. `rdd1.intersection(rdd2)`  
B. `rdd1.intersect(rdd2)`  
C. `rdd1.common(rdd2)`  
D. `rdd1.join(rdd2)`

**Correct Answer:** A  
**Explanation:** `intersection()` returns elements that exist in both RDDs, removing duplicates.

---

### Question 44
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD lazy evaluation benefits

Why is lazy evaluation beneficial in Spark?

A. Enables query optimization  
B. Avoids unnecessary computations  
C. Allows pipeline fusion  
D. All of the above

**Correct Answer:** D  
**Explanation:** Lazy evaluation enables optimization, avoids computing unused results, and allows combining transformations.

---

### Question 45
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD cartesian product

When might you use the `cartesian()` operation?

A. For cross-joins between datasets  
B. When you need all possible combinations  
C. For similarity calculations  
D. All of the above, but use carefully due to size

**Correct Answer:** D  
**Explanation:** `cartesian()` creates all combinations (N×M elements), useful for specific algorithms but potentially expensive.

---

### Question 46
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD task scheduling

How does Spark determine task locality?

A. Based on data location in the cluster  
B. Using network topology  
C. Based on previous execution patterns  
D. All of the above

**Correct Answer:** D  
**Explanation:** Spark considers data locality, network topology, and execution history to optimize task placement.

---

### Question 47
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD saveAsTextFile

How do you control the number of output files when saving an RDD?

A. `rdd.coalesce(1).saveAsTextFile("path")`  
B. `rdd.repartition(5).saveAsTextFile("path")`  
C. Use `saveAsTextFile("path", compressionCodec)`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** The number of output files equals the number of partitions, so `coalesce()` or `repartition()` controls this.

---

### Question 48
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD dependency types

What's the difference between narrow and wide dependencies?

A. Narrow: child partition depends on few parent partitions; Wide: depends on many  
B. Wide dependencies require shuffling, narrow don't  
C. Narrow dependencies enable better fault tolerance  
D. All of the above

**Correct Answer:** D  
**Explanation:** Narrow dependencies have localized computation and better fault tolerance, while wide dependencies require shuffling.

---

### Question 49
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD tree operations

What does `treeReduce()` do differently from `reduce()`?

A. Uses a tree structure for reduction  
B. More efficient for large datasets  
C. Reduces depth of computation tree  
D. All of the above

**Correct Answer:** D  
**Explanation:** `treeReduce()` uses a tree-based approach, reducing the depth of computation and improving efficiency for large datasets.

---

### Question 50
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD unpersist operations

When should you call `unpersist()` on an RDD?

A. When you no longer need the cached data  
B. To free up memory for other operations  
C. When memory usage is high  
D. All of the above

**Correct Answer:** D  
**Explanation:** `unpersist()` removes RDD from cache, freeing memory when the cached data is no longer needed.

---

### Question 51
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD custom partitioners

How do you implement range partitioning?

A. Create a custom RangePartitioner  
B. Sort the RDD and use hash partitioning  
C. Use `partitionBy()` with range function  
D. Range partitioning is not supported for RDDs

**Correct Answer:** A  
**Explanation:** RangePartitioner distributes data across partitions based on key ranges, useful for ordered data.

---

### Question 52
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD accumulators

What are the constraints when using accumulators in RDD operations?

A. Accumulators should only be used in actions  
B. Functions using accumulators should be commutative and associative  
C. Accumulators are only updated once per partition  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Accumulators should be used in actions for reliability, and the functions must be commutative and associative.

---

### Question 53
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD mapPartitionsWithIndex

What additional information does `mapPartitionsWithIndex()` provide?

A. Partition index number  
B. Number of elements in partition  
C. Partition location  
D. All of the above

**Correct Answer:** A  
**Explanation:** `mapPartitionsWithIndex()` provides the partition index as an additional parameter to the processing function.

---

### Question 54
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD storage levels

Which storage level provides the best performance for iterative algorithms?

A. `MEMORY_ONLY`  
B. `MEMORY_AND_DISK`  
C. `MEMORY_ONLY_SER`  
D. It depends on data size and available memory

**Correct Answer:** D  
**Explanation:** The best storage level depends on data size, available memory, and CPU vs memory trade-offs.

---

### Question 55
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD keyBy transformation

What does the `keyBy()` transformation do?

A. Sorts RDD elements by key  
B. Creates a pair RDD with computed keys  
C. Groups elements by key  
D. Filters elements by key

**Correct Answer:** B  
**Explanation:** `keyBy(f)` transforms `RDD[T]` to `RDD[(K, T)]` by applying function `f` to compute keys.

---

### Question 56
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD checkpoint directory

Where should you set the checkpoint directory?

A. Local filesystem  
B. HDFS or other reliable storage  
C. Memory  
D. Any location is fine

**Correct Answer:** B  
**Explanation:** Checkpoint directory should be in reliable, distributed storage like HDFS to ensure fault tolerance.

---

### Question 57
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD collectAsMap

What does `collectAsMap()` do for pair RDDs?

A. Collects as a Python dictionary  
B. Removes duplicate keys  
C. Only works if keys are unique  
D. All of the above

**Correct Answer:** D  
**Explanation:** `collectAsMap()` returns a dictionary, assumes unique keys, and will overwrite values for duplicate keys.

---

### Question 58
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD partitioning benefits

Why is proper partitioning important for RDD performance?

A. Minimizes data shuffling  
B. Enables better locality  
C. Improves parallelism  
D. All of the above

**Correct Answer:** D  
**Explanation:** Good partitioning reduces shuffles, improves data locality, and enables better parallel processing.

---

### Question 59
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** RDD lookup operation

What does the `lookup()` operation return?

A. All values for a given key  
B. First value for a given key  
C. Boolean indicating if key exists  
D. Key-value pair

**Correct Answer:** A  
**Explanation:** `lookup(key)` returns a list of all values associated with the specified key in a pair RDD.

---

### Question 60
**Section:** Apache Spark Architecture and Components  
**Objective:** RDD vs DataFrame performance

When might you choose RDDs over DataFrames?

A. When working with unstructured data  
B. When you need low-level control  
C. When using complex data types not supported by DataFrames  
D. All of the above

**Correct Answer:** D  
**Explanation:** RDDs are preferred for unstructured data, low-level operations, and complex data types that DataFrames don't handle well.

---

## Answer Key Summary

1. B  2. C  3. D  4. D  5. D  6. B  7. B  8. C  9. B  10. A
11. A  12. D  13. B  14. B  15. B  16. D  17. A  18. D  19. D  20. D
21. D  22. C  23. A  24. D  25. B  26. D  27. D  28. D  29. A  30. B
31. A  32. D  33. A  34. D  35. D  36. D  37. B  38. B  39. C  40. C
41. B  42. D  43. A  44. D  45. D  46. D  47. D  48. D  49. D  50. D
51. A  52. D  53. A  54. D  55. B  56. B  57. D  58. D  59. A  60. D

## Score Interpretation
- **90-100% (54-60 correct):** Excellent! RDD mastery achieved
- **80-89% (48-53 correct):** Good understanding of RDD operations
- **70-79% (42-47 correct):** Fair grasp, review key concepts
- **Below 70% (<42 correct):** Focus on RDD fundamentals

## Focus Areas for Improvement
- **RDD Transformations vs Actions:** Master the distinction and when each is executed
- **Partitioning Strategies:** Understand when and how to optimize data partitioning
- **Key-Value Operations:** Practice pair RDD operations like reduceByKey, groupByKey, join
- **Performance Optimization:** Learn when to cache, checkpoint, and choose storage levels
- **Advanced Operations:** Study mapPartitions, aggregate, combineByKey for complex scenarios