## 📏 Función de la Línea Diagonal en la Curva ROC

### **1️⃣ Es la Línea de Referencia (Baseline)**

La línea diagonal representa un **clasificador completamente aleatorio** - es decir, un modelo que adivina al azar.

```python
path=Telco_Customer_Churn.ipynb mode=EXCERPT
ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--',
         label='Random Classifier')
```

Esta línea va del punto **(0, 0)** al punto **(1, 1)** y tiene **AUC = 0.5**.

---

### **2️⃣ ¿Qué Representa un Clasificador Aleatorio?**

Imagina que decides si un cliente hará churn **lanzando una moneda**:

```python
import random

def clasificador_aleatorio(cliente):
    if random.random() > 0.5:
        return "Churn"
    else:
        return "No Churn"
```

**Resultado:**

- De 100 clientes que SÍ harán churn → detectarás ~50 (TPR = 0.5)
- De 100 clientes que NO harán churn → marcarás incorrectamente ~50 (FPR = 0.5)

**Punto en la curva:** (0.5, 0.5) → Está en la diagonal

---

### **3️⃣ Función Principal: Punto de Comparación**

La línea diagonal sirve para **evaluar si tu modelo es útil o no**:

| Posición de tu curva | Interpretación | AUC |
|---------------------|----------------|-----|
| **Por encima de la diagonal** | ✅ Tu modelo es mejor que adivinar | > 0.5 |
| **En la diagonal** | ❌ Tu modelo es inútil (aleatorio) | = 0.5 |
| **Por debajo de la diagonal** | ❌❌ Tu modelo es peor que adivinar* | < 0.5 |

*Si tu modelo está por debajo, puedes invertir las predicciones y mejorará.

---

### **4️⃣ Visualización Comparativa**

```
┌─────────────────────────┐ 1.0
│         ╱╱╱╱╱╱╱╱╱╱╱╱╱  │ ← Tu modelo (AUC = 0.87)
│       ╱╱╱╱╱╱╱╱╱╱╱╱     │   MUCHO mejor que aleatorio
│     ╱╱╱╱╱╱╱╱╱╱╱         │
│   ╱╱╱╱╱╱╱╱╱             │
│ ╱╱╱╱╱╱╱                 │
│╱╱╱╱╱  ← Línea diagonal  │ ← Clasificador aleatorio
│    ╱  (AUC = 0.5)       │   (lanzar una moneda)
└─────────────────────────┘
0.0                      1.0
```

**Interpretación:**

- El **área entre tu curva y la diagonal** representa cuánto mejor es tu modelo que adivinar al azar
- Cuanto mayor sea esa área, mejor es tu modelo

---

### **5️⃣ ¿Por Qué la Diagonal Representa Aleatoriedad?**

Matemáticamente, en un clasificador aleatorio:

```
TPR = FPR (siempre)
```

**Demostración:**

Si asignas probabilidades aleatorias uniformes entre 0 y 1:

| Umbral | % de predicciones "Churn" | TPR | FPR |
|--------|---------------------------|-----|-----|
| 0.9 | 10% | 0.10 | 0.10 |
| 0.7 | 30% | 0.30 | 0.30 |
| 0.5 | 50% | 0.50 | 0.50 |
| 0.3 | 70% | 0.70 | 0.70 |
| 0.1 | 90% | 0.90 | 0.90 |

Todos los puntos caen en la línea **y = x** (la diagonal).

---

### **6️⃣ Cálculo del Área Entre Tu Curva y la Diagonal**

El **beneficio real** de tu modelo se mide como:

```
Ganancia = AUC_modelo - AUC_aleatorio
Ganancia = 0.87 - 0.5 = 0.37
```

Esto significa que tu modelo es **37 puntos porcentuales mejor** que adivinar al azar.

---

### **7️⃣ Ejemplo Práctico de Negocio**

Supongamos que tienes **1,000 clientes**:

- 300 harán churn
- 700 no harán churn

#### **Clasificador Aleatorio (línea diagonal):**
```
Detectados correctamente: 300 × 0.5 = 150 churners
Falsos positivos: 700 × 0.5 = 350 clientes molestos
```

#### **Tu Modelo (AUC = 0.87):**
```
Detectados correctamente: 300 × 0.83 = 249 churners ✅
Falsos positivos: 700 × 0.15 = 105 clientes molestos ✅
```

**Diferencia:**

- Detectas **99 churners más** que el azar
- Molestas a **245 clientes menos** que el azar

---

### **🎯 Resumen: Funciones de la Línea Diagonal**

1. **Referencia de comparación** → Marca el rendimiento mínimo aceptable
2. **Representa aleatoriedad** → Modelo que adivina sin información
3. **Divide el espacio** → Modelos útiles (arriba) vs inútiles (abajo)
4. **Permite calcular ganancia** → AUC_modelo - 0.5 = mejora sobre el azar
5. **Validación visual** → Si tu curva toca la diagonal, algo está mal

**En tu caso:**

- Tu curva está **muy por encima** de la diagonal
- Esto confirma que tu modelo es **significativamente mejor** que adivinar
- La distancia vertical entre tu curva y la diagonal muestra tu **ventaja competitiva**

¿Quedó claro por qué siempre se dibuja esa línea diagonal en las curvas ROC?
