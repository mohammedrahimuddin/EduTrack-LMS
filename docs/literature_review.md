# Literature Review – EduTrack LMS

## 1. Introduction

Educational institutions increasingly use machine learning and learning analytics to understand student performance, monitor learning engagement, and provide personalized learning support.

EduTrack LMS is an AI-powered learning support project that focuses on identifying students who may be at academic risk using student performance and engagement data. It also includes a personalized learning recommendation component.

This literature review examines three research papers related to student performance prediction, early prediction using LMS activity logs, and personalized course recommendation systems.

The reviewed studies provide a foundation for understanding existing approaches, algorithms, datasets, evaluation methods, and research limitations.

---

## 2. Review of Existing Research Papers

### 2.1 Paper 1: Machine Learning for Student Performance Prediction

**Title:** Contextualizing the Current State of Research on the Use of Machine Learning for Student Performance Prediction: A Systematic Literature Review

**Authors:** Khalid Alalawi, Rukshan Athauda, and Raymond Chiong

**Year:** 2023

**Journal:** Engineering Reports, 5(12), e12699

**DOI:** https://doi.org/10.1002/eng2.12699

**Research Objective:**

The study investigates how machine learning techniques have been applied to predict student academic performance and identify students at risk of failing or dropping out.

**Methodology:**

The authors conducted a systematic literature review using the Kitchenham methodology. They reviewed 162 research articles published between January 2010 and October 2022.

The review covered classification, regression, and clustering techniques used in educational prediction systems.

**Techniques Identified:**

- Decision Tree
- Random Forest
- Naive Bayes
- Artificial Neural Networks
- Support Vector Machine

**Key Findings:**

The review identified two major research categories:

- 129 studies focused on academic performance prediction and identifying students at risk.
- 33 studies focused on student dropout and retention prediction.

Historical grades, LMS-related information, and demographic characteristics were among the commonly used features.

**Research Limitations:**

The review identified a need for further research into interventions following the identification of at-risk students. Its findings are also limited to the literature covered up to October 2022.

**Relevance to EduTrack LMS:**

This study provides the research foundation for using machine learning to identify students who may require academic support. EduTrack uses student performance and learning engagement information for at-risk prediction.

---

### 2.2 Paper 2: Early Prediction of Student Performance Using LMS Logs

**Title:** Accurate, Timely, and Portable: Course-Agnostic Early Prediction of Student Performance from LMS Logs

**Authors:** Ricardo Miguel Santos and Roberto Henriques

**Year:** 2023

**Journal:** Computers and Education: Artificial Intelligence, Volume 5, Article 100175

**DOI:** https://doi.org/10.1016/j.caeai.2023.100175

**Research Objective:**

The research aims to identify at-risk and high-performing students at early stages of course completion by analyzing activity logs collected from a Learning Management System.

**Dataset:**

The researchers used Moodle LMS activity logs collected from an information management school during the 2020–2021 academic year. They also conducted a supplementary analysis using data from the University of Oviedo to investigate generalizability.

**Methodology:**

The researchers compared traditional machine learning classifiers with Long Short-Term Memory (LSTM) models.

Predictions were evaluated at different course-completion stages:

- 10%
- 25%
- 33%
- 50%
- 100%

The study examined static aggregated LMS activity features and time-dependent click activity.

**Techniques Used:**

- Random Forest
- Extra Trees
- Logistic Regression
- Support Vector Machine
- Other traditional machine learning classifiers
- Long Short-Term Memory (LSTM)

**Key Findings:**

The study reported an AUC of 0.756 for at-risk student prediction using all course data. Random Forest performed best for this task.

The researchers found that useful early predictions were possible from as early as 25% of course completion.

Their findings also showed that traditional static-feature models generally performed better than the tested LSTM models, although LSTM offered some practical advantages in early prediction settings.

**Research Limitations:**

The findings may vary across institutions and learning environments. The authors also identified limitations related to feature extraction, generalizability, and the need for further validation in real-world educational settings.

**Relevance to EduTrack LMS:**

This paper supports the use of student engagement information for early identification of at-risk students.

EduTrack uses features such as lessons completed, average time per lesson, quiz attempts, and streak days. These features represent learning activity and engagement patterns that are conceptually related to the LMS activity features discussed in the research.

---

### 2.3 Paper 3: Personalized Course Recommendation Using Deep Learning

**Title:** DORIS: Personalized Course Recommendation System Based on Deep Learning

**Authors:** Yinping Ma, Rongbin Ouyang, Xinzheng Long, Zhitong Gao, Tianping Lai, and Chun Fan

**Year:** 2023

**Journal:** PLOS ONE, Volume 18, Issue 6, Article e0284687

**DOI:** https://doi.org/10.1371/journal.pone.0284687

**Research Objective:**

The study proposes a personalized course recommendation system that suggests suitable courses to students based on their academic information, interests, historical course selections, and course characteristics.

**Dataset:**

The researchers collected anonymized data from Peking University covering 2014 to 2021.

The dataset contained:

- 4,568 students
- 5,591 courses
- 208,949 course enrollments
- 53 academic departments

**Methodology:**

The researchers proposed DORIS, a recommendation system based on Deep Factorization Machine (DeepFM).

It combines two components:

- Factorization Machine (FM) for learning feature interactions.
- Deep Neural Network (DNN) for learning complex, high-order feature relationships.

The researchers also used TextRank and Principal Component Analysis (PCA) to process course descriptions.

**Evaluation Metrics:**

- Area Under the Curve (AUC)
- LogLoss

**Key Findings:**

DORIS achieved an AUC of 0.9693 and LogLoss of 0.0349 in the reported experiments.

It outperformed the compared baseline methods, including BPR, DSSM, Logistic Regression, Factorization Machine, and DECOR.

**Research Limitations:**

The authors acknowledged that the proposed method does not completely solve the cold-start problem. They suggested collecting additional student information and exploring transfer learning.

They also recommended investigating more capable text encoders such as CNN, RNN, and BERT.

**Relevance to EduTrack LMS:**

This research supports the personalized recommendation component of EduTrack LMS.

The study demonstrates how student profiles and learning history can be used to recommend suitable courses. EduTrack uses a Matrix Factorization-based recommendation approach with a cold-start fallback to generate personalized top-five learning recommendations.

---

## 3. Comparative Analysis of Research Papers

| Research Paper | Main Focus | Techniques | Evaluation |
|---|---|---|---|
| Alalawi et al. (2023) | Student performance prediction | Random Forest, Decision Tree, SVM, ANN | Systematic literature review |
| Santos & Henriques (2023) | Early at-risk prediction using LMS logs | Random Forest, Extra Trees, LSTM | AUC, Accuracy |
| Ma et al. (2023) | Personalized course recommendation | DeepFM, FM, DNN | AUC, LogLoss |

### Comparative Discussion

The reviewed studies address different but related challenges in educational technology.

The first paper provides a broad overview of machine learning applications in student performance prediction. The second demonstrates how LMS activity logs can support early identification of students who may be at risk. The third focuses on personalized course recommendations using student profiles, historical course selections, and course information.

Together, these studies provide a foundation for developing an educational support system that combines student risk prediction and personalized learning recommendations.

---

## 4. Research Gaps Identified

Based on the reviewed studies, the following research opportunities were identified:

1. Student performance prediction and personalized course recommendation are often investigated as separate research problems.
2. Student engagement information can provide additional signals for identifying learners who may require academic support.
3. Cold-start and sparse interaction data remain important challenges in recommendation systems.
4. Prediction systems require independent evaluation to understand their actual performance.
5. Identifying at-risk students should be followed by appropriate learning support and intervention strategies.

These observations motivate the development of EduTrack LMS as a learning support project that combines student risk prediction with personalized learning recommendations.

---

## 5. Proposed EduTrack LMS Approach

EduTrack LMS focuses on two related components.

### 5.1 Student At-Risk Prediction

The project uses student performance and learning engagement data to predict whether a student may be at risk.

The initial Random Forest model uses four input features:

- lessons_completed
- avg_time_per_lesson_mins
- quiz_attempts
- streak_days

The project also includes preprocessing, exploratory data analysis, model persistence, and independent JSON test evaluation.

### 5.2 Personalized Learning Recommendation

The recommendation component uses Matrix Factorization to identify learning recommendations based on student-item interaction information.

A cold-start fallback is included to provide recommendations when sufficient historical interaction information is unavailable.

The system is designed to generate the top five recommendations.

---

## 6. Conclusion

The reviewed research demonstrates the importance of machine learning, learning analytics, and recommendation techniques in educational systems.

The studies provide useful foundations for student performance prediction, early identification of at-risk learners, and personalized course recommendation.

EduTrack LMS builds on these research directions by combining an initial student at-risk prediction model with a personalized learning recommendation component.

The current implementation requires further validation and improvement before it can be considered suitable for real-world deployment.

---

## 7. References

1. Alalawi, K., Athauda, R., & Chiong, R. (2023). Contextualizing the current state of research on the use of machine learning for student performance prediction: A systematic literature review. *Engineering Reports, 5*(12), e12699. https://doi.org/10.1002/eng2.12699

2. Santos, R. M., & Henriques, R. (2023). Accurate, timely, and portable: Course-agnostic early prediction of student performance from LMS logs. *Computers and Education: Artificial Intelligence, 5*, 100175. https://doi.org/10.1016/j.caeai.2023.100175

3. Ma, Y., Ouyang, R., Long, X., Gao, Z., Lai, T., & Fan, C. (2023). DORIS: Personalized course recommendation system based on deep learning. *PLOS ONE, 18*(6), e0284687. https://doi.org/10.1371/journal.pone.0284687
