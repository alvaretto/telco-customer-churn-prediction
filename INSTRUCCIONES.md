# Instrucciones para Ejecutar el Notebook Optimizado

## Requisitos Previos

### 1. Librerías Necesarias

Asegúrate de tener instaladas las siguientes librerías de Python:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn
```

O si usas conda:

```bash
conda install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn -c conda-forge
```

### 2. Archivos Necesarios

- `Telco-Customer-Churn.ipynb` - El notebook optimizado
- `WA_Fn-UseC_-Telco-Customer-Churn.csv` - El dataset

## Cómo Ejecutar el Notebook

### Opción 1: Jupyter Notebook (Local)

1. Abre una terminal en el directorio del proyecto
2. Ejecuta:
   ```bash
   jupyter notebook
   ```
3. Abre `Telco-Customer-Churn.ipynb`
4. Ejecuta las celdas secuencialmente (Cell → Run All)

### Opción 2: JupyterLab (Local)

1. Abre una terminal en el directorio del proyecto
2. Ejecuta:
   ```bash
   jupyter lab
   ```
3. Abre `Telco-Customer-Churn.ipynb`
4. Ejecuta las celdas secuencialmente

### Opción 3: Google Colab

1. Sube el notebook a Google Drive
2. Abre con Google Colab
3. Sube el archivo CSV cuando se solicite
4. Ejecuta todas las celdas

### Opción 4: VS Code

1. Abre VS Code en el directorio del proyecto
2. Instala la extensión "Jupyter" si no la tienes
3. Abre `Telco-Customer-Churn.ipynb`
4. Selecciona el kernel de Python
5. Ejecuta las celdas

## Tiempo de Ejecución Estimado

- **Secciones 1-4 (EDA)**: ~2-3 minutos
- **Secciones 5-6 (Modelado Baseline)**: ~3-5 minutos
- **Sección 7 (SMOTE y Reentrenamiento)**: ~2-3 minutos
- **Sección 8 (Optimización)**: ~5-10 minutos (puede variar)
- **Secciones 9-10 (Evaluación)**: ~1-2 minutos

**Total**: Aproximadamente 15-25 minutos

## Estructura del Notebook

El notebook está organizado en 10 secciones principales:

1. **Introducción y Carga de Datos**
2. **Análisis de Calidad de Datos**
3. **Análisis Exploratorio (EDA)**
4. **Feature Engineering**
5. **Preparación de Datos**
6. **Modelos Baseline**
7. **Manejo de Desbalanceo**
8. **Optimización de Hiperparámetros**
9. **Evaluación Detallada**
10. **Conclusiones y Recomendaciones**

## Puntos Clave para la Defensa

### Conceptos Fundamentales a Dominar:

1. **Desbalanceo de Clases**:
   - Por qué es un problema (73% vs 27%)
   - Cómo SMOTE ayuda a balancear
   - Impacto en las métricas

2. **Métricas de Evaluación**:
   - Accuracy vs Precision vs Recall
   - Por qué ROC-AUC es importante
   - Interpretación de la matriz de confusión

3. **Feature Engineering**:
   - Justificación de cada feature creada
   - Impacto en el rendimiento del modelo

4. **Optimización**:
   - Por qué usar RandomizedSearchCV
   - Importancia de la validación cruzada
   - Trade-offs en hiperparámetros

5. **Interpretabilidad**:
   - Feature importance
   - Insights de negocio
   - Recomendaciones accionables

## Posibles Preguntas del Profesor

### Técnicas:

1. **¿Por qué usaste SMOTE en lugar de otras técnicas?**
   - SMOTE crea ejemplos sintéticos inteligentes
   - Mejor que simple oversampling
   - Evita overfitting del undersampling

2. **¿Por qué Random Forest fue el mejor modelo?**
   - Robusto ante overfitting
   - Maneja bien features categóricas
   - Proporciona feature importance
   - Buen balance precision/recall

3. **¿Qué significa ROC-AUC de 0.85?**
   - 85% de probabilidad de clasificar correctamente
   - Excelente capacidad discriminativa
   - Mejor que clasificador aleatorio (0.5)

4. **¿Por qué dividiste 80/20 y no 70/30?**
   - Balance entre datos de entrenamiento y validación
   - Suficientes datos para test (~1,400 registros)
   - Estándar en la industria

### De Negocio:

1. **¿Cuáles son los factores más importantes de churn?**
   - Tenure (clientes nuevos en riesgo)
   - Tipo de contrato (mes a mes)
   - Servicios adicionales (tech support)

2. **¿Qué recomendaciones darías a la empresa?**
   - Programas de retención para clientes nuevos
   - Incentivos para contratos largos
   - Promoción de servicios de soporte

3. **¿Cómo implementarías esto en producción?**
   - API para scoring en tiempo real
   - Dashboard de monitoreo
   - Actualización periódica del modelo

## Solución de Problemas

### Error: "No module named 'imblearn'"
```bash
pip install imbalanced-learn
```

### Error: "No module named 'xgboost'"
```bash
pip install xgboost
```

### Error: "FileNotFoundError"
- Verifica que el CSV esté en el mismo directorio
- O ajusta la ruta en la celda de carga de datos

### Advertencias de deprecación
- Son normales, el código funciona correctamente
- Puedes ignorarlas o actualizar las librerías

## Recursos Adicionales

- [Documentación de Scikit-learn](https://scikit-learn.org/)
- [Documentación de XGBoost](https://xgboost.readthedocs.io/)
- [Imbalanced-learn](https://imbalanced-learn.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

## Contacto y Soporte

Si encuentras algún problema o tienes preguntas:
1. Revisa la documentación de las librerías
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de ejecutar las celdas en orden

---

**¡Buena suerte en tu defensa!** 🚀

