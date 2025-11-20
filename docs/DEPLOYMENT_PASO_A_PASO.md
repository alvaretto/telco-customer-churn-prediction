# 🚀 DEPLOYMENT PASO A PASO - RENDER + STREAMLIT CLOUD

## 📋 PREREQUISITOS

- [x] Cuenta de GitHub (ya tienes)
- [x] Repositorio pushed a GitHub (ya tienes)
- [x] Git LFS configurado (ya tienes)
- [ ] Cuenta en Render.com (crear gratis)
- [ ] Cuenta en Streamlit Cloud (usar GitHub para login)

---

## PARTE 1: DEPLOY API EN RENDER (10-15 minutos)

### Paso 1: Crear cuenta en Render

1. Ir a **https://render.com**
2. Click en **"Get Started"**
3. **Sign up with GitHub** (recomendado)
4. Autorizar Render a acceder a tus repos

### Paso 2: Crear Web Service

1. En el dashboard de Render, click **"New +"** → **"Web Service"**
2. Click **"Connect a repository"**
3. Si no ves tu repo:
   - Click **"Configure account"**
   - Seleccionar **"All repositories"** o solo tu repo
   - Click **"Save"**
4. Buscar y seleccionar: **`telco-customer-churn-prediction`**
5. Click **"Connect"**

### Paso 3: Configurar el servicio

**Configuración básica:**
```
Name: telco-churn-api
Region: Oregon (US West) o el más cercano
Branch: main
Root Directory: api
Runtime: Python 3
```

**Build & Deploy:**
```
Build Command: pip install -r requirements.txt
Start Command: gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app
```

**Instance Type:**
```
Free
```

### Paso 4: Variables de entorno (IMPORTANTE)

Click en **"Advanced"** → **"Add Environment Variable"**

Agregar:
```
Key: PYTHON_VERSION
Value: 3.10.0
```

### Paso 5: Deploy

1. Click **"Create Web Service"**
2. Render comenzará a:
   - Clonar tu repo
   - Descargar archivos de Git LFS (modelo de 65 MB)
   - Instalar dependencias
   - Iniciar la aplicación
3. **Esperar 5-10 minutos** (primera vez es más lento)
4. Ver logs en tiempo real en la página

### Paso 6: Verificar deployment

Una vez que veas **"Your service is live 🎉"**:

1. Copiar la URL (algo como: `https://telco-churn-api.onrender.com`)
2. Probar endpoints:

```bash
# Health check
curl https://telco-churn-api.onrender.com/health

# Model info
curl https://telco-churn-api.onrender.com/model_info

# Prediction (ejemplo)
curl -X POST https://telco-churn-api.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 844.2,
    "tenure_group": "6-12 months",
    "TotalServices": 1,
    "AvgChargePerService": 70.35,
    "ChargeToTenureRatio": 5.86,
    "HasMultipleServices": 0,
    "HasStreamingServices": 0
  }'
```

### Paso 7: Guardar URL

Guardar la URL de tu API para usarla en el Dashboard.

---

## PARTE 2: DEPLOY DASHBOARD EN STREAMLIT CLOUD (5-10 minutos)

### Paso 1: Ir a Streamlit Cloud

1. Ir a **https://share.streamlit.io**
2. Click **"Sign in"**
3. **Continue with GitHub**
4. Autorizar Streamlit

### Paso 2: Crear nueva app

1. Click **"New app"**
2. Configurar:

```
Repository: alvaretto/telco-customer-churn-prediction
Branch: main
Main file path: dashboard/app.py
App URL (custom): telco-churn-dashboard (o el que prefieras)
```

3. Click **"Advanced settings"** (opcional):

```
Python version: 3.10
```

### Paso 3: Deploy

1. Click **"Deploy!"**
2. Streamlit comenzará a:
   - Clonar tu repo
   - Descargar archivos de Git LFS
   - Instalar dependencias de `dashboard/requirements.txt`
   - Ejecutar `dashboard/app.py`
3. **Esperar 3-5 minutos**
4. Ver logs en tiempo real

### Paso 4: Verificar dashboard

Una vez que veas la app corriendo:

1. Explorar las páginas:
   - 🏠 Home
   - 📊 Overview
   - 🎯 Risk Analysis (probar predicción)
   - 📈 Model Metrics
   - 💰 ROI Simulator
   - 🔍 Model Monitoring

2. Probar predicción en **Risk Analysis**:
   - Llenar formulario
   - Click "Predict Churn Risk"
   - Ver resultado

### Paso 5: Configurar API URL (si es necesario)

Si el dashboard necesita conectarse a la API:

1. En Streamlit Cloud, ir a **"Settings"** → **"Secrets"**
2. Agregar:

```toml
[api]
url = "https://telco-churn-api.onrender.com"
```

3. Guardar y redeploy

---

## PARTE 3: VERIFICACIÓN FINAL (5 minutos)

### Checklist de verificación:

- [ ] API responde en `/health`
- [ ] API responde en `/model_info`
- [ ] API puede hacer predicciones en `/predict`
- [ ] Dashboard carga correctamente
- [ ] Dashboard puede hacer predicciones
- [ ] Todas las páginas del dashboard funcionan
- [ ] Métricas del modelo se muestran correctamente

### URLs finales:

```
API: https://telco-churn-api.onrender.com
Dashboard: https://telco-churn-dashboard.streamlit.app
GitHub: https://github.com/alvaretto/telco-customer-churn-prediction
```

---

## 🐛 TROUBLESHOOTING

### Problema: "Build failed" en Render

**Solución**:
1. Ver logs completos
2. Verificar que `api/requirements.txt` existe
3. Verificar que `PYTHON_VERSION=3.10.0` está configurado
4. Verificar que Git LFS está funcionando (archivos .pkl deben descargarse)

### Problema: "Application error" en Render

**Solución**:
1. Ver logs de runtime
2. Verificar que el modelo se cargó correctamente
3. Verificar que el puerto está configurado correctamente (`$PORT`)

### Problema: "ModuleNotFoundError" en Streamlit

**Solución**:
1. Verificar que `dashboard/requirements.txt` tiene todas las dependencias
2. Verificar que la ruta del archivo es `dashboard/app.py`
3. Redeploy

### Problema: "Model not found" en Dashboard

**Solución**:
1. Verificar que Git LFS está configurado
2. Verificar que los archivos `.pkl` están en `models/`
3. Verificar rutas relativas en el código

---

## 📊 MONITOREO

### Render:
- **Logs**: Dashboard → Logs (tiempo real)
- **Metrics**: Dashboard → Metrics (CPU, RAM, requests)
- **Restart**: Dashboard → Manual Deploy → "Clear build cache & deploy"

### Streamlit Cloud:
- **Logs**: App → Manage app → Logs
- **Reboot**: App → Manage app → Reboot app
- **Redeploy**: Push a GitHub → auto-redeploy

---

## 🔄 ACTUALIZAR MODELO

Cuando reentrenar el modelo en Colab:

1. **En Colab**: Entrenar y serializar nuevo modelo
2. **Local**: Descargar y reemplazar archivos en `models/`
3. **Git**:
   ```bash
   git add models/
   git commit -m "feat: Actualizar modelo v2"
   git push origin main
   ```
4. **Render**: Auto-redeploy (o manual)
5. **Streamlit**: Auto-redeploy

---

## ✅ ¡LISTO!

Tu proyecto está deployado y accesible públicamente. Puedes:
- Compartir las URLs
- Demostrar el proyecto
- Presentar en el bootcamp
- Agregar al portfolio

**Próximos pasos opcionales**:
- Configurar dominio custom
- Agregar autenticación
- Implementar CI/CD con GitHub Actions
- Agregar monitoreo con Sentry
- Escalar a plan pago si es necesario

