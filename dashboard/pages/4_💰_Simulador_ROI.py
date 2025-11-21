"""
Página de Simulador ROI - Calcular retorno de inversión para estrategias de retención
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Simulador ROI", page_icon="💰", layout="wide")

st.title("💰 Simulador ROI para Estrategias de Retención")
st.markdown("Calcula el retorno de inversión de tus campañas de prevención de churn")
st.markdown("---")

# Parámetros de entrada
st.subheader("📊 Parámetros de la Campaña")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Base de Clientes**")
    total_customers = st.number_input("Total de Clientes", 1000, 100000, 7000, 100)
    current_churn_rate = st.slider("Tasa de Churn Actual (%)", 0.0, 50.0, 26.5, 0.1)
    avg_customer_value = st.number_input("Valor Promedio de Vida del Cliente ($)", 100, 10000, 1500, 50)

with col2:
    st.markdown("**Campaña de Retención**")
    campaign_cost_per_customer = st.number_input("Costo de Campaña por Cliente ($)", 1, 500, 50, 5)
    expected_churn_reduction = st.slider("Reducción de Churn Esperada (%)", 0.0, 100.0, 30.0, 1.0)
    success_rate = st.slider("Tasa de Éxito de la Campaña (%)", 0.0, 100.0, 70.0, 1.0)

st.markdown("---")

# Cálculos
churned_customers = int(total_customers * (current_churn_rate / 100))
potential_saves = int(churned_customers * (expected_churn_reduction / 100) * (success_rate / 100))
campaign_cost = campaign_cost_per_customer * churned_customers
revenue_saved = potential_saves * avg_customer_value
net_benefit = revenue_saved - campaign_cost
roi = ((revenue_saved - campaign_cost) / campaign_cost * 100) if campaign_cost > 0 else 0

# Resultados
st.subheader("📈 Resultados del Análisis ROI")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Clientes en Riesgo",
        f"{churned_customers:,}",
        help="Número de clientes con probabilidad de churn"
    )

with col2:
    st.metric(
        "Clientes Salvados Potenciales",
        f"{potential_saves:,}",
        delta=f"{(potential_saves/churned_customers*100):.1f}%",
        help="Clientes retenidos a través de la campaña"
    )

with col3:
    st.metric(
        "Beneficio Neto",
        f"${net_benefit:,}",
        delta="Positivo" if net_benefit > 0 else "Negativo",
        delta_color="normal" if net_benefit > 0 else "inverse",
        help="Ingresos salvados menos costo de campaña"
    )

with col4:
    st.metric(
        "ROI",
        f"{roi:.1f}%",
        help="Retorno de Inversión"
    )

st.markdown("---")

# Desglose detallado
st.subheader("💵 Desglose Financiero")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Costos")
    st.markdown(f"""
    - **Costo de Campaña por Cliente**: ${campaign_cost_per_customer:,}
    - **Clientes Objetivo**: {churned_customers:,}
    - **Costo Total de Campaña**: ${campaign_cost:,}
    """)

    st.markdown("### Beneficios")
    st.markdown(f"""
    - **Clientes Retenidos**: {potential_saves:,}
    - **Valor Promedio por Cliente**: ${avg_customer_value:,}
    - **Ingresos Totales Salvados**: ${revenue_saved:,}
    """)

with col2:
    # Gráfico de pastel
    fig = go.Figure(data=[go.Pie(
        labels=['Costo de Campaña', 'Beneficio Neto'],
        values=[campaign_cost, max(0, net_benefit)],
        hole=.3,
        marker_colors=['#ff6b6b', '#51cf66']
    )])

    fig.update_layout(
        title='Distribución Costo vs Beneficio',
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Análisis de escenarios
st.subheader("🔍 Análisis de Escenarios")

scenarios = pd.DataFrame({
    'Escenario': ['Conservador', 'Moderado', 'Optimista'],
    'Reducción de Churn (%)': [20, 30, 40],
    'Tasa de Éxito (%)': [60, 70, 80]
})

results = []
for _, row in scenarios.iterrows():
    saves = int(churned_customers * (row['Reducción de Churn (%)'] / 100) * (row['Tasa de Éxito (%)'] / 100))
    revenue = saves * avg_customer_value
    net = revenue - campaign_cost
    roi_val = ((revenue - campaign_cost) / campaign_cost * 100) if campaign_cost > 0 else 0

    results.append({
        'Escenario': row['Escenario'],
        'Clientes Salvados': saves,
        'Ingresos Salvados': revenue,
        'Beneficio Neto': net,
        'ROI (%)': roi_val
    })

df_scenarios = pd.DataFrame(results)

st.dataframe(df_scenarios.style.format({
    'Clientes Salvados': '{:,}',
    'Ingresos Salvados': '${:,.0f}',
    'Beneficio Neto': '${:,.0f}',
    'ROI (%)': '{:.1f}%'
}), use_container_width=True)

# Gráfico de comparación de ROI
fig = px.bar(
    df_scenarios,
    x='Escenario',
    y='ROI (%)',
    title='Comparación de ROI entre Escenarios',
    color='ROI (%)',
    color_continuous_scale='Greens',
    text='ROI (%)'
)

fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(yaxis_title="ROI (%)", showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Recomendaciones
st.subheader("💡 Recomendaciones")

if roi > 100:
    st.success(f"""
    **ROI Excelente ({roi:.1f}%)**

    La campaña de retención muestra retornos financieros sólidos. Acciones recomendadas:
    - Proceder con la campaña inmediatamente
    - Considerar expandir a más segmentos de clientes
    - Monitorear resultados y optimizar continuamente
    """)
elif roi > 50:
    st.info(f"""
    **ROI Bueno ({roi:.1f}%)**

    La campaña es financieramente viable. Acciones recomendadas:
    - Proceder con la campaña
    - Enfocarse primero en clientes de alto valor
    - Probar y refinar estrategias de segmentación
    """)
elif roi > 0:
    st.warning(f"""
    **ROI Marginal ({roi:.1f}%)**

    La campaña muestra retornos positivos pero modestos. Acciones recomendadas:
    - Considerar optimizar costos de campaña
    - Mejorar segmentación para aumentar tasa de éxito
    - Probar en un segmento más pequeño primero
    """)
else:
    st.error(f"""
    **ROI Negativo ({roi:.1f}%)**

    La campaña no es financieramente viable con los parámetros actuales. Acciones recomendadas:
    - Reducir costos de campaña
    - Mejorar segmentación y tasa de éxito
    - Considerar estrategias alternativas de retención
    """)

