"""
Unit tests for the Flask API
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data
    assert data['version'] == '1.0.0'

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code in [200, 503]
    data = response.get_json()
    assert 'status' in data
    assert 'model_loaded' in data
    assert 'preprocessor_loaded' in data
    assert 'timestamp' in data

def test_model_info_endpoint(client):
    """Test the model info endpoint"""
    response = client.get('/model_info')
    assert response.status_code in [200, 503]
    data = response.get_json()
    if response.status_code == 200:
        assert 'model_type' in data
        assert 'metrics' in data

def test_predict_endpoint_no_data(client):
    """Test predict endpoint with no data"""
    response = client.post('/predict', json={})
    assert response.status_code in [400, 503]

def test_predict_endpoint_with_data(client):
    """Test predict endpoint with sample data"""
    sample_data = {
        'gender': 'Female',
        'SeniorCitizen': 0,
        'Partner': 'Yes',
        'Dependents': 'No',
        'tenure': 12,
        'PhoneService': 'Yes',
        'MultipleLines': 'No',
        'InternetService': 'Fiber optic',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'Yes',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'No',
        'StreamingMovies': 'No',
        'Contract': 'Month-to-month',
        'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check',
        'MonthlyCharges': 70.35,
        'TotalCharges': 844.2,
        'ChargeRatio': 0.083,
        'AvgMonthlyCharges': 70.35,
        'TenureGroup': '0-12',
        'TotalServices': 3,
        'SeniorWithDependents': 0,
        'HighValueContract': 0
    }
    
    response = client.post('/predict', json=sample_data)
    assert response.status_code in [200, 503]
    
    if response.status_code == 200:
        data = response.get_json()
        assert 'prediction' in data
        assert 'probability' in data
        assert 'risk_level' in data

def test_predict_batch_endpoint(client):
    """Test batch prediction endpoint"""
    sample_data = [{
        'gender': 'Female',
        'SeniorCitizen': 0,
        'Partner': 'Yes',
        'Dependents': 'No',
        'tenure': 12,
        'PhoneService': 'Yes',
        'MultipleLines': 'No',
        'InternetService': 'Fiber optic',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'Yes',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'No',
        'StreamingMovies': 'No',
        'Contract': 'Month-to-month',
        'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check',
        'MonthlyCharges': 70.35,
        'TotalCharges': 844.2,
        'ChargeRatio': 0.083,
        'AvgMonthlyCharges': 70.35,
        'TenureGroup': '0-12',
        'TotalServices': 3,
        'SeniorWithDependents': 0,
        'HighValueContract': 0
    }]
    
    response = client.post('/predict_batch', json=sample_data)
    assert response.status_code in [200, 503]
    
    if response.status_code == 200:
        data = response.get_json()
        assert 'predictions' in data
        assert 'total' in data
        assert 'churn_count' in data
        assert 'churn_rate' in data

if __name__ == '__main__':
    pytest.main([__file__, '-v'])

