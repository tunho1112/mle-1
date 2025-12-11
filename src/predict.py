import pandas as pd 
import numpy as np
import logging
import mlflow
import time


class ModelPredictor:
    def __init__(
        self,
        mlflow_uri: str = "http://0.0.0.0:5000",
        experiment_name: str = "diabetes_model_xgb",
        model_name: str = "xgb",
        model_version: str = "1"
    ):
        self.mlflow_uri = mlflow_uri
        self.experiment_name = experiment_name
        self.model_name = model_name
        self.model_version = model_version

    def predict(self, df:np.ndarray):
        start_time = time.time()
        mlflow.set_tracking_uri(self.mlflow_uri)
        model_uri = f"models:/{self.model_name}/{self.model_version}"
        self.model = mlflow.sklearn.load_model(model_uri)
        logging.info(f"model loaded from {model_uri}")
        y_pred = self.model.predict(df)
        end_pred = time.time()
        logging.info(f"predict time: {end_pred-start_time}")
        return y_pred.tolist()

if __name__ == "__main__":
    val = pd.read_csv("data/val.csv")
    predictor = ModelPredictor(
        mlflow_uri="http://localhost:5000",
        experiment_name="diabetes_model_xgb",
        model_name="xgb",
        model_version="1"
    )
    val_X = val.drop(columns=['Outcome'])
    val_y = val['Outcome']
    y_pred = predictor.predict(val_X)
    print(y_pred)