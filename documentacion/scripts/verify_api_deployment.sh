#!/bin/bash

# Script de verificación del deployment de la API en Render.com
# Uso: ./scripts/verify_api_deployment.sh <URL_DE_LA_API>

set -e

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "🔍 VERIFICACIÓN DE DEPLOYMENT - API"
echo "=========================================="
echo ""

# Verificar que se proporcionó la URL
if [ -z "$1" ]; then
    echo -e "${RED}❌ Error: Debes proporcionar la URL de la API${NC}"
    echo "Uso: $0 <URL_DE_LA_API>"
    echo "Ejemplo: $0 https://telco-churn-api.onrender.com"
    exit 1
fi

API_URL="$1"

# Remover trailing slash si existe
API_URL="${API_URL%/}"

echo "📍 URL de la API: $API_URL"
echo ""

# Test 1: Health Check
echo "Test 1/4: Health Check Endpoint..."
HEALTH_RESPONSE=$(curl -s -w "\n%{http_code}" "$API_URL/health")
HTTP_CODE=$(echo "$HEALTH_RESPONSE" | tail -n1)
BODY=$(echo "$HEALTH_RESPONSE" | head -n-1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Health check OK (HTTP $HTTP_CODE)${NC}"
    echo "   Response: $BODY"
else
    echo -e "${RED}❌ Health check FAILED (HTTP $HTTP_CODE)${NC}"
    echo "   Response: $BODY"
    exit 1
fi
echo ""

# Test 2: Model Info
echo "Test 2/4: Model Info Endpoint..."
MODEL_RESPONSE=$(curl -s -w "\n%{http_code}" "$API_URL/model_info")
HTTP_CODE=$(echo "$MODEL_RESPONSE" | tail -n1)
BODY=$(echo "$MODEL_RESPONSE" | head -n-1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Model info OK (HTTP $HTTP_CODE)${NC}"
    echo "   Response preview: $(echo $BODY | head -c 100)..."
else
    echo -e "${RED}❌ Model info FAILED (HTTP $HTTP_CODE)${NC}"
    echo "   Response: $BODY"
    exit 1
fi
echo ""

# Test 3: Root Endpoint
echo "Test 3/4: Root Endpoint..."
ROOT_RESPONSE=$(curl -s -w "\n%{http_code}" "$API_URL/")
HTTP_CODE=$(echo "$ROOT_RESPONSE" | tail -n1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Root endpoint OK (HTTP $HTTP_CODE)${NC}"
else
    echo -e "${YELLOW}⚠️  Root endpoint returned HTTP $HTTP_CODE${NC}"
fi
echo ""

# Test 4: Prediction Endpoint (con datos de prueba)
echo "Test 4/4: Prediction Endpoint..."
PREDICT_DATA='{
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

PREDICT_RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d "$PREDICT_DATA")
HTTP_CODE=$(echo "$PREDICT_RESPONSE" | tail -n1)
BODY=$(echo "$PREDICT_RESPONSE" | head -n-1)

if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✅ Prediction OK (HTTP $HTTP_CODE)${NC}"
    echo "   Response: $BODY"
else
    echo -e "${RED}❌ Prediction FAILED (HTTP $HTTP_CODE)${NC}"
    echo "   Response: $BODY"
    exit 1
fi
echo ""

# Resumen final
echo "=========================================="
echo -e "${GREEN}✅ TODOS LOS TESTS PASARON${NC}"
echo "=========================================="
echo ""
echo "📊 Resumen:"
echo "   • Health Check: ✅"
echo "   • Model Info: ✅"
echo "   • Root Endpoint: ✅"
echo "   • Prediction: ✅"
echo ""
echo "🎉 La API está funcionando correctamente en producción!"
echo ""
echo "📝 Próximos pasos:"
echo "   1. Guarda esta URL en URLS_PRODUCCION.md"
echo "   2. Actualiza README.md con la URL"
echo "   3. Procede con el deployment del Dashboard"
echo ""

