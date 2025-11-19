# 📊 Predicción de Abandono de Clientes en Telecomunicaciones

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-yellow.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> Proyecto de Machine Learning para predecir el abandono de clientes (Customer Churn) en empresas de telecomunicaciones utilizando técnicas avanzadas de análisis de datos y modelado predictivo.

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
- [Autor](#-autor)
- [Licencia](#-licencia)

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
├── Telco-Customer-Churn.ipynb          # Notebook principal optimizado
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset (7,043 registros)
├── MEJORAS_REALIZADAS.md                # Documentación de mejoras
├── INSTRUCCIONES.md                     # Guía de ejecución y defensa
├── README.md                            # Este archivo
├── LICENSE                              # Licencia MIT
└── .gitignore                           # Archivos excluidos de Git
```

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

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn jupyter
```

O con conda:

```bash
conda install numpy pandas matplotlib seaborn scikit-learn xgboost imbalanced-learn jupyter -c conda-forge
```

---

## 💻 Uso

### Ejecutar el Notebook

1. Iniciar Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Abrir `Telco-Customer-Churn.ipynb`

3. Ejecutar todas las celdas secuencialmente:
   - Menú: `Cell` → `Run All`
   - O ejecutar celda por celda con `Shift + Enter`

### Tiempo de Ejecución

- **Análisis Exploratorio**: ~2-3 minutos
- **Modelado Baseline**: ~3-5 minutos
- **SMOTE y Reentrenamiento**: ~2-3 minutos
- **Optimización de Hiperparámetros**: ~5-10 minutos
- **Evaluación Final**: ~1-2 minutos

**Total**: Aproximadamente 15-25 minutos

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

Creación de 6 nuevas características derivadas:

| Feature | Descripción |
|---------|-------------|
| `ChargeRatio` | Ratio entre MonthlyCharges y TotalCharges |
| `AvgMonthlyCharges` | Promedio de cargos mensuales según tenure |
| `TenureGroup` | Categorización de tenure (0-12, 13-24, 25-48, 49-72) |
| `TotalServices` | Número total de servicios contratados |
| `SeniorWithDependents` | Combinación de SeniorCitizen y Dependents |
| `HighValueContract` | Identificación de contratos de alto valor |

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

### Rendimiento del Mejor Modelo (Random Forest Optimizado)

| Métrica | Valor |
|---------|-------|
| **ROC-AUC** | ~0.85-0.90 |
| **Accuracy** | ~0.80-0.85 |
| **Precision** | ~0.65-0.75 |
| **Recall** | ~0.75-0.85 |
| **F1-Score** | ~0.70-0.80 |

### Factores Clave de Churn Identificados

1. **Tenure** (Antigüedad del cliente)
   - Clientes nuevos (0-12 meses) tienen mayor riesgo de abandono
   - La retención mejora significativamente después de 24 meses

2. **Contract** (Tipo de contrato)
   - Contratos mes a mes: ~42% de churn
   - Contratos de 1 año: ~11% de churn
   - Contratos de 2 años: ~3% de churn

3. **TotalCharges/MonthlyCharges**
   - Relación directa con probabilidad de churn
   - Clientes con cargos muy altos o muy bajos tienen mayor riesgo

4. **InternetService**
   - Fiber Optic presenta mayor tasa de churn
   - Posible indicador de insatisfacción con el servicio

5. **Servicios Adicionales**
   - TechSupport, OnlineSecurity reducen significativamente el churn
   - Clientes con más servicios tienden a permanecer

### Impacto de SMOTE

- **Mejora en Recall**: +15-20% (mejor detección de clientes en riesgo)
- **Balance Precision-Recall**: Optimizado para el caso de uso
- **Reducción de Falsos Negativos**: Crítico para retención proactiva

---

## 💡 Conclusiones

### Hallazgos Principales

1. ✅ **El modelo Random Forest optimizado** logra excelente capacidad discriminativa (ROC-AUC ~0.85-0.90)
2. ✅ **SMOTE mejora significativamente** la detección de clientes en riesgo
3. ✅ **Los primeros 12 meses** son críticos para la retención
4. ✅ **Contratos de largo plazo** son el factor más protector contra churn
5. ✅ **Servicios adicionales** (soporte técnico, seguridad) aumentan la lealtad

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

### Próximos Pasos

1. 🚀 **Implementación en Producción**: API REST para scoring en tiempo real
2. 📊 **Dashboard Ejecutivo**: Visualización de métricas y clientes en riesgo
3. 🧪 **A/B Testing**: Validar efectividad de estrategias de retención
4. 🔄 **Reentrenamiento Automático**: Pipeline MLOps para actualización continua
5. 🤖 **Modelos Avanzados**: Explorar Deep Learning y AutoML

---

## 👨‍💻 Autor

**Álvaro Ángel Molina**

- GitHub: [@alvaretto](https://github.com/alvaretto)
- Email: alvaretto@users.noreply.github.com

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- Dataset proporcionado por [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- Comunidad de scikit-learn y XGBoost por sus excelentes herramientas
- Proyecto desarrollado como parte de formación en Inteligencia Artificial

---

## 📚 Referencias

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813)

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella ⭐**

</div>

