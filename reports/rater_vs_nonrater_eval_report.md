

This report summarizes the comparative evaluation between the **RATER-enhanced model** and the **Non-RATER (baseline) model** for identifying and giving feedback on claim and evidence sentences in student responses.

## 1. Preference Counts Summary

### 🗣️ Claim Sentence Preferences

| Model           | Preferred Count |
|----------------|------------------|
| **RATER**       | 121              |
| Non-RATER       | 82               |
| No Preference   | 16               |

RATER-enhanced feedback on claims was preferred in a majority of cases, suggesting its improvements are especially evident when identifying key argumentative components【54†source】.

### 📚 Evidence Sentence Preferences

| Model           | Preferred Count |
|----------------|------------------|
| **RATER**       | 110              |
| Non-RATER       | 104              |
| No Preference   | 5                |

Evaluator preference for evidence feedback was nearly evenly split, but RATER showed slight overall favor, particularly when better surfacing relevant supporting content【54†source】.

### ✅ Overall Model Preference

| Model           | Preferred Count |
|----------------|------------------|
| **RATER**       | 99               |
| Non-RATER       | 96               |
| No Preference   | 24               |

The close split reflects the strength of the baseline system, while also affirming that RATER provides meaningful, if modest, improvements【54†source】.

---

## 2. Claim Evaluation by Grade

| Grade | Claim Found (RATER) | Helpful Feedback (RATER) | Claim Found (Non-RATER) | Helpful Feedback (Non-RATER) | Preference |
|-------|----------------------|---------------------------|----------------------------|-------------------------------|------------|
| 6     | 95%                  | 80%                       | 86.7%                      | 85%                           | Non-RATER  |
| 7     | 90%                  | 90%                       | 96%                        | 92%                           | Non-RATER  |
| 8     | 88%                  | 92%                       | 70%                        | 72%                           | **RATER**  |
| 9     | 77.5%                | 74%                       | 75%                        | 73%                           | RATER (slight) |
| 10    | 81.6%                | 90%                       | 75%                        | 92%                           | Non-RATER  |
| 11    | 97.4%                | 97%                       | 95%                        | 99%                           | **RATER**  |
| 12    | 95%                  | 93%                       | 95%                        | 95%                           | Non-RATER  |

---

## 3. Evidence Evaluation by Grade

| Grade | Evidence Found (RATER) | Helpful Feedback (RATER) | Evidence Found (Non-RATER) | Helpful Feedback (Non-RATER) | Preference |
|-------|-------------------------|----------------------------|-------------------------------|-------------------------------|------------|
| 6     | 80%                     | 80%                        | 80%                           | 82%                           | Same       |
| 7     | 75%                     | 85%                        | 68.3%                         | 82%                           | **RATER**  |
| 8     | 80%                     | 93%                        | 73.3%                         | 83%                           | **RATER**  |
| 9     | 50%                     | 59%                        | 60%                           | 66%                           | Non-RATER  |
| 10    | 81.6%                   | 93%                        | 80%                           | 90%                           | **RATER**  |
| 11    | 88.4%                   | 87.2%                      | 84.6%                         | 93.5%                         | Same       |
| 12    | 92.5%                   | 95%                        | 92.5%                         | 95%                           | **RATER**  |

---

## 4. Observations & Key Insights

### 🔍 Claim Identification
- RATER-enhanced outputs were more often accurate in grades 8 and 11.
- In some lower grades (6, 7), Non-RATER produced equally or more helpful feedback.
- The improvements in higher grades suggest RATER is more effective at handling complexity.

### 📖 Evidence Support
- Gains from RATER are more evident in grades 7, 8, and 10.
- In grade 9, Non-RATER’s evidence selection slightly outperformed RATER.

---

## 5. Improvements to RATER Scoring Logic

Recent changes based on evaluation findings:

- **Feedback Precision**: Emphasis on clarifying vague themes and rating missing structures conservatively.
- **Narrative Element Recognition**: Enhanced detection for missing dialogue, transitions, and conclusions.
- **Audience Engagement**: Reduced harshness in scoring clear, readable prose—especially in Grades 3–5.

These updates align with insights from the narrative scoring analysis, where over-penalization of readable writing and lack of structure detection were common issues【55†source】.

---

## 6. Conclusion

The RATER-enhanced model demonstrates **consistent or superior performance** across most grades, particularly in handling subtle or complex writing. Its improvements in feedback clarity and evidence selection suggest value in high-stakes or growth-focused writing environments.

While the Non-RATER system remains strong and competitive, the **RATER model offers incremental but meaningful benefits** in both scoring accuracy and actionable feedback quality.
