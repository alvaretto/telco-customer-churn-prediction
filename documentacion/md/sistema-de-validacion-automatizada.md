---
title: "Sistema de Validación Automatizada - Solución de Errores"
output:
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
    toc: true
    toc_depth: 3
    number_sections: true
  html_document: default
---

# 🔧 Solución: Error en Iteraciones del Notebook Telco Customer Churn

## 📋 Resumen Ejecutivo

**Problema Identificado:** Todas las 10 iteraciones del sistema de validación multi-iteración fallaron con el mismo error.

**Error Específico:**

```
GradientBoostingClassifier.__init__() got an unexpected keyword argument 'n_jobs'
```

**Causa Raíz:** El parámetro `n_jobs` no es compatible con `GradientBoostingClassifier` de scikit-learn.

**Estado:** ✅ Solución identificada y documentada

---

## 🔍 Análisis del Problema

### Contexto

El notebook ejecuta un sistema de validación multi-iteración que:

- Ejecuta 10 iteraciones completas del pipeline de ML
- Cada iteración usa una semilla diferente para validar robustez
- Compara técnicas de balanceo (SMOTE, SMOTETomek, RandomUnderSampler)
- Entrena múltiples modelos (RandomForest, XGBoost, GradientBoosting)
- Valida la robustez del mejor modelo con 3 semillas adicionales

### Ubicación del Error

**Archivo:** `Telco_Customer_Churn.ipynb`

**Función:** `ejecutar_pipeline_simplificado()`

**Línea problemática:** 5032

**Código con error:**

```python
model_copy = type(best_model)(random_state=mini_seed, n_jobs=-1) if hasattr(best_model, 'random_state') else type(best_model)()
```

### ¿Por qué falla?

Los modelos de scikit-learn tienen diferentes parámetros de inicialización:

**Modelos que SÍ aceptan `n_jobs`:**

- `RandomForestClassifier`
- `XGBClassifier` (XGBoost)
- `ExtraTreesClassifier`
- `KNeighborsClassifier`

**Modelos que NO aceptan `n_jobs`:**

- `GradientBoostingClassifier` ❌
- `LogisticRegression` (acepta `n_jobs` solo en versiones recientes)
- `DecisionTreeClassifier`

---

## ✅ Solución Propuesta

### Opción 1: Verificación Dinámica de Parámetros (Recomendada)

Modificar la línea 5032 para verificar si el modelo acepta `n_jobs` antes de pasarlo:

```python
# Crear copia del modelo con parámetros apropiados
model_params = {'random_state': mini_seed} if hasattr(best_model, 'random_state') else {}

# Solo agregar n_jobs si el modelo lo acepta
if 'n_jobs' in type(best_model)().get_params():
    model_params['n_jobs'] = -1

model_copy = type(best_model)(**model_params)
```

### Opción 2: Manejo Específico por Tipo de Modelo

```python
# Crear copia del modelo según su tipo
if isinstance(best_model, GradientBoostingClassifier):
    model_copy = type(best_model)(random_state=mini_seed)
elif hasattr(best_model, 'random_state'):
    model_copy = type(best_model)(random_state=mini_seed, n_jobs=-1)
else:
    model_copy = type(best_model)()
```

### Opción 3: Try-Except (Más Robusta)

```python
# Intentar crear con n_jobs, si falla, crear sin él
try:
    if hasattr(best_model, 'random_state'):
        model_copy = type(best_model)(random_state=mini_seed, n_jobs=-1)
    else:
        model_copy = type(best_model)(n_jobs=-1)
except TypeError:
    # El modelo no acepta n_jobs
    if hasattr(best_model, 'random_state'):
        model_copy = type(best_model)(random_state=mini_seed)
    else:
        model_copy = type(best_model)()
```

---

## 🛠️ Implementación Paso a Paso

### Paso 1: Localizar la Celda

Buscar la celda que contiene la función `ejecutar_pipeline_simplificado()` en el notebook.

### Paso 2: Reemplazar el Código

Localizar estas líneas (aproximadamente líneas 5032-5036):

```python
model_copy = type(best_model)(random_state=mini_seed, n_jobs=-1) if hasattr(best_model, 'random_state') else type(best_model)()
if hasattr(model_copy, 'n_estimators'):
    model_copy.n_estimators = 50  # Reducir para velocidad
if hasattr(model_copy, 'eval_metric'):
    model_copy.eval_metric = 'logloss'
```

Reemplazar con (Opción 1 - Recomendada):

```python
# Crear copia del modelo con parámetros apropiados
model_params = {'random_state': mini_seed} if hasattr(best_model, 'random_state') else {}

# Solo agregar n_jobs si el modelo lo acepta
try:
    if 'n_jobs' in type(best_model)().get_params():
        model_params['n_jobs'] = -1
except:
    pass  # Algunos modelos pueden fallar en get_params()

model_copy = type(best_model)(**model_params)

if hasattr(model_copy, 'n_estimators'):
    model_copy.n_estimators = 50  # Reducir para velocidad
if hasattr(model_copy, 'eval_metric'):
    model_copy.eval_metric = 'logloss'
```

### Paso 3: Ejecutar la Celda

Ejecutar la celda que contiene la función `ejecutar_pipeline_simplificado()` para redefinirla.

### Paso 4: Volver a Ejecutar las Iteraciones

Ejecutar la celda que contiene el bucle de iteraciones:

```python
for i in range(1, N_ITERATIONS + 1):
    ...
```

---

## 📊 Resultados Esperados

Después de aplicar la solución:

**Antes:**

- ❌ 10/10 iteraciones fallidas
- ❌ 0% tasa de éxito
- ❌ No hay modelos entrenados
- ❌ No hay métricas de robustez

**Después:**

- ✅ 10/10 iteraciones exitosas (esperado)
- ✅ 100% tasa de éxito
- ✅ 10 modelos entrenados y guardados
- ✅ Métricas de robustez calculadas
- ✅ Reportes generados para cada iteración

---

## 🔬 Validación de la Solución

### Verificaciones a Realizar

1. **Ejecución sin errores:**

   - Las 10 iteraciones deben completarse sin excepciones
   - Cada iteración debe mostrar "✅ Iteración X completada exitosamente"

2. **Archivos generados:**

   - 10 archivos de modelo: `model_iter1_seed1042.pkl` ... `model_iter10_seed10042.pkl`
   - 10 reportes: `report_iter1_seed1042.md` ... `report_iter10_seed10042.md`
   - 1 archivo consolidado: `all_iterations_results.json`

3. **Métricas esperadas:**

   - ROC-AUC promedio: ~0.84 (±0.01)
   - Recall promedio: ~0.75 (±0.05)
   - Precision promedio: ~0.65 (±0.05)
   - F1-Score promedio: ~0.70 (±0.05)

4. **Criterios de aceptación:**

   - ROC-AUC promedio ≥ 0.82
   - Recall promedio ≥ 0.70
   - Desviación estándar ≤ 0.03
   - Consistencia ≥ 80% iteraciones con ROC-AUC > 0.80

---

## 📝 Notas Adicionales

### Compatibilidad de Parámetros por Modelo

| Modelo | `random_state` | `n_jobs` | `n_estimators` | `eval_metric` |
|--------|----------------|----------|----------------|---------------|
| RandomForestClassifier | ✅ | ✅ | ✅ | ❌ |
| XGBClassifier | ✅ | ✅ | ✅ | ✅ |
| GradientBoostingClassifier | ✅ | ❌ | ✅ | ❌ |
| LogisticRegression | ✅ | ✅* | ❌ | ❌ |
| DecisionTreeClassifier | ✅ | ❌ | ❌ | ❌ |

*Solo en versiones recientes de scikit-learn (≥1.0)

### Mejores Prácticas

Para evitar este tipo de errores en el futuro:

- Usar `inspect.signature()` para verificar parámetros aceptados
- Implementar try-except al instanciar modelos dinámicamente
- Documentar qué parámetros acepta cada modelo
- Usar diccionarios de parámetros en lugar de argumentos posicionales

---

## 🚀 Próximos Pasos

Una vez aplicada la solución:

1. Ejecutar las 10 iteraciones completas
2. Analizar los resultados consolidados
3. Verificar que se cumplan los criterios de aceptación
4. Generar el informe final de deployment
5. Decidir si el modelo está listo para producción

---

## 📞 Soporte

Si después de aplicar la solución persisten los errores:

- Verificar la versión de scikit-learn: `sklearn.__version__`
- Verificar la versión de XGBoost: `xgb.__version__`
- Revisar los logs completos de error
- Verificar que el DataFrame `df` esté cargado correctamente

**Versiones recomendadas:**

- Python: 3.8+
- scikit-learn: 1.0+
- XGBoost: 1.5+
- imbalanced-learn: 0.9+

---

*Documento generado el 2025-11-24*
