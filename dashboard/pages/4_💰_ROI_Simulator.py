"""
ROI Simulator Page - Calculate return on investment for retention strategies
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="ROI Simulator", page_icon="💰", layout="wide")

st.title("💰 ROI Simulator for Retention Strategies")
st.markdown("Calculate the return on investment of your churn prevention campaigns")
st.markdown("---")

# Input parameters
st.subheader("📊 Campaign Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Customer Base**")
    total_customers = st.number_input("Total Customers", 1000, 100000, 7000, 100)
    current_churn_rate = st.slider("Current Churn Rate (%)", 0.0, 50.0, 26.5, 0.1)
    avg_customer_value = st.number_input("Avg Customer Lifetime Value ($)", 100, 10000, 1500, 50)

with col2:
    st.markdown("**Retention Campaign**")
    campaign_cost_per_customer = st.number_input("Campaign Cost per Customer ($)", 1, 500, 50, 5)
    expected_churn_reduction = st.slider("Expected Churn Reduction (%)", 0.0, 100.0, 30.0, 1.0)
    success_rate = st.slider("Campaign Success Rate (%)", 0.0, 100.0, 70.0, 1.0)

st.markdown("---")

# Calculations
churned_customers = int(total_customers * (current_churn_rate / 100))
potential_saves = int(churned_customers * (expected_churn_reduction / 100) * (success_rate / 100))
campaign_cost = campaign_cost_per_customer * churned_customers
revenue_saved = potential_saves * avg_customer_value
net_benefit = revenue_saved - campaign_cost
roi = ((revenue_saved - campaign_cost) / campaign_cost * 100) if campaign_cost > 0 else 0

# Results
st.subheader("📈 ROI Analysis Results")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers at Risk",
        f"{churned_customers:,}",
        help="Number of customers likely to churn"
    )

with col2:
    st.metric(
        "Potential Saves",
        f"{potential_saves:,}",
        delta=f"{(potential_saves/churned_customers*100):.1f}%",
        help="Customers retained through campaign"
    )

with col3:
    st.metric(
        "Net Benefit",
        f"${net_benefit:,}",
        delta="Positive" if net_benefit > 0 else "Negative",
        delta_color="normal" if net_benefit > 0 else "inverse",
        help="Revenue saved minus campaign cost"
    )

with col4:
    st.metric(
        "ROI",
        f"{roi:.1f}%",
        help="Return on Investment"
    )

st.markdown("---")

# Detailed breakdown
st.subheader("💵 Financial Breakdown")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Costs")
    st.markdown(f"""
    - **Campaign Cost per Customer**: ${campaign_cost_per_customer:,}
    - **Customers Targeted**: {churned_customers:,}
    - **Total Campaign Cost**: ${campaign_cost:,}
    """)
    
    st.markdown("### Benefits")
    st.markdown(f"""
    - **Customers Retained**: {potential_saves:,}
    - **Avg Customer Value**: ${avg_customer_value:,}
    - **Total Revenue Saved**: ${revenue_saved:,}
    """)

with col2:
    # Pie chart
    fig = go.Figure(data=[go.Pie(
        labels=['Campaign Cost', 'Net Benefit'],
        values=[campaign_cost, max(0, net_benefit)],
        hole=.3,
        marker_colors=['#ff6b6b', '#51cf66']
    )])
    
    fig.update_layout(
        title='Cost vs Benefit Distribution',
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Scenario analysis
st.subheader("🔍 Scenario Analysis")

scenarios = pd.DataFrame({
    'Scenario': ['Conservative', 'Moderate', 'Optimistic'],
    'Churn Reduction (%)': [20, 30, 40],
    'Success Rate (%)': [60, 70, 80]
})

results = []
for _, row in scenarios.iterrows():
    saves = int(churned_customers * (row['Churn Reduction (%)'] / 100) * (row['Success Rate (%)'] / 100))
    revenue = saves * avg_customer_value
    net = revenue - campaign_cost
    roi_val = ((revenue - campaign_cost) / campaign_cost * 100) if campaign_cost > 0 else 0
    
    results.append({
        'Scenario': row['Scenario'],
        'Customers Saved': saves,
        'Revenue Saved': revenue,
        'Net Benefit': net,
        'ROI (%)': roi_val
    })

df_scenarios = pd.DataFrame(results)

st.dataframe(df_scenarios.style.format({
    'Customers Saved': '{:,}',
    'Revenue Saved': '${:,.0f}',
    'Net Benefit': '${:,.0f}',
    'ROI (%)': '{:.1f}%'
}), use_container_width=True)

# ROI comparison chart
fig = px.bar(
    df_scenarios,
    x='Scenario',
    y='ROI (%)',
    title='ROI Comparison Across Scenarios',
    color='ROI (%)',
    color_continuous_scale='Greens',
    text='ROI (%)'
)

fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(yaxis_title="ROI (%)", showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Recommendations
st.subheader("💡 Recommendations")

if roi > 100:
    st.success(f"""
    **Excellent ROI ({roi:.1f}%)**
    
    The retention campaign shows strong financial returns. Recommended actions:
    - Proceed with the campaign immediately
    - Consider expanding to more customer segments
    - Monitor results and optimize continuously
    """)
elif roi > 50:
    st.info(f"""
    **Good ROI ({roi:.1f}%)**
    
    The campaign is financially viable. Recommended actions:
    - Proceed with the campaign
    - Focus on high-value customers first
    - Test and refine targeting strategies
    """)
elif roi > 0:
    st.warning(f"""
    **Marginal ROI ({roi:.1f}%)**
    
    The campaign shows positive but modest returns. Recommended actions:
    - Consider optimizing campaign costs
    - Improve targeting to increase success rate
    - Test on a smaller segment first
    """)
else:
    st.error(f"""
    **Negative ROI ({roi:.1f}%)**
    
    The campaign is not financially viable at current parameters. Recommended actions:
    - Reduce campaign costs
    - Improve targeting and success rate
    - Consider alternative retention strategies
    """)

