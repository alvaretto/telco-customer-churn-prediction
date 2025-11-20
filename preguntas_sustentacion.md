# Preguntas Técnicas para Sustentación del Proyecto
## Análisis y Predicción de Customer Churn en Telco

### Introducción
Este documento contiene 25 preguntas técnicas fundamentales que evalúan la comprensión profunda de los conceptos de Machine Learning aplicados en el proyecto de predicción de Customer Churn. Las preguntas están organizadas por temas y cubren desde fundamentos teóricos hasta decisiones técnicas específicas del proyecto.

---

## I. PREPROCESAMIENTO Y LIMPIEZA DE DATOS

### 1. ¿Por qué se utiliza StandardScaler en este proyecto y cómo funciona matemáticamente?

**Respuesta:** StandardScaler normaliza las características numéricas restando la media (μ) y dividiendo por la desviación estándar (σ): z = (x - μ) / σ. Esto es crucial porque los algoritmos basados en distancias (KNN, SVM) y los que usan gradiente descendente (Logistic Regression, Neural Networks) son sensibles a la escala de las variables. En nuestro proyecto, variables como `MonthlyCharges` (rango ~20-120) y `tenure` (rango 0-72) tienen escalas muy diferentes, por lo que sin normalización, las variables con mayor magnitud dominarían el modelo. StandardScaler garantiza que todas las características tengan media 0 y desviación estándar 1, permitiendo que el modelo aprenda de manera equitativa de todas las variables.

### 2. ¿Por qué se usa OneHotEncoder con el parámetro drop='first'? ¿Qué problema evita esto?

**Respuesta:** OneHotEncoder con `drop='first'` evita el problema de multicolinealidad perfecta (dummy variable trap). Cuando codificamos una variable categórica con n categorías, crear n columnas binarias genera dependencia lineal perfecta, ya que conociendo n-1 columnas podemos deducir la n-ésima. Por ejemplo, si `Contract` tiene 3 valores (Month-to-month, One year, Two year), crear 3 columnas haría que la suma siempre sea 1. Al eliminar la primera categoría, usamos n-1 columnas, evitando redundancia y mejorando la estabilidad numérica del modelo. Esto es especialmente importante para modelos lineales como Logistic Regression, donde la multicolinealidad puede causar coeficientes inestables y problemas de convergencia.

### 3. ¿Cómo se manejaron los valores faltantes en TotalCharges y por qué se eligió esa estrategia?

**Respuesta:** Los valores faltantes en `TotalCharges` (11 registros con espacios en blanco) se imputaron usando la lógica de negocio: para clientes nuevos con `tenure=0`, `TotalCharges` debe ser igual a `MonthlyCharges`. Esta estrategia es superior a la imputación por media/mediana porque preserva la relación matemática real entre las variables (TotalCharges ≈ MonthlyCharges × tenure). Eliminar estos registros habría sido subóptimo dado que representan clientes nuevos valiosos para el análisis de churn. La imputación basada en dominio mantiene la integridad de los datos y evita introducir sesgos artificiales que podrían afectar el rendimiento del modelo.

### 4. ¿Por qué se utiliza train_test_split con stratify=y? ¿Qué garantiza este parámetro?

**Respuesta:** El parámetro `stratify=y` garantiza que la distribución de la variable objetivo (Churn) se mantenga proporcional en los conjuntos de entrenamiento y prueba. En nuestro dataset, hay un desbalanceo de clases (~73% No Churn, ~27% Churn). Sin estratificación, el split aleatorio podría crear conjuntos con distribuciones diferentes (ej: 70% vs 76%), lo que sesgaría la evaluación del modelo. Con `stratify=y`, ambos conjuntos mantienen la proporción 73.5%/26.5%, asegurando que el modelo se entrene y evalúe en datos representativos. Esto es crítico para métricas como Recall y Precision, que son sensibles al desbalanceo de clases.

---

## II. FEATURE ENGINEERING

### 5. Explique la lógica detrás de la característica ChargeRatio y qué información captura.

**Respuesta:** `ChargeRatio = MonthlyCharges / (TotalCharges + 1)` captura la relación entre el cargo mensual actual y el cargo total histórico del cliente. Un ratio alto indica clientes nuevos o con aumentos recientes en sus cargos mensuales, lo que puede correlacionarse con insatisfacción y mayor probabilidad de churn. El +1 en el denominador evita división por cero para clientes nuevos. Esta característica es valiosa porque combina información temporal (tenure implícito) con información de pricing, revelando patrones que las variables individuales no capturan. Por ejemplo, un cliente con ChargeRatio alto podría estar experimentando un aumento de precio reciente, un factor conocido de churn.

### 6. ¿Qué ventaja ofrece la característica TotalServices sobre usar las variables individuales de servicios?

**Respuesta:** `TotalServices` (suma de servicios contratados) ofrece una representación compacta del nivel de engagement del cliente con la empresa. Mientras que las variables individuales (PhoneService, InternetService, etc.) son binarias o categóricas, TotalServices crea una escala ordinal (0-8) que captura el concepto de "profundidad de relación". Estudios de churn muestran que clientes con más servicios tienen menor probabilidad de abandonar (mayor switching cost). Esta característica reduce dimensionalidad (8 variables → 1) y facilita que el modelo aprenda patrones no lineales. Además, permite interacciones más simples: un cliente con TotalServices=1 y MonthlyCharges alto es un perfil de riesgo diferente a uno con TotalServices=6 y el mismo cargo.

### 7. ¿Por qué se creó TenureGroup categorizando la variable tenure? ¿Qué asume este enfoque?

**Respuesta:** `TenureGroup` discretiza `tenure` en bins (0-12, 12-24, 24-48, 48-72 meses) porque la relación entre tenure y churn no es lineal. Los primeros meses son críticos (alta probabilidad de churn), luego se estabiliza, y clientes de largo plazo tienen muy bajo churn. Al categorizar, permitimos que el modelo capture estos umbrales sin asumir linealidad. Este enfoque asume que hay "fases" distintas en el ciclo de vida del cliente. Sin embargo, tiene el trade-off de perder granularidad (un cliente con 11 meses vs 13 meses se trata muy diferente). Por eso mantenemos también `tenure` numérico, permitiendo que el modelo use ambas representaciones.

---

## III. MANEJO DE DESBALANCEO DE CLASES

### 8. ¿Cómo funciona SMOTE y por qué es superior a técnicas simples de oversampling?

**Respuesta:** SMOTE (Synthetic Minority Over-sampling Technique) genera ejemplos sintéticos de la clase minoritaria interpolando entre vecinos cercanos en el espacio de características. Para cada muestra minoritaria, selecciona k vecinos más cercanos (k=5 por defecto) y crea nuevos puntos en el segmento de línea que los conecta: x_new = x + λ(x_neighbor - x), donde λ ∈ [0,1]. Esto es superior al oversampling aleatorio (duplicar muestras) porque: (1) evita overfitting al no repetir exactamente las mismas muestras, (2) expande la región de decisión de la clase minoritaria de manera más realista, (3) ayuda al modelo a generalizar mejor. En nuestro proyecto, SMOTE balanceó el dataset de 4138/1496 a 4138/4138, mejorando significativamente el Recall (de ~0.55 a ~0.81 en Logistic Regression).

### 9. ¿Cuál es el impacto de aplicar SMOTE solo en el conjunto de entrenamiento y no en el de prueba?

**Respuesta:** Aplicar SMOTE solo en entrenamiento (no en test) es una práctica correcta que evita data leakage y garantiza evaluación realista. Si aplicáramos SMOTE al conjunto completo antes del split, los ejemplos sintéticos del test podrían ser vecinos de ejemplos del train, inflando artificialmente las métricas. Al aplicarlo solo en train, el modelo aprende de un dataset balanceado (mejorando su capacidad de detectar churn), pero se evalúa en la distribución real desbalanceada (73%/27%), reflejando el rendimiento en producción. Esto explica por qué el Accuracy puede bajar ligeramente con SMOTE (de 0.80 a 0.74 en Logistic Regression) mientras que Recall mejora dramáticamente: el modelo prioriza detectar churners reales sobre accuracy global.

### 10. ¿Por qué el Recall mejora significativamente con SMOTE mientras que el Accuracy puede disminuir?

**Respuesta:** Esta aparente paradoja se explica por el trade-off entre métricas en datasets desbalanceados. Sin SMOTE, el modelo aprende que predecir "No Churn" es seguro (73% de acierto base), resultando en alto Accuracy pero bajo Recall para la clase minoritaria. Con SMOTE, el modelo ve igual cantidad de ambas clases durante entrenamiento, aprendiendo a identificar mejor los churners (Recall sube de ~0.55 a ~0.81). Sin embargo, esto aumenta falsos positivos (predecir Churn cuando no lo hay), reduciendo Accuracy global. Matemáticamente: Recall = TP/(TP+FN) mejora porque TP aumenta y FN disminuye, mientras Accuracy = (TP+TN)/(TP+TN+FP+FN) baja porque FP aumenta más de lo que FN disminuye. En problemas de churn, maximizar Recall es más valioso que Accuracy, ya que el costo de perder un cliente (FN) supera el costo de una campaña de retención innecesaria (FP).

---

## IV. ALGORITMOS DE MACHINE LEARNING

### 11. ¿Cómo funciona Logistic Regression y por qué es un buen baseline para clasificación binaria?

**Respuesta:** Logistic Regression modela la probabilidad de la clase positiva usando la función sigmoide: P(y=1|x) = 1/(1+e^(-z)), donde z = β₀ + β₁x₁ + ... + βₙxₙ. Optimiza los coeficientes β minimizando la log-loss mediante gradiente descendente. Es un excelente baseline porque: (1) es interpretable (coeficientes indican importancia/dirección de cada variable), (2) es rápido de entrenar, (3) funciona bien con datos linealmente separables, (4) proporciona probabilidades calibradas útiles para ranking de clientes. En nuestro proyecto, Logistic Regression logró ROC-AUC=0.846 con SMOTE, superando a modelos más complejos como Random Forest (0.824), demostrando que la relación entre features y churn es relativamente lineal después del feature engineering.

### 12. ¿Qué ventajas ofrece Random Forest sobre Decision Trees individuales?

**Respuesta:** Random Forest es un ensemble de múltiples Decision Trees que reduce overfitting mediante dos mecanismos de randomización: (1) Bootstrap Aggregating (Bagging): cada árbol se entrena en una muestra aleatoria con reemplazo del dataset, y (2) Feature Randomness: en cada split, solo se considera un subconjunto aleatorio de features (√n por defecto). Esto reduce la varianza sin aumentar el sesgo. Las ventajas sobre un árbol individual son: menor overfitting (un árbol puede memorizar el training set), mayor robustez a outliers, mejor generalización, y estimación de importancia de features más estable. En nuestro proyecto, Random Forest con 100 árboles logró ROC-AUC=0.824, y la optimización de hiperparámetros mejoró esto a ~0.83, demostrando su capacidad de capturar interacciones no lineales complejas.

### 13. Explique cómo funciona XGBoost y qué lo diferencia de Gradient Boosting tradicional.

**Respuesta:** XGBoost (Extreme Gradient Boosting) construye árboles secuencialmente, donde cada árbol corrige los errores del anterior minimizando una función de pérdida mediante gradiente descendente. La diferencia clave con Gradient Boosting tradicional es: (1) Regularización: XGBoost añade términos L1 y L2 a la función objetivo para prevenir overfitting, (2) Optimización de segunda derivada: usa información de Hessian (segunda derivada) para convergencia más rápida, (3) Manejo de missing values: aprende automáticamente la mejor dirección para valores faltantes, (4) Paralelización: aunque los árboles son secuenciales, la construcción de cada árbol se paraleliza. En nuestro proyecto, XGBoost logró ROC-AUC=0.818, ligeramente inferior a Logistic Regression, sugiriendo que el problema no requiere modelado de interacciones extremadamente complejas.

---

## V. MÉTRICAS DE EVALUACIÓN

### 14. ¿Cómo se calcula el ROC-AUC y por qué es una métrica robusta para datasets desbalanceados?

**Respuesta:** ROC-AUC (Area Under the Receiver Operating Characteristic Curve) mide la capacidad del modelo de discriminar entre clases. La curva ROC grafica True Positive Rate (TPR=TP/(TP+FN)) vs False Positive Rate (FPR=FP/(FP+TN)) para diferentes umbrales de clasificación. El AUC es el área bajo esta curva, con valores entre 0.5 (clasificador aleatorio) y 1.0 (clasificador perfecto). Es robusta para datasets desbalanceados porque: (1) no depende del umbral de clasificación específico, (2) evalúa el ranking de probabilidades, no las predicciones binarias, (3) considera tanto TPR como FPR, balanceando ambas clases. En nuestro proyecto, ROC-AUC=0.846 (Logistic Regression con SMOTE) indica excelente capacidad discriminativa: 84.6% de probabilidad de que un churner aleatorio tenga mayor score que un no-churner aleatorio.

### 15. ¿Qué información proporciona la matriz de confusión que otras métricas no capturan?

**Respuesta:** La matriz de confusión descompone las predicciones en cuatro categorías: True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN), proporcionando una vista completa del comportamiento del modelo. Mientras que métricas agregadas como Accuracy (0.78) ocultan el desempeño por clase, la matriz revela: (1) el tipo específico de errores (FP vs FN), (2) el desempeño en cada clase individualmente, (3) sesgos del modelo hacia una clase. En nuestro proyecto, la matriz del modelo final muestra que de 374 churners reales, detectamos 243 (Recall=0.65) pero generamos 171 falsos positivos. Esta información es crucial para decisiones de negocio: ¿preferimos detectar más churners (aumentar Recall) aceptando más falsos positivos, o minimizar campañas innecesarias (aumentar Precision)?

### 16. ¿Cuál es la diferencia entre Precision y Recall, y cuándo priorizar cada una en problemas de churn?

**Respuesta:** Precision = TP/(TP+FP) mide qué proporción de predicciones positivas son correctas (de los que predecimos como churners, cuántos realmente lo son). Recall = TP/(TP+FN) mide qué proporción de positivos reales detectamos (de todos los churners reales, cuántos identificamos). En churn, generalmente priorizamos Recall porque: (1) el costo de perder un cliente (FN) es alto (pérdida de revenue futuro), (2) el costo de una campaña de retención innecesaria (FP) es relativamente bajo, (3) es mejor contactar clientes que no iban a irse (FP) que perder clientes que sí se irían (FN). En nuestro proyecto, con SMOTE logramos Recall=0.81 en Logistic Regression, sacrificando Precision (0.51), lo cual es aceptable: contactamos más clientes de los necesarios, pero capturamos la mayoría de churners reales.

### 17. ¿Qué representa el F1-Score y cuándo es más útil que Accuracy?

**Respuesta:** F1-Score es la media armónica de Precision y Recall: F1 = 2×(Precision×Recall)/(Precision+Recall). Es más útil que Accuracy en datasets desbalanceados porque: (1) balancea Precision y Recall (no favorece ninguna), (2) penaliza fuertemente modelos con una métrica muy baja (la media armónica es dominada por el valor menor), (3) ignora True Negatives, enfocándose en el desempeño de la clase positiva. En nuestro proyecto, Accuracy=0.78 podría ser engañosa (un modelo que siempre predice "No Churn" tendría 73% accuracy), mientras F1=0.62 refleja mejor el desempeño real en detectar churners. F1 es especialmente útil cuando Precision y Recall son igualmente importantes, aunque en churn típicamente priorizamos Recall.

---

## VI. OPTIMIZACIÓN DE HIPERPARÁMETROS

### 18. ¿Por qué se usa RandomizedSearchCV en lugar de GridSearchCV? ¿Qué ventajas ofrece?

**Respuesta:** RandomizedSearchCV muestrea aleatoriamente n_iter combinaciones del espacio de hiperparámetros, mientras GridSearchCV prueba todas las combinaciones posibles. Las ventajas de RandomizedSearch son: (1) Eficiencia computacional: con 50 iteraciones exploramos un espacio grande sin probar todas las combinaciones (que serían 4×4×3×3×2×2=576 en nuestro caso), (2) Mejor exploración: puede encontrar regiones óptimas que GridSearch perdería si los valores discretos no están bien elegidos, (3) Escalabilidad: el tiempo de ejecución es predecible (50×5 folds = 250 entrenamientos) vs GridSearch que crece exponencialmente. En nuestro proyecto, RandomizedSearchCV con 50 iteraciones y cv=5 encontró hiperparámetros que mejoraron ROC-AUC de 0.824 a ~0.83, un balance óptimo entre tiempo de cómputo y mejora de rendimiento.

### 19. ¿Por qué se usa scoring='roc_auc' en RandomizedSearchCV para este problema?

**Respuesta:** Usamos `scoring='roc_auc'` porque: (1) es robusta a desbalanceo de clases (a diferencia de accuracy), (2) evalúa el ranking de probabilidades, no solo predicciones binarias, permitiendo ajustar el umbral después, (3) es diferenciable y estable, facilitando la comparación entre modelos, (4) alinea con el objetivo de negocio: queremos rankear clientes por probabilidad de churn para priorizar campañas de retención. Alternativas como F1-Score dependen del umbral de clasificación (0.5 por defecto) y pueden ser subóptimas. ROC-AUC evalúa el modelo en todos los umbrales posibles, encontrando hiperparámetros que maximizan la capacidad discriminativa general. En producción, podemos ajustar el umbral según el trade-off Precision/Recall deseado, pero el modelo base debe tener alto ROC-AUC.

### 20. Explique el papel de cv=5 (validación cruzada) en la optimización de hiperparámetros.

**Respuesta:** `cv=5` (5-fold cross-validation) divide el training set en 5 particiones, entrenando 5 modelos donde cada uno usa 4 folds para entrenar y 1 para validar, rotando las particiones. Esto proporciona: (1) Estimación robusta del rendimiento: el score final es el promedio de 5 evaluaciones, reduciendo varianza por splits afortunados/desafortunados, (2) Uso eficiente de datos: cada muestra se usa para validación exactamente una vez, (3) Detección de overfitting: alta varianza entre folds indica inestabilidad del modelo. En nuestro proyecto, usamos StratifiedKFold para mantener la proporción de clases en cada fold (73%/27%), crucial dado el desbalanceo. Los 5 scores de validación cruzada del modelo final (ROC-AUC: 0.84, 0.85, 0.83, 0.84, 0.85) muestran consistencia, confirmando que el modelo generaliza bien.

---

## VII. INTERPRETABILIDAD Y ANÁLISIS DE RESULTADOS

### 21. ¿Cómo se calcula la importancia de características en Random Forest y qué limitaciones tiene?

**Respuesta:** Random Forest calcula importancia mediante Mean Decrease in Impurity (MDI): para cada feature, suma la reducción de impureza (Gini o entropía) que produce en todos los splits de todos los árboles, ponderada por el número de muestras. Features que producen splits más "puros" tienen mayor importancia. Limitaciones: (1) Sesgo hacia features de alta cardinalidad (muchos valores únicos), (2) Correlación entre features puede inflar/deflactar importancias, (3) No distingue entre correlación y causalidad, (4) Puede ser inestable con pequeños cambios en datos. En nuestro proyecto, las top features fueron `tenure`, `MonthlyCharges`, y `TotalCharges`, lo cual tiene sentido de negocio: clientes nuevos con cargos altos son más propensos a churn. Sin embargo, debemos validar con análisis de negocio, no solo confiar ciegamente en las importancias.

### 22. ¿Qué insights de negocio se pueden extraer de las características más importantes del modelo?

**Respuesta:** Las top 3 características (`tenure`, `MonthlyCharges`, `TotalCharges`) revelan insights accionables: (1) **Tenure**: clientes nuevos (0-12 meses) tienen mayor riesgo de churn, sugiriendo implementar programas de onboarding y seguimiento temprano, (2) **MonthlyCharges**: cargos mensuales altos correlacionan con churn, indicando sensibilidad al precio; estrategias de descuentos o bundles podrían retener estos clientes, (3) **TotalCharges**: bajo gasto total histórico (clientes nuevos o de bajo valor) son más volátiles, sugiriendo enfocarse en aumentar engagement temprano. Features derivadas como `Contract_Month-to-month` y `InternetService_Fiber optic` también son importantes, indicando que contratos flexibles y servicios premium son factores de riesgo. Estos insights permiten segmentar clientes y diseñar intervenciones específicas por segmento.

### 23. ¿Cómo interpretaría un ROC-AUC de 0.846 en términos de valor de negocio?

**Respuesta:** ROC-AUC=0.846 significa que si seleccionamos aleatoriamente un cliente que hará churn y uno que no, hay 84.6% de probabilidad de que nuestro modelo asigne mayor score al churner. En términos de negocio: (1) **Priorización efectiva**: podemos rankear clientes por riesgo y enfocar recursos en el top 20-30%, maximizando ROI de campañas de retención, (2) **Reducción de costos**: evitamos contactar clientes de bajo riesgo, reduciendo costos de marketing, (3) **Incremento de retención**: detectando ~65% de churners (Recall), podemos intervenir antes de que se vayan, recuperando potencialmente millones en revenue. Si el costo de retener un cliente es $50 y su lifetime value es $500, incluso con Precision=0.51 (mitad de contactados son falsos positivos), el ROI es positivo: por cada $100 invertidos, salvamos ~1 cliente de $500 valor.

---

## VIII. VALIDACIÓN Y GENERALIZACIÓN

### 24. ¿Por qué es importante usar StratifiedKFold en lugar de KFold regular para este problema?

**Respuesta:** StratifiedKFold mantiene la proporción de clases en cada fold, mientras KFold regular hace splits aleatorios sin considerar la distribución de y. En nuestro dataset desbalanceado (73%/27%), KFold podría crear folds con distribuciones muy diferentes (ej: un fold con 80% No Churn, otro con 65%), resultando en: (1) Estimaciones de rendimiento inestables y poco confiables, (2) Algunos folds más difíciles que otros, inflando la varianza de scores, (3) Modelos entrenados en distribuciones no representativas. StratifiedKFold garantiza que cada fold tenga ~73%/27%, asegurando: (1) Evaluación consistente y justa, (2) Modelos entrenados en datos representativos, (3) Varianza de scores refleja verdadera incertidumbre del modelo, no artefactos del split. Los 5 scores de CV (0.84±0.01) confirman estabilidad gracias a stratification.

### 25. ¿Qué evidencia tenemos de que el modelo generalizará bien a datos nuevos no vistos?

**Respuesta:** Múltiples evidencias de buena generalización: (1) **Validación cruzada consistente**: 5-fold CV con scores estables (ROC-AUC: 0.84, 0.85, 0.83, 0.84, 0.85, std=0.008) indica que el modelo no depende de un split específico, (2) **Test set performance**: ROC-AUC en test (0.83) es similar al CV score (0.84), confirmando que no hay overfitting, (3) **Regularización**: uso de SMOTE solo en train, StandardScaler fit solo en train, y hiperparámetros optimizados con CV previenen data leakage, (4) **Simplicidad del modelo**: Logistic Regression con regularización implícita es menos propenso a overfitting que modelos complejos, (5) **Feature engineering basado en dominio**: características creadas con lógica de negocio (no data mining ciego) son más robustas a cambios en distribución. Sin embargo, debemos monitorear performance en producción y reentrenar periódicamente si la distribución de datos cambia (concept drift).

---

## Conclusión

Estas 25 preguntas cubren los aspectos fundamentales del proyecto de predicción de Customer Churn, desde fundamentos matemáticos hasta decisiones técnicas específicas y su impacto en el negocio. La comprensión profunda de estos conceptos es esencial para defender exitosamente el proyecto en una sustentación de BootCamp de Inteligencia Artificial.

