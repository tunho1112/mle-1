import os
import joblib
import pandas as pd



model = joblib.load(os.environ.get("MODEL_PATH", "models/diabetes_model.pkl"))
scaler = joblib.load(os.environ.get("SCALER_PATH", "models/scaler.pkl"))


data =  {
            "id": "123",
            "data": [[6,148,72,35,0,33.6,0.627,50]],
            "columns": ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
        }

df = pd.DataFrame(data["data"], columns=data["columns"])
df = scaler.transform(df)
y_pred = model.predict(df)
print(y_pred)