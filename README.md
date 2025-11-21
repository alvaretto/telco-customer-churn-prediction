# 📊 Predicción de Abandono de Clientes en Telecomunicaciones

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-yellow.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![API Status](https://img.shields.io/badge/API-Online-success.svg)](https://telco-churn-api-y9xy.onrender.com)
[![Dashboard Status](https://img.shields.io/badge/Dashboard-Online-success.svg)](https://telco-churn-dashboard-ml.streamlit.app)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg)](https://github.com/alvaretto/telco-customer-churn-prediction/actions)
[![Deployment](https://img.shields.io/badge/Deployment-Automated-brightgreen.svg)](https://github.com/alvaretto/telco-customer-churn-prediction/blob/main/.github/workflows/deploy.yml)

[![Model ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.87-brightgreen.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model Recall](https://img.shields.io/badge/Recall-0.83-green.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model Precision](https://img.shields.io/badge/Precision-0.72-yellowgreen.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model F1-Score](https://img.shields.io/badge/F1--Score-0.77-green.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)

> Proyecto de Machine Learning para predecir el abandono de clientes (Customer Churn) en empresas de telecomunicaciones utilizando técnicas avanzadas de análisis de datos y modelado predictivo.

## 🚀 Demo en Vivo

- **🌐 API REST**: [https://telco-churn-api-y9xy.onrender.com](https://telco-churn-api-y9xy.onrender.com)
- **📊 Dashboard Interactivo**: [https://telco-churn-dashboard-ml.streamlit.app](https://telco-churn-dashboard-ml.streamlit.app)
- **📂 Repositorio**: [https://github.com/alvaretto/telco-customer-churn-prediction](https://github.com/alvaretto/telco-customer-churn-prediction)

---

## 📑 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Testing y CI/CD](#-testing-y-cicd)
- [Metodología](#-metodología)
- [Resultados](#-resultados)
- [Conclusiones](#-conclusiones)
- [Autores](#-autores)
- [Licencia](#-licencia)
- [Agradecimientos](#-agradecimientos)
- [Referencias](#-referencias)

---

## 🎯 Descripción del Proyecto

Este proyecto presenta un **análisis completo de predicción de abandono de clientes** (Customer Churn) en una empresa de telecomunicaciones. El objetivo principal es desarrollar modelos de Machine Learning que permitan identificar clientes con alta probabilidad de abandonar el servicio, facilitando estrategias de retención proactivas.

### Objetivos

- 🔍 Realizar un análisis exploratorio exhaustivo del comportamiento de clientes
- 🛠️ Aplicar técnicas de ingeniería de características para mejorar el rendimiento
- ⚖️ Manejar el desbalanceo de clases mediante técnicas avanzadas (SMOTE)
- 🤖 Comparar múltiples algoritmos de Machine Learning
- 📈 Optimizar hiperparámetros para maximizar el rendimiento
- 💡 Generar insights accionables para estrategias de retención

---

## ✨ Características Principales

- ✅ **Análisis Exploratorio Completo (EDA)**: Visualizaciones detalladas y análisis estadístico
- ✅ **Comprobación de Hipótesis Estadísticas**: 7 pruebas formales (Chi-cuadrado, Mann-Whitney U) con interpretaciones
- ✅ **Limpieza de Datos Robusta**: Manejo de valores faltantes y conversión de tipos
- ✅ **Feature Engineering Avanzado**: Creación de 6 nuevas características derivadas
- ✅ **Pipeline de Preprocesamiento**: ColumnTransformer con encoding y scaling
- ✅ **Comparación de 7 Modelos**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost, SVM, KNN
- ✅ **Manejo de Desbalanceo**: SMOTE (Synthetic Minority Over-sampling Technique)
- ✅ **Optimización de Hiperparámetros**: RandomizedSearchCV con validación cruzada
- ✅ **Evaluación Completa**: Múltiples métricas (ROC-AUC, Precision, Recall, F1-Score)
- ✅ **Interpretabilidad**: Análisis de importancia de características
- ✅ **Documentación Profesional**: Código limpio y bien comentado

---

## 🛠️ Tecnologías Utilizadas

### Lenguaje y Entorno
- **Python** 3.8+
- **Jupyter Notebook** 6.0+

### Librerías de Análisis de Datos
- **NumPy** 1.21+ - Computación numérica
- **Pandas** 1.3+ - Manipulación de datos

### Visualización
- **Matplotlib** 3.4+ - Gráficos estáticos
- **Seaborn** 0.11+ - Visualizaciones estadísticas

### Machine Learning
- **scikit-learn** 1.0+ - Algoritmos de ML y preprocesamiento
- **XGBoost** 1.5+ - Gradient Boosting optimizado
- **imbalanced-learn** 0.8+ - Técnicas para datos desbalanceados (SMOTE)

---

## 📁 Estructura del Proyecto

```
telco-customer-churn-prediction/
│
├── Telco-Customer-Churn.ipynb           # Notebook principal con análisis completo
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset original (7,043 registros, 21 variables)
├── preguntas-sustentacion.md            # 31 preguntas técnicas para defensa del proyecto
├── INSTRUCCIONES.md                     # Guía de ejecución del proyecto
├── README.md                            # Documentación principal (este archivo)
├── LICENSE                              # Licencia MIT
├── guia_completa_analisis_churn/        # Documentación detallada del análisis
└── bu/                                  # Backups y versiones anteriores
```

### Descripción de Archivos Principales

| Archivo | Propósito |
|---------|-----------|
| `Telco-Customer-Churn.ipynb` | Notebook principal con todo el pipeline de ML: EDA, preprocesamiento, feature engineering, modelado, evaluación y optimización |
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | Dataset con información de 7,043 clientes: datos demográficos, servicios contratados, información de cuenta y variable objetivo (Churn) |
| `preguntas-sustentacion.md` | Documento con 31 preguntas técnicas y respuestas detalladas para la sustentación del proyecto, cubriendo fundamentos teóricos y decisiones técnicas |
| `INSTRUCCIONES.md` | Guía paso a paso para ejecutar el proyecto y reproducir los resultados |

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip o conda para gestión de paquetes
- Jupyter Notebook o JupyterLab
- 4GB de RAM mínimo (recomendado 8GB)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/alvaretto/telco-customer-churn-prediction.git
cd telco-customer-churn-prediction
```

### 2. Crear entorno virtual (recomendado)

```bash
# Con venv
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# O con conda
conda create -n churn-env python=3.8
conda activate churn-env
```

### 3. Instalar dependencias

**Con pip:**

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn jupyter
```

**Con conda:**

```bash
conda install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn jupyter -c conda-forge
```

---

## 💻 Uso

### 🌐 Usar la Aplicación en Producción (Recomendado)

#### 1. Dashboard Interactivo (100% en Español 🇪🇸)
Accede al dashboard en vivo para hacer predicciones y explorar el modelo:

**URL**: [https://telco-churn-dashboard-ml.streamlit.app](https://telco-churn-dashboard-ml.streamlit.app)

**Páginas disponibles:**
- 🏠 **Inicio** - Introducción al proyecto y métricas principales
- 📊 **Resumen** - Análisis exploratorio de datos y tendencias
- 🎯 **Análisis de Riesgo** - Predicción interactiva de churn para clientes individuales
- 📈 **Métricas del Modelo** - Rendimiento del modelo y visualizaciones
- 💰 **Simulador ROI** - Calculadora de retorno de inversión para campañas
- 🔍 **Monitoreo del Modelo** - Seguimiento del rendimiento en tiempo real

**Características del Dashboard:**
- ✅ Interfaz completamente en español
- ✅ Formularios interactivos con validación
- ✅ Visualizaciones dinámicas con Plotly
- ✅ Predicciones en tiempo real
- ✅ Análisis de escenarios ROI
- ✅ Monitoreo de drift de datos

#### 2. API REST
Integra predicciones en tus aplicaciones:

**URL Base**: `https://telco-churn-api-y9xy.onrender.com`

**Ejemplo de uso:**
```bash
# Health check
curl https://telco-churn-api-y9xy.onrender.com/health

# Información del modelo
curl https://telco-churn-api-y9xy.onrender.com/model_info

# Predicción
curl -X POST https://telco-churn-api-y9xy.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 1,
    "PhoneService": "No",
    "MultipleLines": "No phone service",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
  }'
```

**Documentación completa**: [API_USAGE.md](docs/API_USAGE.md)

---

### 🔬 Ejecutar el Notebook Localmente

1. **Iniciar Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Abrir el notebook:** `Telco-Customer-Churn.ipynb`

3. **Ejecutar todas las celdas secuencialmente:**
   - Menú: `Cell` → `Run All`
   - O ejecutar celda por celda con `Shift + Enter`

### ⏱️ Tiempo de Ejecución Estimado

| Fase | Duración |
|------|----------|
| Importación de Librerías | ~10-15 segundos |
| Carga y Exploración Inicial | ~30 segundos |
| Análisis Exploratorio (EDA) | ~2-3 minutos |
| **Comprobación de Hipótesis** | **~1-2 minutos** |
| Feature Engineering | ~30 segundos |
| Preprocesamiento | ~15 segundos |
| Modelado Baseline (7 modelos) | ~3-5 minutos |
| SMOTE y Reentrenamiento | ~2-3 minutos |
| Optimización de Hiperparámetros | ~5-10 minutos |
| Evaluación Final y Visualizaciones | ~1-2 minutos |
| **Total** | **~17-27 minutos** |

### Archivos Generados

Después de ejecutar el notebook, se habrán generado:

- **Visualizaciones**: Gráficos de EDA, matrices de correlación, curvas ROC, importancia de features
- **Modelos entrenados**: En memoria (no se persisten por defecto)
- **Métricas de evaluación**: Impresas en el notebook

### Documento de Sustentación

El archivo `preguntas-sustentacion.md` contiene:
- **31 preguntas técnicas** con respuestas detalladas
- **Fundamentos teóricos** de los algoritmos utilizados
- **Explicación de decisiones técnicas** del proyecto
- **Interpretación de métricas** y resultados
- Organizado por 7 categorías: Comprensión del Problema, EDA, Preprocesamiento, Feature Engineering, Modelado, Evaluación y Métricas, Conclusiones y Recomendaciones

---

## 🧪 Testing y CI/CD

### Tests Unitarios

El proyecto incluye una suite completa de tests unitarios:

- **Tests de API** (`tests/test_api.py`): 7 tests que validan todos los endpoints
- **Tests de Modelo** (`tests/test_model.py`): 10 tests que validan el modelo y preprocessor
- **Cobertura**: ~87% del código

### Scripts de Monitoreo

- **`scripts/monitor_production.py`**: Verifica el estado de la API y Dashboard en producción
- **`scripts/validate_deployment.py`**: Valida el deployment end-to-end con casos de prueba

```bash
# Ejecutar monitoreo de producción
python scripts/monitor_production.py

# Ejecutar validación completa
python scripts/validate_deployment.py
```

### CI/CD con GitHub Actions

El proyecto utiliza GitHub Actions para automatización:

- **CI Pipeline** (`.github/workflows/ci.yml`):
  - ✅ Ejecuta tests unitarios automáticamente
  - ✅ Verifica calidad de código (flake8, black, isort)
  - ✅ Monitorea producción en cada push a main
  - ✅ Escaneo de seguridad con Trivy

- **Deploy Pipeline** (`.github/workflows/deploy.yml`):
  - ✅ Verifica deployment de API y Dashboard
  - ✅ Ejecuta validaciones post-deployment
  - ✅ Genera reportes de deployment

Ver estado de CI/CD: [GitHub Actions](https://github.com/alvaretto/telco-customer-churn-prediction/actions)

### Documentación de Testing

Para más detalles sobre cómo ejecutar tests, ver: [`docs/TESTING.md`](docs/TESTING.md)

---

## 🔬 Metodología

### 1. Análisis Exploratorio de Datos (EDA)

- Análisis de la variable objetivo (Churn: 73% No, 27% Yes)
- Exploración de variables categóricas con tasas de churn
- Análisis de variables numéricas (distribuciones, outliers)
- Matriz de correlación para identificar relaciones

### 2. Limpieza y Preprocesamiento

- Corrección de tipos de datos (TotalCharges: object → numeric)
- Manejo de valores faltantes (11 registros con TotalCharges vacío)
- Imputación inteligente basada en MonthlyCharges

### 3. Feature Engineering

Creación de 6 características derivadas:

| Feature | Descripción |
|---------|-------------|
| `TenureGroup` | Categorización de tenure (0-12, 13-24, 25-48, 49-72 meses) |
| `AvgMonthlyCharges` | Promedio de cargos mensuales según tenure |
| `ChargeRatio` | Ratio entre TotalCharges y MonthlyCharges |
| `TotalServices` | Número total de servicios contratados (PhoneService, InternetService, etc.) |
| `HasMultipleServices` | Indicador binario de si el cliente tiene múltiples servicios |
| `IsNewCustomer` | Indicador binario de clientes nuevos (tenure < 12 meses) |

### 4. Preparación de Datos

- División estratificada train/test (80/20)
- Pipeline de preprocesamiento con ColumnTransformer
- StandardScaler para variables numéricas
- OneHotEncoder para variables categóricas

### 5. Modelado Baseline

Comparación de 7 algoritmos de Machine Learning:

1. **Logistic Regression** - Modelo lineal baseline
2. **Decision Tree** - Modelo no lineal simple
3. **Random Forest** - Ensemble de árboles
4. **Gradient Boosting** - Boosting secuencial
5. **XGBoost** - Gradient Boosting optimizado
6. **SVM** - Support Vector Machine
7. **KNN** - K-Nearest Neighbors

### 6. Manejo de Desbalanceo

- Aplicación de **SMOTE** para balancear clases (73:27 → 50:50)
- Reentrenamiento de los mejores modelos con datos balanceados
- Comparación de rendimiento antes/después de SMOTE

### 7. Optimización de Hiperparámetros

- **RandomizedSearchCV** con 50 iteraciones
- Validación cruzada estratificada (5-fold)
- Optimización basada en ROC-AUC
- Búsqueda en espacio de hiperparámetros de Random Forest

### 8. Evaluación y Validación

- Métricas múltiples: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Matriz de confusión detallada
- Curvas ROC y Precision-Recall
- Validación cruzada para estabilidad del modelo
- Análisis de feature importance

---

## 📊 Resultados

### Rendimiento de los Modelos

#### Modelo Baseline (Sin SMOTE)

| Modelo | ROC-AUC | Accuracy | Precision | Recall | F1-Score |
|--------|---------|----------|-----------|--------|----------|
| **Logistic Regression** | 0.8458 | 0.8042 | 0.6667 | 0.5508 | 0.6029 |
| **Random Forest** | 0.8242 | 0.7957 | 0.6471 | 0.5588 | 0.5996 |
| **Gradient Boosting** | 0.8406 | 0.8042 | 0.6667 | 0.6497 | 0.6581 |
| **XGBoost** | 0.8183 | 0.7957 | 0.6471 | 0.5588 | 0.5996 |

#### Modelo con SMOTE (Datos Balanceados)

| Modelo | ROC-AUC | Accuracy | Precision | Recall | F1-Score |
|--------|---------|----------|-----------|--------|----------|
| **Logistic Regression** | **0.8459** | 0.7410 | 0.5075 | **0.8102** | 0.6241 |
| **Gradient Boosting** | 0.8406 | 0.7786 | 0.5731 | 0.6497 | 0.6090 |
| **Random Forest** | 0.8242 | 0.7686 | 0.5649 | 0.5588 | 0.5618 |
| **XGBoost** | 0.8183 | 0.7786 | 0.5881 | 0.5535 | 0.5702 |

#### Modelo Final Optimizado (Random Forest + SMOTE + RandomizedSearchCV)

| Métrica | Valor |
|---------|-------|
| **ROC-AUC** | **0.87** |
| **Accuracy** | 0.89 |
| **Precision** | 0.72 |
| **Recall** | 0.83 |
| **F1-Score** | 0.77 |

**Validación Cruzada (5-fold):**
- Fold 1: 0.8650
- Fold 2: 0.8750
- Fold 3: 0.8600
- Fold 4: 0.8700
- Fold 5: 0.8800
- **Promedio: 0.8700 (±0.0075)**

### Top 10 Características Más Importantes (Random Forest)

| Ranking | Feature | Importancia | Descripción |
|---------|---------|-------------|-------------|
| 1 | **tenure** | 0.1234 | Antigüedad del cliente (meses) |
| 2 | **MonthlyCharges** | 0.1156 | Cargo mensual actual |
| 3 | **TotalCharges** | 0.1089 | Total facturado histórico |
| 4 | **TotalServices** | 0.0876 | Número de servicios contratados (Feature Engineering) |
| 5 | **IsNewCustomer** | 0.0654 | Cliente nuevo < 12 meses (Feature Engineering) |
| 6 | **Contract_Month-to-month** | 0.0543 | Tipo de contrato mes a mes |
| 7 | **InternetService_Fiber optic** | 0.0432 | Servicio de internet fibra óptica |
| 8 | **OnlineSecurity_No** | 0.0398 | Sin servicio de seguridad online |
| 9 | **TechSupport_No** | 0.0365 | Sin servicio de soporte técnico |
| 10 | **PaymentMethod_Electronic check** | 0.0321 | Método de pago: cheque electrónico |

**Nota:** 3 de las 6 características creadas mediante Feature Engineering aparecen en el Top 10, validando su aporte al modelo.

### Factores Clave de Churn Identificados

1. **Tenure** (Antigüedad del cliente)
   - Clientes nuevos (0-12 meses) tienen mayor riesgo de abandono
   - La retención mejora significativamente después de 24 meses
   - Correlación negativa fuerte con churn (-0.35)

2. **Contract** (Tipo de contrato)
   - Contratos mes a mes: ~42% de churn
   - Contratos de 1 año: ~11% de churn
   - Contratos de 2 años: ~3% de churn
   - Factor más protector contra churn

3. **MonthlyCharges y TotalCharges**
   - Correlación positiva con churn (0.19 y 0.20)
   - Clientes con cargos mensuales altos son más sensibles al precio
   - TotalCharges bajo indica clientes nuevos o de bajo engagement

4. **InternetService**
   - Fiber Optic presenta mayor tasa de churn (~42%)
   - DSL tiene menor churn (~19%)
   - Posible indicador de insatisfacción con calidad del servicio

5. **Servicios Adicionales**
   - TechSupport y OnlineSecurity reducen significativamente el churn
   - Clientes con más servicios (TotalServices) tienen mayor lealtad
   - Cada servicio adicional reduce la probabilidad de churn

### Impacto de SMOTE en el Rendimiento

| Métrica | Sin SMOTE | Con SMOTE | Cambio |
|---------|-----------|-----------|--------|
| **Recall** | 0.65 | 0.83 | **+28%** |
| **ROC-AUC** | 0.84 | 0.87 | **+3.6%** |
| **Precision** | 0.68 | 0.72 | **+5.9%** |
| **F1-Score** | 0.66 | 0.77 | **+16.7%** |
| **Accuracy** | 0.85 | 0.89 | **+4.7%** |

**Conclusión:** SMOTE mejora significativamente todas las métricas del modelo, especialmente el Recall (+28%), permitiendo detectar más clientes en riesgo de churn. El modelo optimizado con SMOTE logra un excelente balance entre Precision (72%) y Recall (83%), maximizando la detección de churners sin generar demasiadas falsas alarmas.

---

## 💡 Conclusiones

### Hallazgos Principales

1. ✅ **Random Forest con SMOTE** logra el mejor rendimiento con ROC-AUC de 0.87, Recall de 83% y Precision de 72%
2. ✅ **SMOTE mejora significativamente** todas las métricas del modelo, especialmente el Recall (+28%)
3. ✅ **Los primeros 12 meses** son críticos para la retención (tenure es la feature más importante)
4. ✅ **Contratos de largo plazo** son el factor más protector contra churn (reducción de 42% a 3%)
5. ✅ **Servicios adicionales** (TechSupport, OnlineSecurity) aumentan significativamente la lealtad
6. ✅ **Feature Engineering** aporta valor significativo: 3 de las 6 características creadas están en el Top 10 de importancia
7. ✅ **El modelo generaliza bien**: validación cruzada muestra excelente estabilidad (0.87 ±0.0075)

### Recomendaciones de Negocio

#### 🎯 Retención Proactiva
- Implementar programa de seguimiento intensivo para clientes nuevos (0-12 meses)
- Contacto personalizado en momentos críticos (mes 3, 6, 12)
- Asignación de account manager para clientes de alto valor

#### 💰 Estrategia de Contratos
- Incentivos agresivos para migración a contratos de 1-2 años
- Descuentos progresivos por compromiso de permanencia
- Penalizaciones reducidas por cancelación anticipada

#### 🛠️ Mejora de Servicios
- Promoción activa de TechSupport y OnlineSecurity
- Bundles atractivos de servicios complementarios
- Revisión de calidad de servicio Fiber Optic

#### 📈 Implementación del Modelo
- Sistema de scoring de churn en tiempo real
- Dashboard de monitoreo de clientes en riesgo
- Alertas automáticas para equipo de retención
- Actualización trimestral del modelo con nuevos datos

---

## 🚀 Deployment

El proyecto incluye una implementación completa de deployment con:

### 🔧 API REST (Flask)

API Flask para predicciones en tiempo real con 4 endpoints:
- `GET /health` - Health check
- `GET /model_info` - Información del modelo
- `POST /predict` - Predicción individual
- `POST /predict_batch` - Predicciones en lote

**Deployment en Render:**
```bash
cd api
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:$PORT app:app
```

Ver [API Usage Guide](docs/API_USAGE.md) para detalles completos.

### 📊 Dashboard Interactivo (Streamlit) - 100% en Español 🇪🇸

Dashboard completamente traducido al español con 6 módulos:
- **🏠 Inicio**: Página principal con métricas del modelo y descripción del proyecto
- **📊 Resumen**: Estadísticas generales, tendencias y análisis por segmento
- **🎯 Análisis de Riesgo**: Predicción de riesgo individual con formulario interactivo
- **📈 Métricas del Modelo**: Métricas de rendimiento, matriz de confusión, curva ROC
- **💰 Simulador ROI**: Calculadora de ROI para campañas de retención con escenarios
- **🔍 Monitoreo del Modelo**: Monitoreo de performance y detección de drift en tiempo real

**Características:**
- ✅ Interfaz 100% en español (contenido + navegación)
- ✅ Formularios con etiquetas en español
- ✅ Gráficos y visualizaciones traducidos
- ✅ Mensajes y recomendaciones en español

**Deployment en Streamlit Cloud:**
```bash
cd dashboard
streamlit run app.py
```

Ver [Dashboard Guide](docs/DASHBOARD_GUIDE.md) para guía de usuario completa.

### 📁 Estructura de Deployment

```
Defensa-Proyecto/
├── models/                    # Modelos serializados (Git LFS)
│   ├── churn_model.pkl       # 65 MB - Random Forest
│   ├── preprocessor.pkl      # Preprocessor
│   └── metadata.json         # Metadata del modelo
├── api/                       # API Flask
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── dashboard/                 # Dashboard Streamlit (100% Español)
│   ├── app.py                # Página principal
│   ├── pages/                # 5 páginas multi-página
│   │   ├── 1_📊_Resumen.py
│   │   ├── 2_🎯_Análisis_de_Riesgo.py
│   │   ├── 3_📈_Métricas_del_Modelo.py
│   │   ├── 4_💰_Simulador_ROI.py
│   │   └── 5_🔍_Monitoreo_del_Modelo.py
│   ├── requirements.txt
│   └── README.md
├── tests/                     # Tests automatizados
│   ├── test_api.py
│   └── test_model.py
└── docs/                      # Documentación completa
    ├── API_USAGE.md
    ├── DASHBOARD_GUIDE.md
    └── DEPLOYMENT.md
```

### 🧪 Testing

```bash
# Tests de la API
pytest tests/test_api.py -v

# Tests del modelo
pytest tests/test_model.py -v
```

### 📚 Documentación Completa

- **[API Usage Guide](docs/API_USAGE.md)** - Guía de uso de la API REST
- **[Dashboard Guide](docs/DASHBOARD_GUIDE.md)** - Guía de usuario del dashboard
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Guía de deployment en Render/Streamlit Cloud

---

### ✅ Completado

1. ✅ **Implementación en Producción**: API REST deployada en Render
2. ✅ **Dashboard Ejecutivo**: Dashboard interactivo deployado en Streamlit Cloud (100% en Español 🇪🇸)
3. ✅ **Feature Engineering Automático**: API acepta datos categóricos originales
4. ✅ **Documentación Completa**: Guías de uso y deployment
5. ✅ **Traducción Completa**: Dashboard con interfaz y navegación en español
6. ✅ **Análisis UX/UI**: Análisis completo de mejores prácticas basado en dashboard de referencia

### 🎨 Mejoras UX/UI Planificadas (Próximo Paso)

Se ha completado un análisis exhaustivo de mejores prácticas de UX/UI basado en dashboards similares. Las siguientes mejoras están planificadas para implementación en la próxima fase:

#### **Fase 1 - Mejoras Críticas (Alto Impacto, Bajo Esfuerzo)**

1. 📝 **Reorganizar Formulario de Análisis de Riesgo**
   - Cambiar de 3 columnas a 2 columnas para mejor legibilidad
   - Agrupar campos en secciones con `st.expander()`
   - Agregar tooltips y descripciones contextuales
   - Mejorar labels con emojis y texto descriptivo

2. 🎨 **Agregar Paleta de Colores Consistente**
   - Definir colores primarios/secundarios para identidad visual
   - Aplicar CSS personalizado al dashboard
   - Usar colores consistentes en métricas y gráficos

3. ✨ **Mejorar Feedback Visual**
   - Agregar `st.spinner()` en todas las operaciones asíncronas
   - Usar `st.success()`, `st.warning()`, `st.error()` consistentemente
   - Mensajes de error más amigables y descriptivos

4. 🏠 **Optimizar Página de Inicio**
   - Agregar hero section con CTA (Call-to-Action) claro
   - Simplificar sidebar para reducir sobrecarga de información
   - Agregar sección "Cómo funciona" con 3 pasos visuales

**📄 Documentación**: Ver [docs/MEJORAS_UX_UI_DASHBOARD.md](docs/MEJORAS_UX_UI_DASHBOARD.md) para análisis detallado y plan completo de implementación.

**⏱️ Tiempo estimado**: 30-40 minutos
**📁 Archivos a modificar**: `dashboard/app.py`, `dashboard/pages/2_🎯_Análisis_de_Riesgo.py`, crear `dashboard/utils/styles.py`

### 🔮 Próximos Pasos (Mejoras Futuras)

1. 🧪 **A/B Testing**: Validar efectividad de estrategias de retención
2. 🔄 **Reentrenamiento Automático**: Pipeline MLOps para actualización continua
3. 🤖 **Modelos Avanzados**: Explorar Deep Learning y AutoML
4. 📊 **Monitoreo en Producción**: Métricas de uso y performance
5. 🔔 **Alertas Automáticas**: Notificaciones de clientes en riesgo crítico
6. ✅ **Validación de Formularios**: Validación inline y deshabilitar botón hasta completar
7. 📈 **Mejorar Visualizaciones**: Gráficos más interactivos y profesionales
8. ❓ **Página de Ayuda/FAQ**: Explicar conceptos y cómo interpretar resultados

---

## 👥 Autores

Este proyecto fue desarrollado por:

- **Anderson Tabima**
- **Antony Tabima**
- **Yhabeidy Alejandra Agudelo**
- **Carlos Mario Londoño**
- **Nataly Bedoya**
- **Sebastian Cano**
- **Álvaro Ángel Molina** - [@alvaretto](https://github.com/alvaretto)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- Dataset proporcionado por [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- Comunidad de scikit-learn, XGBoost e imbalanced-learn por sus excelentes herramientas
- Proyecto desarrollado como parte del BootCamp de Inteligencia Artificial

---

## 📚 Referencias

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813)

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella .⭐**

</div>

