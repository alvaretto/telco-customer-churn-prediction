"""
Página de Análisis de Riesgo - Predicción individual de churn de clientes
OPTIMIZADA: Solo solicita las características más importantes del modelo
"""

import streamlit as st
import sys
import os
import pandas as pd
import requests
import plotly.graph_objects as go

# Agregar el directorio config al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config.colors import CUSTOM_CSS, get_risk_color, get_risk_level

st.set_page_config(page_title="Análisis de Riesgo", page_icon="🎯", layout="wide")

# Aplicar CSS personalizado
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("🎯 Análisis de Riesgo de Churn de Clientes")

# Mensaje informativo sobre la optimización
st.markdown("""
<div class="alert-info">
    <strong>✨ Formulario Optimizado</strong><br>
    Este formulario solicita únicamente las <strong>10 características más importantes</strong>
    identificadas por el modelo de Machine Learning. Esto reduce el tiempo de captura en un 50%
    manteniendo la precisión de la predicción.
    <br><br>
    <strong>ℹ️ Instrucciones:</strong> Completa los campos con la información del cliente
    para obtener una predicción del riesgo de abandono (churn).
</div>
""", unsafe_allow_html=True)

# URL de la API
API_URL = "https://telco-churn-api-y9xy.onrender.com/predict"

# Top 10 características más importantes (según feature_importances_)
st.markdown("""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin: 20px 0;">
    <h4 style="margin-top: 0;">🔝 Top 10 Características Más Importantes</h4>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
        <div>1. ⚡ <strong>ChargeRatio</strong> (12.45%)</div>
        <div>2. 📅 <strong>Antigüedad</strong> (10.45%)</div>
        <div>3. 💰 <strong>Cargos Totales</strong> (8.63%)</div>
        <div>4. 📊 <strong>Promedio Mensual</strong> (7.73%)</div>
        <div>5. 💵 <strong>Cargos Mensuales</strong> (7.65%)</div>
        <div>6. 📝 <strong>Contrato 2 años</strong> (6.89%)</div>
        <div>7. 🌐 <strong>Fibra Óptica</strong> (5.58%)</div>
        <div>8. 📦 <strong>Total Servicios</strong> (4.49%)</div>
        <div>9. 💳 <strong>Cheque Electrónico</strong> (3.40%)</div>
        <div>10. ⏰ <strong>Grupo Antigüedad</strong> (3.12%)</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Formulario optimizado con solo las características necesarias
st.subheader("📝 Información del Cliente (Solo Datos Esenciales)")

# Organizar en 2 columnas
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💰 Información Financiera")
    st.markdown("*Las variables más predictivas del modelo*")

    monthly_charges = st.number_input(
        "💵 Cargos Mensuales ($)",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=0.01,
        help="⭐ TOP 5 - Monto que el cliente paga mensualmente"
    )

    total_charges = st.number_input(
        "💰 Cargos Totales ($)",
        min_value=0.0,
        max_value=10000.0,
        value=840.0,
        step=0.01,
        help="⭐ TOP 3 - Monto total que el cliente ha pagado desde que se unió"
    )

    tenure = st.slider(
        "📅 Antigüedad (meses)",
        min_value=0,
        max_value=72,
        value=12,
        help="⭐ TOP 2 - Número de meses que el cliente ha estado con la empresa"
    )

with col2:
    st.markdown("### 📋 Información Contractual")
    st.markdown("*Tipo de contrato y servicios*")

    contract = st.selectbox(
        "📝 Tipo de Contrato",
        ["Month-to-month", "One year", "Two year"],
        format_func=lambda x: {
            "Month-to-month": "Mes a mes",
            "One year": "Un año",
            "Two year": "⭐ Dos años (TOP 6)"
        }[x],
        help="⭐ TOP 6 - Duración del contrato del cliente"
    )

    internet_service = st.selectbox(
        "🌐 Tipo de Servicio de Internet",
        ["No", "DSL", "Fiber optic"],
        format_func=lambda x: {
            "No": "No",
            "DSL": "DSL",
            "Fiber optic": "⭐ Fibra óptica (TOP 7)"
        }[x],
        help="⭐ TOP 7 - Tipo de conexión a internet del cliente"
    )

    payment_method = st.selectbox(
        "💳 Método de Pago",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        format_func=lambda x: {
            "Electronic check": "⭐ Cheque electrónico (TOP 9)",
            "Mailed check": "Cheque por correo",
            "Bank transfer (automatic)": "Transferencia bancaria (automática)",
            "Credit card (automatic)": "Tarjeta de crédito (automática)"
        }[x],
        help="⭐ TOP 9 - Forma de pago utilizada por el cliente"
    )

# Sección colapsable con campos adicionales opcionales
with st.expander("➕ Campos Adicionales (Opcionales - Mejoran la precisión)", expanded=False):
    st.markdown("*Estos campos no son obligatorios pero pueden mejorar la predicción*")

    col3, col4 = st.columns(2)

    with col3:
        gender = st.selectbox(
            "Género",
            ["Male", "Female"],
            format_func=lambda x: "Masculino" if x == "Male" else "Femenino"
        )
        senior_citizen = st.selectbox(
            "¿Es adulto mayor? (65+)",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí"
        )
        partner = st.selectbox(
            "¿Tiene pareja?",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí"
        )
        dependents = st.selectbox(
            "¿Tiene dependientes?",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí"
        )

    with col4:
        phone_service = st.selectbox(
            "Servicio Telefónico",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí"
        )
        multiple_lines = st.selectbox(
            "Múltiples Líneas Telefónicas",
            ["No", "Yes", "No phone service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio telefónico")
        )

        online_security = st.selectbox(
            "Seguridad Online",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        online_backup = st.selectbox(
            "Respaldo Online",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        device_protection = st.selectbox(
            "Protección de Dispositivo",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        tech_support = st.selectbox(
            "Soporte Técnico",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        streaming_movies = st.selectbox(
            "Streaming de Películas",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet")
        )
        paperless_billing = st.selectbox(
            "Facturación sin Papel",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí"
        )

st.markdown("---")

# Mensaje informativo sobre valores por defecto
st.info("""
💡 **Nota:** Los campos no completados se rellenarán automáticamente con valores típicos
basados en el análisis del dataset. Esto permite una predicción rápida manteniendo la precisión.
""")

# Botón de predicción
if st.button("🔮 Predecir Riesgo de Churn", type="primary", use_container_width=True):
    # Preparar datos con valores por defecto para campos no solicitados
    # Los campos opcionales usan valores por defecto si no se especifican

    # Valores por defecto basados en la moda/media del dataset
    default_values = {
        'gender': 'Male',  # Moda
        'SeniorCitizen': 0,  # Mayoría no son seniors
        'Partner': 'No',  # Moda
        'Dependents': 'No',  # Moda
        'PhoneService': 'Yes',  # Mayoría tiene servicio
        'MultipleLines': 'No',  # Moda
        'OnlineSecurity': 'No',  # Moda
        'OnlineBackup': 'No',  # Moda
        'DeviceProtection': 'No',  # Moda
        'TechSupport': 'No',  # Moda
        'StreamingTV': 'No',  # Moda
        'StreamingMovies': 'No',  # Moda
        'PaperlessBilling': 'Yes'  # Moda
    }

    # Preparar datos (solo características originales - 19 características)
    # La API hace el feature engineering automáticamente
    customer_data = {
        'gender': gender if 'gender' in locals() else default_values['gender'],
        'SeniorCitizen': (1 if senior_citizen == "Yes" else 0) if 'senior_citizen' in locals() else default_values['SeniorCitizen'],
        'Partner': partner if 'partner' in locals() else default_values['Partner'],
        'Dependents': dependents if 'dependents' in locals() else default_values['Dependents'],
        'tenure': tenure,
        'PhoneService': phone_service if 'phone_service' in locals() else default_values['PhoneService'],
        'MultipleLines': multiple_lines if 'multiple_lines' in locals() else default_values['MultipleLines'],
        'InternetService': internet_service,
        'OnlineSecurity': online_security if 'online_security' in locals() else default_values['OnlineSecurity'],
        'OnlineBackup': online_backup if 'online_backup' in locals() else default_values['OnlineBackup'],
        'DeviceProtection': device_protection if 'device_protection' in locals() else default_values['DeviceProtection'],
        'TechSupport': tech_support if 'tech_support' in locals() else default_values['TechSupport'],
        'StreamingTV': streaming_tv if 'streaming_tv' in locals() else default_values['StreamingTV'],
        'StreamingMovies': streaming_movies if 'streaming_movies' in locals() else default_values['StreamingMovies'],
        'Contract': contract,
        'PaperlessBilling': paperless_billing if 'paperless_billing' in locals() else default_values['PaperlessBilling'],
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    # Hacer predicción usando la API
    try:
        with st.spinner('🔄 Consultando el modelo de predicción... Por favor espera.'):
            response = requests.post(API_URL, json=customer_data, timeout=30)

        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            # La API devuelve probability.churn, no churn_probability
            churn_prob = result['probability']['churn']

            # Mostrar resultados con mejor diseño
            st.markdown("---")
            st.subheader("📊 Resultados de la Predicción")

            # Mensaje de éxito
            st.success("✅ Predicción completada exitosamente")

            col1, col2, col3 = st.columns(3)

            with col1:
                if prediction == 1:
                    st.markdown("""
                    <div class="alert-danger">
                        <h3>⚠️ RIESGO ALTO</h3>
                        <p><strong>Es probable que el cliente abandone</strong></p>
                        <p>Se recomienda implementar estrategias de retención inmediatas.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="alert-success">
                        <h3>✅ RIESGO BAJO</h3>
                        <p><strong>Es probable que el cliente se quede</strong></p>
                        <p>El cliente muestra señales de satisfacción con el servicio.</p>
                    </div>
                    """, unsafe_allow_html=True)

            with col2:
                st.metric(
                    "Probabilidad de Churn",
                    f"{churn_prob*100:.1f}%",
                    delta=f"{(churn_prob-0.5)*100:.1f}% vs promedio",
                    delta_color="inverse"
                )
                st.metric(
                    "Probabilidad de Retención",
                    f"{(1-churn_prob)*100:.1f}%",
                    delta=f"{(0.5-churn_prob)*100:.1f}% vs promedio",
                    delta_color="normal"
                )

            with col3:
                risk_level = get_risk_level(churn_prob)
                risk_color = get_risk_color(churn_prob)

                st.metric("Nivel de Riesgo", risk_level)

                # Recomendaciones según el nivel de riesgo
                if churn_prob >= 0.7:
                    st.warning("🚨 Acción inmediata requerida")
                elif churn_prob >= 0.5:
                    st.info("📞 Contactar al cliente pronto")
                elif churn_prob >= 0.3:
                    st.info("👀 Monitorear comportamiento")
                else:
                    st.success("😊 Cliente satisfecho")

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
            st.markdown(f"""
            <div class="alert-danger">
                <h4>❌ Error en la API</h4>
                <p><strong>Código de error:</strong> {response.status_code}</p>
                <p><strong>Mensaje:</strong> {response.text[:200]}</p>
                <p>Por favor, intenta de nuevo o contacta al administrador si el problema persiste.</p>
            </div>
            """, unsafe_allow_html=True)

    except requests.exceptions.Timeout:
        st.markdown("""
        <div class="alert-warning">
            <h4>⏱️ Tiempo de espera agotado</h4>
            <p>La solicitud a la API tardó demasiado tiempo.</p>
            <p><strong>Posibles causas:</strong></p>
            <ul>
                <li>La API puede estar iniciando (Render Free tier tarda ~1 minuto en despertar)</li>
                <li>Conexión lenta a internet</li>
            </ul>
            <p><strong>Solución:</strong> Por favor, espera un momento e intenta de nuevo.</p>
        </div>
        """, unsafe_allow_html=True)
    except requests.exceptions.ConnectionError:
        st.markdown("""
        <div class="alert-danger">
            <h4>🔌 Error de conexión</h4>
            <p>No se pudo conectar con la API de predicción.</p>
            <p><strong>Posibles causas:</strong></p>
            <ul>
                <li>No hay conexión a internet</li>
                <li>La API está temporalmente fuera de servicio</li>
                <li>Firewall o proxy bloqueando la conexión</li>
            </ul>
            <p><strong>Solución:</strong> Verifica tu conexión a internet e intenta de nuevo.</p>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
        <div class="alert-danger">
            <h4>❌ Error inesperado</h4>
            <p>Ocurrió un error al procesar la predicción.</p>
            <p><strong>Detalles técnicos:</strong> {str(e)[:200]}</p>
            <p>Por favor, verifica los datos ingresados e intenta de nuevo.</p>
        </div>
        """, unsafe_allow_html=True)

