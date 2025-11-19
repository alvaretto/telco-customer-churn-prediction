#!/bin/bash

# Script para descargar resultados desde Google Drive (después de ejecutar en Colab)
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
echo -e "${BLUE}║     Sincronización Google Drive (Colab) → Local           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Verificar que el directorio local existe
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}❌ Error: El directorio $PROJECT_DIR no existe${NC}"
    exit 1
fi

# Mostrar información
echo -e "${YELLOW}☁️  Origen en Drive:${NC} $DRIVE_DIR"
echo -e "${YELLOW}📁 Directorio local:${NC} $PROJECT_DIR"
echo ""

# Advertencia
echo -e "${YELLOW}⚠️  ADVERTENCIA: Esto sobrescribirá archivos locales si hay conflictos${NC}"
echo ""

# Preguntar confirmación
read -p "¿Deseas continuar con la descarga? (s/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    echo -e "${YELLOW}⚠️  Descarga cancelada${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}📥 Descargando archivos desde Google Drive...${NC}"
echo ""

# Sincronizar (solo archivos modificados)
rclone sync "$DRIVE_DIR" "$PROJECT_DIR" \
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
    echo -e "${GREEN}✅ Descarga completada exitosamente${NC}"
    echo ""
    echo -e "${BLUE}📝 Próximos pasos:${NC}"
    echo "   1. Abre VS Code Insiders"
    echo "   2. Revisa el notebook con los resultados de Colab"
    echo "   3. Los outputs y gráficos deberían estar visibles"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Error durante la descarga${NC}"
    exit 1
fi

