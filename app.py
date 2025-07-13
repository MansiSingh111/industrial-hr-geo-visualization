import streamlit as st
import pandas as pd
import plotly.express as px
import os
import numpy as np

st.set_page_config(layout="wide")
st.title("📊 Industrial Human Resource Geo-Visualization")

st.markdown("""
This dashboard provides an interactive view of the industrial workforce across Indian states.
Use the sidebar to filter by state and industry to explore trends in gender participation,
main vs marginal work types, and overall distribution.
""")


# Load data
@st.cache_data
def load_data():
    return pd.read_csv("merged_feature_engineered.csv")

df = load_data()


# Sidebar filters
states = sorted(df["indiastates"].unique())
selected_states = st.sidebar.multiselect("Select States", states, default=states)

industries = sorted(df["industry_group"].unique())
selected_industries = st.sidebar.multiselect("Select Industries", industries, default=industries)


filtered_df = df[df["indiastates"].isin(selected_states) & df["industry_group"].isin(selected_industries)]

if filtered_df.empty:
    st.warning("No data available for selected filters. Please select other options.")
    st.stop()



st.subheader("👷 Industry-wise Workforce Distribution")
industry_counts = filtered_df.groupby("industry_group")["total_workers"].sum().reset_index()
fig1 = px.bar(industry_counts, x="total_workers", y="industry_group", orientation="h", color="industry_group",
              labels={"total_workers": "Total Workers", "industry_group": "Industry Group"},
              title="Total Workers per Industry")
st.plotly_chart(fig1, use_container_width=True)


st.subheader("🚻 Gender-wise Participation")

gender_df = filtered_df.groupby("indiastates")[["main_males", "main_females", "marginal_males", "marginal_females"]].sum().reset_index()
fig2 = px.bar(gender_df, x="indiastates", y=["main_males", "main_females", "marginal_males", "marginal_females"],
              barmode="stack", title="Gender Distribution (Main & Marginal Workers)",
              labels={"value": "Workers", "indiastates": "States"})
st.plotly_chart(fig2, use_container_width=True)


st.subheader("🧑‍🏭 Main vs Marginal Workers by State")

worker_type_df = filtered_df.groupby("indiastates")[["total_main_workers", "total_marginal_workers"]].sum().reset_index()
fig3 = px.bar(worker_type_df, x="indiastates", y=["total_main_workers", "total_marginal_workers"],
              barmode="group", title="Main vs Marginal Workers",
              labels={"value": "Number of Workers", "indiastates": "State"})
st.plotly_chart(fig3, use_container_width=True)


st.subheader("🧩 TreeMap of Worker Distribution")
fig4 = px.treemap(filtered_df, path=["indiastates", "industry_group"], values="total_workers",
                  title="TreeMap: Workers by State and Industry")
st.plotly_chart(fig4, use_container_width=True)


st.header("🔍 Automated EDA Insights")

# 1 » Top industry groups
industry_counts = (
    filtered_df.groupby("industry_group")["total_workers"]
    .sum()
    .sort_values(ascending=False)
)
top_industry = industry_counts.idxmax()
top_industry_workers = int(industry_counts.max())

# 2 » State with the largest workforce
state_counts = (
    filtered_df.groupby("indiastates")["total_workers"]
    .sum()
    .sort_values(ascending=False)
)
top_state = state_counts.idxmax()
top_state_workers = int(state_counts.max())

# 3 » Overall gender totals
gender_tot = filtered_df[
    ["main_males", "main_females", "marginal_males", "marginal_females"]
].sum()
male_total = int(gender_tot["main_males"] + gender_tot["marginal_males"])
female_total = int(gender_tot["main_females"] + gender_tot["marginal_females"])

# 4 » Main vs marginal totals
main_total = int(filtered_df["total_main_workers"].sum())
marginal_total = int(filtered_df["total_marginal_workers"].sum())

# ---- KPI cards -----------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🏭 Top Industry", top_industry, delta=f"{top_industry_workers:,} workers")
col2.metric("📍 Top State",    top_state,    delta=f"{top_state_workers:,} workers")
col3.metric("♂️ Male Workers",   f"{male_total:,}")
col4.metric("♀️ Female Workers", f"{female_total:,}")

# ---- Drill‑down details in an expander -----------------------------
with st.expander("See detailed tables & ratios"):
    st.subheader("Top 5 Industries by Workforce")
    st.table(
        industry_counts.head(5)
        .reset_index()
        .rename(columns={"total_workers": "Workers"})
    )

    st.subheader("Top 5 States by Workforce")
    st.table(
        state_counts.head(5)
        .reset_index()
        .rename(columns={"total_workers": "Workers"})
    )

    # States with highest Main ↔ Marginal ratio
    mm_ratio = (
        filtered_df.groupby("indiastates")[["total_main_workers", "total_marginal_workers"]]
        .sum()
    )
    mm_ratio["main_to_marginal"] = mm_ratio["total_main_workers"] / mm_ratio["total_marginal_workers"].replace(0, np.nan)

    st.subheader("States with Highest Main : Marginal Ratio")
    st.table(
        mm_ratio.sort_values("main_to_marginal", ascending=False)
        .head(5)
        .reset_index()
        .round({"main_to_marginal": 2})
        .rename(columns={"main_to_marginal": "Ratio"})
    )

# ---- Quick narrative summary ---------------------------------------
st.markdown(f"""
**Key Take‑aways (current filters)**  
- **{top_industry}** is the most populous industry group, employing **{top_industry_workers:,}** workers.  
- **{top_state}** leads all states with **{top_state_workers:,}** total workers.  
- Gender split shows **{male_total:,}** males vs **{female_total:,}** females, echoing the disparity seen in the charts.  
- Full‑time (main) roles outnumber part‑time/seasonal (marginal) roles by **{main_total/marginal_total:.2f} : 1**.
""")
# --------------------------------------------------------------------
