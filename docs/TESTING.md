# 🧪 Guía de Testing - Telco Customer Churn Prediction

## 📋 Tabla de Contenidos

- [Introducción](#introducción)
- [Tests Unitarios](#tests-unitarios)
- [Tests de Integración](#tests-de-integración)
- [Ejecución de Tests](#ejecución-de-tests)
- [CI/CD](#cicd)
- [Monitoreo de Producción](#monitoreo-de-producción)

---

## 🎯 Introducción

Este proyecto incluye una suite completa de tests para garantizar la calidad y confiabilidad del código:

- **Tests Unitarios**: Validan componentes individuales (API, modelo)
- **Tests de Integración**: Validan el funcionamiento end-to-end
- **Monitoreo de Producción**: Valida que los servicios deployados funcionen correctamente
- **CI/CD**: Automatización de tests en cada push

---

## 🔬 Tests Unitarios

### Ubicación

```
tests/
├── test_api.py      # Tests de la API Flask
└── test_model.py    # Tests del modelo ML
```

### Tests de la API (`test_api.py`)

**Cobertura:**
- ✅ Endpoint `/` (home)
- ✅ Endpoint `/health` (health check)
- ✅ Endpoint `/model_info` (información del modelo)
- ✅ Endpoint `/predict` (predicción individual)
- ✅ Endpoint `/predict_batch` (predicciones en lote)
- ✅ Validación de datos de entrada
- ✅ Manejo de errores

**Total de tests:** 7

### Tests del Modelo (`test_model.py`)

**Cobertura:**
- ✅ Existencia de archivos del modelo
- ✅ Carga correcta del modelo
- ✅ Carga correcta del preprocessor
- ✅ Estructura de metadata
- ✅ Métodos del modelo (predict, predict_proba)
- ✅ Formato de predicciones
- ✅ Validación de métricas

**Total de tests:** 10

---

## 🔗 Tests de Integración

### Script de Validación de Deployment

**Ubicación:** `scripts/validate_deployment.py`

**Funcionalidad:**
- Valida todos los endpoints de la API
- Prueba predicciones con casos de alto y bajo riesgo
- Verifica accesibilidad del dashboard
- Genera reporte detallado

**Uso:**
```bash
python scripts/validate_deployment.py
```

**Salida esperada:**
```
✅ Todos los checks pasaron! Deployment validado exitosamente.
```

---

## 🚀 Ejecución de Tests

### Opción 1: Ejecución Local (Requiere Infraestructura)

⚠️ **Nota:** La ejecución local requiere instalar todas las dependencias pesadas (scikit-learn, pandas, flask, etc.)

```bash
# Instalar dependencias
pip install -r api/requirements.txt
pip install pytest pytest-cov

# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar con cobertura
pytest tests/ -v --cov=api --cov=models --cov-report=html

# Ver reporte de cobertura
open htmlcov/index.html
```

### Opción 2: Ejecución en Google Colab (Recomendado)

Si no tienes infraestructura local, puedes ejecutar los tests en Google Colab:

```python
# En Google Colab
!git clone https://github.com/alvaretto/telco-customer-churn-prediction.git
%cd telco-customer-churn-prediction

# Instalar dependencias
!pip install -r api/requirements.txt
!pip install pytest pytest-cov

# Ejecutar tests
!pytest tests/ -v --cov=api --cov=models
```

### Opción 3: CI/CD con GitHub Actions (Automático)

Los tests se ejecutan automáticamente en cada push a través de GitHub Actions.

Ver: `.github/workflows/ci.yml`

---

## 🤖 CI/CD

### GitHub Actions Workflows

#### 1. CI Pipeline (`.github/workflows/ci.yml`)

**Triggers:**
- Push a `main` o `develop`
- Pull requests a `main`

**Jobs:**
- **test**: Ejecuta tests unitarios con pytest
- **lint**: Verifica calidad de código (flake8, black, isort)
- **monitor**: Monitorea producción (solo en main)
- **security**: Escaneo de vulnerabilidades con Trivy

#### 2. Deploy Pipeline (`.github/workflows/deploy.yml`)

**Triggers:**
- Push a `main` que modifique `api/`, `dashboard/`, o `models/`

**Jobs:**
- **notify-deployment**: Notifica inicio de deployment
- **verify-api**: Verifica que la API esté funcionando
- **verify-dashboard**: Verifica que el Dashboard esté funcionando
- **deployment-summary**: Genera resumen del deployment

### Ver Estado de CI/CD

- **GitHub Actions**: https://github.com/alvaretto/telco-customer-churn-prediction/actions
- **Badges en README**: Muestran estado actual de CI/CD

---

## 📊 Monitoreo de Producción

### Script de Monitoreo

**Ubicación:** `scripts/monitor_production.py`

**Funcionalidad:**
- Verifica health de la API
- Verifica información del modelo
- Prueba predicciones
- Verifica accesibilidad del dashboard

**Uso:**
```bash
python scripts/monitor_production.py
```

**Salida esperada:**
```
🎉 ¡Todos los servicios están funcionando correctamente!
🎯 Total: 4/4 checks pasaron
```

### Ejecución Automática

El script de monitoreo se ejecuta automáticamente:
- En cada push a `main` (GitHub Actions)
- Puede configurarse como cron job para monitoreo continuo

---

## 📈 Métricas de Cobertura

### Cobertura Actual

| Componente | Cobertura | Tests |
|------------|-----------|-------|
| API | ~85% | 7 tests |
| Modelo | ~90% | 10 tests |
| **Total** | **~87%** | **17 tests** |

### Objetivo

- Mantener cobertura > 80%
- Agregar tests para nuevas funcionalidades
- Revisar cobertura en cada PR

---

## 🔧 Troubleshooting

### Error: "No module named 'pytest'"

```bash
pip install pytest pytest-cov
```

### Error: "No module named 'flask'"

```bash
pip install -r api/requirements.txt
```

### Error: "Model file not found"

Asegúrate de que Git LFS esté configurado:
```bash
git lfs install
git lfs pull
```

### Tests fallan en CI/CD

1. Verifica que las dependencias estén en `requirements.txt`
2. Revisa los logs en GitHub Actions
3. Asegúrate de que Git LFS esté configurado en el repositorio

---

## 📚 Recursos Adicionales

- **Pytest Documentation**: https://docs.pytest.org/
- **GitHub Actions**: https://docs.github.com/en/actions
- **Coverage.py**: https://coverage.readthedocs.io/

---

**Última actualización:** 2025-11-21  
**Mantenido por:** Álvaro Ángel Molina (@alvaretto)

