# 🛠️ Scripts de Formateo de Markdown

Colección de scripts Python para formatear y verificar archivos Markdown automáticamente.

## 📂 Orden de Lectura

Los archivos están numerados secuencialmente para facilitar su lectura:

1. **01_README.md** - Este archivo (documentación general)
2. **02_EJEMPLO_USO.md** - Ejemplos prácticos paso a paso
3. **03_verify_markdown_format.py** - Script de verificación
4. **04_format_markdown_complete.py** - Script principal (TODO EN UNO)
5. **05_fix_markdown_format.py** - Script de corrección de listas
6. **06_add_yaml_header.py** - Script de encabezado YAML

---

## 📋 Scripts Disponibles

### 1. 🚀 `04_format_markdown_complete.py` (RECOMENDADO)

**Script TODO EN UNO** que aplica todas las correcciones automáticamente.

#### Uso:
```bash
# Formateo automático con título extraído del documento
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_documento.md --auto-title

# Formateo con título personalizado
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_documento.md --title "Mi Guía Completa"

# Formateo simple (genera título del nombre del archivo)
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_documento.md
```

#### ¿Qué hace?
- ✅ Agrega/actualiza encabezado YAML con xelatex
- ✅ Inserta líneas vacías entre ":" y listas con viñetas
- ✅ Preserva bloques de código intactos
- ✅ Genera reporte completo de cambios

---

### 2. 🔧 `05_fix_markdown_format.py`

Corrige el formato de listas (inserta líneas vacías).

#### Uso:
```bash
# Corregir archivo (sobrescribe el original)
python scripts/fix-markdown/05_fix_markdown_format.py docs/mi_documento.md

# Corregir y guardar en nuevo archivo
python scripts/fix-markdown/05_fix_markdown_format.py docs/original.md docs/corregido.md
```

#### ¿Qué hace?
- Inserta línea vacía entre líneas que terminan con `:` y listas con viñetas
- Preserva bloques de código
- Muestra estadísticas de correcciones

---

### 3. ✅ `03_verify_markdown_format.py`

Verifica el formato sin modificar el archivo.

#### Uso:
```bash
# Verificación básica
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md

# Verificación detallada (muestra todos los problemas)
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md --verbose
```

#### ¿Qué hace?
- Detecta problemas de formato
- Muestra ubicación exacta de cada problema
- Sugiere correcciones
- No modifica el archivo

---

### 4. 📝 `06_add_yaml_header.py`

Agrega o actualiza solo el encabezado YAML.

#### Uso:
```bash
# Con título automático (extrae del primer H1)
python scripts/fix-markdown/06_add_yaml_header.py docs/mi_documento.md --auto-title

# Con título personalizado
python scripts/fix-markdown/06_add_yaml_header.py docs/mi_documento.md --title "Mi Título"
```

#### ¿Qué hace?
- Agrega encabezado YAML con configuración xelatex
- Extrae título del documento o usa uno personalizado
- Reemplaza YAML existente si lo hay

---

## 🎯 Casos de Uso

### Caso 1: Formatear un documento nuevo
```bash
python scripts/fix-markdown/04_format_markdown_complete.py docs/nuevo_documento.md --auto-title
```

### Caso 2: Verificar antes de corregir
```bash
# Primero verificar
python scripts/fix-markdown/03_verify_markdown_format.py docs/documento.md

# Luego corregir si hay problemas
python scripts/fix-markdown/05_fix_markdown_format.py docs/documento.md
```

### Caso 3: Solo agregar YAML header
```bash
python scripts/fix-markdown/06_add_yaml_header.py docs/documento.md --title "Mi Guía"
```

### Caso 4: Formateo completo con título personalizado
```bash
python scripts/fix-markdown/04_format_markdown_complete.py docs/guia.md --title "Guía Completa de Python"
```

---

## 📊 Ejemplo de Correcciones

### ANTES:
```markdown
Los requisitos son:
- Python 3.8+
- Flask
- SQLAlchemy
```

### DESPUÉS:
```markdown
Los requisitos son:

- Python 3.8+
- Flask
- SQLAlchemy
```

---

## 🔑 Encabezado YAML Generado

```yaml
---
title: "Título del Documento"
output:
  pdf_document:
    latex_engine: xelatex
    keep_tex: false
  html_document: default
  word_document: default
---
```

**Beneficios:**
- ✅ Soporte completo de emojis y Unicode (xelatex)
- ✅ Generación de PDF, HTML y Word
- ✅ Compatible con RMarkdown y Pandoc

---

## 💡 Consejos

1. **Usa `04_format_markdown_complete.py`** para formateo rápido y completo
2. **Usa `03_verify_markdown_format.py`** para revisar sin modificar
3. **Usa `--auto-title`** para extraer el título del documento
4. **Haz backup** antes de formatear archivos importantes (aunque los scripts son seguros)

---

## 🚀 Workflow Recomendado

```bash
# 1. Verificar el documento
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_guia.md

# 2. Formatear completamente
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_guia.md --auto-title

# 3. Verificar resultado
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_guia.md
```

---

## ⚙️ Requisitos

- Python 3.6+
- No requiere librerías externas (solo stdlib)

---

## 📝 Notas

- Todos los scripts preservan los bloques de código intactos
- Los scripts usan encoding UTF-8 para soporte completo de Unicode
- Los archivos originales se sobrescriben por defecto (excepto si especificas archivo de salida)

