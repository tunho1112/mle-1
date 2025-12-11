# Plan: Diabetes Onset Prediction Service with FastAPI

## Project Overview
Build an AI prediction service for predicting the onset of diabetes using XGBoost and FastAPI.
The service accepts patient health data and predicts the likelihood of diabetes onset.

## Project Structure
```
mle-1/
├── models/              # Save trained models
│   └── diabetes_model.pkl
├── src/                 # Source code
│   ├── __init__.py
│   ├── main.py         # FastAPI application
│   ├── model.py        # Model loading and prediction logic
│   ├── schemas.py      # Pydantic schemas for API
│   └── utils.py        # Utility functions (data preprocessing)
├── data/               # Save training and test data
│   ├── train/
│   │   └── diabetes.csv
│   ├── test/
│   │   └── diabetes.csv
│   └── raw/            # Raw data before preprocessing
├── notebooks/          # Jupyter notebooks for exploration
│   └── model_training.ipynb
├── requirements.txt    # Python dependencies
├── README.md
└── plan.md
```

## Implementation Steps

### Phase 1: Data Preparation
1. **Data Collection**
   - Use Pima Indians Diabetes Dataset or similar diabetes dataset
   - Features typically include: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
   - Target variable: Outcome (0 = No diabetes, 1 = Diabetes)
   - Split data into train/test sets (80/20 or 70/30)
   - Store data in CSV format in `data/train/` and `data/test/`

2. **Data Preprocessing**
   - Handle missing values
   - Feature scaling/normalization if needed
   - Handle outliers
   - Create data loaders for training and validation

### Phase 2: Model Development
1. **Model Selection**
   - **Algorithm**: XGBoost (Gradient Boosting)
   - Use XGBoost for binary classification
   - Optimize hyperparameters (learning_rate, max_depth, n_estimators, etc.)

2. **Model Training**
   - Implement training script in Jupyter notebook or Python script
   - Train XGBoost model on training data
   - Validate on test data
   - Save trained model to `models/diabetes_model.pkl` (pickle format)
   - Evaluate model performance (accuracy, precision, recall, F1-score, ROC-AUC)

3. **Model Evaluation**
   - Generate confusion matrix
   - Calculate classification metrics
   - Feature importance analysis
   - Document model metrics

### Phase 3: FastAPI Service Development
1. **Setup FastAPI Application** (`src/main.py`)
   - Create FastAPI app instance
   - Define health check endpoint
   - Configure CORS if needed

2. **Create Schemas** (`src/schemas.py`)
   - Define request/response models using Pydantic
   - Input: Patient health data (JSON with features)
   - Output: Prediction result (diabetes probability, prediction class)

3. **Model Loading** (`src/model.py`)
   - Load saved XGBoost model from `models/` directory
   - Implement prediction function
   - Handle data preprocessing for inference

4. **API Endpoints** (`src/main.py`)
   - `POST /predict`: Accept patient data and return diabetes prediction
   - `GET /health`: Health check endpoint
   - `GET /`: API documentation/info

5. **Data Processing** (`src/utils.py`)
   - Function to preprocess input data
   - Feature validation and transformation
   - Handle data format conversion

### Phase 4: Testing
1. **Unit Tests**
   - Test model loading
   - Test data preprocessing functions
   - Test prediction logic

2. **API Tests**
   - Test prediction endpoint with sample patient data
   - Test error handling (invalid data, missing fields, etc.)
   - Test health check endpoint

3. **Integration Tests**
   - End-to-end testing of the service

### Phase 5: Documentation & Deployment
1. **Documentation**
   - Update README.md with setup instructions
   - Document API endpoints
   - Add example usage

2. **Dependencies** (`requirements.txt`)
   - FastAPI
   - Uvicorn (ASGI server)
   - XGBoost (ML model)
   - scikit-learn (for preprocessing and metrics)
   - pandas (data handling)
   - NumPy
   - Pydantic
   - python-multipart (for file uploads if needed)

3. **Deployment Preparation**
   - Create Dockerfile (optional)
   - Create docker-compose.yml (optional)
   - Configure environment variables

## Technical Stack
- **Framework**: FastAPI
- **ML Framework**: XGBoost
- **Data Processing**: pandas, NumPy, scikit-learn
- **API Server**: Uvicorn
- **Validation**: Pydantic

## API Endpoints Design

### POST /predict
- **Description**: Predict diabetes onset based on patient health data
- **Request**: JSON with patient features
  ```json
  {
    "pregnancies": 6,
    "glucose": 148,
    "blood_pressure": 72,
    "skin_thickness": 35,
    "insulin": 0,
    "bmi": 33.6,
    "diabetes_pedigree_function": 0.627,
    "age": 50
  }
  ```
- **Response**: 
  ```json
  {
    "prediction": 1,
    "prediction_label": "Diabetes",
    "probability": 0.85,
    "probabilities": {
      "no_diabetes": 0.15,
      "diabetes": 0.85
    }
  }
  ```

### GET /health
- **Description**: Health check endpoint
- **Response**: 
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

## Feature Description
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: Diabetes pedigree function
- **Age**: Age in years

## Success Criteria
- [ ] Model achieves >75% accuracy on test set
- [ ] FastAPI service successfully loads model
- [ ] API endpoint accepts patient data and returns predictions
- [ ] Service handles errors gracefully
- [ ] Code is well-structured and documented
- [ ] Tests pass successfully

## Timeline Estimate
- Phase 1 (Data Preparation): 1 day
- Phase 2 (Model Development): 2-3 days
- Phase 3 (FastAPI Service): 1-2 days
- Phase 4 (Testing): 1 day
- Phase 5 (Documentation & Deployment): 1 day

**Total**: ~6-8 days
