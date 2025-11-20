"""
Overview Page - General statistics and visualizations
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")

st.title("📊 Project Overview")
st.markdown("---")

# Sample data for visualization (in production, load from database)
np.random.seed(42)
sample_data = pd.DataFrame({
    'Month': pd.date_range('2024-01-01', periods=12, freq='M'),
    'Total_Customers': np.random.randint(5000, 7000, 12),
    'Churned': np.random.randint(300, 600, 12),
    'Retained': np.random.randint(4500, 6500, 12)
})

sample_data['Churn_Rate'] = (sample_data['Churned'] / sample_data['Total_Customers'] * 100).round(2)

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        f"{sample_data['Total_Customers'].iloc[-1]:,}",
        delta=f"{sample_data['Total_Customers'].iloc[-1] - sample_data['Total_Customers'].iloc[-2]:,}"
    )

with col2:
    st.metric(
        "Churned (Last Month)",
        f"{sample_data['Churned'].iloc[-1]:,}",
        delta=f"{sample_data['Churned'].iloc[-1] - sample_data['Churned'].iloc[-2]:,}",
        delta_color="inverse"
    )

with col3:
    st.metric(
        "Churn Rate",
        f"{sample_data['Churn_Rate'].iloc[-1]:.1f}%",
        delta=f"{sample_data['Churn_Rate'].iloc[-1] - sample_data['Churn_Rate'].iloc[-2]:.1f}%",
        delta_color="inverse"
    )

with col4:
    avg_churn = sample_data['Churn_Rate'].mean()
    st.metric(
        "Avg Churn Rate (12M)",
        f"{avg_churn:.1f}%"
    )

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Churn Trend Over Time")
    fig = px.line(
        sample_data,
        x='Month',
        y='Churn_Rate',
        title='Monthly Churn Rate (%)',
        markers=True
    )
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Churn Rate (%)",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("👥 Customer Distribution")
    fig = go.Figure(data=[
        go.Bar(name='Retained', x=sample_data['Month'], y=sample_data['Retained']),
        go.Bar(name='Churned', x=sample_data['Month'], y=sample_data['Churned'])
    ])
    fig.update_layout(
        barmode='stack',
        title='Customers: Retained vs Churned',
        xaxis_title="Month",
        yaxis_title="Number of Customers",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Churn by segment (sample data)
st.subheader("📊 Churn Analysis by Segment")

col1, col2 = st.columns(2)

with col1:
    # Churn by contract type
    contract_data = pd.DataFrame({
        'Contract': ['Month-to-month', 'One year', 'Two year'],
        'Churn_Rate': [42.7, 11.3, 2.8],
        'Customers': [3875, 1473, 1695]
    })
    
    fig = px.bar(
        contract_data,
        x='Contract',
        y='Churn_Rate',
        title='Churn Rate by Contract Type',
        color='Churn_Rate',
        color_continuous_scale='Reds'
    )
    fig.update_layout(yaxis_title="Churn Rate (%)")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Churn by internet service
    internet_data = pd.DataFrame({
        'Service': ['Fiber optic', 'DSL', 'No'],
        'Churn_Rate': [41.9, 18.9, 7.4],
        'Customers': [3096, 2421, 1526]
    })
    
    fig = px.bar(
        internet_data,
        x='Service',
        y='Churn_Rate',
        title='Churn Rate by Internet Service',
        color='Churn_Rate',
        color_continuous_scale='Reds'
    )
    fig.update_layout(yaxis_title="Churn Rate (%)")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Insights
st.subheader("💡 Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Contract Type Impact**
    
    Month-to-month contracts show 15x higher churn rate compared to two-year contracts.
    
    **Recommendation**: Incentivize longer contracts
    """)

with col2:
    st.warning("""
    **Fiber Optic Concern**
    
    Fiber optic customers have the highest churn rate (41.9%).
    
    **Recommendation**: Investigate service quality issues
    """)

with col3:
    st.success("""
    **Retention Opportunity**
    
    Targeting high-risk customers could reduce churn by 30-40%.
    
    **Recommendation**: Implement proactive retention campaigns
    """)

