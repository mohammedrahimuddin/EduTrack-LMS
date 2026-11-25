
# EduTrack LMS – Data Dictionary

## 1. Dataset Overview

The project uses three official internship datasets:

- aiml_student_performance.csv
- aiml_content_engagement.csv
- aiml_edtech_tests.json

### Dataset Summary

| Dataset | Records | Columns |
|---|---:|---:|
| Student Performance | 1000 | 16 |
| Content Engagement | 600 | 13 |
| EdTech Tests | 50 | JSON test cases |

No missing values or duplicate rows were detected in either CSV dataset.

## 2. Student Performance Dataset

File: `aiml_student_performance.csv`

| Field | Meaning |
|---|---|
| student_id | Pseudonymous learner identifier |
| grade | Student grade |
| subject | Learning subject |
| pre_test_score | Score before learning |
| post_test_score | Score after learning |
| score_improvement | Improvement in test score |
| lessons_completed | Number of completed lessons |
| total_lessons | Total lessons |
| completion_pct | Lesson completion percentage |
| avg_time_per_lesson_mins | Average lesson time |
| quiz_attempts | Number of quiz attempts |
| best_quiz_score | Best quiz score |
| streak_days | Consecutive learning days |
| platform_sessions | Number of platform sessions |
| device | Device used |
| label_at_risk | Target label for at-risk prediction |

### Target Distribution

- Not at risk (0): 850
- At risk (1): 150

### Unique Students and Subjects

- Unique students: 1000
- Unique subjects: 10

## 3. Content Engagement Dataset

File: `aiml_content_engagement.csv`

| Field | Meaning |
|---|---|
| engagement_id | Unique engagement record identifier |
| student_id | Learner identifier |
| content_type | Type of learning content |
| subject | Learning subject |
| date | Engagement date |
| time_spent_mins | Time spent on content |
| completed | Whether content was completed |
| replayed | Whether content was replayed |
| paused_count | Number of pauses |
| liked | Whether content was liked |
| notes_taken | Whether notes were taken |
| difficulty_rating | Learner's difficulty rating |
| engagement_score | Engagement score |

### Content Type Distribution

| Content Type | Records |
|---|---:|
| Reading | 107 |
| Video | 107 |
| Assignment | 101 |
| Practice Problem | 99 |
| Quiz | 96 |
| Live Session | 90 |

- Total records: 600
- Unique students: 459
- Missing values: 0
- Duplicate rows: 0

## 4. EdTech Test Dataset

File: `aiml_edtech_tests.json`

Contains 50 independent test cases for at-risk prediction.

| Field | Meaning |
|---|---|
| test_id | Unique test case identifier |
| input | Input feature object |
| expected_label_at_risk | Expected prediction |
| model_target | Prediction task name |

### Input Features

- lessons_completed
- avg_time_per_lesson_mins
- quiz_attempts
- streak_days

### Expected Label Distribution

- At risk (1): 30
- Not at risk (0): 20

Model target: `at_risk_prediction`

## 5. Data Relationships

Both CSV datasets contain:

- student_id
- subject

The datasets share 459 unique students.

Performance and engagement data can be aggregated at student-subject level for analysis and recommendations.

## 6. Machine Learning Usage

### At-Risk Prediction

Target: `label_at_risk`

Training features:

- lessons_completed
- avg_time_per_lesson_mins
- quiz_attempts
- streak_days

The independent JSON test cases will be used for evaluation.

### Subject Recommendation

The recommendation system will use student performance and aggregated engagement information to rank suitable subjects.

There is no explicit course_id or rating column in the official datasets.

## 7. Data Quality Notes

- Both CSV datasets contain no missing values.
- No duplicate CSV rows were detected.
- Original raw datasets must remain unchanged.
- Processed datasets will be stored in `data/processed/`.
- Synthetic demo data must not overwrite official internship datasets.
