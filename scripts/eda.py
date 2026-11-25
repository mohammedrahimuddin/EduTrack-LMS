
import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
CHARTS = REPORTS / "charts"

CHARTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA / "learning_dataset.csv")
content = pd.read_csv(ROOT / "data" / "raw" / "aiml_content_engagement.csv")

sns.set_theme(style="whitegrid")

# 1. At-risk distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="label_at_risk")
plt.title("At-Risk Student Distribution")
plt.xlabel("At Risk (0 = No, 1 = Yes)")
plt.ylabel("Number of Students")
plt.savefig(CHARTS / "at_risk_distribution.png", dpi=150, bbox_inches="tight")
plt.close()

# 2. Subject-wise performance
plt.figure(figsize=(11, 6))
sns.barplot(data=df, x="subject", y="post_test_score", errorbar=None)
plt.xticks(rotation=45, ha="right")
plt.title("Average Post-Test Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Post-Test Score")
plt.savefig(CHARTS / "subject_performance.png", dpi=150, bbox_inches="tight")
plt.close()

# 3. Pre-test vs post-test
score_data = df[["pre_test_score", "post_test_score"]].mean().reset_index()
score_data.columns = ["Test Type", "Average Score"]

plt.figure(figsize=(7, 5))
sns.barplot(data=score_data, x="Test Type", y="Average Score")
plt.title("Pre-Test vs Post-Test Average Scores")
plt.savefig(CHARTS / "score_comparison.png", dpi=150, bbox_inches="tight")
plt.close()

# 4. Completion percentage
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="completion_pct", bins=20, kde=True)
plt.title("Student Lesson Completion Distribution")
plt.xlabel("Completion Percentage")
plt.savefig(CHARTS / "completion_distribution.png", dpi=150, bbox_inches="tight")
plt.close()

# 5. Engagement by content type
plt.figure(figsize=(9, 5))
sns.barplot(data=content, x="content_type", y="engagement_score", errorbar=None)
plt.xticks(rotation=35, ha="right")
plt.title("Average Engagement by Content Type")
plt.savefig(CHARTS / "content_engagement.png", dpi=150, bbox_inches="tight")
plt.close()

# 6. At-risk vs score improvement
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="label_at_risk", y="score_improvement")
plt.title("Score Improvement vs At-Risk Status")
plt.xlabel("At Risk (0 = No, 1 = Yes)")
plt.savefig(CHARTS / "risk_score_improvement.png", dpi=150, bbox_inches="tight")
plt.close()

# Generate summary
summary = {
    "total_students": int(df["student_id"].nunique()),
    "total_records": len(df),
    "at_risk_students": int(df["label_at_risk"].sum()),
    "not_at_risk_students": int((df["label_at_risk"] == 0).sum()),
    "average_pre_test_score": round(float(df["pre_test_score"].mean()), 2),
    "average_post_test_score": round(float(df["post_test_score"].mean()), 2),
    "average_score_improvement": round(float(df["score_improvement"].mean()), 2),
    "average_completion_pct": round(float(df["completion_pct"].mean()), 2),
    "average_engagement_score": round(float(content["engagement_score"].mean()), 3),
    "average_post_test_by_subject": {
        str(k): round(float(v), 2)
        for k, v in df.groupby("subject")["post_test_score"].mean().items()
    },
}

(REPORTS / "eda_summary.json").write_text(
    json.dumps(summary, indent=2),
    encoding="utf-8"
)

print("\nEDA COMPLETED SUCCESSFULLY")
print(json.dumps(summary, indent=2))
print(f"\nCharts saved in: {CHARTS}")
