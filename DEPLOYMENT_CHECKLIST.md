# ✅ CHECKLIST DE DEPLOYMENT - TELCO CHURN PREDICTION

## 📋 PRE-DEPLOYMENT

### Verificación de archivos
- [x] Modelo entrenado (`models/churn_model.pkl` - 65 MB)
- [x] Preprocessor (`models/preprocessor.pkl` - 7.6 KB)
- [x] Metadata (`models/metadata.json`)
- [x] Git LFS configurado (`.gitattributes`)
- [x] API completa (`api/app.py` + `api/requirements.txt`)
- [x] Dashboard completo (`dashboard/app.py` + páginas)
- [x] Dockerfile para API (`api/Dockerfile`)
- [x] Configuración Render (`render.yaml`)
- [x] Configuración Streamlit (`.streamlit/config.toml`)
- [x] Python version files (`.python-version`, `runtime.txt`)

### Verificación de Git
- [x] Todo committed
- [x] Todo pushed a GitHub
- [x] Git LFS funcionando (archivos .pkl como punteros)
- [x] Branch: `main`

---

## 🚀 DEPLOYMENT - PARTE 1: API EN RENDER

### Paso 1: Preparación (2 min)
- [ ] Abrir https://render.com en navegador
- [ ] Tener GitHub abierto en otra pestaña
- [ ] Tener este checklist visible

### Paso 2: Crear cuenta (3 min)
- [ ] Click en "Get Started"
- [ ] Seleccionar "Sign up with GitHub"
- [ ] Autorizar Render a acceder a GitHub
- [ ] Confirmar email (si es necesario)

### Paso 3: Conectar repositorio (2 min)
- [ ] En dashboard de Render, click "New +" → "Web Service"
- [ ] Click "Connect a repository"
- [ ] Si no ves el repo: "Configure account" → "All repositories"
- [ ] Buscar: `telco-customer-churn-prediction`
- [ ] Click "Connect"

### Paso 4: Configurar servicio (5 min)
- [ ] **Name**: `telco-churn-api`
- [ ] **Region**: Oregon (US West) o el más cercano
- [ ] **Branch**: `main`
- [ ] **Root Directory**: `api`
- [ ] **Runtime**: Python 3
- [ ] **Build Command**: `pip install -r requirements.txt`
- [ ] **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app`
- [ ] **Instance Type**: Free

### Paso 5: Variables de entorno (2 min)
- [ ] Click "Advanced"
- [ ] Click "Add Environment Variable"
- [ ] Key: `PYTHON_VERSION`, Value: `3.10.13`
- [ ] Key: `FLASK_ENV`, Value: `production`

### Paso 6: Deploy (10 min)
- [ ] Click "Create Web Service"
- [ ] Esperar mientras Render:
  - [ ] Clona el repositorio
  - [ ] Descarga archivos Git LFS (modelo 65 MB)
  - [ ] Instala dependencias
  - [ ] Inicia la aplicación
- [ ] Ver logs en tiempo real
- [ ] Esperar mensaje: "Your service is live 🎉"

### Paso 7: Verificar API (3 min)
- [ ] Copiar URL (ej: `https://telco-churn-api.onrender.com`)
- [ ] Guardar URL en un archivo de texto
- [ ] Probar en navegador: `https://tu-url.onrender.com/health`
- [ ] Debe responder: `{"status": "healthy", "model_loaded": true, ...}`
- [ ] Probar: `https://tu-url.onrender.com/model_info`
- [ ] Debe mostrar métricas del modelo

**✅ API DEPLOYADA - Tiempo total: ~25 minutos**

---

## 📊 DEPLOYMENT - PARTE 2: DASHBOARD EN STREAMLIT CLOUD

### Paso 1: Preparación (1 min)
- [ ] Abrir https://share.streamlit.io en navegador
- [ ] Tener la URL de la API de Render lista

### Paso 2: Crear cuenta (2 min)
- [ ] Click "Sign in"
- [ ] Seleccionar "Continue with GitHub"
- [ ] Autorizar Streamlit

### Paso 3: Crear app (3 min)
- [ ] Click "New app"
- [ ] **Repository**: `alvaretto/telco-customer-churn-prediction`
- [ ] **Branch**: `main`
- [ ] **Main file path**: `dashboard/app.py`
- [ ] **App URL**: `telco-churn-dashboard` (o personalizado)

### Paso 4: Configuración avanzada (2 min)
- [ ] Click "Advanced settings"
- [ ] **Python version**: 3.10
- [ ] Click "Save"

### Paso 5: Deploy (5 min)
- [ ] Click "Deploy!"
- [ ] Esperar mientras Streamlit:
  - [ ] Clona el repositorio
  - [ ] Descarga archivos Git LFS
  - [ ] Instala dependencias de `dashboard/requirements.txt`
  - [ ] Ejecuta `dashboard/app.py`
- [ ] Ver logs en tiempo real
- [ ] Esperar a que cargue la aplicación

### Paso 6: Verificar Dashboard (5 min)
- [ ] Copiar URL (ej: `https://telco-churn-dashboard.streamlit.app`)
- [ ] Guardar URL
- [ ] Verificar página Home carga correctamente
- [ ] Navegar a "📊 Overview" - debe cargar
- [ ] Navegar a "🎯 Risk Analysis" - debe cargar formulario
- [ ] Llenar formulario de prueba
- [ ] Click "Predict Churn Risk"
- [ ] Verificar que muestra predicción
- [ ] Navegar a "📈 Model Metrics" - debe mostrar métricas
- [ ] Navegar a "💰 ROI Simulator" - debe cargar
- [ ] Navegar a "🔍 Model Monitoring" - debe cargar

**✅ DASHBOARD DEPLOYADO - Tiempo total: ~18 minutos**

---

## 🎯 VERIFICACIÓN FINAL

### URLs del proyecto
- [ ] **API**: `https://_____________________.onrender.com`
- [ ] **Dashboard**: `https://_____________________.streamlit.app`
- [ ] **GitHub**: `https://github.com/alvaretto/telco-customer-churn-prediction`

### Tests funcionales
- [ ] API `/health` responde correctamente
- [ ] API `/model_info` muestra métricas
- [ ] API `/predict` acepta predicciones (probar con curl o Postman)
- [ ] Dashboard carga todas las páginas
- [ ] Dashboard puede hacer predicciones
- [ ] Métricas del modelo se muestran correctamente

### Documentación
- [ ] Actualizar README.md con URLs de producción
- [ ] Actualizar `seguimiento-estructura-completa.md`
- [ ] Crear archivo `URLS_PRODUCCION.md` con las URLs

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

