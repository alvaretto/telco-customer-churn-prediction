"""
Página de Análisis de Riesgo - Predicción individual de churn de clientes
"""

import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="Análisis de Riesgo", page_icon="🎯", layout="wide")

st.title("🎯 Análisis de Riesgo de Churn de Clientes")
st.markdown("Ingresa la información del cliente para predecir el riesgo de churn")
st.markdown("---")

# URL de la API
API_URL = "https://telco-churn-api-y9xy.onrender.com/predict"

# Formulario de entrada
st.subheader("📝 Información del Cliente")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Demografía**")
    gender = st.selectbox("Género", ["Male", "Female"], format_func=lambda x: "Masculino" if x == "Male" else "Femenino")
    senior_citizen = st.selectbox("Adulto Mayor", ["No", "Yes"], format_func=lambda x: "No" if x == "No" else "Sí")
    partner = st.selectbox("Pareja", ["No", "Yes"], format_func=lambda x: "No" if x == "No" else "Sí")
    dependents = st.selectbox("Dependientes", ["No", "Yes"], format_func=lambda x: "No" if x == "No" else "Sí")

with col2:
    st.markdown("**Servicios**")
    phone_service = st.selectbox("Servicio Telefónico", ["No", "Yes"], format_func=lambda x: "No" if x == "No" else "Sí")
    multiple_lines = st.selectbox("Múltiples Líneas", ["No", "Yes", "No phone service"],
                                   format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio telefónico"))
    internet_service = st.selectbox("Servicio de Internet", ["No", "DSL", "Fiber optic"],
                                     format_func=lambda x: "No" if x == "No" else ("DSL" if x == "DSL" else "Fibra óptica"))
    online_security = st.selectbox("Seguridad Online", ["No", "Yes", "No internet service"],
                                    format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))
    online_backup = st.selectbox("Respaldo Online", ["No", "Yes", "No internet service"],
                                  format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))
    device_protection = st.selectbox("Protección de Dispositivo", ["No", "Yes", "No internet service"],
                                      format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))
    tech_support = st.selectbox("Soporte Técnico", ["No", "Yes", "No internet service"],
                                 format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"],
                                 format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))
    streaming_movies = st.selectbox("Streaming Películas", ["No", "Yes", "No internet service"],
                                     format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"))

with col3:
    st.markdown("**Cuenta**")
    tenure = st.slider("Antigüedad (meses)", 0, 72, 12)
    contract = st.selectbox("Contrato", ["Month-to-month", "One year", "Two year"],
                            format_func=lambda x: "Mes a mes" if x == "Month-to-month" else ("Un año" if x == "One year" else "Dos años"))
    paperless_billing = st.selectbox("Facturación sin Papel", ["No", "Yes"], format_func=lambda x: "No" if x == "No" else "Sí")
    payment_method = st.selectbox("Método de Pago", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ], format_func=lambda x: {
        "Electronic check": "Cheque electrónico",
        "Mailed check": "Cheque por correo",
        "Bank transfer (automatic)": "Transferencia bancaria (automática)",
        "Credit card (automatic)": "Tarjeta de crédito (automática)"
    }[x])
    monthly_charges = st.number_input("Cargos Mensuales ($)", 0.0, 200.0, 70.0, 0.01)
    total_charges = st.number_input("Cargos Totales ($)", 0.0, 10000.0, 840.0, 0.01)

# Estos se calcularán después de presionar el botón

st.markdown("---")

# Botón de predicción
if st.button("🔮 Predecir Riesgo de Churn", type="primary", use_container_width=True):
    # Preparar datos (solo características originales - 19 características)
    # La API hace el feature engineering automáticamente
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

    # Hacer predicción usando la API
    try:
        with st.spinner('Consultando el modelo...'):
            response = requests.post(API_URL, json=customer_data, timeout=30)

        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            churn_prob = result['churn_probability']

            # Mostrar resultados
            st.markdown("---")
            st.subheader("📊 Resultados de la Predicción")

            col1, col2, col3 = st.columns(3)

            with col1:
                if prediction == 1:
                    st.error("### ⚠️ RIESGO ALTO")
                    st.markdown("**Es probable que el cliente abandone**")
                else:
                    st.success("### ✅ RIESGO BAJO")
                    st.markdown("**Es probable que el cliente se quede**")

            with col2:
                st.metric("Probabilidad de Churn", f"{churn_prob*100:.1f}%")
                st.metric("Probabilidad de Retención", f"{(1-churn_prob)*100:.1f}%")

            with col3:
                if churn_prob < 0.3:
                    risk_level = "🟢 Bajo"
                elif churn_prob < 0.5:
                    risk_level = "🟡 Medio"
                elif churn_prob < 0.7:
                    risk_level = "🟠 Alto"
                else:
                    risk_level = "🔴 Crítico"

                st.metric("Nivel de Riesgo", risk_level)

            # Medidor de probabilidad
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = churn_prob * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Probabilidad de Churn (%)"},
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

        else:
            st.error(f"Error en la API: {response.status_code}")
            st.error(f"Mensaje: {response.text}")

    except requests.exceptions.Timeout:
        st.error("⏱️ La solicitud a la API tardó demasiado. Por favor, intenta de nuevo.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 No se pudo conectar con la API. Verifica tu conexión a internet.")
    except Exception as e:
        st.error(f"❌ Error al hacer la predicción: {e}")

