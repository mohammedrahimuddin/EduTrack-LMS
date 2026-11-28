# Model Evaluation Metrics â€” EduTrack LMS

## 1. Introduction

This document describes the evaluation metrics used to assess the Random Forest-based student at-risk prediction model in EduTrack LMS.

The model is evaluated using an independent JSON test dataset containing 50 test cases.

The current implementation calculates Accuracy, Precision, Recall, F1-score, Confusion Matrix, and Classification Report.

## 2. Model Evaluation Setup

| Parameter | Description |
|---|---|
| Model | Random Forest Classifier |
| Training Dataset | `risk_dataset.csv` |
| Independent Test Dataset | `risk_test_dataset.csv` |
| Number of Test Cases | 50 |
| Target Column | `label_at_risk` |
| Positive Class | 1 (At Risk) |
| Negative Class | 0 (Not At Risk) |

The model uses four input features:

- `lessons_completed`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `streak_days`

## 3. Implemented Evaluation Metrics

### 3.1 Accuracy

Accuracy measures the proportion of total predictions that are correct.

Formula:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Where:

- TP = True Positives
- TN = True Negatives
- FP = False Positives
- FN = False Negatives

### 3.2 Precision

Precision measures how many students predicted as at risk are actually at risk according to the test labels.

Formula:

Precision = TP / (TP + FP)

Higher precision means fewer false positive predictions.

### 3.3 Recall

Recall measures how many actual at-risk students are correctly identified by the model.

Formula:

Recall = TP / (TP + FN)

Recall is important because missing students who genuinely need academic support can be harmful.

### 3.4 F1-Score

F1-score is the harmonic mean of Precision and Recall.

Formula:

F1 = 2 Ã— (Precision Ã— Recall) / (Precision + Recall)

It provides a combined measure of precision and recall.

### 3.5 Confusion Matrix

The confusion matrix summarizes correct and incorrect predictions.

| Actual / Predicted | Not At Risk (0) | At Risk (1) |
|---|---|---|
| Not At Risk (0) | True Negative | False Positive |
| At Risk (1) | False Negative | True Positive |

The current training implementation saves the confusion matrix in `risk_metrics.json`.

### 3.6 Classification Report

The model training script also generates a classification report containing:

- Precision
- Recall
- F1-score
- Support

The report is saved inside `risk_training_summary.json`.

## 4. Initial Independent Test Results

The initial recorded results are:

| Metric | Result |
|---|---:|
| Accuracy | 0.46 |
| Precision | 0.6364 |
| Recall | 0.2333 |
| F1-score | 0.3415 |

These results are preliminary and indicate that the current model requires further improvement.

The relatively low recall indicates that the model misses a number of actual at-risk cases.

## 5. Additional Proposed Evaluation Metrics

The following metrics are proposed for future evaluation. They are not currently calculated by the existing training implementation.

### 5.1 ROC-AUC

ROC-AUC measures the model's ability to distinguish between positive and negative classes across different classification thresholds.

It can provide additional insight into classification performance beyond a single threshold.

### 5.2 Specificity

Specificity measures the proportion of actual not-at-risk students correctly classified.

Formula:

Specificity = TN / (TN + FP)

### 5.3 Balanced Accuracy

Balanced accuracy calculates the average recall across the two classes.

Formula:

Balanced Accuracy = (Sensitivity + Specificity) / 2

These additional metrics can help evaluate performance when class distribution is imbalanced.

## 6. Recommendation System Evaluation

The current verified Python implementation does not contain a Matrix Factorization recommendation model.

Therefore, recommendation evaluation metrics are listed as future work and are not presented as completed experimental results.

Potential metrics for a future recommendation component include:

| Metric | Purpose |
|---|---|
| Precision@K | Measures relevant recommendations among the top K results |
| Recall@K | Measures how many relevant items are retrieved in the top K |
| NDCG@K | Measures ranking quality while considering recommendation positions |

These metrics should only be calculated after a recommendation model and suitable ground-truth interaction data are implemented and evaluated.

## 7. Evaluation Limitations

The current evaluation has several limitations:

- The independent test dataset contains only 50 cases.
- The original target-label generation rule is unknown.
- Potential target leakage requires investigation.
- Independent test performance is currently weak.
- The model has not been validated on additional external datasets.
- ROC-AUC and other proposed metrics have not yet been implemented.

## 8. Future Evaluation Improvements

- Investigate the original target-label generation process.
- Improve recall for at-risk students.
- Evaluate the model using additional independent datasets.
- Add ROC-AUC, specificity, and balanced accuracy calculations.
- Examine confusion matrix results for both classes.
- Expand automated testing.
- Evaluate recommendation metrics after implementing a recommendation model.

## 9. Implementation References

The evaluation logic is implemented in:

- `src/train.py` â€” model training and metric calculation.
- `src/config.py` â€” model artifact paths and random state.
- `tests/test_risk_model.py` â€” basic model training and prediction tests.

Generated evaluation files:

- `artifacts/risk_metrics.json`
- `artifacts/risk_training_summary.json`

---

**Project:** EduTrack LMS
**Evaluation Model:** Random Forest Classifier
**Evaluation Dataset:** Independent 50-case JSON test dataset
