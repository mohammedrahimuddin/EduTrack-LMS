# System Architecture â€” EduTrack LMS

## 1. Project Overview

EduTrack LMS is a machine learning-based student support system designed to identify students who may be academically at risk using student performance and learning activity data.

The current implemented system uses a Random Forest classifier for at-risk prediction and provides prediction functionality through a FastAPI backend and Streamlit dashboard.

The project also includes a data preprocessing pipeline that prepares student performance, content engagement, and independent test datasets.

## 2. High-Level System Architecture

```text
             RAW DATA SOURCES
                     |
          +----------+----------+
          |          |          |
          v          v          v
      Student    Engagement   Independent
     Performance    Data       JSON Tests
        CSV         CSV
          |          |
          +-----+----+
                |
                v
        DATA LOADING & VALIDATION
                |
                v
          DATA PREPROCESSING
                |
          +-----+------+
          |            |
          v            v
   Risk Dataset   Learning Dataset
          |            |
          v            v
   Random Forest   Prepared Learning
   Classification     Data Output
          |
          v
   Model Evaluation
          |
          +------------------+
          |                  |
          v                  v
   Saved Model         Metrics & Summary
   (Joblib)             (JSON)
          |
          v
      FastAPI Backend
          |
       /predict
          |
          v
    Streamlit Dashboard
          |
          v
   Student Risk Result
```

Note: The learning dataset is prepared and saved separately. A personalized recommendation model is not currently verified in the implementation.

## 3. Data Sources

The project uses three input files:

| Dataset | Description | Records |
|---|---|---:|
| `aiml_student_performance.csv` | Student academic and learning performance | 1,000 |
| `aiml_content_engagement.csv` | Student interactions with learning content | 600 |
| `aiml_edtech_tests.json` | Independent prediction test cases | 50 |

### Student Performance Features

The performance dataset contains student information, academic scores, lesson completion, quiz activity, learning streaks, and the target label.

Target column: `label_at_risk`

- 0: Not at Risk
- 1: At Risk

### Engagement Features

The engagement dataset includes:

- Content type
- Time spent
- Completion status
- Replays
- Paused count
- Likes
- Notes taken
- Difficulty rating
- Engagement score

## 4. Data Processing Architecture

The data pipeline is implemented in `src/data_loader.py`.

The pipeline contains the following stages:

1. **Data ingestion:** Loads performance CSV, engagement CSV, and independent JSON test cases.
2. **Column validation:** Checks required columns in each dataset.
3. **Record validation:** Checks empty datasets, missing student IDs, and missing subjects.
4. **Data type validation:** Converts numeric columns and validates binary target labels.
5. **Engagement aggregation:** Groups engagement records by student ID and subject.
6. **Data integration:** Joins aggregated engagement data with student performance records.
7. **Missing-value handling:** Creates an engagement availability indicator and fills missing aggregate values.
8. **Risk dataset preparation:** Selects the four model features and target label.
9. **Processed data storage:** Saves the prepared datasets and data summary.

### Generated Processed Files

| File | Purpose |
|---|---|
| `learning_dataset.csv` | Performance data combined with engagement summaries |
| `risk_dataset.csv` | Features and labels for Random Forest training |
| `risk_test_dataset.csv` | Independent JSON test cases converted to CSV |
| `data_summary.json` | Dataset processing summary |

## 5. At-Risk Prediction Model

The project uses a Random Forest Classifier implemented in `src/train.py`.

### Model Configuration

| Parameter | Value |
|---|---:|
| Algorithm | Random Forest Classifier |
| Number of Estimators | 300 |
| Maximum Depth | 8 |
| Minimum Samples per Leaf | 3 |
| Class Weight | Balanced |
| Random State | 42 |

### Input Features

The model uses four features:

1. `lessons_completed`
2. `avg_time_per_lesson_mins`
3. `quiz_attempts`
4. `streak_days`

### Target Variable

`label_at_risk`

The model is trained using the processed risk dataset and evaluated using the independent JSON test dataset.

### Model Artifacts

The trained model and evaluation results are stored in the `artifacts/` directory:

- `risk_model.joblib`
- `risk_metrics.json`
- `risk_training_summary.json`

## 6. Model Evaluation Architecture

The training implementation calculates:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

Evaluation results are stored in JSON files for further inspection.

The independent test dataset contains 50 cases. The initial recorded accuracy was 0.46.

Further validation is necessary because the independent test performance is currently weak.

ROC-AUC is a potential additional evaluation metric but is not currently calculated by the training implementation.

## 7. Backend Architecture

The backend is implemented using FastAPI in `src/api.py`.

### Available Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Checks API health and model availability |
| `/predict` | POST | Predicts student at-risk status |
| `/retrain` | POST | Triggers model retraining |

The prediction endpoint accepts four input features and returns:

- Prediction label
- Risk classification
- Model risk score

The risk score is an uncalibrated model estimate and should not be interpreted as a confirmed probability.

## 8. Dashboard Architecture

The frontend dashboard is implemented using Streamlit in `app/streamlit_app.py`.

Dashboard functionality:

- Student learning input form.
- API URL configuration.
- Prediction request to FastAPI.
- Display of at-risk or not-at-risk results.
- Display of model risk score.
- API error handling.

The dashboard communicates with the backend using HTTP requests.

## 9. Testing Architecture

Automated tests are available in `tests/test_risk_model.py`.

The current test suite checks:

1. Random Forest model training.
2. Prediction output length and valid labels.
3. Prediction probability output shape and value range.

Testing is performed using Pytest.

## 10. Current Limitations

- The original target-label generation rule is unknown.
- Potential target leakage must be investigated.
- Engagement data matches only 57 of 1,000 student-subject records.
- Engagement information is prepared separately and is not currently used as input to the Random Forest model.
- Independent test performance requires improvement.
- ROC-AUC is not currently implemented in the training script.
- A personalized course recommendation model is not currently present in the verified Python implementation.
- API and dashboard require further integration testing.

## 11. Future Architecture Improvements

- Improve independent model evaluation.
- Investigate target-label generation and potential leakage.
- Improve engagement-data integration.
- Add ROC-AUC and other suitable evaluation metrics.
- Expand automated testing.
- Develop and evaluate a personalized recommendation component.
- Validate the system with additional independent datasets.

---

**Project:** EduTrack LMS
**Domain:** Artificial Intelligence and Machine Learning in Education
**Primary Model:** Random Forest Classifier
**Backend:** FastAPI
**Dashboard:** Streamlit
