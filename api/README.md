# 🚀 Telco Customer Churn Prediction API

Flask REST API for predicting customer churn using a Random Forest model.

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
  "timestamp": "2025-11-20T19:45:00"
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
  "n_features": 25,
  "training_date": "2025-11-20T19:25:05"
}
```

### `POST /predict`
Single customer churn prediction

**Request Body:**
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
  "TotalCharges": 844.2,
  "ChargeRatio": 0.083,
  "AvgMonthlyCharges": 70.35,
  "TenureGroup": "0-12",
  "TotalServices": 3,
  "SeniorWithDependents": 0,
  "HighValueContract": 0
}
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
  "timestamp": "2025-11-20T19:45:00"
}
```

### `POST /predict_batch`
Batch churn predictions

**Request Body:**
```json
[
  {customer_1_data},
  {customer_2_data},
  ...
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
        "no_churn": 0.23,
        "churn": 0.77
      },
      "risk_level": "critical"
    },
    ...
  ],
  "total": 100,
  "churn_count": 27,
  "churn_rate": 0.27,
  "timestamp": "2025-11-20T19:45:00"
}
```

## 🛠️ Installation

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Docker

1. Build the image:
```bash
docker build -t churn-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 churn-api
```

## 🌐 Deployment

### Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn --bind 0.0.0.0:$PORT app:app`
5. Deploy!

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

