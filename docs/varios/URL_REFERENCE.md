# 🔗 Referencia de URLs - Telco Customer Churn Prediction

## 📋 URLs de Producción (ACTUALIZADAS)

### ✅ URLs Correctas y Verificadas

| Servicio | URL | Estado |
|----------|-----|--------|
| **API REST** | `https://telco-churn-api-y9xy.onrender.com` | ✅ Online |
| **Dashboard** | `https://telco-churn-dashboard-ml.streamlit.app` | ✅ Online |
| **Repositorio GitHub** | `https://github.com/alvaretto/telco-customer-churn-prediction` | ✅ Activo |

### 🔍 Endpoints de la API

| Endpoint | URL Completa | Método | Descripción |
|----------|--------------|--------|-------------|
| Home | `https://telco-churn-api-y9xy.onrender.com/` | GET | Información de la API |
| Health Check | `https://telco-churn-api-y9xy.onrender.com/health` | GET | Estado de salud |
| Model Info | `https://telco-churn-api-y9xy.onrender.com/model_info` | GET | Información del modelo |
| Predict | `https://telco-churn-api-y9xy.onrender.com/predict` | POST | Predicción individual |
| Predict Batch | `https://telco-churn-api-y9xy.onrender.com/predict_batch` | POST | Predicciones en lote |

---

## ⚠️ URLs Obsoletas (NO USAR)

Las siguientes URLs aparecen en documentación antigua pero **NO son correctas**:

| URL Obsoleta | Razón | Reemplazar por |
|--------------|-------|----------------|
| `https://telco-churn-api.onrender.com` | URL genérica, no es la real | `https://telco-churn-api-y9xy.onrender.com` |
| `https://telco-churn-dashboard.streamlit.app` | URL genérica, no es la real | `https://telco-churn-dashboard-ml.streamlit.app` |

---

## 📝 Archivos que Contienen URLs

### Archivos con URLs Correctas ✅

- `README.md` - URLs actualizadas
- `URLS_PRODUCCION.md` - Documento oficial de URLs
- `DEPLOYMENT_CHECKLIST.md` - URLs verificadas
- `seguimiento-estructura-completa.md` - URLs correctas
- `scripts/monitor_production.py` - URLs correctas
- `scripts/validate_deployment.py` - URLs correctas
- `.github/workflows/deploy.yml` - URLs correctas

### Archivos con URLs Obsoletas ⚠️

Los siguientes archivos contienen URLs genéricas que deben actualizarse:

1. **`PLAN_ACCION_INFRAESTRUCTURA.md`**
   - Línea 7: `https://telco-churn-dashboard.streamlit.app`
   - **Acción**: Actualizar a `https://telco-churn-dashboard-ml.streamlit.app`

2. **`bu/deploy/03-deploy.md`**
   - Múltiples referencias a URLs genéricas
   - **Acción**: Actualizar todas las referencias

3. **`GUIA_DEPLOYMENT_DETALLADA.md`**
   - Múltiples referencias a URLs genéricas
   - **Acción**: Actualizar todas las referencias

---

## 🔧 Cómo Verificar URLs

### Método 1: Script de Monitoreo

```bash
python scripts/monitor_production.py
```

### Método 2: Script de Validación

```bash
python scripts/validate_deployment.py
```

### Método 3: Curl Manual

```bash
# Verificar API
curl https://telco-churn-api-y9xy.onrender.com/health

# Verificar Dashboard
curl -I https://telco-churn-dashboard-ml.streamlit.app
```

---

## 📊 Historial de URLs

### Versión Actual (2025-11-21)

- **API**: `https://telco-churn-api-y9xy.onrender.com`
- **Dashboard**: `https://telco-churn-dashboard-ml.streamlit.app`
- **Deployment**: 2025-11-20 (API), 2025-11-21 (Dashboard)

### Notas

- Las URLs de Render incluyen un sufijo único (`-y9xy`) generado automáticamente
- Las URLs de Streamlit Cloud incluyen el nombre de la app (`-ml`)
- Ambas URLs son permanentes mientras los servicios estén activos

---

## 🚀 Acciones Recomendadas

### Para Desarrolladores

1. **Siempre usar las URLs de este documento** como referencia
2. **Verificar URLs antes de actualizar documentación**
3. **Ejecutar scripts de validación** después de cambios

### Para Actualizar Documentación

```bash
# Buscar URLs obsoletas
grep -r "telco-churn-api.onrender.com" --include="*.md" .
grep -r "telco-churn-dashboard.streamlit.app" --include="*.md" .

# Reemplazar con URLs correctas
# Usar editor de texto o sed para actualizar
```

---

## 📚 Referencias

- **Render Dashboard**: https://dashboard.render.com
- **Streamlit Cloud**: https://share.streamlit.io
- **GitHub Repository**: https://github.com/alvaretto/telco-customer-churn-prediction

---

**Última actualización:** 2025-11-21  
**Mantenido por:** Álvaro Ángel Molina (@alvaretto)  
**Verificación:** Ejecutar `python scripts/monitor_production.py` para verificar estado actual

