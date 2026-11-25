# EduTrack LMS — AI-Powered # EduTrack LMS — AI-Powered Student At-Risk Prediction System

EduTrack LMS is an AI-powered learning support project that analyzes student performance and learning engagement data to identify students who may be at risk and support personalized learning recommendations.

## Features

- Official student performance dataset processing
- Content engagement data analysis
- Data validation and preprocessing
- At-risk student prediction using Random Forest
- Independent JSON test dataset evaluation
- Exploratory Data Analysis (EDA) and visualizations
- FastAPI backend
- Streamlit dashboard
- Model evaluation and documentation

## Technology Stack

- Python 3.11
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- FastAPI
- Streamlit
- Joblib
- Pytest

## Project Structure

```text
EduTrack_LMS/
├── app/
├── artifacts/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── reports/
│   └── charts/
├── scripts/
├── src/
└── tests/
```

## Official Datasets

Place the following files inside `data/raw/`:

1. `aiml_student_performance.csv`
2. `aiml_content_engagement.csv`
3. `aiml_edtech_tests.json`

### Dataset Overview

| Dataset | Records |
|---|---:|
| Student Performance | 1,000 |
| Content Engagement | 600 |
| Independent JSON Test Cases | 50 |

The student performance dataset contains the target column `label_at_risk`.

Target distribution:
- Not at risk (0): 850
- At risk (1): 150

## Setup — Windows PowerShell

Create and activate a Python virtual environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If activation is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Data Processing

Run the data preprocessing pipeline:

```powershell
python -c "from src.data_loader import save_processed_datasets; save_processed_datasets()"
```

Check the actual function name in `src/data_loader.py` if your implementation differs.

## Exploratory Data Analysis

```powershell
python scripts/eda.py
```

EDA outputs are saved in:
- `reports/eda_summary.json`
- `reports/charts/`

## Model Training

```powershell
python -m src.train
```

The initial Random Forest model uses four features:

- `lessons_completed`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `streak_days`

The independent test dataset contains 50 cases.

**Initial independent test results:**

| Metric | Result |
|---|---:|
| Accuracy | 0.46 |
| Precision | 0.6364 |
| Recall | 0.2333 |
| F1-score | 0.3415 |

These results are preliminary and indicate that further model improvement is required.

## Start FastAPI

```powershell
uvicorn src.api:app --reload
```

API documentation:

`http://127.0.0.1:8000/docs`

Health endpoint:

`http://127.0.0.1:8000/health`

## Start Streamlit Dashboard

Open a second PowerShell terminal:

```powershell
streamlit run app/streamlit_app.py
```

## Testing

```powershell
pytest -q
```

## Important Data and Model Limitations

- The original `label_at_risk` generation rule is unknown.
- Test scores are strongly associated with the target label, creating potential target leakage.
- Score improvement is calculated from pre-test and post-test scores.
- The independent JSON test dataset does not contain test-score features.
- Only 57 of 1,000 student-subject records match the engagement dataset.
- Initial independent test performance is weak.

Do not claim that the model is production-ready or that it reliably identifies at-risk students without further validation.

## Responsible Use

Model predictions should support educators, not replace their judgment.

The system must not be the sole basis for grading, admission or academic progression decisions.

## Documentation

Additional project documentation:

- `docs/architecture.md`
- `docs/model_card.md`
- `docs/data_dictionary.md`
- `docs/ab_test_plan.md`

## Future Improvements

- Improve prediction performance.
- Investigate the original target-label generation process.
- Improve engagement-data integration.
- Develop personalized learning recommendations.
- Validate the system with additional independent data.
- Test API and dashboard performance.