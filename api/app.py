from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn risk based on customer and experience data.",
    version="1.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"

model = joblib.load(MODEL_PATH)


class CustomerInput(BaseModel):
    CreditScore: float
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    nps_score: int
    customer_effort_score: int
    satisfaction_score: int
    interaction_channel: str
    complaint_flag: int


def categorize_nps(score: int) -> str:
    if score >= 9:
        return "Promoter"
    elif score >= 7:
        return "Passive"
    return "Detractor"


def risk_segment(score: float) -> str:
    if score >= 0.7:
        return "High risk"
    elif score >= 0.4:
        return "Medium risk"
    return "Low risk"


@app.get("/")
def root():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
def predict(customer: CustomerInput):
    input_dict = customer.dict()

    input_dict["nps_category"] = categorize_nps(input_dict["nps_score"])
    input_dict["low_satisfaction_flag"] = int(input_dict["satisfaction_score"] <= 2)
    input_dict["high_effort_flag"] = int(input_dict["customer_effort_score"] >= 4)

    input_df = pd.DataFrame([input_dict])

    churn_probability = float(model.predict_proba(input_df)[:, 1][0])
    predicted_class = int(model.predict(input_df)[0])

    return {
        "churn_probability": round(churn_probability, 4),
        "predicted_churn": predicted_class,
        "risk_segment": risk_segment(churn_probability)
    }