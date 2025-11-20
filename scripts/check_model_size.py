#!/usr/bin/env python3
"""
Script para verificar el tamaño del modelo de churn y estimar el tamaño total del deployment.
Ejecutar después de entrenar el modelo en el notebook.
"""

import os
import joblib
import json
from pathlib import Path


def get_size_mb(file_path):
    """Obtiene el tamaño de un archivo en MB."""
    if os.path.exists(file_path):
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)
        return size_mb
    return 0


def get_directory_size_mb(directory):
    """Calcula el tamaño total de un directorio en MB."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
                total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)


def check_model_files():
    """Verifica el tamaño de los archivos del modelo."""
    print("=" * 70)
    print("📊 ANÁLISIS DE TAMAÑO DEL DEPLOYMENT - MODELO DE CHURN")
    print("=" * 70)
    print()
    
    # Rutas de archivos del modelo
    model_files = {
        'Modelo Random Forest': 'models/churn_model.pkl',
        'Preprocessor': 'models/preprocessor.pkl',
        'Metadata': 'models/metadata.json'
    }
    
    total_model_size = 0
    
    print("1️⃣  ARCHIVOS DEL MODELO:")
    print("-" * 70)
    
    for name, path in model_files.items():
        size_mb = get_size_mb(path)
        total_model_size += size_mb
        
        if size_mb > 0:
            status = "✅" if size_mb < 100 else "⚠️"
            print(f"{status} {name:25} {size_mb:>10.2f} MB  ({path})")
        else:
            print(f"❌ {name:25} {'NO ENCONTRADO':>10}  ({path})")
    
    print("-" * 70)
    print(f"   {'TOTAL MODELO:':25} {total_model_size:>10.2f} MB")
    print()
    
    # Verificar dataset
    print("2️⃣  DATASET:")
    print("-" * 70)
    dataset_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
    dataset_size = get_size_mb(dataset_path)
    
    if dataset_size > 0:
        print(f"✅ {'Dataset CSV:':25} {dataset_size:>10.2f} MB  ({dataset_path})")
    else:
        print(f"❌ {'Dataset CSV:':25} {'NO ENCONTRADO':>10}  ({dataset_path})")
    print()
    
    # Estimar tamaño de dependencias
    print("3️⃣  ESTIMACIÓN DE DEPENDENCIAS (en contenedor Docker):")
    print("-" * 70)
    dependencies_estimate = {
        'Python 3.9 base image': 50,
        'scikit-learn': 80,
        'pandas': 40,
        'numpy': 30,
        'Flask': 5,
        'joblib': 2,
        'Otras dependencias': 10
    }
    
    total_dependencies = 0
    for dep, size in dependencies_estimate.items():
        total_dependencies += size
        print(f"   {dep:30} ~{size:>6} MB")
    
    print("-" * 70)
    print(f"   {'TOTAL DEPENDENCIAS:':30} ~{total_dependencies:>6} MB")
    print()
    
    # Código de la aplicación
    print("4️⃣  CÓDIGO DE LA APLICACIÓN:")
    print("-" * 70)
    
    code_dirs = ['deployment/api', 'dashboard']
    total_code_size = 0
    
    for code_dir in code_dirs:
        if os.path.exists(code_dir):
            size = get_directory_size_mb(code_dir)
            total_code_size += size
            print(f"✅ {code_dir:30} {size:>10.2f} MB")
        else:
            print(f"⚠️  {code_dir:30} {'NO CREADO AÚN':>10}")
    
    # Estimar código (típicamente muy pequeño)
    if total_code_size == 0:
        total_code_size = 0.5  # Estimación
        print(f"   {'Estimación de código:':30} ~{total_code_size:>9.2f} MB")
    
    print()
    
    # RESUMEN TOTAL
    print("=" * 70)
    print("📦 RESUMEN TOTAL DEL DEPLOYMENT:")
    print("=" * 70)
    
    total_deployment = total_model_size + total_dependencies + total_code_size
    
    print(f"   Modelo + Preprocessor:        {total_model_size:>10.2f} MB")
    print(f"   Dependencias Python:          {total_dependencies:>10.2f} MB (estimado)")
    print(f"   Código de aplicación:         {total_code_size:>10.2f} MB")
    print("-" * 70)
    print(f"   TOTAL ESTIMADO:               {total_deployment:>10.2f} MB")
    print("=" * 70)
    print()
    
    # EVALUACIÓN Y RECOMENDACIONES
    print("🎯 EVALUACIÓN:")
    print("-" * 70)
    
    if total_deployment < 500:
        print("✅ EXCELENTE: El deployment cabe perfectamente en Render Free (512 MB RAM)")
        print("✅ El modelo puede almacenarse en Git (< 100 MB por archivo)")
    elif total_deployment < 1000:
        print("⚠️  ACEPTABLE: El deployment cabe en Render Free, pero está cerca del límite")
        print("💡 Considera optimizar el modelo si es posible")
    else:
        print("❌ PROBLEMA: El deployment excede el límite de Render Free (512 MB RAM)")
        print("💡 SOLUCIONES:")
        print("   - Usar Render Starter Plan ($7/mes) con 512 MB RAM")
        print("   - Optimizar el modelo (reducir n_estimators, max_depth)")
        print("   - Usar Railway (hasta 8 GB RAM en plan gratuito)")
    
    print()
    
    if total_model_size > 100:
        print("⚠️  ADVERTENCIA: Modelo > 100 MB")
        print("💡 No puedes almacenar el modelo directamente en GitHub")
        print("   SOLUCIONES:")
        print("   - Usar Git LFS (Large File Storage)")
        print("   - Almacenar en Google Cloud Storage / AWS S3")
        print("   - Descargar modelo durante el build en Render")
    
    print()
    print("=" * 70)
    
    return {
        'model_size_mb': total_model_size,
        'dependencies_mb': total_dependencies,
        'code_size_mb': total_code_size,
        'total_mb': total_deployment
    }


if __name__ == '__main__':
    results = check_model_files()

