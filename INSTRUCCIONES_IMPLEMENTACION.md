# 📋 Instrucciones para Implementar Selección Automática del Mejor Modelo

## 🎯 Objetivo

Modificar el notebook `Telco_Customer_Churn.ipynb` para que seleccione y optimice automáticamente el mejor modelo según ROC-AUC, en lugar de siempre optimizar Random Forest.

---

## 📂 Archivos Creados

1. ✅ **`codigo_seleccion_automatica_modelo.py`** - Contiene el código Python a agregar
2. ✅ **`SELECCION_AUTOMATICA_MODELO.md`** - Documentación técnica completa
3. ✅ **`INSTRUCCIONES_IMPLEMENTACION.md`** - Este archivo (instrucciones paso a paso)

---

## 🔧 Pasos de Implementación

### **Paso 1: Abrir el Notebook en Google Colab**

1. Ve a [Google Colab](https://colab.research.google.com/)
2. Abre el archivo `Telco_Customer_Churn.ipynb`
3. Asegúrate de que el notebook esté ejecutado hasta la sección de comparativa de modelos

---

### **Paso 2: Agregar Código de Selección Automática**

#### 2.1. Ubicar la Celda Correcta

Busca la celda que contiene este código (aproximadamente línea 3195-3200):

```python
# Crear DataFrame con resultados
results_balanced_df = pd.DataFrame(results_balanced)
results_balanced_df = results_balanced_df.sort_values('ROC-AUC', ascending=False)

print("\n" + "="*80)
print("\nRESUMEN DE RESULTADOS CON SMOTE:\n")
print(results_balanced_df.to_string(index=False))
```

#### 2.2. Crear Nueva Celda

1. Haz clic **DESPUÉS** de esa celda
2. Presiona el botón **"+ Código"** para agregar una nueva celda
3. Copia y pega el siguiente código:

```python
# ============================================================================
# SELECCIÓN AUTOMÁTICA DEL MEJOR MODELO
# ============================================================================

# Seleccionar automáticamente el mejor modelo según ROC-AUC
best_model_name = results_balanced_df.iloc[0]['Modelo']
best_model_roc_auc = results_balanced_df.iloc[0]['ROC-AUC']

print("\n" + "="*80)
print("\n🏆 MEJOR MODELO SEGÚN COMPARATIVA:")
print(f"   • Modelo: {best_model_name}")
print(f"   • ROC-AUC: {best_model_roc_auc:.4f}")
print("\n" + "="*80)
```

4. Ejecuta la celda (Shift + Enter)

---

### **Paso 3: Reemplazar la Optimización de Random Forest**

#### 3.1. Ubicar la Celda de Optimización

Busca la celda que contiene la optimización de Random Forest (aproximadamente línea 3400). Debería verse algo así:

```python
# Optimización de Random Forest con RandomizedSearchCV
param_distributions_rf = {
    'n_estimators': [100, 200, 300],
    ...
}
```

#### 3.2. Reemplazar con Código Dinámico

1. **ELIMINA** todo el contenido de esa celda
2. Abre el archivo `codigo_seleccion_automatica_modelo.py`
3. Copia **TODO** el contenido de la sección "CÓDIGO 2" (desde la línea que dice `import numpy as np` hasta el final)
4. Pégalo en la celda vacía
5. Ejecuta la celda (Shift + Enter)

---

### **Paso 4: Verificar el Funcionamiento**

Después de ejecutar las nuevas celdas, deberías ver:

1. ✅ Mensaje mostrando el mejor modelo seleccionado:
   ```
   🏆 MEJOR MODELO SEGÚN COMPARATIVA:
      • Modelo: Logistic Regression
      • ROC-AUC: 0.8556
   ```

2. ✅ Mensaje de optimización del modelo ganador:
   ```
   🔧 Optimizando Logistic Regression...
   ```

3. ✅ Mejores hiperparámetros encontrados

4. ✅ Métricas finales del modelo optimizado

---

## 📊 Código Completo (Referencia)

Si prefieres ver el código completo, consulta el archivo `codigo_seleccion_automatica_modelo.py`.

---

## ✅ Validación

Para verificar que todo funciona correctamente:

### 1. **Ejecutar el Notebook Completo**

```python
# En una nueva celda, ejecuta:
print(f"Modelo seleccionado: {best_model_metrics['name']}")
print(f"ROC-AUC: {best_model_metrics['roc_auc']:.4f}")
```

Deberías ver el nombre del modelo optimizado (NO siempre "Random Forest Optimizado").

### 2. **Verificar metadata.json**

Después de guardar el modelo, verifica que `models/metadata.json` contenga el nombre correcto del modelo.

---

## 🔄 Flujo Completo

```
1. Comparar 4 modelos con SMOTE
   ↓
2. Ordenar por ROC-AUC (descendente)
   ↓
3. Seleccionar automáticamente el mejor
   ↓
4. Mostrar mensaje: "🏆 MEJOR MODELO: [nombre]"
   ↓
5. Optimizar ese modelo específico
   ↓
6. Actualizar best_model_metrics con nombre dinámico
   ↓
7. Guardar modelo optimizado
   ↓
8. Dashboard muestra el modelo correcto
```

---

## 🐛 Solución de Problemas

### Problema 1: Error "NameError: name 'best_model_name' is not defined"

**Solución:** Asegúrate de ejecutar primero la celda de selección automática (Paso 2) antes de la celda de optimización (Paso 3).

### Problema 2: Siempre optimiza Random Forest

**Solución:** Verifica que hayas reemplazado correctamente la celda de optimización con el código dinámico del Paso 3.

### Problema 3: Error en GridSearchCV o RandomizedSearchCV

**Solución:** Asegúrate de que todas las importaciones estén presentes al inicio del código:

```python
import numpy as np
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
```

---

## 📝 Notas Importantes

1. ⚠️ **No elimines** la celda de comparativa de modelos original
2. ⚠️ **Ejecuta las celdas en orden** para evitar errores
3. ✅ **Guarda el notebook** después de hacer los cambios
4. ✅ **Ejecuta todo el notebook** desde el principio para verificar

---

## 🎉 Resultado Final

Después de implementar estos cambios:

- ✅ El notebook seleccionará automáticamente el mejor modelo
- ✅ Optimizará ese modelo (no siempre Random Forest)
- ✅ Actualizará dinámicamente el nombre en `best_model_metrics`
- ✅ El dashboard mostrará el modelo correcto
- ✅ El sistema será científicamente robusto y adaptativo

---

## 📞 Soporte

Si tienes algún problema durante la implementación, revisa:

1. **`SELECCION_AUTOMATICA_MODELO.md`** - Documentación técnica completa
2. **`codigo_seleccion_automatica_modelo.py`** - Código de referencia
3. Los mensajes de error en Google Colab

**¡Listo! Tu notebook ahora tiene selección automática del mejor modelo.** 🚀

