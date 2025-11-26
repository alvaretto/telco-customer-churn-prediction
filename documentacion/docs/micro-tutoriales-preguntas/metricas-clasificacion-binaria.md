# 📊 Explicación de las Métricas de Clasificación Binaria en tu Notebook

Te explico cómo funcionan las métricas de clasificación binaria que utilizas en `Telco_Customer_Churn.ipynb`:

## 🎯 **1. Métricas Importadas**

En tu notebook importas estas métricas de scikit-learn:

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve,
    precision_recall_curve, average_precision_score
)
```

---

## 📈 **2. Las 5 Métricas Principales**

### **🎯 Accuracy (Exactitud)**
- **¿Qué mide?** Porcentaje total de predicciones correctas
- **Fórmula:** `(VP + VN) / Total`
- **En tu código:**

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
accuracy = accuracy_score(y_test, y_pred)
print(f"  Accuracy: {accuracy:.4f}")
```

**⚠️ Limitación:** No es ideal para datos desbalanceados (como tu caso de churn)

---

### **🎯 Precision (Precisión)**
- **¿Qué mide?** De todos los que predijimos como "churn", ¿cuántos realmente hicieron churn?
- **Fórmula:** `VP / (VP + FP)`
- **Analogía:** Si envías 100 ofertas de retención, ¿cuántas fueron a clientes que realmente iban a irse?

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
precision = precision_score(y_test, y_pred)
print(f"  Precision: {precision:.4f}")
```

**💡 En tu modelo:** 72% significa que de cada 100 clientes que predices como "churn", 72 realmente se van.

---

### **🎯 Recall (Sensibilidad/Exhaustividad)**
- **¿Qué mide?** De todos los que realmente hicieron churn, ¿cuántos detectamos?
- **Fórmula:** `VP / (VP + FN)`
- **Analogía:** De todos los clientes que se fueron, ¿a cuántos detectaste a tiempo?

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
recall = recall_score(y_test, y_pred)
print(f"  Recall: {recall:.4f}")
```

**💡 En tu modelo:** 83% significa que detectas 83 de cada 100 clientes que realmente se van.

**🔥 Importancia:** Esta es la métrica MÁS IMPORTANTE en churn porque no queremos perder clientes en riesgo.

---

### **🎯 F1-Score**
- **¿Qué mide?** Balance armónico entre Precision y Recall
- **Fórmula:** `2 × (Precision × Recall) / (Precision + Recall)`
- **Cuándo usarlo:** Cuando necesitas equilibrio entre precision y recall

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
f1 = f1_score(y_test, y_pred)
print(f"  F1-Score: {f1:.4f}")
```

**💡 En tu modelo:** 77% indica un buen balance entre detectar churners y no molestar a clientes leales.

---

### **🎯 ROC-AUC (Area Under the ROC Curve)**
- **¿Qué mide?** Capacidad del modelo para discriminar entre clases
- **Rango:** 0.5 (aleatorio) a 1.0 (perfecto)
- **Ventaja:** Independiente del umbral de decisión

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"  ROC-AUC: {roc_auc:.4f}")
```

**💡 En tu modelo:** 0.87 es EXCELENTE (>0.8 se considera muy bueno)

---

## 📊 **3. Cómo se Calculan en tu Código**

Tu notebook calcula las métricas en 3 momentos:

### **A) Modelos Baseline (sin balanceo)**
```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
for name, model in models.items():
    model.fit(X_train_processed, y_train)
    y_pred = model.predict(X_test_processed)
    y_pred_proba = model.predict_proba(X_test_processed)[:, 1]

    # Calcular todas las métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
```

### **B) Modelos con SMOTE (datos balanceados)**
Repite el mismo proceso pero con datos balanceados para mejorar el recall.

### **C) Modelo Final Optimizado**
```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
print(f"  Accuracy: {accuracy_score(y_test, y_pred_best):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_best):.4f}")
print(f"  Recall: {recall_score(y_test, y_pred_best):.4f}")
print(f"  F1-Score: {f1_score(y_test, y_pred_best):.4f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_pred_proba_best):.4f}")
```

---

## 📉 **4. Visualizaciones de Métricas**

### **A) Matriz de Confusión**
Muestra los 4 tipos de predicciones:

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
cm = confusion_matrix(y_test, y_pred_best)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Churn', 'Churn'],
            yticklabels=['No Churn', 'Churn'])
```

**Interpretación:**

- **Verdaderos Negativos (VN):** Clientes que NO se fueron y predijimos correctamente
- **Falsos Positivos (FP):** Clientes leales que marcamos como "en riesgo" ❌
- **Falsos Negativos (FN):** Clientes que se fueron pero NO detectamos ❌❌ (¡Lo peor!)
- **Verdaderos Positivos (VP):** Clientes en riesgo que detectamos correctamente ✅

---

### **B) Curva ROC**
Muestra el trade-off entre True Positive Rate y False Positive Rate:

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_best)
roc_auc = roc_auc_score(y_test, y_pred_proba_best)

ax2.plot(fpr, tpr, color='darkorange', lw=2,
         label=f'ROC curve (AUC = {roc_auc:.4f})')
ax2.plot([0, 1], [0, 1], color='navy', lw=2,
         linestyle='--', label='Random Classifier')
```

**Interpretación:**

- Línea diagonal = clasificador aleatorio (AUC = 0.5)
- Cuanto más cerca de la esquina superior izquierda, mejor
- Tu AUC = 0.87 significa que el modelo es muy bueno discriminando

---

### **C) Curva Precision-Recall**
Especialmente útil para datos desbalanceados:

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
precision_curve, recall_curve, _ = precision_recall_curve(y_test, y_pred_proba_best)
avg_precision = average_precision_score(y_test, y_pred_proba_best)

ax3.plot(recall_curve, precision_curve, color='green', lw=2,
         label=f'PR curve (AP = {avg_precision:.4f})')
```

---

## 🎯 **5. ¿Por Qué Estas Métricas en Churn?**

| Métrica | Importancia en Churn | Razón |
|---------|---------------------|-------|
| **Recall** | ⭐⭐⭐⭐⭐ | No podemos perder clientes en riesgo |
| **ROC-AUC** | ⭐⭐⭐⭐⭐ | Mide capacidad general del modelo |
| **F1-Score** | ⭐⭐⭐⭐ | Balance entre detectar churn y no molestar clientes |
| **Precision** | ⭐⭐⭐ | Evita gastar en campañas innecesarias |
| **Accuracy** | ⭐⭐ | Engañosa con datos desbalanceados |

---

## 💡 **6. Resultados de tu Modelo**

Según tu metadata guardada:

```python
'metrics': {
    'roc_auc': 0.87,    # ⭐ Excelente discriminación
    'recall': 0.83,     # ⭐ Detectas 83% de churners
    'precision': 0.72,  # ✅ 72% de tus alertas son correctas
    'f1_score': 0.77    # ✅ Buen balance
}
```

**Interpretación de Negocio:**

- De cada 100 clientes que se van, detectas 83 ✅
- De cada 100 alertas que generas, 72 son correctas ✅
- Solo pierdes 17 de cada 100 clientes en riesgo 🎯

---

## 🔍 **Resumen Visual del Flujo**

```
1. Entrenar modelo → model.fit(X_train, y_train)
2. Hacer predicciones → y_pred = model.predict(X_test)
3. Obtener probabilidades → y_pred_proba = model.predict_proba(X_test)[:, 1]
4. Calcular métricas:
   ├─ accuracy_score(y_test, y_pred)
   ├─ precision_score(y_test, y_pred)
   ├─ recall_score(y_test, y_pred)
   ├─ f1_score(y_test, y_pred)
   └─ roc_auc_score(y_test, y_pred_proba)
5. Visualizar:
   ├─ confusion_matrix()
   ├─ roc_curve()
   └─ precision_recall_curve()
```

¿Te gustaría que profundice en alguna métrica específica o que te muestre cómo interpretar las visualizaciones en más detalle?
