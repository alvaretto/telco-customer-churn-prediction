# Bloque 2: Importación de Librerías

## 📋 Descripción General

Este bloque es como **preparar la caja de herramientas** antes de comenzar un trabajo. Importa todas las librerías (bibliotecas de código) necesarias para realizar el análisis de datos, crear visualizaciones, entrenar modelos y evaluar resultados.

---

## 🎯 Propósito y Objetivo

El objetivo de este bloque es:

1. **Importar todas las herramientas necesarias** para el proyecto
2. **Configurar el entorno de trabajo** (suprimir advertencias, configurar visualizaciones)
3. **Verificar que todo está listo** para comenzar el análisis

### ¿Por qué es importante?

**Analogía del carpintero**: Imagina que eres un carpintero que va a construir una mesa. 
Antes de empezar, necesitas sacar del taller:

- El martillo (para clavar)
- La sierra (para cortar)
- El nivel (para medir)
- El taladro (para perforar)

De la misma manera, este bloque "saca del taller" todas las herramientas de 
software que necesitaremos.

---

## 🔑 Conceptos Clave y Librerías Importadas

### 1. **Librerías de Manipulación de Datos**

#### **NumPy** (`import numpy as np`)
- **¿Qué hace?** Maneja operaciones matemáticas y arrays numéricos
- **Analogía**: Es como una calculadora científica súper potente
- **Uso en el proyecto**: Cálculos matemáticos, manejo de valores faltantes (NaN)

#### **Pandas** (`import pandas as pd`)
- **¿Qué hace?** Manipula y analiza datos en formato de tablas (DataFrames)
- **Analogía**: Es como Excel pero con superpoderes
- **Uso en el proyecto**: Cargar el CSV, limpiar datos, crear nuevas columnas

---

### 2. **Librerías de Visualización**

#### **Matplotlib** (`import matplotlib.pyplot as plt`)
- **¿Qué hace?** Crea gráficos básicos (líneas, barras, dispersión)
- **Analogía**: Es como un lienzo y pinceles para pintar gráficos
- **Uso en el proyecto**: Crear visualizaciones personalizadas

#### **Seaborn** (`import seaborn as sns`)
- **¿Qué hace?** Crea gráficos estadísticos más elegantes y complejos
- **Analogía**: Es como Matplotlib pero con plantillas profesionales pre-diseñadas
- **Uso en el proyecto**: Gráficos de distribución, correlaciones, comparaciones

---

### 3. **Librerías de Preprocesamiento**

#### **train_test_split**
- **¿Qué hace?** Divide los datos en conjuntos de entrenamiento y prueba
- **Analogía**: Como dividir un mazo de cartas en dos grupos: uno para practicar y otro para el examen final

#### **StandardScaler**
- **¿Qué hace?** Normaliza los datos para que estén en la misma escala
- **Analogía**: Como convertir todas las medidas a la misma unidad (metros en vez de mezclar metros, centímetros y kilómetros)

#### **LabelEncoder**
- **¿Qué hace?** Convierte categorías de texto en números
- **Analogía**: Como asignar números a colores (Rojo=1, Azul=2, Verde=3)

#### **ColumnTransformer y Pipeline**
- **¿Qué hace?** Crea flujos de trabajo automatizados para procesar datos
- **Analogía**: Como una línea de ensamblaje en una fábrica donde cada estación hace una tarea específica

---

### 4. **Librerías de Modelos de Machine Learning**

#### **Logistic Regression** (Regresión Logística)
- **¿Qué hace?** Modelo simple para clasificación binaria (Sí/No)
- **Analogía**: Como trazar una línea para separar dos grupos

#### **Decision Tree** (Árbol de Decisión)
- **¿Qué hace?** Toma decisiones siguiendo una serie de preguntas
- **Analogía**: Como un diagrama de flujo de "si esto, entonces aquello"

#### **Random Forest** (Bosque Aleatorio)
- **¿Qué hace?** Combina muchos árboles de decisión
- **Analogía**: Como pedir opinión a 100 expertos y tomar la decisión por mayoría

#### **Gradient Boosting**
- **¿Qué hace?** Construye modelos secuencialmente, cada uno corrigiendo errores del anterior
- **Analogía**: Como un estudiante que aprende de sus errores en cada examen de práctica

#### **SVC** (Support Vector Classifier)
- **¿Qué hace?** Encuentra el mejor límite para separar clases
- **Analogía**: Como encontrar la mejor valla para separar dos rebaños de ovejas

#### **KNeighbors** (K-Vecinos Más Cercanos)
- **¿Qué hace?** Clasifica basándose en los vecinos más cercanos
- **Analogía**: "Dime con quién andas y te diré quién eres"

#### **XGBoost**
- **¿Qué hace?** Versión optimizada y potente de Gradient Boosting
- **Analogía**: Como Gradient Boosting pero con turbo

---

### 5. **Librerías de Métricas de Evaluación**

Estas herramientas miden qué tan bien funcionan nuestros modelos:

- **accuracy_score**: ¿Cuántas predicciones fueron correctas?
- **precision_score**: De las predicciones positivas, ¿cuántas fueron correctas?
- **recall_score**: De todos los casos positivos reales, ¿cuántos detectamos?
- **f1_score**: Balance entre precisión y recall
- **confusion_matrix**: Tabla que muestra aciertos y errores
- **roc_auc_score**: Mide la capacidad de discriminación del modelo

**Analogía del detector de metales**:
- **Accuracy**: ¿Cuántas veces acertó en total?
- **Precision**: Cuando pita, ¿realmente hay metal?
- **Recall**: De todos los metales enterrados, ¿cuántos encontró?

---

### 6. **Librerías para Manejo de Desbalanceo**

#### **SMOTE** (Synthetic Minority Over-sampling Technique)
- **¿Qué hace?** Crea ejemplos sintéticos de la clase minoritaria
- **Analogía**: Si tienes 100 fotos de gatos y solo 10 de perros, SMOTE crea más fotos de perros (sintéticas) para balancear

#### **RandomOverSampler**
- **¿Qué hace?** Duplica aleatoriamente ejemplos de la clase minoritaria
- **Analogía**: Fotocopiar las 10 fotos de perros varias veces

#### **RandomUnderSampler**
- **¿Qué hace?** Reduce ejemplos de la clase mayoritaria
- **Analogía**: Eliminar algunas de las 100 fotos de gatos para igualar

---

### 7. **Librerías de Optimización**

#### **GridSearchCV**
- **¿Qué hace?** Prueba todas las combinaciones posibles de parámetros
- **Analogía**: Como probar todas las combinaciones de una cerradura hasta encontrar la correcta

#### **RandomizedSearchCV**
- **¿Qué hace?** Prueba combinaciones aleatorias de parámetros (más rápido)
- **Analogía**: En vez de probar todas las combinaciones, prueba algunas al azar

---

## 🎨 Configuración de Visualización

El bloque también configura cómo se verán los gráficos:

```python
plt.style.use('seaborn-v0_8-darkgrid')  # Estilo visual
sns.set_palette("husl")                  # Paleta de colores
plt.rcParams['figure.figsize'] = (12, 6) # Tamaño de gráficos
plt.rcParams['font.size'] = 10           # Tamaño de letra
```

**Analogía**: Como configurar el tema de tu teléfono (modo oscuro, colores, tamaño de letra).

---

## 🔗 Relación con el Análisis General

Este bloque es **fundamental** porque:

1. **Sin estas herramientas, no podríamos hacer nada** - Es como intentar cocinar sin utensilios
2. **Establece el entorno de trabajo** - Todo lo que viene después depende de estas importaciones
3. **Organiza las herramientas por categoría** - Facilita encontrar lo que necesitamos

---

## 💡 Puntos Clave para Recordar

1. Las **librerías son herramientas** que nos ahorran escribir código desde cero
2. Cada librería tiene un **propósito específico** (datos, visualización, modelos, métricas)
3. La **configuración inicial** asegura que todo funcione correctamente
4. Este bloque es **preparación**, no análisis - Es como afilar los cuchillos antes de cocinar

---

## 🎓 Conclusión

Este bloque prepara todo el arsenal de herramientas que necesitaremos. Es breve pero crítico: sin él, ningún análisis posterior sería posible. Es la base técnica sobre la que se construye todo el proyecto.

**Siguiente paso**: Cargar los datos y hacer una exploración inicial.

