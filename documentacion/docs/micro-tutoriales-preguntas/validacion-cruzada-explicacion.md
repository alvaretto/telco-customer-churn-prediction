---
title: "Validación Cruzada (Cross-Validation): Explicación Completa"
author: "Bootcamp VirtIA - Tutorial Detallado"
date: "`r Sys.Date()`"
output:
  html_document: default
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
    toc: true
    toc_depth: 3
---

# 🎯 ¿Qué es la Validación Cruzada?

## 📚 Definición Simple

La **validación cruzada** (cross-validation) es una técnica para **evaluar qué tan bien generaliza un modelo** a datos nuevos que nunca ha visto.

**Problema que resuelve:** Si solo divides tus datos en train/test una vez, tu evaluación puede depender de la "suerte" de cómo se dividieron los datos.

**Solución:** Divide los datos de múltiples formas diferentes y promedia los resultados.

---

## 🔄 Validación Tradicional vs Validación Cruzada

### ❌ Problema con Train/Test Simple

```
Dataset completo (100%)
│
├─ Train (80%) ──► Entrenar modelo
└─ Test (20%)  ──► Evaluar modelo ──► ROC-AUC = 0.85
```

**Problema:** ¿Y si el 20% de test era "fácil" o "difícil" por casualidad?

### ✅ Solución: Validación Cruzada con K-Folds

```
Dataset completo (100%)
│
Dividir en K=5 partes iguales (folds)
│
├─ Fold 1 (20%)
├─ Fold 2 (20%)
├─ Fold 3 (20%)
├─ Fold 4 (20%)
└─ Fold 5 (20%)
```

**Proceso:** Entrenar K veces, cada vez usando un fold diferente para validar.

---

## 🎲 Ejemplo Práctico: K-Fold con K=5

Imagina que tienes **1,000 clientes** y quieres validar tu modelo con **5 folds**.

### Paso 1: Dividir en 5 Folds

```
Fold 1: Clientes   1 - 200   (20%)
Fold 2: Clientes 201 - 400   (20%)
Fold 3: Clientes 401 - 600   (20%)
Fold 4: Clientes 601 - 800   (20%)
Fold 5: Clientes 801 - 1000  (20%)
```

### Paso 2: Entrenar y Validar 5 Veces

#### **Iteración 1:**
```
Train: Folds 2, 3, 4, 5 (800 clientes) ──► Entrenar modelo
Test:  Fold 1           (200 clientes) ──► ROC-AUC = 0.87
```

#### **Iteración 2:**
```
Train: Folds 1, 3, 4, 5 (800 clientes) ──► Entrenar modelo
Test:  Fold 2           (200 clientes) ──► ROC-AUC = 0.85
```

#### **Iteración 3:**
```
Train: Folds 1, 2, 4, 5 (800 clientes) ──► Entrenar modelo
Test:  Fold 3           (200 clientes) ──► ROC-AUC = 0.89
```

#### **Iteración 4:**
```
Train: Folds 1, 2, 3, 5 (800 clientes) ──► Entrenar modelo
Test:  Fold 4           (200 clientes) ──► ROC-AUC = 0.84
```

#### **Iteración 5:**
```
Train: Folds 1, 2, 3, 4 (800 clientes) ──► Entrenar modelo
Test:  Fold 5           (200 clientes) ──► ROC-AUC = 0.88
```

### Paso 3: Calcular Promedio

```
ROC-AUC promedio = (0.87 + 0.85 + 0.89 + 0.84 + 0.88) / 5 = 0.866
Desviación estándar = 0.019
```

**Resultado:** El modelo tiene un ROC-AUC de **0.866 ± 0.019**

---

## 📊 Visualización del Proceso

### Diagrama de K-Fold (K=5)

```
┌─────────────────────────────────────────────────────────────┐
│                    DATASET COMPLETO                         │
│                    (1000 clientes)                          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │   Dividir en 5 folds iguales          │
        └───────────────────────────────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
        ▼                                       ▼
┌───────────────┐                       ┌───────────────┐
│  Fold 1 (20%) │                       │  Fold 5 (20%) │
│  Fold 2 (20%) │                       │               │
│  Fold 3 (20%) │   ...                 │               │
│  Fold 4 (20%) │                       │               │
└───────────────┘                       └───────────────┘

ITERACIÓN 1:
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ FOLD 1  │ FOLD 2  │ FOLD 3  │ FOLD 4  │ FOLD 5  │
│  TEST   │  TRAIN  │  TRAIN  │  TRAIN  │  TRAIN  │
│  🔴     │  🟢     │  🟢     │  🟢     │  🟢     │
└─────────┴─────────┴─────────┴─────────┴─────────┘
           ROC-AUC = 0.87

ITERACIÓN 2:
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ FOLD 1  │ FOLD 2  │ FOLD 3  │ FOLD 4  │ FOLD 5  │
│  TRAIN  │  TEST   │  TRAIN  │  TRAIN  │  TRAIN  │


#### 2. Validación Cruzada Explícita del Mejor Modelo

```python
from sklearn.model_selection import cross_val_score

# Validación cruzada estratificada con 5 folds
cv_scores = cross_val_score(
    best_rf,                    # Mejor modelo encontrado
    X_train_balanced,           # Datos de entrenamiento
    y_train_balanced,           # Etiquetas
    cv=5,                       # 5 folds
    scoring='roc_auc'           # Métrica
)

print(f"Scores de validación cruzada: {cv_scores}")
print(f"Media: {cv_scores.mean():.4f}")
print(f"Desviación estándar: {cv_scores.std():.4f}")
```

**Salida típica:**
```
Scores de validación cruzada: [0.9312, 0.9401, 0.9356, 0.9289, 0.9398]
Media: 0.9351
Desviación estándar: 0.0046
```

**Interpretación:**
- El modelo tiene un rendimiento **consistente** (baja desviación estándar)
- ROC-AUC promedio de **0.9351** en validación cruzada
- No hay overfitting (los 5 scores son similares)

---

## 🔍 Tipos de Validación Cruzada

### 1. K-Fold (Estándar)

**Uso:** Datasets balanceados

```python
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
```

**Características:**
- Divide en K partes iguales
- Cada fold tiene aproximadamente el mismo tamaño
- **Problema:** Puede no preservar la proporción de clases

### 2. Stratified K-Fold (Estratificado) ⭐

**Uso:** Datasets desbalanceados (como churn: 73% vs 27%)

```python
from sklearn.model_selection import StratifiedKFold

skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

**Características:**
- Divide en K partes iguales
- **Preserva la proporción de clases** en cada fold
- Si tienes 73% No Churn y 27% Churn, cada fold tendrá esa misma proporción

**Ejemplo:**

```
Dataset original: 730 No Churn, 270 Churn (73% vs 27%)

Con K-Fold estándar (puede variar):
  Fold 1: 150 No Churn, 50 Churn  (75% vs 25%)
  Fold 2: 140 No Churn, 60 Churn  (70% vs 30%)
  Fold 3: 160 No Churn, 40 Churn  (80% vs 20%)  ❌ Desbalanceado
  ...

Con Stratified K-Fold (siempre igual):
  Fold 1: 146 No Churn, 54 Churn  (73% vs 27%)  ✅
  Fold 2: 146 No Churn, 54 Churn  (73% vs 27%)  ✅
  Fold 3: 146 No Churn, 54 Churn  (73% vs 27%)  ✅
  ...
```

### 3. Leave-One-Out (LOO)

**Uso:** Datasets muy pequeños (<100 muestras)

```python
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()
```

**Características:**
- K = número de muestras (si tienes 100 muestras, K=100)
- Cada iteración usa 1 muestra para test y el resto para train
- **Muy costoso computacionalmente**

### 4. Time Series Split

**Uso:** Datos temporales (series de tiempo)

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)
```

**Características:**
- Respeta el orden temporal
- Siempre entrena con datos pasados y valida con datos futuros
- **No mezcla** datos futuros en el entrenamiento

---

## 💡 Ventajas de la Validación Cruzada

### ✅ Ventajas

1. **Evaluación más robusta**: No depende de una sola división aleatoria
2. **Usa todos los datos**: Cada muestra se usa para train y test
3. **Detecta overfitting**: Si hay mucha variación entre folds, hay overfitting
4. **Estima variabilidad**: Obtienes media ± desviación estándar
5. **Mejor para datasets pequeños**: Aprovecha mejor los datos limitados

### ❌ Desventajas

1. **Más costoso computacionalmente**: K veces más lento que train/test simple
2. **No reemplaza el test set final**: Aún necesitas un conjunto de test separado
3. **Puede ser lento con K grande**: K=10 es 10 veces más lento que K=1

---

## 🎲 Ejemplo Numérico Completo

### Escenario: Predicción de Churn con 5,000 Clientes

#### Paso 1: División Inicial

```
Dataset completo: 5,000 clientes
│
├─ Train: 4,000 clientes (80%)  ← Usamos validación cruzada aquí
└─ Test:  1,000 clientes (20%)  ← Guardamos para evaluación final
```

#### Paso 2: Validación Cruzada en Train (K=5)

```
Train set: 4,000 clientes
│
Dividir en 5 folds de 800 clientes cada uno
│
├─ Fold 1: 800 clientes
├─ Fold 2: 800 clientes
├─ Fold 3: 800 clientes
├─ Fold 4: 800 clientes
└─ Fold 5: 800 clientes
```

#### Paso 3: Entrenar 5 Veces

| Iteración | Train (3,200) | Validation (800) | ROC-AUC |
|-----------|---------------|------------------|---------|
| 1         | Folds 2,3,4,5 | Fold 1           | 0.9312  |
| 2         | Folds 1,3,4,5 | Fold 2           | 0.9401  |
| 3         | Folds 1,2,4,5 | Fold 3           | 0.9356  |
| 4         | Folds 1,2,3,5 | Fold 4           | 0.9289  |
| 5         | Folds 1,2,3,4 | Fold 5           | 0.9398  |

**Promedio:** 0.9351 ± 0.0046

#### Paso 4: Entrenar Modelo Final

```
Entrenar con TODOS los 4,000 clientes de train
Evaluar en los 1,000 clientes de test
ROC-AUC en test: 0.8274
```

**¿Por qué es diferente?**
- Validación cruzada: 0.9351 (en train con SMOTE)
- Test final: 0.8274 (en test sin SMOTE)

**Razón:** El test set tiene datos desbalanceados originales, mientras que la validación cruzada usó datos balanceados con SMOTE.

---

## 🔧 Código Práctico

### Ejemplo 1: Validación Cruzada Básica

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Crear modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Validación cruzada con 5 folds
scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,                    # 5 folds
    scoring='roc_auc'        # Métrica
)

print(f"Scores: {scores}")
print(f"Media: {scores.mean():.4f}")
print(f"Std: {scores.std():.4f}")
```

### Ejemplo 2: Validación Cruzada Estratificada

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Crear estrategia de validación cruzada
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Validación cruzada
scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=skfold,               # Usar estratificación
    scoring='roc_auc'
)

print(f"Scores estratificados: {scores}")
```

### Ejemplo 3: Validación Cruzada con Múltiples Métricas

```python
from sklearn.model_selection import cross_validate

# Validación cruzada con múltiples métricas
scoring = ['roc_auc', 'precision', 'recall', 'f1']

results = cross_validate(
    model,
    X_train,
    y_train,
    cv=5,
    scoring=scoring,
    return_train_score=True
)

print(f"ROC-AUC: {results['test_roc_auc'].mean():.4f}")
print(f"Precision: {results['test_precision'].mean():.4f}")
print(f"Recall: {results['test_recall'].mean():.4f}")
print(f"F1-Score: {results['test_f1'].mean():.4f}")
```

---

## 🚀 Resumen Ejecutivo

### ¿Qué es la Validación Cruzada? - Respuesta Corta

**Validación cruzada** es dividir tus datos de entrenamiento en K partes (folds), entrenar K veces usando cada parte como validación una vez, y promediar los resultados.

### ¿Por qué usarla?

1. **Evaluación más confiable** que un solo train/test split
2. **Detecta overfitting** (si hay mucha variación entre folds)
3. **Aprovecha mejor los datos** (especialmente con datasets pequeños)
4. **Estima la variabilidad** del modelo (media ± std)

### ¿Cuándo usarla?

- ✅ **Siempre** durante la optimización de hiperparámetros
- ✅ Para evaluar la **estabilidad** del modelo
- ✅ Con **datasets pequeños** (<10,000 muestras)
- ❌ **No reemplaza** el test set final

### Analogía Simple

Es como **probar un restaurante 5 veces en días diferentes** en lugar de solo una vez:

- **1 visita**: Puede ser un día bueno o malo por casualidad
- **5 visitas**: Obtienes una evaluación más confiable del restaurante
- **Promedio de las 5 visitas**: Calidad real del restaurante

En validación cruzada:

- Cada "visita" = un fold
- "Calidad del restaurante" = rendimiento del modelo
- "Promedio de visitas" = ROC-AUC promedio

¡Y listo! Ahora entiendes la validación cruzada. 🎉
... (continúa para las 5 iteraciones)

RESULTADO FINAL:
ROC-AUC promedio = 0.866 ± 0.019
```

---

## 🎯 En el Notebook de Churn

### Código del Notebook

En el notebook `Telco_Customer_Churn.ipynb`, la validación cruzada se usa en dos lugares:

#### 1. Durante la Optimización de Hiperparámetros

```python
random_search = RandomizedSearchCV(
    estimator=rf_base,
    param_distributions=param_distributions,
    n_iter=20,
    cv=3,              # ← VALIDACIÓN CRUZADA CON 3 FOLDS
    scoring='roc_auc',
    random_state=42
)
```

**¿Qué hace `cv=3`?**

Para **cada una de las 20 combinaciones** de hiperparámetros:

1. Divide los datos de entrenamiento en 3 folds
2. Entrena 3 veces (cada vez con un fold diferente para validar)
3. Calcula el ROC-AUC promedio de los 3 folds
4. Guarda ese promedio como el "score" de esa combinación

**Total de entrenamientos:** 20 combinaciones × 3 folds = **60 entrenamientos**


