---
title: "¿Cómo se Obtienen las Variables Categóricas Más Importantes?"
author: "Bootcamp VirtIA - Tutorial Detallado"
output:
  html_document: default
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
    toc: true
    toc_depth: 3
---

# 🎯 ¿Cómo se Obtienen las Variables Categóricas Más Importantes?

## 📚 Introducción

En el proyecto de predicción de churn, hay **dos métodos principales** para identificar las variables categóricas más importantes:

1. **Análisis Exploratorio (EDA)**: Análisis visual y estadístico de tasas de churn
2. **Feature Importance del Modelo**: Importancia calculada por Random Forest

---

## 🔍 Método 1: Análisis Exploratorio (EDA)

### Paso 1: Identificar Variables Categóricas

```python
# Identificar todas las variables categóricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Excluir ID y variable objetivo
categorical_cols.remove('customerID')
categorical_cols.remove('Churn')

print(f"Variables categóricas a analizar: {len(categorical_cols)}")
print(categorical_cols)
```

**Salida:**
```
Variables categóricas a analizar: 14
['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod',
 'PaperlessBilling']
```

### Paso 2: Seleccionar Variables Importantes Manualmente

En el notebook, se seleccionan **6 variables categóricas clave** basadas en conocimiento del dominio:

```python
important_cats = ['Contract', 'InternetService', 'PaymentMethod',
                  'TechSupport', 'OnlineSecurity', 'PaperlessBilling']
```

**¿Por qué estas 6?**

- **Contract**: Tipo de contrato (mes a mes, anual, bianual)
- **InternetService**: Tipo de servicio de internet (DSL, Fibra, No)
- **PaymentMethod**: Método de pago (cheque, transferencia, tarjeta)
- **TechSupport**: Si tiene soporte técnico (Sí, No, No internet)
- **OnlineSecurity**: Si tiene seguridad online (Sí, No, No internet)
- **PaperlessBilling**: Si usa facturación sin papel (Sí, No)

### Paso 3: Calcular Tasa de Churn por Categoría

```python
# Análisis estadístico
print("\nTasa de Churn por categoría:\n")
for col in important_cats:
    print(f"\n{col}:")
    churn_rate = df.groupby(col)['Churn'].apply(
        lambda x: (x=='Yes').sum()/len(x)*100
    )
    print(churn_rate.sort_values(ascending=False))
```

**Salida típica:**

```
Contract:
Month-to-month    42.71%
One year          11.27%
Two year           2.83%

InternetService:
Fiber optic       41.89%
DSL               18.96%
No                 7.40%

PaymentMethod:
Electronic check         45.29%
Mailed check             19.08%
Bank transfer (auto)     16.67%
Credit card (auto)       15.23%

TechSupport:
No                    41.68%
No internet service    7.40%
Yes                   15.17%

OnlineSecurity:
No                    41.77%
No internet service    7.40%
Yes                   14.63%

PaperlessBilling:
Yes    33.57%
No     16.33%
```

### Paso 4: Visualizar con Gráficos de Barras

```python
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.ravel()

for idx, col in enumerate(important_cats):
    # Crear tabla de contingencia (porcentajes)
    ct = pd.crosstab(df[col], df['Churn'], normalize='index') * 100

    # Graficar
    ct.plot(kind='bar', ax=axes[idx],
            color=['#2ecc71', '#e74c3c'],
            alpha=0.7, edgecolor='black')
    axes[idx].set_title(f'Churn por {col}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Porcentaje (%)')
    axes[idx].legend(title='Churn', labels=['No', 'Yes'])
    axes[idx].grid(axis='y', alpha=0.3)
    axes[idx].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
```

### 📊 Interpretación de Resultados

**Variables con MAYOR impacto en churn:**

1. **Contract (Month-to-month)**: 42.71% de churn
   - Clientes sin compromiso a largo plazo abandonan más

2. **InternetService (Fiber optic)**: 41.89% de churn
   - Posiblemente por precio alto o problemas de servicio

3. **PaymentMethod (Electronic check)**: 45.29% de churn
   - Método de pago menos conveniente

4. **TechSupport (No)**: 41.68% de churn
   - Clientes sin soporte técnico abandonan más

5. **OnlineSecurity (No)**: 41.77% de churn
   - Clientes sin seguridad online abandonan más

6. **PaperlessBilling (Yes)**: 33.57% de churn
   - Facturación digital correlaciona con mayor churn

---

## 🤖 Método 2: Feature Importance del Modelo

### ¿Qué es Feature Importance?

**Feature Importance** es una métrica que indica **cuánto contribuye cada variable** a las predicciones del modelo.

En Random Forest, se calcula como:

- **Promedio de la reducción de impureza** (Gini) que cada variable aporta en todos los árboles del bosque

### Paso 1: Entrenar el Modelo

```python
from sklearn.ensemble import RandomForestClassifier

# Entrenar Random Forest
best_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=2,
    random_state=42
)

best_rf.fit(X_train_balanced, y_train_balanced)
```

### Paso 2: Obtener Feature Importance

```python
# Obtener importancia de características
feature_importance = best_rf.feature_importances_

# Crear DataFrame
importance_df = pd.DataFrame({
    'Feature': feature_names,  # Nombres de todas las features
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

# Top 20 características
top_20 = importance_df.head(20)

print("\nTop 10 Características Más Importantes:\n")
print(importance_df.head(10).to_string(index=False))
```

**Salida típica:**

```
           Feature  Importance
            tenure    0.2847
    MonthlyCharges    0.1523
      TotalCharges    0.1289
  Contract_Two year    0.0876
Contract_Month-to-month 0.0654
InternetService_Fiber optic 0.0543
     TechSupport_No    0.0421
  OnlineSecurity_No    0.0398
PaymentMethod_Electronic check 0.0312
  PaperlessBilling_Yes 0.0287
```

### Paso 3: Visualizar Feature Importance

```python
# Visualizar Top 20
plt.figure(figsize=(12, 8))
bars = plt.barh(range(len(top_20)), top_20['Importance'],
                color=plt.cm.viridis(np.linspace(0, 1, len(top_20))),
                edgecolor='black', alpha=0.7)
plt.yticks(range(len(top_20)), top_20['Feature'])
plt.xlabel('Importancia', fontsize=12, fontweight='bold')
plt.title('Top 20 Características Más Importantes', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.3)

# Añadir valores
for i, (idx, row) in enumerate(top_20.iterrows()):
    plt.text(row['Importance'], i, f" {row['Importance']:.4f}",
             va='center', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.show()
```

---

## 🔑 Variables Categóricas Más Importantes (Resultados del Modelo)

### Top 10 Features (Incluyendo Categóricas)

| Ranking | Feature | Tipo | Importancia | Interpretación |
|---------|---------|------|-------------|----------------|
| 1 | **tenure** | Numérica | 0.2847 | Antigüedad del cliente |
| 2 | **MonthlyCharges** | Numérica | 0.1523 | Cargo mensual |
| 3 | **TotalCharges** | Numérica | 0.1289 | Cargo total acumulado |
| 4 | **Contract_Two year** | **Categórica** | 0.0876 | Contrato de 2 años |
| 5 | **Contract_Month-to-month** | **Categórica** | 0.0654 | Contrato mes a mes |
| 6 | **InternetService_Fiber optic** | **Categórica** | 0.0543 | Internet fibra óptica |
| 7 | **TechSupport_No** | **Categórica** | 0.0421 | Sin soporte técnico |
| 8 | **OnlineSecurity_No** | **Categórica** | 0.0398 | Sin seguridad online |
| 9 | **PaymentMethod_Electronic check** | **Categórica** | 0.0312 | Pago con cheque electrónico |
| 10 | **PaperlessBilling_Yes** | **Categórica** | 0.0287 | Facturación sin papel |

### Solo Variables Categóricas (Top 10)

| Ranking | Variable Categórica | Importancia | Porcentaje |
|---------|---------------------|-------------|------------|
| 1 | **Contract_Two year** | 0.0876 | 8.76% |
| 2 | **Contract_Month-to-month** | 0.0654 | 6.54% |
| 3 | **InternetService_Fiber optic** | 0.0543 | 5.43% |
| 4 | **TechSupport_No** | 0.0421 | 4.21% |
| 5 | **OnlineSecurity_No** | 0.0398 | 3.98% |
| 6 | **PaymentMethod_Electronic check** | 0.0312 | 3.12% |
| 7 | **PaperlessBilling_Yes** | 0.0287 | 2.87% |
| 8 | **InternetService_DSL** | 0.0234 | 2.34% |
| 9 | **OnlineBackup_No** | 0.0198 | 1.98% |
| 10 | **DeviceProtection_No** | 0.0176 | 1.76% |

---

## 🧮 ¿Cómo se Calcula Feature Importance?

### En Random Forest

Random Forest calcula la importancia de cada feature como:

1. **Para cada árbol del bosque:**
   - Cuando se hace un split (división) en un nodo usando una feature
   - Se calcula cuánto **reduce la impureza** (Gini) ese split
   - Se acumula esa reducción para esa feature

2. **Al final:**
   - Se **promedia** la reducción de impureza de cada feature en todos los árboles
   - Se **normaliza** para que la suma de todas las importancias sea 1.0

### Ejemplo Simplificado

Imagina un Random Forest con 3 árboles:

**Árbol 1:**

- Split en `tenure`: reduce impureza en 0.15
- Split en `Contract`: reduce impureza en 0.08

**Árbol 2:**

- Split en `tenure`: reduce impureza en 0.18
- Split en `MonthlyCharges`: reduce impureza en 0.12

**Árbol 3:**

- Split en `Contract`: reduce impureza en 0.10
- Split en `tenure`: reduce impureza en 0.14

**Importancia promedio:**

- `tenure`: (0.15 + 0.18 + 0.14) / 3 = **0.157**
- `Contract`: (0.08 + 0.10) / 2 = **0.090**
- `MonthlyCharges`: 0.12 / 1 = **0.120**

**Normalizado (suma = 1.0):**

- `tenure`: 0.157 / 0.367 = **0.428** (42.8%)
- `MonthlyCharges`: 0.120 / 0.367 = **0.327** (32.7%)
- `Contract`: 0.090 / 0.367 = **0.245** (24.5%)

---

## 🔄 Comparación de Métodos

### Método 1: Análisis Exploratorio (EDA)

**✅ Ventajas:**

- Fácil de entender e interpretar
- No requiere entrenar modelo
- Muestra relación directa con churn
- Útil para presentaciones a stakeholders

**❌ Desventajas:**

- Solo muestra relaciones univariadas (una variable a la vez)
- No captura interacciones entre variables
- Puede ser engañoso (correlación ≠ causalidad)
- Requiere selección manual de variables

**📊 Cuándo usar:**

- Fase inicial de exploración
- Presentaciones a negocio
- Validar hipótesis de dominio

### Método 2: Feature Importance del Modelo

**✅ Ventajas:**

- Captura interacciones entre variables
- Basado en el modelo real que se usará
- Considera todas las variables simultáneamente
- Más preciso para predicción

**❌ Desventajas:**

- Requiere entrenar modelo
- Más difícil de explicar a no técnicos
- Puede ser sesgado por variables correlacionadas
- Depende del tipo de modelo

**📊 Cuándo usar:**

- Selección de features para el modelo
- Optimización de rendimiento
- Análisis técnico profundo
- Reducción de dimensionalidad

---

## 💡 Interpretación de Variables Categóricas Importantes

### 1. Contract (Tipo de Contrato)

**Importancia:** Alta (8.76% + 6.54% = 15.30% combinado)

**Hallazgos:**

- `Contract_Two year`: Importancia 0.0876 → **Protege contra churn**
- `Contract_Month-to-month`: Importancia 0.0654 → **Aumenta churn**

**Acción:**

- ✅ Promover contratos anuales/bianuales con descuentos
- ✅ Ofrecer incentivos para migrar de mes a mes a contratos largos

### 2. InternetService (Tipo de Internet)

**Importancia:** Media-Alta (5.43%)

**Hallazgos:**

- `InternetService_Fiber optic`: Importancia 0.0543 → **Aumenta churn**
- Posiblemente por precio alto o problemas de calidad

**Acción:**

- ✅ Revisar precios de fibra óptica
- ✅ Mejorar calidad de servicio de fibra
- ✅ Ofrecer paquetes promocionales

### 3. TechSupport (Soporte Técnico)

**Importancia:** Media (4.21%)

**Hallazgos:**

- `TechSupport_No`: Importancia 0.0421 → **Aumenta churn**
- Clientes sin soporte técnico abandonan más

**Acción:**

- ✅ Promover servicio de soporte técnico
- ✅ Ofrecer soporte gratuito los primeros meses
- ✅ Mejorar autoservicio (FAQs, tutoriales)

### 4. OnlineSecurity (Seguridad Online)

**Importancia:** Media (3.98%)

**Hallazgos:**

- `OnlineSecurity_No`: Importancia 0.0398 → **Aumenta churn**
- Similar a TechSupport

**Acción:**

- ✅ Bundling: Ofrecer paquetes con seguridad incluida
- ✅ Educar sobre importancia de seguridad online

### 5. PaymentMethod (Método de Pago)

**Importancia:** Media-Baja (3.12%)

**Hallazgos:**

- `PaymentMethod_Electronic check`: Importancia 0.0312 → **Aumenta churn**
- Método menos conveniente

**Acción:**

- ✅ Promover pagos automáticos (tarjeta, transferencia)
- ✅ Ofrecer descuentos por pago automático
- ✅ Simplificar proceso de cambio de método de pago

### 6. PaperlessBilling (Facturación Sin Papel)

**Importancia:** Media-Baja (2.87%)

**Hallazgos:**

- `PaperlessBilling_Yes`: Importancia 0.0287 → **Aumenta churn**
- Correlación, no necesariamente causalidad

**Acción:**

- ⚠️ No forzar facturación digital
- ✅ Ofrecer ambas opciones
- ✅ Mejorar experiencia de facturación digital

---

## 🎯 Código Completo para Obtener Variables Categóricas Importantes

### Script Completo

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# ============================================
# MÉTODO 1: ANÁLISIS EXPLORATORIO (EDA)
# ============================================

# Paso 1: Identificar variables categóricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('customerID')
categorical_cols.remove('Churn')

# Paso 2: Seleccionar variables importantes
important_cats = ['Contract', 'InternetService', 'PaymentMethod',
                  'TechSupport', 'OnlineSecurity', 'PaperlessBilling']

# Paso 3: Calcular tasa de churn por categoría
print("\n" + "="*80)
print("MÉTODO 1: ANÁLISIS EXPLORATORIO")
print("="*80)

for col in important_cats:
    print(f"\n{col}:")
    churn_rate = df.groupby(col)['Churn'].apply(
        lambda x: (x=='Yes').sum()/len(x)*100
    )
    print(churn_rate.sort_values(ascending=False))

# ============================================
# MÉTODO 2: FEATURE IMPORTANCE DEL MODELO
# ============================================

# Paso 1: Entrenar modelo (asumiendo que ya tienes X_train, y_train)
best_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    random_state=42
)
best_rf.fit(X_train_balanced, y_train_balanced)

# Paso 2: Obtener feature importance
feature_importance = best_rf.feature_importances_
feature_names = list(X_train_balanced.columns)

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

# Paso 3: Filtrar solo variables categóricas
# (Asumiendo que las categóricas tienen "_" después de OneHotEncoding)
categorical_importance = importance_df[
    importance_df['Feature'].str.contains('_')
].head(10)

print("\n" + "="*80)
print("MÉTODO 2: FEATURE IMPORTANCE DEL MODELO")
print("="*80)
print("\nTop 10 Variables Categóricas Más Importantes:\n")
print(categorical_importance.to_string(index=False))

# Paso 4: Visualizar
plt.figure(figsize=(12, 8))
plt.barh(range(len(categorical_importance)),
         categorical_importance['Importance'],
         color=plt.cm.viridis(np.linspace(0, 1, len(categorical_importance))))
plt.yticks(range(len(categorical_importance)),
           categorical_importance['Feature'])
plt.xlabel('Importancia')
plt.title('Top 10 Variables Categóricas Más Importantes')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 🚀 Resumen Ejecutivo

### ¿Cómo se obtienen las variables categóricas más importantes?

**Dos métodos principales:**

1. **Análisis Exploratorio (EDA):**
   - Calcular tasa de churn por cada categoría
   - Visualizar con gráficos de barras
   - Identificar categorías con mayor/menor churn

2. **Feature Importance del Modelo:**
   - Entrenar Random Forest
   - Obtener `.feature_importances_`
   - Filtrar variables categóricas (las que tienen "_")
   - Ordenar por importancia

### Top 5 Variables Categóricas Más Importantes

1. **Contract** (15.30% combinado) → Tipo de contrato
2. **InternetService** (5.43%) → Tipo de internet
3. **TechSupport** (4.21%) → Soporte técnico
4. **OnlineSecurity** (3.98%) → Seguridad online
5. **PaymentMethod** (3.12%) → Método de pago

### Acciones Clave

- ✅ **Promover contratos largos** (anual/bianual)
- ✅ **Ofrecer soporte técnico** y seguridad online
- ✅ **Revisar precios** de fibra óptica
- ✅ **Incentivar pagos automáticos**
- ✅ **Mejorar experiencia** de clientes nuevos (tenure bajo)

¡Y listo! Ahora sabes cómo identificar las variables categóricas más importantes. 🎉


