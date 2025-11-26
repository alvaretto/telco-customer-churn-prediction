"""
Página de Análisis de Riesgo - Predicción individual de churn de clientes
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
st.markdown("""
<div class="alert-info">
    <strong>ℹ️ Instrucciones:</strong> Completa el formulario con la información del cliente
    para obtener una predicción del riesgo de abandono (churn).
</div>
""", unsafe_allow_html=True)

# URL de la API
API_URL = "https://telco-churn-api-y9xy.onrender.com/predict"

# Formulario de entrada con mejor organización
st.subheader("📝 Información del Cliente")
st.markdown("Organiza los datos del cliente por categorías para una mejor experiencia")

# Cambiar a 2 columnas en lugar de 3
col1, col2 = st.columns(2)

# Columna 1: Demografía y Servicios Básicos
with col1:
    with st.expander("👤 Información Demográfica", expanded=True):
        st.markdown("*Datos personales del cliente*")
        gender = st.selectbox(
            "Género",
            ["Male", "Female"],
            format_func=lambda x: "Masculino" if x == "Male" else "Femenino",
            help="Género del cliente"
        )
        senior_citizen = st.selectbox(
            "¿Es adulto mayor? (65+)",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí",
            help="Indica si el cliente tiene 65 años o más"
        )
        partner = st.selectbox(
            "¿Tiene pareja?",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí",
            help="Indica si el cliente vive con una pareja"
        )
        dependents = st.selectbox(
            "¿Tiene dependientes?",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí",
            help="Indica si el cliente tiene personas a su cargo (hijos, familiares)"
        )

    with st.expander("📞 Servicios Telefónicos", expanded=True):
        st.markdown("*Servicios de telefonía contratados*")
        phone_service = st.selectbox(
            "Servicio Telefónico",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí",
            help="Indica si el cliente tiene servicio telefónico"
        )
        multiple_lines = st.selectbox(
            "Múltiples Líneas Telefónicas",
            ["No", "Yes", "No phone service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio telefónico"),
            help="Indica si el cliente tiene más de una línea telefónica"
        )

# Columna 2: Servicios de Internet y Cuenta
with col2:
    with st.expander("🌐 Servicios de Internet", expanded=True):
        st.markdown("*Servicios de internet y adicionales*")
        internet_service = st.selectbox(
            "Tipo de Servicio de Internet",
            ["No", "DSL", "Fiber optic"],
            format_func=lambda x: "No" if x == "No" else ("DSL" if x == "DSL" else "Fibra óptica"),
            help="Tipo de conexión a internet del cliente"
        )
        online_security = st.selectbox(
            "Seguridad Online",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Servicio de seguridad online (antivirus, firewall)"
        )
        online_backup = st.selectbox(
            "Respaldo Online",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Servicio de respaldo de datos en la nube"
        )
        device_protection = st.selectbox(
            "Protección de Dispositivo",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Seguro para dispositivos electrónicos"
        )
        tech_support = st.selectbox(
            "Soporte Técnico",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Servicio de soporte técnico 24/7"
        )
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Servicio de televisión por streaming"
        )
        streaming_movies = st.selectbox(
            "Streaming de Películas",
            ["No", "Yes", "No internet service"],
            format_func=lambda x: "No" if x == "No" else ("Sí" if x == "Yes" else "Sin servicio de internet"),
            help="Servicio de películas por streaming"
        )

    with st.expander("💳 Información de Cuenta", expanded=True):
        st.markdown("*Detalles de facturación y contrato*")
        tenure = st.slider(
            "Antigüedad (meses)",
            0, 72, 12,
            help="Número de meses que el cliente ha estado con la empresa"
        )
        contract = st.selectbox(
            "Tipo de Contrato",
            ["Month-to-month", "One year", "Two year"],
            format_func=lambda x: "Mes a mes" if x == "Month-to-month" else ("Un año" if x == "One year" else "Dos años"),
            help="Duración del contrato del cliente"
        )
        paperless_billing = st.selectbox(
            "Facturación sin Papel",
            ["No", "Yes"],
            format_func=lambda x: "No" if x == "No" else "Sí",
            help="Indica si el cliente recibe facturas electrónicas"
        )
        payment_method = st.selectbox(
            "Método de Pago",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ],
            format_func=lambda x: {
                "Electronic check": "Cheque electrónico",
                "Mailed check": "Cheque por correo",
                "Bank transfer (automatic)": "Transferencia bancaria (automática)",
                "Credit card (automatic)": "Tarjeta de crédito (automática)"
            }[x],
            help="Forma de pago utilizada por el cliente"
        )
        monthly_charges = st.number_input(
            "Cargos Mensuales ($)",
            0.0, 200.0, 70.0, 0.01,
            help="Monto que el cliente paga mensualmente"
        )
        total_charges = st.number_input(
            "Cargos Totales ($)",
            0.0, 10000.0, 840.0, 0.01,
            help="Monto total que el cliente ha pagado desde que se unió"
        )

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

