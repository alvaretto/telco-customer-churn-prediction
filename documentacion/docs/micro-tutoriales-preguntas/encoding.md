## 📊 CONVERSIÓN DE VARIABLES CATEGÓRICAS A NUMÉRICAS - Proyecto Telco Churn

Basándome en el análisis del notebook `Telco_Customer_Churn.ipynb`, aquí está el 
detalle completo del proceso de encoding:

---

### 1️⃣ **VARIABLES CATEGÓRICAS IDENTIFICADAS (16 variables)**

El proyecto identificó **16 variables categóricas** que necesitaban ser transformadas:

```python
# Características categóricas (16):
categorical_features = [
    'gender',           # Género: Male, Female
    'Partner',          # Pareja: Yes, No
    'Dependents',       # Dependientes: Yes, No
    'PhoneService',     # Servicio telefónico: Yes, No
    'MultipleLines',    # Múltiples líneas: Yes, No, No phone service
    'InternetService',  # Internet: DSL, Fiber optic, No
    'OnlineSecurity',   # Seguridad online: Yes, No, No internet service
    'OnlineBackup',     # Respaldo online: Yes, No, No internet service
    'DeviceProtection', # Protección: Yes, No, No internet service
    'TechSupport',      # Soporte técnico: Yes, No, No internet service
    'StreamingTV',      # Streaming TV: Yes, No, No internet service
    'StreamingMovies',  # Streaming películas: Yes, No, No internet service
    'Contract',         # Contrato: Month-to-month, One year, Two year
    'PaperlessBilling', # Facturación: Yes, No
    'PaymentMethod',    # Método de pago: Electronic check, Mailed check,
                        #                  Bank transfer (automatic),
                        #                  Credit card (automatic)
    'TenureGroup'       # Grupo de antigüedad: 0-1 año, 1-2 años, 2-4 años, 4+ años
]
```

---

### 2️⃣ **MÉTODO DE ENCODING UTILIZADO: OneHotEncoder**

El proyecto utilizó **OneHotEncoder de scikit-learn** con configuración específica:

```python
from sklearn.preprocessing import OneHotEncoder

# Crear transformador categórico
categorical_transformer = OneHotEncoder(
    drop='first',              # Elimina la primera categoría para evitar multicolinealidad
    sparse_output=False,       # Retorna array denso en lugar de sparse
    handle_unknown='ignore'    # Ignora categorías desconocidas en producción
)
```

---

### 3️⃣ **PIPELINE DE PREPROCESAMIENTO COMPLETO**

Se utilizó **ColumnTransformer** para aplicar diferentes transformaciones a
variables numéricas y categóricas:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Crear transformadores
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')

# Crear preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),    # 9 variables numéricas
        ('cat', categorical_transformer, categorical_features)  # 16 variables categóricas
    ])

# Ajustar y transformar datos
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
```

---

### 4️⃣ **TRANSFORMACIÓN DE LA VARIABLE OBJETIVO (Churn)**

La variable objetivo se transformó usando **map()**:

```python
# Convertir Churn de categórica a binaria
y = df_model['Churn'].map({'Yes': 1, 'No': 0})

# Resultado:
# 'Yes' → 1 (Cliente abandonó)
# 'No'  → 0 (Cliente se quedó)
```

---

### 5️⃣ **MANEJO DE CATEGORÍAS ESPECIALES**

#### **Categorías "No internet service" y "No phone service"**

Estas categorías se manejaron **automáticamente** por OneHotEncoder:

**Ejemplo con `OnlineSecurity`:**

- Categorías originales: `['Yes', 'No', 'No internet service']`
- Después de OneHotEncoder (drop='first'):

  - `OnlineSecurity_No` → 1 si es 'No', 0 si no
  - `OnlineSecurity_No internet service` → 1 si es 'No internet service', 0 si no
  - `OnlineSecurity_Yes` se infiere cuando ambas son 0

**Ejemplo con `MultipleLines`:**

- Categorías originales: `['Yes', 'No', 'No phone service']`
- Después de OneHotEncoder:

  - `MultipleLines_No` → 1 si es 'No', 0 si no
  - `MultipleLines_No phone service` → 1 si es 'No phone service', 0 si no
  - `MultipleLines_Yes` se infiere cuando ambas son 0

---

### 6️⃣ **RESULTADO FINAL DEL ENCODING**

Después del preprocesamiento:

```
Dimensiones originales: (7043, 25)
  - 9 variables numéricas
  - 16 variables categóricas

Dimensiones después del encoding: (7043, 39)
  - 9 variables numéricas (escaladas con StandardScaler)
  - 30 variables categóricas (expandidas con OneHotEncoder)
  
Total: 39 características
```

---

### 7️⃣ **VARIABLES ORDINALES VS NOMINALES**

El proyecto **NO utilizó técnicas especiales** para distinguir entre variables ordinales y nominales. Todas las variables categóricas se trataron como **nominales** usando OneHotEncoder.

#### **Variables que podrían considerarse ordinales:**

- `Contract`: Month-to-month < One year < Two year
- `TenureGroup`: 0-1 año < 1-2 años < 2-4 años < 4+ años

**Razón para usar OneHotEncoder en todas:**

- OneHotEncoder es más seguro y no asume orden
- El modelo (RandomForest) puede aprender relaciones complejas sin necesidad de encoding ordinal
- Evita introducir sesgos de orden artificial

---

### 8️⃣ **ENCODING ADICIONAL PARA ANÁLISIS EXPLORATORIO**

Durante el análisis exploratorio (EDA), se usó **map()** para convertir variables binarias temporalmente:

```python
# Solo para análisis de correlación (no para el modelo final)
binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
for col in binary_cols:
    if col in df_corr.columns:
        df_corr[col] = df_corr[col].map({
            'Yes': 1, 'No': 0,      # Variables Yes/No
            'Male': 1, 'Female': 0   # Variable gender
        })
```

**Nota:** Este encoding fue **solo para visualización** de correlaciones, no se usó en el modelo final.

---

### 9️⃣ **EJEMPLO COMPLETO DE TRANSFORMACIÓN**

#### **Antes del Encoding:**
```python
# Registro original
{
    'gender': 'Female',
    'Partner': 'Yes',
    'InternetService': 'Fiber optic',
    'Contract': 'Month-to-month',
    'PaymentMethod': 'Electronic check',
    'OnlineSecurity': 'No',
    'MultipleLines': 'No phone service'
}
```

#### **Después del OneHotEncoder (drop='first'):**
```python
# Variables expandidas (solo algunas como ejemplo)
{
    'gender_Male': 0,                              # Female es la categoría base
    'Partner_Yes': 1,                              # Yes
    'InternetService_Fiber optic': 1,              # Fiber optic
    'InternetService_No': 0,                       # No es 'No'
    'Contract_One year': 0,                        # No es One year
    'Contract_Two year': 0,                        # No es Two year (Month-to-month es base)
    'PaymentMethod_Electronic check': 1,           # Electronic check
    'PaymentMethod_Mailed check': 0,               # No
    'PaymentMethod_Bank transfer (automatic)': 0,  # No
    'OnlineSecurity_No': 1,                        # No
    'OnlineSecurity_No internet service': 0,       # No
    'MultipleLines_No': 0,                         # No
    'MultipleLines_No phone service': 1            # Sí
}
```

---

### 🔟 **VENTAJAS DEL MÉTODO UTILIZADO**

✅ **OneHotEncoder con drop='first':**

1. **Evita multicolinealidad** (dummy variable trap)
2. **Maneja categorías desconocidas** en producción (`handle_unknown='ignore'`)
3. **Consistente** entre entrenamiento y producción
4. **Integrado en pipeline** de scikit-learn (fácil de guardar y cargar)

✅ **ColumnTransformer:**

1. **Aplica transformaciones diferentes** a variables numéricas y categóricas
2. **Mantiene el orden** de las características
3. **Fácil de serializar** con joblib/pickle

---

### 📋 **RESUMEN TÉCNICO**

| Aspecto | Detalle |
|---------|---------|
| **Método principal** | OneHotEncoder (scikit-learn) |
| **Variables categóricas** | 16 variables |
| **Características finales** | 39 (9 numéricas + 30 categóricas expandidas) |
| **Manejo de "No service"** | Automático por OneHotEncoder |
| **Variables ordinales** | Tratadas como nominales (OneHotEncoder) |
| **Variable objetivo** | map({'Yes': 1, 'No': 0}) |
| **Pipeline** | ColumnTransformer + StandardScaler + OneHotEncoder |
| **Serialización** | preprocessor.pkl (guardado con joblib) |

---

### 💡 **CÓDIGO PARA REPLICAR EL ENCODING**

Si quieres replicar el encoding exacto usado en el proyecto:

```python
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# 1. Definir variables
numeric_features = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 
                    'ChargeRatio', 'AvgMonthlyCharges', 'TotalServices', 
                    'SeniorWithDependents', 'HighValueContract']

categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 
                        'MultipleLines', 'InternetService', 'OnlineSecurity', 
                        'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                        'StreamingTV', 'StreamingMovies', 'Contract', 
                        'PaperlessBilling', 'PaymentMethod', 'TenureGroup']

# 2. Crear preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), 
         categorical_features)
    ])

# 3. Ajustar y transformar
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# 4. Guardar preprocessor
import joblib
joblib.dump(preprocessor, 'preprocessor.pkl')
```

---

¿Necesitas más detalles sobre algún aspecto específico del encoding o quieres ver cómo se aplica en la API de producción?
