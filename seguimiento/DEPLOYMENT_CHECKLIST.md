# ✅ CHECKLIST DE DEPLOYMENT - TELCO CHURN PREDICTION

## 📋 PRE-DEPLOYMENT ✅ COMPLETADO

### Verificación de archivos ✅
- [x] Modelo entrenado (`models/churn_model.pkl` - 65 MB) ✅ Verificado
- [x] Preprocessor (`models/preprocessor.pkl` - 7.6 KB) ✅ Verificado
- [x] Metadata (`models/metadata.json`) ✅ Verificado
- [x] Git LFS configurado (`.gitattributes`) ✅ Funcionando
- [x] API completa (`api/app.py` + `api/requirements.txt`) ✅ 8 dependencias
- [x] Dashboard completo (`dashboard/app.py` + páginas) ✅ 9 dependencias
- [x] Dockerfile para API (`api/Dockerfile`) ✅ Python 3.10-slim
- [x] Configuración Render (`render.yaml`) ✅ Configuración completa
- [x] Configuración Streamlit (`.streamlit/config.toml`) ✅ Configuración completa
- [x] Python version files (`.python-version`, `runtime.txt`) ✅ Python 3.10.13

### Verificación de Git ✅
- [x] Todo committed ✅ Commit: 35245bf
- [x] Todo pushed a GitHub ✅ origin/main actualizado
- [x] Git LFS funcionando (archivos .pkl como punteros) ✅ e9ed72b416, ef8c75c218
- [x] Branch: `main` ✅ Activo

---

## 🚀 DEPLOYMENT - PARTE 1: API EN RENDER ✅ COMPLETADO

### Paso 1: Preparación (2 min) ✅
- [x] Abrir https://render.com en navegador
- [x] Tener GitHub abierto en otra pestaña
- [x] Tener este checklist visible

### Paso 2: Crear cuenta (3 min) ✅
- [x] Click en "Get Started"
- [x] Seleccionar "Sign up with GitHub"
- [x] Autorizar Render a acceder a GitHub
- [x] Confirmar email (si es necesario)

### Paso 3: Conectar repositorio (2 min) ✅
- [x] En dashboard de Render, click "New +" → "Web Service"
- [x] Click "Connect a repository"
- [x] Si no ves el repo: "Configure account" → "All repositories"
- [x] Buscar: `telco-customer-churn-prediction`
- [x] Click "Connect"

### Paso 4: Configurar servicio (5 min) ✅
- [x] **Name**: `telco-churn-api`
- [x] **Region**: Oregon (US West) o el más cercano
- [x] **Branch**: `main`
- [x] **Root Directory**: `api`
- [x] **Runtime**: Python 3
- [x] **Build Command**: `pip install -r requirements.txt`
- [x] **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app`
- [x] **Instance Type**: Free

### Paso 5: Variables de entorno (2 min) ✅
- [x] Click "Advanced"
- [x] Click "Add Environment Variable"
- [x] Key: `PYTHON_VERSION`, Value: `3.10.13`
- [x] Key: `FLASK_ENV`, Value: `production`

### Paso 6: Deploy (10 min) ✅
- [x] Click "Create Web Service"
- [x] Esperar mientras Render:
  - [x] Clona el repositorio
  - [x] Descarga archivos Git LFS (modelo 65 MB)
  - [x] Instala dependencias
  - [x] Inicia la aplicación
- [x] Ver logs en tiempo real
- [x] Esperar mensaje: "Your service is live 🎉"

### Paso 7: Verificar API (3 min) ✅
- [x] Copiar URL: `https://telco-churn-api-y9xy.onrender.com`
- [x] Guardar URL en archivo de texto
- [x] Probar en navegador: `https://telco-churn-api-y9xy.onrender.com/health`
- [x] Responde: `{"status": "healthy", "model_loaded": true, ...}` ✅
- [x] Probar: `https://telco-churn-api-y9xy.onrender.com/model_info`
- [x] Muestra métricas del modelo ✅

### Paso 8: Mejoras Implementadas (30 min) ✅
- [x] Implementar feature engineering automático
- [x] Actualizar API para aceptar datos categóricos originales
- [x] Actualizar scikit-learn a 1.5.2
- [x] Actualizar joblib a 1.4.2
- [x] Agregar metadata con versiones de librerías
- [x] Actualizar documentación (README.md, API_USAGE.md)
- [x] Probar predicciones con datos categóricos
- [x] Verificar funcionamiento completo

**✅ API DEPLOYADA Y MEJORADA - Tiempo total: ~55 minutos**
**URL**: `https://telco-churn-api-y9xy.onrender.com`
**Fecha**: 2025-11-20

---

## 📊 DEPLOYMENT - PARTE 2: DASHBOARD EN STREAMLIT CLOUD ✅ COMPLETADO

### Paso 1: Preparación (1 min) ✅
- [x] Abrir https://share.streamlit.io en navegador
- [x] Tener la URL de la API de Render lista

### Paso 2: Crear cuenta (2 min) ✅
- [x] Click "Sign in"
- [x] Seleccionar "Continue with GitHub"
- [x] Autorizar Streamlit

### Paso 3: Crear app (3 min) ✅
- [x] Click "New app"
- [x] **Repository**: `alvaretto/telco-customer-churn-prediction`
- [x] **Branch**: `main`
- [x] **Main file path**: `dashboard/app.py`
- [x] **App URL**: `telco-churn-dashboard-ml`

### Paso 4: Configuración avanzada (2 min) ✅
- [x] Click "Advanced settings"
- [x] **Python version**: 3.10
- [x] Click "Save"

### Paso 5: Deploy (5 min) ✅
- [x] Click "Deploy!"
- [x] Esperar mientras Streamlit:
  - [x] Clona el repositorio
  - [x] Descarga archivos Git LFS
  - [x] Instala dependencias de `requirements.txt`
  - [x] Ejecuta `dashboard/app.py`
- [x] Ver logs en tiempo real
- [x] Esperar a que cargue la aplicación

### Paso 6: Resolver Errores (15 min) ✅
- [x] Error en `packages.txt` - Eliminado archivo con comentarios problemáticos
- [x] Error en predicción - Agregado preprocesador y feature engineering
- [x] Pusheado cambios a GitHub
- [x] Reboot app en Streamlit Cloud
- [x] Verificar que funcione correctamente

### Paso 7: Verificar Dashboard (5 min) ✅
- [x] Copiar URL: `https://telco-churn-dashboard-ml.streamlit.app`
- [x] Guardar URL
- [x] Verificar página Home carga correctamente ✅
- [x] Navegar a "📊 Overview" - carga correctamente ✅
- [x] Navegar a "🎯 Risk Analysis" - carga formulario ✅
- [x] Llenar formulario de prueba ✅
- [x] Click "Predict Churn Risk" ✅
- [x] Verificar que muestra predicción ✅
- [x] Navegar a "📈 Model Metrics" - muestra métricas ✅
- [x] Navegar a "💰 ROI Simulator" - carga correctamente ✅
- [x] Navegar a "🔍 Model Monitoring" - carga correctamente ✅

**✅ DASHBOARD DEPLOYADO Y FUNCIONANDO - Tiempo total: ~40 minutos**
**URL**: `https://telco-churn-dashboard-ml.streamlit.app`
**Fecha**: 2025-11-21

---

## 🎯 VERIFICACIÓN FINAL

### URLs del proyecto
- [x] **API**: `https://telco-churn-api-y9xy.onrender.com` ✅
- [x] **Dashboard**: `https://telco-churn-dashboard-ml.streamlit.app` ✅
- [x] **GitHub**: `https://github.com/alvaretto/telco-customer-churn-prediction` ✅

### Tests funcionales - API
- [x] API `/health` responde correctamente ✅
- [x] API `/model_info` muestra métricas ✅
- [x] API `/predict` acepta predicciones con datos categóricos ✅
- [x] Predicción de cliente alto riesgo funciona ✅
- [x] Predicción de cliente bajo riesgo funciona ✅
- [x] Feature engineering automático funciona ✅

### Tests funcionales - Dashboard
- [x] Dashboard carga todas las páginas ✅
- [x] Dashboard puede hacer predicciones ✅
- [x] Métricas del modelo se muestran correctamente ✅
- [x] Formulario de Risk Analysis funciona ✅
- [x] Preprocesador aplicado correctamente ✅
- [x] Feature engineering integrado ✅

### Documentación
- [x] Actualizar README.md con URLs de producción ✅
- [x] Actualizar `URLS_PRODUCCION.md` con las URLs ✅
- [x] Actualizar `api/README.md` con feature engineering ✅
- [x] Actualizar `DEPLOYMENT_CHECKLIST.md` ✅
- [x] Actualizar `seguimiento-estructura-completa.md` ✅

---

## 📝 PRÓXIMOS PASOS OPCIONALES

### Mejoras inmediatas
- [ ] Configurar dominio personalizado (Render + Streamlit)
- [ ] Agregar Google Analytics al dashboard
- [ ] Configurar alertas de uptime (UptimeRobot)
- [ ] Agregar badge de status al README

### CI/CD
- [ ] Configurar GitHub Actions para tests automáticos
- [ ] Configurar auto-deploy en cada push
- [ ] Agregar linting (flake8, black)
- [ ] Agregar coverage reports

### Monitoreo
- [ ] Configurar Sentry para error tracking
- [ ] Configurar logs centralizados
- [ ] Dashboard de métricas de uso
- [ ] Alertas de performance

### Seguridad
- [ ] Agregar rate limiting a la API
- [ ] Configurar HTTPS (ya incluido en Render/Streamlit)
- [ ] Agregar autenticación (opcional)
- [ ] Configurar CORS específico (no wildcard)

---

## 🐛 TROUBLESHOOTING RÁPIDO

### API no inicia
1. Ver logs en Render
2. Verificar que Git LFS descargó los archivos .pkl
3. Verificar que `PYTHON_VERSION=3.10.13`
4. Verificar rutas de archivos en `app.py`

### Dashboard no carga modelo
1. Ver logs en Streamlit Cloud
2. Verificar que archivos .pkl están en `models/`
3. Verificar rutas relativas en el código
4. Reboot app desde Streamlit dashboard

### Build failed
1. Verificar `requirements.txt` existe
2. Verificar versiones de dependencias
3. Clear build cache y redeploy

---

## ✅ DEPLOYMENT COMPLETADO

**Fecha**: _______________
**API URL**: _______________
**Dashboard URL**: _______________
**Tiempo total**: ~45 minutos

**Estado**: 🎉 **LISTO PARA PRODUCCIÓN**

---

## 📊 MÉTRICAS DE DEPLOYMENT

- **Tamaño del modelo**: 65 MB
- **Tiempo de carga del modelo**: ~2-3 segundos
- **RAM usada (API)**: ~200-300 MB
- **RAM usada (Dashboard)**: ~400-500 MB
- **Tiempo de respuesta API**: <500ms
- **Uptime esperado**: 99%+ (Render Free puede dormir)

---

**Notas**:
- Render Free tier se duerme después de 15 min sin actividad
- Primera request después de dormir tarda ~30 segundos
- Streamlit Cloud Free: máximo 3 apps, 1 GB RAM por app
- Git LFS Free: 1 GB storage, 1 GB bandwidth/mes

