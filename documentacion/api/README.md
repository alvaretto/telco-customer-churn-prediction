# 🚀 Telco Customer Churn Prediction API

Flask REST API for predicting customer churn using a Random Forest model.

**🌐 Production URL:** `https://telco-churn-api-y9xy.onrender.com`

## ✨ Features

- ✅ Acepta datos categóricos originales (sin preprocesamiento)
- ✅ Aplica feature engineering automáticamente
- ✅ Preprocesamiento automático (scaling y encoding)
- ✅ Predicciones individuales y en lote
- ✅ Niveles de riesgo (low, medium, high, critical)
- ✅ Métricas del modelo (ROC-AUC: 0.87, Recall: 0.83)

## 📋 Endpoints

### `GET /`
Home endpoint with API information

**Response:**
```json
{
  "message": "Telco Customer Churn Prediction API",
  "version": "1.0.0",
  "status": "running",
  "endpoints": {...}
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "preprocessor_loaded": true,
  "timestamp": "2025-11-20T23:58:51"
}
```

### `GET /model_info`
Get model information and metrics

**Response:**
```json
{
  "model_type": "RandomForestClassifier",
  "metrics": {
    "roc_auc": 0.87,
    "recall": 0.83,
    "precision": 0.72,
    "f1_score": 0.77
  },
  "n_features_original": 19,
  "n_features_total": 25,
  "original_features": ["gender", "SeniorCitizen", ...],
  "engineered_features": ["ChargeRatio", "AvgMonthlyCharges", ...],
  "library_versions": {
    "sklearn": "1.5.2",
    "pandas": "2.1.4",
    "numpy": "1.26.2",
    "joblib": "1.4.2"
  }
}
```

### `POST /predict`
Single customer churn prediction

**⚠️ IMPORTANTE:** Solo envía las **19 features originales**. El feature engineering se aplica automáticamente.

**Request Body (solo features originales):**
```json
{
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
```

**Response:**
```json
{
  "prediction": 1,
  "churn": true,
  "probability": {
    "no_churn": 0.391,
    "churn": 0.609
  },
  "risk_level": "high",
  "timestamp": "2025-11-20T23:59:06"
}
```

**Ejemplo con curl:**
```bash
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
```

### `POST /predict_batch`
Batch churn predictions (múltiples clientes a la vez)

**Request Body (array de features originales):**
```json
[
  {
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
  },
  {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "Yes",
    "tenure": 60,
    ...
  }
]
```

**Response:**
```json
{
  "predictions": [
    {
      "index": 0,
      "prediction": 1,
      "churn": true,
      "probability": {
        "no_churn": 0.391,
        "churn": 0.609
      },
      "risk_level": "high"
    },
    {
      "index": 1,
      "prediction": 0,
      "churn": false,
      "probability": {
        "no_churn": 0.764,
        "churn": 0.236
      },
      "risk_level": "low"
    }
  ],
  "total": 2,
  "churn_count": 1,
  "churn_rate": 0.5,
  "timestamp": "2025-11-20T23:59:16"
}
```

## 🔧 Feature Engineering Automático

La API aplica automáticamente las siguientes transformaciones:

1. **ChargeRatio**: `MonthlyCharges / (TotalCharges + 1)`
2. **AvgMonthlyCharges**: `TotalCharges / (tenure + 1)`
3. **TenureGroup**: Categorización de tenure en grupos (0-1 año, 1-2 años, 2-4 años, 4+ años)
4. **TotalServices**: Conteo de servicios contratados
5. **SeniorWithDependents**: Senior citizen con dependientes (binario)
6. **HighValueContract**: Contrato largo + cargos altos (binario)

**No necesitas calcular estas features manualmente**, solo envía los datos originales.

## 🛠️ Installation

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
cd api
python app.py
```

The API will be available at `http://localhost:5000`

### Docker

1. Build the image:
```bash
docker build -t churn-api -f api/Dockerfile .
```

2. Run the container:
```bash
docker run -p 5000:5000 churn-api
```

## 🌐 Deployment

### Render (Producción Actual)

**URL de producción:** `https://telco-churn-api-y9xy.onrender.com`

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set root directory: `api`
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn --bind 0.0.0.0:$PORT app:app`
6. Deploy!

### Environment Variables

- `PORT`: Port to run the API (default: 5000)

## 📊 Risk Levels

- **low**: Churn probability < 30%
- **medium**: Churn probability 30-50%
- **high**: Churn probability 50-70%
- **critical**: Churn probability > 70%

## 🧪 Testing

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d @sample_customer.json
```

## 📝 License

MIT

