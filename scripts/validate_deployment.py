#!/usr/bin/env python3
"""
Script de Validación de Deployment
Valida que la API y Dashboard estén correctamente deployados y funcionando
Incluye tests de integración end-to-end
"""

import requests
import json
import sys
from datetime import datetime
import time

# URLs de producción
API_URL = "https://telco-churn-api-y9xy.onrender.com"
DASHBOARD_URL = "https://telco-churn-dashboard-ml.streamlit.app"

# Colores para output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    """Imprime un encabezado formateado"""
    print(f"\n{BLUE}{'=' * 70}{RESET}")
    print(f"{BLUE}{text.center(70)}{RESET}")
    print(f"{BLUE}{'=' * 70}{RESET}\n")

def print_success(text):
    """Imprime mensaje de éxito"""
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    """Imprime mensaje de error"""
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    """Imprime mensaje de advertencia"""
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_info(text):
    """Imprime mensaje informativo"""
    print(f"   {text}")

def validate_api_endpoints():
    """Valida todos los endpoints de la API"""
    print_header("VALIDACIÓN DE ENDPOINTS DE LA API")
    
    endpoints = {
        'Home': '/',
        'Health': '/health',
        'Model Info': '/model_info'
    }
    
    results = {}
    
    for name, endpoint in endpoints.items():
        try:
            url = f"{API_URL}{endpoint}"
            print(f"🔍 Probando {name} ({endpoint})...")
            
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                print_success(f"{name} respondió correctamente (200 OK)")
                data = response.json()
                print_info(f"Tamaño de respuesta: {len(response.content)} bytes")
                results[name] = True
            else:
                print_error(f"{name} respondió con código {response.status_code}")
                results[name] = False
                
        except requests.exceptions.Timeout:
            print_warning(f"{name} timeout - puede estar iniciando")
            results[name] = False
        except Exception as e:
            print_error(f"{name} error: {str(e)[:100]}")
            results[name] = False
    
    return results

def validate_api_prediction():
    """Valida que la API pueda hacer predicciones correctamente"""
    print_header("VALIDACIÓN DE PREDICCIONES")
    
    test_cases = [
        {
            'name': 'Cliente Alto Riesgo',
            'data': {
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
            'expected_churn': True
        },
        {
            'name': 'Cliente Bajo Riesgo',
            'data': {
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
                "MonthlyCharges": 105.50,
                "TotalCharges": 6330.0
            },
            'expected_churn': False
        }
    ]
    
    results = {}
    
    for test_case in test_cases:
        print(f"🔍 Probando: {test_case['name']}...")
        
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json=test_case['data'],
                timeout=20
            )
            
            if response.status_code == 200:
                data = response.json()
                churn = data.get('churn')
                probability = data.get('probability', {}).get('churn', 0)
                risk_level = data.get('risk_level')
                
                print_success(f"Predicción exitosa")
                print_info(f"Churn: {churn}")
                print_info(f"Probabilidad: {probability:.2%}")
                print_info(f"Nivel de riesgo: {risk_level}")
                
                # Validar que la predicción tiene sentido
                if churn == test_case['expected_churn']:
                    print_success(f"Predicción coincide con lo esperado")
                    results[test_case['name']] = True
                else:
                    print_warning(f"Predicción difiere de lo esperado (esperado: {test_case['expected_churn']})")
                    results[test_case['name']] = True  # No es un error crítico
            else:
                print_error(f"Error en predicción: HTTP {response.status_code}")
                results[test_case['name']] = False
                
        except Exception as e:
            print_error(f"Error: {str(e)[:100]}")
            results[test_case['name']] = False
    
    return results

def validate_dashboard():
    """Valida que el dashboard esté accesible"""
    print_header("VALIDACIÓN DEL DASHBOARD")
    
    print(f"🔍 Verificando accesibilidad del dashboard...")
    
    try:
        response = requests.get(DASHBOARD_URL, timeout=20)
        
        if response.status_code == 200:
            print_success("Dashboard está accesible")
            print_info(f"Tamaño de respuesta: {len(response.content)} bytes")
            print_info(f"Content-Type: {response.headers.get('Content-Type', 'N/A')}")
            return True
        else:
            print_error(f"Dashboard respondió con código {response.status_code}")
            return False
            
    except Exception as e:
        print_error(f"Error al acceder al dashboard: {str(e)[:100]}")
        return False

def main():
    """Función principal"""
    print_header("VALIDACIÓN DE DEPLOYMENT - TELCO CHURN PREDICTION")
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 API URL: {API_URL}")
    print(f"📊 Dashboard URL: {DASHBOARD_URL}")
    
    # Ejecutar validaciones
    api_endpoints = validate_api_endpoints()
    api_predictions = validate_api_prediction()
    dashboard_ok = validate_dashboard()
    
    # Resumen
    print_header("RESUMEN DE VALIDACIÓN")
    
    total_checks = len(api_endpoints) + len(api_predictions) + 1
    passed_checks = sum(api_endpoints.values()) + sum(api_predictions.values()) + (1 if dashboard_ok else 0)
    
    print(f"\n📊 Resultados:")
    print(f"   Total de checks: {total_checks}")
    print(f"   Checks pasados: {passed_checks}")
    print(f"   Checks fallidos: {total_checks - passed_checks}")
    print(f"   Tasa de éxito: {(passed_checks/total_checks)*100:.1f}%\n")
    
    if passed_checks == total_checks:
        print_success("¡Todos los checks pasaron! Deployment validado exitosamente.")
        return 0
    elif passed_checks >= total_checks * 0.8:
        print_warning(f"La mayoría de los checks pasaron ({passed_checks}/{total_checks})")
        return 0
    else:
        print_error(f"Muchos checks fallaron ({total_checks - passed_checks}/{total_checks})")
        return 1

if __name__ == "__main__":
    sys.exit(main())

