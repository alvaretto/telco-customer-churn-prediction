"""
Risk Analysis Page - Individual customer churn prediction
"""

import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go

st.set_page_config(page_title="Risk Analysis", page_icon="🎯", layout="wide")

st.title("🎯 Customer Churn Risk Analysis")
st.markdown("Enter customer information to predict churn risk")
st.markdown("---")

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'churn_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'preprocessor.pkl')

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    model_loaded = True
except Exception as e:
    st.error(f"Error loading model: {e}")
    model_loaded = False

# Input form
st.subheader("📝 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Demographics**")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

with col2:
    st.markdown("**Services**")
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["No", "DSL", "Fiber optic"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

with col3:
    st.markdown("**Account**")
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0, 0.01)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 840.0, 0.01)

# These will be calculated after the button is pressed

st.markdown("---")

# Predict button
if st.button("🔮 Predict Churn Risk", type="primary", use_container_width=True):
    if not model_loaded:
        st.error("Model not loaded. Cannot make prediction.")
    else:
        # Prepare data (original features only - 19 features)
        customer_data = {
            'gender': gender,
            'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone_service,
            'MultipleLines': multiple_lines,
            'InternetService': internet_service,
            'OnlineSecurity': online_security,
            'OnlineBackup': online_backup,
            'DeviceProtection': device_protection,
            'TechSupport': tech_support,
            'StreamingTV': streaming_tv,
            'StreamingMovies': streaming_movies,
            'Contract': contract,
            'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges
        }

        df = pd.DataFrame([customer_data])

        # Apply feature engineering (same as in notebook)
        df['ChargeRatio'] = df['MonthlyCharges'] / (df['TotalCharges'] + 1)
        df['AvgMonthlyCharges'] = df['TotalCharges'] / (df['tenure'] + 1)

        # TenureGroup
        df['TenureGroup'] = pd.cut(df['tenure'],
                                    bins=[0, 12, 24, 48, 72],
                                    labels=['0-1 año', '1-2 años', '2-4 años', '4+ años']).astype(str)

        # TotalServices
        service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
        df['TotalServices'] = (df[service_cols] != 'No').sum(axis=1)

        # SeniorWithDependents
        df['SeniorWithDependents'] = ((df['SeniorCitizen'] == 1) & (df['Dependents'] == 'Yes')).astype(int)

        # HighValueContract
        median_charges = 70.0  # Approximate median from training data
        df['HighValueContract'] = ((df['Contract'].isin(['One year', 'Two year'])) &
                                   (df['MonthlyCharges'] > median_charges)).astype(int)

        # Make prediction
        try:
            # Apply preprocessing
            df_processed = preprocessor.transform(df)

            # Make prediction with preprocessed data
            prediction = model.predict(df_processed)[0]
            probability = model.predict_proba(df_processed)[0]
            
            churn_prob = probability[1]
            
            # Display results
            st.markdown("---")
            st.subheader("📊 Prediction Results")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if prediction == 1:
                    st.error("### ⚠️ HIGH RISK")
                    st.markdown("**Customer likely to churn**")
                else:
                    st.success("### ✅ LOW RISK")
                    st.markdown("**Customer likely to stay**")
            
            with col2:
                st.metric("Churn Probability", f"{churn_prob*100:.1f}%")
                st.metric("Retention Probability", f"{(1-churn_prob)*100:.1f}%")
            
            with col3:
                if churn_prob < 0.3:
                    risk_level = "🟢 Low"
                elif churn_prob < 0.5:
                    risk_level = "🟡 Medium"
                elif churn_prob < 0.7:
                    risk_level = "🟠 High"
                else:
                    risk_level = "🔴 Critical"
                
                st.metric("Risk Level", risk_level)
            
            # Probability gauge
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = churn_prob * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Churn Probability (%)"},
                delta = {'reference': 50},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkred" if churn_prob > 0.5 else "darkgreen"},
                    'steps': [
                        {'range': [0, 30], 'color': "lightgreen"},
                        {'range': [30, 50], 'color': "yellow"},
                        {'range': [50, 70], 'color': "orange"},
                        {'range': [70, 100], 'color': "red"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")

