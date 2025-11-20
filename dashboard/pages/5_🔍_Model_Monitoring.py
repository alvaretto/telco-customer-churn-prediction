"""
Model Monitoring Page - Track model performance over time
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Model Monitoring", page_icon="🔍", layout="wide")

st.title("🔍 Model Performance Monitoring")
st.markdown("Track model performance and detect potential issues")
st.markdown("---")

# Generate sample monitoring data
np.random.seed(42)
dates = pd.date_range(end=datetime.now(), periods=30, freq='D')

monitoring_data = pd.DataFrame({
    'Date': dates,
    'Accuracy': np.random.normal(0.82, 0.02, 30),
    'Precision': np.random.normal(0.72, 0.03, 30),
    'Recall': np.random.normal(0.83, 0.02, 30),
    'F1_Score': np.random.normal(0.77, 0.02, 30),
    'Predictions': np.random.randint(100, 300, 30)
})

# Current metrics
current_metrics = monitoring_data.iloc[-1]

# Status indicators
st.subheader("🎯 Current Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        f"{current_metrics['Accuracy']:.3f}",
        delta=f"{(current_metrics['Accuracy'] - monitoring_data['Accuracy'].mean()):.3f}"
    )

with col2:
    st.metric(
        "Precision",
        f"{current_metrics['Precision']:.3f}",
        delta=f"{(current_metrics['Precision'] - monitoring_data['Precision'].mean()):.3f}"
    )

with col3:
    st.metric(
        "Recall",
        f"{current_metrics['Recall']:.3f}",
        delta=f"{(current_metrics['Recall'] - monitoring_data['Recall'].mean()):.3f}"
    )

with col4:
    st.metric(
        "F1-Score",
        f"{current_metrics['F1_Score']:.3f}",
        delta=f"{(current_metrics['F1_Score'] - monitoring_data['F1_Score'].mean()):.3f}"
    )

st.markdown("---")

# Performance over time
st.subheader("📈 Performance Trends")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Accuracy'],
    mode='lines+markers',
    name='Accuracy',
    line=dict(color='blue')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Precision'],
    mode='lines+markers',
    name='Precision',
    line=dict(color='green')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Recall'],
    mode='lines+markers',
    name='Recall',
    line=dict(color='orange')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['F1_Score'],
    mode='lines+markers',
    name='F1-Score',
    line=dict(color='red')
))

fig.update_layout(
    title='Model Metrics Over Time (Last 30 Days)',
    xaxis_title='Date',
    yaxis_title='Score',
    hovermode='x unified',
    yaxis=dict(range=[0.6, 0.9])
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Prediction volume
st.subheader("📊 Prediction Volume")

fig = px.bar(
    monitoring_data,
    x='Date',
    y='Predictions',
    title='Daily Predictions',
    color='Predictions',
    color_continuous_scale='Blues'
)

fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Number of Predictions',
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Alerts and warnings
st.subheader("⚠️ Alerts & Warnings")

# Check for performance degradation
accuracy_drop = current_metrics['Accuracy'] < monitoring_data['Accuracy'].mean() - 0.05
recall_drop = current_metrics['Recall'] < monitoring_data['Recall'].mean() - 0.05

if accuracy_drop or recall_drop:
    st.warning("""
    **Performance Degradation Detected**
    
    Model performance has dropped below acceptable thresholds. Recommended actions:
    - Review recent predictions for patterns
    - Check for data drift
    - Consider model retraining
    """)
else:
    st.success("""
    **Model Performance: Healthy**
    
    All metrics are within acceptable ranges. No immediate action required.
    """)

st.markdown("---")

# Data drift detection (simulated)
st.subheader("🔄 Data Drift Detection")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Feature Distribution Comparison")
    
    # Simulated feature drift
    feature_drift = pd.DataFrame({
        'Feature': ['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'InternetService'],
        'Drift_Score': [0.02, 0.15, 0.08, 0.25, 0.18],
        'Status': ['✅ Stable', '⚠️ Warning', '✅ Stable', '🔴 Alert', '⚠️ Warning']
    })
    
    st.dataframe(feature_drift, use_container_width=True)

with col2:
    fig = px.bar(
        feature_drift,
        x='Feature',
        y='Drift_Score',
        title='Feature Drift Scores',
        color='Drift_Score',
        color_continuous_scale='Reds'
    )
    
    fig.add_hline(y=0.1, line_dash="dash", line_color="orange", 
                  annotation_text="Warning Threshold")
    fig.add_hline(y=0.2, line_dash="dash", line_color="red", 
                  annotation_text="Alert Threshold")
    
    fig.update_layout(yaxis_title="Drift Score", showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Recommendations
st.subheader("💡 Monitoring Recommendations")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Daily Checks**
    - Monitor prediction volume
    - Check for anomalies
    - Review error logs
    """)

with col2:
    st.info("""
    **Weekly Reviews**
    - Analyze performance trends
    - Check data drift scores
    - Review false positives/negatives
    """)

with col3:
    st.info("""
    **Monthly Actions**
    - Full model evaluation
    - Retrain if needed
    - Update documentation
    """)

