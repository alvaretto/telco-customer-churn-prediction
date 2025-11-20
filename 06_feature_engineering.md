# Bloque 6: Feature Engineering

## 📋 Descripción General

Este bloque es como **un chef que combina ingredientes básicos para crear nuevos sabores**. Tomamos las variables existentes y creamos nuevas características (features) que pueden ayudar a los modelos a predecir mejor el churn.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Crear nuevas variables** derivadas de las existentes
2. **Capturar relaciones complejas** que no son obvias en los datos originales
3. **Mejorar el poder predictivo** del modelo
4. **Simplificar información** agrupando variables relacionadas

### ¿Por qué es importante?

**Analogía del detective**: Un detective no solo mira las pistas individuales, sino que las combina para formar una imagen completa. Por ejemplo:
- Pista 1: Huellas en la puerta
- Pista 2: Ventana rota
- **Nueva pista combinada**: Entrada forzada

De la misma manera, combinamos variables para crear información más útil.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **Creación de Variables Derivadas**

El bloque crea varias nuevas características:

#### **A) Promedio de Cargo Mensual por Mes de Antigüedad**

```python
df_fe['AvgChargesPerMonth'] = df_fe['TotalCharges'] / (df_fe['tenure'] + 1)
```

**¿Qué mide?**
- Cuánto paga el cliente en promedio por mes
- El `+1` evita división por cero para clientes nuevos

**¿Por qué es útil?**
- Captura si el cliente ha tenido aumentos o descuentos a lo largo del tiempo
- Normaliza el gasto por la antigüedad

**Analogía**: Es como calcular tu gasto promedio mensual en café dividiendo lo que has gastado en total entre los meses que llevas comprando.

---

#### **B) Número Total de Servicios Contratados**

```python
services = ['PhoneService', 'InternetService', 'OnlineSecurity', 
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 
            'StreamingTV', 'StreamingMovies']
df_fe['TotalServices'] = (df_fe[services] != 'No').sum(axis=1)
```

**¿Qué mide?**
- Cuenta cuántos servicios tiene contratados el cliente (de 0 a 8)

**¿Por qué es útil?**
- El EDA mostró que clientes con más servicios tienen menos churn
- Resume 8 variables en una sola métrica

**Analogía**: Es como contar cuántos extras pediste en tu hamburguesa (queso, tocino, aguacate, etc.). Más extras = más comprometido con el restaurante.

---

#### **C) Indicador de Cliente Premium**

```python
df_fe['IsPremium'] = ((df_fe['MonthlyCharges'] > df_fe['MonthlyCharges'].median()) & 
                       (df_fe['TotalServices'] >= 3)).astype(int)
```

**¿Qué mide?**
- Si el cliente paga más que la mediana Y tiene 3+ servicios
- Valor: 1 (premium) o 0 (no premium)

**¿Por qué es útil?**
- Identifica clientes de alto valor
- Combina dos dimensiones: gasto y uso de servicios

**Analogía**: Como identificar clientes VIP en un hotel (gastan mucho Y usan muchos servicios).

---

#### **D) Categorías de Antigüedad (Tenure Groups)**

```python
df_fe['TenureGroup'] = pd.cut(df_fe['tenure'], 
                               bins=[0, 12, 24, 48, 72],
                               labels=['0-1 year', '1-2 years', '2-4 years', '4+ years'])
```

**¿Qué hace `pd.cut()`?**
- Divide una variable continua en categorías (bins)
- Como poner edades en grupos: niño, adolescente, adulto, anciano

**Categorías creadas**:
- **0-1 year**: Clientes nuevos (alto riesgo de churn)
- **1-2 years**: Clientes establecidos
- **2-4 years**: Clientes leales
- **4+ years**: Clientes muy leales (bajo riesgo)

**¿Por qué es útil?**
- Los modelos pueden capturar mejor relaciones no lineales
- Refleja que el riesgo de churn no disminuye uniformemente con el tiempo

**Analogía**: Como clasificar estudiantes por año (freshman, sophomore, junior, senior) en vez de solo por edad.

---

#### **E) Indicador de Contrato Flexible**

```python
df_fe['HasFlexibleContract'] = (df_fe['Contract'] == 'Month-to-month').astype(int)
```

**¿Qué mide?**
- Si el cliente tiene contrato mes a mes (1) o no (0)

**¿Por qué es útil?**
- El EDA mostró que contratos mes a mes tienen ~42% de churn
- Simplifica la variable Contract en un indicador binario de riesgo

**Analogía**: Como marcar si alguien tiene un trabajo temporal vs. permanente.

---

#### **F) Ratio de Servicios de Seguridad**

```python
security_services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport']
df_fe['SecurityServicesRatio'] = (df_fe[security_services] != 'No').sum(axis=1) / len(security_services)
```

**¿Qué mide?**
- Proporción de servicios de seguridad contratados (0 a 1)
- 0 = ninguno, 0.5 = mitad, 1 = todos

**¿Por qué es útil?**
- Los servicios de seguridad están asociados con menor churn
- Normaliza el conteo en una escala de 0 a 1

**Analogía**: Como medir qué tan protegida está tu casa (alarma, cámaras, cerraduras, perro guardián) en una escala de 0% a 100%.

---

### 2. **Transformaciones de Variables Existentes**

#### **Codificación de Variables Binarias**

```python
df_fe['gender'] = df_fe['gender'].map({'Male': 1, 'Female': 0})
df_fe['Partner'] = df_fe['Partner'].map({'Yes': 1, 'No': 0})
```

**¿Por qué convertir a números?**
- Los modelos de Machine Learning solo entienden números
- Yes/No → 1/0 es más eficiente que crear columnas dummy

---

## 📊 Resumen de Nuevas Features Creadas

| Feature | Tipo | Descripción | Utilidad |
|---------|------|-------------|----------|
| `AvgChargesPerMonth` | Numérica | Cargo promedio por mes | Detecta cambios en precios |
| `TotalServices` | Numérica | Cantidad de servicios | Mide engagement del cliente |
| `IsPremium` | Binaria | Cliente de alto valor | Segmentación |
| `TenureGroup` | Categórica | Grupo de antigüedad | Captura no-linealidad |
| `HasFlexibleContract` | Binaria | Contrato mes a mes | Indicador de riesgo |
| `SecurityServicesRatio` | Numérica | Proporción de servicios de seguridad | Mide protección |

---

## 🔗 Relación con el Análisis General

El Feature Engineering es el **puente entre el análisis y el modelado**:

1. **Usa insights del EDA**: Las features se basan en hallazgos del análisis exploratorio
2. **Prepara para el modelado**: Crea variables que los modelos pueden usar efectivamente
3. **Mejora el rendimiento**: Features bien diseñadas = mejores predicciones
4. **Reduce dimensionalidad**: Combina múltiples variables en métricas significativas

---

## 💡 Puntos Clave para Recordar

1. **Feature Engineering es un arte Y una ciencia**: Requiere creatividad y conocimiento del dominio
2. **Basado en insights**: Cada feature nueva debe tener una justificación lógica
3. **6 nuevas features** creadas a partir de las originales
4. **Combinación de enfoques**: Agregación, categorización, ratios, indicadores binarios
5. **Mejora interpretabilidad**: Features como `IsPremium` son fáciles de entender para el negocio

---

## 🎓 Conclusión

El Feature Engineering transforma datos crudos en información accionable. No solo creamos variables nuevas, sino que capturamos **conocimiento del negocio** en forma de features que los modelos pueden usar.

**Ejemplo de impacto**: En vez de que el modelo aprenda por sí solo que "contratos mes a mes + tenure bajo = alto riesgo", le damos directamente `HasFlexibleContract` y `TenureGroup` para facilitar su trabajo.

**Siguiente paso**: Preparar los datos para el modelado (división train/test, normalización, encoding).

