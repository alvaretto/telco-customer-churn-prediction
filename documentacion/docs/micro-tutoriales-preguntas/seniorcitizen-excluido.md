# ¿Por qué solo tres variables numéricas en las estadísticas por Churn?

## 📋 Contexto

Este documento explica por qué el análisis exploratorio de datos (EDA) del proyecto Telco Customer Churn muestra estadísticas descriptivas solo para tres variables numéricas (`tenure`, `MonthlyCharges`, `TotalCharges`) cuando el dataset original contiene cuatro variables numéricas.

---

## 🔍 Análisis del Problema

La razón por la que solo se muestran **tres variables** (`tenure`, `MonthlyCharges`, `TotalCharges`) en las estadísticas por Churn es la siguiente:

### 📊 Variables numéricas en el dataset original

El dataset tiene **4 variables numéricas** originalmente:

1. **SeniorCitizen** (int64) - 0 o 1 (binaria)
2. **tenure** (int64) - Meses como cliente
3. **MonthlyCharges** (float64) - Cargo mensual
4. **TotalCharges** (object → convertida a float64) - Cargo total

### 🎯 ¿Por qué se excluyó `SeniorCitizen`?

En el código del notebook (línea 1458), se define explícitamente:

```python
# Variables numéricas
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
```

#### Razones para excluir `SeniorCitizen`:

1. **Es una variable binaria** (solo tiene valores 0 y 1)
   - 0 = No es adulto mayor
   - 1 = Es adulto mayor (65+ años)

2. **Se comporta más como categórica** que como numérica continua
   - No tiene sentido calcular percentiles o desviación estándar
   - La media solo indica la proporción de adultos mayores

3. **Ya fue analizada en la sección de variables categóricas** del EDA
   - Se analizó su relación con Churn usando tablas de contingencia
   - Se visualizó con gráficos de barras

4. **Las estadísticas descriptivas no son informativas** para variables binarias
   - Ejemplo: "El percentil 75 de SeniorCitizen es 0" no aporta valor
   - Es más útil saber: "16.2% de los clientes son adultos mayores"

---

## 💡 Evidencia en el código

### 1. Análisis de Correlación

`SeniorCitizen` **sí aparece** en la matriz de correlación (línea 1536):

```python
SeniorCitizen       0.150889
```

Esto muestra que tiene una correlación positiva moderada con Churn (0.15), lo que significa que los adultos mayores tienen una ligera tendencia a abandonar el servicio.

### 2. Feature Engineering

En el Feature Engineering (línea 2629), se confirma que hay **9 características numéricas** en total después de crear nuevas variables:

```python
Características numéricas (9):
['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges',
 'ChargeRatio', 'AvgMonthlyCharges', 'TotalServices',
 'SeniorWithDependents', 'HighValueContract']
```

### 3. Uso en el modelo

`SeniorCitizen` **sí se utiliza** en el modelo de predicción, solo se excluye de las estadísticas descriptivas por grupo para evitar redundancia.

---

## ✅ Conclusión

La decisión de mostrar solo 3 variables en las estadísticas descriptivas por Churn es **correcta desde el punto de vista analítico** por las siguientes razones:

### Ventajas de este enfoque:

1. **Claridad analítica**
   - `SeniorCitizen` es binaria y se analiza mejor como categórica
   - Las tres variables mostradas son **continuas** y se benefician de estadísticas descriptivas detalladas

2. **Evita redundancia**
   - `SeniorCitizen` ya fue analizada en la sección de variables categóricas
   - No tiene sentido repetir el análisis con estadísticas que no aportan valor

3. **Mejores prácticas de análisis de datos**
   - Las variables binarias se analizan con proporciones y tablas de contingencia
   - Las variables continuas se analizan con medias, medianas, desviaciones estándar, etc.

### Resumen de variables numéricas:

| Variable | Tipo | Incluida en estadísticas por Churn | Razón |
|----------|------|-----------------------------------|-------|
| `SeniorCitizen` | Binaria (0/1) | ❌ No | Se analiza como categórica |
| `tenure` | Continua | ✅ Sí | Variable continua clave |
| `MonthlyCharges` | Continua | ✅ Sí | Variable continua clave |
| `TotalCharges` | Continua | ✅ Sí | Variable continua clave |

---

## 📚 Referencias

- **Notebook principal**: `Telco_Customer_Churn.ipynb`
  - Línea 1458: Definición de `numerical_cols`
  - Línea 1488: Estadísticas por grupo con `groupby`
  - Línea 1536: Correlación de `SeniorCitizen` con Churn
  - Línea 2629: Feature Engineering con todas las variables numéricas

---

## 💭 Nota final

Si deseas incluir `SeniorCitizen` en las estadísticas descriptivas por Churn para fines de comparación o documentación, es posible hacerlo modificando la línea 1458. Sin embargo, desde el punto de vista de mejores prácticas de análisis de datos, el enfoque actual es el más apropiado.
