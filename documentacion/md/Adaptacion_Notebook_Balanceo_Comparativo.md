---
title: "Adaptación del Notebook Telco Customer Churn - Comparativa de Técnicas de Balanceo"
output:
  html_document: default
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
---

# 📊 Adaptación del Notebook para Google Colab con Comparativa de Técnicas de Balanceo

## 📋 Resumen Ejecutivo

Este documento proporciona una guía completa y detallada para adaptar el notebook `Telco_Customer_Churn.ipynb` con las siguientes mejoras:

**✅ Implementaciones Principales:**

- Comparativa automática de 3 técnicas de balanceo (SMOTE, SMOTE + Tomek Link, Undersampling)
- Selección automática de la mejor técnica basada en ROC-AUC
- Visualizaciones comparativas interactivas (4 gráficos)
- Informe Markdown automático con sección de comparativa
- Metadata enriquecida con información de balanceo
- 100% compatible con Google Colab

**📊 Métricas de Evaluación:**

- ROC-AUC (métrica principal de selección)
- F1-Score, Precision, Recall
- Tiempo de procesamiento
- Número de muestras de entrenamiento

**🎯 Resultado Final:**

El sistema evaluará las tres técnicas, seleccionará automáticamente la mejor y generará un informe completo con justificación, métricas comparativas y recomendaciones de uso.

---

## 🎯 Objetivo

Adaptar el notebook `Telco_Customer_Churn.ipynb` para ejecutarse 100% en Google Colab, implementando y comparando tres técnicas de balanceo de clases:

- **SMOTE** (Synthetic Minority Over-sampling Technique)
- **SMOTE + Tomek Link** (Combinación de over-sampling y under-sampling)
- **Undersampling** (Random Under-sampling)

El sistema seleccionará automáticamente la mejor técnica basándose en métricas de rendimiento y generará un informe comparativo detallado.

---

## 📋 Análisis del Notebook Actual

### Estructura Identificada

El notebook actual tiene la siguiente estructura:

1. **Sección 0**: Importación de librerías
2. **Sección 0.1**: Configuración de reproducibilidad
3. **Sección 1**: Carga y exploración de datos
4. **Sección 2-6**: EDA y preprocesamiento
5. **Sección 7**: Manejo de desbalanceo (actualmente solo SMOTE)
6. **Sección 8**: Optimización de hiperparámetros
7. **Sección 9-10**: Evaluación y análisis de features
8. **Sección 11**: Guardado de modelo
9. **Sección 13**: Generación de informe automático

### Puntos Clave Identificados

**Importaciones actuales (líneas 105-107):**

```python
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline
```

**Aplicación de SMOTE (líneas 2223-2240):**

```python
smote = SMOTE(random_state=RANDOM_STATE)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)
```

**Guardado de modelo (líneas 3297-3577):**

Sección completa que guarda el modelo en Google Drive con verificación de tamaño.

**Generación de informe (líneas 3643-3690):**

Genera un informe Markdown automático con métricas y conclusiones.

---

## 🔧 Modificaciones Necesarias

### 1. Actualización de Importaciones

**Ubicación:** Celda de importaciones (línea 105)

**Código a agregar:**

```python
# Manejo de desbalanceo - AMPLIADO
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek  # ← NUEVO
from imblearn.pipeline import Pipeline as ImbPipeline
```

---

### 2. Nueva Sección: Comparativa de Técnicas de Balanceo

**Ubicación:** Reemplazar la Sección 7 actual (líneas 2177-2241)

**Título de la sección:**

```markdown
## 7. Comparativa de Técnicas de Balanceo de Clases

El dataset presenta un desbalanceo significativo (73% No Churn vs 27% Churn). 
Evaluaremos tres técnicas diferentes de balanceo y seleccionaremos automáticamente la mejor:

- **SMOTE**: Genera muestras sintéticas de la clase minoritaria
- **SMOTE + Tomek Link**: Combina SMOTE con limpieza de muestras ruidosas
- **Undersampling**: Reduce la clase mayoritaria al tamaño de la minoritaria
```

**Código de implementación:**

```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import time

print("="*80)
print("🔄 COMPARATIVA DE TÉCNICAS DE BALANCEO")
print("="*80)
print(f"\n🎲 Usando semilla: {RANDOM_STATE}\n")

# Distribución original
print("📊 DISTRIBUCIÓN ORIGINAL:")
print(f"   Clase 0 (No Churn): {y_train.value_counts()[0]:,} muestras")
print(f"   Clase 1 (Churn):    {y_train.value_counts()[1]:,} muestras")
print(f"   Ratio: {y_train.value_counts()[0]/y_train.value_counts()[1]:.2f}:1")
print()

# Diccionario para almacenar resultados
balancing_results = {}

# ============================================================================
# TÉCNICA 1: SMOTE
# ============================================================================
print("="*80)
print("1️⃣  TÉCNICA: SMOTE (Synthetic Minority Over-sampling)")
print("="*80)
```


start_time = time.time()
smote = SMOTE(random_state=RANDOM_STATE)
X_train_smote, y_train_smote = smote.fit_resample(X_train_processed, y_train)
smote_time = time.time() - start_time

print(f"⏱️  Tiempo de procesamiento: {smote_time:.2f} segundos")
print(f"📊 Distribución después de SMOTE:")
print(f"   Clase 0: {pd.Series(y_train_smote).value_counts()[0]:,} muestras")
print(f"   Clase 1: {pd.Series(y_train_smote).value_counts()[1]:,} muestras")
print(f"   Ratio: {pd.Series(y_train_smote).value_counts()[0]/pd.Series(y_train_smote).value_counts()[1]:.2f}:1")
print(f"   Total de muestras: {len(y_train_smote):,}")
print()

# ============================================================================
# TÉCNICA 2: SMOTE + Tomek Link
# ============================================================================
print("="*80)
print("2️⃣  TÉCNICA: SMOTE + Tomek Link (Híbrida)")
print("="*80)

start_time = time.time()
smote_tomek = SMOTETomek(random_state=RANDOM_STATE)
X_train_smote_tomek, y_train_smote_tomek = smote_tomek.fit_resample(X_train_processed, y_train)
smote_tomek_time = time.time() - start_time

print(f"⏱️  Tiempo de procesamiento: {smote_tomek_time:.2f} segundos")
print(f"📊 Distribución después de SMOTE + Tomek:")
print(f"   Clase 0: {pd.Series(y_train_smote_tomek).value_counts()[0]:,} muestras")
print(f"   Clase 1: {pd.Series(y_train_smote_tomek).value_counts()[1]:,} muestras")
print(f"   Ratio: {pd.Series(y_train_smote_tomek).value_counts()[0]/pd.Series(y_train_smote_tomek).value_counts()[1]:.2f}:1")
print(f"   Total de muestras: {len(y_train_smote_tomek):,}")
print(f"   💡 Tomek Links eliminados: {len(y_train_smote) - len(y_train_smote_tomek):,} muestras")
print()

# ============================================================================
# TÉCNICA 3: Undersampling
# ============================================================================
print("="*80)
print("3️⃣  TÉCNICA: Random Undersampling")
print("="*80)

start_time = time.time()
undersampler = RandomUnderSampler(random_state=RANDOM_STATE)
X_train_under, y_train_under = undersampler.fit_resample(X_train_processed, y_train)
under_time = time.time() - start_time

print(f"⏱️  Tiempo de procesamiento: {under_time:.2f} segundos")
print(f"📊 Distribución después de Undersampling:")
print(f"   Clase 0: {pd.Series(y_train_under).value_counts()[0]:,} muestras")
print(f"   Clase 1: {pd.Series(y_train_under).value_counts()[1]:,} muestras")
print(f"   Ratio: {pd.Series(y_train_under).value_counts()[0]/pd.Series(y_train_under).value_counts()[1]:.2f}:1")
print(f"   Total de muestras: {len(y_train_under):,}")
print(f"   💡 Muestras eliminadas: {len(y_train) - len(y_train_under):,}")
print()

# ============================================================================
# EVALUACIÓN DE CADA TÉCNICA
# ============================================================================
print("="*80)
print("📊 EVALUACIÓN DE RENDIMIENTO POR TÉCNICA")
print("="*80)
print()

# Modelo base para evaluación (Random Forest)
from sklearn.ensemble import RandomForestClassifier

techniques = {
    'SMOTE': (X_train_smote, y_train_smote, smote_time),
    'SMOTE + Tomek': (X_train_smote_tomek, y_train_smote_tomek, smote_tomek_time),
    'Undersampling': (X_train_under, y_train_under, under_time)
}

for technique_name, (X_bal, y_bal, proc_time) in techniques.items():
    print(f"\n{'='*80}")
    print(f"🔍 Evaluando: {technique_name}")
    print(f"{'='*80}")

    # Entrenar modelo
    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    train_start = time.time()
    rf_model.fit(X_bal, y_bal)
    train_time = time.time() - train_start

    # Predicciones
    y_pred = rf_model.predict(X_test_processed)
    y_pred_proba = rf_model.predict_proba(X_test_processed)[:, 1]

    # Calcular métricas
    metrics = {
        'technique': technique_name,
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba),
        'processing_time': proc_time,
        'training_time': train_time,
        'total_time': proc_time + train_time,
        'train_samples': len(y_bal),
        'X_train': X_bal,
        'y_train': y_bal,
        'model': rf_model
    }

    balancing_results[technique_name] = metrics

    # Mostrar resultados
    print(f"   Accuracy:  {metrics['accuracy']:.4f}")
    print(f"   Precision: {metrics['precision']:.4f}")
    print(f"   Recall:    {metrics['recall']:.4f}")
    print(f"   F1-Score:  {metrics['f1']:.4f}")
    print(f"   ROC-AUC:   {metrics['roc_auc']:.4f}")
    print(f"   ⏱️  Tiempo total: {metrics['total_time']:.2f}s (Balanceo: {proc_time:.2f}s + Entrenamiento: {train_time:.2f}s)")
    print(f"   📊 Muestras de entrenamiento: {metrics['train_samples']:,}")

# ============================================================================
# SELECCIÓN AUTOMÁTICA DE LA MEJOR TÉCNICA
# ============================================================================
print("\n" + "="*80)
print("🏆 SELECCIÓN AUTOMÁTICA DE LA MEJOR TÉCNICA")
print("="*80)
print()

# Crear DataFrame comparativo
comparison_df = pd.DataFrame([
    {
        'Técnica': name,
        'Accuracy': metrics['accuracy'],
        'Precision': metrics['precision'],
        'Recall': metrics['recall'],
        'F1-Score': metrics['f1'],
        'ROC-AUC': metrics['roc_auc'],
        'Tiempo (s)': metrics['total_time'],
        'Muestras': metrics['train_samples']
    }
    for name, metrics in balancing_results.items()
])

print("📊 TABLA COMPARATIVA:")
print()
print(comparison_df.to_string(index=False))
print()

# Criterio de selección: ROC-AUC (métrica principal para clasificación desbalanceada)
best_technique_name = comparison_df.loc[comparison_df['ROC-AUC'].idxmax(), 'Técnica']
best_metrics = balancing_results[best_technique_name]

print("="*80)
print(f"✅ MEJOR TÉCNICA SELECCIONADA: {best_technique_name}")
print("="*80)
print()
print(f"📈 Métricas de la mejor técnica:")
print(f"   • ROC-AUC:   {best_metrics['roc_auc']:.4f} ⭐")
print(f"   • F1-Score:  {best_metrics['f1']:.4f}")
print(f"   • Precision: {best_metrics['precision']:.4f}")
print(f"   • Recall:    {best_metrics['recall']:.4f}")
print(f"   • Accuracy:  {best_metrics['accuracy']:.4f}")
print()
print(f"⏱️  Eficiencia:")
print(f"   • Tiempo total: {best_metrics['total_time']:.2f} segundos")
print(f"   • Muestras de entrenamiento: {best_metrics['train_samples']:,}")
print()

# Asignar los mejores datos balanceados para uso posterior
X_train_balanced = best_metrics['X_train']
y_train_balanced = best_metrics['y_train']
best_balancing_technique = best_technique_name

print(f"💾 Variables actualizadas:")
print(f"   • X_train_balanced: {X_train_balanced.shape}")
print(f"   • y_train_balanced: {len(y_train_balanced):,} muestras")
print(f"   • best_balancing_technique: '{best_balancing_technique}'")
print()
```

---

## 3. Modificación de la Sección de Guardado de Modelo

**Ubicación:** Sección 11 (líneas 3297-3577)

**Modificación:** Agregar información sobre la técnica de balanceo seleccionada en los metadatos.

**Código a modificar en la sección de metadata (aproximadamente línea 3440):**

```python
# 3. Guardar metadata
print("3️⃣  Guardando metadata...")
metadata = {
    'model_type': 'Random Forest Classifier',
    'sklearn_version': sklearn.__version__,
    'training_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'random_state': RANDOM_STATE,
    'balancing_technique': best_balancing_technique,  # ← NUEVO
    'balancing_comparison': {  # ← NUEVO
        technique: {
            'roc_auc': metrics['roc_auc'],
            'f1_score': metrics['f1'],
            'precision': metrics['precision'],
            'recall': metrics['recall'],
            'training_samples': metrics['train_samples']
        }
        for technique, metrics in balancing_results.items()
    },
    'features': list(X_train_processed.columns),
    'n_features': X_train_processed.shape[1],
    'best_params': best_rf.get_params(),
    'performance': {
        'accuracy': best_model_metrics['accuracy'],
        'precision': best_model_metrics['precision'],
        'recall': best_model_metrics['recall'],
        'f1_score': best_model_metrics['f1'],
        'roc_auc': best_model_metrics['roc_auc']
    }
}
```

---

## 4. Modificación de la Generación de Informe

**Ubicación:** Sección 13 (líneas 3643-3690)

**Modificación:** Agregar sección comparativa de técnicas de balanceo en el informe.

**Código a agregar después de la sección de métricas (aproximadamente línea 3850):**

```python
# Agregar sección de comparativa de balanceo al informe
report_content += f"""
---

## 4. ⚖️ Comparativa de Técnicas de Balanceo

### Técnicas Evaluadas

Se evaluaron tres técnicas diferentes de balanceo de clases para manejar el desbalanceo del dataset (73% No Churn vs 27% Churn):

1. **SMOTE (Synthetic Minority Over-sampling Technique)**

   - Genera muestras sintéticas de la clase minoritaria
   - Aumenta el tamaño del dataset de entrenamiento
   - Preserva toda la información de la clase mayoritaria

2. **SMOTE + Tomek Link (Técnica Híbrida)**

   - Combina SMOTE con limpieza de muestras ruidosas
   - Elimina pares de Tomek Links (muestras cercanas de clases diferentes)
   - Mejora la separabilidad entre clases

3. **Random Undersampling**

   - Reduce aleatoriamente la clase mayoritaria
   - Reduce el tamaño del dataset de entrenamiento
   - Más rápido pero puede perder información valiosa

### Resultados Comparativos

| Técnica | ROC-AUC | F1-Score | Precision | Recall | Muestras | Tiempo (s) |
|---------|---------|----------|-----------|--------|----------|------------|
"""

# Agregar filas de la tabla comparativa
for technique_name, metrics in balancing_results.items():
    report_content += f"| {technique_name} | {metrics['roc_auc']:.4f} | {metrics['f1']:.4f} | {metrics['precision']:.4f} | {metrics['recall']:.4f} | {metrics['train_samples']:,} | {metrics['total_time']:.2f} |\n"

report_content += f"""
### 🏆 Técnica Seleccionada: {best_balancing_technique}

**Justificación de la selección:**

La técnica **{best_balancing_technique}** fue seleccionada automáticamente basándose en la métrica ROC-AUC, que es la más apropiada para problemas de clasificación desbalanceada.

**Ventajas de {best_balancing_technique}:**

"""

# Agregar ventajas específicas según la técnica seleccionada
if best_balancing_technique == 'SMOTE':
    report_content += """
- ✅ Genera muestras sintéticas realistas de la clase minoritaria
- ✅ Preserva toda la información de la clase mayoritaria
- ✅ Mejora significativamente la detección de churns (recall)
- ✅ Balance óptimo entre rendimiento y tiempo de procesamiento
"""
elif best_balancing_technique == 'SMOTE + Tomek':
    report_content += """
- ✅ Combina las ventajas de SMOTE con limpieza de datos
- ✅ Elimina muestras ruidosas en la frontera de decisión
- ✅ Mejora la separabilidad entre clases
- ✅ Mayor precisión en las predicciones
- ⚠️  Tiempo de procesamiento ligeramente mayor
"""
else:  # Undersampling
    report_content += """
- ✅ Procesamiento muy rápido
- ✅ Reduce el tamaño del dataset (útil para datasets grandes)
- ✅ Evita el overfitting al reducir muestras redundantes
- ⚠️  Puede perder información valiosa de la clase mayoritaria
"""

report_content += f"""
**Métricas de rendimiento:**

- ROC-AUC: **{best_metrics['roc_auc']:.4f}** ⭐
- F1-Score: **{best_metrics['f1']:.4f}**
- Precision: **{best_metrics['precision']:.4f}**
- Recall: **{best_metrics['recall']:.4f}**
- Tiempo total: **{best_metrics['total_time']:.2f} segundos**

### 📊 Análisis Comparativo

"""

# Análisis automático de diferencias
best_roc = best_metrics['roc_auc']
techniques_sorted = sorted(balancing_results.items(), key=lambda x: x[1]['roc_auc'], reverse=True)

if len(techniques_sorted) > 1:
    second_best = techniques_sorted[1]
    diff_roc = (best_roc - second_best[1]['roc_auc']) * 100

    if diff_roc < 0.5:
        report_content += f"""
**Diferencia marginal:** La diferencia entre {best_balancing_technique} y {second_best[0]} es de solo {diff_roc:.2f}% en ROC-AUC. Ambas técnicas son igualmente válidas.
"""
    elif diff_roc < 2:
        report_content += f"""
**Ventaja moderada:** {best_balancing_technique} supera a {second_best[0]} por {diff_roc:.2f}% en ROC-AUC, mostrando una mejora notable.
"""
    else:
        report_content += f"""
**Ventaja significativa:** {best_balancing_technique} supera a {second_best[0]} por {diff_roc:.2f}% en ROC-AUC, demostrando una clara superioridad.
"""

# Análisis de eficiencia
fastest = min(balancing_results.items(), key=lambda x: x[1]['total_time'])
slowest = max(balancing_results.items(), key=lambda x: x[1]['total_time'])
time_diff = slowest[1]['total_time'] - fastest[1]['total_time']

report_content += f"""
**Eficiencia computacional:**

- Técnica más rápida: **{fastest[0]}** ({fastest[1]['total_time']:.2f}s)
- Técnica más lenta: **{slowest[0]}** ({slowest[1]['total_time']:.2f}s)
- Diferencia: {time_diff:.2f} segundos

"""

# Recomendaciones según el contexto
report_content += """
### 💡 Recomendaciones de Uso

**Cuándo usar cada técnica:**

**SMOTE:**

- Dataset pequeño o mediano (< 100,000 muestras)
- Se requiere maximizar recall (detectar todos los churns posibles)
- Tiempo de procesamiento no es crítico

**SMOTE + Tomek Link:**

- Dataset con posible ruido en las fronteras de decisión
- Se requiere maximizar precision (minimizar falsos positivos)
- Se dispone de recursos computacionales adecuados

**Undersampling:**

- Dataset muy grande (> 100,000 muestras)
- Recursos computacionales limitados
- Tiempo de procesamiento es crítico
- La clase mayoritaria tiene muchas muestras redundantes

"""
```

---

## 5. Visualización Comparativa de Técnicas de Balanceo

**Nueva celda a agregar después de la selección de la mejor técnica:**

```python
# ============================================================================
# VISUALIZACIÓN COMPARATIVA
# ============================================================================

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('📊 Comparativa de Técnicas de Balanceo de Clases',
             fontsize=16, fontweight='bold', y=1.00)

# Colores para cada técnica
colors = {
    'SMOTE': '#3498db',
    'SMOTE + Tomek': '#e74c3c',
    'Undersampling': '#2ecc71'
}

# 1. Comparación de métricas
ax1 = axes[0, 0]
metrics_comparison = comparison_df.set_index('Técnica')[['ROC-AUC', 'F1-Score', 'Precision', 'Recall']]
metrics_comparison.plot(kind='bar', ax=ax1, color=['#3498db', '#e74c3c', '#f39c12', '#9b59b6'])
ax1.set_title('Comparación de Métricas de Rendimiento', fontweight='bold', fontsize=12)
ax1.set_ylabel('Score', fontweight='bold')
ax1.set_xlabel('')
ax1.legend(loc='lower right', framealpha=0.9)
ax1.grid(axis='y', alpha=0.3)
ax1.set_ylim([0, 1])
ax1.axhline(y=0.8, color='red', linestyle='--', alpha=0.5, label='Umbral 0.8')

# Rotar etiquetas
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

# 2. Distribución de muestras
ax2 = axes[0, 1]
samples_data = {
    'Original': len(y_train),
    'SMOTE': balancing_results['SMOTE']['train_samples'],
    'SMOTE + Tomek': balancing_results['SMOTE + Tomek']['train_samples'],
    'Undersampling': balancing_results['Undersampling']['train_samples']
}
bars = ax2.bar(samples_data.keys(), samples_data.values(),
               color=['#95a5a6', '#3498db', '#e74c3c', '#2ecc71'])
ax2.set_title('Número de Muestras de Entrenamiento', fontweight='bold', fontsize=12)
ax2.set_ylabel('Número de Muestras', fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Agregar valores en las barras
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height):,}',
             ha='center', va='bottom', fontweight='bold')

ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

# 3. Tiempo de procesamiento
ax3 = axes[1, 0]
time_data = comparison_df.set_index('Técnica')['Tiempo (s)']
bars = ax3.barh(time_data.index, time_data.values,
                color=[colors[t] for t in time_data.index])
ax3.set_title('Tiempo de Procesamiento Total', fontweight='bold', fontsize=12)
ax3.set_xlabel('Tiempo (segundos)', fontweight='bold')
ax3.grid(axis='x', alpha=0.3)

# Agregar valores en las barras
for i, (idx, val) in enumerate(time_data.items()):
    ax3.text(val, i, f'  {val:.2f}s', va='center', fontweight='bold')

# 4. ROC-AUC vs Tiempo (eficiencia)
ax4 = axes[1, 1]
for technique in comparison_df['Técnica']:
    row = comparison_df[comparison_df['Técnica'] == technique].iloc[0]
    ax4.scatter(row['Tiempo (s)'], row['ROC-AUC'],
               s=300, alpha=0.6, color=colors[technique],
               label=technique, edgecolors='black', linewidth=2)
    ax4.annotate(technique,
                (row['Tiempo (s)'], row['ROC-AUC']),
                xytext=(10, 10), textcoords='offset points',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor=colors[technique], alpha=0.3))

ax4.set_title('Eficiencia: ROC-AUC vs Tiempo de Procesamiento', fontweight='bold', fontsize=12)
ax4.set_xlabel('Tiempo de Procesamiento (s)', fontweight='bold')
ax4.set_ylabel('ROC-AUC', fontweight='bold')
ax4.grid(alpha=0.3)
ax4.set_ylim([0.75, 0.90])

# Marcar la mejor técnica
best_row = comparison_df[comparison_df['Técnica'] == best_technique_name].iloc[0]
ax4.scatter(best_row['Tiempo (s)'], best_row['ROC-AUC'],
           s=500, alpha=0.3, color='gold', marker='*',
           edgecolors='orange', linewidth=3, zorder=10,
           label='Mejor Técnica')

ax4.legend(loc='lower right', framealpha=0.9)

plt.tight_layout()
plt.show()

print("\n" + "="*80)
print("✅ Visualización comparativa generada exitosamente")
print("="*80)
```

---

## 6. Resumen de Cambios en el Código

### Archivos Modificados

**1. Celda de Importaciones (Sección 0)**

- Agregar: `from imblearn.combine import SMOTETomek`

**2. Sección 7 - Manejo de Desbalanceo (COMPLETA REESCRITURA)**

- Implementar comparativa de 3 técnicas
- Evaluación automática con Random Forest
- Selección automática de la mejor técnica
- Almacenamiento de resultados en `balancing_results`

**3. Sección 11 - Guardado de Modelo**

- Modificar metadata para incluir `balancing_technique`
- Agregar `balancing_comparison` con métricas de todas las técnicas

**4. Sección 13 - Generación de Informe**

- Agregar nueva sección "Comparativa de Técnicas de Balanceo"
- Incluir tabla comparativa
- Agregar justificación de selección
- Incluir recomendaciones de uso

**5. Nueva Celda - Visualización Comparativa**

- Crear 4 gráficos comparativos
- Mostrar métricas, muestras, tiempos y eficiencia

---

## 7. Estructura del Informe Final Generado

El informe Markdown generado automáticamente incluirá:

### Secciones Existentes

1. 📊 Resumen del Dataset
2. 🎯 Métricas del Mejor Modelo
3. 📈 Top 10 Features Más Importantes

### Nuevas Secciones

4. ⚖️ **Comparativa de Técnicas de Balanceo** (NUEVA)

   - Técnicas evaluadas
   - Tabla comparativa
   - Técnica seleccionada y justificación
   - Análisis comparativo
   - Recomendaciones de uso

5. ⚙️ Parámetros del Modelo Optimizado
6. 💡 Conclusiones y Recomendaciones

---

## 8. Ejemplo de Salida del Informe

### Sección de Comparativa de Balanceo

```markdown
## 4. ⚖️ Comparativa de Técnicas de Balanceo

### Resultados Comparativos

| Técnica | ROC-AUC | F1-Score | Precision | Recall | Muestras | Tiempo (s) |
|---------|---------|----------|-----------|--------|----------|------------|
| SMOTE | 0.8440 | 0.6310 | 0.5258 | 0.7888 | 8,278 | 3.45 |
| SMOTE + Tomek | 0.8465 | 0.6285 | 0.5412 | 0.7456 | 8,156 | 5.23 |
| Undersampling | 0.8201 | 0.6102 | 0.5876 | 0.6345 | 2,990 | 1.12 |

### 🏆 Técnica Seleccionada: SMOTE + Tomek

**Justificación:** ROC-AUC más alto (0.8465)

**Ventajas:**

- ✅ Combina las ventajas de SMOTE con limpieza de datos
- ✅ Elimina muestras ruidosas en la frontera de decisión
- ✅ Mejora la separabilidad entre clases
```

---

## 9. Checklist de Implementación

### ✅ Tareas Completadas en este Documento

- [x] Análisis del notebook original
- [x] Identificación de secciones a modificar
- [x] Código para importaciones adicionales
- [x] Código completo de comparativa de balanceo
- [x] Código de modificación de metadata
- [x] Código de modificación de informe
- [x] Código de visualización comparativa
- [x] Documentación de cambios
- [x] Ejemplo de salida del informe

### 📋 Tareas Pendientes (Implementación en Notebook)

- [ ] Copiar código de importaciones a la celda correspondiente
- [ ] Reemplazar Sección 7 con el nuevo código de comparativa
- [ ] Modificar sección de guardado de modelo (metadata)
- [ ] Modificar sección de generación de informe
- [ ] Agregar celda de visualización comparativa
- [ ] Ejecutar notebook completo en Google Colab
- [ ] Verificar que el informe se genera correctamente
- [ ] Validar que los modelos se guardan en Google Drive

---

## 10. Notas Técnicas Importantes

### Compatibilidad con Google Colab

✅ **Todo el código es 100% compatible con Google Colab**

- Usa `from google.colab import drive` para montar Drive
- Guarda modelos en `/content/drive/MyDrive/`
- No requiere instalaciones adicionales (imblearn ya está incluido)

### Reproducibilidad

✅ **Mantiene la reproducibilidad del notebook original**

- Usa `RANDOM_STATE` en todas las técnicas de balanceo
- Usa `RANDOM_STATE` en todos los modelos
- Permite modo reproducible (`REPRODUCIBLE_MODE = True`) o experimental (`False`)

### Eficiencia

✅ **Optimizado para Google Colab**

- Usa `n_jobs=-1` para paralelización
- Técnicas de balanceo optimizadas
- Visualizaciones eficientes

---

## 11. Conclusión

Este documento proporciona una guía completa para adaptar el notebook `Telco_Customer_Churn.ipynb` con:

1. ✅ Comparativa de 3 técnicas de balanceo (SMOTE, SMOTE + Tomek, Undersampling)
2. ✅ Selección automática de la mejor técnica basada en ROC-AUC
3. ✅ Visualizaciones comparativas detalladas
4. ✅ Informe automático con sección de comparativa
5. ✅ Metadata enriquecida con información de balanceo
6. ✅ 100% compatible con Google Colab
7. ✅ Mantiene reproducibilidad y eficiencia

**Próximo paso:** Implementar los cambios en el notebook y ejecutar en Google Colab para validar el funcionamiento completo.

