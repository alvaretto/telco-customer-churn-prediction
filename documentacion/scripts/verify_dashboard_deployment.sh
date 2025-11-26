#!/bin/bash

# Script de verificación del deployment del Dashboard en Streamlit Cloud
# Uso: ./scripts/verify_dashboard_deployment.sh <URL_DEL_DASHBOARD>

set -e

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "=========================================="
echo "🔍 VERIFICACIÓN DE DEPLOYMENT - DASHBOARD"
echo "=========================================="
echo ""

# Verificar que se proporcionó la URL
if [ -z "$1" ]; then
    echo -e "${RED}❌ Error: Debes proporcionar la URL del Dashboard${NC}"
    echo "Uso: $0 <URL_DEL_DASHBOARD>"
    echo "Ejemplo: $0 https://telco-churn-dashboard.streamlit.app"
    exit 1
fi

DASHBOARD_URL="$1"

# Remover trailing slash si existe
DASHBOARD_URL="${DASHBOARD_URL%/}"

echo "📍 URL del Dashboard: $DASHBOARD_URL"
echo ""

# Test 1: Verificar que el dashboard responde
echo "Test 1/3: Verificando accesibilidad del Dashboard..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$DASHBOARD_URL")

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Dashboard accesible (HTTP $HTTP_CODE)${NC}"
else
    echo -e "${RED}❌ Dashboard no accesible (HTTP $HTTP_CODE)${NC}"
    echo "   Verifica que el deployment en Streamlit Cloud haya terminado"
    exit 1
fi
echo ""

# Test 2: Verificar que los archivos del modelo están disponibles
echo "Test 2/3: Verificando carga del modelo..."
echo -e "${YELLOW}ℹ️  Este test requiere verificación manual en el navegador${NC}"
echo "   1. Abre: $DASHBOARD_URL"
echo "   2. Verifica que la página principal carga sin errores"
echo "   3. Navega a '📈 Model Metrics' y verifica que muestra métricas"
echo ""
read -p "¿La página principal carga correctamente? (s/n): " MAIN_PAGE
if [ "$MAIN_PAGE" != "s" ] && [ "$MAIN_PAGE" != "S" ]; then
    echo -e "${RED}❌ Verificación manual falló${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Página principal OK${NC}"
echo ""

# Test 3: Verificar navegación entre páginas
echo "Test 3/3: Verificando páginas del Dashboard..."
echo -e "${YELLOW}ℹ️  Verifica manualmente que estas páginas cargan:${NC}"
echo "   • 📊 Overview"
echo "   • 🎯 Risk Analysis"
echo "   • 📈 Model Metrics"
echo "   • 💰 ROI Simulator"
echo "   • 🔍 Model Monitoring"
echo ""
read -p "¿Todas las páginas cargan correctamente? (s/n): " ALL_PAGES
if [ "$ALL_PAGES" != "s" ] && [ "$ALL_PAGES" != "S" ]; then
    echo -e "${RED}❌ Verificación de páginas falló${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Todas las páginas OK${NC}"
echo ""

# Resumen final
echo "=========================================="
echo -e "${GREEN}✅ DASHBOARD VERIFICADO${NC}"
echo "=========================================="
echo ""
echo "📊 Resumen:"
echo "   • Accesibilidad: ✅"
echo "   • Página principal: ✅"
echo "   • Navegación: ✅"
echo ""
echo "🎉 El Dashboard está funcionando correctamente en producción!"
echo ""
echo "📝 Próximos pasos:"
echo "   1. Guarda esta URL en URLS_PRODUCCION.md"
echo "   2. Actualiza README.md con la URL"
echo "   3. Prueba hacer una predicción en '🎯 Risk Analysis'"
echo "   4. Verifica las métricas en '📈 Model Metrics'"
echo ""
echo "🔗 URLs del Proyecto:"
echo "   • Dashboard: $DASHBOARD_URL"
echo ""

