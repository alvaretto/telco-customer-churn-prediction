# 🚀 Scripts de Formateo de Markdown

## 📖 Bienvenido

Esta carpeta contiene scripts Python para formatear automáticamente archivos Markdown.

---

## 📂 Orden de Lectura (Secuencial)

Los archivos están numerados para facilitar su lectura:

### 📚 Documentación

1. **00_INICIO.md** ← Estás aquí (guía rápida de inicio)
2. **01_README.md** - Documentación completa de todos los scripts
3. **02_EJEMPLO_USO.md** - Tutorial paso a paso con ejemplos prácticos

### 🛠️ Scripts Python

3. **03_verify_markdown_format.py** - Verificar formato (sin modificar)
4. **04_format_markdown_complete.py** - ⭐ **PRINCIPAL** - Formateo completo
5. **05_fix_markdown_format.py** - Corregir solo listas
6. **06_add_yaml_header.py** - Agregar solo encabezado YAML

---

## ⚡ Inicio Rápido

### Opción 1: Formateo Completo (RECOMENDADO)

```bash
# Formatear un documento con título automático
python scripts/fix-markdown/04_format_markdown_complete.py docs/mi_documento.md --auto-title
```

### Opción 2: Solo Verificar

```bash
# Verificar sin modificar
python scripts/fix-markdown/03_verify_markdown_format.py docs/mi_documento.md
```

---

## 🎯 ¿Qué Hacen Estos Scripts?

### ✅ Correcciones que Aplican:

1. **Agregan encabezado YAML** con configuración xelatex (soporte de emojis)
2. **Insertan líneas vacías** entre líneas que terminan con `:` y listas con viñetas
3. **Preservan bloques de código** intactos
4. **Generan reportes** detallados de cambios

### 📋 Ejemplo de Corrección:

**ANTES:**
```markdown
Los requisitos son:
- Python 3.8+
- Flask
```

**DESPUÉS:**
```markdown
Los requisitos son:

- Python 3.8+
- Flask
```

---

## 📊 ¿Qué Script Usar?

| Necesitas... | Usa este script |
|-------------|-----------------|
| Formatear todo automáticamente | `04_format_markdown_complete.py` ⭐ |
| Solo verificar sin modificar | `03_verify_markdown_format.py` |
| Solo corregir listas | `05_fix_markdown_format.py` |
| Solo agregar YAML header | `06_add_yaml_header.py` |

---

## 🔍 Próximos Pasos

1. **Lee la documentación completa**: `01_README.md`
2. **Revisa los ejemplos**: `02_EJEMPLO_USO.md`
3. **Prueba con tus documentos**: Usa `04_format_markdown_complete.py`

---

## 💡 Consejo Rápido

Para la mayoría de casos, simplemente ejecuta:

```bash
python scripts/fix-markdown/04_format_markdown_complete.py tu_documento.md --auto-title
```

¡Y listo! Tu documento estará formateado correctamente. ✨

---

## 📞 Ayuda

Si necesitas ayuda con algún script, ejecuta:

```bash
python scripts/fix-markdown/04_format_markdown_complete.py
```

Sin argumentos, mostrará la ayuda completa.

---

## ✅ Características

- 🔄 **Reutilizables** - Funcionan con cualquier archivo Markdown
- 🛡️ **Seguros** - Preservan bloques de código
- 📊 **Informativos** - Reportes detallados
- 🌍 **Unicode** - Soporte completo de emojis
- 🚀 **Fáciles** - Sintaxis simple

---

**¡Comienza ahora!** Lee `01_README.md` para más detalles. 📚

