#!/usr/bin/env python3
"""
Script para probar la API de predicción de churn en producción
Demuestra cómo usar la API con datos categóricos originales
"""

import requests
import json

# URL de la API en producción
API_URL = "https://telco-churn-api-y9xy.onrender.com"

def test_health():
    """Probar el endpoint de health check"""
    print("=" * 70)
    print("1️⃣  PROBANDO HEALTH CHECK")
    print("=" * 70)
    
    response = requests.get(f"{API_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_model_info():
    """Probar el endpoint de información del modelo"""
    print("=" * 70)
    print("2️⃣  PROBANDO MODEL INFO")
    print("=" * 70)
    
    response = requests.get(f"{API_URL}/model_info")
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Modelo: {data.get('model_type')}")
    print(f"ROC-AUC: {data.get('metrics', {}).get('roc_auc')}")
    print(f"Features originales: {data.get('n_features_original')}")
    print(f"Features totales (con engineering): {data.get('n_features_total')}")
    print(f"Versiones de librerías: {json.dumps(data.get('library_versions'), indent=2)}")
    print()

def test_predict_high_risk():
    """Probar predicción para cliente de alto riesgo"""
    print("=" * 70)
    print("3️⃣  PROBANDO PREDICCIÓN - CLIENTE DE ALTO RIESGO")
    print("=" * 70)
    
    # Cliente con características de alto riesgo de churn
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
    
    response = requests.post(
        f"{API_URL}/predict",
        json=customer_data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Predicción: {'CHURN' if result['churn'] else 'NO CHURN'}")
    print(f"Probabilidad de churn: {result['probability']['churn']:.2%}")
    print(f"Nivel de riesgo: {result['risk_level'].upper()}")
    print()

def test_predict_low_risk():
    """Probar predicción para cliente de bajo riesgo"""
    print("=" * 70)
    print("4️⃣  PROBANDO PREDICCIÓN - CLIENTE DE BAJO RIESGO")
    print("=" * 70)
    
    # Cliente con características de bajo riesgo de churn
    customer_data = {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 60,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Two year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Bank transfer (automatic)",
        "MonthlyCharges": 105.5,
        "TotalCharges": 6330.0
    }
    
    response = requests.post(
        f"{API_URL}/predict",
        json=customer_data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    result = response.json()
    print(f"Predicción: {'CHURN' if result['churn'] else 'NO CHURN'}")
    print(f"Probabilidad de churn: {result['probability']['churn']:.2%}")
    print(f"Nivel de riesgo: {result['risk_level'].upper()}")
    print()

if __name__ == "__main__":
    print("\n🚀 PROBANDO API DE PREDICCIÓN DE CHURN EN PRODUCCIÓN\n")
    
    try:
        test_health()
        test_model_info()
        test_predict_high_risk()
        test_predict_low_risk()
        
        print("=" * 70)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

