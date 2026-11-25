
from pathlib import Path
import json

import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"

PERFORMANCE_FILE = "aiml_student_performance.csv"
ENGAGEMENT_FILE = "aiml_content_engagement.csv"
TEST_FILE = "aiml_edtech_tests.json"


# --------------------------------------------------
# REQUIRED COLUMNS
# --------------------------------------------------

PERFORMANCE_COLUMNS = [
    "student_id",
    "grade",
    "subject",
    "pre_test_score",
    "post_test_score",
    "score_improvement",
    "lessons_completed",
    "total_lessons",
    "completion_pct",
    "avg_time_per_lesson_mins",
    "quiz_attempts",
    "best_quiz_score",
    "streak_days",
    "platform_sessions",
    "device",
    "label_at_risk",
]

ENGAGEMENT_COLUMNS = [
    "engagement_id",
    "student_id",
    "content_type",
    "subject",
    "date",
    "time_spent_mins",
    "completed",
    "replayed",
    "paused_count",
    "liked",
    "notes_taken",
    "difficulty_rating",
    "engagement_score",
]

TEST_FEATURES = [
    "lessons_completed",
    "avg_time_per_lesson_mins",
    "quiz_attempts",
    "streak_days",
]

TARGET_COLUMN = "label_at_risk"


# --------------------------------------------------
# COMMON VALIDATION
# --------------------------------------------------

def validate_columns(df, required_columns, filename):
    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(
            f"{filename} is missing required columns: {sorted(missing)}"
        )


def validate_student_data(df, filename):
    if df.empty:
        raise ValueError(f"{filename} contains no records.")

    if df["student_id"].isna().any():
        raise ValueError(f"{filename} contains missing student IDs.")

    if df["subject"].isna().any():
        raise ValueError(f"{filename} contains missing subjects.")


# --------------------------------------------------
# LOAD STUDENT PERFORMANCE DATA
# --------------------------------------------------

def load_performance(raw_dir=RAW_DIR):
    path = Path(raw_dir) / PERFORMANCE_FILE

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    validate_columns(df, PERFORMANCE_COLUMNS, PERFORMANCE_FILE)

    validate_student_data(df, PERFORMANCE_FILE)

    df["student_id"] = df["student_id"].astype(str).str.strip()
    df["subject"] = df["subject"].astype(str).str.strip()

    numeric_columns = [
        "pre_test_score",
        "post_test_score",
        "score_improvement",
        "lessons_completed",
        "total_lessons",
        "completion_pct",
        "avg_time_per_lesson_mins",
        "quiz_attempts",
        "best_quiz_score",
        "streak_days",
        "platform_sessions",
        "label_at_risk",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if not df[TARGET_COLUMN].isin([0, 1]).all():
        raise ValueError("label_at_risk must contain only 0 or 1.")

    if df.duplicated().any():
        raise ValueError("Duplicate rows found in performance dataset.")

    return df


# --------------------------------------------------
# LOAD CONTENT ENGAGEMENT DATA
# --------------------------------------------------

def load_engagement(raw_dir=RAW_DIR):
    path = Path(raw_dir) / ENGAGEMENT_FILE

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    validate_columns(df, ENGAGEMENT_COLUMNS, ENGAGEMENT_FILE)

    validate_student_data(df, ENGAGEMENT_FILE)

    df["student_id"] = df["student_id"].astype(str).str.strip()
    df["subject"] = df["subject"].astype(str).str.strip()

    numeric_columns = [
        "time_spent_mins",
        "completed",
        "replayed",
        "paused_count",
        "liked",
        "notes_taken",
        "difficulty_rating",
        "engagement_score",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if df.duplicated().any():
        raise ValueError("Duplicate rows found in engagement dataset.")

    return df


# --------------------------------------------------
# LOAD INDEPENDENT EDTECH TEST CASES
# --------------------------------------------------

def load_test_cases(raw_dir=RAW_DIR):
    path = Path(raw_dir) / TEST_FILE

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list) or not records:
        raise ValueError("EdTech test dataset must be a non-empty JSON list.")

    rows = []

    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Invalid test case format.")

        if "input" not in record:
            raise ValueError("Test case is missing its input object.")

        if "expected_label_at_risk" not in record:
            raise ValueError("Test case is missing its expected label.")

        input_data = record["input"]

        missing = set(TEST_FEATURES) - set(input_data)

        if missing:
            raise ValueError(
                f"Test case {record.get('test_id')} is missing: {sorted(missing)}"
            )

        row = {
            "test_id": record.get("test_id"),
            **{feature: input_data[feature] for feature in TEST_FEATURES},
            TARGET_COLUMN: record["expected_label_at_risk"],
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    for column in TEST_FEATURES + [TARGET_COLUMN]:
        df[column] = pd.to_numeric(df[column], errors="raise")

    if not df[TARGET_COLUMN].isin([0, 1]).all():
        raise ValueError("Test labels must contain only 0 or 1.")

    return df


# --------------------------------------------------
# AGGREGATE ENGAGEMENT BY STUDENT AND SUBJECT
# --------------------------------------------------

def aggregate_engagement(engagement):
    grouped = engagement.groupby(
        ["student_id", "subject"],
        as_index=False
    ).agg(
        engagement_records=("engagement_id", "count"),
        content_type_count=("content_type", "nunique"),
        avg_time_spent_mins=("time_spent_mins", "mean"),
        completion_rate=("completed", "mean"),
        replay_rate=("replayed", "mean"),
        avg_paused_count=("paused_count", "mean"),
        like_rate=("liked", "mean"),
        notes_rate=("notes_taken", "mean"),
        avg_difficulty_rating=("difficulty_rating", "mean"),
        avg_engagement_score=("engagement_score", "mean"),
    )

    return grouped


# --------------------------------------------------
# PREPARE COMBINED LEARNING DATASET
# --------------------------------------------------


def prepare_learning_dataset(performance, engagement):
    engagement_summary = aggregate_engagement(engagement)

    learning_data = performance.merge(
        engagement_summary,
        on=["student_id", "subject"],
        how="left",
        validate="one_to_one",
    )

    engagement_columns = [
        "engagement_records",
        "content_type_count",
        "avg_time_spent_mins",
        "completion_rate",
        "replay_rate",
        "avg_paused_count",
        "like_rate",
        "notes_rate",
        "avg_difficulty_rating",
        "avg_engagement_score",
    ]

    learning_data["engagement_data_available"] = (
        learning_data["engagement_records"].notna().astype(int)
    )

    learning_data[engagement_columns] = (
        learning_data[engagement_columns].fillna(0)
    )

    return learning_data



# --------------------------------------------------
# PREPARE AT-RISK TRAINING DATA
# --------------------------------------------------

def prepare_risk_dataset(performance):
    columns = [
        "student_id",
        *TEST_FEATURES,
        TARGET_COLUMN,
    ]

    return performance[columns].copy()


# --------------------------------------------------
# SAVE PROCESSED DATASETS
# --------------------------------------------------

def save_processed_datasets(raw_dir=RAW_DIR):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    performance = load_performance(raw_dir)
    engagement = load_engagement(raw_dir)
    test_cases = load_test_cases(raw_dir)

    learning_data = prepare_learning_dataset(
        performance,
        engagement
    )

    risk_data = prepare_risk_dataset(performance)

    learning_path = PROCESSED_DIR / "learning_dataset.csv"
    risk_path = PROCESSED_DIR / "risk_dataset.csv"
    test_path = PROCESSED_DIR / "risk_test_dataset.csv"

    learning_data.to_csv(learning_path, index=False)
    risk_data.to_csv(risk_path, index=False)
    test_cases.to_csv(test_path, index=False)

    summary = {
        "performance_records": len(performance),
        "engagement_records": len(engagement),
        "test_cases": len(test_cases),
        "learning_dataset_rows": len(learning_data),
        "risk_dataset_rows": len(risk_data),
        "risk_test_rows": len(test_cases),
        "students": int(performance["student_id"].nunique()),
        "subjects": int(performance["subject"].nunique()),
        "engagement_students": int(engagement["student_id"].nunique()),
    }

    summary_path = PROCESSED_DIR / "data_summary.json"

    summary_path.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8"
    )

    print("\nDATA PREPARATION COMPLETED")
    print("-" * 40)
    print(json.dumps(summary, indent=2))

    print("\nSAVED FILES:")
    print(learning_path)
    print(risk_path)
    print(test_path)
    print(summary_path)

    return summary


if __name__ == "__main__":
    save_processed_datasets()
