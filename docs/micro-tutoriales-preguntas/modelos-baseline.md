## 🎯 ¿Qué son los Modelos Baseline?

Los **modelos baseline** son modelos de Machine Learning entrenados con **configuraciones por defecto** (sin optimización) que sirven como **punto de referencia inicial** para evaluar el rendimiento y comparar diferentes algoritmos.

**Analogía**: Es como una audición deportiva donde varios atletas compiten con su rendimiento natural (sin entrenamiento especializado) para ver quiénes tienen más potencial.

---

## 🔑 Características Clave de los Modelos Baseline

1. **Configuración por defecto**: Se usan los parámetros predeterminados de cada algoritmo
2. **Línea base de rendimiento**: Establecen un punto de partida antes de optimizar
3. **Comparación justa**: Todos los modelos se evalúan bajo las mismas condiciones
4. **Identificación de candidatos**: Ayudan a decidir en qué modelos invertir tiempo de optimización

---

## 📊 Modelos Baseline en Tu Proyecto

Según tu notebook `Telco_Customer_Churn.ipynb`, entrenas **7 modelos baseline**:

```python 
path=Telco_Customer_Churn.ipynb mode=EXCERPT
models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42, n_estimators=100),
    'XGBoost': xgb.XGBClassifier(random_state=42, n_estimators=100, eval_metric='logloss'),
    'SVM': SVC(random_state=42, probability=True),
    'KNN': KNeighborsClassifier()
}
```

---

## 🎓 Cómo Escoger los Mejores Modelos Baseline

### **Paso 1: Entrenar Todos los Modelos**
Entrenas los 7 modelos con los datos de entrenamiento y evalúas su rendimiento con múltiples métricas.

### **Paso 2: Evaluar con Métricas Apropiadas**
En tu contexto de predicción de churn, las métricas clave son:

- **Accuracy**: Porcentaje de predicciones correctas
- **Precision**: De los que predijiste como churn, ¿cuántos realmente lo hicieron?
- **Recall**: De todos los que hicieron churn, ¿cuántos detectaste? ⭐ **MUY IMPORTANTE para churn**
- **F1-Score**: Balance entre Precision y Recall
- **ROC-AUC**: Capacidad de discriminar entre clases (0.5 = aleatorio, 1.0 = perfecto)

### **Paso 3: Comparar Resultados**
Según tu documentación, los resultados típicos son:

**🏆 Mejores modelos (Ensemble Methods)**:

1. **XGBoost**: ~85% accuracy, ~0.85 ROC-AUC
2. **Random Forest**: ~84% accuracy, ~0.84 ROC-AUC
3. **Gradient Boosting**: ~83% accuracy, ~0.83 ROC-AUC

**📊 Rendimiento moderado**:

4. **Logistic Regression**: ~80% accuracy
5. **SVM**: ~79% accuracy

**📉 Menor rendimiento**:

6. **Decision Tree**: ~75% accuracy (propenso a overfitting)
7. **KNN**: ~76% accuracy

### **Paso 4: Seleccionar los Mejores Candidatos**
En tu proyecto, seleccionaste **4 modelos** para continuar:

```python 
path=Telco_Customer_Churn.ipynb mode=EXCERPT
best_models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42, n_estimators=100),
    'XGBoost': xgb.XGBClassifier(random_state=42, n_estimators=100, eval_metric='logloss')
}
```

---

## 💡 Criterios para Escoger Modelos Baseline

### **1. Rendimiento en Métricas Clave**
- Prioriza **Recall** en problemas de churn (no perder clientes en riesgo)
- Considera **F1-Score** para balance
- Revisa **ROC-AUC** para capacidad de discriminación

### **2. Tipo de Problema**
- **Ensemble methods** (Random Forest, XGBoost, Gradient Boosting) suelen ganar en problemas tabulares
- **Logistic Regression** es buena para interpretabilidad

### **3. Recursos Computacionales**
- **Random Forest/XGBoost**: Más lentos pero más precisos
- **Logistic Regression**: Rápido y eficiente

### **4. Interpretabilidad**
- **Logistic Regression**: Muy interpretable
- **Decision Tree**: Interpretable
- **Random Forest/XGBoost**: Menos interpretables pero proporcionan feature importance

---

## 🔄 Flujo Completo en Tu Proyecto

```
1. Entrenar 7 modelos baseline
   ↓
2. Evaluar con métricas (Accuracy, Precision, Recall, F1, ROC-AUC)
   ↓
3. Seleccionar los 4 mejores (Logistic Regression, Random Forest, Gradient Boosting, XGBoost)
   ↓
4. Reentrenar con datos balanceados (SMOTE)
   ↓
5. Optimizar hiperparámetros del mejor modelo (Random Forest)
   ↓
6. Evaluar modelo final
```

---

## 📝 Recomendaciones Prácticas

1. **Siempre entrena múltiples modelos**: No sabes cuál funcionará mejor hasta probarlo
2. **Usa validación cruzada**: Para evaluación más robusta
3. **Considera el contexto de negocio**: En churn, Recall es más importante que Precision
4. **No te cases con un modelo**: Los ensemble methods suelen ganar, pero no siempre
5. **Establece una línea base simple**: A veces Logistic Regression es suficiente

---

## 🎯 Resumen

- **Baseline** = Configuración por defecto, sin optimización
- **Propósito** = Comparar algoritmos y establecer punto de referencia
- **En tu proyecto** = 7 modelos → seleccionas 4 mejores → optimizas el mejor
- **Criterio principal** = Rendimiento en métricas clave (especialmente Recall para churn)
- **Ganadores típicos** = XGBoost, Random Forest, Gradient Boosting

¿Te gustaría que profundice en algún aspecto específico, como cómo interpretar las métricas o cómo implementar la selección de modelos en tu notebook?
