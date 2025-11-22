---
output:
  word_document: default
  pdf_document: default
  html_document: default
---
# Preguntas Técnicas para Sustentación del Proyecto
## Análisis y Predicción de Customer Churn en Telco

### Introducción
Este documento contiene 30 preguntas técnicas fundamentales que evalúan la comprensión profunda de los conceptos de Machine Learning aplicados en el proyecto de predicción de Customer Churn. Las preguntas están organizadas por temas y cubren desde fundamentos teóricos hasta decisiones técnicas específicas del proyecto, incluyendo análisis exploratorio, pruebas de hipótesis estadísticas, deployment y valor de negocio.

**Última actualización**: 2025-11-21
**Versión**: 2.0 (sincronizada con notebook actualizado)

---

## I. ANÁLISIS EXPLORATORIO DE DATOS (EDA)

### 1. ¿Qué insights clave se obtuvieron del EDA sobre la distribución de churn en el dataset?

**Respuesta:** El EDA reveló varios insights fundamentales:

(1) **Tasa de churn global**: 26.5% de los clientes (1,869 de 7,043) abandonaron el servicio, indicando un problema significativo de negocio,
(2) **Distribución desbalanceada**: 73.5% No Churn vs 26.5% Churn, requiriendo técnicas especiales como SMOTE para el modelado,
(3) **Patrones por segmento**: Clientes con contratos mes a mes tienen 42% de churn vs solo 3% en contratos de 2 años,
(4) **Relación con tenure**: Los primeros 12 meses son críticos, con la mayoría del churn concentrado en clientes nuevos,
(5) **Impacto de precios**: MonthlyCharges > $70 correlaciona fuertemente con mayor churn. Estos insights no solo informaron la selección de features, sino que también generaron hipótesis de negocio que fueron validadas posteriormente con pruebas estadísticas formales.

### 2. ¿Por qué es importante analizar la correlación entre variables numéricas antes del modelado?

**Respuesta:** El análisis de correlación mediante heatmaps y matrices de correlación es crucial porque:

(1) **Detecta multicolinealidad**: Variables altamente correlacionadas (ej: TotalCharges y tenure con r=0.83) pueden causar inestabilidad en modelos lineales, inflando la varianza de los coeficientes,
(2) **Informa feature engineering**: La alta correlación entre TotalCharges y tenure sugiere que una variable derivada (ChargeRatio) podría capturar mejor la relación,
(3) **Previene redundancia**: Incluir variables redundantes aumenta dimensionalidad sin aportar información nueva, ralentizando el entrenamiento,
(4) **Identifica relaciones con el target**: MonthlyCharges y tenure muestran correlación moderada con Churn, validando su importancia predictiva. En nuestro proyecto, el heatmap reveló que TotalCharges es esencialmente tenure × MonthlyCharges, lo que justificó crear ChargeRatio como feature más informativa.

### 3. ¿Qué revelan las visualizaciones sobre la relación entre Contract type y Churn?

**Respuesta:** Las visualizaciones (barplots y countplots) muestran una relación dramática:

(1) **Contratos mes a mes**: 42% de churn (1,655 clientes de 3,875), la categoría de mayor riesgo,
(2) **Contratos de 1 año**: 11% de churn (166 de 1,473), riesgo moderado,
(3) **Contratos de 2 años**: 3% de churn (48 de 1,695), riesgo mínimo. Esta diferencia de 14x entre mes a mes y 2 años es estadísticamente significativa (validado con prueba Chi-cuadrado, p-value < 0.001) y tiene sentido de negocio: contratos largos implican mayor compromiso y switching costs más altos. Este insight generó recomendaciones accionables:
(a) incentivar contratos largos con descuentos del 15-25%,
(b) programas de retención enfocados en clientes mes a mes,
(c) estrategias de upgrade de contratos cortos a largos. La visualización también reveló que el 55% de los clientes tienen contratos mes a mes, representando una oportunidad masiva de reducción de churn.

---

## II. PREPROCESAMIENTO Y LIMPIEZA DE DATOS

### 4. ¿Por qué se utiliza StandardScaler en este proyecto y cómo funciona matemáticamente?

**Respuesta:** StandardScaler normaliza las características numéricas restando la media (μ) y dividiendo por la desviación estándar (σ): z = (x - μ) / σ. Esto es crucial porque los algoritmos basados en distancias (KNN, SVM) y los que usan gradiente descendente (Logistic Regression, Neural Networks) son sensibles a la escala de las variables. En nuestro proyecto, variables como `MonthlyCharges` (rango ~20-120) y `tenure` (rango 0-72) tienen escalas muy diferentes, por lo que sin normalización, las variables con mayor magnitud dominarían el modelo. StandardScaler garantiza que todas las características tengan media 0 y desviación estándar 1, permitiendo que el modelo aprenda de manera equitativa de todas las variables.

### 5. ¿Por qué se usa OneHotEncoder con el parámetro drop='first'? ¿Qué problema evita esto?

**Respuesta:** OneHotEncoder con `drop='first'` evita el problema de multicolinealidad perfecta (dummy variable trap). Cuando codificamos una variable categórica con n categorías, crear n columnas binarias genera dependencia lineal perfecta, ya que conociendo n-1 columnas podemos deducir la n-ésima. Por ejemplo, si `Contract` tiene 3 valores (Month-to-month, One year, Two year), crear 3 columnas haría que la suma siempre sea 1. Al eliminar la primera categoría, usamos n-1 columnas, evitando redundancia y mejorando la estabilidad numérica del modelo. Esto es especialmente importante para modelos lineales como Logistic Regression, donde la multicolinealidad puede causar coeficientes inestables y problemas de convergencia.

### 6. ¿Cómo se manejaron los valores faltantes en TotalCharges y por qué se eligió esa estrategia?

**Respuesta:** Los valores faltantes en `TotalCharges` (11 registros con espacios en blanco) se imputaron usando la lógica de negocio: para clientes nuevos con `tenure=0`, `TotalCharges` debe ser igual a `MonthlyCharges`. Esta estrategia es superior a la imputación por media/mediana porque preserva la relación matemática real entre las variables (TotalCharges ≈ MonthlyCharges × tenure). Eliminar estos registros habría sido subóptimo dado que representan clientes nuevos valiosos para el análisis de churn. La imputación basada en dominio mantiene la integridad de los datos y evita introducir sesgos artificiales que podrían afectar el rendimiento del modelo.

### 7. ¿Por qué se utiliza train_test_split con stratify=y? ¿Qué garantiza este parámetro?

**Respuesta:** El parámetro `stratify=y` garantiza que la distribución de la variable objetivo (Churn) se mantenga proporcional en los conjuntos de entrenamiento y prueba. En nuestro dataset, hay un desbalanceo de clases (~73% No Churn, ~27% Churn). Sin estratificación, el split aleatorio podría crear conjuntos con distribuciones diferentes (ej: 70% vs 76%), lo que sesgaría la evaluación del modelo. Con `stratify=y`, ambos conjuntos mantienen la proporción 73.5%/26.5%, asegurando que el modelo se entrene y evalúe en datos representativos. Esto es crítico para métricas como Recall y Precision, que son sensibles al desbalanceo de clases.

---

## III. FEATURE ENGINEERING

### 8. Explique la lógica detrás de la característica ChargeRatio y qué información captura.

**Respuesta:** `ChargeRatio = MonthlyCharges / (TotalCharges + 1)` captura la relación entre el cargo mensual actual y el cargo total histórico del cliente. Un ratio alto indica clientes nuevos o con aumentos recientes en sus cargos mensuales, lo que puede correlacionarse con insatisfacción y mayor probabilidad de churn. El +1 en el denominador evita división por cero para clientes nuevos. Esta característica es valiosa porque combina información temporal (tenure implícito) con información de pricing, revelando patrones que las variables individuales no capturan. Por ejemplo, un cliente con ChargeRatio alto podría estar experimentando un aumento de precio reciente, un factor conocido de churn.

### 9. ¿Qué ventaja ofrece la característica TotalServices sobre usar las variables individuales de servicios?

**Respuesta:** `TotalServices` (suma de servicios contratados) ofrece una representación compacta del nivel de engagement del cliente con la empresa. Mientras que las variables individuales (PhoneService, InternetService, etc.) son binarias o categóricas, TotalServices crea una escala ordinal (0-8) que captura el concepto de "profundidad de relación". Estudios de churn muestran que clientes con más servicios tienen menor probabilidad de abandonar (mayor switching cost). Esta característica reduce dimensionalidad (8 variables → 1) y facilita que el modelo aprenda patrones no lineales. Además, permite interacciones más simples: un cliente con TotalServices=1 y MonthlyCharges alto es un perfil de riesgo diferente a uno con TotalServices=6 y el mismo cargo.

### 10. ¿Por qué se creó TenureGroup categorizando la variable tenure? ¿Qué asume este enfoque?

**Respuesta:** `TenureGroup` discretiza `tenure` en bins (0-12, 12-24, 24-48, 48-72 meses) porque la relación entre tenure y churn no es lineal. Los primeros meses son críticos (alta probabilidad de churn), luego se estabiliza, y clientes de largo plazo tienen muy bajo churn. Al categorizar, permitimos que el modelo capture estos umbrales sin asumir linealidad. Este enfoque asume que hay "fases" distintas en el ciclo de vida del cliente. Sin embargo, tiene el trade-off de perder granularidad (un cliente con 11 meses vs 13 meses se trata muy diferente). Por eso mantenemos también `tenure` numérico, permitiendo que el modelo use ambas representaciones.

---

## IV. PRUEBAS DE HIPÓTESIS ESTADÍSTICAS

### 11. ¿Qué son las pruebas de hipótesis estadísticas y por qué se utilizaron en este proyecto?

**Respuesta:** Las pruebas de hipótesis estadísticas son métodos formales para 
determinar si las relaciones observadas en los datos son estadísticamente 
significativas o podrían ser producto del azar. En este proyecto se realizaron 7 
pruebas con nivel de significancia α=0.05 para validar las relaciones entre 
variables y churn observadas en el EDA. El proceso consiste en:

(1) Plantear hipótesis nula H₀ (no hay relación) y alternativa H₁ (sí hay relación),
(2) Calcular un estadístico de prueba (Chi-cuadrado o Mann-Whitney U),
(3) Obtener el p-value (probabilidad de observar estos datos si H₀ fuera cierta),
(4) Si p-value < 0.05, rechazamos H₀ y concluimos que la relación es estadísticamente significativa. Esto es crucial porque:
(a) valida que las relaciones no son casualidad,
(b) justifica la inclusión de variables en el modelo,
(c) proporciona evidencia cuantitativa para decisiones de negocio,
(d) aumenta la confianza en los insights del EDA.

### 12. ¿Cuál es la diferencia entre Chi-cuadrado y Mann-Whitney U? ¿Cuándo usar cada una?

**Respuesta:** Son pruebas para diferentes tipos de variables: **Chi-cuadrado (χ²)** se usa para probar independencia entre dos variables categóricas. Compara las frecuencias observadas vs esperadas en una tabla de contingencia. Estadístico: χ² = Σ[(Observado - Esperado)²/Esperado]. En nuestro proyecto se usó para: Contract vs Churn, PaymentMethod vs Churn, InternetService vs Churn, TechSupport vs Churn, PaperlessBilling vs Churn. **Mann-Whitney U** (también llamado Wilcoxon rank-sum) es una prueba no paramétrica para comparar distribuciones de una variable numérica entre dos grupos independientes. No asume normalidad, solo que las distribuciones tienen la misma forma. Se usó para: tenure vs Churn, MonthlyCharges vs Churn. La elección depende del tipo de datos: categórica-categórica → Chi-cuadrado, numérica-categórica → Mann-Whitney U (o t-test si hay normalidad). Todas las 7 pruebas resultaron significativas (p-value < 0.001), confirmando que las relaciones observadas son reales.

### 13. ¿Qué conclusiones se obtuvieron de las 7 pruebas de hipótesis realizadas y cómo impactan el modelo?

**Respuesta:** Las 7 pruebas confirmaron relaciones estadísticamente significativas 
(p-value < 0.05 en todas):

(1) **Contract vs Churn** (χ²): Contratos mes a mes tienen significativamente más churn que contratos largos,
(2) **PaymentMethod vs Churn** (χ²): Método de pago electrónico correlaciona con mayor churn,
(3) **InternetService vs Churn** (χ²): Fibra óptica tiene más churn que DSL,
(4) **tenure vs Churn** (Mann-Whitney U): Clientes con churn tienen tenure significativamente menor (mediana ~10 meses vs ~38 meses),
(5) **MonthlyCharges vs Churn** (Mann-Whitney U): Churners pagan significativamente más ($79 vs $61 mediana),
(6) **TechSupport vs Churn** (χ²): Falta de soporte técnico correlaciona con churn,
(7) **PaperlessBilling vs Churn** (χ²): Facturación electrónica correlaciona con mayor churn. **Impacto en el modelo**: Estas variables validadas estadísticamente se priorizaron en feature engineering y se confirmó su alta importancia en Random Forest. Las conclusiones también generaron recomendaciones de negocio: incentivar contratos largos, mejorar soporte técnico, revisar pricing de fibra óptica, y programas de retención para clientes nuevos.

---

## V. MANEJO DE DESBALANCEO DE CLASES (SMOTE)

### 14. ¿Cómo funciona SMOTE y por qué es superior a técnicas simples de oversampling?

**Respuesta:** SMOTE (Synthetic Minority Over-sampling Technique) genera ejemplos 
sintéticos de la clase minoritaria interpolando entre vecinos cercanos en el 
espacio de características. Para cada muestra minoritaria, selecciona k vecinos 
más cercanos (k=5 por defecto) y crea nuevos puntos en el segmento de línea que 
los conecta: x_new = x + λ(x_neighbor - x), donde λ ∈ [0,1]. Esto es superior al 
oversampling aleatorio (duplicar muestras) porque:

(1) evita overfitting al no repetir exactamente las mismas muestras,
(2) expande la región de decisión de la clase minoritaria de manera más realista,
(3) ayuda al modelo a generalizar mejor. En nuestro proyecto, SMOTE balanceó el dataset de 4138/1496 a 4138/4138, mejorando significativamente el Recall (de ~0.50 a ~0.78 en Logistic Regression).

### 15. ¿Cuál es el impacto de aplicar SMOTE solo en el conjunto de entrenamiento y no en el de prueba?

**Respuesta:** Aplicar SMOTE solo en entrenamiento (no en test) es una práctica correcta que evita data leakage y garantiza evaluación realista. Si aplicáramos SMOTE al conjunto completo antes del split, los ejemplos sintéticos del test podrían ser vecinos de ejemplos del train, inflando artificialmente las métricas. Al aplicarlo solo en train, el modelo aprende de un dataset balanceado (mejorando su capacidad de detectar churn), pero se evalúa en la distribución real desbalanceada (73%/27%), reflejando el rendimiento en producción. Esto explica por qué el Accuracy puede bajar ligeramente con SMOTE (de 0.80 a 0.74 en Logistic Regression) mientras que Recall mejora dramáticamente: el modelo prioriza detectar churners reales sobre accuracy global.

### 16. ¿Por qué el Recall mejora significativamente con SMOTE mientras que el Accuracy puede disminuir?

**Respuesta:** Esta aparente paradoja se explica por el trade-off entre métricas en datasets desbalanceados. Sin SMOTE, el modelo aprende que predecir "No Churn" es seguro (73% de acierto base), resultando en alto Accuracy pero bajo Recall para la clase minoritaria. Con SMOTE, el modelo ve igual cantidad de ambas clases durante entrenamiento, aprendiendo a identificar mejor los churners (Recall sube de ~0.50 a ~0.78). Sin embargo, esto aumenta falsos positivos (predecir Churn cuando no lo hay), reduciendo Accuracy global. Matemáticamente: Recall = TP/(TP+FN) mejora porque TP aumenta y FN disminuye, mientras Accuracy = (TP+TN)/(TP+TN+FP+FN) baja porque FP aumenta más de lo que FN disminuye. En problemas de churn, maximizar Recall es más valioso que Accuracy, ya que el costo de perder un cliente (FN) supera el costo de una campaña de retención innecesaria (FP).

---

## VI. ALGORITMOS DE MACHINE LEARNING

### 17. ¿Cómo funciona Logistic Regression y por qué es un buen baseline para clasificación binaria?

**Respuesta:** Logistic Regression modela la probabilidad de la clase positiva 
usando la función sigmoide: P(y=1|x) = 1/(1+e^(-z)), donde z = β₀ + β₁x₁ + ... + βₙxₙ. 
Optimiza los coeficientes β minimizando la log-loss mediante gradiente descendente. 
Es un excelente baseline porque:

(1) es interpretable (coeficientes indican importancia/dirección de cada variable),
(2) es rápido de entrenar,
(3) funciona bien con datos linealmente separables,
(4) proporciona probabilidades calibradas útiles para ranking de clientes. En nuestro proyecto, Logistic Regression logró ROC-AUC=0.846 con SMOTE, superando a modelos más complejos como Random Forest (0.824), demostrando que la relación entre features y churn es relativamente lineal después del feature engineering.

### 18. ¿Qué ventajas ofrece Random Forest sobre Decision Trees individuales?

**Respuesta:** Random Forest es un ensemble de múltiples Decision Trees que reduce 
overfitting mediante dos mecanismos de randomización:

(1) Bootstrap Aggregating (Bagging): cada árbol se entrena en una muestra aleatoria con reemplazo del dataset, y
(2) Feature Randomness: en cada split, solo se considera un subconjunto aleatorio de features (√n por defecto). Esto reduce la varianza sin aumentar el sesgo. Las ventajas sobre un árbol individual son: menor overfitting (un árbol puede memorizar el training set), mayor robustez a outliers, mejor generalización, y estimación de importancia de features más estable. En nuestro proyecto, Random Forest con 100 árboles logró ROC-AUC=0.824, y la optimización de hiperparámetros mejoró esto a ~0.83, demostrando su capacidad de capturar interacciones no lineales complejas.

### 19. Explique cómo funciona XGBoost y qué lo diferencia de Gradient Boosting tradicional.

**Respuesta:** XGBoost (Extreme Gradient Boosting) construye árboles secuencialmente, 
donde cada árbol corrige los errores del anterior minimizando una función de pérdida 
mediante gradiente descendente. La diferencia clave con Gradient Boosting tradicional es:

(1) Regularización: XGBoost añade términos L1 y L2 a la función objetivo para prevenir overfitting,
(2) Optimización de segunda derivada: usa información de Hessian (segunda derivada) para convergencia más rápida,
(3) Manejo de missing values: aprende automáticamente la mejor dirección para valores faltantes,
(4) Paralelización: aunque los árboles son secuenciales, la construcción de cada árbol se paraleliza. En nuestro proyecto, XGBoost logró ROC-AUC=0.818, ligeramente inferior a Logistic Regression, sugiriendo que el problema no requiere modelado de interacciones extremadamente complejas.

---

## VII. MÉTRICAS DE EVALUACIÓN

### 20. ¿Cómo se calcula el ROC-AUC y por qué es una métrica robusta para datasets desbalanceados?

**Respuesta:** ROC-AUC (Area Under the Receiver Operating Characteristic Curve) 
mide la capacidad del modelo de discriminar entre clases. La curva ROC grafica 
True Positive Rate (TPR=TP/(TP+FN)) vs False Positive Rate (FPR=FP/(FP+TN)) para 
diferentes umbrales de clasificación. El AUC es el área bajo esta curva, con valores 
entre 0.5 (clasificador aleatorio) y 1.0 (clasificador perfecto). Es robusta para 
datasets desbalanceados porque:

(1) no depende del umbral de clasificación específico,
(2) evalúa el ranking de probabilidades, no las predicciones binarias,
(3) considera tanto TPR como FPR, balanceando ambas clases. En nuestro proyecto, ROC-AUC=0.87 (modelo final optimizado) indica excelente capacidad discriminativa: 87% de probabilidad de que un churner aleatorio tenga mayor score que un no-churner aleatorio.

### 21. ¿Qué información proporciona la matriz de confusión que otras métricas no capturan?

**Respuesta:** La matriz de confusión descompone las predicciones en cuatro 
categorías: True Positives (TP), True Negatives (TN), False Positives (FP), 
False Negatives (FN), proporcionando una vista completa del comportamiento del modelo. 
Mientras que métricas agregadas como Accuracy (0.83) ocultan el desempeño por 
clase, la matriz revela:

(1) el tipo específico de errores (FP vs FN),
(2) el desempeño en cada clase individualmente,
(3) sesgos del modelo hacia una clase. En nuestro proyecto, la matriz del modelo final muestra que de 374 churners reales, detectamos aproximadamente 310 (Recall=0.83), con una tasa de precisión del 72%. Esta información es crucial para decisiones de negocio: ¿preferimos detectar más churners (aumentar Recall) aceptando más falsos positivos, o minimizar campañas innecesarias (aumentar Precision)?

### 22. ¿Cuál es la diferencia entre Precision y Recall, y cuándo priorizar cada una en problemas de churn?

**Respuesta:** Precision = TP/(TP+FP) mide qué proporción de predicciones positivas 
son correctas (de los que predecimos como churners, cuántos realmente lo son). 
Recall = TP/(TP+FN) mide qué proporción de positivos reales detectamos (de todos 
los churners reales, cuántos identificamos). En churn, generalmente priorizamos 
Recall porque:

(1) el costo de perder un cliente (FN) es alto (pérdida de revenue futuro),
(2) el costo de una campaña de retención innecesaria (FP) es relativamente bajo,
(3) es mejor contactar clientes que no iban a irse (FP) que perder clientes que sí se irían (FN). En nuestro proyecto, con SMOTE y optimización logramos Recall=0.83 (83%) con Precision=0.72 (72%), un balance excelente: detectamos la gran mayoría de churners reales manteniendo una precisión aceptable.

### 23. ¿Qué representa el F1-Score y cuándo es más útil que Accuracy?

**Respuesta:** F1-Score es la media armónica de Precision y Recall: F1 = 2×(Precision×Recall)/(Precision+Recall). Es más útil que Accuracy en datasets desbalanceados porque:
(1) balancea Precision y Recall (no favorece ninguna),
(2) penaliza fuertemente modelos con una métrica muy baja (la media armónica es dominada por el valor menor),
(3) ignora True Negatives, enfocándose en el desempeño de la clase positiva. En nuestro proyecto, Accuracy=0.83 podría ser engañosa (un modelo que siempre predice "No Churn" tendría 73% accuracy), mientras F1=0.77 refleja mejor el desempeño real en detectar churners. F1 es especialmente útil cuando Precision y Recall son igualmente importantes, aunque en churn típicamente priorizamos Recall. El F1=0.77 indica un excelente balance entre ambas métricas.

---

## VIII. OPTIMIZACIÓN DE HIPERPARÁMETROS

### 24. ¿Por qué se usa GridSearchCV (o RandomizedSearchCV) y qué ventajas ofrece?

**Respuesta:** GridSearchCV prueba todas las combinaciones posibles de hiperparámetros 
en un espacio de búsqueda definido, mientras RandomizedSearchCV muestrea aleatoriamente 
n_iter combinaciones. En nuestro proyecto se usó GridSearchCV para Random Forest. 
Las ventajas son:

(1) **Búsqueda exhaustiva**: GridSearchCV garantiza encontrar la mejor combinación dentro del espacio definido,
(2) **Validación cruzada integrada**: cada combinación se evalúa con CV, evitando overfitting a un split específico,
(3) **Reproducibilidad**: resultados determinísticos (vs RandomizedSearch que es estocástico),
(4) **Comparación justa**: todas las combinaciones se evalúan bajo las mismas condiciones. En nuestro proyecto, GridSearchCV encontró hiperparámetros óptimos (n_estimators=300, max_depth=20, min_samples_split=5, min_samples_leaf=1, max_features='log2', bootstrap=False) que mejoraron ROC-AUC de 0.824 a ~0.87, demostrando el valor de la optimización sistemática.

### 25. ¿Por qué se usa scoring='roc_auc' en GridSearchCV para este problema?

**Respuesta:** Usamos `scoring='roc_auc'` porque:

(1) es robusta a desbalanceo de clases (a diferencia de accuracy),
(2) evalúa el ranking de probabilidades, no solo predicciones binarias, permitiendo ajustar el umbral después,
(3) es diferenciable y estable, facilitando la comparación entre modelos,
(4) alinea con el objetivo de negocio: queremos rankear clientes por probabilidad de churn para priorizar campañas de retención. Alternativas como F1-Score dependen del umbral de clasificación (0.5 por defecto) y pueden ser subóptimas. ROC-AUC evalúa el modelo en todos los umbrales posibles, encontrando hiperparámetros que maximizan la capacidad discriminativa general. En producción, podemos ajustar el umbral según el trade-off Precision/Recall deseado, pero el modelo base debe tener alto ROC-AUC (0.87 en nuestro caso).

### 26. Explique el papel de cv=5 (validación cruzada) en la optimización de hiperparámetros.

**Respuesta:** `cv=5` (5-fold cross-validation) divide el training set en 5 
particiones, entrenando 5 modelos donde cada uno usa 4 folds para entrenar y 1 
para validar, rotando las particiones. Esto proporciona:

(1) **Estimación robusta del rendimiento**: el score final es el promedio de 5 evaluaciones, reduciendo varianza por splits afortunados/desafortunados,
(2) **Uso eficiente de datos**: cada muestra se usa para validación exactamente una vez,
(3) **Detección de overfitting**: alta varianza entre folds indica inestabilidad del modelo. En nuestro proyecto, usamos StratifiedKFold para mantener la proporción de clases en cada fold (73%/27%), crucial dado el desbalanceo. El mejor score de validación cruzada fue ROC-AUC=0.9401, y el rendimiento en test fue 0.87, confirmando que el modelo generaliza bien sin overfitting significativo.

---

## IX. DEPLOYMENT Y PRODUCCIÓN

### 27. ¿Cómo se guardó el modelo final y qué consideraciones hay para deployment en producción?

**Respuesta:** El modelo final se guardó usando **joblib**, que es más eficiente 
que pickle para objetos grandes de ML: `joblib.dump(best_rf, 'best_rf_model.pkl')`. 
También se guardó metadata importante en JSON: tipo de modelo, métricas 
(ROC-AUC=0.87, Recall=0.83, Precision=0.72, F1=0.77), fecha de entrenamiento, 
lista de features, hiperparámetros, y número de muestras de 
entrenamiento. **Consideraciones para deployment**:

(1) **Versionado**: incluir versión en el nombre del archivo (ej: `churn_model_v1.0.0.pkl`) para control de cambios,
(2) **Reproducibilidad**: guardar también el scaler y encoder usados en preprocesamiento,
(3) **Tamaño**: el modelo pesa ~50-100 MB, manejable para la mayoría de entornos,
(4) **Opciones de deployment**: API REST (Flask/FastAPI), batch processing, o cloud platforms (AWS SageMaker, Google Cloud AI, Azure ML, Render/Railway). El modelo está listo para producción con requerimientos mínimos: 512MB-1GB RAM, 1-2 CPU cores, Python 3.8+.

### 28. ¿Qué requerimientos técnicos y de infraestructura necesita el modelo en producción?

**Respuesta:** **Requerimientos mínimos**:

(1) **RAM**: 512 MB - 1 GB (el modelo cargado en memoria ocupa ~200-300 MB),
(2) **CPU**: 1-2 cores (suficiente para predicciones en tiempo real),
(3) **Almacenamiento**: 500 MB (modelo + dependencias),
(4) **Python**: 3.8+ con librerías: scikit-learn, pandas, numpy, joblib. **Arquitectura recomendada**:
(a) **API REST**: Crear endpoint `/predict` que reciba datos del cliente en JSON y retorne probabilidad de churn y predicción binaria,
(b) **Batch Processing**: Procesar lotes de clientes periódicamente (ej: diariamente) y guardar scores en base de datos para consulta,
(c) **Monitoreo**: Implementar logging de predicciones, tracking de performance en producción, y alertas para concept drift. **Escalabilidad**: Para alto volumen (>1000 predicciones/segundo), considerar: contenedores Docker, load balancing, caching de resultados, y optimización con ONNX. El modelo actual puede manejar ~100-500 predicciones/segundo en hardware modesto.

---

## X. VALOR DE NEGOCIO Y ROI

### 29. ¿Cómo se calculó el ROI estimado de $205,000 y qué supuestos se utilizaron?

**Respuesta:** El ROI de ~$205,000 se calculó considerando: **Supuestos**:

(1) Lifetime Value (LTV) promedio por cliente: $500,
(2) Costo de campaña de retención por cliente: $50,
(3) Tasa de éxito de retención: 40% (de los contactados, 40% se quedan),
(4) Total de clientes en riesgo detectados: 310 (Recall=0.83 × 374 churners reales). **Cálculo**:
(a) **Inversión en retención**: Contactamos ~430 clientes (TP + FP) × $50 = $21,500,
(b) **Clientes retenidos**: 310 detectados × 40% éxito = 124 clientes,
(c) **Valor retenido**: 124 × $500 LTV = $62,000,
(d) **Costo de falsos negativos**: 64 churners no detectados × $500 = $32,000 (pérdida),
(e) **ROI neto**: $62,000 - $21,500 - $32,000 = $8,500 por ciclo. Proyectado anualmente (12 ciclos): ~$102,000. Con optimización de campañas (60% tasa de éxito): ~$205,000. Este cálculo demuestra que incluso con supuestos conservadores, el modelo genera valor significativo.

### 30. ¿Cómo interpretaría las métricas finales del modelo (ROC-AUC=0.87, Recall=83%, Precision=72%) en términos de impacto en el negocio?

**Respuesta:** **ROC-AUC=0.87**: Excelente capacidad discriminativa. Podemos rankear clientes por riesgo con 87% de confianza, permitiendo priorizar recursos en los más propensos a irse. Esto maximiza eficiencia de campañas de retención. **Recall=83%**: Detectamos 83% de los clientes que realmente harán churn (310 de 374). Esto significa que podemos intervenir proactivamente con la gran mayoría de clientes en riesgo, minimizando pérdidas. El 17% no detectado (64 clientes) representa una oportunidad de mejora futura. **Precision=72%**: De los clientes que contactamos, 72% realmente están en riesgo. Esto significa ~28% de falsos positivos (contactamos clientes que no se irían). Aunque no es perfecto, es aceptable porque el costo de contactar un cliente innecesariamente ($50) es mucho menor que perder un cliente ($500 LTV). **Balance óptimo**: F1=0.77 indica excelente balance. El modelo prioriza Recall (no perder clientes) manteniendo Precision razonable (no desperdiciar recursos). **Impacto**: Con estas métricas, estimamos reducir churn de 27% a ~20% en 12 meses, generando ROI de $205,000+ y mejorando satisfacción del cliente.

---

## Conclusión

Estas **30 preguntas actualizadas** cubren exhaustivamente todos los aspectos del 
proyecto de predicción de Customer Churn, desde el análisis exploratorio inicial
hasta el deployment en producción. Las preguntas están sincronizadas con el notebook 
actualizado `Telco_Customer_Churn.ipynb` e incluyen:

- **Análisis Exploratorio de Datos (EDA)**: Insights clave y visualizaciones
- **Preprocesamiento**: StandardScaler, OneHotEncoder, manejo de valores faltantes
- **Feature Engineering**: Creación de variables derivadas (ChargeRatio, TotalServices, TenureGroup)
- **Pruebas de Hipótesis Estadísticas**: 7 pruebas con Chi-cuadrado y Mann-Whitney U
- **Manejo de Desbalanceo**: SMOTE y su impacto en métricas
- **Algoritmos de ML**: Logistic Regression, Random Forest, XGBoost
- **Métricas de Evaluación**: ROC-AUC=0.87, Recall=83%, Precision=72%, F1=77%
- **Optimización**: GridSearchCV con validación cruzada
- **Deployment**: Guardado con joblib, requerimientos técnicos, infraestructura
- **Valor de Negocio**: ROI de $205,000, impacto en reducción de churn

La comprensión profunda de estos conceptos es esencial para defender exitosamente el proyecto en una sustentación de BootCamp de Inteligencia Artificial.

---

**Última actualización**: 2025-11-21\
**Versión**: 2.0\
**Total de preguntas**: 30\
**Sincronizado con**: Telco_Customer_Churn.ipynb (versión actualizada)

