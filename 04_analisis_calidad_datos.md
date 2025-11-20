# Bloque 4: Análisis de Calidad de Datos

## 📋 Descripción General

Este bloque es como una **inspección de calidad en una fábrica**. Después de cargar los datos, necesitamos verificar que estén en buen estado: buscar valores faltantes, detectar inconsistencias y corregir problemas antes de continuar con el análisis.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Detectar valores faltantes** (missing values) en el dataset
2. **Identificar anomalías** en los tipos de datos
3. **Investigar el problema de TotalCharges** detectado anteriormente
4. **Limpiar y corregir** los datos problemáticos
5. **Verificar** que los datos estén listos para el análisis

### ¿Por qué es importante?

**Analogía de la cocina**: Imagina que vas a preparar una ensalada. Antes de cocinar, necesitas:
- Revisar que todas las verduras estén frescas (no falten ingredientes)
- Lavar y limpiar lo que esté sucio
- Desechar lo que esté en mal estado

Los datos son igual: necesitan limpieza antes de usarlos.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **Detección de Valores Faltantes**

```python
df.isnull().sum()  # Cuenta valores nulos por columna
```

**¿Qué son valores faltantes?**
- Datos que no existen o no fueron registrados
- En Pandas se representan como `NaN` (Not a Number) o `None`

**Analogía**: Es como tener un formulario donde algunas personas dejaron preguntas en blanco.

**Resultado inicial**: ¡No hay valores `NaN` explícitos! Pero...

---

### 2. **Investigación del Problema de TotalCharges**

El bloque anterior detectó que `TotalCharges` está como texto (object) en vez de número. Este bloque investiga por qué:

```python
df['TotalCharges'].dtype  # Retorna: object
```

**Descubrimiento clave**: Hay **11 registros** con espacios en blanco (' ') en lugar de números.

**Analogía**: Es como encontrar que en 11 formularios, en vez de escribir un número en "Total a pagar", dejaron un espacio vacío.

---

### 3. **Análisis de Registros Problemáticos**

El código examina estos 11 registros:

```python
espacios_blancos = df[df['TotalCharges'] == ' ']
```

**Hallazgo importante**:
- Todos tienen `tenure = 0` (son clientes nuevos, con 0 meses de antigüedad)
- Tienen `MonthlyCharges` pero no `TotalCharges`

**Lógica de negocio**: Si un cliente es nuevo (tenure=0), su cargo total debería ser igual a su cargo mensual (aún no ha pagado más de un mes).

**Analogía**: Si acabas de contratar Netflix hoy, tu pago total hasta ahora es igual a la mensualidad, no más.

---

### 4. **Estrategia de Limpieza**

El bloque implementa una solución en 3 pasos:

#### **Paso 1: Convertir espacios en blanco a NaN**
```python
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
```

**¿Por qué?** Porque Pandas maneja mejor los valores `NaN` que los espacios en blanco.

#### **Paso 2: Convertir a numérico**
```python
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
```

**¿Qué hace `pd.to_numeric()`?**
- Convierte texto a números
- `errors='coerce'` significa: "si no puedes convertir, pon NaN"

**Analogía**: Es como un traductor que convierte palabras a números, y si no puede, deja un espacio en blanco.

#### **Paso 3: Imputar valores faltantes**
```python
df.loc[df['TotalCharges'].isna(), 'TotalCharges'] = \
    df.loc[df['TotalCharges'].isna(), 'MonthlyCharges']
```

**¿Qué significa "imputar"?**
- Rellenar valores faltantes con valores razonables
- En este caso: TotalCharges = MonthlyCharges para clientes nuevos

**Analogía**: Es como completar las respuestas en blanco de un formulario usando lógica (si alguien nació en 2000 y estamos en 2025, tiene ~25 años).

---

### 5. **Verificación Final**

```python
df['TotalCharges'].isna().sum()  # Retorna: 0
df.isnull().sum().sum()          # Retorna: 0
```

**Confirmación**: ✅ Ya no hay valores faltantes en todo el dataset.

---

## 📊 Hallazgos Clave del Análisis de Calidad

### **Problemas Detectados**
1. ⚠️ 11 registros con `TotalCharges` vacío (espacios en blanco)
2. ⚠️ Todos corresponden a clientes nuevos (tenure = 0)
3. ⚠️ `TotalCharges` estaba almacenado como texto en vez de número

### **Soluciones Aplicadas**
1. ✅ Convertir espacios en blanco a NaN
2. ✅ Convertir `TotalCharges` de texto a número (float64)
3. ✅ Imputar valores faltantes usando `MonthlyCharges`
4. ✅ Verificar que no queden valores faltantes

### **Estado Final**
- ✅ 0 valores faltantes en todo el dataset
- ✅ Todos los tipos de datos son correctos
- ✅ Los datos están limpios y listos para análisis

---

## 🔗 Relación con el Análisis General

Este bloque es **crítico** porque:

1. **Datos sucios = Resultados incorrectos**: Si no limpiamos los datos, los modelos aprenderán patrones incorrectos
2. **Previene errores futuros**: Muchas funciones de análisis fallan con valores faltantes
3. **Mejora la calidad del modelo**: Datos limpios = mejores predicciones

**Analogía del edificio**: No puedes construir un edificio sólido sobre cimientos débiles. Los datos limpios son los cimientos del análisis.

---

## 💡 Puntos Clave para Recordar

1. **Valores faltantes** pueden estar ocultos (como espacios en blanco)
2. **Siempre investigar** por qué faltan datos antes de eliminarlos
3. **Imputación inteligente**: Usar lógica de negocio para rellenar valores
4. **Verificación**: Siempre confirmar que la limpieza funcionó
5. **11 registros** fueron corregidos (0.16% del dataset)
6. **TotalCharges** ahora es numérico y completo

---

## 🎓 Conclusión

Este bloque demuestra que la **calidad de datos es fundamental**. Encontramos un problema sutil (espacios en blanco en vez de NaN), lo investigamos, entendimos su causa (clientes nuevos) y aplicamos una solución lógica (igualar a MonthlyCharges).

**Lección importante**: Los datos del mundo real casi nunca están perfectos. La limpieza de datos es una parte esencial (y a menudo la más larga) de cualquier proyecto de ciencia de datos.

**Siguiente paso**: Con los datos limpios, podemos proceder al Análisis Exploratorio de Datos (EDA) para entender patrones y relaciones.

