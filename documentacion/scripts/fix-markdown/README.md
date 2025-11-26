# 🔧 Script de Formateo Completo de Markdown

## 📋 Descripción

`04_format_markdown_complete.py` es un script TODO EN UNO que aplica todas las correcciones de formato necesarias para archivos Markdown, especialmente aquellos que contienen emojis y caracteres Unicode.

## ✨ Características

### Correcciones Automáticas

1. **Encabezado YAML con xelatex**
   - Agrega o actualiza el encabezado YAML
   - Configura `xelatex` como motor LaTeX (soporte Unicode/emojis)
   - Configura salidas para PDF, HTML y Word

2. **Formato de Listas**
   - Inserta líneas vacías entre líneas que terminan con `:` y listas
   - Detecta todos los patrones: `:`, `:**`, `?**`
   - Soporta listas con viñetas (`-`, `*`, `+`) y numeradas (`1.`, `2.`, etc.)
   - Respeta bloques de código (no modifica código)

3. **Validación Final**
   - Verifica que no queden casos pendientes
   - Genera reporte detallado de correcciones
   - Modo de solo validación disponible

## 🚀 Uso

### Sintaxis Básica

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py <archivo.md> [opciones]
```

### Opciones Disponibles

| Opción | Descripción |
|--------|-------------|
| `--title "Título"` | Especifica el título del documento |
| `--auto-title` | Extrae el título del primer H1 del documento |
| `--backup` | Crea una copia de seguridad antes de modificar |
| `--verbose` | Muestra información detallada de cada corrección |
| `--no-yaml` | No agrega/actualiza el encabezado YAML |
| `--validate-only` | Solo valida el formato sin hacer cambios |
| `--help`, `-h` | Muestra la ayuda |

## 📚 Ejemplos de Uso

### Ejemplo 1: Formateo Básico

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/mi_guia.md
```

**Resultado:**
- Agrega encabezado YAML con título generado del nombre del archivo
- Aplica todas las correcciones de formato
- Valida el resultado final

### Ejemplo 2: Con Título Automático

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/tutorial.md --auto-title
```

**Resultado:**
- Extrae el título del primer `# Título` del documento
- Remueve emojis del título
- Aplica todas las correcciones

### Ejemplo 3: Con Título Personalizado

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/guia.md --title "Guía Completa de ML"
```

**Resultado:**
- Usa el título especificado
- Aplica todas las correcciones

### Ejemplo 4: Con Backup y Verbose

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/importante.md --backup --verbose
```

**Resultado:**
- Crea backup: `importante.md.backup_20250126_143022`
- Muestra detalles de cada corrección aplicada
- Aplica todas las correcciones

### Ejemplo 5: Solo Validación

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/revisar.md --validate-only
```

**Resultado:**
- No modifica el archivo
- Muestra casos pendientes de corrección
- Retorna código de salida 0 si está OK, 1 si hay problemas

### Ejemplo 6: Sin YAML

```bash
python documentacion/scripts/fix-markdown/04_format_markdown_complete.py docs/simple.md --no-yaml
```

**Resultado:**
- Solo aplica correcciones de formato
- No agrega/modifica encabezado YAML

## 📊 Salida del Script

### Ejemplo de Salida Exitosa

```
======================================================================
🚀 FORMATEANDO MARKDOWN: preguntas_sustentacion.md
======================================================================

📖 Paso 1/5: Leyendo archivo...
   ✅ 7349 líneas leídas
   💾 Backup creado: preguntas_sustentacion.md.backup_20250126_143022

📝 Paso 2/5: Procesando título...
   ✅ Título extraído: Guía de Preguntas para Entender tu Proyecto

🔧 Paso 3/5: Aplicando correcciones de formato...
   ✅ 535 correcciones de formato aplicadas

📋 Paso 4/5: Agregando encabezado YAML...
   ✅ Encabezado YAML agregado

🔍 Paso 5/5: Validación final...
   ✅ Validación exitosa: No quedan casos pendientes

======================================================================
✅ FORMATEO COMPLETADO
======================================================================
📄 Archivo: preguntas_sustentacion.md
📊 Líneas iniciales: 7349
📊 Líneas finales: 7904
📈 Líneas añadidas: 555
🔧 Correcciones aplicadas: 535
📝 Título: Guía de Preguntas para Entender tu Proyecto
💻 Motor LaTeX: xelatex (soporte Unicode/emojis)
💾 Backup: preguntas_sustentacion.md.backup_20250126_143022
✅ Casos pendientes: 0
======================================================================
```

## 🔍 Patrones Detectados

El script detecta y corrige los siguientes patrones:

### Patrón 1: Texto normal con dos puntos

```markdown
ANTES:
Los requisitos son:
- Python 3.8+
- Flask

DESPUÉS:
Los requisitos son:

- Python 3.8+
- Flask
```

### Patrón 2: Texto en negrita con dos puntos

```markdown
ANTES:
**Acción:**
- Implementar mejoras
- Monitorear resultados

DESPUÉS:
**Acción:**

- Implementar mejoras
- Monitorear resultados
```

### Patrón 3: Pregunta en negrita

```markdown
ANTES:
**¿Es mucho?**
- No, 27 features es manejable
- Alta dimensionalidad sería >100

DESPUÉS:
**¿Es mucho?**

- No, 27 features es manejable
- Alta dimensionalidad sería >100
```

### Patrón 4: Listas numeradas

```markdown
ANTES:
Para cada técnica:
1. Balancear datos
2. Entrenar modelo

DESPUÉS:
Para cada técnica:

1. Balancear datos
2. Entrenar modelo
```

## ⚙️ Funcionamiento Interno

### Algoritmo de Corrección

1. **Lectura del archivo**
   - Lee el contenido completo
   - Divide en líneas

2. **Procesamiento de título**
   - Extrae o genera el título según opciones

3. **Aplicación de correcciones**
   - Remueve YAML existente si lo hay
   - Itera línea por línea
   - Detecta bloques de código (no los modifica)
   - Identifica patrones que necesitan corrección
   - Inserta líneas vacías donde corresponde

4. **Agregado de YAML**
   - Crea encabezado YAML con configuración óptima
   - Incluye soporte para PDF, HTML y Word

5. **Validación final**
   - Verifica que no queden casos pendientes
   - Genera reporte de resultados

## 🛡️ Seguridad

- **Backup automático**: Usa `--backup` para crear copia de seguridad
- **Validación previa**: Usa `--validate-only` para revisar sin modificar
- **Preservación de código**: No modifica bloques de código
- **Encoding UTF-8**: Maneja correctamente caracteres Unicode

## 🐛 Solución de Problemas

### Error: "El archivo no existe"

```bash
❌ Error: El archivo 'docs/archivo.md' no existe
```

**Solución:** Verifica la ruta del archivo

### Advertencia: "Casos aún pendientes"

```bash
⚠️  Advertencia: 3 casos aún pendientes
```

**Solución:** Ejecuta con `--verbose` para ver detalles y corrige manualmente

## 📝 Notas

- El script es **idempotente**: ejecutarlo múltiples veces produce el mismo resultado
- **Preserva el contenido**: solo agrega líneas vacías y encabezado YAML
- **Compatible con Git**: los cambios son fáciles de revisar en diffs

## 🤝 Contribuciones

Para mejorar el script:
1. Agrega nuevos patrones de detección
2. Mejora el algoritmo de validación
3. Agrega más opciones de configuración

## 📄 Licencia

Este script es parte del proyecto BootCamp VirtIA - Semana 05

