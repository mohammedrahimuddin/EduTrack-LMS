# EduTrack LMS — AI-Powered Student At-Risk Prediction and Personalized Learning System

## 1. Project Overview

EduTrack LMS is an AI-powered learning support system designed to analyze student performance and learning engagement data. The project focuses on identifying students who may be academically at risk and supporting personalized learning through course recommendations.

The system combines machine learning, data analysis, and a recommendation approach to explore how learning analytics can support better educational outcomes.

### Project Objectives

- Analyze student academic performance and learning engagement.
- Identify students who may be at academic risk.
- Apply machine learning techniques for student risk prediction.
- Generate personalized learning recommendations.
- Provide access to model functionality through a FastAPI backend and Streamlit dashboard.

## 2. Key Features

- Student performance dataset processing.
- Learning content engagement analysis.
- Data validation and preprocessing.
- At-risk student prediction using Random Forest.
- Independent JSON test dataset evaluation.
- Exploratory Data Analysis (EDA) and visualizations.
- Matrix Factorization-based personalized course recommendation.
- Cold-start fallback for recommendation scenarios.
- FastAPI backend.
- Streamlit dashboard.
- Model evaluation and project documentation.

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib |
| Backend | FastAPI |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| Testing | Pytest |
| Version Control | Git and GitHub |

## 4. Project Structure

```text
EduTrack_LMS/
├── app/
├── artifacts/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── literature_review.md
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── model_card.md
│   └── ab_test_plan.md
├── reports/
│   └── charts/
├── scripts/
├── src/
├── tests/
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## 5. Dataset Description

Place the following dataset files inside the `data/raw/` directory:

1. `aiml_student_performance.csv`
2. `aiml_content_engagement.csv`
3. `aiml_edtech_tests.json`

### Dataset Overview

| Dataset | Records |
|---|---:|
| Student Performance | 1,000 |
| Content Engagement | 600 |
| Independent JSON Test Cases | 50 |

The student performance dataset includes the target column `label_at_risk`.

**Target Distribution**

| Category | Label | Records |
|---|---:|---:|
| Not at Risk | 0 | 850 |
| At Risk | 1 | 150 |

## 6. Installation and Setup

### Requirements

- Python 3.11
- Visual Studio Code or another Python IDE
- Git
- Required packages listed in `requirements.txt`

### Windows PowerShell Setup

Create a virtual environment:

```powershell
py -3.11 -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 7. Data Processing and Analysis

### Data Preprocessing

Run the preprocessing pipeline:

```powershell
python -c "from src.data_loader import save_processed_datasets; save_processed_datasets()"
```

Check `src/data_loader.py` if the function name differs in your implementation.

### Exploratory Data Analysis

```powershell
python scripts/eda.py
```

EDA outputs are saved in:

- `reports/eda_summary.json`
- `reports/charts/`

## 8. Machine Learning Model

The project uses a Random Forest classifier for student at-risk prediction.

The initial model uses the following four input features:

- `lessons_completed`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `streak_days`

### Train the Model

```powershell
python -m src.train
```

### Initial Independent Test Results

The initial model was evaluated using the independent JSON test dataset containing 50 cases.

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 0.46 |
| Precision | 0.6364 |
| Recall | 0.2333 |
| F1-score | 0.3415 |

These results are preliminary. They indicate that the model requires further improvement and validation before practical deployment.

## 9. Personalized Learning Recommendations

EduTrack LMS also includes a personalized learning recommendation component.

The recommendation approach uses Matrix Factorization to learn student-course interaction patterns and generate a top-five course recommendation list.

A cold-start fallback is included for situations where sufficient interaction history is unavailable.

The recommendation component is separate from the Random Forest at-risk prediction model.

## 10. Research and Literature Review

The project is supported by a review of three relevant research studies covering student performance prediction, LMS activity-based early prediction, and personalized course recommendation.

### Research Papers Reviewed

**Paper 1: Machine Learning for Student Performance Prediction**

Alalawi, K., Athauda, R., & Chiong, R. (2023). *Contextualizing the Current State of Research on the Use of Machine Learning for Student Performance Prediction: A Systematic Literature Review.*

Engineering Reports, 5(12), e12699.

DOI: https://doi.org/10.1002/eng2.12699

**Paper 2: Early Prediction from LMS Logs**

Santos, R. M., & Henriques, R. (2023). *Accurate, Timely, and Portable: Course-Agnostic Early Prediction of Student Performance from LMS Logs.*

Computers and Education: Artificial Intelligence, 5, 100175.

DOI: https://doi.org/10.1016/j.caeai.2023.100175

**Paper 3: Personalized Course Recommendation**

Ma, Y., Ouyang, R., Long, X., Gao, Z., Lai, T., & Fan, C. (2023). *DORIS: Personalized Course Recommendation System Based on Deep Learning.*

PLOS ONE, 18(6), e0284687.

DOI: https://doi.org/10.1371/journal.pone.0284687

### Identified Research Gap

The reviewed studies demonstrate the usefulness of machine learning for student performance prediction, LMS activity analysis, and personalized course recommendations.

However, challenges remain in combining student risk identification with personalized learning support, handling limited interaction data, and validating models using independent datasets.

EduTrack LMS explores these areas through a student at-risk prediction component and a separate personalized recommendation component.

For detailed methodology, paper summaries, comparison, and research gaps, see:

**[Read the Complete Literature Review](docs/literature_review.md)**

## 11. Run the FastAPI Backend

Start the API server:

```powershell
uvicorn src.api:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

## 12. Run the Streamlit Dashboard

Open another PowerShell terminal, activate the virtual environment, and run:

```powershell
streamlit run app/streamlit_app.py
```

## 13. Testing

Run the project tests:

```powershell
pytest -q
```

## 14. Limitations

The current project has several limitations that must be considered:

- The original `label_at_risk` generation rule is unknown.
- Test scores are strongly associated with the target label, creating potential target leakage.
- Score improvement is calculated from pre-test and post-test scores.
- The independent JSON test dataset does not contain test-score features.
- Only 57 of 1,000 student-subject records match the engagement dataset.
- Initial independent test performance is weak.
- Further