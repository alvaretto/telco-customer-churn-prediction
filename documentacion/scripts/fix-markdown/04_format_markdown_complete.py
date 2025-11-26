#!/usr/bin/env python3
"""
Script TODO EN UNO para formatear archivos Markdown completamente.

Aplica todas las correcciones:
1. Agrega/actualiza encabezado YAML con xelatex
2. Inserta líneas vacías entre ":" y listas con viñetas/numeradas
3. Detecta todos los patrones: :, :**, ?**
4. Verifica el formato final
5. Genera reporte detallado de correcciones

Uso:
    python scripts/fix-markdown/04_format_markdown_complete.py <archivo.md>
    python scripts/fix-markdown/04_format_markdown_complete.py <archivo.md> --title "Mi Título"
    python scripts/fix-markdown/04_format_markdown_complete.py <archivo.md> --auto-title
    python scripts/fix-markdown/04_format_markdown_complete.py <archivo.md> --backup
    python scripts/fix-markdown/04_format_markdown_complete.py <archivo.md> --verbose

Ejemplos:
    python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_guia.md --auto-title
    python scripts/fix-markdown/04_format_markdown_complete.py docs/tutorial.md --title "Tutorial Completo"
    python scripts/fix-markdown/04_format_markdown_complete.py docs/guia.md --backup --verbose

Opciones:
    --title "Título"    Especifica el título del documento
    --auto-title        Extrae el título del primer H1 del documento
    --backup            Crea una copia de seguridad antes de modificar
    --verbose           Muestra información detallada de cada corrección
    --no-yaml           No agrega/actualiza el encabezado YAML
    --validate-only     Solo valida el formato sin hacer cambios
"""

import sys
import os
import re
import shutil
from datetime import datetime

def validate_format(lines, verbose=False):
    """
    Valida el formato del archivo y retorna casos pendientes de corrección.

    Args:
        lines: Lista de líneas del archivo
        verbose: Si True, muestra información detallada

    Returns:
        Lista de diccionarios con casos pendientes
    """
    pending = []
    i = 0
    code_blocks = 0

    while i < len(lines) - 1:
        current = lines[i].rstrip()
        next_line = lines[i + 1].strip()

        # Contar bloques de código
        if '```' in lines[i]:
            code_blocks += 1

        in_code = (code_blocks % 2 == 1)

        # Verificar si termina con : y siguiente empieza con - o número
        if (not in_code and
            current.endswith(':') and
            (next_line.startswith('-') or
             next_line.startswith('*') or
             next_line.startswith('+') or
             re.match(r'^\d+\.', next_line)) and
            next_line != ''):

            pending.append({
                'line': i + 1,
                'text': current[-80:] if len(current) > 80 else current,
                'next': next_line[:60] if len(next_line) > 60 else next_line
            })

        i += 1

    return pending


def format_markdown_complete(input_file, title=None, auto_title=False,
                            create_backup=False, verbose=False,
                            add_yaml=True, validate_only=False):
    """
    Aplica todas las correcciones de formato al archivo Markdown.

    Args:
        input_file: Ruta del archivo a formatear
        title: Título del documento (opcional)
        auto_title: Si True, extrae el título del primer H1
        create_backup: Si True, crea una copia de seguridad
        verbose: Si True, muestra información detallada
        add_yaml: Si True, agrega/actualiza el encabezado YAML
        validate_only: Si True, solo valida sin hacer cambios

    Returns:
        True si tuvo éxito, False en caso contrario
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe")
        return False

    print(f"\n{'='*70}")
    print(f"🚀 FORMATEANDO MARKDOWN: {os.path.basename(input_file)}")
    print(f"{'='*70}\n")

    # Paso 1: Leer archivo
    print("📖 Paso 1/5: Leyendo archivo...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    print(f"   ✅ {len(lines)} líneas leídas")

    # Si es solo validación, validar y salir
    if validate_only:
        print("\n🔍 Modo validación: Verificando formato...")
        pending = validate_format(lines, verbose)

        if len(pending) == 0:
            print(f"\n{'='*70}")
            print("✅ VALIDACIÓN EXITOSA: No hay casos pendientes de corrección")
            print(f"{'='*70}\n")
            return True
        else:
            print(f"\n⚠️  Se encontraron {len(pending)} casos pendientes:\n")
            for idx, case in enumerate(pending[:20], 1):
                print(f"{idx}. Línea {case['line']}: {case['text']}")
                if verbose:
                    print(f"   Siguiente: {case['next']}")

            if len(pending) > 20:
                print(f"\n... y {len(pending) - 20} casos más")

            print(f"\n{'='*70}")
            print(f"❌ VALIDACIÓN FALLIDA: {len(pending)} correcciones necesarias")
            print(f"{'='*70}\n")
            return False

    # Crear backup si se solicita
    if create_backup:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{input_file}.backup_{timestamp}"
        shutil.copy2(input_file, backup_file)
        print(f"   💾 Backup creado: {os.path.basename(backup_file)}")
    
    # Paso 2: Extraer/determinar título
    print("\n📝 Paso 2/5: Procesando título...")
    if add_yaml:
        if auto_title:
            for line in lines:
                match = re.match(r'^#\s+(.+)$', line.strip())
                if match:
                    title = match.group(1).strip()
                    # Remover emojis comunes
                    title = re.sub(r'[📊🔍💡✅❌🎯📖🚀⚠️💻📈📉🔧🎨📝🎓🌍💰⚖️🔥]', '', title).strip()
                    print(f"   ✅ Título extraído: {title}")
                    break
        elif title:
            print(f"   ✅ Título especificado: {title}")
        else:
            title = os.path.splitext(os.path.basename(input_file))[0].replace('_', ' ').title()
            print(f"   ✅ Título generado: {title}")
    else:
        print(f"   ⏭️  Omitiendo encabezado YAML (--no-yaml)")
    
    # Paso 3: Aplicar correcciones de formato
    print("\n🔧 Paso 3/5: Aplicando correcciones de formato...")

    # Remover YAML existente si lo hay
    content_lines = lines.copy()
    yaml_removed = False
    if content_lines and content_lines[0].strip() == '---':
        yaml_end = -1
        for i, line in enumerate(content_lines[1:], 1):
            if line.strip() == '---':
                yaml_end = i
                break
        if yaml_end > 0:
            content_lines = content_lines[yaml_end + 1:]
            yaml_removed = True
            print(f"   ⚠️  YAML existente removido")

    # Aplicar correcciones de listas
    corrected_lines = []
    code_blocks = 0
    corrections_count = 0
    corrections_detail = []

    for i in range(len(content_lines)):
        line = content_lines[i]

        # Detectar bloques de código
        if '```' in line:
            code_blocks += 1

        in_code_block = (code_blocks % 2 == 1)

        if in_code_block:
            corrected_lines.append(line)
            continue

        # Verificar formato de listas
        if i < len(content_lines) - 1:
            current_stripped = line.rstrip()
            next_line = content_lines[i + 1]
            next_stripped = next_line.strip()

            # Detectar todos los patrones:
            # - Termina con : (normal)
            # - Termina con :** (negrita)
            # - Termina con ?** (pregunta en negrita)
            ends_with_colon = (current_stripped.endswith(':') or
                              current_stripped.endswith(':**') or
                              current_stripped.endswith('?**'))

            # Detectar listas con viñetas o numeradas
            starts_with_list = (next_stripped.startswith('-') or
                               next_stripped.startswith('*') or
                               next_stripped.startswith('+') or
                               re.match(r'^\d+\.', next_stripped))

            if (ends_with_colon and
                starts_with_list and
                len(current_stripped) > 1 and
                next_stripped != ''):

                corrected_lines.append(line)
                corrected_lines.append('')  # Línea vacía
                corrections_count += 1

                # Guardar detalle de la corrección
                if verbose or corrections_count <= 10:
                    corrections_detail.append({
                        'line': i + 1,
                        'text': current_stripped[-70:] if len(current_stripped) > 70 else current_stripped
                    })

                continue

        corrected_lines.append(line)

    print(f"   ✅ {corrections_count} correcciones de formato aplicadas")

    # Mostrar detalles si es verbose o hay pocas correcciones
    if verbose and corrections_detail:
        print(f"\n   📋 Detalles de correcciones:")
        for idx, detail in enumerate(corrections_detail[:20], 1):
            print(f"      {idx}. Línea {detail['line']}: {detail['text']}")
        if len(corrections_detail) > 20:
            print(f"      ... y {len(corrections_detail) - 20} más")
    elif corrections_count > 0 and corrections_count <= 10:
        print(f"\n   📋 Correcciones aplicadas:")
        for idx, detail in enumerate(corrections_detail, 1):
            print(f"      {idx}. Línea {detail['line']}: {detail['text']}")
    
    # Paso 4: Agregar encabezado YAML
    if add_yaml:
        print("\n📋 Paso 4/5: Agregando encabezado YAML...")
        yaml_header = [
            "---",
            f'title: "{title}"',
            "output:",
            "  pdf_document:",
            "    latex_engine: xelatex",
            "    keep_tex: false",
            "  html_document: default",
            "  word_document: default",
            "---"
        ]

        final_content = '\n'.join(yaml_header + [''] + corrected_lines)
        print(f"   ✅ Encabezado YAML agregado")
    else:
        print("\n📋 Paso 4/5: Omitiendo encabezado YAML...")
        final_content = '\n'.join(corrected_lines)
        print(f"   ⏭️  Sin encabezado YAML")

    # Escribir archivo
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

    # Paso 5: Validación final
    print("\n🔍 Paso 5/5: Validación final...")
    final_lines = final_content.split('\n')
    pending = validate_format(final_lines, verbose=False)

    if len(pending) == 0:
        print(f"   ✅ Validación exitosa: No quedan casos pendientes")
    else:
        print(f"   ⚠️  Advertencia: {len(pending)} casos aún pendientes")
        if verbose:
            for idx, case in enumerate(pending[:5], 1):
                print(f"      {idx}. Línea {case['line']}: {case['text']}")

    # Resumen final
    print(f"\n{'='*70}")
    print(f"✅ FORMATEO COMPLETADO")
    print(f"{'='*70}")
    print(f"📄 Archivo: {os.path.basename(input_file)}")
    print(f"📊 Líneas iniciales: {len(lines)}")
    print(f"📊 Líneas finales: {len(final_lines)}")
    print(f"📈 Líneas añadidas: {len(final_lines) - len(lines)}")
    print(f"🔧 Correcciones aplicadas: {corrections_count}")
    if add_yaml:
        print(f"📝 Título: {title}")
        print(f"💻 Motor LaTeX: xelatex (soporte Unicode/emojis)")
    if yaml_removed:
        print(f"⚠️  YAML anterior removido y reemplazado")
    if create_backup:
        print(f"💾 Backup: {os.path.basename(backup_file)}")
    print(f"✅ Casos pendientes: {len(pending)}")
    print(f"{'='*70}\n")

    return True

if __name__ == "__main__":
    # Verificar si se solicita ayuda
    if len(sys.argv) < 2 or '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 else 1)

    input_file = sys.argv[1]
    title = None
    auto_title = False
    create_backup = False
    verbose = False
    add_yaml = True
    validate_only = False

    # Parsear argumentos
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == '--title' and i + 1 < len(sys.argv):
            title = sys.argv[i + 1]
            i += 2
        elif arg == '--auto-title':
            auto_title = True
            i += 1
        elif arg == '--backup':
            create_backup = True
            i += 1
        elif arg == '--verbose':
            verbose = True
            i += 1
        elif arg == '--no-yaml':
            add_yaml = False
            i += 1
        elif arg == '--validate-only':
            validate_only = True
            i += 1
        else:
            print(f"⚠️  Argumento desconocido: {arg}")
            i += 1

    # Ejecutar formateo
    success = format_markdown_complete(
        input_file,
        title=title,
        auto_title=auto_title,
        create_backup=create_backup,
        verbose=verbose,
        add_yaml=add_yaml,
        validate_only=validate_only
    )

    sys.exit(0 if success else 1)

