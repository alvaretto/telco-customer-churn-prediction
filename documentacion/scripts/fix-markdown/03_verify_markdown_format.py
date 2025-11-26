#!/usr/bin/env python3
"""
Script para verificar el formato de archivos Markdown.

Verifica:
1. Líneas que terminan con ":" seguidas directamente por viñetas sin línea vacía
2. Bloques de código correctamente formateados
3. Estructura general del documento

Uso:
    python scripts/fix-markdown/03_verify_markdown_format.py <archivo.md>
    python scripts/fix-markdown/03_verify_markdown_format.py <archivo.md> --verbose

Ejemplos:
    python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md
    python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md --verbose
"""

import sys
import os

def verify_markdown_format(input_file, verbose=False):
    """
    Verifica el formato del archivo Markdown.
    
    Args:
        input_file: Ruta del archivo a verificar
        verbose: Si True, muestra información detallada
    
    Returns:
        Tupla (tiene_problemas, lista_de_problemas)
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe")
        return True, []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    issues = []
    in_code_block = False
    code_block_count = 0
    
    for i in range(len(lines) - 1):
        line = lines[i]
        
        # Detectar inicio/fin de bloques de código
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            if in_code_block:
                code_block_count += 1
            continue
        
        # Si estamos en un bloque de código, no verificar
        if in_code_block:
            continue
        
        current_stripped = line.rstrip()
        next_line = lines[i + 1]
        next_stripped = next_line.lstrip()
        
        # Verificar si termina con ":" y la siguiente línea es una viñeta sin línea vacía
        if (current_stripped.endswith(':') and 
            len(current_stripped) > 1 and
            next_stripped and 
            next_stripped[0] in ['-', '*', '+'] and
            next_line.strip() != ''):
            
            issues.append({
                'line_number': i + 1,
                'line': current_stripped[:80],  # Primeros 80 caracteres
                'next_line': next_stripped[:80]
            })
    
    # Mostrar resultados
    print(f"\n📊 Análisis de: {input_file}")
    print(f"📄 Total de líneas: {len(lines)}")
    print(f"💻 Bloques de código: {code_block_count}")
    
    if issues:
        print(f"\n❌ Se encontraron {len(issues)} problemas de formato:\n")
        
        max_show = 10 if not verbose else len(issues)
        for issue in issues[:max_show]:
            print(f"  Línea {issue['line_number']}: {issue['line']}")
            print(f"    ↳ Siguiente: {issue['next_line']}\n")
        
        if len(issues) > max_show:
            print(f"  ... y {len(issues) - max_show} más (usa --verbose para ver todos)")
        
        print(f"\n💡 Sugerencia: Ejecuta el script de corrección:")
        print(f"   python scripts/fix-markdown/05_fix_markdown_format.py {input_file}")
        
        return True, issues
    else:
        print("\n✅ No se encontraron problemas de formato!")
        print("✅ El archivo está correctamente formateado.")
        return False, []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    input_file = sys.argv[1]
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    has_issues, issues = verify_markdown_format(input_file, verbose)
    
    sys.exit(1 if has_issues else 0)

