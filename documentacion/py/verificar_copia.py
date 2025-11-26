#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

dest = '/home/bootcamp/Escritorio/Expo IA/Nuevos PDFs/sistema-de-validacion-automatizada.md'
log_file = '/tmp/verificacion_copia.txt'

with open(log_file, 'w') as f:
    if os.path.exists(dest):
        size = os.path.getsize(dest)
        f.write(f"EXISTE: {size} bytes\n")
        
        # Leer primeras líneas
        with open(dest, 'r', encoding='utf-8') as df:
            lines = df.readlines()[:5]
            f.write(f"Primeras 5 lineas:\n")
            for line in lines:
                f.write(line)
    else:
        f.write("NO EXISTE\n")

print(f"Resultado escrito en: {log_file}")

