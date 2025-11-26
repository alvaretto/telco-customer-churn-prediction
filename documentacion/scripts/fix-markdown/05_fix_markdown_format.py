#!/usr/bin/env python3
"""
Script para corregir el formato de archivos Markdown.

Correcciones que aplica:
1. Insertar línea vacía entre líneas que terminan con ":" y listas con viñetas
2. Mantener intactos los bloques de código
3. Preservar la estructura del documento

Uso:
    python scripts/fix-markdown/05_fix_markdown_format.py <archivo.md>
    python scripts/fix-markdown/05_fix_markdown_format.py <archivo.md> <archivo_salida.md>

Ejemplos:
    python scripts/fix-markdown/05_fix_markdown_format.py docs/mi_documento.md
    python scripts/fix-markdown/05_fix_markdown_format.py docs/original.md docs/corregido.md
"""

import re
import sys
import os

def fix_markdown_format(input_file, output_file=None):
    """
    Corrige el formato del archivo Markdown.
    
    Args:
        input_file: Ruta del archivo de entrada
        output_file: Ruta del archivo de salida (si es None, sobrescribe el original)
    
    Returns:
        Tupla (archivo_salida, num_correcciones)
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe")
        return None, 0
    
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    corrected_lines = []
    in_code_block = False
    corrections_count = 0
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Detectar inicio/fin de bloques de código
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            corrected_lines.append(line)
            i += 1
            continue
        
        # Si estamos en un bloque de código, no modificar
        if in_code_block:
            corrected_lines.append(line)
            i += 1
            continue
        
        # Verificar si la línea termina con ":" y la siguiente comienza con "-", "*", o "+"
        if i < len(lines) - 1:
            current_stripped = line.rstrip()
            next_line = lines[i + 1]
            next_stripped = next_line.lstrip()
            
            # Verificar si termina con ":" y la siguiente línea es una viñeta
            if (current_stripped.endswith(':') and 
                len(current_stripped) > 1 and  # No solo ":"
                next_stripped and 
                next_stripped[0] in ['-', '*', '+'] and
                next_line.strip() != ''):  # La siguiente línea no está vacía
                
                # Verificar que no haya ya una línea vacía
                if next_line.strip() != '':
                    corrected_lines.append(line)
                    corrected_lines.append('\n')  # Insertar línea vacía
                    corrections_count += 1
                    i += 1
                    continue
        
        corrected_lines.append(line)
        i += 1
    
    # Escribir el archivo corregido
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(corrected_lines)
    
    print(f"✅ Archivo corregido: {output_file}")
    print(f"📊 Correcciones aplicadas: {corrections_count}")
    print(f"📄 Líneas originales: {len(lines)}")
    print(f"📄 Líneas finales: {len(corrected_lines)}")
    
    return output_file, corrections_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    result, count = fix_markdown_format(input_file, output_file)
    
    if result:
        sys.exit(0)
    else:
        sys.exit(1)

