## 📚 ¿Qué es la Imputación?

**Imputación** es el proceso de **rellenar valores faltantes** (missing values) en un dataset con valores razonables, en lugar de simplemente eliminar los registros incompletos.

### 🎯 Definición Simple

> **Imputar = Completar espacios en blanco con valores lógicos**

## 🔍 Proceso de Imputación en Nuestro Notebook

En el archivo `Telco_Customer_Churn.ipynb`, la imputación se realiza en **3 pasos**:

### **Paso 1: Detectar el Problema**

Primero se identifican los valores faltantes:

```python
# Detectar espacios en blanco en TotalCharges
espacios_blancos = df[df['TotalCharges'] == ' ']
print(f"Registros con TotalCharges vacío: {len(espacios_blancos)}")
```

**Resultado:** 11 registros con TotalCharges vacío

### **Paso 2: Convertir a NaN**

Se convierten los espacios en blanco a `NaN` (Not a Number), que es el formato estándar de pandas para valores faltantes:

```python
# Convertir espacios en blanco a NaN
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)

# Convertir a numérico
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
```

**Estado:** Ahora tenemos 11 valores `NaN` en TotalCharges

### **Paso 3: Imputar (Rellenar) los Valores Faltantes**

Aquí es donde ocurre la **imputación**:

```python
# Estrategia: Para clientes nuevos (tenure=0), TotalCharges debería ser igual a MonthlyCharges
df.loc[df['TotalCharges'].isna(), 'TotalCharges'] = df.loc[df['TotalCharges'].isna(), 'MonthlyCharges']

print(f"Después de la imputación:")
print(f"Registros con TotalCharges NaN: {df['TotalCharges'].isna().sum()}")
```

**Resultado:** 0 valores faltantes (todos fueron imputados)

## 📊 Ejemplo Concreto

Veamos cómo funciona con un registro real:

### **ANTES de la imputación:**
```
customerID: 4472-LVYGI
tenure: 0
MonthlyCharges: 52.55
TotalCharges: [VACÍO/NaN]
```

### **DESPUÉS de la imputación:**
```
customerID: 4472-LVYGI
tenure: 0
MonthlyCharges: 52.55
TotalCharges: 52.55  ← ¡Imputado!
```

**Lógica aplicada:** Como `tenure = 0` (cliente nuevo), `TotalCharges = MonthlyCharges`

## 🎨 Analogías para Entender la Imputación

### **Analogía 1: Formulario Incompleto**

Imagina que tienes un formulario donde alguien escribió:

- Fecha de nacimiento: 2000
- Edad: [EN BLANCO]

**Imputación:** Calculas la edad usando la fecha de nacimiento (2025 - 2000 = 25 años)

### **Analogía 2: Factura de Netflix**

Si acabas de contratar Netflix hoy:

- Cargo mensual: $15
- Total pagado hasta ahora: [EN BLANCO]

**Imputación:** Como es tu primer mes, el total pagado = $15 (igual al cargo mensual)

### **Analogía 3: Completar un Puzzle**

Tienes un puzzle con una pieza faltante. En lugar de tirar todo el puzzle (eliminar el registro), **creas una pieza que encaje lógicamente** (imputación).

## 🔧 Tipos de Imputación

Existen diferentes estrategias de imputación:

| Estrategia | Descripción | Ejemplo en nuestro caso |
|------------|-------------|-------------------------|
| **Por media** | Rellenar con el promedio | ❌ No usada (no tiene sentido lógico) |
| **Por mediana** | Rellenar con la mediana | ❌ No usada (no tiene sentido lógico) |
| **Por moda** | Rellenar con el valor más frecuente | ❌ No usada (no tiene sentido lógico) |
| **Por lógica de negocio** | Rellenar usando reglas del dominio | ✅ **USADA**: TotalCharges = MonthlyCharges para tenure=0 |

## ✅ ¿Por Qué Esta Estrategia de Imputación es Correcta?

La imputación en nuestro notebook es **inteligente** porque:

1. ✅ **Usa lógica de negocio**: Para clientes nuevos, TotalCharges = MonthlyCharges
2. ✅ **Preserva la relación matemática**: TotalCharges ≈ MonthlyCharges × tenure
3. ✅ **No introduce sesgos**: No usa promedios arbitrarios
4. ✅ **Mantiene la integridad**: Los datos siguen siendo coherentes

## 🚫 Alternativas Descartadas

### **Opción 1: Eliminar los 11 registros**
❌ **Problema:** Perderíamos información valiosa de clientes nuevos

### **Opción 2: Imputar con la media de TotalCharges**
❌ **Problema:** La media es ~$2,283, pero estos clientes son nuevos (tenure=0), por lo que no tiene sentido que tengan cargos tan altos

### **Opción 3: Dejar los valores vacíos**
❌ **Problema:** Los modelos de Machine Learning no pueden trabajar con valores faltantes

## 📈 Verificación Final

Después de la imputación, se verifica que todo esté correcto:

```python
# Verificar que no hay valores faltantes
print(f"Total de valores faltantes en el dataset: {df.isnull().sum().sum()}")
```

**Resultado:** 0 valores faltantes ✅

## 🎓 Conclusión

**Imputación** es el proceso de **completar valores faltantes de manera inteligente**, usando lógica de negocio en lugar de simplemente eliminar datos o usar promedios arbitrarios.

En nuestro caso:

- 🔍 **Detectamos:** 11 registros con TotalCharges vacío
- 🧠 **Analizamos:** Todos tienen tenure=0 (clientes nuevos)
- ✅ **Imputamos:** TotalCharges = MonthlyCharges (lógica de negocio)
- 🎯 **Resultado:** Dataset completo y coherente

Esta es una práctica estándar en **Data Science** y es fundamental para mantener la calidad de los datos antes de entrenar modelos de Machine Learning. 📊✨
