
import json
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from src.config import (
    PROCESSED_DIR,
    ARTIFACT_DIR,
    RISK_MODEL_PATH,
    RISK_METRICS_PATH,
    RISK_SUMMARY_PATH,
    RANDOM_STATE,
)


FEATURES = [
    "lessons_completed",
    "avg_time_per_lesson_mins",
    "quiz_attempts",
    "streak_days",
]

TARGET = "label_at_risk"


def main():
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    train_path = PROCESSED_DIR / "risk_dataset.csv"
    test_path = PROCESSED_DIR / "risk_test_dataset.csv"

    if not train_path.exists() or not test_path.exists():
        raise FileNotFoundError(
            "Processed datasets not found. "
            "Run the data processing script first."
        )

    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    X_train = train_data[FEATURES]
    y_train = train_data[TARGET]

    X_test = test_data[FEATURES]
    y_test = test_data[TARGET]

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        min_samples_leaf=3,
        class_weight="balanced",
        random_state=RANDOM_STATE,
    )

    print("Training At-Risk Prediction Model...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "precision": round(
            float(precision_score(y_test, predictions, zero_division=0)), 4
        ),
        "recall": round(
            float(recall_score(y_test, predictions, zero_division=0)), 4
        ),
        "f1_score": round(
            float(f1_score(y_test, predictions, zero_division=0)), 4
        ),
        "test_cases": int(len(y_test)),
        "confusion_matrix": confusion_matrix(
            y_test, predictions, labels=[0, 1]
        ).tolist(),
    }

    joblib.dump(model, RISK_MODEL_PATH)

    RISK_METRICS_PATH.write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8",
    )

    summary = {
        "model": "RandomForestClassifier",
        "training_records": int(len(train_data)),
        "independent_test_records": int(len(test_data)),
        "features": FEATURES,
        "target": TARGET,
        "metrics": metrics,
        "classification_report": classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=["Not At Risk", "At Risk"],
            output_dict=True,
            zero_division=0,
        ),
    }

    RISK_SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    print("\nMODEL TRAINING COMPLETED")
    print("-" * 40)
    print(json.dumps(metrics, indent=2))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=["Not At Risk", "At Risk"],
            zero_division=0,
        )
    )

    print("\nMODEL SAVED:", RISK_MODEL_PATH)
    print("METRICS SAVED:", RISK_METRICS_PATH)
    print("SUMMARY SAVED:", RISK_SUMMARY_PATH)


if __name__ == "__main__":
    main()
