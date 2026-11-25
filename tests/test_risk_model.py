import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.train import FEATURES, TARGET


def sample_data():
    return pd.DataFrame({
        "lessons_completed": [5, 10, 15, 20, 25, 30, 35, 40],
        "avg_time_per_lesson_mins": [10, 15, 20, 25, 30, 35, 40, 45],
        "quiz_attempts": [1, 2, 2, 3, 4, 4, 5, 6],
        "streak_days": [1, 3, 5, 8, 12, 18, 24, 30],
        "label_at_risk": [1, 1, 1, 1, 0, 0, 0, 0]
    })


def test_model_training():
    data = sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(data[FEATURES], data[TARGET])

    assert hasattr(model, "predict")


def test_prediction_output():
    data = sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(data[FEATURES], data[TARGET])

    prediction = model.predict(data[FEATURES])

    assert len(prediction) == len(data)
    assert set(prediction).issubset({0, 1})


def test_prediction_probability():
    data = sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model.fit(data[FEATURES], data[TARGET])

    probabilities = model.predict_proba(data[FEATURES])

    assert probabilities.shape == (len(data), 2)
    assert ((probabilities >= 0) & (probabilities <= 1)).all()