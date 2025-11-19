# 🔐 Configuración de GitHub y Seguridad

## ✅ Estado Actual del Repositorio

### Repositorio Configurado Exitosamente

- **URL**: https://github.com/alvaretto/telco-customer-churn-prediction
- **Rama principal**: `main`
- **Archivos sincronizados**: 7 archivos
- **Primer commit**: Completado exitosamente
- **Push inicial**: ✅ Exitoso

### Archivos en el Repositorio

```
✅ .gitignore                           # Configuración de archivos excluidos
✅ INSTRUCCIONES.md                     # Guía de ejecución
✅ LICENSE                              # Licencia MIT
✅ MEJORAS_REALIZADAS.md                # Documentación de mejoras
✅ README.md                            # Documentación principal
✅ Telco-Customer-Churn.ipynb           # Notebook optimizado
✅ WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
```

---

## 🚨 ACCIÓN URGENTE REQUERIDA: Rotar Token de GitHub

### ⚠️ IMPORTANTE - SEGURIDAD

El token de acceso personal (PAT) utilizado en esta configuración **ha sido expuesto** en esta conversación y debe ser **rotado inmediatamente** por razones de seguridad.

### Pasos para Rotar el Token

#### 1. Revocar el Token Actual

1. Ve a GitHub: https://github.com/settings/tokens
2. Busca el token actual (probablemente llamado algo como "repo-access" o similar)
3. Haz clic en **"Delete"** o **"Revoke"**
4. Confirma la revocación

#### 2. Crear un Nuevo Token

1. En la misma página, haz clic en **"Generate new token"** → **"Generate new token (classic)"**
2. Configura el token:
   - **Note**: `telco-churn-project-token` (o el nombre que prefieras)
   - **Expiration**: 90 días (recomendado) o personalizado
   - **Scopes** (permisos necesarios):
     - ✅ `repo` (acceso completo a repositorios privados)
     - ✅ `workflow` (si usas GitHub Actions)
3. Haz clic en **"Generate token"**
4. **COPIA EL TOKEN INMEDIATAMENTE** (solo se muestra una vez)

#### 3. Actualizar la Configuración Local

```bash
# Navegar al directorio del proyecto
cd /home/bootcamp/Proyectos-2026/Proyectos-Varios/BootCampVirtIA/Semana-05/Defensa-Proyecto

# Remover el remote actual
git remote remove origin

# Agregar el remote con el NUEVO token
git remote add origin https://alvaretto:TU_NUEVO_TOKEN@github.com/alvaretto/telco-customer-churn-prediction.git

# Verificar la configuración
git remote -v
```

#### 4. Verificar que Funciona

```bash
# Hacer un cambio pequeño para probar
echo "# Test" >> test.txt
git add test.txt
git commit -m "Test: Verificar nuevo token"
git push origin main

# Si funciona, eliminar el archivo de prueba
git rm test.txt
git commit -m "Remove test file"
git push origin main
```

---

## 🔒 Mejores Prácticas de Seguridad

### 1. Usar SSH en Lugar de HTTPS (Recomendado)

SSH es más seguro y no requiere tokens en la URL:

```bash
# Generar clave SSH (si no tienes una)
ssh-keygen -t ed25519 -C "alvaretto@users.noreply.github.com"

# Copiar la clave pública
cat ~/.ssh/id_ed25519.pub

# Agregar la clave a GitHub:
# https://github.com/settings/keys → "New SSH key"

# Cambiar el remote a SSH
git remote set-url origin git@github.com:alvaretto/telco-customer-churn-prediction.git

# Verificar
git remote -v
```

### 2. Usar Git Credential Manager

Alternativa para HTTPS sin exponer tokens:

```bash
# Instalar Git Credential Manager (si no está instalado)
# En Arch Linux:
sudo pacman -S git-credential-manager-core

# Configurar
git config --global credential.helper manager-core

# La próxima vez que hagas push, se te pedirá autenticación
# y se guardará de forma segura
```

### 3. Nunca Commitear Tokens o Credenciales

El `.gitignore` ya está configurado para excluir:
- `*.key`
- `*.pem`
- `credentials.json`
- `config.ini`

**Siempre verifica antes de hacer commit:**
```bash
git status
git diff
```

---

## 📝 Configuración Adicional del Repositorio en GitHub

### 1. Configurar Descripción del Repositorio

1. Ve a: https://github.com/alvaretto/telco-customer-churn-prediction
2. Haz clic en el ícono de engranaje (⚙️) junto a "About"
3. Agrega la descripción:

```
Proyecto de Machine Learning para predecir abandono de clientes en telecomunicaciones. 
Incluye EDA, ingeniería de características, SMOTE para desbalanceo de clases y 
comparación de 7 algoritmos de ML con optimización de hiperparámetros.
```

### 2. Agregar Topics/Etiquetas

En la misma sección "About", agrega estos topics:

```
machine-learning
data-science
customer-churn
churn-prediction
python
scikit-learn
xgboost
smote
imbalanced-data
feature-engineering
random-forest
telecommunications
jupyter-notebook
data-analysis
predictive-analytics
```

### 3. Configurar GitHub Pages (Opcional)

Si quieres publicar el notebook como página web:

1. Ve a Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / `root`
4. Save

---

## 🔄 Comandos Útiles para Sincronización

### Flujo de Trabajo Diario

```bash
# 1. Verificar estado
git status

# 2. Agregar cambios
git add .

# 3. Commit con mensaje descriptivo
git commit -m "Descripción de los cambios"

# 4. Push al repositorio remoto
git push origin main

# 5. Pull para obtener cambios remotos (si trabajas desde múltiples lugares)
git pull origin main
```

### Comandos de Verificación

```bash
# Ver historial de commits
git log --oneline -10

# Ver archivos rastreados
git ls-files

# Ver configuración del remote
git remote -v

# Ver ramas
git branch -a

# Ver diferencias antes de commit
git diff
```

---

## 📊 Próximos Pasos

1. ✅ **Rotar el token de GitHub** (URGENTE)
2. ✅ **Configurar descripción y topics** en GitHub
3. ⚪ Considerar migrar a SSH para mayor seguridad
4. ⚪ Configurar GitHub Pages si deseas publicar el proyecto
5. ⚪ Agregar badges adicionales al README (build status, etc.)
6. ⚪ Considerar agregar GitHub Actions para CI/CD

---

## 🆘 Solución de Problemas

### Error: "Authentication failed"
- Verifica que el token no haya expirado
- Asegúrate de que el token tenga los permisos correctos (`repo`)
- Rota el token y actualiza la configuración

### Error: "Permission denied"
- Verifica que seas el propietario del repositorio
- Confirma que el token tenga permisos de escritura

### Error: "Remote already exists"
```bash
git remote remove origin
git remote add origin URL_CORRECTA
```

---

**Fecha de configuración**: 18 de Noviembre de 2025  
**Estado**: ✅ Repositorio configurado y sincronizado exitosamente

