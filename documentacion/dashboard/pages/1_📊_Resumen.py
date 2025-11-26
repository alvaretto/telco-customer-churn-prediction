"""
Página de Resumen - Estadísticas generales y visualizaciones
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Resumen", page_icon="📊", layout="wide")

st.title("📊 Resumen del Proyecto")
st.markdown("---")

# Datos de muestra para visualización (en producción, cargar desde base de datos)
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
        "Total de Clientes",
        f"{sample_data['Total_Customers'].iloc[-1]:,}",
        delta=f"{sample_data['Total_Customers'].iloc[-1] - sample_data['Total_Customers'].iloc[-2]:,}"
    )

with col2:
    st.metric(
        "Churn (Último Mes)",
        f"{sample_data['Churned'].iloc[-1]:,}",
        delta=f"{sample_data['Churned'].iloc[-1] - sample_data['Churned'].iloc[-2]:,}",
        delta_color="inverse"
    )

with col3:
    st.metric(
        "Tasa de Churn",
        f"{sample_data['Churn_Rate'].iloc[-1]:.1f}%",
        delta=f"{sample_data['Churn_Rate'].iloc[-1] - sample_data['Churn_Rate'].iloc[-2]:.1f}%",
        delta_color="inverse"
    )

with col4:
    avg_churn = sample_data['Churn_Rate'].mean()
    st.metric(
        "Tasa Promedio de Churn (12M)",
        f"{avg_churn:.1f}%"
    )

st.markdown("---")

# Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Tendencia de Churn a lo Largo del Tiempo")
    fig = px.line(
        sample_data,
        x='Month',
        y='Churn_Rate',
        title='Tasa de Churn Mensual (%)',
        markers=True
    )
    fig.update_layout(
        xaxis_title="Mes",
        yaxis_title="Tasa de Churn (%)",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("👥 Distribución de Clientes")
    fig = go.Figure(data=[
        go.Bar(name='Retenidos', x=sample_data['Month'], y=sample_data['Retained']),
        go.Bar(name='Churn', x=sample_data['Month'], y=sample_data['Churned'])
    ])
    fig.update_layout(
        barmode='stack',
        title='Clientes: Retenidos vs Churn',
        xaxis_title="Mes",
        yaxis_title="Número de Clientes",
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Churn por segmento (datos de muestra)
st.subheader("📊 Análisis de Churn por Segmento")

col1, col2 = st.columns(2)

with col1:
    # Churn por tipo de contrato
    contract_data = pd.DataFrame({
        'Contract': ['Mes a mes', 'Un año', 'Dos años'],
        'Churn_Rate': [42.7, 11.3, 2.8],
        'Customers': [3875, 1473, 1695]
    })

    fig = px.bar(
        contract_data,
        x='Contract',
        y='Churn_Rate',
        title='Tasa de Churn por Tipo de Contrato',
        color='Churn_Rate',
        color_continuous_scale='Reds'
    )
    fig.update_layout(yaxis_title="Tasa de Churn (%)")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Churn por servicio de internet
    internet_data = pd.DataFrame({
        'Service': ['Fibra óptica', 'DSL', 'No'],
        'Churn_Rate': [41.9, 18.9, 7.4],
        'Customers': [3096, 2421, 1526]
    })

    fig = px.bar(
        internet_data,
        x='Service',
        y='Churn_Rate',
        title='Tasa de Churn por Servicio de Internet',
        color='Churn_Rate',
        color_continuous_scale='Reds'
    )
    fig.update_layout(yaxis_title="Tasa de Churn (%)")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Insights
st.subheader("💡 Insights Clave")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Impacto del Tipo de Contrato**

    Los contratos mes a mes muestran una tasa de churn 15 veces mayor comparado con contratos de dos años.

    **Recomendación**: Incentivar contratos más largos
    """)

with col2:
    st.warning("""
    **Preocupación con Fibra Óptica**

    Los clientes de fibra óptica tienen la tasa de churn más alta (41.9%).

    **Recomendación**: Investigar problemas de calidad del servicio
    """)

with col3:
    st.success("""
    **Oportunidad de Retención**

    Enfocarse en clientes de alto riesgo podría reducir el churn en 30-40%.

    **Recomendación**: Implementar campañas proactivas de retención
    """)

