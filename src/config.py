from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"

ARTIFACT_DIR = ROOT / "artifacts"

RISK_MODEL_PATH = ARTIFACT_DIR / "risk_model.joblib"
RISK_METRICS_PATH = ARTIFACT_DIR / "risk_metrics.json"
RISK_SUMMARY_PATH = ARTIFACT_DIR / "risk_training_summary.json"

RANDOM_STATE = 42