from pathlib import Path
import numpy as np
import pandas as pd
import json

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)
students = [f"S{i:03d}" for i in range(1, 81)]
courses = [f"C{i:03d}" for i in range(1, 31)]
student_topics = {s: int(rng.integers(0, 5)) for s in students}
course_topics = {c: i % 5 for i, c in enumerate(courses)}
rows = []
for student in students:
    for course in rng.choice(courses, size=int(rng.integers(8, 17)), replace=False):
        match = student_topics[student] == course_topics[course]
        rating = float(np.clip(rng.normal(4.0 if match else 2.2, 0.7), 1, 5))
        rows.append({"student_id": student, "course_id": course, "rating": round(rating, 2)})
df = pd.DataFrame(rows)
df.to_csv(RAW / "aiml_student_performance.csv", index=False)
df.sample(frac=0.35, random_state=42).to_csv(RAW / "aiml_content_engagement.csv", index=False)
(RAW / "aiml_edtech_tests.json").write_text(json.dumps({"dataset": "synthetic_demo", "note": "Replace with official portal data."}, indent=2), encoding="utf-8")
print(f"Demo data generated in {RAW}")
