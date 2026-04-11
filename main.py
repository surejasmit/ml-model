from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def read_root():
    return {"message": "ML API running !"}

@app.post("/predict")
def predict(data: dict):
    features = [[data["feature1"], data["feature2"]]]
    prediction = model.predict(features)
    return {"prediction": prediction[0]}