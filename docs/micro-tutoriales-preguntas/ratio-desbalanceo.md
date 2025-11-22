## 1. ¿Qué representa este ratio en términos de distribución de clases?

El ratio **2.77:1** significa que por cada **cliente que abandona** (Churn = Yes), hay aproximadamente **2.77 clientes que permanecen** (Churn = No).

**Distribución exacta del dataset:**

- **Clientes que NO abandonaron**: 5,174 (73.46%)
- **Clientes que SÍ abandonaron**: 1,869 (26.54%)
- **Total de clientes**: 7,043

Esto indica un **desbalanceo moderado** donde la clase mayoritaria (No Churn) representa casi 3 veces más casos que la clase minoritaria (Churn).

---

## 2. ¿Cómo se calcula este ratio de 2.77:1?

El cálculo es muy simple y se encuentra en el notebook principal:

```python
print(f"\nRatio de desbalanceo: {churn_counts['No']/churn_counts['Yes']:.2f}:1")
```

**Cálculo matemático:**
```
Ratio = Clientes No Churn / Clientes Churn
Ratio = 5,174 / 1,869
Ratio = 2.77:1
```

Este cálculo se realiza después del análisis exploratorio inicial de datos (EDA) para cuantificar el nivel de desbalanceo.

---

## 3. ¿Qué implicaciones tiene este desbalanceo para el modelo de ML?

El desbalanceo de 2.77:1 tiene **implicaciones críticas** para el entrenamiento del modelo:

### **Problemas que causa:**

1. **Sesgo hacia la clase mayoritaria**: Los modelos tienden a predecir "No Churn" con más frecuencia porque es la clase dominante (73%).

2. **Baja sensibilidad (Recall)**: El modelo puede tener dificultades para detectar clientes que realmente harán churn (la clase minoritaria).

3. **Métricas engañosas**: Un modelo "ingenuo" que siempre prediga "No Churn" tendría un 73% de accuracy, pero sería completamente inútil para el negocio.

4. **Aprendizaje desigual**: Durante el entrenamiento, el modelo ve muchos más ejemplos de "No Churn", lo que dificulta aprender los patrones de "Churn".

### **Analogía del proyecto:**

Como se explica en la documentación:

> **Analogía de la enfermedad rara**: Imagina un test médico para una enfermedad que solo afecta al 3% de la población:

> - Un modelo "tonto" que siempre dice "NO tienes la enfermedad" tendría 97% de accuracy
> - Pero sería inútil porque nunca detectaría a los enfermos

Lo mismo ocurre con el churn: necesitamos detectar específicamente a los que **SÍ se van**, no solo tener alta accuracy general.

---

## 4. ¿Dónde en el código se identifica o calcula este ratio?

El ratio se calcula en **múltiples puntos** del proyecto:

### **a) Análisis Exploratorio Inicial (EDA)**

En el notebook `Telco_Customer_Churn.ipynb`, después de cargar los datos:

```python
# Estadísticas
print("\nEstadísticas de Churn:")
print(f"Total de clientes: {len(df)}")
print(f"Clientes que NO abandonaron: {churn_counts['No']} ({100*churn_counts['No']/len(df):.2f}%)")
print(f"Clientes que SÍ abandonaron: {churn_counts['Yes']} ({100*churn_counts['Yes']/len(df):.2f}%)")
print(f"\nRatio de desbalanceo: {churn_counts['No']/churn_counts['Yes']:.2f}:1")
```

**Salida:**
```
Estadísticas de Churn:

Total de clientes: 7043
Clientes que NO abandonaron: 5174 (73.46%)
Clientes que SÍ abandonaron: 1869 (26.54%)

Ratio de desbalanceo: 2.77:1
```

### **b) Antes de aplicar SMOTE**

También se calcula el ratio en el conjunto de entrenamiento antes de balancear:

```python
print("Distribución ANTES de SMOTE:")
print(y_train.value_counts())
print(f"\nRatio: {y_train.value_counts()[0]/y_train.value_counts()[1]:.2f}:1")
```

**Salida:**
```
Distribución ANTES de SMOTE:
Churn
0    4139
1    1495
dtype: int64

Ratio: 2.77:1
```

### **c) Documentación**

El ratio también está documentado en:

- `guia_completa_analisis_churn/09_manejo_desbalanceo_clases.md`
- `README.md`
- Visualizaciones (gráficos de barras y pie charts)

---

## 5. ¿Qué técnicas se están utilizando para manejar este desbalanceo?

El proyecto utiliza **SMOTE (Synthetic Minority Over-sampling Technique)** como técnica principal para manejar el desbalanceo.

### **a) ¿Qué es SMOTE?**

SMOTE es una técnica que **crea ejemplos sintéticos** de la clase minoritaria (Churn = Yes) para balancear el dataset.

**Cómo funciona:**

1. Toma un ejemplo de la clase minoritaria
2. Encuentra sus K vecinos más cercanos (también de la clase minoritaria)
3. Crea nuevos ejemplos **interpolando** entre el ejemplo original y sus vecinos

**Analogía visual:**
```
Original:  A -------- B
                ↓
Sintético: A -- X -- B
```
Donde X es un nuevo ejemplo creado "entre" A y B.

### **b) Implementación en el código**

```python
# Aplicar SMOTE
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_processed, y_train)
```

**Resultado del balanceo:**

```
Distribución ANTES de SMOTE:
0    4139
1    1495
Ratio: 2.77:1

Distribución DESPUÉS de SMOTE:
0    4139
1    4139
Ratio: 1.00:1
```

SMOTE **duplica la clase minoritaria** creando ejemplos sintéticos hasta igualar la clase mayoritaria (balance 50/50).

### **c) ¿Por qué SMOTE y no otras técnicas?**

El proyecto considera tres técnicas principales:

| Técnica | Descripción | Ventajas | Desventajas |
|---------|-------------|----------|-------------|
| **SMOTE** ✅ | Crea ejemplos sintéticos | Ejemplos realistas, no duplicados | Puede crear ejemplos en zonas de solapamiento |
| **RandomOverSampler** | Duplica ejemplos existentes | Simple | Puede causar overfitting |
| **RandomUnderSampler** | Elimina ejemplos de clase mayoritaria | Reduce tamaño del dataset | Pierde información valiosa |

**SMOTE es la mejor opción** porque:

- ✅ Crea ejemplos realistas (no duplicados)
- ✅ Aumenta la diversidad de la clase minoritaria
- ✅ No pierde información de la clase mayoritaria
- ✅ Mejora el aprendizaje del modelo

### **d) Regla importante: SMOTE solo en entrenamiento**

**Importante**: SMOTE solo se aplica al conjunto de **entrenamiento**, NUNCA al de prueba.

**¿Por qué?**

**Analogía del examen**:

- Puedes estudiar con material adicional (SMOTE en train)
- Pero el examen debe ser con preguntas reales (test sin modificar)

### **e) Impacto de SMOTE en las métricas**

**Comparación de resultados:**

| Modelo | Métrica | Sin SMOTE | Con SMOTE | Mejora |
|--------|---------|-----------|-----------|--------|
| Random Forest | **Recall** | ~50% | ~78% | **+28%** |
| XGBoost | **Recall** | ~52% | ~80% | **+28%** |
| Logistic Regression | **Recall** | ~45% | ~81% | **+36%** |

**Interpretación:**

- **Recall aumenta significativamente** (~30% de mejora): El modelo detecta muchos más clientes que harán churn
- **Accuracy baja ligeramente** (84% → 82%): Trade-off aceptable
- **Precision baja un poco** (70% → 65%): Más falsos positivos, pero aceptable para el negocio

### **f) Otras técnicas consideradas (pero no implementadas)**

El proyecto también importa otras técnicas de balanceo:

```python
# Manejo de desbalanceo
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline
```

Aunque están disponibles, **SMOTE es la única técnica aplicada** porque ofrece el mejor balance entre rendimiento y realismo de los datos sintéticos.

---

## 📊 Resumen Visual

Según la imagen que compartiste:

```
Distribución de Churn:
┌─────────────────────────────┐
│ No:  5174 (73.5%) █████████ │
│ Yes: 1869 (26.5%) ███       │
└─────────────────────────────┘

Ratio de desbalanceo: 2.77:1
```

**Conclusión:** El ratio de 2.77:1 es un desbalanceo moderado que requiere atención especial. SMOTE resuelve este problema eficazmente, mejorando el Recall en ~30% y permitiendo que el modelo detecte mejor a los clientes en riesgo de churn, que es el objetivo principal del negocio.
