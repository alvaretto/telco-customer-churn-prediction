---
title: "¿Cómo se Obtienen los Hiperparámetros?"
author: "Bootcamp VirtIA - Explicación Detallada"
date: "`r Sys.Date()`"
output:
  html_document: default
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
    toc: true
    toc_depth: 3
---

# 🎯 ¿Cómo se Obtienen los Hiperparámetros?

## 📚 Conceptos Fundamentales

### ¿Qué son los Hiperparámetros?

Los **hiperparámetros** son parámetros de configuración del modelo que **NO se aprenden** durante el entrenamiento, sino que **se definen ANTES** de entrenar el modelo.

**Diferencia clave:**

- **Parámetros**: Se aprenden automáticamente (ej: pesos de una red neuronal, coeficientes de regresión)
- **Hiperparámetros**: Se configuran manualmente (ej: número de árboles, profundidad máxima)

### Ejemplos en Random Forest

Para un Random Forest, los hiperparámetros incluyen:

- `n_estimators`: Número de árboles en el bosque (100, 200, 300...)
- `max_depth`: Profundidad máxima de cada árbol (10, 20, None...)
- `min_samples_split`: Mínimo de muestras para dividir un nodo (2, 5, 10...)
- `min_samples_leaf`: Mínimo de muestras en una hoja (1, 2, 4...)
- `max_features`: Número de features a considerar ('sqrt', 'log2')
- `bootstrap`: Si usar muestreo con reemplazo (True, False)

---

## 🔍 Proceso de Obtención de Hiperparámetros

### Paso 1: Definir el Espacio de Búsqueda

Primero, defines un **diccionario** con los hiperparámetros que quieres probar y sus posibles valores:

```python
param_distributions = {
    'n_estimators': [100, 200, 300],        # 3 opciones
    'max_depth': [10, 20, None],            # 3 opciones
    'min_samples_split': [2, 5],            # 2 opciones
    'min_samples_leaf': [1, 2],             # 2 opciones
    'max_features': ['sqrt', 'log2'],       # 2 opciones
    'bootstrap': [True, False]              # 2 opciones
}
```

**Total de combinaciones posibles**: 3 × 3 × 2 × 2 × 2 × 2 = **144 combinaciones**

### Paso 2: Crear el Modelo Base

Creas una instancia del modelo sin especificar los hiperparámetros (usará valores por defecto):

```python
rf_base = RandomForestClassifier(random_state=42)
```

### Paso 3: Configurar RandomizedSearchCV

`RandomizedSearchCV` es una herramienta que:

1. **Prueba combinaciones aleatorias** de hiperparámetros
2. **Evalúa cada combinación** usando validación cruzada
3. **Selecciona la mejor combinación** según la métrica elegida

```python
random_search = RandomizedSearchCV(
    estimator=rf_base,                      # Modelo a optimizar
    param_distributions=param_distributions, # Espacio de búsqueda
    n_iter=20,                              # Probar 20 combinaciones aleatorias
    cv=3,                                   # Validación cruzada con 3 folds
    scoring='roc_auc',                      # Métrica a optimizar
    random_state=42,                        # Reproducibilidad
    n_jobs=-1,                              # Usar todos los CPUs
    verbose=1                               # Mostrar progreso
)
```

**¿Por qué 20 iteraciones y no las 144 posibles?**

- **Eficiencia**: Probar 20 combinaciones toma ~3 minutos vs ~20 minutos para todas
- **Efectividad**: RandomizedSearchCV encuentra buenas combinaciones rápidamente
- **Trade-off**: Pérdida mínima de precisión (~0.5-1%) con 85% menos tiempo

### Paso 4: Entrenar y Buscar

El método `.fit()` realiza la búsqueda:

```python
random_search.fit(X_train_balanced, y_train_balanced)
```

**¿Qué hace internamente?**

1. **Selecciona 20 combinaciones aleatorias** del espacio de búsqueda
2. **Para cada combinación**:
   - Divide los datos en 3 folds (cv=3)
   - Entrena el modelo en 2 folds y valida en 1
   - Repite 3 veces (cada fold se usa una vez para validación)
   - Calcula el promedio de ROC-AUC de los 3 folds
3. **Guarda la combinación con mejor ROC-AUC promedio**

### Paso 5: Obtener los Mejores Hiperparámetros

Una vez completada la búsqueda, accedes a los resultados:

```python
# Mejores hiperparámetros encontrados
print(random_search.best_params_)
# Ejemplo de salida:
# {
#     'n_estimators': 200,
#     'max_depth': 20,
#     'min_samples_split': 2,
#     'min_samples_leaf': 1,
#     'max_features': 'sqrt',
#     'bootstrap': True
# }

# Mejor score de validación cruzada
print(random_search.best_score_)  # Ej: 0.9365

# Modelo ya entrenado con los mejores hiperparámetros
best_model = random_search.best_estimator_
```

---

## 🎲 Ejemplo Práctico Paso a Paso

### Simulación de lo que hace RandomizedSearchCV

Imagina que RandomizedSearchCV prueba estas 5 combinaciones (de las 20):

| Iteración | n_estimators | max_depth | min_samples_split | ROC-AUC (CV) |
|-----------|--------------|-----------|-------------------|--------------|
| 1         | 100          | 10        | 2                 | 0.9201       |
| 2         | 200          | 20        | 5                 | **0.9365** ✅ |
| 3         | 300          | None      | 2                 | 0.9287       |
| 4         | 100          | 20        | 5                 | 0.9156       |
| 5         | 200          | 10        | 2                 | 0.9298       |

## 📊 Visualización del Proceso

### Diagrama de Flujo

```
┌─────────────────────────────────────────────────────────────┐
│ 1. DEFINIR ESPACIO DE BÚSQUEDA                              │
│    param_distributions = {                                  │
│        'n_estimators': [100, 200, 300],                     │
│        'max_depth': [10, 20, None],                         │
│        ...                                                  │
│    }                                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CREAR RandomizedSearchCV                                 │
│    random_search = RandomizedSearchCV(...)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. ENTRENAR (random_search.fit())                           │
│                                                             │
│    Para cada una de las 20 iteraciones:                    │
│    ┌─────────────────────────────────────────────┐         │
│    │ a) Seleccionar combinación aleatoria        │         │
│    │    Ej: n_estimators=200, max_depth=20       │         │
│    └──────────────┬──────────────────────────────┘         │
│                   │                                         │
│                   ▼                                         │
│    ┌─────────────────────────────────────────────┐         │
│    │ b) Validación Cruzada (3 folds)             │         │
│    │    Fold 1: Train en 2/3, Test en 1/3        │         │
│    │    Fold 2: Train en 2/3, Test en 1/3        │         │
│    │    Fold 3: Train en 2/3, Test en 1/3        │         │
│    └──────────────┬──────────────────────────────┘         │
│                   │                                         │
│                   ▼                                         │
│    ┌─────────────────────────────────────────────┐         │
│    │ c) Calcular ROC-AUC promedio                │         │
│    │    Promedio de los 3 folds                  │         │
│    └─────────────────────────────────────────────┘         │
│                                                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. SELECCIONAR MEJOR COMBINACIÓN                            │
│    best_params_ = combinación con mayor ROC-AUC             │
│    best_score_ = mejor ROC-AUC promedio                     │
│    best_estimator_ = modelo entrenado con best_params_      │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 Preguntas Frecuentes

### ❓ ¿Por qué no usar los hiperparámetros por defecto?

Los valores por defecto de scikit-learn son genéricos y rara vez son óptimos para tu dataset específico. La optimización puede mejorar el rendimiento en 5-15%.

### ❓ ¿Cómo sé qué valores incluir en el espacio de búsqueda?

1. **Documentación**: Lee la documentación del modelo
2. **Experiencia**: Valores comunes en la literatura
3. **Experimentación**: Prueba rangos amplios primero, luego refina
4. **Recursos**: Tutoriales y papers del área

### ❓ ¿Qué pasa si aumento n_iter de 20 a 100?

- ✅ **Ventaja**: Mayor probabilidad de encontrar mejores hiperparámetros
- ❌ **Desventaja**: Tiempo de ejecución 5x mayor
- 💡 **Recomendación**: Empieza con 20, si el tiempo lo permite, aumenta a 50

### ❓ ¿Por qué usar random_state?

Para **reproducibilidad**: Si ejecutas el código dos veces con la misma semilla, obtendrás exactamente los mismos resultados.

```python
# Sin random_state: resultados diferentes cada vez
random_search = RandomizedSearchCV(...)  # ❌

# Con random_state: resultados idénticos
random_search = RandomizedSearchCV(..., random_state=42)  # ✅
```

### ❓ ¿Qué significa cv=3?

**Validación cruzada con 3 folds**:

1. Divide los datos de entrenamiento en 3 partes iguales
2. Entrena 3 veces, cada vez usando 2 partes para entrenar y 1 para validar
3. Promedia los resultados de las 3 validaciones

**Ventaja**: Evaluación más robusta que un solo train/test split

---

## 🎯 Código Completo del Notebook

Aquí está el código exacto usado en el notebook `Telco_Customer_Churn.ipynb`:

```python
from sklearn.model_selection import RandomizedSearchCV

# Paso 1: Definir espacio de búsqueda
param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True, False]
}

# Paso 2: Crear modelo base
rf_base = RandomForestClassifier(random_state=42)

# Paso 3: Configurar RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=rf_base,
    param_distributions=param_distributions,
    n_iter=20,        # Probar 20 combinaciones
    cv=3,             # Validación cruzada con 3 folds
    scoring='roc_auc',
    random_state=42,
    n_jobs=-1,        # Usar todos los CPUs disponibles
    verbose=1
)

# Paso 4: Entrenar y buscar
random_search.fit(X_train_balanced, y_train_balanced)

# Paso 5: Obtener resultados
print("Mejores hiperparámetros encontrados:")
print(random_search.best_params_)

print(f"\nMejor score de validación cruzada (ROC-AUC): {random_search.best_score_:.4f}")

# Paso 6: Usar el mejor modelo
best_rf = random_search.best_estimator_
y_pred = best_rf.predict(X_test_processed)
y_pred_proba = best_rf.predict_proba(X_test_processed)[:, 1]
```

---

## 📈 Resultados Típicos

Cuando ejecutas este código, obtienes algo como:

```
Iniciando búsqueda de hiperparámetros (OPTIMIZADA)...
🎲 Usando semilla: 42
⚡ Configuración: n_iter=20, cv=3 (Opción Moderada)
⏱️  Tiempo estimado: ~3 minutos

Fitting 3 folds for each of 20 candidates, totalling 60 fits
[Parallel(n_jobs=-1)]: Done  60 out of  60 | elapsed:  2.8min finished

================================================================================

Mejores hiperparámetros encontrados:
{
    'n_estimators': 200,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'max_features': 'sqrt',
    'max_depth': 20,
    'bootstrap': True
}

Mejor score de validación cruzada (ROC-AUC): 0.9365

Rendimiento en conjunto de prueba:
  Accuracy: 0.8274
  Precision: 0.6667
  Recall: 0.5700
  F1-Score: 0.6147
  ROC-AUC: 0.8274
```

---

## 🚀 Resumen Ejecutivo

### ¿Cómo se obtienen los hiperparámetros? - Respuesta Corta

1. **Defines** un espacio de búsqueda con posibles valores
2. **RandomizedSearchCV prueba** combinaciones aleatorias
3. **Cada combinación se evalúa** con validación cruzada
4. **Se selecciona** la combinación con mejor métrica (ROC-AUC)
5. **Accedes** a los mejores valores con `.best_params_`

### Analogía Simple

Es como **buscar la mejor receta de pizza**:

- **Ingredientes variables** = hiperparámetros (cantidad de queso, tiempo de horneado, temperatura)
- **Espacio de búsqueda** = todas las combinaciones posibles de ingredientes
- **RandomizedSearchCV** = probar 20 recetas aleatorias en lugar de las 144 posibles
- **Validación cruzada** = hacer que 3 personas diferentes prueben cada pizza
- **Mejor receta** = la que obtuvo mejor calificación promedio

¡Y listo! Ahora tienes los mejores hiperparámetros para tu modelo. 🎉


