# Model Card — EduTrack LMS

## 1. Purpose

EduTrack LMS is an AI-powered learning support system designed to analyze student performance, identify students who may be at risk, and support personalized learning recommendations.

## 2. Model

**Primary prediction model:** Random Forest Classifier.

**Target:** `label_at_risk`

**Training dataset:** Official student performance dataset containing 1,000 records.

**Target distribution:**
- Not at risk (0): 850
- At risk (1): 150

## 3. Input Features

The initial risk prediction model uses:

- `lessons_completed`
- `avg_time_per_lesson_mins`
- `quiz_attempts`
- `streak_days`

The official JSON test dataset contains 50 independent test cases.

## 4. Evaluation

The initial four-feature Random Forest model was evaluated on the independent JSON test dataset.

| Metric | Result |
|---|---:|
| Accuracy | 0.46 |
| Precision | 0.6364 |
| Recall | 0.2333 |
| F1-score | 0.3415 |
| Test cases | 50 |

These results indicate that the initial model requires improvement. They do not establish reliable at-risk detection.

## 5. Data Analysis Findings

Analysis of the official dataset found:

- Post-test scores are strongly associated with the at-risk label.
- All 775 students with post-test scores above 50 are labelled not at risk.
- Among 225 students with post-test scores of 50 or below, 150 are at risk and 75 are not at risk.
- Learning activity features show relatively small differences between the two label groups.
- The exact rule used to generate `label_at_risk` is currently unknown.

## 6. Data Limitations and Potential Target Leakage

Pre-test score, post-test score and score improvement show strong associations with the target label.

Score improvement is calculated as:

`score_improvement = post_test_score - pre_test_score`

Therefore, score improvement is not an independent feature.

Using test scores for prediction may introduce target leakage if these scores were used to generate the original labels. The exact label-generation process has not been documented or verified.

The 50-case JSON test dataset does not contain pre-test or post-test scores, so score-based exploratory models cannot be evaluated directly on that test dataset.

## 7. Known Limitations

- The initial four-feature model has weak independent test performance.
- The independent test dataset has a different class distribution from the training dataset.
- The engagement dataset matches only a small proportion of student-subject records.
- Missing engagement matches must not automatically be interpreted as zero engagement.
- The original target-label generation process is unknown.
- Offline evaluation does not demonstrate actual improvement in student learning.

## 8. Human Oversight

Predictions should be treated as decision-support signals, not final judgments about students.

Educators should review student progress and additional context before taking action.

The model must not be the sole basis for grading, admission, academic progression or other high-impact decisions.

## 9. Monitoring and Future Improvements

- Monitor precision, recall, F1-score and confusion matrix.
- Check class imbalance and prediction errors.
- Validate new datasets before retraining.
- Investigate the original label-generation process.
- Evaluate models without target leakage.
- Improve engagement-data coverage and validation.
- Conduct real-world evaluation before claiming learning benefits.