"""
Telco Customer Churn Prediction API
Flask REST API for churn prediction using Random Forest model
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import os
from datetime import datetime
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model and preprocessor
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'churn_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'preprocessor.pkl')
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
    print("✅ Model and preprocessor loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    preprocessor = None
    metadata = {}

# Original features expected from user (before feature engineering)
ORIGINAL_FEATURES = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
    'MonthlyCharges', 'TotalCharges'
]


def apply_feature_engineering(df):
    """
    Apply feature engineering to match training data

    Args:
        df (pd.DataFrame): DataFrame with original features

    Returns:
        pd.DataFrame: DataFrame with engineered features
    """
    df_fe = df.copy()

    # 1. ChargeRatio: Monthly charges relative to total charges
    df_fe['ChargeRatio'] = df_fe['MonthlyCharges'] / (df_fe['TotalCharges'] + 1)

    # 2. AvgMonthlyCharges: Average monthly charges based on tenure
    df_fe['AvgMonthlyCharges'] = df_fe['TotalCharges'] / (df_fe['tenure'] + 1)

    # 3. TenureGroup: Categorize tenure into groups
    df_fe['TenureGroup'] = pd.cut(
        df_fe['tenure'],
        bins=[0, 12, 24, 48, 72],
        labels=['0-1 año', '1-2 años', '2-4 años', '4+ años']
    ).astype(str)

    # 4. TotalServices: Count of services contracted
    service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    df_fe['TotalServices'] = 0
    for col in service_cols:
        if col in df_fe.columns:
            df_fe['TotalServices'] += (df_fe[col] != 'No').astype(int)

    # 5. SeniorWithDependents: Senior citizen with dependents
    df_fe['SeniorWithDependents'] = (
        (df_fe['SeniorCitizen'] == 1) & (df_fe['Dependents'] == 'Yes')
    ).astype(int)

    # 6. HighValueContract: Long contract + high charges
    median_charges = df_fe['MonthlyCharges'].median()
    df_fe['HighValueContract'] = (
        (df_fe['Contract'].isin(['One year', 'Two year'])) &
        (df_fe['MonthlyCharges'] > median_charges)
    ).astype(int)

    return df_fe


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        'message': 'Telco Customer Churn Prediction API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'POST /predict': 'Single customer churn prediction',
            'POST /predict_batch': 'Batch churn predictions',
            'GET /health': 'Health check',
            'GET /model_info': 'Model information and metrics'
        },
        'documentation': '/docs'
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    is_healthy = model is not None and preprocessor is not None
    
    return jsonify({
        'status': 'healthy' if is_healthy else 'unhealthy',
        'model_loaded': model is not None,
        'preprocessor_loaded': preprocessor is not None,
        'timestamp': datetime.now().isoformat()
    }), 200 if is_healthy else 503


@app.route('/model_info', methods=['GET'])
def model_info():
    """Get model information and metrics"""
    if not metadata:
        return jsonify({'error': 'Model metadata not available'}), 503

    return jsonify({
        'model_type': metadata.get('model_type'),
        'metrics': metadata.get('metrics'),
        'n_features_total': metadata.get('n_features'),
        'n_features_original': len(ORIGINAL_FEATURES),
        'original_features': ORIGINAL_FEATURES,
        'engineered_features': ['ChargeRatio', 'AvgMonthlyCharges', 'TenureGroup',
                                'TotalServices', 'SeniorWithDependents', 'HighValueContract'],
        'training_date': metadata.get('training_date'),
        'model_size_mb': metadata.get('model_size_mb'),
        'environment': metadata.get('environment'),
        'library_versions': metadata.get('library_versions')
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Single customer churn prediction

    Expected JSON body with original customer features (before feature engineering)
    """
    if model is None or preprocessor is None:
        return jsonify({'error': 'Model not loaded'}), 503

    try:
        # Get JSON data
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Validate original features
        missing_features = set(ORIGINAL_FEATURES) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing features',
                'missing': list(missing_features),
                'expected_features': ORIGINAL_FEATURES
            }), 400

        # Apply feature engineering
        df_engineered = apply_feature_engineering(df)

        # Apply preprocessing (scaling and encoding)
        df_processed = preprocessor.transform(df_engineered)

        # Make prediction
        prediction = model.predict(df_processed)[0]
        probability = model.predict_proba(df_processed)[0]

        # Prepare response
        response = {
            'prediction': int(prediction),
            'churn': bool(prediction),
            'probability': {
                'no_churn': float(probability[0]),
                'churn': float(probability[1])
            },
            'risk_level': get_risk_level(probability[1]),
            'timestamp': datetime.now().isoformat()
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/predict_batch', methods=['POST'])
def predict_batch():
    """
    Batch churn predictions

    Expected JSON body with list of original customer features (before feature engineering)
    """
    if model is None or preprocessor is None:
        return jsonify({'error': 'Model not loaded'}), 503

    try:
        # Get JSON data
        data = request.get_json()

        if not data or not isinstance(data, list):
            return jsonify({'error': 'Expected list of customer data'}), 400

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Validate features
        missing_features = set(ORIGINAL_FEATURES) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing features',
                'missing': list(missing_features),
                'expected_features': ORIGINAL_FEATURES
            }), 400

        # Apply feature engineering
        df_engineered = apply_feature_engineering(df)

        # Apply preprocessing (scaling and encoding)
        df_processed = preprocessor.transform(df_engineered)

        # Make predictions
        predictions = model.predict(df_processed)
        probabilities = model.predict_proba(df_processed)

        # Prepare response
        results = []
        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            results.append({
                'index': i,
                'prediction': int(pred),
                'churn': bool(pred),
                'probability': {
                    'no_churn': float(prob[0]),
                    'churn': float(prob[1])
                },
                'risk_level': get_risk_level(prob[1])
            })

        response = {
            'predictions': results,
            'total': len(results),
            'churn_count': int(sum(predictions)),
            'churn_rate': float(sum(predictions) / len(predictions)),
            'timestamp': datetime.now().isoformat()
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_risk_level(churn_probability):
    """
    Classify risk level based on churn probability

    Args:
        churn_probability (float): Probability of churn (0-1)

    Returns:
        str: Risk level (low, medium, high, critical)
    """
    if churn_probability < 0.3:
        return 'low'
    elif churn_probability < 0.5:
        return 'medium'
    elif churn_probability < 0.7:
        return 'high'
    else:
        return 'critical'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

