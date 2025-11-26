**R² (R-cuadrado) NO se usa en este proyecto porque es una métrica para problemas de REGRESIÓN, no de CLASIFICACIÓN**.

## 🎯 Diferencia Fundamental

### **Tu Proyecto: Clasificación Binaria**

- **Objetivo**: Predecir una **categoría** → Churn: **Sí** o **No**
- **Salida del modelo**: Clase discreta (0 o 1)
- **Métricas apropiadas**: Accuracy, Precision, Recall, F1-Score, ROC-AUC ✅

### **R² es para Regresión**

- **Objetivo**: Predecir un **valor numérico continuo**
- **Ejemplos**: Predecir precio de una casa ($150,000), temperatura (23.5°C), ventas ($45,230)
- **Salida del modelo**: Número continuo
- **Métricas apropiadas**: R², MAE, MSE, RMSE ✅

---

## 📊 Comparación de Métricas

| Tipo de Problema | Ejemplos | Métricas Correctas | ❌ NO Usar |
|------------------|----------|-------------------|-----------|
| **Clasificación Binaria** | Churn (Sí/No), Spam (Sí/No), Fraude (Sí/No) | Accuracy, Precision, Recall, F1, ROC-AUC | R², MAE, MSE |
| **Clasificación Multiclase** | Tipo de producto (A/B/C), Sentimiento (Positivo/Neutral/Negativo) | Accuracy, Precision, Recall, F1 (macro/micro) | R², MAE, MSE |
| **Regresión** | Precio de casa, Temperatura, Ventas | R², MAE, MSE, RMSE | Accuracy, Precision, Recall |

---

## 🔍 ¿Qué es R² (R-cuadrado)?

**Definición**: Mide qué porcentaje de la **variabilidad** de los datos es explicada por el modelo.

**Fórmula conceptual**: 
```
R² = 1 - (Error del modelo / Error de predecir siempre el promedio)
```

**Rango**:

- **1.0** = Modelo perfecto (explica 100% de la variabilidad)
- **0.5** = Modelo explica 50% de la variabilidad
- **0.0** = Modelo tan malo como predecir siempre el promedio
- **Negativo** = Modelo peor que predecir el promedio

**Ejemplo de Regresión**:
```python
# Predecir precio de casas
y_real = [100000, 150000, 200000, 250000]
y_pred = [105000, 145000, 205000, 248000]

r2 = r2_score(y_real, y_pred)  # ≈ 0.98 (excelente)
```

---

## ✅ Métricas que SÍ Usas (y por qué son correctas)

Tu proyecto usa las métricas **estándar de la industria** para clasificación binaria:

```json
path=models/metadata.json mode=EXCERPT
"metrics": {
  "roc_auc": 0.87,
  "recall": 0.83,
  "precision": 0.72,
  "f1_score": 0.77
}
```

### **1. ROC-AUC (0.87)** 🏆

- **Qué mide**: Capacidad del modelo para discriminar entre clases
- **Interpretación**: 87% de probabilidad de que el modelo clasifique correctamente un churner vs no-churner
- **Excelente para**: Comparar modelos, independiente del umbral

### **2. Recall (0.83)** 🎯

- **Qué mide**: De todos los clientes que SÍ hicieron churn, ¿cuántos detectamos?
- **Interpretación**: Detectas 83% de los churners reales
- **Crítico para**: No perder clientes en riesgo

### **3. Precision (0.72)** 🔍

- **Qué mide**: De los que predijimos como churn, ¿cuántos realmente lo hicieron?
- **Interpretación**: 72% de tus predicciones de churn son correctas
- **Crítico para**: Evitar falsas alarmas (gastar recursos en clientes que no harán churn)

### **4. F1-Score (0.77)** ⚖️

- **Qué mide**: Balance entre Precision y Recall
- **Interpretación**: Métrica equilibrada del rendimiento general

---

## 🤔 ¿Cuándo SÍ Usarías R²?

Si tu proyecto fuera **diferente**, por ejemplo:

### **Proyecto de Regresión: Predecir Ingresos del Cliente**

```python
# Objetivo: Predecir cuánto gastará un cliente (valor continuo)
y_real = [45.50, 120.30, 89.99, 200.00]  # Gastos reales
y_pred = [48.20, 115.80, 92.10, 195.50]  # Predicciones

# Aquí SÍ usarías R²
r2 = r2_score(y_real, y_pred)
mae = mean_absolute_error(y_real, y_pred)
rmse = np.sqrt(mean_squared_error(y_real, y_pred))
```

---

## 📝 Resumen

| Aspecto | Tu Proyecto | Si Fuera Regresión |
|---------|-------------|-------------------|
| **Tipo** | Clasificación Binaria | Regresión |
| **Predice** | Categoría (Churn: Sí/No) | Valor numérico (ej: $150.50) |
| **Métricas** | ✅ Accuracy, Precision, Recall, F1, ROC-AUC | ✅ R², MAE, MSE, RMSE |
| **Usar R²** | ❌ NO (no tiene sentido) | ✅ SÍ (métrica principal) |

---

## 💡 Conclusión

**No ves R² porque tu proyecto es de clasificación, no de regresión**. Las métricas que estás usando (ROC-AUC, Recall, Precision, F1-Score) son las **correctas y estándar** para predicción de churn.

Tu modelo con **ROC-AUC de 0.87** y **Recall de 0.83** tiene un rendimiento **excelente** para un problema de clasificación binaria. 🎉

¿Te gustaría que profundice en alguna de las métricas que SÍ estás usando, o tienes dudas sobre cómo interpretarlas?
