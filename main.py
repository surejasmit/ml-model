from fastapi import FastAPI
import joblib
import os
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(model_path)

@app.get("/")
def read_root():
    return {"message": "ML API running !"}

@app.post("/predict")
def predict(data: dict):
    features = [[data["feature1"], data["feature2"]]]
    prediction = model.predict(features)
    return {"prediction": prediction[0]}