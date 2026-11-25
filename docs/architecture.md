# System Architecture — EduTrack LMS

## 1. Overview

EduTrack LMS is an AI-powered learning support system that processes student performance and content engagement data to support at-risk student identification and personalized learning recommendations.

## 2. System Architecture

```text
Official Student Performance CSV
              |
              v
       Data Validation
              |
              v
     Data Preprocessing
              |
       +------+------+
       |             |
       v             v
 Risk Dataset   Learning Dataset
       |             |
       v             v
 Random Forest   Learning Analysis
 Risk Model      & Recommendations
       |             |
       +------+------+
              |
              v
       Prediction Output
              |
              v
        FastAPI Service
              |
              v
      Streamlit Dashboard
```

## 3. Data Sources

The system uses three official data files:

- `aiml_student_performance.csv`
- `aiml_content_engagement.csv`
- `aiml_edtech_tests.json`

The student performance dataset contains 1,000 records and includes academic performance, learning activity and the `label_at_risk` target.

The content engagement dataset contains 600 records describing student interactions with learning content.

The JSON file contains 50 independent test cases for at-risk prediction.

## 4. Data Processing

The data loader performs the following operations:

1. Loads the official CSV and JSON files.
2. Validates required columns and data types.
3. Checks student records and target labels.
4. Aggregates content engagement information.
5. Combines performance and engagement information using student ID and subject.
6. Creates processed learning and risk datasets.

Engagement data is available for only 57 matching student-subject records out of 1,000. Missing matches must be distinguished from genuine zero engagement.

## 5. Machine Learning Model

The initial risk prediction model uses a Random Forest Classifier.

Input features:

- `lessons_completed`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `streak_days`

Target:

- `label_at_risk`

The model is trained using the official performance dataset and evaluated against the independent 50-case JSON test dataset.

The initial independent test accuracy was 0.46. Further model improvement and validation are required.

## 6. API and Dashboard

**FastAPI:** Intended to expose prediction and system endpoints.

**Streamlit:** Intended to provide a user-facing dashboard for viewing student information and prediction results.

The API and dashboard integration must be verified against the current implementation before claiming production readiness.

## 7. Limitations

- The original at-risk label-generation rule is unknown.
- Test scores have a strong association with the target label, creating potential target leakage if used as prediction features.
- The independent test dataset contains only four prediction features.
- Engagement-data matching coverage is limited.
- Initial independent test performance is weak.

## 8. Future Improvements

- Investigate and document the original label-generation process.
- Improve model precision, recall and F1-score.
- Validate the model on additional independent data.
- Improve engagement-data integration.
- Develop and validate personalized learning recommendations.
- Test API performance and dashboard usability.
- Monitor model performance after deployment.