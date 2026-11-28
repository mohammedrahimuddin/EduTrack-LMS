# Data Pipeline Documentation â€” EduTrack LMS

## 1. Introduction

The EduTrack LMS data pipeline prepares student performance data, content engagement data, and independent test cases for machine learning model training and evaluation.

The pipeline is implemented in:

`src/data_loader.py`

It validates input datasets, aggregates engagement information, prepares separate datasets, and saves processed outputs.

## 2. Pipeline Architecture

```text
       RAW DATA SOURCES
              |
     +--------+---------+
     |        |         |
     v        v         v
 Performance Engagement JSON Test
    CSV        CSV       Cases
     |        |         |
     +--------+---------+
              |
              v
       DATA INGESTION
              |
              v
       COLUMN VALIDATION
              |
              v
       RECORD VALIDATION
              |
              v
      DATA TYPE VALIDATION
              |
        +-----+------+
        |            |
        v            v
  Engagement     Independent
  Aggregation    Test Preparation
        |
        v
  Performance Data
     Integration
        |
        +------------+
        |            |
        v            v
 Learning Dataset  Risk Dataset
        |            |
        v            v
  learning_dataset risk_dataset
       .csv            .csv

              Independent Test
                     |
                     v
             risk_test_dataset.csv

       All processed outputs
              |
              v
       data_summary.json
```

## 3. Input Data Sources

The pipeline reads three files from `data/raw/`.

| File | Purpose |
|---|---|
| `aiml_student_performance.csv` | Academic performance and student learning information |
| `aiml_content_engagement.csv` | Student interaction and content engagement information |
| `aiml_edtech_tests.json` | Independent test cases for risk prediction |

### 3.1 Student Performance Dataset

Important fields include:

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

### 3.2 Content Engagement Dataset

Important fields include:

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

### 3.3 Independent JSON Test Dataset

Each test case contains:

- `test_id`
- `input`
- `expected_label_at_risk`

The input object contains the four prediction features used by the Random Forest model.

## 4. Data Ingestion

The data loader provides three loading functions:

| Function | Responsibility |
|---|---|
| `load_performance()` | Loads the student performance CSV |
| `load_engagement()` | Loads the content engagement CSV |
| `load_test_cases()` | Loads independent JSON test cases |

The loader checks whether the input files exist before reading them.

JSON data is loaded using UTF-8 encoding.

## 5. Data Validation

The pipeline performs several validation operations.

### 5.1 Required Column Validation

The `validate_columns()` function checks whether all required columns are present.

Missing required columns raise a `ValueError`.

### 5.2 Student Record Validation

The `validate_student_data()` function checks:

- Dataset is not empty.
- Student IDs are not missing.
- Subject values are not missing.

### 5.3 Numeric Data Validation

Numeric columns are converted using Pandas numeric conversion.

Invalid numeric values raise an error instead of being silently accepted.

### 5.4 Target Label Validation

The target column `label_at_risk` must contain only:

- 0 â€” Not At Risk
- 1 â€” At Risk

### 5.5 Duplicate Validation

Duplicate rows are checked in the student performance and engagement datasets.

## 6. Engagement Data Aggregation

The `aggregate_engagement()` function groups engagement records using:

- `student_id`
- `subject`

It calculates:

| Aggregated Feature | Calculation |
|---|---|
| `engagement_records` | Number of engagement records |
| `content_type_count` | Unique content types |
| `avg_time_spent_mins` | Average time spent |
| `completion_rate` | Mean completion value |
| `replay_rate` | Mean replay value |
| `avg_paused_count` | Average pause count |
| `like_rate` | Mean liked value |
| `notes_rate` | Mean notes-taken value |
| `avg_difficulty_rating` | Average difficulty rating |
| `avg_engagement_score` | Average engagement score |

## 7. Performance and Engagement Integration

The `prepare_learning_dataset()` function combines performance data with aggregated engagement information.

The integration uses:

- `student_id`
- `subject`

A left join is used to preserve the student performance records.

The merge uses one-to-one validation.

### Engagement Availability

The pipeline creates an additional feature:

`engagement_data_available`

- 1 indicates engagement data is available.
- 0 indicates no matching engagement record was found.

Missing engagement aggregate values are filled with zero.

This indicator helps distinguish missing engagement information from matched records.

The current dataset has limited engagement matching coverage: 57 out of 1,000 student-subject records.

## 8. Risk Dataset Preparation

The `prepare_risk_dataset()` function creates the dataset for Random Forest training.

It selects:

| Feature | Description |
|---|---|
| `student_id` | Student identifier |
| `lessons_completed` | Completed lessons |
| `avg_time_per_lesson_mins` | Average time per lesson |
| `quiz_attempts` | Number of quiz attempts |
| `streak_days` | Learning streak |
| `label_at_risk` | Target label |

The model uses the four numerical features, while `student_id` is retained as an identifier and not used as a model input.

## 9. Independent Test Data Preparation

The `load_test_cases()` function validates and converts JSON test cases into a Pandas DataFrame.

It checks:

- JSON structure.
- Presence of the input object.
- Presence of the expected target label.
- Presence of all four prediction features.
- Numeric feature values.
- Binary expected labels.

The resulting dataset is used for independent model evaluation.

## 10. Processed Data Outputs

The pipeline saves files in `data/processed/`.

| Output File | Description |
|---|---|
| `learning_dataset.csv` | Student performance with aggregated engagement information |
| `risk_dataset.csv` | Student features and at-risk target |
| `risk_test_dataset.csv` | Independent test cases in CSV format |
| `data_summary.json` | Summary of processing records and dataset sizes |

The processed directory is created automatically when the pipeline runs.

## 11. Running the Data Pipeline

Activate the Python virtual environment and run:

```powershell
python -m src.data_loader
```

Alternatively:

```powershell
python -c "from src.data_loader import save_processed_datasets; save_processed_datasets()"
```

The pipeline prints a processing summary and the paths of generated files.

## 12. Model Training Integration

After successful data preparation, run:

```powershell
python -m src.train
```

The training script reads:

- `data/processed/risk_dataset.csv`
- `data/processed/risk_test_dataset.csv`

It trains the Random Forest model and saves the model and evaluation artifacts in `artifacts/`.

## 13. Pipeline Limitations

- Engagement data matching is limited to 57 of 1,000 student-subject records.
- Missing engagement aggregate values are filled with zero; the availability indicator should be considered during analysis.
- The original at-risk label generation process is unknown.
- Potential target leakage requires further investigation.
- The independent JSON test dataset contains only four prediction features.
- Additional validation is needed before using the pipeline with real-world educational data.

## 14. Future Improvements

- Investigate missing engagement records.
- Improve data integration coverage.
- Add more comprehensive data quality checks.
- Add explicit range validation for numeric fields.
- Add automated data pipeline tests.
- Improve data versioning and reproducibility.
- Validate the pipeline using additional datasets.

---

**Project:** EduTrack LMS
**Pipeline Module:** `src/data_loader.py`
**Data Processing Library:** Pandas
**Primary Language:** Python 3.11
