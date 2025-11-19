#!/bin/bash

# Script para sincronización bidireccional inteligente
# Mantiene sincronizados los archivos más recientes entre local y Drive
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
echo -e "${BLUE}║     Sincronización Bidireccional (Local ↔ Drive)          ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Verificar que el directorio local existe
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}❌ Error: El directorio $PROJECT_DIR no existe${NC}"
    exit 1
fi

# Mostrar información
echo -e "${YELLOW}📁 Directorio local:${NC} $PROJECT_DIR"
echo -e "${YELLOW}☁️  Google Drive:${NC} $DRIVE_DIR"
echo ""
echo -e "${BLUE}ℹ️  Este script sincroniza archivos en ambas direcciones${NC}"
echo -e "${BLUE}   manteniendo siempre la versión más reciente.${NC}"
echo ""

# Preguntar confirmación
read -p "¿Deseas continuar? (s/N): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    echo -e "${YELLOW}⚠️  Sincronización cancelada${NC}"
    exit 0
fi

echo ""
echo -e "${BLUE}🔄 Sincronizando archivos (bidireccional)...${NC}"
echo ""

# Usar bisync para sincronización bidireccional
rclone bisync "$PROJECT_DIR" "$DRIVE_DIR" \
    --progress \
    --exclude ".git/**" \
    --exclude ".venv/**" \
    --exclude "__pycache__/**" \
    --exclude "*.pyc" \
    --exclude ".DS_Store" \
    --exclude "node_modules/**" \
    --verbose \
    --create-empty-src-dirs \
    --compare size,modtime \
    --slow-hash-sync-only \
    --resilient

# Verificar resultado
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Sincronización bidireccional completada${NC}"
    echo ""
else
    echo ""
    echo -e "${YELLOW}⚠️  Nota: Si es la primera vez que ejecutas este script,${NC}"
    echo -e "${YELLOW}   necesitas inicializar bisync con:${NC}"
    echo ""
    echo -e "${BLUE}   rclone bisync \"$PROJECT_DIR\" \"$DRIVE_DIR\" --resync${NC}"
    echo ""
    echo -e "${RED}❌ Error durante la sincronización${NC}"
    exit 1
fi

