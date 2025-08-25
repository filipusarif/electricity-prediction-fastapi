from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from schemas import InputData, PredictionResult
import base64
import matplotlib.pyplot as plt
import io

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

@app.post("/visualize/residential/forecast")
def forecast_residential_base64(data: InputData):
    years = list(range(data.Year, data.Year + 10))
    df = pd.DataFrame({
        "Region": data.Region,
        "Year": years,
        "Intensity": data.Intensity,
        "NominalPrice": data.NominalPrice,
        "RealPrice": data.RealPrice
    })
    predictions = pipeline_res.predict(df)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(years, predictions, marker='o')
    ax.set_title("Prediksi 10 Tahun Konsumsi Residential")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Konsumsi (KWh)")
    plt.tight_layout()

    # Save to buffer and encode
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image_base64": img_base64}

@app.post("/visualize/industrial/forecast")
def forecast_industrial_base64(data: InputData):
    years = list(range(data.Year, data.Year + 10))
    df = pd.DataFrame({
        "Region": data.Region,
        "Year": years,
        "Intensity": data.Intensity,
        "NominalPrice": data.NominalPrice,
        "RealPrice": data.RealPrice
    })
    predictions = pipeline_res.predict(df)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(years, predictions, marker='o')
    ax.set_title("Prediksi 10 Tahun Konsumsi Industrial")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Konsumsi (KWh)")
    plt.tight_layout()

    # Save to buffer and encode
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image_base64": img_base64}

@app.post("/visualize/residential/price-sensitivity")
def price_sensitivity_residential_base64(data: InputData):
    harga_range = list(range(int(data.RealPrice) - 50, int(data.RealPrice) + 60, 10))
    df = pd.DataFrame({
        "Region": data.Region,
        "Year": data.Year,
        "Intensity": data.Intensity,
        "NominalPrice": data.NominalPrice,
        "RealPrice": harga_range
    })
    predictions = pipeline_res.predict(df)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(harga_range, predictions, marker='s', color='green')
    ax.set_title("Sensitivitas Terhadap Harga Riil (Residential)")
    ax.set_xlabel("Real Price")
    ax.set_ylabel("Konsumsi (KWh)")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image_base64": img_base64}

@app.post("/visualize/industrial/price-sensitivity")
def price_sensitivity_industrial_base64(data: InputData):
    harga_range = list(range(int(data.RealPrice) - 50, int(data.RealPrice) + 60, 10))
    df = pd.DataFrame({
        "Region": data.Region,
        "Year": data.Year,
        "Intensity": data.Intensity,
        "NominalPrice": data.NominalPrice,
        "RealPrice": harga_range
    })
    predictions = pipeline_res.predict(df)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(harga_range, predictions, marker='s', color='green')
    ax.set_title("Sensitivitas Terhadap Harga Riil (Industrial)")
    ax.set_xlabel("Real Price")
    ax.set_ylabel("Konsumsi (KWh)")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image_base64": img_base64}