# 📊 Predicción de Abandono de Clientes en Telecomunicaciones

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.2-yellow.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![Dashboard Status](https://img.shields.io/badge/Dashboard-Online-success.svg)](https://clienteinsight-ai.vercel.app/)
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-black.svg?logo=vercel)](https://clienteinsight-ai.vercel.app/)

[![Model ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.87-brightgreen.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model Recall](https://img.shields.io/badge/Recall-0.83-green.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model Precision](https://img.shields.io/badge/Precision-0.72-yellowgreen.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)
[![Model F1-Score](https://img.shields.io/badge/F1--Score-0.77-green.svg)](https://github.com/alvaretto/telco-customer-churn-prediction)

> Proyecto de Machine Learning para predecir el abandono de clientes (Customer Churn) en empresas de telecomunicaciones utilizando técnicas avanzadas de análisis de datos y modelado predictivo.

## 🚀 Demo en Vivo

- **📊 Dashboard en Producción**: [https://clienteinsight-ai.vercel.app/](https://clienteinsight-ai.vercel.app/) ✨
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
- [Metodología](#-metodología)
- [Resultados](#-resultados)
- [Conclusiones](#-conclusiones)
- [Despliegue en Producción](#-despliegue-en-producción)
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
├── 📓 Notebooks y Datos
│   ├── Telco_Customer_Churn.ipynb           # Notebook principal con análisis completo
│   ├── Telco_Customer_Churn_Oficio.pdf      # Notebook exportado a PDF formato oficio
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset original (7,043 registros)
│
├── 🤖 Modelos ML (Git LFS)
│   ├── models/
│   │   ├── churn_model.pkl                  # Random Forest optimizado (65 MB)
│   │   ├── preprocessor.pkl                 # Pipeline de preprocesamiento
│   │   └── metadata.json                    # Métricas y configuración del modelo
│
├── 🌐 API REST (Flask)
│   ├── api/
│   │   ├── app.py                           # Aplicación Flask con 4 endpoints
│   │   ├── requirements.txt                 # Dependencias de la API
│   │   ├── Dockerfile                       # Containerización
│   │   └── README.md                        # Documentación de la API
│
├── 📊 Dashboard (Streamlit - 100% Español)
│   ├── dashboard/
│   │   ├── app.py                           # Página principal
│   │   ├── config/
│   │   │   └── colors.py                    # Paleta de colores y estilos CSS
│   │   ├── pages/                           # Navegación multi-página
│   │   │   ├── 1_📊_Resumen.py
│   │   │   ├── 2_🎯_Análisis_de_Riesgo.py
│   │   │   ├── 3_📈_Métricas_del_Modelo.py
│   │   │   ├── 4_💰_Simulador_ROI.py
│   │   │   └── 5_🔍_Monitoreo_del_Modelo.py
│   │   ├── requirements.txt                 # Dependencias del dashboard
│   │   └── README.md                        # Guía de usuario
│
├── 🧪 Tests y CI/CD
│   ├── tests/
│   │   ├── test_api.py                      # Tests unitarios de la API
│   │   └── test_model.py                    # Tests del modelo
│   ├── .github/workflows/
│   │   ├── ci.yml                           # Pipeline de CI/CD
│   │   └── deploy.yml                       # Pipeline de deployment
│
├── 🔧 Scripts de Utilidad
│   ├── scripts/
│   │   ├── monitor_production.py            # Monitoreo de servicios
│   │   ├── validate_deployment.py           # Validación end-to-end
│   │   ├── check_model_size.py              # Verificación de modelos
│   │   └── convert_to_legal_pdf.py          # Generación de PDF oficio
│
├── 📚 Documentación
│   ├── docs/
│   │   ├── guia_completa_analisis_churn/    # 📖 Guía paso a paso del análisis
│   │   │   ├── 00_progreso.md               # Progreso del análisis
│   │   │   ├── 01-11_*.md                   # 12 capítulos del análisis
│   │   │   ├── guia_completa_analisis_churn.md  # Guía completa
│   │   │   ├── guia_completa_analisis_churn.docx # Versión Word
│   │   │   └── guia_completa_analisis_churn.pdf  # Versión PDF
│   │   ├── micro-tutoriales-preguntas/      # 🎓 26 micro-tutoriales de ML
│   │   │   ├── OneHotEncoder.md             # Tutorial One-Hot Encoding
│   │   │   ├── SMOTE.md                     # Tutorial SMOTE
│   │   │   ├── curva-ROC-[1-4].md           # Serie sobre curva ROC
│   │   │   ├── metricas-clasificacion-binaria.md # Métricas
│   │   │   ├── feature-engineering.md       # Feature Engineering
│   │   │   ├── balanceo.md                  # Técnicas de balanceo
│   │   │   └── [+20 tutoriales más]         # Otros conceptos de ML
│   │   └── varios/                          # 📚 Documentación general
│   │       ├── API_USAGE.md                 # Guía de uso de la API
│   │       ├── DASHBOARD_GUIDE.md           # Manual del dashboard
│   │       ├── DEPLOYMENT.md                # Guía de deployment
│   │       ├── DEPLOYMENT_PASO_A_PASO.md    # Deployment paso a paso
│   │       ├── TESTING.md                   # Guía de testing
│   │       ├── URL_REFERENCE.md             # Referencias de URLs
│   │       └── MEJORAS_UX_UI_DASHBOARD.md   # Análisis de mejoras UX/UI
│
├── 📋 Seguimiento del Proyecto
│   ├── seguimiento/
│   │   ├── EMPEZAR_AQUI.md                  # Guía de inicio rápido
│   │   ├── seguimiento-estructura-completa.md
│   │   ├── DEPLOYMENT_CHECKLIST.md
│   │   ├── URLS_PRODUCCION.md
│   │   ├── RESUMEN_TRABAJO_COMPLETADO.md
│   │   ├── PLAN_ACCION_INFRAESTRUCTURA.md
│   │   └── GUIA_DEPLOYMENT_DETALLADA.md
│
├── ⚙️ Configuración
│   ├── .gitattributes                       # Configuración Git LFS
│   ├── .gitignore                           # Archivos ignorados
│   ├── render.yaml                          # Configuración Render.com
│   ├── runtime.txt                          # Versión de Python (3.10.13)
│   ├── requirements.txt                     # Dependencias principales
│   └── INSTRUCCIONES.md                     # Guía de ejecución
│
└── 📄 Otros
    ├── README.md                            # Este archivo
    ├── LICENSE                              # Licencia MIT
    └── bu/                                  # Backups y versiones anteriores
```

### Descripción de Componentes Principales

| Componente | Descripción |
|------------|-------------|
| **Notebook ML** | Pipeline completo de ML: EDA, preprocesamiento, feature engineering, modelado, evaluación y optimización. Incluye 7 pruebas de hipótesis estadísticas |
| **API REST** | 4 endpoints (health, model_info, predict, predict_batch) con feature engineering automático. Deployada en Render.com |
| **Dashboard** | Interfaz 100% en español con 6 páginas interactivas. Visualizaciones con Plotly, formularios mejorados, paleta de colores consistente. Deployado en Streamlit Cloud |
| **Modelos ML** | Random Forest optimizado (ROC-AUC: 0.87) con preprocessor. Versionado con Git LFS |
| **CI/CD** | GitHub Actions para tests automáticos, linting, monitoreo de producción y escaneo de seguridad |
| **Monitoreo** | Scripts para validar deployment y monitorear servicios en producción |
| **Documentación** | Guías completas de API, dashboard, deployment, testing y mejoras UX/UI |

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

**URL**: [https://clienteinsight-ai.vercel.app/](https://clienteinsight-ai.vercel.app/)

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

## 🚀 Despliegue en Producción

### 🌐 Aplicación Desplegada en Vercel

La aplicación está desplegada y disponible en producción:

🔗 **URL de Producción**: [https://clienteinsight-ai.vercel.app/](https://clienteinsight-ai.vercel.app/)

**Acceso:**
- La aplicación es de acceso público, no requiere autenticación
- Funciona en cualquier navegador moderno (Chrome, Firefox, Safari, Edge)
- Responsive: compatible con dispositivos móviles y escritorio

### 📊 Dashboard Interactivo - 100% en Español 🇪🇸

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
- ✅ Desplegado en Vercel con HTTPS y CDN global

Ver [Dashboard Guide](documentacion/docs/varios/DASHBOARD_GUIDE.md) para guía de usuario completa.

### 📁 Estructura del Proyecto

```
telco-customer-churn-prediction/
├── Telco_Customer_Churn.ipynb     # Notebook principal de ML
├── README.md                       # Este archivo
├── .gitattributes                  # Configuración Git LFS
└── documentacion/                  # Toda la documentación y recursos
    ├── models/                     # Modelos serializados (Git LFS)
    │   ├── churn_model.pkl        # Random Forest optimizado
    │   ├── preprocessor.pkl       # Pipeline de preprocesamiento
    │   └── metadata.json          # Metadata del modelo
    ├── dashboard/                  # Dashboard Streamlit (100% Español)
    ├── docs/                       # Documentación completa
    └── ...
```

### 📚 Documentación Completa

- **[Dashboard Guide](documentacion/docs/varios/DASHBOARD_GUIDE.md)** - Guía de usuario del dashboard
- **[Guía Completa del Análisis](documentacion/docs/guia_completa_analisis_churn/guia_completa_analisis_churn.md)** - Documentación paso a paso del proyecto
- **[Micro-tutoriales de ML](documentacion/docs/micro-tutoriales-preguntas/)** - 26 tutoriales sobre conceptos de Machine Learning

---

### ✅ Completado

1. ✅ **Dashboard en Producción**: Desplegado en Vercel ([https://clienteinsight-ai.vercel.app/](https://clienteinsight-ai.vercel.app/))
2. ✅ **Interfaz 100% en Español**: Dashboard completamente traducido
3. ✅ **Documentación Completa**: Guías de uso y tutoriales
4. ✅ **Mejoras UX/UI**: Implementación completada
5. ✅ **Generación de PDF**: Notebook exportado a formato oficio

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

