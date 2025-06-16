import streamlit as st
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import seaborn as sns

# Load evaluation config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

evaluations = {ev["name"]: ev for ev in config["evaluations"]}

# Sidebar
st.sidebar.title("🧪 Evaluation Dashboard")
selected_name = st.sidebar.selectbox("Choose Evaluation", list(evaluations.keys()))
selected_eval = evaluations[selected_name]

# Title and intro
st.title(selected_name)

with open(selected_eval["description_file"], "r", encoding="utf-8") as f:
    st.markdown(f.read())

# RATER vs OpenAI Evaluation
if selected_eval["id"] == "rater_vs_openai":
    df = pd.read_csv(selected_eval["data_file"])

    # Total preference chart across Claim, Evidence, Overall
    total_df = df.groupby("Metric")[["Prefer RATER", "Prefer OpenAI Only", "No Preference"]].sum().reset_index()
    melted_total = total_df.melt(id_vars="Metric", var_name="Preference", value_name="Count")

    st.subheader("📊 Total Preferences by Metric")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=melted_total, x="Metric", y="Count", hue="Preference", ax=ax1, ci=None)

    for bar in ax1.patches:
        height = bar.get_height()
        if height > 0:
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1, f"{int(height)}", ha='center')
    st.pyplot(fig1)

    # Grade-specific view
    st.subheader("🎓 Filter by Grade and Metric")
    metric = st.selectbox("Metric", sorted(df["Metric"].unique()))
    grade = st.selectbox("Grade", ["All"] + sorted(df["Grade"].unique()))
    filtered = df[df["Metric"] == metric]
    if grade != "All":
        filtered = filtered[filtered["Grade"] == grade]

    melted = filtered.melt(id_vars=["Grade", "Metric"],
                           value_vars=["Prefer RATER", "Prefer OpenAI Only", "No Preference"],
                           var_name="Preference", value_name="Count")

    st.subheader(f"Preferences for {metric} ({'All Grades' if grade == 'All' else 'Grade ' + str(grade)})")

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=melted, x="Grade", y="Count", hue="Preference", ax=ax2, ci=None)
    for bar in ax2.patches:
        height = bar.get_height()
        if height > 0:
            ax2.text(bar.get_x() + bar.get_width()/2., height + 1, f"{int(height)}", ha='center')
    st.pyplot(fig2)

# Narrative Autoscoring Evaluation
elif selected_eval["id"] == "narrative_autoscoring":
    st.subheader("Narrative Autoscoring Breakdown")
    st.markdown(
        "This evaluation contains two perspectives:\n- **Rubric Agreement** (Sheet 1)\n- **Over/Under Rating** (Sheet 2)")

    sheet = st.radio("Select View", ["Rubric Agreement", "Over/Under/Match"])
    xls = pd.ExcelFile(selected_eval["data_file"])

    if sheet == "Rubric Agreement":
        st.subheader(f"📊 Total Score agreement ")
        df = xls.parse(xls.sheet_names[0])
        st.dataframe(df)

            # Plot Total Agreement Score (from "Total" row)
        score_df = df.copy()
        score_df_clean = score_df[score_df['Grade'] != 'Total'].copy()
        criteria_cols = score_df_clean.columns[1:]

        score_df_total = score_df[score_df['Grade'] == 'Total'].copy()
        total_score_pct = {}
        for col in criteria_cols:
            score_str = score_df_total[col].values[0]
            score, total = map(float, score_str.split('/'))
            total_score_pct[col] = (score / total) * 100

        st.subheader("📊 Total Score Agreement by Criterion (from Total row)")
        fig2, ax = plt.subplots(figsize=(10, 6))
        bars = sns.barplot(x=list(total_score_pct.keys()), y=list(total_score_pct.values()), ax=ax)
        ax.set_ylabel("Score Agreement (%)")
        ax.set_title("Total Score Agreement by Criterion")
        plt.xticks(rotation=45, ha='right')

        for bar in bars.patches:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 1, f"{height:.1f}%", ha='center')

        st.pyplot(fig2)
    else:
        xls = pd.ExcelFile(selected_eval["data_file"])
        rating_df = xls.parse("underrating_overrating_matching")

        # Extract columns with underrating/overrating/matching values
        criteria_columns_comp = [col for col in rating_df.columns if 'underrating/overrating/matching' in col]

        # Build long-form data
        comparison_data = []
        for _, row in rating_df.iterrows():
            for col in criteria_columns_comp:
                val = row[col]
                if isinstance(val, str) and '\\' in val:
                    parts = val.strip().split('\\')
                    if len(parts) == 3:
                        underrating, overrating, matching = map(int, parts)
                        comparison_data.append({
                            'Grade': str(row['Grade']),
                            'Criterion': col.replace(' underrating/overrating/matching', ''),
                            'Underrating': underrating,
                            'Overrating': overrating,
                            'Matching': matching
                        })

        comp_df = pd.DataFrame(comparison_data)
        comp_df = comp_df[comp_df['Grade'] != 'Total']

        # Grade selection
        st.subheader("🎓 Rating Distribution by Criterion")
        grade_to_plot = st.selectbox("Select Grade", sorted(comp_df["Grade"].unique()))

        single_grade_df = comp_df[comp_df["Grade"] == grade_to_plot]
        melted_single = single_grade_df.melt(
            id_vars="Criterion",
            value_vars=["Underrating", "Overrating", "Matching"],
            var_name="Rating Type", value_name="Count"
        )

        # Plot bar chart
        st.subheader(f"📊 Rating Distribution - Grade {grade_to_plot}")
        fig, ax = plt.subplots(figsize=(10, 6))
        barplot = sns.barplot(data=melted_single, x='Criterion', y='Count', hue='Rating Type', ax=ax)
        for bar in barplot.patches:
            height = bar.get_height()
            if height > 0:
                barplot.annotate(f'{int(height)}', (bar.get_x() + bar.get_width() / 2, height + 1),
                                 ha='center', va='bottom')

        # Show total responses below
        single_grade_df['Total Responses'] = single_grade_df[['Underrating', 'Overrating', 'Matching']].sum(axis=1)
        st.markdown("**Total Responses per Criterion:**")
        st.dataframe(single_grade_df[['Criterion', 'Total Responses']].reset_index(drop=True))

        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

