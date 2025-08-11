# Apache Spark Developer Associate - Complete Code Examples

# ========================================
# 1. SPARK SESSION AND CONFIGURATION
# ========================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark import StorageLevel
import pyspark.sql.functions as F

# Create Spark Session with configurations
spark = SparkSession.builder \
    .appName("SparkDeveloperExamples") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")

# ========================================
# 2. CREATING DATAFRAMES
# ========================================

# --- From Data ---
# Create DataFrame from Python data
data = [
    ("Alice", 25, "Engineer", 75000),
    ("Bob", 30, "Manager", 85000),
    ("Charlie", 35, "Director", 95000),
    ("Diana", 28, "Engineer", 78000)
]

columns = ["name", "age", "job_title", "salary"]
df_employees = spark.createDataFrame(data, columns)

# Create DataFrame with explicit schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("job_title", StringType(), True),
    StructField("salary", DoubleType(), True)
])

df_with_schema = spark.createDataFrame(data, schema)

# --- From Files ---
# CSV with options
df_csv = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", ",") \
    .option("nullValue", "NULL") \
    .csv("/path/to/file.csv")

# JSON with multiline
df_json = spark.read \
    .option("multiLine", "true") \
    .option("mode", "PERMISSIVE") \
    .json("/path/to/file.json")

# Parquet (schema preserved)
df_parquet = spark.read.parquet("/path/to/file.parquet")

# With explicit schema for CSV
csv_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("age", IntegerType(), True)
])

df_csv_schema = spark.read \
    .option("header", "true") \
    .schema(csv_schema) \
    .csv("/path/to/file.csv")

# ========================================
# 3. BASIC DATAFRAME OPERATIONS
# ========================================

# --- Selection and Projection ---
# Select specific columns
df_selected = df_employees.select("name", "salary")
df_selected = df_employees.select(col("name"), col("salary"))
df_selected = df_employees.select(F.col("name"), F.col("salary"))

# Select with aliases
df_aliased = df_employees.select(
    col("name").alias("employee_name"),
    col("salary").alias("annual_salary")
)

# Select all columns plus new ones
df_with_new = df_employees.select("*", 
    (col("salary") * 0.1).alias("bonus"),
    lit("USD").alias("currency")
)

# --- Filtering ---
# Basic filtering
df_filtered = df_employees.filter(col("age") > 25)
df_filtered = df_employees.where(col("age") > 25)  # Same as filter

# Multiple conditions
df_complex_filter = df_employees.filter(
    (col("age") > 25) & 
    (col("salary") > 80000) & 
    (col("job_title") != "Manager")
)

# String filtering
df_string_filter = df_employees.filter(
    col("name").startswith("A") | 
    col("job_title").contains("Engineer")
)

# IN and NOT IN
df_in_filter = df_employees.filter(
    col("job_title").isin(["Engineer", "Director"])
)

# Null filtering
df_not_null = df_employees.filter(col("name").isNotNull())
df_null = df_employees.filter(col("name").isNull())

# --- Sorting ---
# Single column sort
df_sorted = df_employees.orderBy("salary")
df_sorted_desc = df_employees.orderBy(col("salary").desc())

# Multiple column sort
df_multi_sort = df_employees.orderBy(
    col("job_title").asc(),
    col("salary").desc()
)

# --- Column Operations ---
# Add new columns
df_with_columns = df_employees \
    .withColumn("salary_k", col("salary") / 1000) \
    .withColumn("age_group", 
        when(col("age") < 30, "Young")
        .when(col("age") < 40, "Middle")
        .otherwise("Senior")
    ) \
    .withColumn("is_high_earner", col("salary") > 80000)

# Rename columns
df_renamed = df_employees \
    .withColumnRenamed("name", "employee_name") \
    .withColumnRenamed("job_title", "position")

# Drop columns
df_dropped = df_employees.drop("age", "job_title")

# Cast columns
df_cast = df_employees \
    .withColumn("salary_str", col("salary").cast("string")) \
    .withColumn("age_double", col("age").cast("double"))

# ========================================
# 4. STRING FUNCTIONS
# ========================================

# Create sample data with strings
string_data = [
    ("John Doe", "john.doe@email.com", "123-456-7890"),
    ("jane smith", "JANE.SMITH@EMAIL.COM", "987-654-3210"),
    ("Bob Wilson", "bob@company.org", "555-123-4567")
]

df_strings = spark.createDataFrame(
    string_data, 
    ["name", "email", "phone"]
)

# String transformations
df_string_ops = df_strings.select(
    # Case functions
    upper("name").alias("name_upper"),
    lower("email").alias("email_lower"),
    initcap("name").alias("name_proper"),
    
    # Length and substring
    length("name").alias("name_length"),
    substring("phone", 1, 3).alias("area_code"),
    
    # Trim and pad
    trim(lit("  hello  ")).alias("trimmed"),
    lpad("name", 20, "*").alias("left_padded"),
    rpad("name", 20, "*").alias("right_padded"),
    
    # Replace and extract
    regexp_replace("phone", "[^0-9]", "").alias("phone_digits"),
    regexp_extract("email", "([^@]+)@", 1).alias("username"),
    
    # Split and concat
    split("name", " ").alias("name_parts"),
    concat("name", lit(" - "), "email").alias("name_email")
)

# ========================================
# 5. DATE AND TIME FUNCTIONS
# ========================================

# Create sample data with dates
date_data = [
    ("2023-01-15", "2023-01-15 09:30:00"),
    ("2023-06-22", "2023-06-22 14:45:30"),
    ("2023-12-03", "2023-12-03 18:20:15")
]

df_dates = spark.createDataFrame(
    date_data,
    ["date_str", "timestamp_str"]
).select(
    to_date("date_str").alias("date_col"),
    to_timestamp("timestamp_str").alias("timestamp_col")
)

# Date operations
df_date_ops = df_dates.select(
    # Current date/time
    current_date().alias("today"),
    current_timestamp().alias("now"),
    
    # Extract components
    year("date_col").alias("year"),
    month("date_col").alias("month"),
    dayofmonth("date_col").alias("day"),
    dayofweek("date_col").alias("day_of_week"),
    dayofyear("date_col").alias("day_of_year"),
    weekofyear("date_col").alias("week_of_year"),
    
    # Date arithmetic
    date_add("date_col", 30).alias("date_plus_30"),
    date_sub("date_col", 7).alias("date_minus_7"),
    datediff(current_date(), "date_col").alias("days_ago"),
    
    # Format dates
    date_format("timestamp_col", "yyyy-MM-dd HH:mm").alias("formatted"),
    
    # Truncate dates
    date_trunc("month", "timestamp_col").alias("month_start"),
    date_trunc("year", "timestamp_col").alias("year_start")
)

# ========================================
# 6. AGGREGATIONS AND GROUP BY
# ========================================

# Sample sales data
sales_data = [
    ("North", "Electronics", 1000, "2023-01-15"),
    ("South", "Clothing", 750, "2023-01-16"),
    ("North", "Electronics", 1200, "2023-01-17"),
    ("East", "Books", 300, "2023-01-18"),
    ("South", "Electronics", 950, "2023-01-19"),
    ("West", "Clothing", 600, "2023-01-20")
]

df_sales = spark.createDataFrame(
    sales_data,
    ["region", "category", "amount", "date"]
).withColumn("date", to_date("date"))

# Basic aggregations
df_basic_agg = df_sales.agg(
    count("*").alias("total_rows"),
    sum("amount").alias("total_sales"),
    avg("amount").alias("avg_sales"),
    min("amount").alias("min_sales"),
    max("amount").alias("max_sales"),
    stddev("amount").alias("stddev_sales")
)

# Group by single column
df_region_agg = df_sales.groupBy("region").agg(
    count("*").alias("transaction_count"),
    sum("amount").alias("total_sales"),
    avg("amount").alias("avg_sales"),
    collect_list("category").alias("categories"),
    collect_set("category").alias("unique_categories")
)

# Group by multiple columns
df_multi_group = df_sales.groupBy("region", "category").agg(
    sum("amount").alias("total_sales"),
    count("*").alias("transaction_count"),
    max("amount").alias("max_transaction")
)

# Having clause (filter after grouping)
df_having = df_sales.groupBy("region").agg(
    sum("amount").alias("total_sales")
).filter(col("total_sales") > 1000)

# Advanced aggregations
df_advanced_agg = df_sales.groupBy("region").agg(
    # Percentiles
    expr("percentile_approx(amount, 0.5)").alias("median_sales"),
    expr("percentile_approx(amount, array(0.25, 0.75))").alias("quartiles"),
    
    # First and last values
    first("amount").alias("first_amount"),
    last("amount").alias("last_amount"),
    
    # Count distinct
    countDistinct("category").alias("unique_categories_count")
)

# ========================================
# 7. JOINS
# ========================================

# Create sample datasets for joins
customers_data = [
    (1, "Alice", "alice@email.com"),
    (2, "Bob", "bob@email.com"),
    (3, "Charlie", "charlie@email.com"),
    (4, "Diana", "diana@email.com")
]

orders_data = [
    (101, 1, 150.0, "2023-01-15"),
    (102, 2, 200.0, "2023-01-16"),
    (103, 1, 75.0, "2023-01-17"),
    (104, 5, 300.0, "2023-01-18")  # Customer 5 doesn't exist
]

df_customers = spark.createDataFrame(
    customers_data,
    ["customer_id", "name", "email"]
)

df_orders = spark.createDataFrame(
    orders_data,
    ["order_id", "customer_id", "amount", "order_date"]
)

# Different types of joins
# Inner join (default)
df_inner = df_customers.join(
    df_orders,
    "customer_id",  # Join on same column name
    "inner"
)

# Left join
df_left = df_customers.join(
    df_orders,
    df_customers.customer_id == df_orders.customer_id,  # Explicit condition
    "left"
)

# Right join
df_right = df_customers.join(df_orders, "customer_id", "right")

# Full outer join
df_full = df_customers.join(df_orders, "customer_id", "full")

# Self join example
df_employees_mgr = spark.createDataFrame([
    (1, "Alice", None),
    (2, "Bob", 1),
    (3, "Charlie", 1),
    (4, "Diana", 2)
], ["emp_id", "name", "manager_id"])

df_self_join = df_employees_mgr.alias("emp").join(
    df_employees_mgr.alias("mgr"),
    col("emp.manager_id") == col("mgr.emp_id"),
    "left"
).select(
    col("emp.name").alias("employee"),
    col("mgr.name").alias("manager")
)

# Multiple join conditions
df_complex_join = df_customers.join(
    df_orders,
    (df_customers.customer_id == df_orders.customer_id) & 
    (df_orders.amount > 100),
    "inner"
)

# ========================================
# 8. WINDOW FUNCTIONS
# ========================================

# Sample data for window functions
employee_data = [
    ("Alice", "Engineering", 75000, "2020-01-15"),
    ("Bob", "Engineering", 82000, "2019-03-10"),
    ("Charlie", "Sales", 65000, "2021-06-20"),
    ("Diana", "Engineering", 78000, "2020-11-05"),
    ("Eve", "Sales", 70000, "2019-09-15"),
    ("Frank", "Marketing", 60000, "2022-02-28")
]

df_emp_window = spark.createDataFrame(
    employee_data,
    ["name", "department", "salary", "hire_date"]
).withColumn("hire_date", to_date("hire_date"))

# Window specifications
dept_window = Window.partitionBy("department").orderBy("salary")
dept_salary_window = Window.partitionBy("department").orderBy(col("salary").desc())
running_total_window = Window.partitionBy("department").orderBy("hire_date") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Ranking functions
df_ranking = df_emp_window.select(
    "*",
    row_number().over(dept_salary_window).alias("row_num"),
    rank().over(dept_salary_window).alias("rank"),
    dense_rank().over(dept_salary_window).alias("dense_rank"),
    percent_rank().over(dept_salary_window).alias("percent_rank"),
    ntile(3).over(dept_salary_window).alias("tertile")
)

# Analytic functions
df_analytic = df_emp_window.select(
    "*",
    lag("salary", 1).over(dept_window).alias("prev_salary"),
    lead("salary", 1).over(dept_window).alias("next_salary"),
    first("salary").over(dept_salary_window).alias("highest_salary"),
    last("salary").over(dept_salary_window).alias("lowest_salary")
)

# Aggregate window functions
df_window_agg = df_emp_window.select(
    "*",
    sum("salary").over(running_total_window).alias("running_total"),
    avg("salary").over(Window.partitionBy("department")).alias("dept_avg_salary"),
    count("*").over(Window.partitionBy("department")).alias("dept_count"),
    (col("salary") - avg("salary").over(Window.partitionBy("department"))).alias("salary_diff_from_avg")
)

# ========================================
# 9. COMPLEX DATA TYPES
# ========================================

# Arrays
array_data = [
    ("Alice", ["Python", "SQL", "Spark"]),
    ("Bob", ["Java", "Scala", "Kafka"]),
    ("Charlie", ["R", "SQL"])
]

df_arrays = spark.createDataFrame(
    array_data,
    ["name", "skills"]
)

# Array operations
df_array_ops = df_arrays.select(
    "*",
    size("skills").alias("skill_count"),
    array_contains("skills", "SQL").alias("knows_sql"),
    sort_array("skills").alias("skills_sorted"),
    array_distinct("skills").alias("unique_skills")
)

# Explode arrays
df_exploded = df_arrays.select(
    "name",
    explode("skills").alias("skill")
)

# Maps/Structs
complex_data = [
    ("Alice", {"street": "123 Main St", "city": "NYC", "zip": "10001"}),
    ("Bob", {"street": "456 Oak Ave", "city": "LA", "zip": "90210"})
]

df_complex = spark.createDataFrame(
    complex_data,
    ["name", "address"]
)

# Access nested data
df_nested_access = df_complex.select(
    "name",
    col("address.street").alias("street"),
    col("address.city").alias("city"),
    col("address.zip").alias("zip_code")
)

# Create structs
df_with_struct = df_employees.select(
    "name",
    struct(
        col("age"),
        col("job_title"),
        col("salary")
    ).alias("employee_info")
)

# ========================================
# 10. USER DEFINED FUNCTIONS (UDFs)
# ========================================

# Simple UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, IntegerType

@udf(returnType=StringType())
def categorize_salary(salary):
    if salary >= 80000:
        return "High"
    elif salary >= 60000:
        return "Medium"
    else:
        return "Low"

# Apply UDF
df_with_udf = df_employees.withColumn(
    "salary_category",
    categorize_salary(col("salary"))
)

# UDF with multiple inputs
@udf(returnType=IntegerType())
def calculate_years_to_retirement(age, retirement_age=65):
    return max(0, retirement_age - age)

df_retirement = df_employees.withColumn(
    "years_to_retirement",
    calculate_years_to_retirement(col("age"))
)

# Pandas UDF (Vectorized) - More efficient
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(returnType="double")
def calculate_tax(salary_series: pd.Series) -> pd.Series:
    return salary_series * 0.25  # 25% tax rate

df_with_tax = df_employees.withColumn(
    "tax_amount",
    calculate_tax(col("salary"))
)

# ========================================
# 11. DATA CLEANING AND NULL HANDLING
# ========================================

# Sample data with nulls and issues
dirty_data = [
    ("Alice", 25, "Engineer", 75000.0),
    ("Bob", None, "Manager", 85000.0),
    (None, 35, "Director", None),
    ("Diana", 28, "", 78000.0),
    ("Eve", -5, "Engineer", 80000.0)  # Invalid age
]

df_dirty = spark.createDataFrame(
    dirty_data,
    ["name", "age", "job_title", "salary"]
)

# Check for nulls
df_null_counts = df_dirty.select([
    count(when(col(c).isNull(), c)).alias(f"{c}_nulls")
    for c in df_dirty.columns
])

# Drop nulls
df_drop_any_null = df_dirty.na.drop()  # Drop rows with any null
df_drop_all_null = df_dirty.na.drop(how="all")  # Drop only if all are null
df_drop_subset = df_dirty.na.drop(subset=["name", "salary"])  # Drop if specific columns are null

# Fill nulls
df_fill_nulls = df_dirty.na.fill({
    "name": "Unknown",
    "age": 0,
    "job_title": "TBD",
    "salary": 0.0
})

# Fill with column-specific values
df_fill_specific = df_dirty.na.fill(0, ["age", "salary"]) \
    .na.fill("Unknown", ["name", "job_title"])

# Replace specific values
df_replaced = df_dirty.replace(["", "TBD"], ["Unknown", "To Be Determined"], "job_title")

# Data validation and cleaning
df_cleaned = df_dirty.filter(
    col("name").isNotNull() &
    (col("age") > 0) & (col("age") < 100) &
    col("job_title").isNotNull() &
    (col("salary") > 0)
)

# ========================================
# 12. PERFORMANCE OPTIMIZATION
# ========================================

# Caching strategies
# Cache frequently used DataFrames
df_to_cache = df_sales.filter(col("amount") > 500)
df_to_cache.cache()
df_to_cache.count()  # Trigger caching

# Different storage levels
df_to_cache.persist(StorageLevel.MEMORY_ONLY)
df_to_cache.persist(StorageLevel.MEMORY_AND_DISK)
df_to_cache.persist(StorageLevel.DISK_ONLY)

# Unpersist when done
df_to_cache.unpersist()

# Partitioning
# Repartition by column (hash partitioning)
df_repartitioned = df_sales.repartition(4, "region")

# Range partitioning for ordered data
df_range_partitioned = df_sales.repartitionByRange(4, "amount")

# Coalesce to reduce partitions
df_coalesced = df_sales.coalesce(2)

# Broadcast joins for small tables
from pyspark.sql.functions import broadcast

df_broadcast_join = df_orders.join(
    broadcast(df_customers),  # Broadcast the smaller table
    "customer_id"
)

# ========================================
# 13. FILE I/O OPERATIONS
# ========================================

# Writing DataFrames
# Write as Parquet (recommended)
df_sales.write \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .parquet("/path/to/output.parquet")

# Write as CSV
df_sales.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("/path/to/output.csv")

# Write as JSON
df_sales.write \
    .mode("overwrite") \
    .json("/path/to/output.json")

# Partitioned writes
df_sales.write \
    .mode("overwrite") \
    .partitionBy("region") \
    .parquet("/path/to/partitioned_output")

# Write modes
df_sales.write.mode("overwrite").parquet("/path")  # Replace all data
df_sales.write.mode("append").parquet("/path")     # Add to existing data
df_sales.write.mode("ignore").parquet("/path")     # Skip if exists
df_sales.write.mode("error").parquet("/path")      # Fail if exists (default)

# ========================================
# 14. SPARK SQL INTEGRATION
# ========================================

# Create temporary views
df_sales.createOrReplaceTempView("sales")
df_customers.createOrReplaceTempView("customers")

# Execute SQL queries
sql_result = spark.sql("""
    SELECT 
        region,
        category,
        SUM(amount) as total_sales,
        COUNT(*) as transaction_count,
        AVG(amount) as avg_sales
    FROM sales
    GROUP BY region, category
    ORDER BY total_sales DESC
""")

# Complex SQL with joins
sql_join_result = spark.sql("""
    SELECT 
        c.name,
        c.email,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as total_spent
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name, c.email
    ORDER BY total_spent DESC
""")

# Window functions in SQL
sql_window_result = spark.sql("""
    SELECT 
        name,
        department,
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank,
        LAG(salary) OVER (PARTITION BY department ORDER BY salary) as prev_salary
    FROM employees
""")

# ========================================
# 15. COMMON PATTERNS AND BEST PRACTICES
# ========================================

# Efficient filtering with predicate pushdown
# Good: Filter early
filtered_df = spark.read.parquet("/large/dataset") \
    .filter(col("date") >= "2023-01-01") \
    .filter(col("region") == "North")

# Chain operations efficiently
result = df_sales \
    .filter(col("amount") > 100) \
    .groupBy("region") \
    .agg(sum("amount").alias("total")) \
    .orderBy(col("total").desc())

# Use built-in functions instead of UDFs when possible
# Good: Built-in function
df.withColumn("amount_category", 
    when(col("amount") > 1000, "High")
    .when(col("amount") > 500, "Medium")
    .otherwise("Low")
)

# Avoid collecting large datasets
# Bad: Don't do this with large data
# large_data = df.collect()  # Brings all data to driver

# Good: Use sampling or aggregations
sample_data = df.sample(0.1).collect()  # 10% sample
summary_stats = df.agg(count("*"), avg("amount")).collect()

# Schema validation
def validate_schema(df, expected_columns):
    actual_columns = set(df.columns)
    expected_columns = set(expected_columns)
    
    missing = expected_columns - actual_columns
    extra = actual_columns - expected_columns
    
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if extra:
        print(f"Warning: Extra columns: {extra}")

# Usage
validate_schema(df_sales, ["region", "category", "amount", "date"])

# ========================================
# 16. DEBUGGING AND MONITORING
# ========================================

# Explain query execution plan
df_sales.filter(col("amount") > 500).explain()
df_sales.filter(col("amount") > 500).explain(True)  # Extended explanation

# Show DataFrame schema
df_sales.printSchema()

# Get DataFrame statistics
df_sales.describe().show()
df_sales.summary().show()

# Count and show sample data
print(f"Row count: {df_sales.count()}")
df_sales.show(5)  # Show first 5 rows
df_sales.show(5, truncate=False)  # Don't truncate long strings

# Check partitioning
print(f"Number of partitions: {df_sales.rdd.getNumPartitions()}")

# Monitor Spark application
spark.sparkContext.statusTracker().getExecutorInfos()

# Stop Spark session when done
# spark.stop()