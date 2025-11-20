# Bloque 8: Entrenamiento de Modelos Baseline

## 📋 Descripción General

Este bloque es como **una competencia deportiva donde varios atletas compiten** para ver quién es el mejor. Entrenamos múltiples algoritmos de Machine Learning diferentes y comparamos su rendimiento para identificar cuáles funcionan mejor para predecir el churn.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Entrenar múltiples modelos** con configuraciones por defecto (baseline)
2. **Evaluar el rendimiento** de cada modelo con métricas apropiadas
3. **Comparar resultados** para identificar los mejores candidatos
4. **Establecer una línea base** de rendimiento antes de optimizar

### ¿Por qué probar múltiples modelos?

**Analogía del transporte**: Si necesitas ir de A a B, podrías usar:
- Bicicleta (rápida para distancias cortas)
- Auto (versátil)
- Tren (eficiente para largas distancias)
- Avión (rápido pero costoso)

Cada uno tiene ventajas y desventajas. Lo mismo pasa con los algoritmos: cada uno tiene fortalezas en diferentes tipos de problemas.

---

## 🔑 Modelos Entrenados y Sus Características

### 1. **Logistic Regression (Regresión Logística)**

**¿Cómo funciona?**
- Encuentra una línea (o hiperplano) que separa las dos clases
- Calcula la probabilidad de que un cliente haga churn

**Ventajas**:
- ✅ Simple y rápido
- ✅ Fácil de interpretar
- ✅ Funciona bien con relaciones lineales

**Desventajas**:
- ❌ Asume relaciones lineales
- ❌ No captura patrones complejos

**Analogía**: Es como trazar una línea recta en un mapa para separar dos regiones.

---

### 2. **Decision Tree (Árbol de Decisión)**

**¿Cómo funciona?**
- Hace una serie de preguntas (if-then-else)
- Cada pregunta divide los datos en grupos más puros

**Ejemplo de decisiones**:
```
¿Contrato mes a mes?
├─ Sí → ¿Tenure < 12 meses?
│  ├─ Sí → CHURN (alta probabilidad)
│  └─ No → NO CHURN
└─ No → NO CHURN
```

**Ventajas**:
- ✅ Muy interpretable
- ✅ Captura relaciones no lineales
- ✅ No requiere normalización

**Desventajas**:
- ❌ Propenso a overfitting (memorizar en vez de aprender)
- ❌ Inestable (pequeños cambios en datos → árbol muy diferente)

**Analogía**: Como un diagrama de flujo de decisiones que sigues paso a paso.

---

### 3. **Random Forest (Bosque Aleatorio)**

**¿Cómo funciona?**
- Crea muchos árboles de decisión (100-1000)
- Cada árbol vota
- La decisión final es por mayoría

**Ventajas**:
- ✅ Muy robusto y preciso
- ✅ Reduce overfitting vs. un solo árbol
- ✅ Maneja bien datos complejos
- ✅ Proporciona importancia de features

**Desventajas**:
- ❌ Menos interpretable que un solo árbol
- ❌ Más lento de entrenar

**Analogía**: Como pedir opinión a 100 expertos y tomar la decisión por votación mayoritaria.

---

### 4. **Gradient Boosting**

**¿Cómo funciona?**
- Construye árboles secuencialmente
- Cada árbol nuevo corrige los errores del anterior
- Es como aprender de tus errores iterativamente

**Ventajas**:
- ✅ Muy preciso
- ✅ Captura patrones complejos
- ✅ Funciona bien en competencias de ML

**Desventajas**:
- ❌ Más lento de entrenar
- ❌ Requiere ajuste cuidadoso de parámetros
- ❌ Propenso a overfitting si no se configura bien

**Analogía**: Como un estudiante que hace un examen de práctica, revisa sus errores, estudia esas áreas y mejora en el siguiente intento.

---

### 5. **XGBoost (Extreme Gradient Boosting)**

**¿Cómo funciona?**
- Versión optimizada y mejorada de Gradient Boosting
- Incluye regularización para prevenir overfitting
- Muy eficiente computacionalmente

**Ventajas**:
- ✅ Estado del arte en muchos problemas
- ✅ Muy preciso
- ✅ Maneja bien datos desbalanceados
- ✅ Rápido (comparado con Gradient Boosting tradicional)

**Desventajas**:
- ❌ Muchos hiperparámetros para ajustar
- ❌ Menos interpretable

**Analogía**: Como Gradient Boosting pero con turbo y mejor motor.

---

### 6. **Support Vector Machine (SVM)**

**¿Cómo funciona?**
- Encuentra el mejor hiperplano que separa las clases
- Maximiza el margen entre las clases

**Ventajas**:
- ✅ Efectivo en espacios de alta dimensión
- ✅ Funciona bien con datos no lineales (usando kernels)

**Desventajas**:
- ❌ Lento con datasets grandes
- ❌ Sensible a la escala de datos
- ❌ Difícil de interpretar

**Analogía**: Como encontrar la mejor valla para separar dos rebaños de ovejas, maximizando el espacio entre ellas.

---

### 7. **K-Nearest Neighbors (KNN)**

**¿Cómo funciona?**
- Para clasificar un punto, mira sus K vecinos más cercanos
- Asigna la clase más común entre esos vecinos

**Ventajas**:
- ✅ Simple de entender
- ✅ No requiere entrenamiento (lazy learning)

**Desventajas**:
- ❌ Lento en predicción con datasets grandes
- ❌ Sensible a la escala y ruido
- ❌ Requiere elegir K apropiado

**Analogía**: "Dime con quién andas y te diré quién eres" - si tus 5 vecinos más cercanos hicieron churn, probablemente tú también.

---

## 📊 Métricas de Evaluación

El bloque evalúa cada modelo con múltiples métricas:

### **1. Accuracy (Exactitud)**
- **¿Qué mide?** Porcentaje de predicciones correctas
- **Fórmula**: (Aciertos totales) / (Total de predicciones)
- **Problema**: Puede ser engañosa con datos desbalanceados

**Ejemplo**: Si 73% de clientes NO hacen churn, un modelo que siempre predice "NO" tendría 73% de accuracy pero sería inútil.

### **2. Precision (Precisión)**
- **¿Qué mide?** De los que predijimos como churn, ¿cuántos realmente lo hicieron?
- **Fórmula**: Verdaderos Positivos / (Verdaderos Positivos + Falsos Positivos)
- **Importancia**: Evita falsas alarmas

**Analogía**: De todas las veces que el detector de humo sonó, ¿cuántas veces realmente había fuego?

### **3. Recall (Sensibilidad)**
- **¿Qué mide?** De todos los que realmente hicieron churn, ¿cuántos detectamos?
- **Fórmula**: Verdaderos Positivos / (Verdaderos Positivos + Falsos Negativos)
- **Importancia**: No perder clientes en riesgo

**Analogía**: De todos los incendios que hubo, ¿cuántos detectó el detector de humo?

### **4. F1-Score**
- **¿Qué mide?** Balance entre Precision y Recall
- **Fórmula**: 2 × (Precision × Recall) / (Precision + Recall)
- **Importancia**: Métrica equilibrada

### **5. ROC-AUC**
- **¿Qué mide?** Capacidad del modelo para discriminar entre clases
- **Rango**: 0.5 (aleatorio) a 1.0 (perfecto)
- **Importancia**: Independiente del umbral de decisión

---

## 🏆 Resultados Típicos (Baseline)

**Modelos de mejor rendimiento** (generalmente):
1. **XGBoost**: ~85% accuracy, ~0.85 ROC-AUC
2. **Random Forest**: ~84% accuracy, ~0.84 ROC-AUC
3. **Gradient Boosting**: ~83% accuracy, ~0.83 ROC-AUC

**Modelos de rendimiento moderado**:
4. **Logistic Regression**: ~80% accuracy
5. **SVM**: ~79% accuracy

**Modelos de menor rendimiento**:
6. **Decision Tree**: ~75% accuracy (overfitting)
7. **KNN**: ~76% accuracy

---

## 🔗 Relación con el Análisis General

Este bloque es **crucial** porque:

1. **Identifica candidatos**: Descubrimos qué modelos funcionan mejor
2. **Establece baseline**: Punto de referencia para mejoras futuras
3. **Informa optimización**: Sabemos en qué modelos invertir tiempo
4. **Valida el enfoque**: Confirma que el problema es predecible

---

## 💡 Puntos Clave para Recordar

1. **7 modelos diferentes** entrenados y comparados
2. **Ensemble methods** (Random Forest, Gradient Boosting, XGBoost) suelen ganar
3. **Accuracy no es suficiente** - necesitamos múltiples métricas
4. **Baseline = configuración por defecto** - aún no optimizado
5. **Desbalanceo de clases** afecta el rendimiento (se abordará en el siguiente bloque)

---

## 🎓 Conclusión

El entrenamiento de modelos baseline es como una audición: probamos varios candidatos para ver quiénes tienen potencial. Los modelos ensemble (Random Forest, XGBoost) generalmente destacan, pero todos aportan información valiosa.

**Siguiente paso**: Manejar el desbalanceo de clases con técnicas como SMOTE para mejorar la detección de churn.

