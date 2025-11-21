# 🌐 URLs DE PRODUCCIÓN - TELCO CHURN PREDICTION

## 📊 PROYECTO DEPLOYADO

### URLs Principales

#### 🔗 API REST (Render)
```
URL: https://telco-churn-api-y9xy.onrender.com
Status: ✅ DEPLOYADO Y FUNCIONANDO
Última actualización: 2025-11-20 23:59 UTC
```

**Endpoints disponibles:**
- `GET /` - Información de la API ✅
- `GET /health` - Health check ✅
- `GET /model_info` - Información del modelo y métricas ✅
- `POST /predict` - Predicción individual ✅ (acepta datos categóricos originales)
- `POST /predict_batch` - Predicciones en lote ✅

**Mejoras implementadas:**
- ✅ Feature engineering automático (6 features adicionales)
- ✅ Acepta datos categóricos originales (19 features)
- ✅ Preprocesamiento automático (scaling + encoding)
- ✅ Versiones de librerías actualizadas (scikit-learn 1.5.2)

#### 📊 Dashboard (Streamlit Cloud)
```
URL: https://[PENDIENTE-DEPLOYMENT].streamlit.app
Status: ⏳ Pendiente de deployment
```

**Páginas disponibles:**
- 🏠 Home - Overview del proyecto
- 📊 Overview - Estadísticas y análisis
- 🎯 Risk Analysis - Predicción interactiva
- 📈 Model Metrics - Métricas del modelo
- 💰 ROI Simulator - Calculadora de ROI
- 🔍 Model Monitoring - Monitoreo del modelo

#### 📦 Repositorio GitHub
```
URL: https://github.com/alvaretto/telco-customer-churn-prediction
Status: ✅ Activo
Branch: main
```

---

## 🧪 EJEMPLOS DE USO

### Probar API con curl

```bash
# Health check
curl https://telco-churn-api-y9xy.onrender.com/health

# Información del modelo
curl https://telco-churn-api-y9xy.onrender.com/model_info

# Predicción individual (SOLO FEATURES ORIGINALES - Feature engineering automático)
curl -X POST https://telco-churn-api-y9xy.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 844.2
  }'

# Respuesta esperada:
# {
#   "churn": true,
#   "prediction": 1,
#   "probability": {
#     "churn": 0.609,
#     "no_churn": 0.391
#   },
#   "risk_level": "high",
#   "timestamp": "2025-11-20T23:59:06"
# }
```

### Probar API con Python

```python
import requests

# URL de la API en producción
API_URL = "https://telco-churn-api-y9xy.onrender.com"

# Health check
response = requests.get(f"{API_URL}/health")
print(response.json())

# Predicción (SOLO features originales - 19 features)
customer_data = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 844.2
}

response = requests.post(f"{API_URL}/predict", json=customer_data)
print(response.json())
# Output: {'churn': True, 'prediction': 1, 'probability': {'churn': 0.609, 'no_churn': 0.391}, 'risk_level': 'high', ...}
```

---

## 📊 INFORMACIÓN DE DEPLOYMENT

### Configuración API (Render)
- **Plan**: Free
- **Region**: Oregon (US West)
- **Runtime**: Python 3.10.13
- **Workers**: 2
- **Threads**: 2
- **RAM**: 512 MB
- **Auto-deploy**: Habilitado (push a main)

### Configuración Dashboard (Streamlit Cloud)
- **Plan**: Free
- **Runtime**: Python 3.10
- **RAM**: 1 GB
- **Auto-deploy**: Habilitado (push a main)

### Modelo ML
- **Tipo**: RandomForestClassifier
- **Tamaño**: 65 MB
- **Features**: 25
- **ROC-AUC**: 0.87
- **Recall**: 0.83
- **Precision**: 0.72
- **F1-Score**: 0.77

---

## 🔄 ACTUALIZACIÓN DEL MODELO

Para actualizar el modelo en producción:

1. **Entrenar nuevo modelo en Colab**
2. **Serializar y descargar**
3. **Actualizar archivos locales**:
   ```bash
   # Reemplazar archivos en models/
   cp nuevo_modelo.pkl models/churn_model.pkl
   cp nuevo_preprocessor.pkl models/preprocessor.pkl
   ```
4. **Commit y push**:
   ```bash
   git add models/
   git commit -m "feat: Actualizar modelo v2 - ROC-AUC 0.XX"
   git push origin main
   ```
5. **Auto-deploy**: Render y Streamlit detectan el cambio y redeploy automáticamente

---

## 📈 MONITOREO

### Render (API)
- **Dashboard**: https://dashboard.render.com
- **Logs**: Dashboard → Services → telco-churn-api → Logs
- **Metrics**: Dashboard → Services → telco-churn-api → Metrics

### Streamlit Cloud (Dashboard)
- **Dashboard**: https://share.streamlit.io
- **Logs**: Apps → telco-churn-dashboard → Manage app → Logs
- **Analytics**: Apps → telco-churn-dashboard → Analytics

---

## 🎯 PRÓXIMOS PASOS

### ✅ Completado
- [x] URL real de la API: `https://telco-churn-api-y9xy.onrender.com`
- [x] Fecha de deployment API: 2025-11-20
- [x] Feature engineering automático implementado
- [x] Versiones de librerías actualizadas (scikit-learn 1.5.2)
- [x] Documentación actualizada

### ⏳ Pendiente
- [ ] URL real del Dashboard (Streamlit Cloud)
- [ ] Deployment del Dashboard
- [ ] Capturas de pantalla
- [ ] Métricas de uso iniciales
- [ ] Integración Dashboard → API

---

**Última actualización**: 2025-11-20 23:59 UTC
**Estado**: 🟢 API DEPLOYADA | ⏳ Dashboard pendiente
**Responsable**: Álvaro Ángel Molina (@alvaretto)

## 📊 Historial de Cambios

### 2025-11-20 23:59 UTC - Feature Engineering Automático
- ✅ Implementado feature engineering automático en API
- ✅ API ahora acepta datos categóricos originales (19 features)
- ✅ Actualizado scikit-learn a 1.5.2 para compatibilidad
- ✅ Actualizado joblib a 1.4.2
- ✅ Agregado metadata con versiones de librerías
- ✅ Documentación actualizada (API_USAGE.md, README.md)

### 2025-11-20 19:45 UTC - Deployment Inicial
- ✅ API deployada en Render
- ✅ Health checks funcionando
- ✅ Modelo cargado correctamente (65 MB)

