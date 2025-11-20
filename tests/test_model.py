"""
Unit tests for the ML model
"""

import pytest
import joblib
import pandas as pd
import numpy as np
import os
import json

# Paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'churn_model.pkl')
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'preprocessor.pkl')
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

@pytest.fixture
def model():
    """Load the trained model"""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

@pytest.fixture
def preprocessor():
    """Load the preprocessor"""
    if os.path.exists(PREPROCESSOR_PATH):
        return joblib.load(PREPROCESSOR_PATH)
    return None

@pytest.fixture
def metadata():
    """Load model metadata"""
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, 'r') as f:
            return json.load(f)
    return {}

def test_model_exists():
    """Test that model file exists"""
    assert os.path.exists(MODEL_PATH), "Model file not found"

def test_preprocessor_exists():
    """Test that preprocessor file exists"""
    assert os.path.exists(PREPROCESSOR_PATH), "Preprocessor file not found"

def test_metadata_exists():
    """Test that metadata file exists"""
    assert os.path.exists(METADATA_PATH), "Metadata file not found"

def test_model_loads(model):
    """Test that model loads successfully"""
    assert model is not None, "Model failed to load"

def test_preprocessor_loads(preprocessor):
    """Test that preprocessor loads successfully"""
    assert preprocessor is not None, "Preprocessor failed to load"

def test_metadata_structure(metadata):
    """Test metadata has required fields"""
    assert 'model_type' in metadata
    assert 'metrics' in metadata
    assert 'features' in metadata
    assert 'n_features' in metadata

def test_model_has_predict_method(model):
    """Test that model has predict method"""
    if model is not None:
        assert hasattr(model, 'predict'), "Model missing predict method"
        assert hasattr(model, 'predict_proba'), "Model missing predict_proba method"

def test_model_prediction_shape(model, metadata):
    """Test that model predictions have correct shape"""
    if model is None or not metadata:
        pytest.skip("Model or metadata not available")
    
    # Create sample data
    features = metadata.get('features', [])
    if not features:
        pytest.skip("No features in metadata")
    
    # Create dummy data (all zeros for simplicity)
    sample_data = pd.DataFrame([[0] * len(features)], columns=features)
    
    try:
        prediction = model.predict(sample_data)
        assert prediction.shape == (1,), "Prediction shape incorrect"
        assert prediction[0] in [0, 1], "Prediction not binary"
    except Exception as e:
        pytest.fail(f"Prediction failed: {e}")

def test_model_probability_shape(model, metadata):
    """Test that model probabilities have correct shape"""
    if model is None or not metadata:
        pytest.skip("Model or metadata not available")
    
    features = metadata.get('features', [])
    if not features:
        pytest.skip("No features in metadata")
    
    sample_data = pd.DataFrame([[0] * len(features)], columns=features)
    
    try:
        probabilities = model.predict_proba(sample_data)
        assert probabilities.shape == (1, 2), "Probability shape incorrect"
        assert np.isclose(probabilities.sum(), 1.0), "Probabilities don't sum to 1"
    except Exception as e:
        pytest.fail(f"Probability prediction failed: {e}")

def test_metadata_metrics(metadata):
    """Test that metadata contains valid metrics"""
    if not metadata:
        pytest.skip("Metadata not available")
    
    metrics = metadata.get('metrics', {})
    assert 'roc_auc' in metrics
    assert 'recall' in metrics
    assert 'precision' in metrics
    assert 'f1_score' in metrics
    
    # Check metric ranges
    assert 0 <= metrics['roc_auc'] <= 1
    assert 0 <= metrics['recall'] <= 1
    assert 0 <= metrics['precision'] <= 1
    assert 0 <= metrics['f1_score'] <= 1

if __name__ == '__main__':
    pytest.main([__file__, '-v'])

