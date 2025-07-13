# 📊 Industrial Human Resource Geo-Visualization

This project visualizes the industrial classification of India's workforce using interactive dashboards, exploratory data analysis (EDA), and charts. It highlights employment trends by **gender**, **worker type (main vs marginal)**, and **industrial sectors** across Indian states.

---

## 📌 Problem Statement

In India, understanding the industrial distribution of the workforce is crucial for effective planning and policy-making. The classification of main and marginal workers — excluding cultivators and agricultural laborers — provides insights into economic structure and labor trends across states.

However, raw classification tables are often non-interactive and difficult to interpret. This project addresses that gap by:

- Analyzing and visualizing industrial workforce patterns by sector, gender, and geography.
- Comparing **main** vs **marginal** worker employment.
- Creating an interactive dashboard to explore the data intuitively.

---

## 🧰 Technologies Used

- **Python**
- **Pandas** – Data manipulation and cleaning  
- **Seaborn & Matplotlib** – Static plots for EDA  
- **Plotly** – Interactive visualizations  
- **Streamlit** – Web-based dashboard development  
- **Jupyter Notebook** – Exploratory analysis and scripting  

---

## 📂 Project Structure

```
📁 industrial-hr-geo-visualisation/
│
├── 📜 app.py                      # Streamlit dashboard script
├── 📓 EDA_and_scripts.ipynb      # Full EDA and preprocessing notebook
├── 📁 data/
│   ├── merged_cleaned_data.csv
│   ├── merged_feature_engineered.csv
│   └── 📁 eda_charts/
│       ├── industry_worker_distribution.png
│       ├── state_worker_distribution.png
│       ├── main_vs_marginal_workers.png
│       ├── main_workers_gender.png
│       ├── marginal_workers_gender.png
│       ├── worker_distribution_histogram.png
│       ├── dominant_industry_by_state.png
│       ├── interactive_barplot.html
│       └── interactive_treemap.html
```

---

## 📊 Sample Visuals

### 🔹 Total Workers by Industry
![Industry Chart](data/eda_charts/industry_worker_distribution.png)

### 🔹 Main vs Marginal Workers
![Main vs Marginal](data/eda_charts/main_vs_marginal_workers.png)

---

## 🚀 How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/industrial-hr-geo-visualisation.git
   cd industrial-hr-geo-visualisation
   ```

2. **Install dependencies**  
   Create a virtual environment (optional) and install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

4. Open the provided local URL in your browser to interact with the dashboard.

---

## 🙋‍♀️ Author

**Mansi Singh**  
Connect with me on [LinkedIn](linkedin.com/in/mansi-singh-13684b261)
