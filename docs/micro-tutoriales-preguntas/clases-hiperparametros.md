## 🎯 **Clases (Variable Objetivo)**

En tu proyecto, las **clases** son los valores posibles de la variable objetivo que quieres predecir:

```python
# Variable objetivo: Churn (Yes/No)
y = df_model['Churn'].map({'Yes': 1, 'No': 0})
```

**Las 2 clases son:**

- **"No" (0)**: Cliente que **NO abandona** el servicio
- **"Yes" (1)**: Cliente que **SÍ abandona** el servicio (churn)

Este es un problema de **clasificación binaria** porque solo hay 2 clases posibles.

---

## ⚙️ **Hiperparámetros**

Los **hiperparámetros** son configuraciones del modelo que **NO se aprenden** de los datos, sino que **tú defines antes** de entrenar. En tu notebook, optimizaste los hiperparámetros del modelo **Random Forest**:

```python
# Definir espacio de búsqueda para Random Forest
param_distributions = {
    'n_estimators': [100, 200, 300, 500],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True, False]
}
```

### **Significado de cada hiperparámetro:**

| Hiperparámetro | Qué controla | Valores probados |
|----------------|--------------|------------------|
| **n_estimators** | Número de árboles en el bosque | 100, 200, 300, 500 |
| **max_depth** | Profundidad máxima de cada árbol | 10, 20, 30, None (sin límite) |
| **min_samples_split** | Mínimo de muestras para dividir un nodo | 2, 5, 10 |
| **min_samples_leaf** | Mínimo de muestras en cada hoja | 1, 2, 4 |
| **max_features** | Características a considerar en cada división | 'sqrt', 'log2' |
| **bootstrap** | Si usar muestreo con reemplazo | True, False |

### **Mejores hiperparámetros encontrados:**

Después de la optimización con `RandomizedSearchCV`, los mejores valores fueron:

```python
{
    'n_estimators': 300,
    'max_depth': 20,
    'min_samples_split': 5,
    'min_samples_leaf': 1,
    'max_features': 'log2',
    'bootstrap': False
}
```

Con un **ROC-AUC de 0.9401** en validación cruzada.

---

## 📊 **Resumen**

- **Clases**: Los 2 resultados posibles que predices (Churn: Sí/No)
- **Hiperparámetros**: Configuraciones del modelo que ajustas para mejorar el rendimiento (como n_estimators, max_depth, etc.)

¿Necesitas que te explique algún hiperparámetro específico con más detalle?
