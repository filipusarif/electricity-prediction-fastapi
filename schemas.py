from pydantic import BaseModel

class InputData(BaseModel):
    Region: int
    Year: int
    Intensity: float
    NominalPrice: float
    RealPrice: float

class PredictionResult(BaseModel):
    prediction_kwh: float
