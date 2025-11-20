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

# Expected features (from metadata)
EXPECTED_FEATURES = metadata.get('features', [])


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
        'n_features': metadata.get('n_features'),
        'features': metadata.get('features'),
        'training_date': metadata.get('training_date'),
        'model_size_mb': metadata.get('model_size_mb'),
        'environment': metadata.get('environment')
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Single customer churn prediction
    
    Expected JSON body with customer features
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
        
        # Validate features
        missing_features = set(EXPECTED_FEATURES) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing features',
                'missing': list(missing_features)
            }), 400
        
        # Select only expected features in correct order
        df = df[EXPECTED_FEATURES]
        
        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0]
        
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
    
    Expected JSON body with list of customer features
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
        missing_features = set(EXPECTED_FEATURES) - set(df.columns)
        if missing_features:
            return jsonify({
                'error': 'Missing features',
                'missing': list(missing_features)
            }), 400

        # Select only expected features in correct order
        df = df[EXPECTED_FEATURES]

        # Make predictions
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)

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

