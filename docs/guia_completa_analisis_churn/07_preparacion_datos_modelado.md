# Bloque 7: Preparación de Datos para Modelado

## 📋 Descripción General

Este bloque es como **preparar los ingredientes antes de cocinar**. Tenemos los 
datos limpios y las features creadas, pero ahora necesitamos transformarlos al 
formato exacto que los algoritmos de Machine Learning requieren.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Separar variables predictoras (X) de la variable objetivo (y)**
2. **Dividir datos en conjuntos de entrenamiento y prueba**
3. **Codificar variables categóricas** en formato numérico
4. **Normalizar variables numéricas** a la misma escala
5. **Crear un pipeline de preprocesamiento** automatizado

### ¿Por qué es importante?

**Analogía del examen**: Imagina que vas a tomar un examen:
- **Entrenamiento**: Estudias con ejercicios de práctica
- **Prueba**: Tomas el examen real con preguntas nuevas

Si estudias con las mismas preguntas del examen, memorizarás las respuestas pero 
no aprenderás realmente. Por eso separamos los datos.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **Separación de Variables (X e y)**

```python
X = df_model.drop(['Churn', 'customerID'], axis=1)
y = df_model['Churn'].map({'Yes': 1, 'No': 0})
```

**¿Qué hace esto?**

- **X**: Variables predictoras (features) - todo excepto Churn y customerID
- **y**: Variable objetivo - Churn convertido a 1 (Yes) y 0 (No)

**¿Por qué eliminar customerID?**

- Es solo un identificador único, no tiene poder predictivo
- Sería como usar el número de cédula para predecir si alguien se enferma

**Analogía**: X son las pistas que el detective tiene, y es el culpable que debe descubrir.

---

### 2. **División Train/Test (80/20)**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
```

**Parámetros importantes**:

#### **test_size=0.20**

- 80% de datos para entrenar
- 20% de datos para probar
- **Analogía**: De 100 problemas de matemáticas, practicas con 80 y te evalúan con 20 nuevos

#### **random_state=42**

- Fija la semilla aleatoria para reproducibilidad
- Siempre obtendremos la misma división
- **Analogía**: Como usar la misma baraja de cartas mezclada de la misma forma cada vez

#### **stratify=y**

- Mantiene la misma proporción de churn en train y test
- Si hay 27% de churn en total, habrá ~27% en train y ~27% en test
- **Analogía**: Si una clase tiene 30% niños y 70% niñas, al dividir en grupos 
mantienes esa proporción

**¿Por qué es crítico?**

- **Sin stratify**: Podrías tener 40% churn en train y 10% en test (desbalance)
- **Con stratify**: Ambos conjuntos son representativos

---

### 3. **Identificación de Tipos de Variables**

```python
categorical_features = X_train.select_dtypes(include=['object']).columns.tolist()
numerical_features = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
```

**¿Por qué separar?**

- Variables categóricas y numéricas requieren transformaciones diferentes
- **Categóricas**: Necesitan codificación (texto → números)
- **Numéricas**: Necesitan normalización (misma escala)

---

### 4. **Codificación de Variables Categóricas (One-Hot Encoding)**

```python
OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore')
```

**¿Qué es One-Hot Encoding?**

Convierte categorías en columnas binarias (0 o 1).

**Ejemplo con InternetService**:

- Original: ['DSL', 'Fiber optic', 'No']
- Después de One-Hot:

  - `InternetService_Fiber optic`: 1 si es Fiber, 0 si no
  - `InternetService_No`: 1 si es No, 0 si no
  - (DSL se infiere cuando ambas son 0)

**Parámetros**:

- **drop='first'**: Elimina la primera categoría para evitar multicolinealidad
- **sparse=False**: Retorna array denso (más fácil de manejar)
- **handle_unknown='ignore'**: Si aparece una categoría nueva en test, la ignora

**Analogía**: Es como tener casillas de verificación:

- ☐ DSL
- ☐ Fiber optic  
- ☐ No internet

Marcas la que aplica (1) y dejas las demás vacías (0).

---

### 5. **Normalización de Variables Numéricas (StandardScaler)**

```python
StandardScaler()
```

**¿Qué hace StandardScaler?**

Transforma los datos para que tengan:

- **Media = 0**
- **Desviación estándar = 1**

**Fórmula**: `(valor - media) / desviación_estándar`

**¿Por qué es necesario?**

**Problema sin normalización**:

- `tenure`: rango 0-72
- `MonthlyCharges`: rango 18-118
- `TotalCharges`: rango 0-8,000+

Algunos algoritmos (como SVM, KNN) son sensibles a la escala. Sin normalización, 
`TotalCharges` dominaría porque tiene valores mucho más grandes.

**Analogía**: Es como convertir todas las medidas a la misma unidad antes de 
compararlas:

- Altura: metros
- Peso: kilogramos
- Edad: años

Sin normalización sería como comparar metros con milímetros (los milímetros siempre parecerían más importantes por ser números más grandes).

---

### 6. **Pipeline de Preprocesamiento**

```python
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(...), categorical_features)
    ]
)
```

**¿Qué es un Pipeline?**

Un flujo de trabajo automatizado que aplica transformaciones en orden.

**Ventajas**:

1. **Automatización**: Aplica todas las transformaciones con un solo comando
2. **Consistencia**: Las mismas transformaciones se aplican a train y test
3. **Previene data leakage**: No usa información de test para transformar train
4. **Reproducibilidad**: Fácil de replicar

**Analogía**: Es como una línea de ensamblaje en una fábrica:

- Estación 1: Normalizar números
- Estación 2: Codificar categorías
- Producto final: Datos listos para el modelo

---

### 7. **Aplicación del Preprocesamiento**

```python
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
```

**Diferencia crítica**:

- **fit_transform** en train: Aprende los parámetros (media, desviación) Y transforma
- **transform** en test: Solo transforma usando los parámetros aprendidos de train

**¿Por qué esta diferencia?**

**Analogía del profesor**: 

- El profesor (preprocessor) aprende de los estudiantes de práctica (train)
- Luego aplica lo aprendido a los estudiantes del examen (test)
- NO debe aprender nada de los estudiantes del examen (evita data leakage)

---

## 📊 Resultado de la Preparación

**Antes**:

- Variables categóricas como texto
- Variables numéricas en diferentes escalas
- Todo en un solo DataFrame

**Después**:

- Todo convertido a números
- Variables normalizadas (media=0, std=1)
- Listo para alimentar a los modelos

**Dimensiones**:

- **X_train**: ~5,634 filas (80%)
- **X_test**: ~1,409 filas (20%)
- **Columnas**: Aumentan por One-Hot Encoding

---

## 🔗 Relación con el Análisis General

Este bloque es el **último paso antes del modelado**:

1. **Cierra el preprocesamiento**: Datos completamente listos
2. **Previene errores comunes**: Data leakage, escalas incorrectas
3. **Optimiza el rendimiento**: Modelos funcionan mejor con datos normalizados
4. **Facilita la evaluación**: División train/test permite medir rendimiento real

---

## 💡 Puntos Clave para Recordar

1. **División 80/20** con stratify para mantener proporciones
2. **One-Hot Encoding** para variables categóricas
3. **StandardScaler** para variables numéricas
4. **Pipeline** automatiza y asegura consistencia
5. **fit_transform** en train, **transform** en test (evita data leakage)
6. **random_state=42** para reproducibilidad

---

## 🎓 Conclusión

La preparación de datos es como preparar el escenario antes de una obra de teatro: todo debe estar en su lugar, con el formato correcto y listo para la acción. Un preprocesamiento adecuado es la diferencia entre un modelo que funciona y uno que falla.

**Siguiente paso**: Entrenar múltiples modelos baseline y comparar su rendimiento.

