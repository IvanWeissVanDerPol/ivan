# MLflow - Comprehensive Study Guide for Databricks Certifications

## Overview
MLflow is an open source platform for developing models and generative AI applications on Databricks. It provides tools for the complete machine learning lifecycle including tracking, models, model registry, and AI agent evaluation.

## Core Components

### 1. Tracking
- **Experiment management** - Track experiments to record and compare parameters and results
- **Run logging** - Log parameters, metrics, and artifacts
- **Comparison capabilities** - Compare different runs and experiments
- **Version control** - Track code versions and data lineage

### 2. Models
- **Standardized format** - Package ML models for deployment
- **Multi-framework support** - Works with various ML libraries
- **Deployment flexibility** - Deploy to various serving platforms
- **Model artifacts** - Store model files, dependencies, and metadata

### 3. Model Registry
- **Centralized repository** - Manage model deployment process
- **Version management** - Track model versions
- **Staging workflow** - Move models from staging to production
- **Annotation capabilities** - Add descriptions and tags

### 4. AI Agent Evaluation and Tracing
- **Agent development** - Build high-quality AI agents
- **Performance evaluation** - Compare and assess agents
- **Troubleshooting** - Debug agent behavior
- **Request tracing** - Track inputs, outputs, and metadata

## MLflow 3 on Databricks

### Key Features

#### Logged Models
- **Lifecycle tracking** - Persist model information throughout lifecycle
- **Cross-environment** - Track across development, staging, production
- **Artifact linking** - Connect metadata, metrics, parameters, and code
- **Model comparison** - Compare performance across models

```python
import mlflow

# Log a model
with mlflow.start_run():
    model = train_model(data)
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_param("max_depth", 10)
```

#### Deployment Jobs
- **Lifecycle management** - Manage evaluation, approval, deployment
- **Unity Catalog governance** - Governed by Unity Catalog
- **Activity logging** - All events saved to activity log
- **Workflow orchestration** - Automated deployment pipelines

### Enhanced Tracking Capabilities

#### Experiment Organization
```python
# Set experiment
mlflow.set_experiment("/Shared/my-experiment")

# Start run with context manager
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("rmse", 0.786)
    mlflow.log_artifact("model.pkl")
```

#### Auto-logging
```python
# Enable autolog for scikit-learn
mlflow.sklearn.autolog()

# Train model - metrics automatically logged
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)
```

## Working with Models

### Model Formats
MLflow supports multiple model formats:

```python
# Scikit-learn
mlflow.sklearn.log_model(model, "model")

# TensorFlow
mlflow.tensorflow.log_model(model, "model")

# PyTorch
mlflow.pytorch.log_model(model, "model")

# Custom Python function
mlflow.pyfunc.log_model(model, "model")

# Spark MLlib
mlflow.spark.log_model(model, "model")
```

### Model Signatures
```python
from mlflow.models.signature import infer_signature

# Infer signature from training data
signature = infer_signature(X_train, predictions)

# Log model with signature
mlflow.sklearn.log_model(
    model, 
    "model",
    signature=signature
)
```

### Model Loading
```python
# Load as original framework
model = mlflow.sklearn.load_model("runs:/run-id/model")

# Load as PyFunc (universal interface)
model = mlflow.pyfunc.load_model("runs:/run-id/model")

# Load from model registry
model = mlflow.pyfunc.load_model("models:/MyModel/Production")
```

## Model Registry with Unity Catalog

### Model Registration
```python
# Register model from run
model_uri = f"runs:/{run_id}/model"
model_version = mlflow.register_model(
    model_uri=model_uri,
    name="my-model"
)

# Register directly during logging
mlflow.sklearn.log_model(
    model,
    "model",
    registered_model_name="my-model"
)
```

### Model Versioning
```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# List model versions
versions = client.search_model_versions("name='my-model'")

# Get specific version
version = client.get_model_version("my-model", version="1")

# Update version stage
client.transition_model_version_stage(
    name="my-model",
    version="1",
    stage="Production"
)
```

### Model Stages
- **None** - Initial stage
- **Staging** - Pre-production testing
- **Production** - Live deployment
- **Archived** - Retired models

### Model Aliases (New in MLflow 2.9+)
```python
# Set alias for model version
client.set_registered_model_alias(
    name="my-model",
    alias="champion",
    version="3"
)

# Load model by alias
model = mlflow.pyfunc.load_model("models:/my-model@champion")
```

## Experiment Tracking

### Basic Tracking
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

# Set tracking URI (optional on Databricks)
# mlflow.set_tracking_uri("databricks")

# Set experiment
experiment = mlflow.set_experiment("/Shared/my-experiment")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    
    # Train model
    model = RandomForestRegressor(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Log metrics
    mlflow.log_metric("mse", mean_squared_error(y_test, predictions))
    mlflow.log_metric("r2", r2_score(y_test, predictions))
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Log artifacts
    mlflow.log_artifact("feature_importance.png")
```

### Advanced Tracking

#### Nested Runs
```python
with mlflow.start_run():
    mlflow.log_param("algorithm", "hyperparameter_tuning")
    
    for alpha in [0.1, 0.5, 1.0]:
        with mlflow.start_run(nested=True):
            mlflow.log_param("alpha", alpha)
            model = Ridge(alpha=alpha)
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            mlflow.log_metric("score", score)
```

#### Custom Metrics
```python
# Log multiple metrics
mlflow.log_metrics({
    "training_score": train_score,
    "validation_score": val_score,
    "test_score": test_score
})

# Log metric with step (for iterative algorithms)
for epoch in range(10):
    loss = train_epoch()
    mlflow.log_metric("loss", loss, step=epoch)
```

#### Artifacts and Files
```python
# Log single file
mlflow.log_artifact("model_summary.txt")

# Log directory
mlflow.log_artifacts("charts/", artifact_path="visualizations")

# Log figure
import matplotlib.pyplot as plt
plt.savefig("plot.png")
mlflow.log_artifact("plot.png")

# Log text
mlflow.log_text("Model description", "model_info.txt")

# Log dict as JSON
mlflow.log_dict({"hyperparameters": params}, "config.json")
```

## AI Agent Development and Tracing

### MLflow Tracing
```python
import mlflow

# Enable tracing
mlflow.llms.enable_traces()

# Trace agent execution
@mlflow.trace
def agent_function(query):
    # Agent logic here
    response = process_query(query)
    return response

# Manual tracing
with mlflow.start_trace(name="agent_request") as trace:
    response = agent_function("What is the weather?")
    trace.log_outputs({"response": response})
```

### Agent Evaluation
```python
from mlflow.models import evaluate

# Evaluate agent
results = evaluate(
    data=evaluation_dataset,
    model=agent_model,
    evaluators=["default", "bleu", "rouge"],
    model_type="question-answering"
)
```

## Model Serving Integration

### Deploy Models
```python
# Deploy registered model
import requests

# Model serving endpoint
endpoint_url = "https://workspace.databricks.com/model/my-model/Production/invocations"

# Make prediction request
response = requests.post(
    endpoint_url,
    headers={"Authorization": f"Bearer {token}"},
    json={"dataframe_split": {"columns": columns, "data": data}}
)
```

### A/B Testing
```python
# Deploy multiple model versions
# Traffic splitting handled by Databricks Model Serving
# Metrics automatically tracked in MLflow
```

## Best Practices

### 1. Experiment Organization
```python
# Use hierarchical naming
experiment_name = "/Shared/project-name/model-type/timestamp"
mlflow.set_experiment(experiment_name)

# Use descriptive run names
with mlflow.start_run(run_name="rf_hyperparameter_tuning"):
    pass

# Add tags for filtering
mlflow.set_tag("team", "data-science")
mlflow.set_tag("project", "customer-churn")
```

### 2. Model Documentation
```python
# Use model signatures
signature = infer_signature(X_train, predictions)

# Add model description
mlflow.sklearn.log_model(
    model,
    "model",
    signature=signature,
    metadata={
        "description": "Random Forest model for customer churn prediction",
        "training_data_version": "v1.2",
        "feature_engineering_version": "v2.1"
    }
)
```

### 3. Reproducibility
```python
# Log environment
mlflow.log_artifact("requirements.txt")

# Log code
mlflow.log_artifact("training_script.py")

# Use consistent random seeds
mlflow.log_param("random_seed", 42)
```

### 4. Performance Monitoring
```python
# Log comprehensive metrics
mlflow.log_metrics({
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1_score": f1,
    "auc_roc": auc_roc,
    "training_time": training_time,
    "inference_time": inference_time
})
```

## Integration with Unity Catalog

### Governance Features
- **Access control** - Fine-grained permissions
- **Lineage tracking** - Data and model lineage
- **Cross-workspace access** - Share models across workspaces
- **Audit logging** - Track all model operations

### Model Governance
```python
# Models automatically inherit UC permissions
# Access controlled by UC grants
# Lineage automatically tracked
```

## Common Patterns

### Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10]
}

with mlflow.start_run():
    mlflow.log_param("tuning_method", "grid_search")
    
    for params in ParameterGrid(param_grid):
        with mlflow.start_run(nested=True):
            mlflow.log_params(params)
            
            model = RandomForestRegressor(**params)
            model.fit(X_train, y_train)
            
            score = model.score(X_test, y_test)
            mlflow.log_metric("score", score)
            
            if score > best_score:
                best_score = score
                mlflow.sklearn.log_model(model, "model")
```

### Model Comparison
```python
# Compare multiple algorithms
algorithms = {
    "random_forest": RandomForestRegressor(),
    "gradient_boost": GradientBoostingRegressor(),
    "linear_regression": LinearRegression()
}

for name, model in algorithms.items():
    with mlflow.start_run(run_name=f"{name}_baseline"):
        mlflow.log_param("algorithm", name)
        
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        mlflow.sklearn.log_model(model, "model")
```

### Feature Engineering Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

with mlflow.start_run():
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor())
    ])
    
    # Log pipeline parameters
    mlflow.log_param("preprocessing", "standard_scaler")
    mlflow.log_param("model_type", "random_forest")
    
    # Train pipeline
    pipeline.fit(X_train, y_train)
    
    # Log entire pipeline
    mlflow.sklearn.log_model(pipeline, "pipeline")
```

## Troubleshooting Common Issues

### 1. Large Models
```python
# For large models, use model artifacts
mlflow.log_artifact("large_model.pkl")

# Or use cloud storage
model_path = "s3://my-bucket/models/model.pkl"
mlflow.log_param("model_path", model_path)
```

### 2. Custom Dependencies
```python
# Log conda environment
mlflow.sklearn.log_model(
    model,
    "model",
    conda_env="conda_env.yaml"
)

# Or specify pip requirements
mlflow.sklearn.log_model(
    model,
    "model",
    pip_requirements=["scikit-learn==1.0.0", "pandas==1.3.0"]
)
```

### 3. Memory Issues
```python
# For large datasets, log only essential metrics
# Use model checkpointing for iterative training
# Consider using Databricks ML Runtime optimizations
```

## Certification Focus Areas

### For Data Engineer Associate/Professional
- MLflow integration with data pipelines
- Model lifecycle management
- Experiment tracking for batch processing
- Integration with Unity Catalog

### For Machine Learning Associate/Professional
- Complete MLflow workflow
- Model registry operations
- Experiment management
- Model deployment patterns
- A/B testing strategies

### For Generative AI Engineer Associate
- AI agent development with MLflow
- Tracing and evaluation
- LLM model management
- Agent deployment patterns

## Quick Reference

### Essential Commands
```python
# Experiment management
mlflow.set_experiment("/Shared/experiment")
mlflow.start_run()
mlflow.end_run()

# Logging
mlflow.log_param("param", value)
mlflow.log_metric("metric", value)
mlflow.log_artifact("file.txt")
mlflow.sklearn.log_model(model, "model")

# Model registry
mlflow.register_model(model_uri, "model_name")
mlflow.pyfunc.load_model("models:/model_name/Production")

# Client operations
from mlflow.tracking import MlflowClient
client = MlflowClient()
client.get_experiment_by_name("experiment_name")
client.list_registered_models()
```

### Common Patterns
```python
# Complete workflow
with mlflow.start_run():
    # Log hyperparameters
    mlflow.log_params(hyperparams)
    
    # Train model
    model = train_model(data, hyperparams)
    
    # Evaluate model
    metrics = evaluate_model(model, test_data)
    mlflow.log_metrics(metrics)
    
    # Log model
    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="my_model"
    )
```