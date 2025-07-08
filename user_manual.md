# Tara Metal Industries Lead Conversion Prediction Solution - User Manual

## Table of Contents
1. Introduction
2. Project Overview
3. Key Features
4. Installation & Setup
5. Using the Streamlit App
6. Understanding the Model & Results
7. Key Considerations
8. Troubleshooting
9. Contact & Support

---

## 1. Introduction
This user manual provides step-by-step guidance for using the Tara Metal Industries Lead Conversion Prediction solution. The solution includes a machine learning model and an interactive Streamlit app to help you score sales leads and gain actionable business insights.

## 2. Project Overview
- **Objective:** Predict the probability of sales lead conversion using behavioral, demographic, and interaction data.
- **Components:**
  - Jupyter notebook for model training and evaluation (`model_training.ipynb`)
  - Streamlit app for lead scoring and analytics (`app.py`)
  - Requirements file for environment setup (`requirements.txt`)

## 3. Key Features
- Batch prediction from uploaded CSV files
- Single-lead manual prediction form
- Lead status assignment (Hot/Warm/Cold)
- Interactive visualizations (pie, bar, histogram)
- Downloadable enhanced CSV with predictions

## 4. Installation & Setup
1. **Install Python 3.8+** (if not already installed)
2. **Install dependencies:**
   - Open a terminal in the project directory
   - Run: `pip install -r requirements.txt`
3. **Run the Streamlit app:**
   - In the terminal, run: `streamlit run app.py`
   - The app will open in your browser

## 5. Using the Streamlit App
- **Batch Prediction:**
  - Upload a CSV file with lead data (see template for required columns)
  - View predictions, lead status, and download results
  - Explore visualizations for business insights
- **Single Lead Prediction:**
  - Fill out the manual entry form for a new lead
  - Instantly view conversion probability and status

## 6. Understanding the Model & Results
- **Model:** Trained using Logistic Regression, Random Forest, and XGBoost (best selected via evaluation)
- **Features:** Includes engineered features (log transforms, interaction terms)
- **Lead Status:**
  - 🔴 Hot: Probability ≥ 0.75
  - 🟡 Warm: 0.5 ≤ Probability < 0.75
  - 🔵 Cold: Probability < 0.5
- **Visualizations:**
  - Pie chart: Lead status distribution
  - Bar charts: Top regions and product interests
  - Histogram: Probability distribution

## 7. Key Considerations
- **Data Quality:** Ensure input data matches required columns and formats
- **Model Limitations:** Predictions are probabilistic, not guarantees
- **Interpretability:** Feature importance and business logic are considered
- **Security:** Do not upload sensitive data to public servers
- **Updates:** Retrain the model periodically with new data for best results

## 8. Troubleshooting
- **App not starting:** Ensure Python and Streamlit are installed, and PATH is set
- **File upload errors:** Check CSV format and required columns
- **Model errors:** Ensure `best_lead_conversion_model.pkl` is present in the app directory

## 9. Contact & Support
For questions or support, contact the project maintainer or your data science team.

---

*This manual was generated on July 3, 2025.*
