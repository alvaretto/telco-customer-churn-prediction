#!/bin/bash

# Script para actualizar URLs de producción en la documentación
# Uso: ./scripts/update_production_urls.sh <API_URL> <DASHBOARD_URL>

set -e

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "=========================================="
echo "📝 ACTUALIZACIÓN DE URLs DE PRODUCCIÓN"
echo "=========================================="
echo ""

# Verificar argumentos
if [ -z "$1" ] || [ -z "$2" ]; then
    echo -e "${RED}❌ Error: Debes proporcionar ambas URLs${NC}"
    echo "Uso: $0 <API_URL> <DASHBOARD_URL>"
    echo "Ejemplo: $0 https://telco-churn-api.onrender.com https://telco-churn-dashboard.streamlit.app"
    exit 1
fi

API_URL="$1"
DASHBOARD_URL="$2"
GITHUB_URL="https://github.com/alvaretto/telco-customer-churn-prediction"

echo "📍 API URL: $API_URL"
echo "📍 Dashboard URL: $DASHBOARD_URL"
echo "📍 GitHub URL: $GITHUB_URL"
echo ""

# Actualizar URLS_PRODUCCION.md
echo "1/3: Actualizando URLS_PRODUCCION.md..."
cat > URLS_PRODUCCION.md << EOF
# 🌐 URLs DE PRODUCCIÓN - TELCO CHURN PREDICTION

**Fecha de deployment**: $(date +"%Y-%m-%d")  
**Última actualización**: $(date +"%Y-%m-%d %H:%M:%S")

---

## 🔗 URLs ACTIVAS

### 🚀 API REST (Render.com)
**URL**: $API_URL

**Endpoints disponibles:**
- \`GET /\` - Información de la API
- \`GET /health\` - Health check
- \`GET /model_info\` - Información del modelo y métricas
- \`POST /predict\` - Predicción individual
- \`POST /predict_batch\` - Predicciones en lote

**Ejemplos de uso:**
\`\`\`bash
# Health check
curl $API_URL/health

# Model info
curl $API_URL/model_info

# Predicción
curl -X POST $API_URL/predict \\
  -H "Content-Type: application/json" \\
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
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 844.2
  }'
\`\`\`

---

### 📊 DASHBOARD (Streamlit Cloud)
**URL**: $DASHBOARD_URL

**Páginas disponibles:**
- 🏠 **Home** - Overview del proyecto
- 📊 **Overview** - Estadísticas generales
- 🎯 **Risk Analysis** - Predicción individual interactiva
- 📈 **Model Metrics** - Métricas del modelo
- 💰 **ROI Simulator** - Simulador de retorno de inversión
- 🔍 **Model Monitoring** - Monitoreo del modelo

---

### 📦 REPOSITORIO (GitHub)
**URL**: $GITHUB_URL

**Información:**
- Branch principal: \`main\`
- Git LFS: Habilitado (modelo 65 MB)
- CI/CD: Auto-deploy en Render y Streamlit

---

## 📊 MÉTRICAS DEL MODELO

- **Tipo**: RandomForestClassifier
- **ROC-AUC**: 0.87
- **Recall**: 0.83
- **Precision**: 0.72
- **F1-Score**: 0.77
- **Features**: 25 características
- **Tamaño del modelo**: 65 MB

---

## 🔧 INFORMACIÓN TÉCNICA

### Stack Tecnológico
- **Backend**: Flask 3.0.0 + Gunicorn 21.2.0
- **Frontend**: Streamlit 1.29.0
- **ML**: scikit-learn 1.3.2
- **Python**: 3.10.13
- **Deployment**: Render.com (API) + Streamlit Cloud (Dashboard)

### Recursos
- **API RAM**: ~200-300 MB
- **Dashboard RAM**: ~400-500 MB
- **Tiempo de respuesta**: <500ms

---

## 📝 NOTAS

- Render Free tier se duerme después de 15 min sin actividad
- Primera request después de dormir tarda ~30 segundos
- Streamlit Cloud Free: máximo 3 apps, 1 GB RAM por app
- Auto-deploy habilitado: cada push a \`main\` redeploya automáticamente

---

*Última actualización: $(date +"%Y-%m-%d %H:%M:%S")*
EOF

echo -e "${GREEN}✅ URLS_PRODUCCION.md actualizado${NC}"
echo ""

# Crear badge para README
echo "2/3: Generando badges para README.md..."
echo ""
echo -e "${BLUE}Agrega estos badges a tu README.md:${NC}"
echo ""
echo "[![API Status](https://img.shields.io/badge/API-Live-success)]($API_URL)"
echo "[![Dashboard](https://img.shields.io/badge/Dashboard-Live-success)]($DASHBOARD_URL)"
echo "[![Python](https://img.shields.io/badge/Python-3.10.13-blue)](https://www.python.org/)"
echo "[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)"
echo ""

# Resumen
echo "3/3: Resumen de actualización..."
echo ""
echo -e "${GREEN}✅ URLs actualizadas exitosamente${NC}"
echo ""
echo "📝 Archivos actualizados:"
echo "   • URLS_PRODUCCION.md"
echo ""
echo "📝 Próximos pasos manuales:"
echo "   1. Actualiza README.md con los badges mostrados arriba"
echo "   2. Commit y push de los cambios"
echo "   3. Verifica que las URLs funcionan correctamente"
echo ""

