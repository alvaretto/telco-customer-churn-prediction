#!/usr/bin/env python3
"""
Script para agregar o actualizar el encabezado YAML en archivos Markdown.

Agrega configuración para:
1. Motor LaTeX xelatex (soporte de emojis y Unicode)
2. Configuración de PDF, HTML y Word
3. Título del documento

Uso:
    python scripts/fix-markdown/06_add_yaml_header.py <archivo.md> [--title "Título del documento"]
    python scripts/fix-markdown/06_add_yaml_header.py <archivo.md> --auto-title

Ejemplos:
    python scripts/fix-markdown/06_add_yaml_header.py docs/mi_documento.md --title "Mi Guía"
    python scripts/fix-markdown/06_add_yaml_header.py docs/mi_documento.md --auto-title
"""

import sys
import os
import re

def extract_title_from_content(lines):
    """Extrae el título del primer encabezado H1 del documento."""
    for line in lines:
        # Buscar primer H1 (# Título)
        match = re.match(r'^#\s+(.+)$', line.strip())
        if match:
            # Limpiar emojis y caracteres especiales del título
            title = match.group(1).strip()
            # Remover emojis comunes
            title = re.sub(r'[📊🔍💡✅❌🎯📖🚀⚠️💻📈📉🔧🎨📝]', '', title).strip()
            return title
    return "Documento sin título"

def add_or_update_yaml_header(input_file, title=None, auto_title=False, output_file=None):
    """
    Agrega o actualiza el encabezado YAML del archivo Markdown.
    
    Args:
        input_file: Ruta del archivo de entrada
        title: Título del documento (opcional)
        auto_title: Si True, extrae el título del primer H1
        output_file: Ruta del archivo de salida (si es None, sobrescribe el original)
    
    Returns:
        Ruta del archivo modificado
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe")
        return None
    
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    # Determinar el título
    if auto_title:
        title = extract_title_from_content(lines)
        print(f"📝 Título extraído: {title}")
    elif title is None:
        title = "Documento"
    
    # Verificar si ya tiene encabezado YAML
    has_yaml = content.strip().startswith('---')
    
    if has_yaml:
        # Encontrar el final del YAML existente
        yaml_end = -1
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                yaml_end = i
                break
        
        if yaml_end > 0:
            # Remover YAML existente
            remaining_content = '\n'.join(lines[yaml_end + 1:])
            print(f"⚠️  Reemplazando encabezado YAML existente...")
        else:
            remaining_content = content
    else:
        remaining_content = content
    
    # Crear nuevo encabezado YAML
    yaml_header = f"""---
title: "{title}"
output:
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
  html_document: default
  word_document: default
---
"""
    
    # Combinar YAML con contenido
    new_content = yaml_header + remaining_content
    
    # Escribir archivo
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Encabezado YAML agregado/actualizado: {output_file}")
    print(f"📊 Configuración:")
    print(f"   - Título: {title}")
    print(f"   - Motor LaTeX: xelatex (soporte Unicode/emojis)")
    print(f"   - Formatos: PDF, HTML, Word")
    
    return output_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    input_file = sys.argv[1]
    title = None
    auto_title = False
    
    # Procesar argumentos
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--title' and i + 1 < len(sys.argv):
            title = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--auto-title':
            auto_title = True
            i += 1
        else:
            i += 1
    
    result = add_or_update_yaml_header(input_file, title, auto_title)
    
    sys.exit(0 if result else 1)

