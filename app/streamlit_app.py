import requests
import streamlit as st

st.set_page_config(
    page_title="EduTrack LMS",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduTrack LMS")
st.subheader("AI-Powered Student At-Risk Prediction System")

st.write(
    "Enter student learning details to predict whether "
    "the student may be at risk."
)

with st.sidebar:
    st.header("API Configuration")

    api_url = st.text_input(
        "API URL",
        "http://127.0.0.1:8000"
    )

    st.info("Make sure the FastAPI server is running.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Student Learning Details")

    lessons_completed = st.number_input(
        "Lessons Completed",
        min_value=0,
        max_value=40,
        value=20
    )

    avg_time = st.number_input(
        "Average Time Per Lesson (minutes)",
        min_value=0.0,
        value=25.0
    )

with col2:
    st.subheader("Learning Activity")

    quiz_attempts = st.number_input(
        "Quiz Attempts",
        min_value=0,
        value=3
    )

    streak_days = st.number_input(
        "Learning Streak (Days)",
        min_value=0,
        value=10
    )

st.divider()

if st.button("Predict Student Risk", type="primary"):

    payload = {
        "lessons_completed": lessons_completed,
        "avg_time_per_lesson_mins": avg_time,
        "quiz_attempts": quiz_attempts,
        "streak_days": streak_days
    }

    try:
        response = requests.post(
            f"{api_url.rstrip('/')}/predict",
            json=payload,
            timeout=10
        )

        response.raise_for_status()
        result = response.json()

        st.subheader("Prediction Results")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            if result["prediction"] == 1:
                st.error("⚠️ Student At Risk")
            else:
                st.success("✅ Student Not At Risk")

        with result_col2:
            risk_score = result["risk_probability"]
            st.metric(
                "Model Risk Score",
                f"{risk_score:.2%}"
            )

        st.progress(risk_score)

        st.caption(
            "Risk score is an uncalibrated model estimate, "
            "not a confirmed probability."
        )

    except requests.RequestException as exc:
        st.error(f"API request failed: {exc}")
        st.warning("Start the FastAPI server and try again.")

st.divider()

st.caption(
    "EduTrack LMS | AI-Powered Adaptive Learning System"
)