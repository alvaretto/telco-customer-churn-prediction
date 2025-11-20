# 🚀 GUÍA DETALLADA DE DEPLOYMENT - PASO A PASO

**Proyecto**: Telco Customer Churn Prediction  
**Fecha**: 2025-11-20  
**Tiempo estimado**: 30-40 minutos  
**Prerequisitos**: ✅ Todos verificados

---

## ✅ PRE-DEPLOYMENT COMPLETADO

- ✅ Modelo entrenado (65 MB) y serializado
- ✅ Git LFS configurado y funcionando
- ✅ Todos los archivos committed y pushed
- ✅ Configuración verificada (runtime.txt, render.yaml)
- ✅ Requirements.txt completos (API: 8 deps, Dashboard: 9 deps)
- ✅ Scripts de verificación creados

---

## 🎯 PARTE 1: DEPLOYMENT DE LA API EN RENDER.COM

### ⏱️ Tiempo estimado: 20-25 minutos

### Paso 1: Crear cuenta en Render (3 minutos)

1. **Abre tu navegador** y ve a: https://render.com

2. **Click en "Get Started"** (botón azul en la esquina superior derecha)

3. **Selecciona "Sign up with GitHub"**
   - Esto te redirigirá a GitHub para autorizar
   - Click en "Authorize Render"
   - Confirma tu contraseña de GitHub si te lo pide

4. **Verifica tu email** (si es necesario)
   - Revisa tu bandeja de entrada
   - Click en el link de verificación

5. **Completa tu perfil** (opcional)
   - Nombre, empresa, etc.
   - Puedes saltarte esto y hacerlo después

✅ **Checkpoint**: Deberías estar en el Dashboard de Render

---

### Paso 2: Conectar tu repositorio (2 minutos)

1. **En el Dashboard de Render**, click en **"New +"** (esquina superior derecha)

2. **Selecciona "Web Service"**

3. **Conectar repositorio**:
   - Si es la primera vez, click en **"Connect a repository"**
   - Verás una lista de tus repositorios de GitHub
   - Si NO ves `telco-customer-churn-prediction`:
     - Click en **"Configure account"**
     - Selecciona **"All repositories"** o busca el repo específico
     - Click en **"Save"**

4. **Busca y selecciona** `telco-customer-churn-prediction`

5. **Click en "Connect"**

✅ **Checkpoint**: Deberías ver la pantalla de configuración del servicio

---

### Paso 3: Configurar el servicio (5 minutos)

**IMPORTANTE**: Copia exactamente estos valores

1. **Name**: `telco-churn-api`
   - Este será parte de tu URL: `telco-churn-api.onrender.com`

2. **Region**: Selecciona **Oregon (US West)** o el más cercano a ti

3. **Branch**: `main`
   - Debe estar seleccionado por defecto

4. **Root Directory**: `api`
   - ⚠️ MUY IMPORTANTE: Escribe exactamente `api`
   - Esto le dice a Render que use solo la carpeta `api/`

5. **Runtime**: Debe detectar automáticamente **Python 3**
   - Si no, selecciona "Python 3" del dropdown

6. **Build Command**:
   ```
   pip install -r requirements.txt
   ```
   - Copia y pega exactamente esto

7. **Start Command**:
   ```
   gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app
   ```
   - Copia y pega exactamente esto
   - ⚠️ Asegúrate de que no haya espacios extra

8. **Instance Type**: Selecciona **Free**
   - 512 MB RAM, suficiente para nuestro modelo

✅ **Checkpoint**: Todos los campos deberían estar llenos

---

### Paso 4: Configurar variables de entorno (2 minutos)

1. **Scroll down** hasta la sección **"Environment Variables"**

2. **Click en "Advanced"** para expandir

3. **Click en "Add Environment Variable"**

4. **Agrega la primera variable**:
   - **Key**: `PYTHON_VERSION`
   - **Value**: `3.10.13`
   - Click en "Add"

5. **Click en "Add Environment Variable"** nuevamente

6. **Agrega la segunda variable**:
   - **Key**: `FLASK_ENV`
   - **Value**: `production`
   - Click en "Add"

✅ **Checkpoint**: Deberías ver 2 variables de entorno configuradas

---

### Paso 5: Iniciar el deployment (10-15 minutos)

1. **Scroll hasta el final** de la página

2. **Click en "Create Web Service"** (botón azul grande)

3. **Espera mientras Render**:
   - ⏳ Clona el repositorio (~30 segundos)
   - ⏳ Descarga archivos Git LFS (~1-2 minutos)
     - Verás: "Downloading models/churn_model.pkl (65 MB)"
   - ⏳ Instala dependencias (~3-5 minutos)
     - Verás: "Installing flask, scikit-learn, etc."
   - ⏳ Inicia la aplicación (~1-2 minutos)
     - Verás: "Starting gunicorn..."

4. **Monitorea los logs** en tiempo real
   - Deberías ver mensajes como:
     ```
     ==> Cloning from https://github.com/alvaretto/telco-customer-churn-prediction...
     ==> Downloading Git LFS files...
     ==> Installing dependencies...
     ==> Starting service...
     ✅ Model and preprocessor loaded successfully
     ```

5. **Espera el mensaje final**:
   ```
   ==> Your service is live 🎉
   ```

✅ **Checkpoint**: El deployment debería estar completo

---

### Paso 6: Verificar el deployment de la API (3 minutos)

1. **Copia la URL de tu API**
   - Render te mostrará la URL en la parte superior
   - Ejemplo: `https://telco-churn-api.onrender.com`
   - Click en el icono de copiar 📋

2. **Abre una nueva pestaña** en tu navegador

3. **Prueba el endpoint de health**:
   - Pega la URL y agrega `/health` al final
   - Ejemplo: `https://telco-churn-api.onrender.com/health`
   - Presiona Enter

4. **Deberías ver una respuesta JSON**:
   ```json
   {
     "status": "healthy",
     "model_loaded": true,
     "preprocessor_loaded": true,
     "timestamp": "2025-11-20T..."
   }
   ```

5. **Prueba el endpoint de model_info**:
   - Cambia `/health` por `/model_info`
   - Deberías ver las métricas del modelo (ROC-AUC: 0.87, etc.)

6. **Ejecuta el script de verificación**:
   ```bash
   ./scripts/verify_api_deployment.sh https://telco-churn-api.onrender.com
   ```
   - Reemplaza la URL con tu URL real
   - El script ejecutará 4 tests automáticos

✅ **Checkpoint**: La API está funcionando correctamente

**🎉 ¡API DEPLOYADA EXITOSAMENTE!**

---

## 🎯 PARTE 2: DEPLOYMENT DEL DASHBOARD EN STREAMLIT CLOUD

### ⏱️ Tiempo estimado: 15-20 minutos

### Paso 1: Crear cuenta en Streamlit Cloud (2 minutos)

1. **Abre tu navegador** y ve a: https://share.streamlit.io

2. **Click en "Sign in"** (esquina superior derecha)

3. **Selecciona "Continue with GitHub"**
   - Esto te redirigirá a GitHub para autorizar
   - Click en "Authorize streamlit"
   - Confirma tu contraseña de GitHub si te lo pide

4. **Acepta los términos** (si te lo pide)

✅ **Checkpoint**: Deberías estar en el Dashboard de Streamlit Cloud

---

### Paso 2: Crear nueva app (3 minutos)

1. **En el Dashboard de Streamlit**, click en **"New app"** (botón azul)

2. **Configurar la app**:

   **Repository**:
   - Selecciona `alvaretto/telco-customer-churn-prediction`
   - Si no lo ves, click en "Paste GitHub URL" y pega:
     ```
     https://github.com/alvaretto/telco-customer-churn-prediction
     ```

   **Branch**:
   - Selecciona `main`

   **Main file path**:
   - Escribe exactamente: `dashboard/app.py`
   - ⚠️ MUY IMPORTANTE: Debe ser exactamente `dashboard/app.py`

   **App URL** (opcional):
   - Puedes personalizar la URL
   - Ejemplo: `telco-churn-dashboard`
   - O dejar el default que Streamlit genera

✅ **Checkpoint**: Todos los campos deberían estar llenos

---

### Paso 3: Configuración avanzada (2 minutos)

1. **Click en "Advanced settings"** (abajo del formulario)

2. **Python version**:
   - Selecciona **3.10** del dropdown
   - ⚠️ IMPORTANTE: Debe ser 3.10, no 3.11 o 3.12

3. **Secrets** (opcional, déjalo vacío por ahora)

4. **Click en "Save"**

✅ **Checkpoint**: Configuración avanzada guardada

---

### Paso 4: Iniciar el deployment (5-10 minutos)

1. **Click en "Deploy!"** (botón azul grande)

2. **Espera mientras Streamlit**:
   - ⏳ Clona el repositorio (~30 segundos)
   - ⏳ Descarga archivos Git LFS (~1-2 minutos)
     - Verás: "Downloading LFS files..."
   - ⏳ Instala dependencias (~2-3 minutos)
     - Verás: "Installing requirements..."
   - ⏳ Ejecuta la aplicación (~1-2 minutos)
     - Verás: "Running dashboard/app.py..."

3. **Monitorea los logs** en la parte inferior
   - Deberías ver mensajes como:
     ```
     Cloning repository...
     Downloading Git LFS files...
     Installing dependencies from dashboard/requirements.txt...
     Starting Streamlit app...
     ```

4. **Espera a que cargue la aplicación**
   - Verás la interfaz del dashboard aparecer
   - Puede tardar 5-10 minutos la primera vez

✅ **Checkpoint**: El dashboard debería estar visible

---

### Paso 5: Verificar el deployment del Dashboard (5 minutos)

1. **Copia la URL del Dashboard**
   - Streamlit te mostrará la URL en la parte superior
   - Ejemplo: `https://telco-churn-dashboard.streamlit.app`

2. **Verifica la página principal**:
   - Deberías ver el título "Telco Customer Churn Prediction"
   - Métricas del modelo (ROC-AUC: 0.87, etc.)
   - Sin errores en la barra lateral

3. **Navega a cada página** (usa la barra lateral):
   - 📊 **Overview** - Debe cargar estadísticas
   - 🎯 **Risk Analysis** - Debe mostrar formulario de predicción
   - 📈 **Model Metrics** - Debe mostrar matriz de confusión y ROC curve
   - 💰 **ROI Simulator** - Debe mostrar calculadora
   - 🔍 **Model Monitoring** - Debe mostrar gráficos de monitoreo

4. **Prueba hacer una predicción**:
   - Ve a "🎯 Risk Analysis"
   - Llena el formulario con datos de prueba
   - Click en "Predict Churn Risk"
   - Deberías ver la predicción y probabilidad

5. **Ejecuta el script de verificación**:
   ```bash
   ./scripts/verify_dashboard_deployment.sh https://telco-churn-dashboard.streamlit.app
   ```
   - Reemplaza la URL con tu URL real
   - Sigue las instrucciones del script

✅ **Checkpoint**: El Dashboard está funcionando correctamente

**🎉 ¡DASHBOARD DEPLOYADO EXITOSAMENTE!**

---

## 🎯 PARTE 3: POST-DEPLOYMENT

### ⏱️ Tiempo estimado: 5 minutos

### Paso 1: Actualizar URLs en documentación (2 minutos)

1. **Ejecuta el script de actualización**:
   ```bash
   ./scripts/update_production_urls.sh \
     https://telco-churn-api.onrender.com \
     https://telco-churn-dashboard.streamlit.app
   ```
   - Reemplaza las URLs con tus URLs reales
   - Esto actualizará `URLS_PRODUCCION.md` automáticamente

2. **Verifica el archivo generado**:
   ```bash
   cat URLS_PRODUCCION.md
   ```

✅ **Checkpoint**: URLS_PRODUCCION.md actualizado

---

### Paso 2: Actualizar README.md (2 minutos)

1. **Abre README.md** en tu editor

2. **Agrega los badges** al inicio del archivo (después del título):
   ```markdown
   [![API Status](https://img.shields.io/badge/API-Live-success)](https://telco-churn-api.onrender.com)
   [![Dashboard](https://img.shields.io/badge/Dashboard-Live-success)](https://telco-churn-dashboard.streamlit.app)
   [![Python](https://img.shields.io/badge/Python-3.10.13-blue)](https://www.python.org/)
   [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
   ```

3. **Agrega una sección de "Demo en Vivo"**:
   ```markdown
   ## 🌐 Demo en Vivo

   - **🚀 API REST**: https://telco-churn-api.onrender.com
   - **📊 Dashboard**: https://telco-churn-dashboard.streamlit.app
   - **📦 Repositorio**: https://github.com/alvaretto/telco-customer-churn-prediction
   ```

✅ **Checkpoint**: README.md actualizado

---

### Paso 3: Commit y push de cambios (1 minuto)

```bash
# Agregar archivos modificados
git add URLS_PRODUCCION.md README.md scripts/ GUIA_DEPLOYMENT_DETALLADA.md

# Commit
git commit -m "docs: Actualizar URLs de producción y agregar guía de deployment"

# Push
git push origin main
```

✅ **Checkpoint**: Cambios pushed a GitHub

---

## 🎉 ¡DEPLOYMENT COMPLETADO!

### 📊 Resumen Final

**URLs de Producción**:
- 🚀 **API**: https://telco-churn-api.onrender.com
- 📊 **Dashboard**: https://telco-churn-dashboard.streamlit.app
- 📦 **GitHub**: https://github.com/alvaretto/telco-customer-churn-prediction

**Tiempo total**: ~40 minutos

**Estado**:
- ✅ API deployada y funcionando
- ✅ Dashboard deployado y funcionando
- ✅ Documentación actualizada
- ✅ Scripts de verificación ejecutados
- ✅ Cambios committed y pushed

---

## 📝 Próximos Pasos Opcionales

1. **Configurar dominio personalizado** (Render + Streamlit)
2. **Agregar Google Analytics** al dashboard
3. **Configurar alertas de uptime** (UptimeRobot)
4. **Agregar CI/CD con GitHub Actions**
5. **Configurar monitoreo con Sentry**

---

## 🐛 Troubleshooting

### API no inicia
- **Problema**: Build failed en Render
- **Solución**:
  1. Verifica logs en Render
  2. Confirma que Git LFS descargó archivos .pkl
  3. Verifica que `PYTHON_VERSION=3.10.13`

### Dashboard no carga modelo
- **Problema**: Error al cargar modelo
- **Solución**:
  1. Verifica logs en Streamlit Cloud
  2. Confirma que archivos .pkl están en `models/`
  3. Reboot app desde Streamlit dashboard

### Deployment muy lento
- **Problema**: Tarda más de 15 minutos
- **Solución**:
  1. Normal en primera vez (descarga Git LFS)
  2. Deployments subsecuentes serán más rápidos
  3. Verifica que no haya errores en logs

---

**¿Necesitas ayuda?** Revisa `DEPLOYMENT_CHECKLIST.md` o `docs/DEPLOYMENT_PASO_A_PASO.md`

**¡Felicitaciones por tu deployment exitoso!** 🎉🚀

