from pydantic import BaseModel


class Data(BaseModel):
    id: str = 123
    data: list = [[6,148,72,35,0,33.6,0.627,50]]
    columns: list = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
