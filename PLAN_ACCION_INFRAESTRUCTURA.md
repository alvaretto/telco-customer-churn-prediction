# 🎯 PLAN DE ACCIÓN AJUSTADO A INFRAESTRUCTURA LIMITADA

## 📊 ANÁLISIS DE TU SITUACIÓN

### ✅ Lo que TIENES:
- **RAM local**: 39 GB (¡EXCELENTE!)
- **Modelo entrenado**: En Colab, serializado, descargado
- **Archivos del modelo**: En `models/` (65 MB)
- **Estructura completa**: API + Dashboard + Tests + Docs
- **Git LFS**: Configurado y funcionando
- **GitHub**: Todo pushed correctamente

### ⚠️ PROBLEMA DETECTADO:
- **Python 3.13.7** local es **demasiado nuevo**
- **scikit-learn 1.3.2** no compila en Python 3.13
- Necesitas Python 3.10 o 3.11 para compatibilidad

---

## 💡 RESPUESTAS A TUS PREGUNTAS

### 1. ¿Puedo probar API y Dashboard localmente?

**✅ SÍ, pero necesitas Python 3.10 o 3.11**

**Opción A: Usar Docker (RECOMENDADO)**
```bash
# La API ya tiene Dockerfile
cd api
docker build -t churn-api .
docker run -p 5000:5000 churn-api

# Acceder a: http://localhost:5000
```

**Opción B: Instalar Python 3.10 con pyenv**
```bash
# Instalar pyenv
curl https://pyenv.run | bash

# Instalar Python 3.10
pyenv install 3.10.13
pyenv local 3.10.13

# Crear venv con Python 3.10
python -m venv venv
source venv/bin/activate
pip install -r api/requirements.txt
```

**Opción C: Ir directo a deployment en cloud** ⭐ **MÁS FÁCIL**
- Render y Streamlit Cloud usan Python 3.10 por defecto
- No necesitas configurar nada localmente
- Deploy en 10-15 minutos

### 2. ¿Los tests se pueden ejecutar localmente?

**Respuesta**: Misma situación que la API

- **Con Python 3.10/3.11**: ✅ Sí, sin problemas
- **Con Python 3.13**: ❌ No, incompatibilidad
- **En cloud (GitHub Actions)**: ✅ Sí, configurando Python 3.10

**Requisitos de recursos para tests**:
- RAM: < 1 GB
- CPU: Mínimo
- Tiempo: 10-30 segundos

Los tests son **muy ligeros**, solo cargan el modelo y hacen predicciones de prueba.

### 3. ¿Debería ir directo a deployment en cloud?

**✅ SÍ, ES LA MEJOR OPCIÓN EN TU CASO**

**Ventajas**:
- ✅ No necesitas configurar Python 3.10 localmente
- ✅ Render/Streamlit Cloud usan Python 3.10 por defecto
- ✅ Deployment en 10-15 minutos
- ✅ Puedes probar todo en producción directamente
- ✅ Git LFS ya está configurado
- ✅ Gratis para proyectos pequeños

**Desventajas**:
- ⚠️ Primer deploy puede tardar 5-10 minutos
- ⚠️ Si hay errores, toma más tiempo debuggear
- ⚠️ Render Free tier se duerme después de 15 min de inactividad

**Recomendación**: **Deploy directo a cloud** ⭐

### 4. Workflow recomendado

**WORKFLOW ÓPTIMO PARA TU CASO:**

```
┌─────────────────────────────────────────────────────────┐
│  FASE 1: ENTRENAMIENTO (Google Colab)                  │
├─────────────────────────────────────────────────────────┤
│  1. Entrenar modelo en Colab (GPU gratis)              │
│  2. Serializar modelo (joblib)                         │
│  3. Guardar en Google Drive                            │
│  4. Descargar a local                                  │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  FASE 2: VERSIONADO (Local + GitHub)                   │
├─────────────────────────────────────────────────────────┤
│  1. Mover modelos a models/                            │
│  2. Configurar Git LFS                                 │
│  3. Commit y push a GitHub                             │
│  4. Crear estructura de deployment                     │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  FASE 3: DEPLOYMENT (Cloud - Sin setup local)          │
├─────────────────────────────────────────────────────────┤
│  API:                                                   │
│  1. Render.com → Conectar GitHub                       │
│  2. Configurar build/start commands                    │
│  3. Deploy automático                                  │
│                                                         │
│  Dashboard:                                             │
│  1. Streamlit Cloud → Conectar GitHub                  │
│  2. Seleccionar dashboard/app.py                       │
│  3. Deploy automático                                  │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  FASE 4: TESTING (Cloud o Local con Python 3.10)       │
├─────────────────────────────────────────────────────────┤
│  Opción A: Probar en producción directamente           │
│  Opción B: GitHub Actions con Python 3.10              │
│  Opción C: Local con Docker                            │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  FASE 5: ITERACIÓN (Colab → GitHub → Cloud)            │
├─────────────────────────────────────────────────────────┤
│  1. Reentrenar en Colab (si es necesario)              │
│  2. Actualizar modelos en GitHub                       │
│  3. Render/Streamlit auto-redeploy                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 PLAN DE ACCIÓN INMEDIATO

### OPCIÓN 1: Deploy Directo a Cloud (RECOMENDADO) ⭐

**Tiempo estimado**: 20-30 minutos

#### Paso 1: Deploy API en Render (10-15 min)

1. **Ir a [render.com](https://render.com)**
2. **Sign up / Login** (gratis)
3. **New → Web Service**
4. **Connect GitHub** → Seleccionar tu repo
5. **Configurar**:
   ```
   Name: telco-churn-api
   Region: Oregon (US West)
   Branch: main
   Root Directory: api
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60 app:app
   Instance Type: Free
   ```
6. **Environment Variables**:
   ```
   PYTHON_VERSION=3.10.0
   ```
7. **Create Web Service**
8. **Esperar 5-10 minutos** (primera vez)
9. **Verificar**: `https://your-app.onrender.com/health`

#### Paso 2: Deploy Dashboard en Streamlit Cloud (5-10 min)

1. **Ir a [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with GitHub**
3. **New app**
4. **Configurar**:
   ```
   Repository: alvaretto/telco-customer-churn-prediction
   Branch: main
   Main file path: dashboard/app.py
   App URL: telco-churn-dashboard (o el que prefieras)
   ```
5. **Deploy!**
6. **Esperar 3-5 minutos**
7. **Verificar**: `https://telco-churn-dashboard.streamlit.app`

#### Paso 3: Probar en Producción (5 min)

```bash
# Test API
curl https://your-app.onrender.com/health
curl https://your-app.onrender.com/model_info

# Test Dashboard
# Abrir en navegador y probar Risk Analysis
```

---

### OPCIÓN 2: Probar Localmente con Docker (Alternativa)

**Tiempo estimado**: 15-20 minutos

#### Requisitos:
- Docker instalado

#### Pasos:

```bash
# 1. Build API
cd api
docker build -t churn-api .

# 2. Run API
docker run -p 5000:5000 churn-api

# 3. Test
curl http://localhost:5000/health

# 4. Dashboard (sin Docker, requiere Python 3.10)
# Mejor deployar directo a Streamlit Cloud
```

---

### OPCIÓN 3: Setup Local con Python 3.10 (Más complejo)

**Tiempo estimado**: 30-45 minutos

Solo si realmente necesitas probar localmente y no quieres usar Docker.

```bash
# 1. Instalar pyenv
curl https://pyenv.run | bash

# 2. Configurar shell (agregar a ~/.zshrc)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 3. Reiniciar shell
exec $SHELL

# 4. Instalar Python 3.10
pyenv install 3.10.13

# 5. Usar Python 3.10 en el proyecto
cd /path/to/proyecto
pyenv local 3.10.13

# 6. Crear venv
python -m venv venv
source venv/bin/activate

# 7. Instalar dependencias
pip install -r api/requirements.txt

# 8. Ejecutar API
cd api
python app.py
```

---

## 📋 COMPARACIÓN DE OPCIONES

| Opción | Tiempo | Dificultad | Ventajas | Desventajas |
|--------|--------|------------|----------|-------------|
| **Deploy Cloud** ⭐ | 20-30 min | Fácil | No requiere setup local, URL pública, gratis | Primer deploy lento |
| **Docker Local** | 15-20 min | Media | Rápido para probar, aislado | Requiere Docker |
| **Python 3.10 Local** | 30-45 min | Difícil | Control total | Complejo, requiere pyenv |

---

## 🎯 MI RECOMENDACIÓN FINAL

### Para ti, la mejor opción es:

**🚀 DEPLOY DIRECTO A CLOUD (Opción 1)**

**Razones**:
1. ✅ Ya tienes todo en GitHub con Git LFS
2. ✅ No necesitas configurar Python 3.10 localmente
3. ✅ Render y Streamlit Cloud son gratuitos
4. ✅ Obtienes URLs públicas para demostrar
5. ✅ Auto-deploy cuando haces push
6. ✅ Menos tiempo de setup (20-30 min vs 45+ min)

**Próximos pasos inmediatos**:
1. Deploy API en Render (10-15 min)
2. Deploy Dashboard en Streamlit Cloud (5-10 min)
3. Probar ambos en producción (5 min)
4. Si todo funciona, ¡listo para presentar!
5. Si hay errores, debuggear viendo logs en Render/Streamlit

---

## 📚 RECURSOS ÚTILES

- **Render Docs**: https://render.com/docs/deploy-flask
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Git LFS**: https://git-lfs.github.com
- **Troubleshooting**: Ver `docs/DEPLOYMENT.md` en tu proyecto

---

## ❓ PREGUNTAS FRECUENTES

**P: ¿Necesito pagar algo?**
R: No, Render Free y Streamlit Cloud Free son suficientes.

**P: ¿Qué pasa si el modelo es muy grande?**
R: 65 MB está bien. Render Free soporta hasta 512 MB RAM.

**P: ¿Puedo actualizar el modelo después?**
R: Sí, solo actualiza los archivos en GitHub y Render/Streamlit auto-redeploy.

**P: ¿Cómo debuggeo errores en producción?**
R: Render y Streamlit tienen logs en tiempo real en su dashboard.

**P: ¿Necesito Docker para deployar?**
R: No, Render y Streamlit Cloud manejan todo automáticamente.

---

## ✅ CHECKLIST ANTES DE DEPLOYAR

- [x] Modelo entrenado y serializado
- [x] Archivos en `models/` (churn_model.pkl, preprocessor.pkl, metadata.json)
- [x] Git LFS configurado
- [x] Estructura completa creada (API + Dashboard + Tests + Docs)
- [x] Todo pushed a GitHub
- [ ] Cuenta en Render.com
- [ ] Cuenta en Streamlit Cloud (con GitHub)
- [ ] Leer `docs/DEPLOYMENT.md`

---

**¿Listo para deployar? ¡Vamos!** 🚀

