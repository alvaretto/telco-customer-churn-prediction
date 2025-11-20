# Bloque 10: Optimización de Hiperparámetros

## 📋 Descripción General

Este bloque es como **afinar un instrumento musical** para que suene perfecto. Los modelos tienen "perillas" (hiperparámetros) que controlan su comportamiento. Aquí buscamos la mejor combinación de configuraciones para maximizar el rendimiento del modelo.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Identificar el mejor modelo** de los candidatos anteriores
2. **Definir un espacio de búsqueda** de hiperparámetros
3. **Aplicar GridSearchCV o RandomizedSearchCV** para encontrar la mejor configuración
4. **Evaluar el modelo optimizado** y comparar con el baseline
5. **Seleccionar el modelo final** para producción

### ¿Por qué es importante?

**Analogía del café**: Hacer café perfecto requiere ajustar:
- Temperatura del agua
- Tiempo de extracción
- Cantidad de café
- Molienda

Cambiar cualquiera de estos parámetros afecta el sabor final. Lo mismo pasa con los modelos de ML.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **¿Qué son los Hiperparámetros?**

**Hiperparámetros** son configuraciones que se establecen ANTES del entrenamiento y controlan cómo aprende el modelo.

**Diferencia con parámetros**:
- **Parámetros**: El modelo los aprende de los datos (ej: pesos en regresión)
- **Hiperparámetros**: Los definimos nosotros (ej: profundidad de un árbol)

**Analogía del estudiante**:
- **Parámetros**: El conocimiento que adquiere estudiando
- **Hiperparámetros**: Cuántas horas estudia, qué técnica usa, en qué ambiente

---

### 2. **Hiperparámetros Comunes por Modelo**

#### **Random Forest**

```python
param_grid = {
    'n_estimators': [100, 200, 300],      # Número de árboles
    'max_depth': [10, 20, 30, None],      # Profundidad máxima
    'min_samples_split': [2, 5, 10],      # Mínimo para dividir nodo
    'min_samples_leaf': [1, 2, 4],        # Mínimo en hoja
    'max_features': ['sqrt', 'log2']      # Features por split
}
```

**Explicación**:

- **n_estimators**: Más árboles = más robusto pero más lento
  - **Analogía**: Más jueces en un panel = decisión más confiable
  
- **max_depth**: Controla cuán profundo puede crecer cada árbol
  - **Analogía**: Cuántos niveles de preguntas puede hacer
  - Muy profundo = overfitting, muy superficial = underfitting
  
- **min_samples_split**: Mínimo de ejemplos para dividir un nodo
  - **Analogía**: No dividir un grupo si es muy pequeño
  - Previene overfitting
  
- **min_samples_leaf**: Mínimo de ejemplos en cada hoja
  - **Analogía**: Cada conclusión debe basarse en al menos X casos
  
- **max_features**: Cuántas features considerar en cada split
  - **sqrt**: Raíz cuadrada del total (más diversidad)
  - **log2**: Logaritmo base 2 (más conservador)

---

#### **XGBoost**

```python
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.8, 0.9, 1.0],
    'colsample_bytree': [0.8, 0.9, 1.0],
    'gamma': [0, 0.1, 0.2]
}
```

**Explicación**:

- **learning_rate**: Qué tan rápido aprende el modelo
  - **Analogía**: Tamaño del paso al caminar
  - Bajo (0.01) = lento pero preciso
  - Alto (0.3) = rápido pero puede pasarse
  
- **subsample**: Fracción de datos usados en cada árbol
  - **Analogía**: Usar una muestra aleatoria para cada decisión
  - Previene overfitting
  
- **colsample_bytree**: Fracción de features usadas por árbol
  - Similar a max_features en Random Forest
  
- **gamma**: Reducción mínima de pérdida para hacer un split
  - **Analogía**: Cuánto debe mejorar una pregunta para hacerla
  - Mayor gamma = modelo más conservador

---

### 3. **GridSearchCV vs. RandomizedSearchCV**

#### **GridSearchCV (Búsqueda Exhaustiva)**

**¿Cómo funciona?**
- Prueba TODAS las combinaciones posibles de hiperparámetros

**Ejemplo**:
```python
n_estimators: [100, 200]
max_depth: [10, 20]
```
Combinaciones: 2 × 2 = 4 pruebas

**Ventajas**:
- ✅ Garantiza encontrar la mejor combinación en el espacio definido
- ✅ Exhaustivo

**Desventajas**:
- ❌ Muy lento con muchos parámetros
- ❌ Crece exponencialmente

**Analogía**: Probar todas las combinaciones de ropa en tu armario.

---

#### **RandomizedSearchCV (Búsqueda Aleatoria)**

**¿Cómo funciona?**
- Prueba un número fijo de combinaciones aleatorias

**Ejemplo**:
```python
n_estimators: [100, 200, 300, 400, 500]
max_depth: [5, 10, 15, 20, 25, 30]
learning_rate: [0.01, 0.05, 0.1, 0.15, 0.2]
```
Combinaciones posibles: 5 × 6 × 5 = 150
Pero solo prueba, por ejemplo, 30 aleatorias

**Ventajas**:
- ✅ Mucho más rápido
- ✅ Puede explorar espacios grandes
- ✅ Sorprendentemente efectivo

**Desventajas**:
- ❌ No garantiza encontrar el óptimo absoluto
- ❌ Resultados pueden variar entre ejecuciones

**Analogía**: Probar 20 combinaciones aleatorias de ropa en vez de todas.

---

### 4. **Validación Cruzada (Cross-Validation)**

Tanto GridSearchCV como RandomizedSearchCV usan **validación cruzada** para evaluar cada combinación.

**¿Qué es CV=5?**

Divide los datos de entrenamiento en 5 partes (folds):

```
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
Fold 4: [Train] [Train] [Train] [Test] [Train]
Fold 5: [Train] [Train] [Train] [Train] [Test]
```

**Proceso**:
1. Entrena con 4 folds, evalúa en 1
2. Repite 5 veces (cada fold es test una vez)
3. Promedia los resultados

**Ventajas**:
- ✅ Usa todos los datos para entrenar y evaluar
- ✅ Resultados más robustos
- ✅ Reduce varianza de la evaluación

**Analogía**: En vez de un solo examen, tomas 5 exámenes diferentes y promedias la nota.

---

### 5. **Proceso de Optimización**

```python
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,
    verbose=2
)

grid_search.fit(X_train_balanced, y_train_balanced)
best_model = grid_search.best_estimator_
```

**Parámetros importantes**:

- **estimator**: El modelo a optimizar
- **param_grid**: Espacio de búsqueda
- **cv=5**: 5-fold cross-validation
- **scoring='f1'**: Métrica a optimizar (F1-Score)
- **n_jobs=-1**: Usa todos los cores del CPU (paralelización)
- **verbose=2**: Muestra progreso detallado

**Resultado**:
- **best_estimator_**: Modelo con los mejores hiperparámetros
- **best_params_**: Diccionario con la mejor configuración
- **best_score_**: Mejor score obtenido en CV

---

## 📊 Resultados Típicos de la Optimización

### **Antes de Optimización (Baseline con SMOTE)**

| Modelo | F1-Score | Recall | Precision |
|--------|----------|--------|-----------|
| Random Forest | 0.71 | 0.78 | 0.65 |
| XGBoost | 0.73 | 0.80 | 0.67 |

### **Después de Optimización**

| Modelo | F1-Score | Recall | Precision |
|--------|----------|--------|-----------|
| Random Forest | 0.75 | 0.82 | 0.69 |
| XGBoost | 0.77 | 0.84 | 0.71 |

**Mejora**: ~4-5% en todas las métricas

---

### **Mejores Hiperparámetros Encontrados (Ejemplo)**

**XGBoost**:
```python
{
    'n_estimators': 200,
    'max_depth': 5,
    'learning_rate': 0.1,
    'subsample': 0.9,
    'colsample_bytree': 0.9,
    'gamma': 0.1
}
```

**Interpretación**:
- 200 árboles (balance entre rendimiento y velocidad)
- Profundidad moderada (5) para evitar overfitting
- Learning rate moderado (0.1) para convergencia estable
- Subsample y colsample altos (0.9) para usar la mayoría de datos/features
- Gamma bajo (0.1) para permitir splits útiles

---

## 🔗 Relación con el Análisis General

Este bloque es el **refinamiento final**:

1. **Maximiza el rendimiento**: Exprime el último % de mejora
2. **Selecciona el modelo final**: El que irá a producción
3. **Documenta la configuración**: Reproducibilidad
4. **Valida robustez**: CV asegura que no es suerte

---

## 💡 Puntos Clave para Recordar

1. **Hiperparámetros** controlan cómo aprende el modelo
2. **GridSearchCV**: Exhaustivo pero lento
3. **RandomizedSearchCV**: Rápido y efectivo para espacios grandes
4. **Cross-Validation (CV=5)**: Evaluación robusta
5. **Mejora típica**: 3-5% sobre baseline
6. **Scoring='f1'**: Optimizamos F1-Score (balance precision/recall)

---

## 🎓 Conclusión

La optimización de hiperparámetros es como ajustar la receta perfecta: pequeños cambios en los ingredientes pueden hacer una gran diferencia. No siempre da mejoras dramáticas, pero ese 3-5% extra puede ser la diferencia entre un modelo bueno y uno excelente.

**Siguiente paso**: Evaluación detallada del mejor modelo con análisis de errores, curvas ROC, feature importance y recomendaciones de negocio.

