from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from schemas import InputData, PredictionResult

app = FastAPI(
    title="Japan Electricity Consumption API",
    description="API for predicting residential and industrial electricity consumption in Japan",
    version="1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
pipeline_res = joblib.load("./models/pipeline_res.pkl")
pipeline_ind = joblib.load("./models/pipeline_ind.pkl")

@app.post("/predict/residential", response_model=PredictionResult)
def predict_residential(data: InputData):
    df = pd.DataFrame([data.dict()])
    prediction = pipeline_res.predict(df)[0]
    return {"prediction_kwh": round(prediction, 2)}

@app.post("/predict/industrial", response_model=PredictionResult)
def predict_industrial(data: InputData):
    df = pd.DataFrame([data.dict()])
    prediction = pipeline_ind.predict(df)[0]
    return {"prediction_kwh": round(prediction, 2)}

