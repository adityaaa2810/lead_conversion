# 🔮 Tara Metal Industries - Lead Conversion Predictor

An intelligent, interactive Streamlit-based tool for predicting the probability of lead conversion in sales, built for **Tara Metal Industries**. This solution uses machine learning to classify leads into 🔴 Hot, 🟡 Warm, and 🔵 Cold categories, helping prioritize follow-ups and improve conversion strategies.

---

## 📂 Project Structure

├── app.py # Main Streamlit app

├── oldapp.py # Previous version of the Streamlit app

├── model_training.ipynb # Jupyter notebook for model development

├── best_lead_conversion_model.pkl# Trained ML model (serialized)

├── custom_components.py # Custom feature encoder (TargetEncoder)

├── tara_metal_leads_5000.csv # Sample lead data (raw)

├── tara_metal_leads_realistic_5000.csv # More realistic lead dataset

├── requirements.txt # Python package dependencies

├── user_manual.md # Comprehensive usage manual

└── README.md # Project documentation

---

## 🚀 Features

- 📁 Upload lead data in bulk via CSV
- 👤 Predict single lead manually through an interactive form
- 🧠 AI-based conversion probability scoring
- 🎯 Lead categorization into Hot / Warm / Cold
- 📊 Dynamic visualizations:
  - Lead status pie chart
  - Top converting regions and product interests
  - Conversion probability distribution
- 💾 Download enhanced results with predictions

---

## 🛠️ Installation

1. **Clone the repository:**

git clone https://github.com/jiyapatel2107/lead-conversion-app.git
cd lead-conversion-app

2.  **Install Dependencies**

pip install -r requirements.txt

3.  **Run the Streamlit app:**
streamlit run app.py

---

## 📊 How to Use

- **✅ Batch Prediction**
  
Prepare a CSV file with leads (columns like lead_id, company_type, region, etc.)

Upload the file in the app interface

View predictions, download enhanced CSV, and explore visual analytics

- **🧍 Manual Lead Prediction**
  
Scroll to the Single Lead Prediction section

Fill out the form with required details

Submit to view conversion probability and lead status instantly

- **🧠 Model Overview**
  
Built using ensemble techniques (Logistic Regression, Random Forest, XGBoost)

Includes advanced feature engineering:

Log transformations

Interaction features

Custom target encoding (TargetEncoder)

- **Lead status mapping:**

🔴 Hot – Probability ≥ 0.75

🟡 Warm – 0.5 ≤ Probability < 0.75

🔵 Cold – Probability < 0.5

- **🧪 Sample Data Format**

Ensure your CSV includes columns such as:

lead_id,company_type,region,product_interest,inquiry_channel,company_size,
order_quantity_est,response_time_hrs,quotation_shared,catalog_requested,followups

**❗ Troubleshooting**

App won’t start: Ensure Python 3.8+ and all packages in requirements.txt are installed

Model not found: Ensure best_lead_conversion_model.pkl is in the same directory as app.py

Errors uploading CSV: Validate column names and data types

**📘 Additional Docs**

Check the User Manual for detailed guidance on installation, usage, and troubleshooting.

**👥 Author**

Jiya Patel

📧 [jiya2172005@gmail.com ]
---
