# 📘 API Usage Guide

Complete guide for using the Telco Customer Churn Prediction API.

## 🚀 Quick Start

### Base URL

**Local Development:**
```
http://localhost:5000
```

**Production (Render):**
```
https://your-app-name.onrender.com
```

## 📋 Endpoints

### 1. Home - `GET /`

Get API information and available endpoints.

**Request:**
```bash
curl http://localhost:5000/
```

**Response:**
```json
{
  "message": "Telco Customer Churn Prediction API",
  "version": "1.0.0",
  "status": "running",
  "endpoints": {
    "POST /predict": "Single customer churn prediction",
    "POST /predict_batch": "Batch churn predictions",
    "GET /health": "Health check",
    "GET /model_info": "Model information and metrics"
  }
}
```

---

### 2. Health Check - `GET /health`

Check if the API and model are running properly.

**Request:**
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "preprocessor_loaded": true,
  "timestamp": "2025-11-20T19:45:00.123456"
}
```

**Status Codes:**
- `200`: Healthy
- `503`: Unhealthy (model not loaded)

---

### 3. Model Info - `GET /model_info`

Get model information and performance metrics.

**Request:**
```bash
curl http://localhost:5000/model_info
```

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
  "n_features": 25,
  "features": ["gender", "SeniorCitizen", ...],
  "training_date": "2025-11-20T19:25:05.731544",
  "model_size_mb": 64.09,
  "environment": "Google Colab"
}
```

---

### 4. Single Prediction - `POST /predict`

Predict churn for a single customer.

**Request:**
```bash
curl -X POST http://localhost:5000/predict \
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
    "TotalCharges": 844.2,
    "ChargeRatio": 0.083,
    "AvgMonthlyCharges": 70.35,
    "TenureGroup": "0-12",
    "TotalServices": 3,
    "SeniorWithDependents": 0,
    "HighValueContract": 0
  }'
```

**Response:**
```json
{
  "prediction": 1,
  "churn": true,
  "probability": {
    "no_churn": 0.23,
    "churn": 0.77
  },
  "risk_level": "critical",
  "timestamp": "2025-11-20T19:45:00.123456"
}
```

**Risk Levels:**
- `low`: < 30% churn probability
- `medium`: 30-50% churn probability
- `high`: 50-70% churn probability
- `critical`: > 70% churn probability

---

### 5. Batch Prediction - `POST /predict_batch`

Predict churn for multiple customers at once.

**Request:**
```bash
curl -X POST http://localhost:5000/predict_batch \
  -H "Content-Type: application/json" \
  -d '[
    {customer_1_data},
    {customer_2_data},
    {customer_3_data}
  ]'
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
        "no_churn": 0.23,
        "churn": 0.77
      },
      "risk_level": "critical"
    },
    ...
  ],
  "total": 3,
  "churn_count": 2,
  "churn_rate": 0.67,
  "timestamp": "2025-11-20T19:45:00.123456"
}
```

## 🔧 Error Handling

### Common Errors

**400 Bad Request - Missing Data:**
```json
{
  "error": "No data provided"
}
```

**400 Bad Request - Missing Features:**
```json
{
  "error": "Missing features",
  "missing": ["tenure", "MonthlyCharges"]
}
```

**503 Service Unavailable - Model Not Loaded:**
```json
{
  "error": "Model not loaded"
}
```

## 💻 Code Examples

### Python

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "gender": "Female",
    "SeniorCitizen": 0,
    # ... other features
}

response = requests.post(url, json=data)
result = response.json()

print(f"Churn Probability: {result['probability']['churn']:.2%}")
print(f"Risk Level: {result['risk_level']}")
```

### JavaScript

```javascript
const url = 'http://localhost:5000/predict';
const data = {
  gender: 'Female',
  SeniorCitizen: 0,
  // ... other features
};

fetch(url, {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
  console.log(`Churn Probability: ${result.probability.churn}`);
  console.log(`Risk Level: ${result.risk_level}`);
});
```

## 📊 Required Features

All 25 features must be provided for prediction. See `/model_info` endpoint for the complete list.

