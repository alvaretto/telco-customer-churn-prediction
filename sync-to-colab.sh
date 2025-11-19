#!/bin/bash

# Script para sincronizar proyecto local a Google Drive (para usar en Colab)
# Autor: Configuración automática
# Fecha: 2025-11-19

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuración
PROJECT_DIR="/home/bootcamp/Proyectos-2026/Proyectos-Varios/BootCampVirtIA/Semana-05/Defensa-Proyecto"
DRIVE_DIR="gdrive:Colab Notebooks/Defensa-Proyecto"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Sincronización Local → Google Drive (Colab)           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Verificar que el directorio local existe
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}❌ Error: El directorio $PROJECT_DIR no existe${NC}"
    exit 1
fi

# Mostrar información
echo -e "${YELLOW}📁 Directorio local:${NC} $PROJECT_DIR"
echo -e "${YELLOW}☁️  Destino en Drive:${NC} $DRIVE_DIR"
echo ""

# Preguntar confirmación
read -p "¿Deseas continuar con la sincronización? (s/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    echo -e "${YELLOW}⚠️  Sincronización cancelada${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}📤 Subiendo archivos a Google Drive...${NC}"
echo ""

# Sincronizar (solo archivos modificados)
rclone sync "$PROJECT_DIR" "$DRIVE_DIR" \
    --progress \
    --exclude ".git/**" \
    --exclude ".venv/**" \
    --exclude "__pycache__/**" \
    --exclude "*.pyc" \
    --exclude ".DS_Store" \
    --exclude "node_modules/**" \
    --verbose

# Verificar resultado
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Sincronización completada exitosamente${NC}"
    echo ""
    echo -e "${BLUE}🌐 Próximos pasos:${NC}"
    echo "   1. Abre Google Colab: https://colab.research.google.com/"
    echo "   2. Ve a 'Archivo' → 'Abrir notebook'"
    echo "   3. Selecciona la pestaña 'Google Drive'"
    echo "   4. Navega a: Colab Notebooks/Defensa-Proyecto/"
    echo "   5. Abre: Telco-Customer-Churn.ipynb"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Error durante la sincronización${NC}"
    exit 1
fi

