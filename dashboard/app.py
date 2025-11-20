"""
Telco Customer Churn Prediction Dashboard
Main page - Home and Overview
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# Page configuration
st.set_page_config(
    page_title="Churn Prediction Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load metadata
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

try:
    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
except Exception as e:
    st.error(f"Error loading model metadata: {e}")
    metadata = {}

# Title and description
st.title("📊 Telco Customer Churn Prediction Dashboard")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/phone-disconnected.png", width=80)
    st.title("Navigation")
    st.markdown("""
    Use the pages in the sidebar to navigate:
    
    - **📊 Overview**: Project summary
    - **🎯 Risk Analysis**: Predict churn risk
    - **📈 Model Metrics**: Model performance
    - **💰 ROI Simulator**: Calculate ROI
    - **🔍 Model Monitoring**: Track performance
    """)
    
    st.markdown("---")
    st.markdown("### Model Info")
    if metadata:
        st.metric("Model Type", metadata.get('model_type', 'N/A'))
        st.metric("ROC-AUC", f"{metadata.get('metrics', {}).get('roc_auc', 0):.2f}")
        st.metric("Features", metadata.get('n_features', 'N/A'))

# Main content
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="ROC-AUC Score",
        value=f"{metadata.get('metrics', {}).get('roc_auc', 0):.2f}",
        delta="0.87"
    )

with col2:
    st.metric(
        label="Recall",
        value=f"{metadata.get('metrics', {}).get('recall', 0):.2f}",
        delta="0.83"
    )

with col3:
    st.metric(
        label="Precision",
        value=f"{metadata.get('metrics', {}).get('precision', 0):.2f}",
        delta="0.72"
    )

with col4:
    st.metric(
        label="F1-Score",
        value=f"{metadata.get('metrics', {}).get('f1_score', 0):.2f}",
        delta="0.77"
    )

st.markdown("---")

# Project description
st.header("🎯 About This Project")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Customer Churn Prediction System
    
    This dashboard provides an interactive interface for predicting and analyzing customer churn
    in the telecommunications industry.
    
    **Key Features:**
    - 🎯 **Risk Analysis**: Predict churn probability for individual customers
    - 📈 **Model Metrics**: Detailed performance metrics and visualizations
    - 💰 **ROI Simulator**: Calculate return on investment for retention strategies
    - 🔍 **Monitoring**: Track model performance over time
    
    **Model Details:**
    - **Algorithm**: Random Forest Classifier
    - **Training Date**: {training_date}
    - **Features**: {n_features} customer attributes
    - **Training Samples**: {n_samples} customers
    """.format(
        training_date=metadata.get('training_date', 'N/A')[:10],
        n_features=metadata.get('n_features', 'N/A'),
        n_samples=metadata.get('n_samples_train', 'N/A')
    ))

with col2:
    st.info("""
    **Quick Start:**
    
    1. Navigate to **Risk Analysis** to predict churn for a customer
    2. Check **Model Metrics** to understand model performance
    3. Use **ROI Simulator** to calculate retention strategy ROI
    4. Monitor model health in **Model Monitoring**
    """)

st.markdown("---")

# Features overview
st.header("📋 Model Features")

if metadata.get('features'):
    features = metadata['features']
    
    # Create columns for features
    n_cols = 3
    cols = st.columns(n_cols)
    
    for i, feature in enumerate(features):
        with cols[i % n_cols]:
            st.markdown(f"✓ {feature}")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>Telco Customer Churn Prediction Dashboard v1.0.0</p>
    <p>Built with Streamlit | Model: Random Forest Classifier</p>
</div>
""", unsafe_allow_html=True)

