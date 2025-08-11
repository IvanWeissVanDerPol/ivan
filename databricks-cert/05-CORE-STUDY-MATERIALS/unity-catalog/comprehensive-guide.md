# Unity Catalog - Comprehensive Study Guide for Databricks Certifications

## Overview
Unity Catalog is a centralized data catalog that provides access control, auditing, lineage, quality monitoring, and data discovery capabilities across Databricks workspaces.

## Key Features

### 1. Define Once, Secure Everywhere
- **Single place** to administer data access policies
- **Applies across all workspaces** in a region
- **Consistent governance** across environments

### 2. Standards-Compliant Security Model
- **ANSI SQL-based** permissions model
- **Familiar syntax** for granting permissions
- **Fine-grained access control** down to row/column level

### 3. Built-in Auditing and Lineage
- **Automatic audit logs** capture user-level access
- **Data lineage tracking** shows how assets are created and used
- **Cross-language support** for lineage capture

### 4. Data Discovery
- **Tagging and documentation** capabilities
- **Search interface** for finding data assets
- **Metadata enrichment** for better discoverability

### 5. System Tables
- **Operational data access** including audit logs
- **Billable usage information**
- **Lineage data** for analytics

## Unity Catalog Object Model

### Three-Level Hierarchy
```
metastore
    ├── catalog
    │   ├── schema
    │   │   ├── table
    │   │   ├── view
    │   │   ├── volume
    │   │   ├── function
    │   │   └── model
    │   └── schema
    └── catalog
```

### Namespace Format
All objects referenced as: `catalog.schema.object`

## Core Objects

### Level 1: Metastore and Catalogs

#### Metastore
- **Top-level container** for metadata
- **One per region** recommended
- **Multi-tenant environment** with logical boundaries
- **Account-level resource**

#### Catalogs
- **Organize data assets** at high level
- **Mirror organizational units** or development lifecycles
- **Data isolation boundary**
- **Security boundary**

```sql
-- Create catalog
CREATE CATALOG my_catalog;

-- Use catalog
USE CATALOG my_catalog;

-- Grant permissions on catalog
GRANT USE CATALOG ON CATALOG my_catalog TO `data-team`;
```

### Level 2: Schemas

#### Schemas (Databases)
- **Contain tables, views, volumes, models, functions**
- **Logical organization** within catalogs
- **Project or team-level grouping**
- **Fine-grained security boundary**

```sql
-- Create schema
CREATE SCHEMA my_catalog.my_schema;

-- Create schema with managed location
CREATE SCHEMA my_catalog.my_schema 
MANAGED LOCATION 's3://my-bucket/my-schema/';

-- Grant permissions on schema
GRANT CREATE TABLE ON SCHEMA my_catalog.my_schema TO `dev-team`;
```

### Level 3: Data and AI Objects

#### Tables
- **Managed tables**: Unity Catalog manages full lifecycle
- **External tables**: Unity Catalog manages access only
- **Delta format** for managed tables (required)
- **Multiple formats** for external tables

```sql
-- Create managed table
CREATE TABLE my_catalog.my_schema.sales (
    id BIGINT,
    amount DECIMAL(10,2),
    date DATE
) USING DELTA;

-- Create external table
CREATE TABLE my_catalog.my_schema.external_sales
USING PARQUET
LOCATION 's3://my-bucket/sales-data/';
```

#### Views
- **Saved queries** against tables
- **Can span multiple catalogs/schemas**
- **Support for dynamic views** (row/column level security)

```sql
-- Create view
CREATE VIEW my_catalog.my_schema.high_value_sales AS
SELECT * FROM my_catalog.my_schema.sales
WHERE amount > 1000;

-- Create dynamic view with row-level security
CREATE VIEW my_catalog.my_schema.secure_sales AS
SELECT * FROM my_catalog.my_schema.sales
WHERE CASE 
  WHEN is_member('finance-team') THEN TRUE
  WHEN is_member('sales-team') THEN sales_person = current_user()
  ELSE FALSE
END;
```

#### Volumes
- **Store non-tabular data** (files, images, documents)
- **Managed volumes**: Unity Catalog manages lifecycle
- **External volumes**: Access control only
- **Support for any file format**

```sql
-- Create managed volume
CREATE VOLUME my_catalog.my_schema.my_volume;

-- Create external volume
CREATE VOLUME my_catalog.my_schema.external_volume
LOCATION 's3://my-bucket/files/';

-- Access files in volume
LIST '/Volumes/my_catalog/my_schema/my_volume/';
```

#### Functions
- **User-defined functions (UDFs)**
- **Scalar or table functions**
- **Reusable business logic**

```sql
-- Create SQL function
CREATE FUNCTION my_catalog.my_schema.calculate_tax(amount DECIMAL(10,2))
RETURNS DECIMAL(10,2)
RETURN amount * 0.08;

-- Create Python UDF
CREATE FUNCTION my_catalog.my_schema.process_data(input STRING)
RETURNS STRING
LANGUAGE PYTHON
AS
$$
def process_data(input_str):
    return input_str.upper()
return process_data(input)
$$;
```

#### Models
- **MLflow models** registered in Unity Catalog
- **Version management**
- **Deployment tracking**
- **Access control**

```python
import mlflow

# Register model in Unity Catalog
mlflow.register_model(
    model_uri="runs:/run-id/model",
    name="my_catalog.my_schema.my_model"
)
```

## External Data Access Objects

### Storage Credentials
- **Encapsulate cloud credentials**
- **Long-term access** to cloud storage
- **Reusable across external locations**

```sql
-- Create storage credential (AWS)
CREATE STORAGE CREDENTIAL my_credential
USING AWS (
    IAM_ROLE_ARN 'arn:aws:iam::account:role/role-name'
);
```

### External Locations
- **Reference storage path and credentials**
- **Used for external tables and volumes**
- **Can be used for managed storage locations**

```sql
-- Create external location
CREATE EXTERNAL LOCATION my_location
URL 's3://my-bucket/data/'
WITH (STORAGE CREDENTIAL my_credential);

-- Grant access to external location
GRANT READ FILES ON EXTERNAL LOCATION my_location TO `data-team`;
```

### Connections
- **Access external databases**
- **Lakehouse Federation**
- **Read-only access to external systems**

```sql
-- Create connection for external database
CREATE CONNECTION my_mysql_conn
TYPE mysql
OPTIONS (
  host 'mysql-server.example.com',
  port '3306',
  database 'mydb',
  user 'username'
);
```

## Security and Access Control

### Privilege Model

#### Object Privileges
- **USE CATALOG**: Access catalog and its objects
- **USE SCHEMA**: Access schema and its objects
- **SELECT**: Read table/view data
- **MODIFY**: Update/delete table data
- **CREATE TABLE**: Create tables in schema
- **CREATE SCHEMA**: Create schemas in catalog
- **MANAGE**: Manage permissions on object

#### Administrative Privileges
- **ALL PRIVILEGES**: All permissions on object
- **MODIFY**: Manage object properties
- **MANAGE**: Grant/revoke permissions

### Granting and Revoking Permissions

```sql
-- Grant catalog access
GRANT USE CATALOG ON CATALOG my_catalog TO `data-team`;

-- Grant schema permissions
GRANT CREATE TABLE, USE SCHEMA ON SCHEMA my_catalog.my_schema TO `dev-team`;

-- Grant table permissions
GRANT SELECT ON TABLE my_catalog.my_schema.sales TO `analysts`;

-- Grant with inheritance
GRANT SELECT ON CATALOG my_catalog TO `read-only-users`;

-- Revoke permissions
REVOKE SELECT ON TABLE my_catalog.my_schema.sales FROM `temp-user`;
```

### Row and Column Level Security

#### Dynamic Views
```sql
-- Column-level security
CREATE VIEW my_catalog.my_schema.masked_customers AS
SELECT 
    customer_id,
    name,
    CASE 
        WHEN is_member('pii-access') THEN email
        ELSE 'REDACTED'
    END as email,
    city
FROM my_catalog.my_schema.customers;

-- Row-level security
CREATE VIEW my_catalog.my_schema.region_sales AS
SELECT * FROM my_catalog.my_schema.sales
WHERE region = (
    SELECT region FROM my_catalog.my_schema.user_regions 
    WHERE user_name = current_user()
);
```

## Data Governance Features

### Auditing
- **Automatic audit logging**
- **User-level access tracking**
- **Query history**
- **Permission changes**

```sql
-- Query audit logs using system tables
SELECT * FROM system.access.audit
WHERE service_name = 'unityCatalog'
AND action_name = 'createTable'
ORDER BY event_time DESC;
```

### Lineage
- **Automatic lineage capture**
- **Table and column-level tracking**
- **Cross-workspace visibility**
- **Upstream/downstream relationships**

```sql
-- Query lineage information
SELECT * FROM system.information_schema.table_lineage
WHERE source_table_full_name = 'my_catalog.my_schema.sales';
```

### Data Quality Monitoring
- **Schema drift detection**
- **Data freshness monitoring**
- **Quality metrics**
- **Alerting capabilities**

```sql
-- Create quality monitor
CREATE QUALITY MONITOR my_catalog.my_schema.sales_monitor
ON TABLE my_catalog.my_schema.sales
WITH OPTIONS (
    freshness_threshold = INTERVAL 1 DAY,
    anomaly_detection = true
);
```

## Storage Management

### Managed vs External Objects

#### Managed Tables/Volumes
- **Unity Catalog manages full lifecycle**
- **Stored in managed storage locations**
- **Automatic optimization**
- **Better performance**

```sql
-- Create managed table
CREATE TABLE my_catalog.my_schema.managed_table (
    id BIGINT,
    name STRING
) USING DELTA;
```

#### External Tables/Volumes
- **Access control only**
- **Data managed outside Databricks**
- **Flexibility for external access**
- **Multiple format support**

```sql
-- Create external table
CREATE TABLE my_catalog.my_schema.external_table (
    id BIGINT,
    name STRING
)
USING PARQUET
LOCATION '/external-location/data/';
```

### Storage Location Hierarchy

#### Hierarchy Evaluation Order
1. **Schema-level** storage location
2. **Catalog-level** storage location
3. **Metastore-level** storage location (default)

```sql
-- Set catalog-level managed location
ALTER CATALOG my_catalog 
SET MANAGED LOCATION 's3://my-bucket/catalog-data/';

-- Set schema-level managed location
ALTER SCHEMA my_catalog.my_schema 
SET MANAGED LOCATION 's3://my-bucket/schema-data/';
```

## Best Practices

### 1. Naming Conventions
```sql
-- Use consistent naming patterns
-- Environment_BusinessDomain_DataType
prod_sales_raw
dev_marketing_processed
staging_finance_curated
```

### 2. Security Design
- **Principle of least privilege**
- **Use groups instead of individual users**
- **Implement role-based access control**
- **Regular access reviews**

### 3. Storage Organization
- **Separate catalogs by environment** (dev, staging, prod)
- **Organize schemas by business domain**
- **Use appropriate storage locations for compliance**

### 4. Governance Implementation
- **Document data assets with tags and descriptions**
- **Implement data classification schemes**
- **Set up monitoring and alerting**
- **Regular lineage reviews**

## Common Operations

### Catalog Management
```sql
-- Create catalog with properties
CREATE CATALOG sales_catalog
COMMENT 'Sales data catalog'
WITH MANAGED LOCATION 's3://sales-bucket/data/';

-- Show catalogs
SHOW CATALOGS;

-- Describe catalog
DESCRIBE CATALOG EXTENDED sales_catalog;

-- Drop catalog (must be empty)
DROP CATALOG sales_catalog;
```

### Schema Management
```sql
-- Create schema with properties
CREATE SCHEMA sales_catalog.raw_data
COMMENT 'Raw sales data'
WITH MANAGED LOCATION 's3://sales-bucket/raw/';

-- Show schemas
SHOW SCHEMAS IN sales_catalog;

-- Describe schema
DESCRIBE SCHEMA EXTENDED sales_catalog.raw_data;

-- Alter schema
ALTER SCHEMA sales_catalog.raw_data 
SET OWNER TO `data-engineering-team`;
```

### Table Management
```sql
-- Create table with properties
CREATE TABLE sales_catalog.raw_data.transactions (
    id BIGINT NOT NULL,
    customer_id BIGINT,
    amount DECIMAL(10,2),
    transaction_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
USING DELTA
PARTITIONED BY (transaction_date)
TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = 'true',
    'delta.autoOptimize.autoCompact' = 'true'
);

-- Show tables
SHOW TABLES IN sales_catalog.raw_data;

-- Describe table
DESCRIBE TABLE EXTENDED sales_catalog.raw_data.transactions;

-- Show table history
DESCRIBE HISTORY sales_catalog.raw_data.transactions;
```

## Integration with Other Services

### MLflow Integration
```python
# Register model in Unity Catalog
import mlflow

model_name = "my_catalog.my_schema.my_model"
model_version = mlflow.register_model(
    model_uri="runs:/run-id/model",
    name=model_name
)
```

### Delta Sharing
```sql
-- Create share
CREATE SHARE my_share
COMMENT 'Sales data share';

-- Add table to share
ADD TABLE my_catalog.my_schema.sales TO SHARE my_share;

-- Create recipient
CREATE RECIPIENT customer_recipient
USING ID 'recipient-uuid'
COMMENT 'External customer recipient';
```

## System Tables

Unity Catalog provides system tables for monitoring and governance:

### Information Schema
```sql
-- Table information
SELECT * FROM system.information_schema.tables
WHERE catalog_name = 'my_catalog';

-- Column information
SELECT * FROM system.information_schema.columns
WHERE table_catalog = 'my_catalog';

-- Function information
SELECT * FROM system.information_schema.routines
WHERE routine_catalog = 'my_catalog';
```

### Access Tables
```sql
-- Audit logs
SELECT * FROM system.access.audit
WHERE event_date >= current_date() - 7;

-- Billing usage
SELECT * FROM system.billing.usage
WHERE usage_date >= current_date() - 30;
```

## Troubleshooting Common Issues

### Permission Errors
```sql
-- Check user permissions
SHOW GRANTS ON CATALOG my_catalog FOR USER 'user@company.com';

-- Check current user
SELECT current_user();

-- Check group membership
SELECT is_member('my-group');
```

### Storage Access Issues
```sql
-- Test external location access
LIST '/external-location/path/';

-- Check storage credential
DESCRIBE STORAGE CREDENTIAL my_credential;
```

### Performance Issues
```sql
-- Check table statistics
ANALYZE TABLE my_catalog.my_schema.my_table COMPUTE STATISTICS;

-- Optimize table
OPTIMIZE my_catalog.my_schema.my_table;

-- Check table properties
SHOW TBLPROPERTIES my_catalog.my_schema.my_table;
```

## Certification Focus Areas

### For Data Engineer Associate/Professional
- Unity Catalog object hierarchy and navigation
- Table and schema creation and management
- Security and access control basics
- External location and storage credential setup
- Data pipeline integration with Unity Catalog

### For Data Analyst Associate
- Querying across catalogs and schemas
- Understanding three-part naming
- Basic security concepts
- Working with views and functions
- Data discovery and exploration

### For Machine Learning Associate/Professional
- Model registration and versioning
- Feature store integration
- ML pipeline governance
- Model deployment with Unity Catalog
- Experiment tracking integration

## Quick Reference

### Essential Commands
```sql
-- Navigation
USE CATALOG my_catalog;
USE SCHEMA my_catalog.my_schema;

-- Object creation
CREATE CATALOG catalog_name;
CREATE SCHEMA catalog.schema_name;
CREATE TABLE catalog.schema.table_name (...);

-- Permissions
GRANT privilege ON object TO principal;
REVOKE privilege ON object FROM principal;
SHOW GRANTS ON object;

-- Information
SHOW CATALOGS;
SHOW SCHEMAS IN catalog_name;
SHOW TABLES IN catalog_name.schema_name;
DESCRIBE object_name;
```

### Common Patterns
```sql
-- Three-part naming
SELECT * FROM catalog.schema.table;

-- Cross-catalog queries
SELECT a.*, b.name 
FROM catalog1.schema1.table1 a
JOIN catalog2.schema2.table2 b ON a.id = b.id;

-- Secure view pattern
CREATE VIEW secure_data AS
SELECT 
    id,
    CASE WHEN is_member('admin') THEN sensitive_column 
         ELSE 'REDACTED' 
    END as sensitive_column
FROM raw_data;
```