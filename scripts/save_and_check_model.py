"""
Script para agregar al final del notebook Telco-Customer-Churn.ipynb
Serializa el modelo y verifica su tamaño inmediatamente.
"""

import joblib
import json
import os
from datetime import datetime


def save_model_and_check_size(model, preprocessor, X, y, model_metrics):
    """
    Guarda el modelo, preprocessor y metadata, y verifica el tamaño.
    
    Parámetros:
    -----------
    model : sklearn model
        Modelo entrenado (ej: best_model)
    preprocessor : sklearn transformer
        Pipeline de preprocesamiento
    X : DataFrame
        Features utilizadas para entrenamiento
    y : Series
        Target variable
    model_metrics : dict
        Diccionario con métricas del modelo (roc_auc, recall, precision, f1)
    """
    
    # Crear directorio si no existe
    os.makedirs('models', exist_ok=True)
    
    print("=" * 70)
    print("💾 GUARDANDO MODELO Y VERIFICANDO TAMAÑO")
    print("=" * 70)
    print()
    
    # 1. Guardar modelo
    print("1️⃣  Guardando modelo Random Forest...")
    model_path = 'models/churn_model.pkl'
    joblib.dump(model, model_path)
    model_size = os.path.getsize(model_path) / (1024 * 1024)
    print(f"   ✅ Modelo guardado: {model_path}")
    print(f"   📊 Tamaño: {model_size:.2f} MB")
    print()
    
    # 2. Guardar preprocessor
    print("2️⃣  Guardando preprocessor...")
    preprocessor_path = 'models/preprocessor.pkl'
    joblib.dump(preprocessor, preprocessor_path)
    preprocessor_size = os.path.getsize(preprocessor_path) / (1024 * 1024)
    print(f"   ✅ Preprocessor guardado: {preprocessor_path}")
    print(f"   📊 Tamaño: {preprocessor_size:.2f} MB")
    print()
    
    # 3. Guardar metadata
    print("3️⃣  Guardando metadata...")
    metadata = {
        'model_type': type(model).__name__,
        'model_params': model.get_params() if hasattr(model, 'get_params') else {},
        'metrics': model_metrics,
        'training_date': datetime.now().isoformat(),
        'features': list(X.columns),
        'n_features': len(X.columns),
        'n_samples_train': len(X),
        'target_name': y.name if hasattr(y, 'name') else 'Churn',
        'model_size_mb': round(model_size, 2),
        'preprocessor_size_mb': round(preprocessor_size, 2)
    }
    
    metadata_path = 'models/metadata.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    metadata_size = os.path.getsize(metadata_path) / (1024 * 1024)
    print(f"   ✅ Metadata guardada: {metadata_path}")
    print(f"   📊 Tamaño: {metadata_size:.4f} MB")
    print()
    
    # 4. Resumen de tamaños
    total_size = model_size + preprocessor_size + metadata_size
    
    print("=" * 70)
    print("📦 RESUMEN DE ARCHIVOS GUARDADOS:")
    print("=" * 70)
    print(f"   Modelo (churn_model.pkl):        {model_size:>10.2f} MB")
    print(f"   Preprocessor (preprocessor.pkl): {preprocessor_size:>10.2f} MB")
    print(f"   Metadata (metadata.json):        {metadata_size:>10.4f} MB")
    print("-" * 70)
    print(f"   TOTAL:                           {total_size:>10.2f} MB")
    print("=" * 70)
    print()
    
    # 5. Evaluación para deployment
    print("🎯 EVALUACIÓN PARA DEPLOYMENT:")
    print("-" * 70)
    
    if total_size < 10:
        print("✅ EXCELENTE: Modelo muy ligero (< 10 MB)")
        print("   ✅ Perfecto para Git (sin Git LFS)")
        print("   ✅ Carga rápida en Render/Railway")
        print("   ✅ Bajo consumo de RAM en producción")
    elif total_size < 50:
        print("✅ MUY BUENO: Modelo ligero (< 50 MB)")
        print("   ✅ Puede almacenarse en Git directamente")
        print("   ✅ Deployment rápido en Render/Railway")
    elif total_size < 100:
        print("✅ BUENO: Modelo de tamaño moderado (< 100 MB)")
        print("   ✅ Puede almacenarse en Git (límite 100 MB)")
        print("   ⚠️  Considera usar Git LFS si crece más")
    else:
        print("⚠️  GRANDE: Modelo > 100 MB")
        print("   ❌ NO puede almacenarse directamente en GitHub")
        print("   💡 SOLUCIONES:")
        print("      - Usar Git LFS (Large File Storage)")
        print("      - Almacenar en Google Cloud Storage")
        print("      - Almacenar en AWS S3")
        print("      - Reducir complejidad del modelo")
    
    print()
    
    # 6. Estimación de RAM en producción
    estimated_ram = total_size * 3  # Regla general: 3x el tamaño del modelo
    
    print("💾 ESTIMACIÓN DE RAM EN PRODUCCIÓN:")
    print("-" * 70)
    print(f"   Tamaño del modelo:               {total_size:>10.2f} MB")
    print(f"   RAM estimada necesaria:          {estimated_ram:>10.2f} MB")
    print()
    
    if estimated_ram < 512:
        print("   ✅ Cabe en Render Free (512 MB RAM)")
        print("   ✅ Cabe en Railway Free (512 MB RAM)")
    elif estimated_ram < 1024:
        print("   ⚠️  Puede ser justo para Render Free (512 MB RAM)")
        print("   ✅ Cabe en Railway Free (8 GB RAM)")
        print("   💡 Considera Railway si tienes problemas en Render")
    else:
        print("   ❌ Excede Render Free (512 MB RAM)")
        print("   ✅ Cabe en Railway Free (8 GB RAM)")
        print("   💡 RECOMENDACIÓN: Usar Railway en lugar de Render")
    
    print()
    print("=" * 70)
    
    # 7. Verificar que se puede cargar
    print("🔍 VERIFICANDO QUE EL MODELO SE PUEDE CARGAR...")
    print("-" * 70)
    
    try:
        loaded_model = joblib.load(model_path)
        loaded_preprocessor = joblib.load(preprocessor_path)
        print("   ✅ Modelo cargado correctamente")
        print("   ✅ Preprocessor cargado correctamente")
        
        # Verificar que tiene los métodos necesarios
        assert hasattr(loaded_model, 'predict'), "Modelo no tiene método predict"
        assert hasattr(loaded_model, 'predict_proba'), "Modelo no tiene método predict_proba"
        print("   ✅ Métodos predict y predict_proba disponibles")
        
    except Exception as e:
        print(f"   ❌ ERROR al cargar el modelo: {e}")
        return False
    
    print()
    print("=" * 70)
    print("✅ MODELO GUARDADO Y VERIFICADO EXITOSAMENTE")
    print("=" * 70)
    print()
    print("📝 PRÓXIMOS PASOS:")
    print("   1. Ejecutar: python scripts/check_model_size.py")
    print("   2. Revisar el tamaño total del deployment")
    print("   3. Continuar con la creación de la API Flask")
    print()
    
    return True


# EJEMPLO DE USO EN EL NOTEBOOK:
# ================================
# Agregar esta celda al final del notebook después de entrenar el modelo:

"""
# Guardar modelo y verificar tamaño
from scripts.save_and_check_model import save_model_and_check_size

model_metrics = {
    'roc_auc': 0.87,
    'recall': 0.83,
    'precision': 0.72,
    'f1_score': 0.77
}

save_model_and_check_size(
    model=best_model,
    preprocessor=preprocessor,
    X=X_train,
    y=y_train,
    model_metrics=model_metrics
)
"""

