# 🌐 URLs DE PRODUCCIÓN - TELCO CHURN PREDICTION

## 📊 PROYECTO DEPLOYADO

### URLs Principales

#### 🔗 API REST (Render)
```
URL: https://[PENDIENTE-DEPLOYMENT].onrender.com
Status: ⏳ Pendiente de deployment
```

**Endpoints disponibles:**
- `GET /` - Información de la API
- `GET /health` - Health check
- `GET /model_info` - Información del modelo y métricas
- `POST /predict` - Predicción individual
- `POST /predict_batch` - Predicciones en lote

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
curl https://[TU-API-URL].onrender.com/health

# Información del modelo
curl https://[TU-API-URL].onrender.com/model_info

# Predicción individual
curl -X POST https://[TU-API-URL].onrender.com/predict \
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
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 844.2,
    "tenure_group": "6-12 months",
    "TotalServices": 1,
    "AvgChargePerService": 70.35,
    "ChargeToTenureRatio": 5.86,
    "HasMultipleServices": 0,
    "HasStreamingServices": 0
  }'
```

### Probar API con Python

```python
import requests

# URL de tu API
API_URL = "https://[TU-API-URL].onrender.com"

# Health check
response = requests.get(f"{API_URL}/health")
print(response.json())

# Predicción
customer_data = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    # ... resto de features
}

response = requests.post(f"{API_URL}/predict", json=customer_data)
print(response.json())
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

Una vez deployado, actualizar este archivo con:
- [ ] URL real de la API
- [ ] URL real del Dashboard
- [ ] Fecha de deployment
- [ ] Capturas de pantalla
- [ ] Métricas de uso iniciales

---

**Última actualización**: 2025-11-20
**Estado**: ⏳ Preparado para deployment
**Responsable**: Álvaro Ángel Molina (@alvaretto)

