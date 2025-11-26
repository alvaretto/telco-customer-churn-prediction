---
title: "¿Qué es lo que se Aleatoriza con random_state?"
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

# 🎲 ¿Qué es lo que se Aleatoriza con `random_state`?

## 📚 Definición Simple

**`random_state`** es un parámetro que **controla la aleatoriedad** en algoritmos de machine learning. Funciona como una **semilla** que determina qué números "aleatorios" se generarán.

---

## 🔍 ¿Qué se Aleatoriza Exactamente?

En el proyecto de churn, `random_state` controla la aleatoriedad en **múltiples procesos**:

### 1. **División Train/Test** 🎯

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)
```

**¿Qué se aleatoriza?**

- **Qué filas van a train y cuáles a test**
- Sin `random_state`: cada ejecución crearía divisiones diferentes
- Con `random_state=42`: siempre las mismas filas en train/test

**Analogía:** Es como barajar un mazo de cartas. Con `random_state=42`, siempre barajas de la misma forma.

---

### 2. **Modelos de Machine Learning** 🤖

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
models = {
    'Random Forest': RandomForestClassifier(random_state=RANDOM_STATE, n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(random_state=RANDOM_STATE),
    'XGBoost': xgb.XGBClassifier(random_state=RANDOM_STATE),
}
```

**¿Qué se aleatoriza en cada modelo?**

#### **Random Forest:**

- **Selección aleatoria de features** en cada split
- **Selección aleatoria de muestras** (bootstrap) para cada árbol
- **Orden de construcción** de los árboles

#### **Gradient Boosting:**

- **Inicialización de pesos**
- **Muestreo de datos** en cada iteración
- **Selección de features** para cada árbol

#### **Logistic Regression:**

- **Inicialización de pesos** (cuando usa solver iterativo)
- **Orden de procesamiento** de datos en algunos solvers

---

### 3. **SMOTE (Balanceo de Datos)** ⚖️

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
smote = SMOTE(random_state=RANDOM_STATE)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)
```

**¿Qué se aleatoriza?**

- **Selección de vecinos** para crear ejemplos sintéticos
- **Posición de los nuevos puntos** entre vecinos
- **Orden de generación** de ejemplos sintéticos

**Ejemplo:**

```
Cliente A: [tenure=10, MonthlyCharges=50]
Cliente B: [tenure=15, MonthlyCharges=60]

SMOTE crea un punto aleatorio entre A y B:
Cliente Sintético: [tenure=12.3, MonthlyCharges=54.7]
                                    ↑ Aleatorio
```

---

### 4. **RandomizedSearchCV (Optimización)** 🔧

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
random_search = RandomizedSearchCV(
    estimator=rf_base,
    param_distributions=param_distributions,
    n_iter=20,
    cv=3,
    random_state=RANDOM_STATE,
)
```

**¿Qué se aleatoriza?**

- **Qué 20 combinaciones** de hiperparámetros se prueban (de 144 posibles)
- **Orden de evaluación** de las combinaciones

**Ejemplo:**

```
Posibles combinaciones: 144
Con random_state=42, siempre prueba las mismas 20:
  1. n_estimators=200, max_depth=10, ...
  2. n_estimators=100, max_depth=None, ...
  ...
  20. n_estimators=300, max_depth=20, ...
```

---

### 5. **Validación Cruzada (StratifiedKFold)** 📊

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
cv_scores = cross_val_score(best_rf, X_train_balanced, y_train_balanced,
                            cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE),
                            scoring='roc_auc', n_jobs=-1)
```

**¿Qué se aleatoriza?**

- **Cómo se dividen los datos** en los 5 folds
- **Orden de las filas** antes de dividir (cuando `shuffle=True`)

---

## 🎯 En el Proyecto: Modo Reproducible vs Experimental

El notebook tiene una configuración especial:

```python
# path=Telco_Customer_Churn.ipynb mode=EXCERPT
REPRODUCIBLE_MODE = False  # True = resultados fijos, False = resultados variables

if REPRODUCIBLE_MODE:
    RANDOM_STATE = 42
    print("🔒 MODO REPRODUCIBLE ACTIVADO")
else:
    RANDOM_STATE = np.random.randint(0, 10000)
    print("🔬 MODO EXPERIMENTAL ACTIVADO")
    print(f"   → Semilla aleatoria: {RANDOM_STATE}")
```

### **Modo Reproducible (RANDOM_STATE = 42):**

✅ **Ventajas:**

- Resultados idénticos en cada ejecución
- Fácil de depurar
- Permite comparar cambios en el código

❌ **Desventajas:**

- Puede ocultar variabilidad del modelo
- No prueba robustez

### **Modo Experimental (RANDOM_STATE = aleatorio):**

✅ **Ventajas:**

- Prueba robustez del modelo
- Detecta si resultados dependen de la semilla
- Más realista

❌ **Desventajas:**

- Resultados diferentes cada vez
- Difícil de reproducir bugs

---

## 🔑 Conceptos Clave

### 1. **Reproducibilidad**

```python
# Ejecución 1 con random_state=42
ROC-AUC: 0.8274

# Ejecución 2 con random_state=42
ROC-AUC: 0.8274  # ✅ Idéntico

# Ejecución 3 sin random_state
ROC-AUC: 0.8301  # ❌ Diferente
```

### 2. **Números Pseudoaleatorios**

Los números "aleatorios" en computadoras **no son realmente aleatorios**:

```
Semilla 42 → Secuencia: [0.374, 0.950, 0.731, 0.598, ...]
Semilla 42 → Secuencia: [0.374, 0.950, 0.731, 0.598, ...]  # Siempre igual
Semilla 99 → Secuencia: [0.123, 0.456, 0.789, 0.012, ...]  # Diferente
```

### 3. **¿Por qué 42?**

Es una **convención** en la comunidad de ML (referencia a "The Hitchhiker's Guide to the Galaxy"). Puedes usar cualquier número:

```python
random_state=42   # ✅ Común
random_state=0    # ✅ También común
random_state=123  # ✅ Válido
random_state=999  # ✅ Válido
```

---

## 📋 Resumen Ejecutivo

### ¿Qué se aleatoriza con `random_state`?

1. **División de datos** (train/test, folds)
2. **Construcción de modelos** (árboles, pesos, muestras)
3. **Generación de datos sintéticos** (SMOTE)
4. **Selección de hiperparámetros** (RandomizedSearchCV)
5. **Orden de procesamiento** (shuffle en validación cruzada)

### ¿Cuándo usar `random_state`?

- ✅ **Siempre** en producción y experimentos científicos
- ✅ Para **depurar** y comparar modelos
- ✅ Para **reproducir** resultados en papers/reportes

### ¿Cuándo NO usar `random_state`?

- ⚠️ Para **probar robustez** del modelo
- ⚠️ Para **validar estabilidad** de resultados
- ⚠️ En **análisis de sensibilidad**

---

## 💡 Analogía Final

**`random_state` es como el código de una caja fuerte:**

- **Sin código (sin random_state):** Cada vez que abres la caja, encuentras cosas diferentes
- **Con código 42 (random_state=42):** Siempre encuentras exactamente las mismas cosas en el mismo orden

¿Te quedó claro qué se aleatoriza con `random_state`? 🤓

