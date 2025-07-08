import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(page_title="Lead Conversion Predictor", layout="centered")
st.title("Tara Metal Industries - Lead Conversion Predictor")

@st.cache_resource
def load_model():
    return joblib.load('best_lead_conversion_model.pkl')

model = load_model()

st.markdown("""
### 🖥️ Predictive Lead Conversion App
Upload a CSV of leads (with columns like lead_id, company_type, region, etc.) to predict conversion probability for each lead.\n\n- Each lead will be assigned a status: 🔵 Cold, 🟡 Warm, 🔴 Hot\n- View results and download the enhanced CSV\n- See interactive visualizations of lead status probabilities
""")

uploaded_file = st.file_uploader("Upload Leads CSV", type=["csv"])

def feature_engineering(df):
    df = df.copy()
    # Fill missing values for required columns
    for col in ["company_type", "region", "product_interest", "inquiry_channel", "company_size", "quotation_shared", "catalog_requested"]:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
    # Numeric columns
    for col in ["order_quantity_est", "response_time_hrs", "followups"]:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = 0
    # Feature engineering
    df["log_order_quantity_est"] = np.log1p(df["order_quantity_est"])
    df["log_response_time_hrs"] = np.log1p(df["response_time_hrs"])
    df["followups_squared"] = df["followups"] ** 2
    df["product_channel"] = df["product_interest"] + '_' + df["inquiry_channel"]
    return df

def assign_status(prob):
    if prob >= 0.75:
        return "🔴 Hot"
    elif prob >= 0.5:
        return "🟡 Warm"
    else:
        return "🔵 Cold"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df_fe = feature_engineering(df)
    # Predict probabilities
    proba = model.predict_proba(df_fe)[:, 1]
    df["conversion_probability"] = proba
    df["lead_status"] = df["conversion_probability"].apply(assign_status)

    st.success(f"Predictions complete! Showing top 10 leads:")
    st.dataframe(df.head(10))

    # Download enhanced CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Enhanced CSV", csv, "tara_leads_with_predictions.csv", "text/csv")

    # Pie chart: Lead Status Distribution
    st.markdown("#### Lead Status Distribution")
    status_counts = df["lead_status"].value_counts().reset_index()
    status_counts.columns = ["Lead Status", "Count"]
    fig = px.pie(status_counts, names="Lead Status", values="Count", color="Lead Status", color_discrete_map={"🔴 Hot": "red", "🟡 Warm": "gold", "🔵 Cold": "blue"})
    st.plotly_chart(fig, use_container_width=True)

    # Bar chart: Top 5 converting regions
    st.markdown("#### Top 5 Converting Regions")
    region_conv = df.groupby("region")["conversion_probability"].mean().sort_values(ascending=False).head(5).reset_index()
    fig_region = px.bar(region_conv, x="region", y="conversion_probability", color="conversion_probability", color_continuous_scale="Blues", labels={"conversion_probability": "Avg. Conversion Probability"})
    st.plotly_chart(fig_region, use_container_width=True)

    # Bar chart: Top 5 converting product interests
    st.markdown("#### Top 5 Converting Product Interests")
    prod_conv = df.groupby("product_interest")["conversion_probability"].mean().sort_values(ascending=False).head(5).reset_index()
    fig_prod = px.bar(prod_conv, x="product_interest", y="conversion_probability", color="conversion_probability", color_continuous_scale="Oranges", labels={"conversion_probability": "Avg. Conversion Probability"})
    st.plotly_chart(fig_prod, use_container_width=True)

    # Probability Distribution
    st.markdown("#### Probability Distribution")
    fig2 = px.histogram(df, x="conversion_probability", nbins=20, color="lead_status", color_discrete_map={"🔴 Hot": "red", "🟡 Warm": "gold", "🔵 Cold": "blue"}, title="Predicted Conversion Probability Distribution")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("#### Top Hot Leads")
    st.dataframe(df[df["lead_status"]=="🔴 Hot"].sort_values("conversion_probability", ascending=False).head(10))

# --- Single Lead Manual Entry Form ---
st.markdown("---")
st.markdown("### Predict a Single Lead Manually")
with st.form("single_lead_form"):
    col1, col2 = st.columns(2)
    with col1:
        company_type = st.selectbox("Company Type", ["Hotel Chain", "Retailer", "Online Seller", "Distributor"])
        region = st.selectbox("Region", ["West", "South", "North", "East", "Central"])
        product_interest = st.selectbox("Product Interest", ["Both", "Water Storage", "Kitchenware"])
        inquiry_channel = st.selectbox("Inquiry Channel", ["Website", "WhatsApp", "Reference", "Exhibition", "Dealer"])
        company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
    with col2:
        order_quantity_est = st.slider("Order Quantity Estimate", min_value=0, max_value=1000, value=300)
        response_time_hrs = st.slider("Response Time (hrs)", min_value=0, max_value=100, value=24)
        quotation_shared = st.selectbox("Quotation Shared", ["Yes", "No"])
        catalog_requested = st.selectbox("Catalog Requested", ["Yes", "No"])
        followups = st.slider("Number of Followups", min_value=0, max_value=10, value=2)
    submit_btn = st.form_submit_button("Predict Single Lead")

if 'submit_btn' in locals() and submit_btn:
    single_dict = {
        'company_type': company_type,
        'region': region,
        'product_interest': product_interest,
        'inquiry_channel': inquiry_channel,
        'company_size': company_size,
        'order_quantity_est': order_quantity_est,
        'response_time_hrs': response_time_hrs,
        'quotation_shared': quotation_shared,
        'catalog_requested': catalog_requested,
        'followups': followups,
    }
    # Feature engineering for single lead
    single_dict['log_order_quantity_est'] = np.log1p(order_quantity_est)
    single_dict['log_response_time_hrs'] = np.log1p(response_time_hrs)
    single_dict['followups_squared'] = followups ** 2
    single_dict['product_channel'] = product_interest + '_' + inquiry_channel
    single_df = pd.DataFrame([single_dict])
    single_proba = model.predict_proba(single_df)[:, 1][0]
    single_status = assign_status(single_proba)
    st.info(f"Predicted probability of conversion: {single_proba:.2%}  |  Status: {single_status}")
    if single_status == "🔴 Hot":
        st.balloons()
