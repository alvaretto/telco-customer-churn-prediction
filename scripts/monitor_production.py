#!/usr/bin/env python3
"""
Script de Monitoreo de Producción
Verifica el estado de la API y Dashboard en producción
No requiere dependencias pesadas - solo requests
"""

import requests
import json
from datetime import datetime
import sys

# URLs de producción
API_URL = "https://telco-churn-api-y9xy.onrender.com"
DASHBOARD_URL = "https://telco-churn-dashboard-ml.streamlit.app"

def check_api_health():
    """Verifica el estado de salud de la API"""
    print("🔍 Verificando API...")
    try:
        response = requests.get(f"{API_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API está funcionando")
            print(f"   - Status: {data.get('status')}")
            print(f"   - Modelo cargado: {data.get('model_loaded')}")
            print(f"   - Preprocessor cargado: {data.get('preprocessor_loaded')}")
            return True
        else:
            print(f"❌ API respondió con código {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("⏱️  API timeout - puede estar iniciando (Render Free tier)")
        return False
    except Exception as e:
        print(f"❌ Error al verificar API: {e}")
        return False

def check_api_model_info():
    """Verifica la información del modelo"""
    print("\n🔍 Verificando información del modelo...")
    try:
        response = requests.get(f"{API_URL}/model_info", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Información del modelo disponible")
            print(f"   - Tipo: {data.get('model_type')}")
            print(f"   - Features: {data.get('n_features')}")
            metrics = data.get('metrics', {})
            print(f"   - ROC-AUC: {metrics.get('roc_auc', 'N/A')}")
            print(f"   - Recall: {metrics.get('recall', 'N/A')}")
            return True
        else:
            print(f"❌ Model info respondió con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error al verificar model info: {e}")
        return False

def check_api_prediction():
    """Verifica que la API pueda hacer predicciones"""
    print("\n🔍 Verificando predicción de la API...")
    
    # Datos de prueba (cliente de alto riesgo)
    test_data = {
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
    
    try:
        response = requests.post(f"{API_URL}/predict", json=test_data, timeout=15)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Predicción exitosa")
            print(f"   - Churn: {data.get('churn')}")
            print(f"   - Probabilidad: {data.get('probability', {}).get('churn', 'N/A')}")
            print(f"   - Nivel de riesgo: {data.get('risk_level')}")
            return True
        else:
            print(f"❌ Predicción respondió con código {response.status_code}")
            print(f"   Respuesta: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"❌ Error al verificar predicción: {e}")
        return False

def check_dashboard():
    """Verifica que el dashboard esté accesible"""
    print("\n🔍 Verificando Dashboard...")
    try:
        response = requests.get(DASHBOARD_URL, timeout=15)
        if response.status_code == 200:
            print(f"✅ Dashboard está accesible")
            print(f"   - Tamaño de respuesta: {len(response.content)} bytes")
            return True
        else:
            print(f"❌ Dashboard respondió con código {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error al verificar Dashboard: {e}")
        return False

def main():
    """Función principal"""
    print("=" * 60)
    print("🚀 MONITOREO DE PRODUCCIÓN - TELCO CHURN PREDICTION")
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    results = {
        'api_health': check_api_health(),
        'api_model_info': check_api_model_info(),
        'api_prediction': check_api_prediction(),
        'dashboard': check_dashboard()
    }
    
    print("\n" + "=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    
    total = len(results)
    passed = sum(results.values())
    
    for check, status in results.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {check.replace('_', ' ').title()}")
    
    print(f"\n🎯 Total: {passed}/{total} checks pasaron")
    
    if passed == total:
        print("🎉 ¡Todos los servicios están funcionando correctamente!")
        return 0
    else:
        print("⚠️  Algunos servicios tienen problemas")
        return 1

if __name__ == "__main__":
    sys.exit(main())

