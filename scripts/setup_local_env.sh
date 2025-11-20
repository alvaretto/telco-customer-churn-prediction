#!/bin/bash

echo "============================================================"
echo "🔧 CONFIGURACIÓN DEL ENTORNO LOCAL"
echo "============================================================"

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Entorno virtual creado${NC}"
    else
        echo -e "${RED}❌ Error creando entorno virtual${NC}"
        exit 1
    fi
fi

# Activar entorno virtual
echo ""
echo "🔄 Activando entorno virtual..."
source venv/bin/activate

echo ""
echo "📦 Instalando dependencias mínimas para inferencia..."
echo ""

# Instalar dependencias básicas
pip install --quiet --upgrade pip
pip install --quiet joblib==1.3.2 scikit-learn==1.3.2 pandas==2.1.4 numpy==1.26.2

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependencias básicas instaladas${NC}"
else
    echo -e "${RED}❌ Error instalando dependencias${NC}"
    exit 1
fi

echo ""
echo "🧪 Ejecutando test de carga del modelo..."
echo ""

python3 scripts/test_model_loading.py

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}============================================================${NC}"
    echo -e "${GREEN}✅ ENTORNO LOCAL CONFIGURADO CORRECTAMENTE${NC}"
    echo -e "${GREEN}============================================================${NC}"
    echo ""
    echo "🚀 Próximos pasos:"
    echo ""
    echo "1️⃣ Probar la API:"
    echo "   cd api"
    echo "   pip3 install -r requirements.txt"
    echo "   python3 app.py"
    echo ""
    echo "2️⃣ Probar el Dashboard:"
    echo "   cd dashboard"
    echo "   pip3 install -r requirements.txt"
    echo "   streamlit run app.py"
    echo ""
    echo "3️⃣ Ejecutar tests:"
    echo "   pip3 install pytest"
    echo "   pytest tests/ -v"
    echo ""
else
    echo -e "${RED}❌ Error en el test de carga${NC}"
    exit 1
fi

