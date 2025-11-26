# 📚 Ejemplo de Uso de los Scripts de Formateo

## 📂 Ubicación de los Scripts

Todos los scripts están en: `scripts/fix-markdown/`

- **03_verify_markdown_format.py** - Verificar formato
- **04_format_markdown_complete.py** - Formateo completo (RECOMENDADO)
- **05_fix_markdown_format.py** - Corregir solo listas
- **06_add_yaml_header.py** - Agregar solo YAML

---

## 🎯 Escenario: Tienes un documento Markdown sin formatear

Supongamos que tienes este documento (`docs/mi_tutorial.md`):

```markdown
# Tutorial de Python

## Introducción

Este tutorial cubre los conceptos básicos de Python.

## Requisitos:
- Python 3.8+
- pip
- virtualenv

## Instalación:
1. Descargar Python
2. Instalar pip
3. Crear entorno virtual

## Características principales:
- Fácil de aprender
- Sintaxis clara
- Gran comunidad

```

---

## 🔍 Paso 1: Verificar el formato

```bash
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_tutorial.md
```

**Salida esperada:**
```
📊 Análisis de: docs/mi_tutorial.md
📄 Total de líneas: 20
💻 Bloques de código: 0

❌ Se encontraron 3 problemas de formato:

  Línea 7: ## Requisitos:
    ↳ Siguiente: - Python 3.8+

  Línea 12: ## Instalación:
    ↳ Siguiente: 1. Descargar Python

  Línea 17: ## Características principales:
    ↳ Siguiente: - Fácil de aprender

💡 Sugerencia: Ejecuta el script de corrección:
   python scripts/fix-markdown/05_fix_markdown_format.py docs/mi_tutorial.md
```

---

## 🔧 Paso 2: Aplicar correcciones

### Opción A: Formateo completo (RECOMENDADO)

```bash
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_tutorial.md --auto-title
```

**Salida esperada:**
```
============================================================
🚀 FORMATEANDO MARKDOWN: docs/mi_tutorial.md
============================================================

📖 Paso 1/4: Leyendo archivo...
   ✅ 20 líneas leídas

📝 Paso 2/4: Procesando título...
   ✅ Título extraído: Tutorial de Python

🔧 Paso 3/4: Aplicando correcciones de formato...
   ✅ 3 correcciones de formato aplicadas

📋 Paso 4/4: Agregando encabezado YAML...
   ✅ Encabezado YAML agregado

============================================================
✅ FORMATEO COMPLETADO
============================================================
📄 Archivo: docs/mi_tutorial.md
📊 Líneas finales: 32
🔧 Correcciones: 3
📝 Título: Tutorial de Python
💻 Motor LaTeX: xelatex (soporte Unicode/emojis)
============================================================
```

### Opción B: Solo corregir formato de listas

```bash
python scripts/fix-markdown/05_fix_markdown_format.py docs/mi_tutorial.md
```

**Salida esperada:**
```
✅ Archivo corregido: docs/mi_tutorial.md
📊 Correcciones aplicadas: 3
📄 Líneas originales: 20
📄 Líneas finales: 23
```

---

## ✅ Paso 3: Verificar resultado

```bash
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_tutorial.md
```

**Salida esperada:**
```
📊 Análisis de: docs/mi_tutorial.md
📄 Total de líneas: 32
💻 Bloques de código: 0

✅ No se encontraron problemas de formato!
✅ El archivo está correctamente formateado.
```

---

## 📄 Resultado Final

El documento ahora tiene este formato:

```markdown
---
title: "Tutorial de Python"
output:
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
  html_document: default
  word_document: default
---
# Tutorial de Python

## Introducción

Este tutorial cubre los conceptos básicos de Python.

## Requisitos:

- Python 3.8+
- pip
- virtualenv

## Instalación:

1. Descargar Python
2. Instalar pip
3. Crear entorno virtual

## Características principales:

- Fácil de aprender
- Sintaxis clara
- Gran comunidad
```

---

## 🎨 Casos de Uso Adicionales

### Formatear múltiples archivos

```bash
# Formatear todos los archivos .md en un directorio
for file in docs/*.md; do
    python scripts/fix-markdown/04_format_markdown_complete.py "$file" --auto-title
done
```

### Verificar múltiples archivos

```bash
# Verificar todos los archivos .md
for file in docs/**/*.md; do
    echo "Verificando: $file"
    python scripts/fix-markdown/03_verify_markdown_format.py "$file"
    echo "---"
done
```

### Usar título personalizado

```bash
python scripts/fix-markdown/04_format_markdown_complete.py docs/guia.md --title "Guía Completa de Machine Learning"
```

### Solo agregar YAML header

```bash
python scripts/fix-markdown/06_add_yaml_header.py docs/documento.md --auto-title
```

---

## 💡 Tips y Trucos

1. **Siempre verifica primero**: Usa `03_verify_markdown_format.py` antes de aplicar correcciones
2. **Usa `--auto-title`**: Extrae automáticamente el título del primer H1
3. **Haz backup**: Aunque los scripts son seguros, siempre es buena práctica
4. **Formateo en lote**: Usa loops para formatear múltiples archivos
5. **Integra en CI/CD**: Puedes usar estos scripts en pipelines de integración continua

---

## 🚀 Workflow Completo

```bash
# 1. Verificar estado actual
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md

# 2. Formatear completamente
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_documento.md --auto-title

# 3. Verificar resultado
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md

# 4. Generar PDF (opcional)
pandoc docs/mi_documento.md -o docs/mi_documento.pdf
```

---

## 📊 Comparación de Scripts

| Script | Agrega YAML | Corrige Listas | Verifica | Modifica Archivo |
|--------|-------------|----------------|----------|------------------|
| `04_format_markdown_complete.py` | ✅ | ✅ | ✅ | ✅ |
| `05_fix_markdown_format.py` | ❌ | ✅ | ❌ | ✅ |
| `03_verify_markdown_format.py` | ❌ | ❌ | ✅ | ❌ |
| `06_add_yaml_header.py` | ✅ | ❌ | ❌ | ✅ |

**Recomendación**: Usa `04_format_markdown_complete.py` para la mayoría de casos.

