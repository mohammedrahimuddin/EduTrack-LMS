# A/B Test Design — EduTrack LMS

## 1. Objective and Hypothesis

Evaluate whether personalized learning recommendations improve learner engagement compared with the standard course catalogue.

**Hypothesis:** Learners assigned to personalized recommendations (Treatment B) will have a higher seven-day enrollment rate in a recommended course than learners using the standard catalogue (Control A).

## 2. Experiment Design

- **Population:** Eligible active learners.
- **Randomization:** Stable learner-ID assignment, one assignment per learner.
- **Control Group (A):** Existing course discovery experience.
- **Treatment Group (B):** Top-five EduTrack learning recommendations.
- **Duration:** At least two full weeks and until the pre-registered sample-size target is reached.

## 3. Evaluation Metrics

### Primary Metric
Proportion of learners enrolling in at least one recommended course within seven days.

### Secondary Metrics
- Recommendation click-through rate.
- Course start rate.
- Course completion rate.
- Time to first enrollment.

### Guardrail Metrics
- Course withdrawals.
- Learner complaints.
- API errors.
- API response latency.
- Subgroup outcomes.

## 4. Statistical Analysis

Before launching the experiment:

- Define the baseline enrollment rate.
- Define the minimum detectable effect.
- Set significance level (alpha) to 0.05.
- Set statistical power to 0.80.
- Calculate the required sample size.

Analyze results using the intention-to-treat approach.

Report:
- Absolute lift.
- Relative lift.
- 95% confidence intervals.
- Group balance.
- Primary and secondary metric results.

Avoid unplanned repeated significance checks.

## 5. Risks and Mitigation

- Use stable learner assignment to reduce contamination.
- Run the experiment across multiple weeks to reduce novelty effects.
- Log recommendation impressions to measure actual exposure.
- Audit permitted learner cohorts for disparate outcomes.
- Monitor API reliability and response latency.

## 6. Current Experiment Status

**Status:** Planned — Not yet conducted.

No improvement in learner engagement or enrollment is claimed because the experiment has not been run.

## 7. Future Steps

1. Validate the recommendation system.
2. Prepare experiment tracking and logging.
3. Define baseline metrics and sample size.
4. Randomly assign eligible learners.
5. Run the experiment.
6. Analyze results and document findings.