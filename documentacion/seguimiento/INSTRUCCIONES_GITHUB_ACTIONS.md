# 📋 Instrucciones para Agregar GitHub Actions Workflows

## ⚠️ Problema Detectado

El push de los workflows de GitHub Actions fue rechazado porque el **Personal Access Token (PAT)** actual no tiene el scope `workflow` necesario.

---

## ✅ Solución: Agregar Workflows Manualmente en GitHub

### Opción 1: Actualizar el Personal Access Token (Recomendado para el futuro)

1. Ve a GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Haz clic en **Generate new token** → **Generate new token (classic)**
3. Configura el token:
   - **Note**: `Telco Churn Project - Full Access`
   - **Expiration**: 90 días (o el período que prefieras)
   - **Scopes**: Selecciona los siguientes:
     - ✅ `repo` (Full control of private repositories)
     - ✅ `workflow` (Update GitHub Action workflows) ← **IMPORTANTE**
     - ✅ `write:packages` (si usas GitHub Packages)
4. Haz clic en **Generate token**
5. **Copia el token** (solo se muestra una vez)
6. Actualiza el token en tu configuración local:
   ```bash
   git remote set-url origin https://alvaretto:NUEVO_TOKEN@github.com/alvaretto/telco-customer-churn-prediction.git
   ```

### Opción 2: Crear los Workflows Manualmente en GitHub (Solución Inmediata)

#### Paso 1: Crear el directorio de workflows

1. Ve a tu repositorio en GitHub: https://github.com/alvaretto/telco-customer-churn-prediction
2. Haz clic en **Add file** → **Create new file**
3. En el campo de nombre, escribe: `.github/workflows/ci.yml`
4. GitHub creará automáticamente los directorios `.github/workflows/`

#### Paso 2: Agregar el contenido de `ci.yml`

Copia y pega el siguiente contenido en el archivo:

```yaml
# Contenido del archivo: .github/workflows/ci.yml
# (Ver el archivo local en tu proyecto para copiar el contenido completo)
```

**Ubicación del archivo local**: `.github/workflows/ci.yml`

#### Paso 3: Crear el segundo workflow `deploy.yml`

1. Haz clic en **Add file** → **Create new file**
2. En el campo de nombre, escribe: `.github/workflows/deploy.yml`
3. Copia y pega el contenido del archivo local `.github/workflows/deploy.yml`

#### Paso 4: Commit los cambios

1. Scroll hacia abajo
2. En **Commit new file**:
   - **Commit message**: `ci: agregar workflows de GitHub Actions para CI/CD`
   - **Description**: `Agregar pipelines de CI/CD y deployment automático`
3. Selecciona **Commit directly to the main branch**
4. Haz clic en **Commit new file**

---

## 📁 Archivos de Workflows Disponibles Localmente

Los archivos de workflows están disponibles en tu proyecto local:

1. **`.github/workflows/ci.yml`** - Pipeline de CI/CD completo
   - Ejecuta tests unitarios
   - Verifica calidad de código (flake8, black, isort)
   - Monitorea producción
   - Escaneo de seguridad con Trivy

2. **`.github/workflows/deploy.yml`** - Pipeline de deployment
   - Notifica deployments
   - Verifica API y Dashboard
   - Genera resumen de deployment

---

## 🔄 Sincronizar Cambios Después de Agregar Workflows en GitHub

Después de crear los workflows manualmente en GitHub, sincroniza tu repositorio local:

```bash
# Descargar los cambios del remoto
git pull origin main

# Verificar que los workflows están presentes
ls -la .github/workflows/

# Deberías ver:
# ci.yml
# deploy.yml
```

---

## 🎯 Verificar que GitHub Actions Funciona

1. Ve a tu repositorio en GitHub
2. Haz clic en la pestaña **Actions**
3. Deberías ver los workflows:
   - **CI/CD Pipeline**
   - **Deployment Verification**
4. Los workflows se ejecutarán automáticamente en el próximo push a `main`

---

## 📊 Estado Actual del Push

✅ **Push exitoso** del commit `4844dd7`:
- ✅ Scripts de monitoreo y validación
- ✅ Documentación actualizada (TESTING.md, URL_REFERENCE.md)
- ✅ Mejoras UX/UI completas (dashboard mejorado)
- ✅ Badges de estado en README
- ✅ URLs corregidas en toda la documentación

⏳ **Pendiente**:
- Los workflows de GitHub Actions (`.github/workflows/*.yml`)
- Se pueden agregar manualmente siguiendo las instrucciones anteriores

---

## 🚀 Próximos Pasos

1. **Opción A**: Actualizar el PAT con scope `workflow` y hacer push de los workflows
2. **Opción B**: Crear los workflows manualmente en GitHub (más rápido)
3. **Verificar Streamlit Cloud**: El dashboard se redesplegará automáticamente con las mejoras UX/UI
4. **Revisar el README**: Los nuevos badges ya están visibles en GitHub

---

## 📞 Soporte

Si tienes problemas:
1. Revisa la documentación de GitHub Actions: https://docs.github.com/en/actions
2. Verifica los permisos del PAT: https://github.com/settings/tokens
3. Consulta el archivo `RESUMEN_TRABAJO_COMPLETADO.md` para más detalles

---

**Fecha**: 2025-11-21  
**Commit exitoso**: `4844dd7`  
**Estado**: ✅ Push completado (excepto workflows)

