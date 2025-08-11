# Apache Spark Developer Associate - Practice Exam 02
## Focus: DataFrame Operations and Data Manipulation
**Difficulty Level:** Intermediate  
**Time Limit:** 90 minutes  
**Questions:** 65

---

### Question 1
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Given a DataFrame with nested JSON data, which function is used to extract nested fields?

A. `col("data.field")`  
B. `getField(col("data"), "field")`  
C. `col("data").getField("field")`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** Both `col("data.field")` and `col("data").getField("field")` can access nested fields in structured data.

---

### Question 2
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

You have a DataFrame with duplicate records. You want to keep only the most recent record for each customer_id based on timestamp. Which approach is correct?

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc
```

A. `df.dropDuplicates(["customer_id"])`  
B. `df.groupBy("customer_id").agg(max("timestamp"))`  
C. `df.withColumn("rn", row_number().over(Window.partitionBy("customer_id").orderBy(desc("timestamp")))).filter(col("rn") == 1).drop("rn")`  
D. `df.distinct()`

**Correct Answer:** C  
**Explanation:** Using window functions with `row_number()` allows you to keep the most recent record per group, which `dropDuplicates()` cannot do based on ordering.

---

### Question 3
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

Which join type returns all records from both DataFrames, with null values where there's no match?

A. `inner`  
B. `left_outer`  
C. `right_outer`  
D. `full_outer`

**Correct Answer:** D  
**Explanation:** Full outer join returns all records from both DataFrames, filling with nulls where there's no match on either side.

---

### Question 4
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

What's the correct way to convert a Unix timestamp (in seconds) to a timestamp column?

A. `from_unixtime(col("unix_timestamp"))`  
B. `to_timestamp(col("unix_timestamp"))`  
C. `unix_timestamp_to_date(col("unix_timestamp"))`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** `from_unixtime()` converts Unix timestamp to timestamp format. `to_timestamp()` is used for string-to-timestamp conversion.

---

### Question 5
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which window function calculates a running total?

A. `sum().over(Window.partitionBy("category").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow))`  
B. `sum().over(Window.partitionBy("category").orderBy("date"))`  
C. `cumsum().over(Window.partitionBy("category").orderBy("date"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both expressions create a running total. Option B uses the default frame (unbounded preceding to current row) when an order by is specified.

---

### Question 6
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a new column that concatenates two string columns with a separator?

A. `df.withColumn("full_name", col("first_name") + " " + col("last_name"))`  
B. `df.withColumn("full_name", concat(col("first_name"), lit(" "), col("last_name")))`  
C. `df.withColumn("full_name", concat_ws(" ", col("first_name"), col("last_name")))`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both `concat()` with `lit()` and `concat_ws()` (concat with separator) work correctly. Option A won't work in PySpark.

---

### Question 7
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as filtering

Which filter condition correctly handles null values?

A. `df.filter(col("column") != None)`  
B. `df.filter(col("column").isNotNull())`  
C. `df.filter(col("column") != null)`  
D. `df.filter("column IS NOT NULL")`

**Correct Answer:** B and D  
**Explanation:** `isNotNull()` method and SQL string "IS NOT NULL" correctly handle null comparisons. Regular equality operators don't work with nulls.

---

### Question 8
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the correct way to handle null values in a Python UDF?

```python
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import udf

def safe_divide(x, y):
    if y is None or y == 0:
        return None
    return x / y

safe_divide_udf = udf(safe_divide, IntegerType())
```

A. The UDF as written handles nulls correctly  
B. Python UDFs automatically handle nulls  
C. You need to use `@udf` decorator  
D. UDFs cannot return None

**Correct Answer:** A  
**Explanation:** The UDF correctly checks for None values and returns None when appropriate. Python UDFs need explicit null handling.

---

### Question 9
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you pivot a DataFrame from long to wide format?

```python
# Sample data: sales data with columns: region, quarter, amount
```

A. `df.pivot("quarter").sum("amount")`  
B. `df.groupBy("region").pivot("quarter").sum("amount")`  
C. `df.pivot("region", "quarter", "amount")`  
D. `df.transpose("quarter", "amount")`

**Correct Answer:** B  
**Explanation:** Pivoting requires grouping by the non-pivot columns, then pivoting on the pivot column, and aggregating the values.

---

### Question 10
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data validation operations on DataFrames

Which approach efficiently counts null values in all columns?

A. `df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])`  
B. `df.select([sum(col(c).isNull().cast("integer")).alias(c + "_nulls") for c in df.columns])`  
C. `df.agg(*[count(when(col(c).isNull(), c)).alias(c) for c in df.columns])`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three approaches count null values across columns, with slight differences in output format and performance characteristics.

---

### Question 11
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you extract the day of week from a date column?

A. `dayofweek(col("date_column"))`  
B. `date_format(col("date_column"), "E")`  
C. `extract("dayofweek", col("date_column"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `dayofweek()` returns 1-7 for Sunday-Saturday, while `date_format()` with "E" returns day names.

---

### Question 12
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

What's the difference between join() and crossJoin()?

A. join() requires a join condition, crossJoin() doesn't  
B. crossJoin() produces a Cartesian product  
C. join() is more efficient than crossJoin()  
D. All of the above

**Correct Answer:** D  
**Explanation:** `crossJoin()` creates a Cartesian product without conditions, while `join()` requires conditions and is typically more efficient.

---

### Question 13
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you handle multiple conditions in when().otherwise()?

A. `when(condition1, value1).when(condition2, value2).otherwise(default_value)`  
B. `when(condition1 & condition2, value).otherwise(default_value)`  
C. `when(condition1 | condition2, value).otherwise(default_value)`  
D. All of the above are valid patterns

**Correct Answer:** D  
**Explanation:** All patterns are valid: chaining for multiple cases, using & for AND conditions, and | for OR conditions.

---

### Question 14
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which function calculates the median value?

A. `median(col("column"))`  
B. `percentile_approx(col("column"), 0.5)`  
C. `expr("percentile_approx(column, 0.5)")`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Spark doesn't have a built-in `median()` function. Use `percentile_approx()` with 0.5 or SQL expression.

---

### Question 15
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you replace null values with a default value?

A. `df.fillna({"column": "default_value"})`  
B. `df.na.fill({"column": "default_value"})`  
C. `df.withColumn("column", coalesce(col("column"), lit("default_value")))`  
D. All of the above

**Correct Answer:** D  
**Explanation:** `fillna()`, `na.fill()`, and `coalesce()` all can replace null values, with different syntax and flexibility.

---

### Question 16
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as conversion between formats

How do you convert a DataFrame column to a list in the driver?

A. `df.select("column").collect()`  
B. `[row["column"] for row in df.select("column").collect()]`  
C. `df.select("column").rdd.map(lambda row: row[0]).collect()`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both list comprehension and RDD mapping can extract column values to a Python list, though B is more readable.

---

### Question 17
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Which function is used to cast a column to a different data type?

A. `col("column").cast("string")`  
B. `cast(col("column"), StringType())`  
C. `col("column").astype("string")`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** Both `cast()` and `astype()` can change column data types, accepting string type names or type objects.

---

### Question 18
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

How do you remove rows where all values are null?

A. `df.dropna(how="all")`  
B. `df.na.drop(how="all")`  
C. `df.filter(~(all column conditions are null))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `dropna(how="all")` and `na.drop(how="all")` remove rows where all values are null.

---

### Question 19
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

When joining DataFrames with the same column names, how do you avoid column name conflicts?

A. Use aliases before joining: `df1.alias("a").join(df2.alias("b"), join_condition)`  
B. Select specific columns after joining  
C. Use column expressions: `df1.join(df2, df1["id"] == df2["id"])`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All approaches help avoid column conflicts: aliases, explicit column selection, and column expressions.

---

### Question 20
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you calculate the difference between two dates in days?

A. `datediff(col("end_date"), col("start_date"))`  
B. `col("end_date") - col("start_date")`  
C. `date_sub(col("end_date"), col("start_date"))`  
D. `days_between(col("start_date"), col("end_date"))`

**Correct Answer:** A  
**Explanation:** `datediff()` calculates the number of days between two dates. Simple subtraction doesn't work with date columns.

---

### Question 21
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate a rolling average over the last 3 rows?

A. `avg().over(Window.orderBy("date").rowsBetween(-2, 0))`  
B. `avg().over(Window.orderBy("date").rangeBetween(-2, 0))`  
C. `mean().over(Window.orderBy("date").rows(3))`  
D. `rolling_avg().over(Window.orderBy("date"))`

**Correct Answer:** A  
**Explanation:** `rowsBetween(-2, 0)` creates a window of the current row and 2 preceding rows for a 3-row rolling window.

---

### Question 22
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a column with row numbers?

A. `df.withColumn("row_num", monotonically_increasing_id())`  
B. `df.withColumn("row_num", row_number().over(Window.orderBy(lit(1))))`  
C. `df.withColumn("row_num", rank().over(Window.orderBy("id")))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `monotonically_increasing_id()` creates unique increasing IDs (not necessarily consecutive), while `row_number()` creates consecutive numbers.

---

### Question 23
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the performance impact of using Python UDFs compared to Scala UDFs?

A. Python UDFs are faster  
B. Scala UDFs are faster due to JVM execution  
C. No significant difference  
D. It depends on the function complexity

**Correct Answer:** B  
**Explanation:** Scala UDFs run in the JVM avoiding serialization overhead, while Python UDFs require data serialization between JVM and Python processes.

---

### Question 24
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as filtering

How do you filter rows based on multiple conditions using different logical operators?

A. `df.filter((col("age") > 18) & (col("country") == "USA"))`  
B. `df.filter((col("age") > 65) | (col("status") == "VIP"))`  
C. `df.filter(~(col("active") == False))`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All examples show valid logical operators: & (AND), | (OR), and ~ (NOT) for complex filtering conditions.

---

### Question 25
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you rename all columns to lowercase?

A. `df.toDF(*[c.lower() for c in df.columns])`  
B. `df.select([col(c).alias(c.lower()) for c in df.columns])`  
C. `df.withColumnsRenamed({c: c.lower() for c in df.columns})`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both approaches work: `toDF()` renames all columns at once, and `select()` with aliases. Option C uses a non-existent method.

---

### Question 26
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data validation operations on DataFrames

How do you check if a DataFrame contains a specific column?

A. `"column_name" in df.columns`  
B. `df.columns.contains("column_name")`  
C. `df.hasColumn("column_name")`  
D. `"column_name" in df.schema.names`

**Correct Answer:** A  
**Explanation:** `df.columns` returns a list of column names, so you can use the `in` operator to check existence.

---

### Question 27
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

What's the difference between union() and join()?

A. union() combines rows vertically, join() combines columns horizontally  
B. union() requires same schema, join() doesn't  
C. union() is faster than join()  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `union()` stacks DataFrames vertically (same schema required), while `join()` combines DataFrames horizontally based on conditions.

---

### Question 28
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you convert a string date to timestamp with a specific format?

A. `to_timestamp(col("date_string"), "yyyy-MM-dd HH:mm:ss")`  
B. `to_date(col("date_string"), "yyyy-MM-dd")`  
C. `date_format(col("date_string"), "yyyy-MM-dd")`  
D. Both A and B for different purposes

**Correct Answer:** D  
**Explanation:** `to_timestamp()` converts to timestamp type with time, `to_date()` converts to date type only.

---

### Question 29
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

Which aggregation function returns the first non-null value?

A. `first(col("column"))`  
B. `coalesce(*[col(c) for c in columns])`  
C. `first(col("column"), ignorenulls=True)`  
D. Both A and C

**Correct Answer:** C  
**Explanation:** `first()` with `ignorenulls=True` returns the first non-null value. Default `first()` might return null if the first value is null.

---

### Question 30
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you add multiple columns at once?

A. `df.withColumn("col1", expr1).withColumn("col2", expr2)`  
B. `df.select("*", expr1.alias("col1"), expr2.alias("col2"))`  
C. `df.withColumns({"col1": expr1, "col2": expr2})`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both chaining `withColumn()` and using `select()` with expressions work. Option C uses a non-existent method.

---

### Question 31
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as sorting

How do you sort by multiple columns with different sort orders?

A. `df.orderBy(asc("col1"), desc("col2"))`  
B. `df.sort(col("col1").asc(), col("col2").desc())`  
C. `df.orderBy("col1", col("col2").desc())`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three approaches correctly sort by multiple columns with different orders.

---

### Question 32
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

How do you register a Python UDF for use in SQL queries?

A. `spark.udf.register("my_udf", python_function, return_type)`  
B. `spark.sql.register("my_udf", python_function)`  
C. `spark.catalog.registerFunction("my_udf", python_function)`  
D. UDFs cannot be used in SQL

**Correct Answer:** A  
**Explanation:** `spark.udf.register()` makes a Python UDF available for use in SQL queries with a given name.

---

### Question 33
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a column that shows the percentage of total?

```python
# Calculate each row's percentage of the sum
```

A. `df.withColumn("percentage", col("amount") / sum("amount") * 100)`  
B. `df.withColumn("percentage", col("amount") / df.agg(sum("amount")).collect()[0][0] * 100)`  
C. `df.withColumn("percentage", col("amount") / sum("amount").over(Window.partitionBy()) * 100)`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Option B collects the sum to driver, Option C uses window function. Option A won't work as it mixes DataFrame and aggregation operations.

---

### Question 34
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

How do you find duplicate records based on specific columns?

A. `df.groupBy("col1", "col2").count().filter(col("count") > 1)`  
B. `df.exceptAll(df.dropDuplicates(["col1", "col2"]))`  
C. `df.withColumn("cnt", count("*").over(Window.partitionBy("col1", "col2"))).filter(col("cnt") > 1)`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All approaches can identify duplicates: groupBy with count, set difference, and window functions.

---

### Question 35
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

What's the difference between inner join and semi join?

A. Semi join returns only columns from the left DataFrame  
B. Semi join returns records from left that have matches in right  
C. Semi join doesn't duplicate rows for multiple matches  
D. All of the above

**Correct Answer:** D  
**Explanation:** Semi join acts like an "exists" filter, returning left DataFrame columns only for rows with matches in right DataFrame.

---

### Question 36
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you get the current timestamp in Spark?

A. `current_timestamp()`  
B. `now()`  
C. `current_date()`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** `current_timestamp()` returns current timestamp. There's no `now()` function, and `current_date()` returns only date without time.

---

### Question 37
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate cumulative sum within groups?

A. `sum().over(Window.partitionBy("group").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow))`  
B. `sum().over(Window.partitionBy("group").orderBy("date"))`  
C. `cumsum().over(Window.partitionBy("group"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both expressions calculate cumulative sum. Option B uses the default frame when orderBy is specified.

---

### Question 38
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a conditional column based on multiple conditions?

A. ```python
when(col("age") < 18, "Minor")
.when(col("age") < 65, "Adult")
.otherwise("Senior")
```  
B. ```python
case(col("age") < 18, "Minor")
.when(col("age") < 65, "Adult")
.else("Senior")
```  
C. ```python
if_else(col("age") < 18, "Minor",
        if_else(col("age") < 65, "Adult", "Senior"))
```  
D. Only A is correct

**Correct Answer:** D  
**Explanation:** Only the `when().when().otherwise()` pattern is correct Spark SQL syntax.

---

### Question 39
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as iterating

How do you iterate over DataFrame rows in the driver?

A. `for row in df.collect(): print(row)`  
B. `df.foreach(lambda row: print(row))`  
C. `df.rdd.foreach(lambda row: print(row))`  
D. Both A and C, but B executes on executors

**Correct Answer:** D  
**Explanation:** `collect()` brings data to driver for iteration. `foreach()` executes actions on executors, not driver.

---

### Question 40
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

How do you perform an anti-join (records in left that don't match right)?

A. `df1.join(df2, join_condition, "anti")`  
B. `df1.join(df2, join_condition, "left_anti")`  
C. `df1.subtract(df2)`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both "anti" and "left_anti" perform anti-joins, returning left records without matches in right.

---

### Question 41
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you flatten an array of structs into separate columns?

A. `df.select(col("array_col.*"))`  
B. `df.select(explode(col("array_col")).alias("exploded")).select("exploded.*")`  
C. `df.withColumn("exploded", explode(col("array_col"))).select("exploded.*")`  
D. Both B and C approach the problem correctly

**Correct Answer:** B  
**Explanation:** You need to explode the array first, then extract the struct fields. Option C won't work with `withColumn`.

---

### Question 42
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data validation operations on DataFrames

How do you check data quality by finding rows with invalid email formats?

A. `df.filter(~col("email").rlike(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"))`  
B. `df.filter(col("email").isNull() | (col("email") == ""))`  
C. `df.filter(~col("email").contains("@"))`  
D. All approaches check different aspects of email validity

**Correct Answer:** D  
**Explanation:** Each filter checks different validation rules: regex pattern, null/empty values, and basic @ symbol presence.

---

### Question 43
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the correct way to create a vectorized UDF (Pandas UDF)?

```python
import pandas as pd
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import IntegerType

@pandas_udf(returnType=IntegerType())
def multiply_by_two(s: pd.Series) -> pd.Series:
    return s * 2
```

A. The code above is correct  
B. Need to specify `functionType=PandasUDFType.SCALAR`  
C. Should use `@udf` decorator instead  
D. Pandas UDFs are not supported

**Correct Answer:** A  
**Explanation:** The pandas_udf decorator with return type is the correct modern syntax for vectorized UDFs.

---

### Question 44
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you truncate a timestamp to the hour?

A. `date_trunc("hour", col("timestamp_col"))`  
B. `trunc(col("timestamp_col"), "hour")`  
C. `hour(col("timestamp_col"))`  
D. `date_format(col("timestamp_col"), "yyyy-MM-dd HH")`

**Correct Answer:** A  
**Explanation:** `date_trunc()` truncates timestamps to specified units. `hour()` extracts only the hour value.

---

### Question 45
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate the standard deviation of a column?

A. `stddev(col("column"))`  
B. `stddev_pop(col("column"))`  
C. `stddev_samp(col("column"))`  
D. All of the above are valid

**Correct Answer:** D  
**Explanation:** `stddev()` defaults to sample standard deviation, while `stddev_pop()` and `stddev_samp()` are explicit versions.

---

### Question 46
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you handle missing values by forward filling within groups?

```python
from pyspark.sql.window import Window
```

A. `df.withColumn("filled", last("value", ignorenulls=True).over(Window.partitionBy("group").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)))`  
B. `df.fillna(method="ffill")`  
C. `df.na.fill(method="forward")`  
D. Forward fill is not supported in Spark

**Correct Answer:** A  
**Explanation:** Forward filling requires window functions with `last()` ignoring nulls. Methods B and C don't exist in Spark (they're pandas methods).

---

### Question 47
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

When should you use broadcast joins?

A. When one DataFrame is small enough to fit in memory  
B. When you want to avoid shuffling the large DataFrame  
C. When the join is performed frequently  
D. All of the above

**Correct Answer:** D  
**Explanation:** Broadcast joins are optimal when one DataFrame is small (< 10MB by default), avoiding shuffle overhead on large DataFrames.

---

### Question 48
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as conversion between formats

How do you convert a DataFrame to JSON format?

A. `df.toJSON()`  
B. `df.toJson()`  
C. `df.write.json("path")`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** `toJSON()` returns an RDD of JSON strings, while `write.json()` writes to files in JSON format.

---

### Question 49
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a map (dictionary) column from key-value pairs?

A. `create_map(col("key1"), col("value1"), col("key2"), col("value2"))`  
B. `map_from_arrays(col("keys"), col("values"))`  
C. `to_map(col("key_value_pairs"))`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `create_map()` creates maps from alternating key-value columns, while `map_from_arrays()` creates maps from key and value arrays.

---

### Question 50
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

How do you keep the first occurrence of duplicates based on a timestamp?

A. `df.dropDuplicates(["id"]).orderBy("timestamp")`  
B. `df.orderBy("timestamp").dropDuplicates(["id"])`  
C. `df.withColumn("rn", row_number().over(Window.partitionBy("id").orderBy("timestamp"))).filter(col("rn") == 1)`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Option B orders first then drops duplicates (keeping first by timestamp). Option C uses window functions for the same result.

---

### Question 51
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you calculate age from birth date?

A. `floor(datediff(current_date(), col("birth_date")) / 365.25)`  
B. `year(current_date()) - year(col("birth_date"))`  
C. `months_between(current_date(), col("birth_date")) / 12`  
D. Option A is most accurate

**Correct Answer:** D  
**Explanation:** Option A accounts for leap years (365.25), making it most accurate. Option B ignores month/day, Option C is also approximate.

---

### Question 52
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

How do you union multiple DataFrames with the same schema?

A. `df1.union(df2).union(df3)`  
B. `df1.unionAll(df2).unionAll(df3)`  
C. `reduce(lambda x, y: x.union(y), [df1, df2, df3])`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All approaches work: chaining unions, using unionAll (deprecated but equivalent), and using reduce function.

---

### Question 53
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate percentiles for a column?

A. `df.select(expr("percentile_approx(column, 0.5) as median"))`  
B. `df.agg(expr("percentile_approx(column, array(0.25, 0.5, 0.75)) as quartiles"))`  
C. `df.stat.approxQuantile("column", [0.25, 0.5, 0.75], 0.01)`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All approaches calculate percentiles: single percentile, multiple percentiles with expr, and using approxQuantile method.

---

### Question 54
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

What's the difference between UDF and built-in function performance?

A. UDFs have serialization overhead  
B. Built-in functions are optimized by Catalyst  
C. UDFs cannot be pushed down in query optimization  
D. All of the above

**Correct Answer:** D  
**Explanation:** UDFs have performance overhead due to serialization, lack of Catalyst optimization, and reduced pushdown optimization opportunities.

---

### Question 55
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create an array column from multiple columns?

A. `array(col("col1"), col("col2"), col("col3"))`  
B. `create_array(col("col1"), col("col2"), col("col3"))`  
C. `to_array(col("col1"), col("col2"), col("col3"))`  
D. Both A and B

**Correct Answer:** A  
**Explanation:** The `array()` function creates array columns from multiple column expressions. Options B and C are not valid functions.

---

### Question 56
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data validation operations on DataFrames

How do you find rows where any column has null values?

A. `df.filter(col("col1").isNull() | col("col2").isNull() | col("col3").isNull())`  
B. `df.filter(reduce(lambda x, y: x | y, [col(c).isNull() for c in df.columns]))`  
C. `df.where(" OR ".join([f"{c} IS NULL" for c in df.columns]))`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All approaches work: explicit OR conditions, reduce function for dynamic OR, and SQL string with dynamic OR conditions.

---

### Question 57
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

How do you implement a full outer join with coalescing of join keys?

A. `df1.join(df2, join_condition, "full_outer").select(coalesce(df1["id"], df2["id"]).alias("id"), ...)`  
B. `df1.join(df2, ["id"], "full_outer")`  
C. `df1.join(df2, df1["id"] == df2["id"], "full_outer").select(coalesce(df1["id"], df2["id"]).alias("id"), ...)`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** Both approaches handle full outer joins with coalescing. Option B automatically handles join key coalescing when using column names.

---

### Question 58
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate and utilize Date data type

How do you format a date column for display?

A. `date_format(col("date_col"), "yyyy-MM-dd")`  
B. `format_date(col("date_col"), "yyyy-MM-dd")`  
C. `col("date_col").format("yyyy-MM-dd")`  
D. `to_string(col("date_col"), "yyyy-MM-dd")`

**Correct Answer:** A  
**Explanation:** `date_format()` converts dates to formatted strings. The other functions don't exist in Spark SQL.

---

### Question 59
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform operations on DataFrames such as printing schema

How do you get detailed information about DataFrame schema including nullable property?

A. `df.schema`  
B. `df.printSchema()`  
C. `df.dtypes`  
D. Both A and B

**Correct Answer:** D  
**Explanation:** Both `schema` property and `printSchema()` method show nullable information, while `dtypes` only shows column names and types.

---

### Question 60
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you create a struct column from multiple columns?

A. `struct(col("col1"), col("col2"), col("col3"))`  
B. `create_struct("col1", "col2", "col3")`  
C. `struct("col1", "col2", "col3")`  
D. Both A and C

**Correct Answer:** D  
**Explanation:** The `struct()` function can take both column expressions and string column names to create struct columns.

---

### Question 61
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform aggregate operations on DataFrames

How do you calculate mode (most frequent value) of a column?

A. `mode(col("column"))`  
B. `df.groupBy("column").count().orderBy(desc("count")).limit(1)`  
C. `first(col("column")).over(Window.orderBy(desc(count("column"))))`  
D. Spark doesn't have a built-in mode function

**Correct Answer:** B  
**Explanation:** Spark doesn't have a built-in mode function. You need to group by the column, count occurrences, and find the maximum.

---

### Question 62
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Create and invoke user-defined functions

How do you handle exceptions in UDFs?

```python
def safe_divide_udf(x, y):
    try:
        return x / y if y != 0 else None
    except:
        return None
```

A. The UDF handles exceptions correctly  
B. UDFs should not handle exceptions  
C. Use try-except with specific exception types  
D. Return error codes instead of None

**Correct Answer:** A  
**Explanation:** Handling exceptions in UDFs and returning None for invalid operations is a good practice to prevent job failures.

---

### Question 63
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

How do you sample a DataFrame?

A. `df.sample(0.1)`  
B. `df.sample(fraction=0.1, seed=42)`  
C. `df.sample(withReplacement=False, fraction=0.1)`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All are valid sampling methods with different parameter specifications for fraction, seed, and replacement strategy.

---

### Question 64
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Perform data deduplication operations on DataFrames

How do you identify and mark duplicate records without removing them?

A. `df.withColumn("is_duplicate", count("*").over(Window.partitionBy("key_cols")) > 1)`  
B. `df.withColumn("duplicate_count", count("*").over(Window.partitionBy("key_cols")))`  
C. `df.withColumn("row_num", row_number().over(Window.partitionBy("key_cols").orderBy("timestamp")))`  
D. All approaches identify duplicates differently

**Correct Answer:** D  
**Explanation:** Option A marks boolean duplicate flag, Option B counts duplicates, Option C numbers occurrences - all useful for different purposes.

---

### Question 65
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Combine DataFrames with operations

How do you perform a self-join to find related records?

A. `df.alias("a").join(df.alias("b"), col("a.manager_id") == col("b.employee_id"))`  
B. `df.join(df, "common_column")`  
C. `df.crossJoin(df).filter(condition)`  
D. Both A and C are valid approaches

**Correct Answer:** D  
**Explanation:** Both aliasing for column disambiguation and cross join with filter work for self-joins, depending on the use case.

---

## Answer Key Summary

1. D  2. C  3. D  4. A  5. D  6. D  7. B,D  8. A  9. B  10. D
11. D  12. D  13. D  14. D  15. D  16. D  17. D  18. D  19. D  20. A
21. A  22. D  23. B  24. D  25. D  26. A  27. D  28. D  29. C  30. D
31. D  32. A  33. D  34. D  35. D  36. A  37. D  38. D  39. D  40. D
41. B  42. D  43. A  44. A  45. D  46. A  47. D  48. D  49. D  50. D
51. D  52. D  53. D  54. D  55. A  56. D  57. D  58. A  59. D  60. D
61. B  62. A  63. D  64. D  65. D

## Score Interpretation
- **90-100% (59-65 correct):** Excellent! Advanced DataFrame skills
- **80-89% (52-58 correct):** Good grasp of DataFrame operations
- **70-79% (46-51 correct):** Fair understanding, practice complex operations
- **Below 70% (<46 correct):** Focus on DataFrame fundamentals

## Focus Areas for Improvement
- **Window Functions:** Practice partitioning, ordering, and frame specifications
- **Complex Joins:** Master different join types and optimization strategies
- **Date/Time Manipulation:** Learn all date functions and format patterns
- **Data Quality:** Implement comprehensive validation and cleansing techniques
- **UDF Performance:** Understand when to use built-ins vs custom functions