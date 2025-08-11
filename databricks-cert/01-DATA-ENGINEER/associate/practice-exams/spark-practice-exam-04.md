# Apache Spark Developer Associate - Practice Exam 04
## Focus: Spark SQL Advanced (Schema Operations, Data Types, Validation)
**Difficulty Level:** Intermediate to Advanced  
**Time Limit:** 90 minutes  
**Questions:** 70

---

### Question 1
**Section:** Using Spark SQL  
**Objective:** Query files using SQL and DataFrame API

Which of the following statements about schema evolution in Parquet files is TRUE?

A. Schema evolution is not supported in Parquet files  
B. You can only add columns, not remove them  
C. Spark automatically handles compatible schema changes like adding nullable columns  
D. Schema evolution requires rebuilding the entire dataset

**Correct Answer:** C  
**Explanation:** Spark supports schema evolution for Parquet files, automatically handling compatible changes like adding nullable columns or changing data types in compatible ways.

---

### Question 2
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manipulate columns, rows, and table structures

Given a DataFrame with nested struct columns, which function correctly extracts a field from a struct column named 'address' to get the 'city' field?

A. `df.select(col("address.city"))`  
B. `df.select(col("address").getField("city"))`  
C. `df.select(col("address").getItem("city"))`  
D. Both A and B are correct

**Correct Answer:** D  
**Explanation:** Both dot notation (`col("address.city")`) and the `getField()` method work for extracting fields from struct columns.

---

### Question 3
**Section:** Using Spark SQL  
**Objective:** Configure Spark settings for structured data processing

Which Spark SQL configuration enables automatic schema merging when reading Parquet files?

A. `spark.sql.parquet.mergeSchema = true`  
B. `spark.sql.parquet.autoMergeSchema = true`  
C. `spark.sql.adaptive.enabled = true`  
D. `spark.sql.adaptive.coalescePartitions.enabled = true`

**Correct Answer:** A  
**Explanation:** The `spark.sql.parquet.mergeSchema` configuration controls whether Spark automatically merges schemas when reading multiple Parquet files with different schemas.

---

### Question 4
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply data type casting and manipulation

What happens when you cast a string "abc" to IntegerType using `cast()`?

A. Returns 0  
B. Throws an exception  
C. Returns null  
D. Returns -1

**Correct Answer:** C  
**Explanation:** When casting fails (like converting non-numeric string to integer), Spark returns null rather than throwing an exception.

---

### Question 5
**Section:** Using Spark SQL  
**Objective:** Create and configure data frames using complex data types

Which of the following correctly creates a DataFrame with an array column?

A. `spark.createDataFrame([(1, [1,2,3])], ["id", "numbers"])`  
B. `spark.createDataFrame([(1, "1,2,3")], ["id", "numbers"])`  
C. Both A and B create array columns  
D. Neither creates an array column

**Correct Answer:** A  
**Explanation:** Option A creates a DataFrame with an actual array column. Option B creates a string column, not an array.

---

### Question 6
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle complex data types (arrays, maps, structs)

Which function correctly explodes an array column named 'items' into separate rows?

A. `df.select(col("*"), explode(col("items")))`  
B. `df.select(col("*"), explode(col("items")).alias("item"))`  
C. `df.select(col("*"), col("items").explode())`  
D. Both A and B are correct

**Correct Answer:** D  
**Explanation:** Both options use the `explode()` function correctly. Option B additionally provides an alias for the exploded column.

---

### Question 7
**Section:** Using Spark SQL  
**Objective:** Work with complex data types in SQL

In SQL, which function extracts all keys from a map column named 'properties'?

A. `MAP_KEYS(properties)`  
B. `KEYS(properties)`  
C. `GET_KEYS(properties)`  
D. `EXTRACT_KEYS(properties)`

**Correct Answer:** A  
**Explanation:** `MAP_KEYS()` is the correct SQL function to extract all keys from a map column.

---

### Question 8
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply schema validation and enforcement

Which of the following approaches enforces a strict schema when reading JSON files?

A. Setting `multiline=true`  
B. Providing a schema using `.schema()`  
C. Setting `inferSchema=false`  
D. Using `.option("enforceSchema", "true")`

**Correct Answer:** B  
**Explanation:** Providing an explicit schema using `.schema()` enforces strict schema validation when reading data.

---

### Question 9
**Section:** Using Spark SQL  
**Objective:** Handle data type conversions and compatibility

What is the result of this SQL query: `SELECT CAST('2023-12-25' AS DATE)`?

A. A string value '2023-12-25'  
B. A date value representing December 25, 2023  
C. An error because the format is incorrect  
D. A timestamp value

**Correct Answer:** B  
**Explanation:** The CAST function successfully converts the string in ISO format to a date value.

---

### Question 10
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with nested and semi-structured data

Which function correctly flattens a struct column named 'person' with fields 'name' and 'age'?

A. `df.select(col("person.*"))`  
B. `df.select(col("person").getField("*"))`  
C. `df.selectExpr("person.*")`  
D. Both A and C are correct

**Correct Answer:** D  
**Explanation:** Both `col("person.*")` and `selectExpr("person.*")` can be used to flatten struct columns.

---

### Question 11
**Section:** Using Spark SQL  
**Objective:** Optimize data reading with schema management

When is schema inference most expensive in terms of performance?

A. When reading Parquet files  
B. When reading JSON files  
C. When reading CSV files  
D. When reading ORC files

**Correct Answer:** B  
**Explanation:** JSON schema inference is most expensive because Spark needs to scan through all files to determine the complete schema, especially with varying structures.

---

### Question 12
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply data validation techniques

Which approach validates that a column contains only positive numbers?

A. `df.filter(col("value") > 0)`  
B. `df.where(col("value").isNotNull() & (col("value") > 0))`  
C. `df.select("*").where(col("value") >= 1)`  
D. All of the above can be used for validation

**Correct Answer:** D  
**Explanation:** All approaches can be used for validation, but option B is most comprehensive as it also checks for null values.

---

### Question 13
**Section:** Using Spark SQL  
**Objective:** Handle schema conflicts and merging

What happens when you try to union two DataFrames with different column orders but same column names and types?

A. The operation fails with an error  
B. Spark automatically aligns columns by name  
C. Spark aligns columns by position, potentially causing data misalignment  
D. Spark creates new columns for mismatched positions

**Correct Answer:** C  
**Explanation:** Union operations align columns by position, not by name, which can cause data misalignment if column orders differ.

---

### Question 14
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage complex data transformations

Which method correctly adds multiple columns to a DataFrame in a single operation?

A. `df.withColumns({"col1": expr1, "col2": expr2})`  
B. `df.withColumn("col1", expr1).withColumn("col2", expr2)`  
C. `df.select("*", expr1.alias("col1"), expr2.alias("col2"))`  
D. All of the above

**Correct Answer:** D  
**Explanation:** All three approaches can add multiple columns. `withColumns()` is most efficient for multiple columns, while chaining `withColumn()` or using `select()` also work.

---

### Question 15
**Section:** Using Spark SQL  
**Objective:** Work with data type precision and scale

Which data type should you use for precise decimal calculations in financial applications?

A. FloatType  
B. DoubleType  
C. DecimalType  
D. StringType

**Correct Answer:** C  
**Explanation:** DecimalType provides exact precision for financial calculations, avoiding floating-point rounding errors that can occur with FloatType and DoubleType.

---

### Question 16
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle schema evolution scenarios

When adding a new column to an existing Parquet table, which approach maintains backward compatibility?

A. Adding the column as non-nullable  
B. Adding the column as nullable with a default value  
C. Recreating the entire table  
D. Both B and C

**Correct Answer:** B  
**Explanation:** Adding nullable columns with default values maintains backward compatibility, allowing older readers to still access the data.

---

### Question 17
**Section:** Using Spark SQL  
**Objective:** Apply advanced data type operations

Which SQL function correctly checks if an array contains a specific value?

A. `ARRAY_CONTAINS(array_col, value)`  
B. `CONTAINS(array_col, value)`  
C. `IN_ARRAY(value, array_col)`  
D. `ARRAY_INCLUDES(array_col, value)`

**Correct Answer:** A  
**Explanation:** `ARRAY_CONTAINS()` is the correct SQL function to check if an array contains a specific value.

---

### Question 18
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement data quality checks

Which approach efficiently checks for duplicate values across multiple columns?

A. `df.groupBy(["col1", "col2"]).count().where(col("count") > 1)`  
B. `df.distinct().count() != df.count()`  
C. `df.dropDuplicates(["col1", "col2"]).count() != df.count()`  
D. All of the above

**Correct Answer:** A  
**Explanation:** Option A is most efficient for finding duplicates across specific columns, while B and C compare entire rows or specific subsets.

---

### Question 19
**Section:** Using Spark SQL  
**Objective:** Handle timestamp and date operations

What is the difference between `CURRENT_TIMESTAMP()` and `NOW()` in Spark SQL?

A. `CURRENT_TIMESTAMP()` includes timezone, `NOW()` doesn't  
B. They are identical functions  
C. `NOW()` is not supported in Spark SQL  
D. `CURRENT_TIMESTAMP()` is more precise

**Correct Answer:** C  
**Explanation:** Spark SQL supports `CURRENT_TIMESTAMP()` but not `NOW()`. Use `CURRENT_TIMESTAMP()` for current timestamp values.

---

### Question 20
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize schema operations

When should you provide an explicit schema instead of relying on schema inference?

A. When reading small files  
B. When schema is stable and performance is critical  
C. When working with development environments  
D. Never, inference is always better

**Correct Answer:** B  
**Explanation:** Explicit schemas improve performance by avoiding the inference step and provide type safety, especially important in production environments with stable schemas.

---

### Question 21
**Section:** Using Spark SQL  
**Objective:** Work with null handling and data validation

Which function replaces null values with a specified value?

A. `COALESCE(col, default_value)`  
B. `ISNULL(col, default_value)`  
C. `NVLL(col, default_value)`  
D. `IFNULL(col, default_value)`

**Correct Answer:** A  
**Explanation:** `COALESCE()` returns the first non-null value from its arguments, effectively replacing nulls with a default value.

---

### Question 22
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle binary and raw data types

Which data type is most appropriate for storing image data?

A. StringType  
B. BinaryType  
C. ArrayType  
D. MapType

**Correct Answer:** B  
**Explanation:** BinaryType is designed for storing binary data such as images, documents, or other binary content.

---

### Question 23
**Section:** Using Spark SQL  
**Objective:** Apply complex type transformations

Which SQL expression correctly transforms an array of integers to an array of strings?

A. `CAST(array_col AS ARRAY<STRING>)`  
B. `TRANSFORM(array_col, x -> CAST(x AS STRING))`  
C. `MAP(array_col, CAST AS STRING)`  
D. `ARRAY_MAP(array_col, STRING)`

**Correct Answer:** B  
**Explanation:** The `TRANSFORM()` function applies a lambda expression to each element in an array, allowing element-wise transformations.

---

### Question 24
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Manage schema compatibility

What happens when you write a DataFrame with additional columns to a Delta table with fewer columns?

A. The operation fails  
B. Extra columns are ignored  
C. New columns are automatically added to the table schema  
D. Depends on the schema evolution setting

**Correct Answer:** D  
**Explanation:** The behavior depends on Delta table schema evolution settings. By default, it may fail, but with schema evolution enabled, new columns can be added.

---

### Question 25
**Section:** Using Spark SQL  
**Objective:** Handle JSON data processing

Which function correctly extracts a value from a JSON string column?

A. `JSON_EXTRACT(json_col, '$.field')`  
B. `GET_JSON_OBJECT(json_col, '$.field')`  
C. `JSON_VALUE(json_col, '$.field')`  
D. All of the above

**Correct Answer:** B  
**Explanation:** `GET_JSON_OBJECT()` is the correct function in Spark SQL for extracting values from JSON strings using JSONPath expressions.

---

### Question 26
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement data type conversions

Which approach safely converts string dates to DateType with error handling?

A. `col("date_str").cast("date")`  
B. `to_date(col("date_str"), "yyyy-MM-dd")`  
C. `date_format(col("date_str"), "yyyy-MM-dd")`  
D. Both A and B handle errors safely

**Correct Answer:** B  
**Explanation:** `to_date()` with a format pattern provides safer conversion and better error handling than simple casting.

---

### Question 27
**Section:** Using Spark SQL  
**Objective:** Work with array operations

What does the SQL expression `ARRAY_REMOVE(array_col, NULL)` do?

A. Removes the first null element from the array  
B. Removes all null elements from the array  
C. Returns true if the array contains null  
D. Replaces null elements with empty strings

**Correct Answer:** B  
**Explanation:** `ARRAY_REMOVE()` removes all occurrences of the specified value (including NULL) from an array.

---

### Question 28
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle schema merging scenarios

When reading multiple Parquet files with different schemas, which setting allows automatic schema merging?

A. `.option("mergeSchema", "true")`  
B. `.option("autoMergeSchema", "true")`  
C. Setting the Spark configuration before reading  
D. Both A and C

**Correct Answer:** D  
**Explanation:** You can enable schema merging either through the read option or by setting the Spark configuration `spark.sql.parquet.mergeSchema`.

---

### Question 29
**Section:** Using Spark SQL  
**Objective:** Apply date and time functions

Which function extracts the day of week from a date column?

A. `DAY(date_col)`  
B. `DAYOFWEEK(date_col)`  
C. `EXTRACT(DOW FROM date_col)`  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both `DAYOFWEEK()` and `EXTRACT(DOW FROM date)` can extract the day of week from a date column.

---

### Question 30
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize complex data operations

Which approach is most efficient for checking if a column contains only valid email addresses?

A. Using a UDF with regex validation  
B. Using built-in `rlike()` function with regex  
C. Converting to RDD and using map operations  
D. Using SQL LIKE patterns

**Correct Answer:** B  
**Explanation:** The built-in `rlike()` function is optimized and more efficient than UDFs for regex pattern matching.

---

### Question 31
**Section:** Using Spark SQL  
**Objective:** Handle map data type operations

Which SQL function adds a new key-value pair to an existing map column?

A. `MAP_ADD(map_col, key, value)`  
B. `MAP_CONCAT(map_col, MAP(key, value))`  
C. `MAP_INSERT(map_col, key, value)`  
D. `ADD_TO_MAP(map_col, key, value)`

**Correct Answer:** B  
**Explanation:** `MAP_CONCAT()` can be used to add new key-value pairs by concatenating the original map with a new map containing the new key-value pair.

---

### Question 32
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply advanced schema validation

Which approach validates that a DataFrame matches an expected schema exactly?

A. Comparing column names only  
B. Comparing column names and types  
C. Using `df.schema == expected_schema`  
D. All of the above can be used

**Correct Answer:** C  
**Explanation:** Comparing `df.schema` with the expected schema checks both column names and types for exact schema matching.

---

### Question 33
**Section:** Using Spark SQL  
**Objective:** Work with conditional expressions

What is the difference between `CASE` and `IF` expressions in Spark SQL?

A. `CASE` supports multiple conditions, `IF` only supports two outcomes  
B. `IF` is faster than `CASE`  
C. They are identical in functionality  
D. `CASE` only works with string comparisons

**Correct Answer:** A  
**Explanation:** `CASE` expressions support multiple conditions and outcomes, while `IF` is limited to a single condition with two outcomes (true/false).

---

### Question 34
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle data type precision

When defining a DecimalType, what do the precision and scale parameters represent?

A. Precision is total digits, scale is digits after decimal point  
B. Precision is digits before decimal, scale is total digits  
C. Both represent the same value  
D. Precision is accuracy, scale is size

**Correct Answer:** A  
**Explanation:** In DecimalType(precision, scale), precision is the total number of digits, and scale is the number of digits after the decimal point.

---

### Question 35
**Section:** Using Spark SQL  
**Objective:** Apply string manipulation functions

Which function correctly pads a string to a specific length?

A. `PAD(string, length, padString)`  
B. `LPAD(string, length, padString)` or `RPAD(string, length, padString)`  
C. `PADDING(string, length, padString)`  
D. `STRING_PAD(string, length, padString)`

**Correct Answer:** B  
**Explanation:** `LPAD()` pads on the left and `RPAD()` pads on the right to achieve the specified string length.

---

### Question 36
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement error handling strategies

Which approach handles schema evolution errors gracefully when reading data?

A. Using try-catch blocks around read operations  
B. Setting `spark.sql.adaptive.enabled = true`  
C. Using `PERMISSIVE` mode when reading JSON/CSV  
D. Using explicit schema definitions

**Correct Answer:** C  
**Explanation:** `PERMISSIVE` mode allows Spark to handle malformed records gracefully by putting them in a special column rather than failing.

---

### Question 37
**Section:** Using Spark SQL  
**Objective:** Work with window functions on complex types

Can window functions be applied to array or map columns directly?

A. Yes, all window functions work with complex types  
B. No, you must explode complex types first  
C. Only aggregate window functions work with complex types  
D. Only ranking functions work with complex types

**Correct Answer:** C  
**Explanation:** Only aggregate window functions like `collect_list()` or `collect_set()` can work with complex types directly. Other window functions require scalar values.

---

### Question 38
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize data type operations

Which data type conversion is most expensive in terms of performance?

A. StringType to IntegerType  
B. IntegerType to LongType  
C. StringType to TimestampType  
D. DoubleType to DecimalType

**Correct Answer:** C  
**Explanation:** String to timestamp conversion is most expensive because it requires parsing and format validation, especially with various date formats.

---

### Question 39
**Section:** Using Spark SQL  
**Objective:** Handle aggregate functions with complex types

Which aggregate function correctly concatenates string values in a group?

A. `STRING_AGG(col)`  
B. `CONCAT_WS(',', COLLECT_LIST(col))`  
C. `GROUP_CONCAT(col)`  
D. `ARRAY_JOIN(COLLECT_LIST(col), ',')`

**Correct Answer:** B  
**Explanation:** `CONCAT_WS()` combined with `COLLECT_LIST()` effectively concatenates string values in a group with a specified separator.

---

### Question 40
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply schema evolution best practices

Which practice ensures forward compatibility when evolving schemas?

A. Always add columns at the end  
B. Never remove columns, only add nullable ones  
C. Use schema versioning  
D. All of the above

**Correct Answer:** D  
**Explanation:** All practices contribute to forward compatibility: adding columns at the end maintains column order, keeping nullable additions ensures old readers work, and versioning helps track changes.

---

### Question 41
**Section:** Using Spark SQL  
**Objective:** Work with timezone operations

How does `CURRENT_TIMESTAMP()` handle timezone information?

A. Returns UTC time always  
B. Returns local timezone of the driver  
C. Returns timezone based on Spark session timezone setting  
D. Timezone is not supported

**Correct Answer:** C  
**Explanation:** `CURRENT_TIMESTAMP()` returns timestamp based on the Spark session's timezone setting, which can be configured using `spark.sql.session.timeZone`.

---

### Question 42
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle nested schema transformations

Which approach correctly renames a field within a nested struct column?

A. `df.withColumnRenamed("struct.field", "struct.newField")`  
B. `df.withColumn("struct", col("struct").withField("newField", col("struct.field")).dropFields("field"))`  
C. `df.select(col("*"), col("struct").getField("field").alias("newField"))`  
D. Nested field renaming is not supported

**Correct Answer:** B  
**Explanation:** Using `withField()` and `dropFields()` on struct columns allows renaming nested fields by adding the field with a new name and dropping the old one.

---

### Question 43
**Section:** Using Spark SQL  
**Objective:** Apply advanced casting operations

What happens when you cast a very large number to a smaller numeric type?

A. The operation fails with an exception  
B. The value is truncated without warning  
C. The value becomes null  
D. The behavior depends on Spark configuration

**Correct Answer:** B  
**Explanation:** Spark truncates values when casting to smaller numeric types without throwing exceptions, which can lead to data loss if not handled carefully.

---

### Question 44
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement data validation patterns

Which pattern efficiently validates that all values in a column are within a specific range?

A. `df.filter(col("value").between(min_val, max_val)).count() == df.count()`  
B. `df.agg(min("value").between(min_val, max_val) & max("value").between(min_val, max_val))`  
C. `df.select((col("value") >= min_val) & (col("value") <= max_val)).collect()`  
D. Using a UDF to check each value

**Correct Answer:** A  
**Explanation:** Option A is most efficient as it uses Spark's built-in optimization for filtering and counting, avoiding expensive collect operations or complex aggregations.

---

### Question 45
**Section:** Using Spark SQL  
**Objective:** Handle data type inference

When reading CSV files, which configuration forces string type for all columns?

A. `spark.sql.csv.inferSchema = false`  
B. `spark.read.option("inferSchema", "false")`  
C. Both A and B  
D. This is not possible

**Correct Answer:** B  
**Explanation:** Setting the `inferSchema` option to false when reading CSV files treats all columns as strings, avoiding automatic type inference.

---

### Question 46
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with union operations and schema matching

How can you union DataFrames with different but compatible schemas?

A. Use `unionByName()` instead of `union()`  
B. Cast all columns to a common schema first  
C. Use schema evolution settings  
D. Both A and B

**Correct Answer:** D  
**Explanation:** `unionByName()` handles schema differences by matching columns by name, while casting to a common schema ensures type compatibility.

---

### Question 47
**Section:** Using Spark SQL  
**Objective:** Apply functions to array elements

Which SQL function applies a condition to filter array elements?

A. `FILTER(array_col, x -> condition)`  
B. `ARRAY_FILTER(array_col, condition)`  
C. `WHERE(array_col, condition)`  
D. `SELECT_ARRAY(array_col, condition)`

**Correct Answer:** A  
**Explanation:** The `FILTER()` higher-order function applies a lambda expression condition to filter elements within an array.

---

### Question 48
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize schema operations for performance

Which approach minimizes schema inference overhead when reading multiple files?

A. Read one file first to get schema, then apply to all  
B. Use schema caching  
C. Enable adaptive query execution  
D. Use smaller partition sizes

**Correct Answer:** A  
**Explanation:** Reading a representative file first to infer schema, then applying that schema to all files avoids repeated inference operations.

---

### Question 49
**Section:** Using Spark SQL  
**Objective:** Handle timestamp precision and formatting

Which function formats a timestamp with microsecond precision?

A. `DATE_FORMAT(timestamp, 'yyyy-MM-dd HH:mm:ss.SSSSSS')`  
B. `FORMAT_TIMESTAMP(timestamp, 'yyyy-MM-dd HH:mm:ss.SSSSSS')`  
C. `TIMESTAMP_FORMAT(timestamp, 'yyyy-MM-dd HH:mm:ss.SSSSSS')`  
D. Microsecond precision is not supported

**Correct Answer:** A  
**Explanation:** `DATE_FORMAT()` can format timestamps with microsecond precision using the pattern 'SSSSSS' for microseconds.

---

### Question 50
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply complex validation rules

Which approach validates that a JSON string column contains valid JSON?

A. `get_json_object(col, '$') is not null`  
B. `from_json(col, schema) is not null`  
C. Using a try-catch in UDF  
D. All of the above can validate JSON

**Correct Answer:** D  
**Explanation:** All approaches can validate JSON: `get_json_object()` with root path, `from_json()` with schema validation, or UDF with error handling.

---

### Question 51
**Section:** Using Spark SQL  
**Objective:** Work with regex operations on data types

Which function performs case-insensitive regex matching?

A. `RLIKE(column, pattern)`  
B. `REGEXP_LIKE(column, pattern, 'i')`  
C. `REGEXP(column, pattern) WITH CASE_INSENSITIVE`  
D. `ILIKE(column, pattern)`

**Correct Answer:** B  
**Explanation:** `REGEXP_LIKE()` supports flags including 'i' for case-insensitive matching, while `RLIKE()` doesn't have flag support.

---

### Question 52
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle schema compatibility issues

What strategy should you use when joining DataFrames with overlapping column names?

A. Ignore the issue, Spark handles it automatically  
B. Rename columns before joining  
C. Use alias for DataFrames  
D. Both B and C

**Correct Answer:** D  
**Explanation:** Both renaming columns and using DataFrame aliases help resolve column name conflicts during joins.

---

### Question 53
**Section:** Using Spark SQL  
**Objective:** Apply mathematical operations with precision

Which approach maintains precision when performing financial calculations?

A. Use DOUBLE type for all calculations  
B. Use DECIMAL type with appropriate precision and scale  
C. Use BIGINT and handle decimal places manually  
D. Convert to strings for calculations

**Correct Answer:** B  
**Explanation:** DECIMAL type with appropriate precision and scale maintains exact decimal precision required for financial calculations.

---

### Question 54
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement data type constraints

How can you enforce that a column contains only positive integers?

A. Use schema validation during read  
B. Add check constraints (not supported in DataFrames)  
C. Use filtering and validation logic  
D. Use custom data types

**Correct Answer:** C  
**Explanation:** DataFrames don't support check constraints, so validation must be implemented through filtering and business logic.

---

### Question 55
**Section:** Using Spark SQL  
**Objective:** Handle null semantics in operations

How do comparison operations handle null values?

A. Null equals null returns true  
B. Null compared to any value returns false  
C. Null compared to any value returns null  
D. Null handling depends on the operation

**Correct Answer:** C  
**Explanation:** In SQL semantics, any comparison involving null returns null (unknown), not true or false.

---

### Question 56
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Work with user-defined types

Can you create custom data types in Spark DataFrames?

A. Yes, by extending UserDefinedType  
B. No, only built-in types are supported  
C. Only for simple wrapper types  
D. Only through Scala, not Python

**Correct Answer:** A  
**Explanation:** You can create custom data types by extending UserDefinedType, though this is advanced usage and requires careful implementation.

---

### Question 57
**Section:** Using Spark SQL  
**Objective:** Apply type coercion rules

What happens when you add an IntegerType column to a LongType column?

A. The result is IntegerType  
B. The result is LongType  
C. An error occurs  
D. The result is DoubleType

**Correct Answer:** B  
**Explanation:** Spark's type coercion rules promote the result to the wider type (LongType) to avoid data loss.

---

### Question 58
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize struct operations

Which approach is most efficient for accessing multiple fields from a struct column?

A. Multiple `getField()` calls  
B. Selecting `struct.*` to flatten all fields  
C. Using selectExpr with dot notation  
D. Converting struct to JSON and parsing

**Correct Answer:** B  
**Explanation:** Selecting `struct.*` is most efficient as it flattens all fields in a single operation rather than multiple separate field extractions.

---

### Question 59
**Section:** Using Spark SQL  
**Objective:** Handle temporal data types

What's the difference between DATE and TIMESTAMP data types?

A. DATE includes time information, TIMESTAMP doesn't  
B. TIMESTAMP includes time information, DATE doesn't  
C. They are identical  
D. DATE is for older versions, TIMESTAMP for newer

**Correct Answer:** B  
**Explanation:** TIMESTAMP includes both date and time information with precision up to microseconds, while DATE only stores the date portion.

---

### Question 60
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply schema evolution strategies

Which approach allows gradual migration when changing column data types?

A. Change all at once  
B. Add new column with new type, migrate data, drop old column  
C. Use type casting during read  
D. Schema changes are not possible

**Correct Answer:** B  
**Explanation:** The safest approach is to add a new column with the desired type, migrate data gradually, and eventually drop the old column.

---

### Question 61
**Section:** Using Spark SQL  
**Objective:** Work with interval data types

Which function calculates the difference between two timestamps as an interval?

A. `TIMESTAMPDIFF(end_ts, start_ts)`  
B. `INTERVAL(end_ts - start_ts)`  
C. `end_ts - start_ts`  
D. `DATEDIFF(end_ts, start_ts)`

**Correct Answer:** C  
**Explanation:** Simple subtraction of timestamps returns an interval type representing the time difference.

---

### Question 62
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle binary data operations

Which approach efficiently compares binary data columns?

A. Convert to string and compare  
B. Use built-in binary comparison operators  
C. Convert to hex and compare  
D. Binary comparison is not supported

**Correct Answer:** B  
**Explanation:** Spark supports direct binary comparison operations, which are more efficient than string conversions.

---

### Question 63
**Section:** Using Spark SQL  
**Objective:** Apply conditional type operations

Which pattern handles multiple data types in a single column (variant/union types)?

A. Use StringType and parse as needed  
B. Use complex types like struct with type indicator  
C. Use MapType with type information  
D. Union types are not directly supported

**Correct Answer:** D  
**Explanation:** Spark doesn't directly support union/variant types. Common patterns include using struct with type indicators or string representation.

---

### Question 64
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Optimize type casting performance

When is explicit casting necessary versus automatic type coercion?

A. Explicit casting is always faster  
B. When narrowing types or when automatic coercion might lose precision  
C. Only for string conversions  
D. Explicit casting is never necessary

**Correct Answer:** B  
**Explanation:** Explicit casting is necessary when narrowing types (e.g., Long to Int) or when you need control over potential precision loss.

---

### Question 65
**Section:** Using Spark SQL  
**Objective:** Handle schema metadata and annotations

How can you add metadata to DataFrame columns?

A. Metadata cannot be added to columns  
B. Using `.withMetadata()` when creating columns  
C. Only through schema definitions  
D. Metadata is only for documentation

**Correct Answer:** B  
**Explanation:** Column metadata can be added using `.withMetadata()` method and is useful for documentation and tooling integration.

---

### Question 66
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Apply advanced data validation techniques

Which approach validates complex business rules across multiple columns?

A. Column-level constraints  
B. Row-level validation using UDFs  
C. SQL CHECK constraints  
D. Schema-level validation

**Correct Answer:** B  
**Explanation:** Complex business rules requiring multiple columns typically need row-level validation implemented through UDFs or complex SQL expressions.

---

### Question 67
**Section:** Using Spark SQL  
**Objective:** Work with locale-specific data types

How does locale affect date and number formatting in Spark?

A. Spark uses system locale automatically  
B. Locale must be specified in formatting functions  
C. Locale affects parsing but not formatting  
D. Spark doesn't support locale-specific operations

**Correct Answer:** B  
**Explanation:** Locale-specific formatting requires explicit specification in functions like `date_format()` or when parsing numbers with locale-specific formats.

---

### Question 68
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Handle schema validation in production

Which approach ensures schema consistency across different environments?

A. Always use schema inference  
B. Store schemas in external schema registry  
C. Hard-code schemas in application  
D. Use version control for schema files

**Correct Answer:** B  
**Explanation:** External schema registries provide centralized schema management and versioning, ensuring consistency across environments.

---

### Question 69
**Section:** Using Spark SQL  
**Objective:** Apply type safety in SQL operations

Which practice improves type safety when writing SQL queries?

A. Always use string literals  
B. Use strongly-typed column references  
C. Avoid type casting  
D. Use dynamic SQL generation

**Correct Answer:** B  
**Explanation:** Using strongly-typed column references and avoiding string literals improves type safety and catches errors at compile time.

---

### Question 70
**Section:** Developing Apache Spark DataFrame/DataSet API Applications  
**Objective:** Implement comprehensive data type strategies

Which strategy provides the best balance of performance, maintainability, and type safety?

A. Use strings for everything and parse as needed  
B. Define explicit schemas with appropriate types and validation  
C. Rely entirely on automatic inference  
D. Use the most general types possible

**Correct Answer:** B  
**Explanation:** Explicit schemas with appropriate types provide optimal performance through columnar optimizations, maintainability through clear contracts, and type safety through validation.

---

## Answer Key Summary

1. C  2. D  3. A  4. C  5. A  6. D  7. A  8. B  9. B  10. D
11. B  12. D  13. C  14. D  15. C  16. B  17. A  18. A  19. C  20. B
21. A  22. B  23. B  24. D  25. B  26. B  27. B  28. D  29. D  30. B
31. B  32. C  33. A  34. A  35. B  36. C  37. C  38. C  39. B  40. D
41. C  42. B  43. B  44. A  45. B  46. D  47. A  48. A  49. A  50. D
51. B  52. D  53. B  54. C  55. C  56. A  57. B  58. B  59. B  60. B
61. C  62. B  63. D  64. B  65. B  66. B  67. B  68. B  69. B  70. B

## Score Interpretation
- **90-100% (63-70 correct):** Excellent! Advanced SQL and schema mastery
- **80-89% (56-62 correct):** Good preparation, review complex type operations
- **70-79% (49-55 correct):** Fair understanding, focus on schema evolution and validation
- **Below 70% (<49 correct):** More study needed on data types and SQL operations

## Next Steps
- Review explanations for incorrect answers
- Practice with complex schema operations
- Study advanced SQL functions and data type handling
- Focus on production-ready schema management practices