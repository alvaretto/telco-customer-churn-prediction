# Bloque 9: Manejo del Desbalanceo de Clases

## 📋 Descripción General

Este bloque es como **equilibrar una balanza desnivelada**. Recordemos que tenemos 73% de clientes que NO hacen churn y solo 27% que SÍ lo hacen. Este desbalanceo puede hacer que los modelos sean "perezosos" y simplemente predigan siempre la clase mayoritaria. Aquí aplicamos técnicas para balancear las clases y mejorar la detección de churn.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Aplicar SMOTE** para balancear las clases en el conjunto de entrenamiento
2. **Reentrenar los mejores modelos** con datos balanceados
3. **Comparar resultados** antes y después del balanceo
4. **Mejorar el Recall** (detección de clientes que harán churn)

### ¿Por qué es importante?

**Analogía de la enfermedad rara**: Imagina un test médico para una enfermedad que solo afecta al 3% de la población:
- Un modelo "tonto" que siempre dice "NO tienes la enfermedad" tendría 97% de accuracy
- Pero sería inútil porque nunca detectaría a los enfermos

Lo mismo pasa con el churn: necesitamos detectar específicamente a los que SÍ se van, no solo tener alta accuracy general.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **El Problema del Desbalanceo**

**Distribución original**:
- **No Churn**: ~5,163 clientes (73%)
- **Churn**: ~1,869 clientes (27%)

**Ratio**: ~2.76:1 (casi 3 veces más "No" que "Yes")

**Consecuencias**:
- Los modelos aprenden mejor la clase mayoritaria
- Baja sensibilidad para detectar churn
- Métricas engañosas (alta accuracy pero bajo recall)

**Analogía del profesor**: Si en una clase hay 73 estudiantes callados y 27 habladores, el profesor prestará más atención a los callados (mayoría) y puede ignorar a los habladores (minoría).

---

### 2. **SMOTE (Synthetic Minority Over-sampling Technique)**

**¿Qué es SMOTE?**

Una técnica que crea **ejemplos sintéticos** de la clase minoritaria (Churn=Yes) para balancear el dataset.

**¿Cómo funciona?**

1. Toma un ejemplo de la clase minoritaria
2. Encuentra sus K vecinos más cercanos (también de la clase minoritaria)
3. Crea nuevos ejemplos interpolando entre el ejemplo original y sus vecinos

**Analogía visual**:
```
Original:  A -------- B
                ↓
Sintético: A -- X -- B
```

Donde X es un nuevo ejemplo creado "entre" A y B.

**Ventajas de SMOTE**:
- ✅ Crea ejemplos realistas (no duplicados)
- ✅ Aumenta la diversidad de la clase minoritaria
- ✅ Mejora el aprendizaje del modelo

**Diferencia con otras técnicas**:
- **RandomOverSampler**: Simplemente duplica ejemplos existentes (puede causar overfitting)
- **RandomUnderSampler**: Elimina ejemplos de la clase mayoritaria (pierde información)
- **SMOTE**: Crea nuevos ejemplos sintéticos (balance sin pérdida de información)

---

### 3. **Aplicación de SMOTE**

```python
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
```

**Resultado**:
- **Antes**: 5,163 No Churn, 1,869 Churn
- **Después**: 5,163 No Churn, 5,163 Churn (balanceado 50/50)

**Importante**: SMOTE solo se aplica al conjunto de **entrenamiento**, NUNCA al de prueba.

**¿Por qué?**

**Analogía del examen**: 
- Puedes estudiar con material adicional (SMOTE en train)
- Pero el examen debe ser con preguntas reales (test sin modificar)

---

### 4. **Reentrenamiento de Modelos**

El bloque reentrena los mejores modelos (identificados en el bloque anterior) con los datos balanceados:

1. **Logistic Regression**
2. **Random Forest**
3. **Gradient Boosting**
4. **XGBoost**

**Configuración**: Se mantienen los parámetros por defecto (baseline) para comparación justa.

---

## 📊 Comparación de Resultados: Antes vs. Después de SMOTE

### **Métricas Típicas - Antes de SMOTE**

| Modelo | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| Random Forest | 84% | 70% | 50% | 58% |
| XGBoost | 85% | 72% | 52% | 60% |

**Problema**: Recall bajo (solo detecta ~50% de los churns)

### **Métricas Típicas - Después de SMOTE**

| Modelo | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| Random Forest | 82% | 65% | 78% | 71% |
| XGBoost | 83% | 67% | 80% | 73% |

**Mejora**: Recall aumenta significativamente (~30% de mejora)

---

### **Interpretación de los Cambios**

#### **Accuracy baja ligeramente** (84% → 82%)
- **¿Por qué?** Ahora el modelo comete más "falsos positivos" (predice churn cuando no lo hay)
- **¿Es malo?** No necesariamente - depende del objetivo de negocio

#### **Recall aumenta significativamente** (50% → 78%)
- **¿Por qué?** El modelo ahora detecta mejor la clase minoritaria
- **¿Es bueno?** ¡Sí! Detectamos más clientes en riesgo

#### **Precision baja un poco** (70% → 65%)
- **¿Por qué?** Más falsos positivos
- **Trade-off**: Sacrificamos un poco de precisión por mucho más recall

---

### **Trade-off: Precision vs. Recall**

**Analogía del detector de metales**:

**Antes de SMOTE** (Alta Precision, Bajo Recall):
- Cuando pita, casi siempre hay metal (pocas falsas alarmas)
- Pero se pierde mucho metal (no detecta todo)

**Después de SMOTE** (Precision moderada, Alto Recall):
- Pita más veces, algunas falsas alarmas
- Pero encuentra casi todo el metal

**Para el negocio de Telco**:
- **Falso Positivo**: Ofrecemos descuento a alguien que no se iba a ir (costo: descuento innecesario)
- **Falso Negativo**: No detectamos a alguien que se va (costo: perder el cliente completo)

**Conclusión**: Es mejor tener algunos falsos positivos que perder clientes reales.

---

## 🔗 Relación con el Análisis General

Este bloque es **crítico** porque:

1. **Corrige un problema fundamental**: El desbalanceo de clases
2. **Mejora la métrica clave**: Recall (detección de churn)
3. **Alinea con objetivos de negocio**: Preferimos detectar más churns aunque tengamos algunas falsas alarmas
4. **Prepara para optimización**: Datos balanceados permiten mejor ajuste de hiperparámetros

---

## 💡 Puntos Clave para Recordar

1. **Desbalanceo original**: 73% No Churn, 27% Churn
2. **SMOTE** crea ejemplos sintéticos de la clase minoritaria
3. **Solo se aplica a train**, nunca a test
4. **Recall mejora ~30%** (de ~50% a ~78%)
5. **Trade-off**: Accuracy baja un poco, pero Recall aumenta mucho
6. **Para el negocio**: Mejor detectar más churns con algunas falsas alarmas

---

## 🎓 Conclusión

El manejo del desbalanceo de clases transforma un modelo "perezoso" que ignora la clase minoritaria en uno que realmente detecta clientes en riesgo. SMOTE es como darle al modelo "gafas especiales" para ver mejor la clase minoritaria.

**Lección importante**: En problemas de negocio, la métrica más importante no siempre es accuracy. Para churn, Recall es crítico porque el costo de perder un cliente es mucho mayor que el costo de una falsa alarma.

**Siguiente paso**: Optimizar hiperparámetros de los mejores modelos para exprimir el máximo rendimiento.

