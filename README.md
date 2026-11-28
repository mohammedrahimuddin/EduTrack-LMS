# EduTrack LMS â€” AI-Powered Student At-Risk Prediction System

## 1. Project Overview

EduTrack LMS is a machine learning-based educational support system designed to analyze student academic performance and learning engagement data to identify students who may be academically at risk.

The project uses a Random Forest Classifier to predict student at-risk status based on learning activity features. It also includes a data processing pipeline, independent model evaluation, a FastAPI backend, and a Streamlit dashboard.

The primary objective is to explore how machine learning and learning analytics can support educators in identifying students who may need additional academic assistance.

### Project Objectives

- Analyze student academic performance and learning engagement data.
- Identify students who may be academically at risk.
- Apply machine learning techniques for student risk prediction.
- Evaluate the prediction model using an independent test dataset.
- Prepare processed datasets for machine learning.
- Provide prediction functionality through a FastAPI backend.
- Display prediction results through a Streamlit dashboard.
- Study research approaches for future personalized learning recommendations.

## 2. Key Features

- Student performance dataset processing.
- Learning content engagement data analysis.
- Data validation and preprocessing.
- Student at-risk prediction using Random Forest.
- Independent JSON test dataset evaluation.
- Exploratory Data Analysis (EDA) and visualizations.
- Engagement data aggregation by student and subject.
- Model evaluation and performance reporting.
- FastAPI prediction backend.
- Streamlit interactive dashboard.
- Automated model tests using Pytest.
- Technical documentation and literature review.

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Matplotlib |
| Backend Framework | FastAPI |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| API Validation | Pydantic |
| Testing | Pytest |
| Version Control | Git and GitHub |

## 4. Project Architecture

The system follows a modular architecture consisting of data ingestion, validation, preprocessing, model training, evaluation, backend services, and dashboard integration.

### High-Level Workflow

```text
       RAW DATA SOURCES
              |
      +-------+--------+
      |       |        |
      v       v        v
 Performance Engagement JSON Test
    CSV        CSV       Cases
      |       |        |
      +-------+--------+
              |
              v
       DATA INGESTION
              |
              v
       DATA VALIDATION
              |
              v
      DATA PREPROCESSING
              |
        +-----+------+
        |            |
        v            v
 Learning Dataset  Risk Dataset
        |            |
        |            v
        |       Random Forest
        |        Classifier
        |            |
        |            v
        |       Model Evaluation
        |            |
        |            v
        |       Saved Model
        |            |
        |            v
        |       FastAPI Backend
        |            |
        |            v
        |      Streamlit Dashboard
        |            |
        |            v
        |      Prediction Results
        |
        v
  Processed Learning Data
```

The learning dataset is prepared separately for further analysis and future learning-support functionality. A personalized recommendation model is not currently included in the verified implementation.

## 5. Project Structure

```text
EduTrack_LMS/
â”‚
â”œâ”€â”€ app/
â”‚   â””â”€â”€ streamlit_app.py
â”‚
â”œâ”€â”€ artifacts/
â”‚   â”œâ”€â”€ risk_model.joblib
â”‚   â”œâ”€â”€ risk_metrics.json
â”‚   â””â”€â”€ risk_training_summary.json
â”‚
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ raw/
â”‚   â”‚   â”œâ”€â”€ aiml_student_performance.csv
â”‚   â”‚   â”œâ”€â”€ aiml_content_engagement.csv
â”‚   â”‚   â””â”€â”€ aiml_edtech_tests.json
â”‚   â”‚
â”‚   â””â”€â”€ processed/
â”‚       â”œâ”€â”€ learning_dataset.csv
â”‚       â”œâ”€â”€ risk_dataset.csv
â”‚       â”œâ”€â”€ risk_test_dataset.csv
â”‚       â””â”€â”€ data_summary.json
â”‚
â”œâ”€â”€ docs/
â”‚   â”œâ”€â”€ literature_review.md
â”‚   â”œâ”€â”€ architecture.md
â”‚   â”œâ”€â”€ data_pipeline.md
â”‚   â”œâ”€â”€ evaluation_metrics.md
â”‚   â”œâ”€â”€ data_dictionary.md
â”‚   â”œâ”€â”€ model_card.md
â”‚   â””â”€â”€ ab_test_plan.md
â”‚
â”œâ”€â”€ reports/
â”‚   â””â”€â”€ charts/
â”‚
â”œâ”€â”€ scripts/
â”‚   â”œâ”€â”€ eda.py
â”‚   â””â”€â”€ retrain.py
â”‚
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ api.py
â”‚   â”œâ”€â”€ config.py
â”‚   â”œâ”€â”€ data_loader.py
â”‚   â”œâ”€â”€ train.py
â”‚   â””â”€â”€ __init__.py
â”‚
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_risk_model.py
â”‚
â”œâ”€â”€ .gitignore
â”œâ”€â”€ pytest.ini
â”œâ”€â”€ requirements.txt
â””â”€â”€ README.md
```

*Note: The tree represents the main project files and expected generated artifacts. Generated files may not exist until the relevant pipeline or training command has been executed.*

## 6. Dataset Description

The project uses three input datasets stored in `data/raw/`.

### Input Datasets

| Dataset | Filename | Records |
|---|---|---:|
| Student Performance | `aiml_student_performance.csv` | 1,000 |
| Content Engagement | `aiml_content_engagement.csv` | 600 |
| Independent Test Cases | `aiml_edtech_tests.json` | 50 |

### 6.1 Student Performance Dataset

This dataset contains student academic and learning activity information.

Important columns include:

- `student_id`
- `grade`
- `subject`
- `pre_test_score`
- `post_test_score`
- `score_improvement`
- `lessons_completed`
- `total_lessons`
- `completion_pct`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `best_quiz_score`
- `streak_days`
- `platform_sessions`
- `device`
- `label_at_risk`

### 6.2 Content Engagement Dataset

This dataset contains information about student interactions with learning content.

Important columns include:

- `engagement_id`
- `student_id`
- `content_type`
- `subject`
- `date`
- `time_spent_mins`
- `completed`
- `replayed`
- `paused_count`
- `liked`
- `notes_taken`
- `difficulty_rating`
- `engagement_score`

### 6.3 Independent JSON Test Dataset

The JSON dataset contains 50 independent test cases.

Each test case includes four input features and an expected at-risk label.

### Target Distribution

The student performance dataset contains the following target distribution:

| Category | Label | Records |
|---|---:|---:|
| Not at Risk | 0 | 850 |
| At Risk | 1 | 150 |
| Total | | 1,000 |

## 7. Installation and Setup

### Requirements

- Python 3.11
- Visual Studio Code or another Python IDE
- Git
- Packages listed in `requirements.txt`

### Step 1: Clone the Repository

```powershell
git clone https://github.com/mohammedrahimuddin/EduTrack_LMS.git
```

Move into the project directory:

```powershell
cd EduTrack_LMS
```

### Step 2: Create a Virtual Environment

```powershell
py -3.11 -m venv .venv
```

### Step 3: Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 8. Data Processing Pipeline

The data processing pipeline is implemented in:

`src/data_loader.py`

### Pipeline Stages

1. Data ingestion from CSV and JSON files.
2. Required column validation.
3. Student record validation.
4. Numeric data type validation.
5. Duplicate record checks.
6. Engagement data aggregation.
7. Integration of performance and engagement data.
8. Risk dataset preparation.
9. Independent test dataset preparation.
10. Saving processed datasets and data summary.

### Run the Data Processing Pipeline

```powershell
python -m src.data_loader
```

Alternatively:

```powershell
python -c "from src.data_loader import save_processed_datasets; save_processed_datasets()"
```

### Generated Processed Datasets

| Filename | Description |
|---|---|
| `learning_dataset.csv` | Performance data integrated with engagement summaries |
| `risk_dataset.csv` | Prepared features and target for risk prediction |
| `risk_test_dataset.csv` | Independent test cases converted into CSV |
| `data_summary.json` | Summary of processed data records |

The processed datasets are stored in `data/processed/`.

### Engagement Data Integration

Engagement records are aggregated using `student_id` and `subject`.

The pipeline creates an `engagement_data_available` indicator to distinguish records with matching engagement information from records without a match.

Currently, only 57 of 1,000 student-subject records match the engagement dataset. This is an important data limitation that requires further investigation.

For detailed pipeline documentation, see [Data Pipeline](docs/data_pipeline.md).

## 9. Exploratory Data Analysis

The project includes an Exploratory Data Analysis script.

Run:

```powershell
python scripts/eda.py
```

The EDA process helps examine dataset characteristics, distributions, and relationships between student learning features.

EDA outputs are intended to be saved in:

- `reports/eda_summary.json`
- `reports/charts/`

## 10. Machine Learning Model

### 10.1 Random Forest Classifier

EduTrack LMS uses a Random Forest Classifier to identify students who may be academically at risk.

The model is implemented in:

`src/train.py`

### 10.2 Input Features

The model uses four input features:

| Feature | Description |
|---|---|
| `lessons_completed` | Number of lessons completed |
| `avg_time_per_lesson_mins` | Average time spent per lesson |
| `quiz_attempts` | Number of quiz attempts |
| `streak_days` | Number of consecutive learning days |

Target variable:

`label_at_risk`

- 0: Not at Risk
- 1: At Risk

### 10.3 Model Configuration

| Parameter | Value |
|---|---:|
| Algorithm | Random Forest Classifier |
| Number of Estimators | 300 |
| Maximum Depth | 8 |
| Minimum Samples per Leaf | 3 |
| Class Weight | Balanced |
| Random State | 42 |

### 10.4 Train the Model

First, prepare the processed datasets:

```powershell
python -m src.data_loader
```

Then train the model:

```powershell
python -m src.train
```

The training script reads the processed risk dataset and independent test dataset.

The trained model and evaluation results are saved in the `artifacts/` directory.

## 11. Model Evaluation

The Random Forest model is evaluated using the independent JSON test dataset containing 50 test cases.

### Implemented Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

### Initial Independent Test Results

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 0.46 |
| Precision | 0.6364 |
| Recall | 0.2333 |
| F1-score | 0.3415 |

These are preliminary results from the initial model evaluation.

The relatively low recall indicates that the model misses a number of actual at-risk cases. Further investigation and model improvement are required.

### Evaluation Artifacts

The training script generates:

- `artifacts/risk_metrics.json`
- `artifacts/risk_training_summary.json`

ROC-AUC, specificity, and balanced accuracy are proposed for future evaluation and are not currently calculated by the training implementation.

For detailed metric definitions and limitations, see [Evaluation Metrics](docs/evaluation_metrics.md).

## 12. FastAPI Backend

The backend is implemented using FastAPI in:

`src/api.py`

### Start the API Server

```powershell
uvicorn src.api:app --reload
```

### Available API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Checks API health and model availability |
| `/predict` | POST | Predicts student at-risk status |
| `/retrain` | POST | Triggers model retraining |

### API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

### Health Endpoint

```text
http://127.0.0.1:8000/health
```

### Prediction Input Example

```json
{
  "lessons_completed": 20,
  "avg_time_per_lesson_mins": 25.0,
  "quiz_attempts": 3,
  "streak_days": 10
}
```

The prediction endpoint returns:

- Prediction label.
- Risk classification.
- Model risk score.

The risk score is an uncalibrated model estimate and must not be interpreted as a confirmed probability.

## 13. Streamlit Dashboard

The dashboard is implemented in:

`app/streamlit_app.py`

### Start the Dashboard

Open a second PowerShell terminal, activate the virtual environment, and run:

```powershell
streamlit run app/streamlit_app.py
```

### Dashboard Features

- Student learning details input.
- Learning activity input.
- FastAPI backend URL configuration.
- Student risk prediction request.
- At-risk or not-at-risk result display.
- Model risk score visualization.
- API connection error handling.

The dashboard communicates with the FastAPI backend through HTTP requests.

Make sure the FastAPI server is running before requesting predictions from the dashboard.

## 14. Automated Testing

The project uses Pytest for basic model testing.

Test file:

`tests/test_risk_model.py`

The existing test suite contains three tests:

1. Model training test.
2. Prediction output validation.
3. Prediction probability validation.

### Run Tests

```powershell
pytest -q
```

The tests verify basic Random Forest training and prediction functionality. Additional integration tests for the data pipeline, API, and dashboard are planned future improvements.

## 15. Research and Literature Review

The project is supported by a literature review of three research papers covering student performance prediction, early prediction using LMS activity logs, and personalized course recommendation systems.

### Paper 1: Student Performance Prediction

Alalawi, K., Athauda, R., & Chiong, R. (2023).

*Contextualizing the Current State of Research on the Use of Machine Learning for Student Performance Prediction: A Systematic Literature Review.*

Engineering Reports, 5(12), e12699.

DOI: https://doi.org/10.1002/eng2.12699

### Paper 2: Early Prediction Using LMS Logs

Santos, R. M., & Henriques, R. (2023).

*Accurate, Timely, and Portable: Course-Agnostic Early Prediction of Student Performance from LMS Logs.*

Computers and Education: Artificial Intelligence, 5, 100175.

DOI: https://doi.org/10.1016/j.caeai.2023.100175

### Paper 3: Personalized Course Recommendation

Ma, Y., Ouyang, R., Long, X., Gao, Z., Lai, T., & Fan, C. (2023).

*DORIS: Personalized Course Recommendation System Based on Deep Learning.*

PLOS ONE, 18(6), e0284687.

DOI: https://doi.org/10.1371/journal.pone.0284687

### Identified Research Gap

The reviewed studies demonstrate the usefulness of machine learning for student performance prediction, LMS activity analysis, and personalized course recommendation.

However, challenges remain in integrating student risk identification with personalized learning support, handling limited interaction data, and validating models using independent datasets.

EduTrack LMS currently focuses on student at-risk prediction and learning engagement data preparation. Personalized recommendation functionality is a proposed future extension and is not currently implemented in the verified Python code.

For detailed paper summaries, methodology, comparison, and research gaps, see:

[Read the Complete Literature Review](docs/literature_review.md)

## 16. Project Documentation

The following documents provide additional technical details about EduTrack LMS.

| Document | Description |
|---|---|
| [Literature Review](docs/literature_review.md) | Review of three research papers and identified research gaps |
| [Architecture](docs/architecture.md) | System architecture, components, and model workflow |
| [Data Pipeline](docs/data_pipeline.md) | Data ingestion, validation, preprocessing, and generated datasets |
| [Evaluation Metrics](docs/evaluation_metrics.md) | Model evaluation metrics, initial results, and proposed improvements |
| [Data Dictionary](docs/data_dictionary.md) | Dataset fields and descriptions |
| [Model Card](docs/model_card.md) | Model details, evaluation, and limitations |
| [A/B Test Plan](docs/ab_test_plan.md) | Proposed model comparison and evaluation plan |

## 17. Limitations

The current project has several limitations:

- The original `label_at_risk` generation rule is unknown.
- Test scores are strongly associated with the target label, creating potential target leakage that requires investigation.
- Score improvement is calculated from pre-test and post-test scores.
- The independent JSON test dataset does not contain test-score features.
- Only 57 of 1,000 student-subject records match the engagement dataset.
- Engagement features are prepared separately and are not currently used as inputs to the Random Forest model.
- Initial independent test performance is weak.
- The independent test dataset contains only 50 cases.
- ROC-AUC is not currently calculated by the training script.
- A personalized course recommendation model is not currently present in the verified Python implementation.
- Further validation is required before real-world use.

The current model should not be considered production-ready.

## 18. Responsible Use

EduTrack LMS is intended as an educational research and learning support project.

Model predictions should assist educators rather than replace their professional judgment.

The predictions must not be used as the sole basis for:

- Student grading.
- Admission decisions.
- Academic progression.
- Other high-impact educational decisions.

Additional validation is necessary before any real-world educational deployment.

## 19. Future Improvements

- Improve student at-risk prediction performance.
- Investigate the original target-label generation process.
- Investigate potential target leakage.
- Improve engagement-data integration and matching coverage.
- Add ROC-AUC, specificity, and balanced accuracy evaluation.
- Expand automated testing for the data pipeline and API.
- Validate the model using additional independent datasets.
- Develop and evaluate a personalized learning recommendation component.
- Evaluate recommendation quality using suitable ranking metrics after implementation.
- Improve API and dashboard integration testing.
- Monitor model performance using additional educational data.

---

**Project:** EduTrack LMS
**Domain:** Artificial Intelligence and Machine Learning in Education
**Primary Model:** Random Forest Classifier
**Backend:** FastAPI
**Dashboard:** Streamlit
**Programming Language:** Python 3.11
