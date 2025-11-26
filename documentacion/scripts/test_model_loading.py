#!/usr/bin/env python3
"""
Script rápido para verificar que el modelo se puede cargar localmente
Requiere: joblib, scikit-learn
"""

import os
import sys
import time
import json

print("=" * 60)
print("🧪 TEST DE CARGA DEL MODELO")
print("=" * 60)

# Verificar que los archivos existen
model_path = 'models/churn_model.pkl'
preprocessor_path = 'models/preprocessor.pkl'
metadata_path = 'models/metadata.json'

print("\n1️⃣ Verificando archivos...")
for path in [model_path, preprocessor_path, metadata_path]:
    if os.path.exists(path):
        size = os.path.getsize(path) / (1024 * 1024)  # MB
        print(f"   ✅ {path} ({size:.2f} MB)")
    else:
        print(f"   ❌ {path} NO ENCONTRADO")
        sys.exit(1)

# Intentar importar dependencias
print("\n2️⃣ Verificando dependencias...")
try:
    import joblib
    print("   ✅ joblib instalado")
except ImportError:
    print("   ❌ joblib NO instalado. Ejecuta: pip install joblib")
    sys.exit(1)

try:
    import sklearn
    print(f"   ✅ scikit-learn {sklearn.__version__} instalado")
except ImportError:
    print("   ❌ scikit-learn NO instalado. Ejecuta: pip install scikit-learn")
    sys.exit(1)

# Cargar modelo
print("\n3️⃣ Cargando modelo...")
start_time = time.time()

try:
    model = joblib.load(model_path)
    load_time = time.time() - start_time
    print(f"   ✅ Modelo cargado en {load_time:.2f} segundos")
    print(f"   📊 Tipo: {type(model).__name__}")
except Exception as e:
    print(f"   ❌ Error cargando modelo: {e}")
    sys.exit(1)

# Cargar preprocessor
print("\n4️⃣ Cargando preprocessor...")
try:
    preprocessor = joblib.load(preprocessor_path)
    print(f"   ✅ Preprocessor cargado")
except Exception as e:
    print(f"   ❌ Error cargando preprocessor: {e}")
    sys.exit(1)

# Cargar metadata
print("\n5️⃣ Cargando metadata...")
try:
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    print(f"   ✅ Metadata cargada")
    print(f"   📊 Modelo: {metadata.get('model_type')}")
    print(f"   📊 Features: {metadata.get('n_features')}")
    print(f"   📊 ROC-AUC: {metadata.get('metrics', {}).get('roc_auc')}")
except Exception as e:
    print(f"   ❌ Error cargando metadata: {e}")
    sys.exit(1)

# Test de predicción simple
print("\n6️⃣ Test de predicción...")
try:
    import pandas as pd
    import numpy as np
    
    # Crear datos de prueba (todos ceros)
    features = metadata.get('features', [])
    test_data = pd.DataFrame([[0] * len(features)], columns=features)
    
    # Hacer predicción
    prediction = model.predict(test_data)[0]
    probability = model.predict_proba(test_data)[0]
    
    print(f"   ✅ Predicción exitosa")
    print(f"   📊 Resultado: {prediction}")
    print(f"   📊 Probabilidades: No Churn={probability[0]:.2f}, Churn={probability[1]:.2f}")
except Exception as e:
    print(f"   ❌ Error en predicción: {e}")
    sys.exit(1)

# Resumen
print("\n" + "=" * 60)
print("✅ TODOS LOS TESTS PASARON")
print("=" * 60)
print("\n💡 El modelo está listo para usar en:")
print("   - API Flask (api/app.py)")
print("   - Dashboard Streamlit (dashboard/app.py)")
print("   - Tests automatizados (tests/)")
print("\n🚀 Próximo paso: Ejecutar la API o el Dashboard")
print("=" * 60)

