# 🚀 Builde MLOPs for Prediction ML System
This project aims to build a full MLOps pipeline for a machine learning prediction system, focusing on diabetes prediction. It covers the steps from data processing, model training, evaluation, and deployment, to automating workflows with best practices. The goal is to demonstrate a robust, reproducible, and scalable approach to operationalizing ML models in production environments.\


## 📑 Table of Contents
- [📊 Dataset](#-dataset)
- [🌐 Architecture Overview](#-architecture-overview)
  - [1. Develop Model](#1-develop-model)
  - [2. Web API](#2-web-api)

- [📖 Details](#-details)


## 🛠️ Prerequisite
To get started with this project, please ensure you have the following installed:
- Python 3.9 
- `miniconda`, `docker` installed

Install the required dependencies using the following command:

## 📊 Dataset
> Onset of Diabetes Prediction
Link: [data](https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/)

This dataset is comprised of 8 input variables that describe medical details of patients and one output variable to indicate whether the patient will have an onset of diabetes within 5 years.
You can learn more about this dataset on the UCI Machine Learning Repository website.

## 1. Develop Model


```bash
conda create -n mle1 python=3.9
conda activate mle1
pip install -r requirements.txtProcessing Data
```
Setting up MLflow Tracking Server with Docker
```bash
docker compose -f deployment/mlflow/docker-compose.yml up -d
```
- The tracking server will be available at: [http://localhost:5000](http://localhost:5000)
![mlflow](images/mlflow_dashboard.png)

### Development model:
Run the following command to process your dataset:
```bash
python src/split_data.py
```
Training model and push model to model registry [http://localhost:5000](http://localhost:5000)

```bash
python src/train.py --model_name xgb # with xgb model
```
![](images/mlflow_model.png)

### Prediction Model
You can use the trained and registered model for prediction by loading it from the MLflow

Example usage:

```bash
python src/predict.py
```
This will:
- Load the saved model from the MLflow registry (using the default config or the one you provide in the script).
- Run predictions using the validation dataset (`data/val.csv`).
You can specify different model names or versions by editing the script or updating the CLI options inside `src/predict.py`:

## 2. Web API
To run the RESTful API service using FastAPI and Uvicorn in `src/main.py`, use the following command:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8080
```
The service will be available at [http://localhost:8080](http://localhost:8080).
![](images/web_api.png)
#### 📖 API Endpoints
- **POST /predict**  
  - Runs inference using the loaded model.
  - Expects a JSON payload containing:
    - `id`: (string or int) input id/reference
    - `data`: list of lists (rows of feature values)
    - `columns`: list of column names (feature names)

  - Example request:
    ```json
    {
      "id": "123",
      "data": [[6,148,72,35,0,33.6,0.627,50]],
      "columns": ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
    }
    ```
  - Example using `curl`:
    ```bash
    curl -X POST "http://localhost:8080/predict" \
         -H "Content-Type: application/json" \
         -d '{
              "id": "123",
              "data": [[6,148,72,35,0,33.6,0.627,50]],
              "columns": ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
            }'
    ```

  - Example response:
    ```json
    {
      "id": "123",
      "predictions": [1]
    }
    ```

#### 🔧 Observability & Monitoring

- The API integrates with Prometheus for metrics (available at `:8099/metrics`).
- Distributed tracing is enabled with Jaeger (default host: `jaeger:6831`).

### ▶️ Running the API

If you are using Docker, the API will be exposed at `http://localhost:8080`.

Otherwise, you can run locally for development:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8080
```

See `src/main.py` for detailed implementation and configuration options.
