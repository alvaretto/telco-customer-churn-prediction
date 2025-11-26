#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

source = '/home/bootcamp/Proyectos-2026/Proyectos-Varios/BootCampVirtIA/Semana-05/Defensa-Proyecto/sistema-de-validacion-automatizada.md'
dest = '/home/bootcamp/Escritorio/Expo IA/Nuevos PDFs/sistema-de-validacion-automatizada.md'

try:
    # Verificar que el archivo fuente existe
    if not os.path.exists(source):
        print(f"ERROR: Archivo fuente no existe: {source}", file=sys.stderr)
        sys.exit(1)
    
    # Leer el contenido
    with open(source, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Escribir en el destino
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Verificar
    source_size = os.path.getsize(source)
    dest_size = os.path.getsize(dest)
    
    print("="*80, file=sys.stderr)
    print("ARCHIVO COPIADO EXITOSAMENTE", file=sys.stderr)
    print("="*80, file=sys.stderr)
    print(f"\nOrigen: {source}", file=sys.stderr)
    print(f"Tamaño: {source_size:,} bytes ({source_size/1024:.1f} KB)", file=sys.stderr)
    print(f"\nDestino: {dest}", file=sys.stderr)
    print(f"Tamaño: {dest_size:,} bytes ({dest_size/1024:.1f} KB)", file=sys.stderr)
    
    if source_size == dest_size:
        print("\nVerificacion: Los tamaños coinciden", file=sys.stderr)
        sys.exit(0)
    else:
        print(f"\nADVERTENCIA: Los tamaños difieren", file=sys.stderr)
        sys.exit(1)
    
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)

