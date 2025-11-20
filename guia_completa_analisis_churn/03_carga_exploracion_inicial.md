# Bloque 3: Carga y Exploración Inicial de Datos

## 📋 Descripción General

Este bloque es el **primer contacto real con los datos**. Es como abrir una caja misteriosa para ver qué hay dentro. Aquí cargamos el archivo CSV con la información de los clientes y hacemos una inspección inicial para entender su estructura, tamaño y contenido.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Cargar el dataset** desde el archivo CSV de manera robusta
2. **Verificar las dimensiones** (cuántas filas y columnas tiene)
3. **Inspeccionar las primeras filas** para ver cómo lucen los datos
4. **Identificar los tipos de datos** de cada columna
5. **Obtener estadísticas descriptivas** básicas

### ¿Por qué es importante?

**Analogía del médico**: Antes de diagnosticar a un paciente, el médico necesita:
- Conocer sus datos básicos (edad, peso, altura)
- Ver su historial médico
- Hacer un examen físico inicial

De la misma manera, antes de analizar los datos, necesitamos conocerlos, verlos y entender su estructura básica.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **Función `cargar_datos()` - Carga Robusta**

El código crea una función personalizada que intenta cargar el archivo desde múltiples ubicaciones posibles.

**¿Por qué hacer esto?**

**Analogía**: Es como buscar tus llaves en varios lugares donde podrían estar (bolsillo, mesa, bolso) en vez de asumir que están en un solo lugar.

**Beneficios**:

- Funciona en diferentes entornos (Google Colab, local, servidor)
- Evita errores por rutas incorrectas
- Hace el código más portable y robusto

### 2. **Carga del CSV con Pandas**

`pd.read_csv()` lee el archivo CSV y lo convierte en un DataFrame de Pandas.

**Analogía**: Es como escanear un documento físico y convertirlo en un archivo digital que puedes editar.

### 3. **Inspección de Dimensiones**

**Resultado**: `(7043, 21)`
- **7,043 filas** = 7,043 clientes
- **21 columnas** = 21 variables por cliente

**Analogía**: Es como saber que tienes un álbum de fotos con 7,043 páginas y cada página tiene 21 datos diferentes.

### 4. **Tipos de Datos (`dtypes`)**

**Tipos principales encontrados**:
- **object**: Texto (categorías como "Yes", "No", "Male", "Female")
- **int64**: Números enteros (como tenure: 1, 2, 34, 45)
- **float64**: Números decimales (como MonthlyCharges: 29.85, 56.95)

**Observación importante**: `TotalCharges` aparece como **object** (texto) cuando debería ser numérico. ¡Esto es una señal de alerta!

### 5. **Estadísticas Descriptivas (`df.describe()`)**

Para variables numéricas, calcula:

- **count**: Cantidad de valores
- **mean**: Promedio
- **std**: Desviación estándar
- **min/max**: Valores mínimo y máximo
- **25%, 50%, 75%**: Cuartiles

**Ejemplo con `tenure` (meses como cliente)**:

- **Promedio**: 32.37 meses (~2.7 años)
- **Mínimo**: 0 meses (clientes nuevos)
- **Máximo**: 72 meses (6 años)

---

## 📊 Hallazgos Clave de la Exploración Inicial

### **Dimensiones del Dataset**
- ✅ 7,043 clientes
- ✅ 21 variables
- ✅ Tamaño manejable para análisis

### **Tipos de Variables**

1. **Variables Demográficas**:
   - `gender`: Género (Male/Female)
   - `SeniorCitizen`: Si es adulto mayor (0/1)
   - `Partner`: Tiene pareja (Yes/No)
   - `Dependents`: Tiene dependientes (Yes/No)

2. **Variables de Servicio**:
   - `PhoneService`: Servicio telefónico
   - `InternetService`: Tipo de internet (DSL/Fiber optic/No)
   - Servicios adicionales: OnlineSecurity, OnlineBackup, etc.

3. **Variables de Cuenta**:
   - `tenure`: Meses como cliente
   - `Contract`: Tipo de contrato
   - `PaymentMethod`: Método de pago
   - `MonthlyCharges`: Cargo mensual
   - `TotalCharges`: Cargo total

4. **Variable Objetivo**:
   - `Churn`: Si el cliente se fue (Yes/No)

### **Problema Detectado**
- ⚠️ `TotalCharges` está como texto (object) en vez de número
- Esto indica que hay valores no numéricos que necesitaremos investigar y limpiar

---

## 🔗 Relación con el Análisis General

Este bloque es el **punto de partida del análisis de datos**:

1. **Confirma que tenemos los datos** correctamente cargados
2. **Identifica la estructura** que trabajaremos
3. **Detecta problemas iniciales** (como TotalCharges)
4. **Establece el contexto** para la limpieza y análisis posterior

---

## 💡 Puntos Clave para Recordar

1. **Carga robusta**: El código busca el archivo en múltiples ubicaciones
2. **7,043 clientes** con **21 variables** cada uno
3. **Tres tipos de datos**: object (texto), int64 (enteros), float64 (decimales)
4. **Problema detectado**: TotalCharges debería ser numérico pero está como texto
5. **Estadísticas iniciales**: Los clientes tienen en promedio 32 meses de antigüedad

---

## 🎓 Conclusión

Este bloque es como el **reconocimiento del terreno** antes de construir. Nos da una visión panorámica de los datos: qué tenemos, cómo está estructurado y qué problemas potenciales existen.

**Siguiente paso**: Analizar la calidad de los datos en profundidad y detectar valores faltantes o inconsistencias.

