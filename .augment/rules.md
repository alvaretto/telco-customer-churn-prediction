# Reglas del Proyecto: Telco Customer Churn Prediction

## 🚫 Restricciones de Ejecución

### **NUNCA ejecutar notebooks localmente**

- ❌ **NO ejecutar** `Telco_Customer_Churn.ipynb` en el entorno local
- ❌ **NO usar** comandos como `jupyter nbconvert --execute`
- ❌ **NO intentar** ejecutar celdas del notebook con Python local

**Razón:** El proyecto requiere infraestructura de Machine Learning avanzada que **NO está disponible localmente**.

### ✅ Entorno de Ejecución Correcto

- ✅ **Google Colab ÚNICAMENTE**
- ✅ El notebook está diseñado para ejecutarse en Google Colab
- ✅ Incluye detección automática de entorno (`IN_COLAB`)

---

## 📝 Modificaciones Permitidas

### ✅ Operaciones Seguras en Local

1. **Edición del notebook:**
   - ✅ Modificar celdas de código
   - ✅ Agregar nuevas secciones
   - ✅ Actualizar markdown
   - ✅ Cambiar configuraciones

2. **Análisis estático:**
   - ✅ Leer el contenido del notebook
   - ✅ Buscar patrones en el código
   - ✅ Validar estructura JSON

3. **Gestión de archivos:**
   - ✅ Modificar `config.json`
   - ✅ Actualizar `models/metadata.json`
   - ✅ Crear documentación (`.md`)

### ❌ Operaciones Prohibidas en Local

1. **Ejecución:**
   - ❌ Ejecutar el notebook completo
   - ❌ Ejecutar celdas individuales
   - ❌ Entrenar modelos
   - ❌ Cargar modelos guardados (requieren dependencias de Colab)

2. **Instalación de dependencias ML:**
   - ❌ Instalar librerías pesadas de ML localmente
   - ❌ Configurar entornos de ML complejos

---

## 🎯 Flujo de Trabajo Recomendado

### Para Modificaciones del Notebook:

1. **Editar localmente** (usando herramientas de edición)
2. **Subir a Google Colab**
3. **Ejecutar en Colab**
4. **Descargar resultados** (si es necesario)

### Para Validación de Cambios:

1. **Validación estática local** (sintaxis, estructura)
2. **Ejecución en Google Colab** (validación funcional)
3. **Revisión de resultados**

---

## 📋 Recordatorios

- 🔴 **CRÍTICO:** Nunca sugerir ejecutar el notebook localmente
- 🟡 **IMPORTANTE:** Siempre mencionar que la ejecución es en Google Colab
- 🟢 **RECOMENDADO:** Validar cambios estáticamente antes de subir a Colab

---

## 🔧 Herramientas Locales Permitidas

- ✅ Editores de texto/código
- ✅ Git (control de versiones)
- ✅ Validadores JSON
- ✅ Linters de Python (para análisis estático)
- ✅ Herramientas de documentación

---

## 📚 Documentación

Para más información sobre la validación de robustez implementada, consultar:
- `CAMBIOS_VALIDACION_ROBUSTEZ.md`
- `semilla-aleatoria-RANDOM_STATE.md` (en `/home/bootcamp/Escritorio/Expo IA/Nuevos PDFs/`)

