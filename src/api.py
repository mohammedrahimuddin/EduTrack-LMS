
import joblib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.config import RISK_MODEL_PATH
from src.train import main as train_model


app = FastAPI(
    title="EduTrack LMS - At-Risk Prediction API",
    version="2.0.0"
)


class PredictionRequest(BaseModel):
    lessons_completed: int = Field(..., ge=0)
    avg_time_per_lesson_mins: float = Field(..., ge=0)
    quiz_attempts: int = Field(..., ge=0)
    streak_days: int = Field(..., ge=0)


def get_model():
    if not RISK_MODEL_PATH.exists():
        raise HTTPException(
            status_code=503,
            detail="Risk model not trained. Run python -m src.train"
        )

    return joblib.load(RISK_MODEL_PATH)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_ready": RISK_MODEL_PATH.exists()
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    model = get_model()

    try:
        features = [[
            request.lessons_completed,
            request.avg_time_per_lesson_mins,
            request.quiz_attempts,
            request.streak_days
        ]]

        prediction = int(model.predict(features)[0])

        probabilities = model.predict_proba(features)[0]
        risk_index = list(model.classes_).index(1)
        risk_score = float(probabilities[risk_index])

        return {
            "prediction": prediction,
            "risk_label": (
                "At Risk" if prediction == 1 else "Not At Risk"
            ),
            "risk_probability": round(risk_score, 4)
        }

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )


@app.post("/retrain")
def retrain():
    try:
        train_model()

        return {
            "status": "completed",
            "message": "At-risk prediction model retrained successfully"
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )
