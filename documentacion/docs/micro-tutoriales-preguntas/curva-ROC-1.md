## 📊 ¿Cómo se Calcula la Curva ROC y el AUC?

### **1️⃣ Conceptos Básicos**

Primero, tu modelo no solo predice "Churn" o "No Churn", sino que da **probabilidades**:

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
y_pred_proba = model.predict_proba(X_test_processed)[:, 1]
# Ejemplo de salida: [0.23, 0.87, 0.45, 0.92, 0.15, ...]
```

Cada número es la **probabilidad de que el cliente haga churn** (entre 0 y 1).

---

### **2️⃣ Los Dos Ejes de la Curva ROC**

La curva ROC grafica dos tasas:

#### **TPR (True Positive Rate) = Recall = Sensibilidad**
```
TPR = VP / (VP + FN)
```
- **¿Qué mide?** De todos los clientes que SÍ hicieron churn, ¿cuántos detectamos?
- **Eje Y** de la curva ROC

#### **FPR (False Positive Rate)**
```
FPR = FP / (FP + VN)
```
- **¿Qué mide?** De todos los clientes que NO hicieron churn, ¿a cuántos marcamos incorrectamente como "churn"?
- **Eje X** de la curva ROC

---

### **3️⃣ Cómo se Construye la Curva ROC**

El truco está en **variar el umbral de decisión**:

| Umbral | Decisión |
|--------|----------|
| Si probabilidad ≥ 0.5 | Predecir "Churn" |
| Si probabilidad < 0.5 | Predecir "No Churn" |

Pero **¿y si cambiamos ese 0.5?**

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_best)
```

Esta función hace lo siguiente:

```
Para cada umbral posible (0.0, 0.01, 0.02, ..., 0.99, 1.0):
    1. Clasificar clientes usando ese umbral
    2. Calcular TPR (cuántos churners detectamos)
    3. Calcular FPR (cuántos falsos positivos generamos)
    4. Guardar el punto (FPR, TPR)
```

**Ejemplo numérico:**

| Umbral | TPR (Recall) | FPR | Punto en la curva |
|--------|--------------|-----|-------------------|
| 0.9 | 0.20 | 0.01 | (0.01, 0.20) |
| 0.7 | 0.50 | 0.05 | (0.05, 0.50) |
| **0.5** | **0.83** | **0.15** | **(0.15, 0.83)** ← Tu modelo |
| 0.3 | 0.95 | 0.40 | (0.40, 0.95) |
| 0.1 | 0.99 | 0.80 | (0.80, 0.99) |

Al unir todos estos puntos, obtienes la **curva ROC** 📈

---

### **4️⃣ ¿Por Qué la Línea Diagonal es un Clasificador Aleatorio?**

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--',
         label='Random Classifier')
```

**Imagina que lanzas una moneda** para decidir si un cliente hará churn:

- Si sale cara → "Churn"
- Si sale cruz → "No Churn"

**Resultado:**

- Detectarás el 50% de los churners reales (TPR = 0.5)
- Pero también marcarás incorrectamente al 50% de los no-churners (FPR = 0.5)

**Punto en la curva:** (0.5, 0.5) → Está en la diagonal

Para **cualquier umbral aleatorio**, siempre caerás en la línea diagonal porque:
```
TPR = FPR (siempre)
```

---

### **5️⃣ Cómo se Calcula el AUC (Área Bajo la Curva)**

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
roc_auc = roc_auc_score(y_test, y_pred_proba_best)
# Resultado: 0.87
```

El **AUC** es literalmente el **área** debajo de la curva ROC:

```
┌─────────────────────────┐ 1.0
│         ╱╱╱╱╱╱╱╱╱╱╱╱╱  │ ← Curva ROC (tu modelo)
│       ╱╱╱╱╱╱╱╱╱╱╱╱     │
│     ╱╱╱╱╱╱╱╱╱╱╱         │ AUC = 0.87
│   ╱╱╱╱╱╱╱╱╱             │ (área sombreada)
│ ╱╱╱╱╱╱╱                 │
│╱╱╱╱╱                    │
└─────────────────────────┘
0.0                      1.0
        FPR
```

**Cálculo matemático:**
```
AUC = ∫₀¹ TPR(FPR) d(FPR)
```

En la práctica, scikit-learn usa el **método del trapecio** para calcular el área:

```python
# Simplificado (lo que hace internamente)
area = 0
for i in range(len(fpr) - 1):
    # Área de cada trapecio
    width = fpr[i+1] - fpr[i]
    height = (tpr[i] + tpr[i+1]) / 2
    area += width * height
```

---

### **6️⃣ ¿Qué Significa AUC = 0.87?**

| AUC | Interpretación | Significado |
|-----|----------------|-------------|
| **0.5** | Aleatorio | La línea diagonal (inútil) |
| **0.7-0.8** | Aceptable | Mejor que adivinar |
| **0.8-0.9** | **Excelente** | **← Tu modelo (0.87)** |
| **0.9-1.0** | Sobresaliente | Casi perfecto |
| **1.0** | Perfecto | Sospechoso (overfitting) |

**Interpretación práctica de 0.87:**

> Si tomas un cliente que hizo churn y otro que NO hizo churn al azar, tu modelo tiene un **87% de probabilidad** de asignarle una probabilidad más alta al que realmente hizo churn.

---

### **7️⃣ ¿Por Qué "Más Cerca de la Esquina Superior Izquierda es Mejor"?**

La **esquina superior izquierda** es el punto (0, 1):

- **FPR = 0** → No hay falsos positivos (no molestas a clientes leales)
- **TPR = 1** → Detectas el 100% de los churners

**Modelo perfecto:**
```
┌─────────────────────────┐ 1.0 ← Llegas aquí inmediatamente
│█████████████████████████│
│█████████████████████████│ AUC = 1.0
│                         │
│                         │
│                         │
└─────────────────────────┘
0.0                      1.0
```

**Tu modelo (AUC = 0.87):**
```
┌─────────────────────────┐ 1.0
│         ╱╱╱╱╱╱╱╱╱╱╱╱╱  │ ← Muy cerca de la esquina
│       ╱╱╱╱╱╱╱╱╱╱╱╱     │
│     ╱╱╱╱╱╱╱╱╱╱╱         │ AUC = 0.87 (Excelente)
│   ╱╱╱╱╱╱╱╱╱             │
│ ╱╱╱╱╱╱╱                 │
└─────────────────────────┘
```

**Clasificador aleatorio (AUC = 0.5):**
```
┌─────────────────────────┐ 1.0
│                    ╱╱╱╱ │
│                ╱╱╱╱     │
│            ╱╱╱╱         │ AUC = 0.5 (Inútil)
│        ╱╱╱╱             │
│    ╱╱╱╱                 │
└─────────────────────────┘
```

---

### **🎯 Resumen**

1. **Tu modelo genera probabilidades** (0.0 a 1.0) para cada cliente
2. **La curva ROC** se construye probando diferentes umbrales de decisión
3. **Cada punto** en la curva es un par (FPR, TPR) para un umbral específico
4. **El AUC** es el área bajo esa curva (0.87 en tu caso)
5. **0.87 es excelente** porque está muy por encima del 0.5 (aleatorio)
6. **Significa** que tu modelo discrimina muy bien entre churners y no-churners

¿Te quedó más claro? ¿Quieres que profundice en algún aspecto específico?
