---
title: "Cliente Insight - Predicción de Customer Churn"
author: "Grupo 3 Equipo Cliente Insight"
date: "Noviembre 2025"
subtitle: Sistema de Machine Learning para Análisis de Fuga de Clientes
---

<div align="center">

# 📊 Cliente Insight - Predicción de Customer Churn

<img src="Logo Cliente Insight.png" alt="Cliente Insight Logo" width="200">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-006600?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Deployed](https://img.shields.io/badge/Deployed-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://clienteinsight-ai.vercel.app/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)](https://clienteinsight-ai.vercel.app/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**Sistema inteligente de predicción de fuga de clientes para empresas de telecomunicaciones**

[🚀 Ver Demo en Vivo](https://clienteinsight-ai.vercel.app/) | [📖 Documentación](#-guía-de-uso) | [🐛 Reportar Bug](https://github.com/issues)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Instalación](#-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Despliegue](#-despliegue)
- [Métricas del Modelo](#-métricas-del-modelo)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Documentación](#-documentación)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 🎯 Descripción

**Cliente Insight** es un sistema de Machine Learning diseñado para predecir la probabilidad de que un cliente abandone (churn) los servicios de una empresa de telecomunicaciones. Utiliza algoritmos avanzados de clasificación para identificar clientes en riesgo, permitiendo implementar estrategias de retención proactivas.

### Impacto Esperado del Negocio

| Métrica | Valor Esperado |
|---------|----------------|
| 🎯 Reducción de Churn | 15-25% |
| 💰 Ahorro Anual Estimado | 20-35% en costos de adquisición |
| 📊 ROI de Campañas | >300% |
| 👥 Clientes en Riesgo Detectados | 1,489 clientes |
| 💵 Ingreso Anual Recuperado | $375,279 (con 30% retención) |

---

## ✨ Características Principales

- 🔮 **Predicción de Churn**: Modelo Logistic Regression Optimizado con 85.05% ROC-AUC
- 📊 **Análisis Exploratorio Completo**: 15 visualizaciones del comportamiento del cliente
- ⚖️ **Manejo de Datos Desbalanceados**: Implementación de SMOTE, SMOTE+Tomek y Undersampling
- 🎛️ **Optimización de Hiperparámetros**: RandomizedSearchCV para mejor rendimiento
- 📈 **Feature Engineering Avanzado**: 25 características incluyendo variables derivadas
- 🔍 **Interpretabilidad**: Análisis de importancia de características y top 10 features
- 🎲 **Validación de Robustez**: Modelo validado con 5 semillas diferentes (APPROVED)
- 💾 **Pipeline de Producción**: Modelo listo para deployment con serialización completa
- 📝 **Informes Automáticos**: Generación automática de reportes en Markdown
- 📚 **Documentación Completa**: Guías, preguntas de sustentación y análisis de gráficas

---

## 🛠️ Tech Stack

### Análisis y Modelado
| Tecnología | Propósito |
|------------|-----------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Lenguaje principal |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulación de datos |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Operaciones numéricas |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) | Algoritmos de ML |
| ![XGBoost](https://img.shields.io/badge/XGBoost-006600?style=flat-square) | Gradient Boosting |

### Visualización
| Tecnología | Propósito |
|------------|-----------|
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square) | Gráficos base |
| ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square) | Visualizaciones estadísticas |

### Balanceo de Datos
| Tecnología | Propósito |
|------------|-----------|
| ![imbalanced-learn](https://img.shields.io/badge/imbalanced--learn-FF6F00?style=flat-square) | SMOTE, Undersampling |

---

## 📦 Dataset

El proyecto utiliza el dataset **Telco Customer Churn** de IBM:

| Característica | Valor |
|----------------|-------|
| 📊 Registros | 7,043 clientes |
| 🔢 Variables Originales | 21 features + 1 target |
| 🔧 Variables con Feature Engineering | 25 features + 1 target |
| 🎯 Variable Objetivo | `Churn` (Yes/No) |
| ⚖️ Distribución | 73.46% No Churn / 26.54% Churn |
| 📊 Ratio de Desbalanceo | 2.77:1 |
| 📁 Archivo | `WA_Fn-UseC_-Telco-Customer-Churn.csv` |

### Variables del Dataset

| Categoría | Variables |
|-----------|-----------|
| **Demografía** | gender, SeniorCitizen, Partner, Dependents |
| **Servicios** | PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies |
| **Cuenta** | Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, tenure |
| **Features Engineered** | AvgMonthlyCharges, Charge_Ratio, y otras variables derivadas |

---

## ⚡ Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip o conda

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/alvaretto/cliente-insight.git
cd cliente-insight
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn joblib
```

4. **Ejecutar el notebook**
```bash
jupyter notebook Telco_Customer_Churn.ipynb
```

### Google Colab (Alternativa)

Puedes ejecutar el notebook directamente en Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alvaretto/cliente-insight/blob/main/Telco_Customer_Churn.ipynb)

---

## 📖 Guía de Uso

### Estructura del Notebook

El análisis está organizado en **13 secciones**:

| # | Sección | Descripción |
|:-:|---------|-------------|
| 0 | ⚙️ Configuración | Imports, semillas y funciones auxiliares |
| 1 | 📂 Carga de Datos | Carga robusta y exploración inicial |
| 2 | 🧹 Limpieza | Tratamiento de nulos y conversión de tipos |
| 3 | 📊 EDA | Análisis exploratorio de datos con 15 gráficas |
| 4 | 🔧 Feature Engineering | Creación de nuevas características (25 features totales) |
| 5 | ✂️ Preparación | División train/test y pipeline |
| 6 | 🤖 Modelos Baseline | Entrenamiento de 7 algoritmos |
| 7 | ⚖️ Balanceo | SMOTE, SMOTE+Tomek, Undersampling |
| 8 | 🎯 Optimización | RandomizedSearchCV |
| 9 | 📈 Evaluación | Métricas y curvas ROC |
| 10 | 🔍 Interpretabilidad | Feature importance y validación de robustez |
| 11 | 💾 Guardado | Exportar modelo para producción |
| 12 | 📋 Resumen | Metodología y resultados |
| 13 | 📝 Informe | Generación automática de informe en Markdown |

### 📚 Documentación Adicional

El proyecto incluye documentación completa en múltiples formatos:

| Documento | Descripción | Formatos |
|-----------|-------------|----------|
| **Guía Completa** | Explicación detallada de cada bloque del notebook | MD, PDF, HTML |
| **Preguntas de Sustentación** | Preguntas y respuestas sobre el proyecto | MD, PDF, HTML |
| **Análisis de Gráficas** | Interpretación de las 15 visualizaciones | MD, PDF, HTML |
| **Informe Automático** | Reporte generado automáticamente con métricas | MD |

### 📊 Informes Automáticos

El notebook genera automáticamente un informe completo que incluye:

- ✅ Resumen del dataset y calidad de datos
- ✅ Métricas de rendimiento del modelo
- ✅ Matriz de confusión detallada
- ✅ Top 10 features más importantes
- ✅ Comparativa de técnicas de balanceo
- ✅ Validación de robustez del modelo
- ✅ Recomendaciones de acción
- ✅ Impacto esperado en el negocio

### Ejemplo de Predicción

```python
import joblib

# Cargar modelo y preprocesador
model = joblib.load('models/churn_model.joblib')
preprocessor = joblib.load('models/preprocessor.joblib')

# Datos del cliente nuevo
nuevo_cliente = {
    'tenure': 12,
    'MonthlyCharges': 70.5,
    'TotalCharges': 846.0,
    'Contract': 'Month-to-month',
    'PaymentMethod': 'Electronic check',
    # ... otras características
}

# Preprocesar y predecir
X_nuevo = preprocessor.transform([nuevo_cliente])
probabilidad_churn = model.predict_proba(X_nuevo)[0][1]

print(f"Probabilidad de Churn: {probabilidad_churn:.2%}")
```

---

## 🚀 Despliegue

### 🌐 Aplicación en Producción

<div align="center">

### ✅ La aplicación está desplegada y disponible en:

# 🔗 [https://clienteinsight-ai.vercel.app/](https://clienteinsight-ai.vercel.app/)

[![Ver Aplicación](https://img.shields.io/badge/🚀_Ver_Aplicación_en_Vivo-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://clienteinsight-ai.vercel.app/)

</div>

### Plataforma de Despliegue

| Aspecto | Detalle |
|---------|---------|
| 🌐 **Plataforma** | Vercel |
| 🔗 **URL de Producción** | [clienteinsight-ai.vercel.app](https://clienteinsight-ai.vercel.app/) |
| ⚡ **Estado** | Production Ready |
| 🔄 **CI/CD** | Despliegue automático desde GitHub |

### Características del Deployment

- ✅ **Alta Disponibilidad**: Infraestructura serverless de Vercel
- ✅ **HTTPS Seguro**: Certificado SSL automático
- ✅ **CDN Global**: Distribución de contenido optimizada
- ✅ **Despliegue Continuo**: Actualización automática con cada push

---

## 📊 Métricas del Modelo

### Rendimiento del Modelo Final (Logistic Regression Optimizado)

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| 📈 **ROC-AUC** | 0.8505 | ✅ Muy buena capacidad discriminativa |
| 🎯 **Accuracy** | 74.10% | Predicciones correctas totales |
| 📊 **Recall** | 79.68% | ✅ Detección de clientes en riesgo |
| 🔍 **Precision** | 50.77% | Alertas correctas de churn |
| ⚖️ **F1-Score** | 0.6202 | Balance Precision-Recall |
| 🔄 **CV Score** | 0.8389 | Validación cruzada (5-fold) |

### 🎲 Validación de Robustez

| Métrica | Valor | Estado |
|---------|-------|--------|
| **Estado de Validación** | APPROVED ✅ | Listo para producción |
| **Semillas Evaluadas** | [42, 123, 456, 789, 2024] | 5 configuraciones |
| **ROC-AUC Promedio** | 0.8515 | Rendimiento consistente |
| **Desviación Estándar** | 0.0071 | ✅ Muy estable (< 0.02) |
| **Rango de Variación** | [0.8466, 0.8638] | ✅ Bajo (< 0.05) |

### Modelos Evaluados (Baseline sin balanceo)

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.8041 | 0.6655 | 0.5267 | 0.5881 | 0.8484 |
| Gradient Boosting | 0.7963 | 0.6495 | 0.5053 | 0.5684 | 0.8439 |
| XGBoost | 0.7850 | 0.6092 | 0.5294 | 0.5665 | 0.8227 |
| Random Forest | 0.7842 | 0.6199 | 0.4840 | 0.5435 | 0.8227 |
| SVM | 0.8041 | 0.6655 | 0.5267 | 0.5881 | 0.8041 |
| KNN | 0.7672 | 0.5661 | 0.5267 | 0.5457 | 0.7772 |
| Decision Tree | 0.7175 | 0.4689 | 0.4840 | 0.4763 | 0.6424 |

### Técnicas de Balanceo Comparadas

| Técnica | ROC-AUC | F1-Score | Precision | Recall | Tiempo (s) | Muestras |
|---------|---------|----------|-----------|--------|------------|----------|
| **Undersampling** ⭐ | 0.8321 | 0.6227 | 0.5168 | 0.7834 | 0.57 | 2,990 |
| SMOTE + Tomek | 0.8289 | 0.5923 | 0.5884 | 0.5963 | 1.75 | 8,022 |
| SMOTE | 0.8295 | 0.5638 | 0.5608 | 0.5668 | 1.34 | 8,278 |

> **Nota:** El modelo final usa **Undersampling** como técnica de balanceo seleccionada automáticamente por mejor ROC-AUC.

### 🔝 Top 10 Features Más Importantes

| Ranking | Feature | Importancia | Interpretación |
|---------|---------|-------------|----------------|
| 1 | **Contract_Two year** | 152.47% | 🎯 Factor más determinante |
| 2 | **InternetService_Fiber optic** | 69.41% | Tipo de servicio de internet |
| 3 | **Contract_One year** | 68.12% | Contratos anuales reducen churn |
| 4 | **PhoneService_Yes** | 64.84% | Servicio telefónico |
| 5 | **tenure** | 57.73% | Antigüedad del cliente |
| 6 | **AvgMonthlyCharges** | 41.90% | Promedio de cargos mensuales |
| 7 | **Charge_Ratio** | 40.06% | Ratio de cargos (feature engineered) |
| 8 | **PaperlessBilling_Yes** | 36.72% | Facturación sin papel |
| 9 | **OnlineSecurity_Yes** | 35.25% | Seguridad online |
| 10 | **PaymentMethod_Electronic check** | 33.70% | Método de pago electrónico |

> **💡 Insight Clave:** El tipo de contrato es el factor más determinante. Promover contratos anuales/bianuales reduce significativamente el churn.

---

## 📁 Estructura del Proyecto

```
cliente-insight/
├── 📊 Telco_Customer_Churn.ipynb              # Notebook principal de análisis
├── 📦 WA_Fn-UseC_-Telco-Customer-Churn.csv    # Dataset original
│
├── 📖 Documentación
│   ├── README.md                               # Este archivo
│   ├── Guia-Completa-Cliente-Insight.md       # Guía detallada del proyecto
│   ├── Preguntas-Sustentacion-Cliente-Insight.md  # Preguntas y respuestas
│   ├── preguntas-graficas-cliente-insight.md  # Análisis de gráficas
│   └── informe_churn_*.md                     # Informes automáticos generados
│
├── 📄 Documentación Exportada (PDF/HTML)
│   ├── Guia-Completa-Cliente-Insight.pdf
│   ├── Guia-Completa-Cliente-Insight.html
│   ├── Preguntas-Sustentacion-Cliente-Insight.pdf
│   ├── Preguntas-Sustentacion-Cliente-Insight.html
│   ├── preguntas-graficas-cliente-insight.pdf
│   ├── preguntas-graficas-cliente-insight.html
│   └── README.html
│
├── 📊 Visualizaciones
│   └── graficas_churn/                        # 15 gráficas generadas
│       ├── grafica_01.png                     # Distribución de Churn
│       ├── grafica_02.png                     # Churn por Género
│       ├── grafica_03.png                     # Churn por Senior Citizen
│       ├── grafica_04.png                     # Churn por Partner
│       ├── grafica_05.png                     # Churn por Dependents
│       ├── grafica_06.png                     # Churn por Tipo de Contrato
│       ├── grafica_07.png                     # Churn por Método de Pago
│       ├── grafica_08.png                     # Churn por Internet Service
│       ├── grafica_09.png                     # Distribución de Tenure
│       ├── grafica_10.png                     # Distribución de Monthly Charges
│       ├── grafica_11.png                     # Distribución de Total Charges
│       ├── grafica_12.png                     # Correlación de Variables
│       ├── grafica_13.png                     # Feature Importance
│       ├── grafica_14.png                     # Curva ROC
│       └── grafica_15.png                     # Matriz de Confusión
│
├── 🖼️ Logo Cliente Insight.png                # Logo del proyecto
│
└── 📄 models/                                  # Modelos serializados (generados)
    ├── churn_model_*.joblib                   # Modelo entrenado
    ├── preprocessor_*.joblib                  # Pipeline de preprocesamiento
    ├── model_metadata_*.json                  # Metadatos del modelo
    └── feature_names_*.json                   # Nombres de características
```

### 📊 Gráficas Generadas

El proyecto incluye **15 visualizaciones** que cubren:

- **Análisis Exploratorio**: Distribuciones y relaciones entre variables
- **Análisis de Churn**: Patrones de abandono por diferentes características
- **Evaluación del Modelo**: Curvas ROC, matrices de confusión, importancia de features
- **Insights de Negocio**: Visualizaciones para toma de decisiones

---

## 📚 Documentación

El proyecto cuenta con documentación completa y detallada:

### 📖 Guías y Manuales

#### 1. Guía Completa de Cliente Insight
**Archivo:** `Guia-Completa-Cliente-Insight.md` ([PDF](Guia-Completa-Cliente-Insight.pdf) | [HTML](Guia-Completa-Cliente-Insight.html))

Documentación exhaustiva que incluye:
- Explicación detallada de cada uno de los 13 bloques del notebook
- Código relevante con comentarios
- Interpretación de resultados
- Mejores prácticas aplicadas
- Conceptos de Machine Learning explicados

#### 2. Preguntas de Sustentación
**Archivo:** `Preguntas-Sustentacion-Cliente-Insight.md` ([PDF](Preguntas-Sustentacion-Cliente-Insight.pdf) | [HTML](Preguntas-Sustentacion-Cliente-Insight.html))

Preguntas y respuestas sobre:
- Metodología del proyecto
- Decisiones técnicas tomadas
- Interpretación de métricas
- Justificación de algoritmos seleccionados
- Manejo de datos desbalanceados

#### 3. Análisis de Gráficas
**Archivo:** `preguntas-graficas-cliente-insight.md` ([PDF](preguntas-graficas-cliente-insight.pdf) | [HTML](preguntas-graficas-cliente-insight.html))

Análisis detallado de las 15 visualizaciones:
- Interpretación de cada gráfica
- Insights de negocio
- Patrones identificados
- Recomendaciones basadas en datos

#### 4. Informes Automáticos
**Archivo:** `informe_churn_*.md`

Reportes generados automáticamente que incluyen:
- Resumen ejecutivo del dataset
- Métricas de rendimiento actualizadas
- Matriz de confusión
- Top 10 features más importantes
- Comparativa de técnicas de balanceo
- Validación de robustez
- Recomendaciones de acción
- Impacto esperado en el negocio

### 📊 Visualizaciones

El proyecto genera **15 gráficas** profesionales guardadas en `graficas_churn/`:

| Gráfica | Descripción | Insights |
|---------|-------------|----------|
| `grafica_01.png` | Distribución de Churn | 26.54% de clientes abandonan |
| `grafica_02.png` | Churn por Género | Sin diferencia significativa |
| `grafica_03.png` | Churn por Senior Citizen | Mayores tienen más churn |
| `grafica_04.png` | Churn por Partner | Sin pareja = más churn |
| `grafica_05.png` | Churn por Dependents | Sin dependientes = más churn |
| `grafica_06.png` | Churn por Tipo de Contrato | Mes a mes = alto churn |
| `grafica_07.png` | Churn por Método de Pago | Cheque electrónico = más churn |
| `grafica_08.png` | Churn por Internet Service | Fibra óptica = más churn |
| `grafica_09.png` | Distribución de Tenure | Clientes nuevos en riesgo |
| `grafica_10.png` | Distribución de Monthly Charges | Cargos altos = más churn |
| `grafica_11.png` | Distribución de Total Charges | Correlación con tenure |
| `grafica_12.png` | Correlación de Variables | Heatmap de relaciones |
| `grafica_13.png` | Feature Importance | Top 10 características |
| `grafica_14.png` | Curva ROC | ROC-AUC = 0.8505 |
| `grafica_15.png` | Matriz de Confusión | Rendimiento del modelo |

### 🎯 Formatos Disponibles

Toda la documentación está disponible en múltiples formatos:
- **Markdown (.md)**: Para visualización en GitHub y editores
- **PDF (.pdf)**: Para impresión y distribución
- **HTML (.html)**: Para visualización en navegadores

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. **Commit** tus cambios (`git commit -m 'Agregar nueva característica'`)
4. **Push** a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un **Pull Request**

### Áreas de Contribución

- 🐛 Corrección de bugs
- ✨ Nuevas características
- 📚 Mejoras de documentación
- 🧪 Tests adicionales
- 🎨 Mejoras de UI/UX

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👥 Autores

Este proyecto fue desarrollado por:

- **Anderson Tabima**
- **Antony Tabima**
- **Yhabeidy Alejandra Agudelo**
- **Carlos Mario Londoño**
- **Natalia Bedoya**
- **Sebastian Cano**
- **Álvaro Ángel Molina** - [@alvaretto](https://github.com/alvaretto)

---

## 📞 Contacto y Soporte

- 🌐 **Aplicación en Vivo**: [clienteinsight-ai.vercel.app](https://clienteinsight-ai.vercel.app/)
- 🐛 **Reportar Issues**: [GitHub Issues](https://github.com/alvaretto/cliente-insight/issues)
- 📧 **Contacto**: [@alvaretto](https://github.com/alvaretto)

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡dale una estrella!

[![GitHub stars](https://img.shields.io/github/stars/alvaretto/cliente-insight?style=social)](https://github.com/alvaretto/cliente-insight)

**[🚀 Ver Demo en Vivo](https://clienteinsight-ai.vercel.app/)**

</div>

