# Bloque 5: Análisis Exploratorio de Datos (EDA)

## 📋 Descripción General

Este bloque es como **ser un detective que investiga un caso**. Ahora que los 
datos están limpios, exploramos en profundidad para descubrir patrones, tendencias 
y relaciones que nos ayuden a entender por qué los clientes abandonan el servicio.

---

## 🎯 Propósito y Objetivo

Los objetivos principales de este bloque son:

1. **Analizar la variable objetivo (Churn)**: ¿Cuántos clientes se van vs. se quedan?
2. **Explorar variables categóricas**: ¿Qué características tienen los clientes que se van?
3. **Analizar variables numéricas**: ¿Hay diferencias en cargos o antigüedad?
4. **Estudiar correlaciones**: ¿Qué variables están relacionadas entre sí?
5. **Generar visualizaciones** que cuenten la historia de los datos

### ¿Por qué es importante?

**Analogía del médico**: Antes de recetar un tratamiento, el médico necesita:

- Entender los síntomas
- Identificar patrones
- Buscar causas subyacentes

El EDA es el "diagnóstico" que nos permite entender el problema antes de construir modelos.

---

## 🔑 Conceptos Clave y Técnicas Utilizadas

### 1. **Análisis de la Variable Objetivo: Churn**

**Distribución de Churn**:
- **No** (se quedaron): ~73% de los clientes
- **Yes** (se fueron): ~27% de los clientes

**¿Qué significa esto?**

**Analogía del restaurante**: De cada 100 clientes que entran, 27 no vuelven nunca. Eso es un problema serio que cuesta dinero.

**Implicación importante**: Hay **desbalanceo de clases**

- Más clientes se quedan que se van
- Esto puede afectar el entrenamiento de modelos (los modelos tienden a predecir la clase mayoritaria)

---

### 2. **Análisis de Variables Categóricas**

El bloque examina cómo diferentes características se relacionan con el churn:

#### **Género (Gender)**

- **Hallazgo**: El churn es similar entre hombres y mujeres
- **Conclusión**: El género NO es un factor determinante

#### **Adultos Mayores (SeniorCitizen)**

- **Hallazgo**: Los adultos mayores tienen MAYOR tasa de churn
- **Analogía**: Como si los clientes mayores fueran más propensos a cambiar de proveedor

#### **Tipo de Contrato (Contract)**

- **Hallazgo clave**: 

  - Contratos mes a mes: ALTA tasa de churn (~42%)
  - Contratos de 1 año: Churn moderado (~11%)
  - Contratos de 2 años: BAJA tasa de churn (~3%)

**Analogía del gimnasio**: Las personas con membresía mensual cancelan más fácilmente que las que pagaron por todo el año.

**Insight de negocio**: ¡Ofrecer contratos largos reduce significativamente el churn!

#### **Servicio de Internet (InternetService)**

- **Hallazgo**: Clientes con Fibra Óptica tienen MAYOR churn que DSL
- **Posible razón**: Fibra óptica es más cara, los clientes son más sensibles al precio

#### **Servicios Adicionales**

- **OnlineSecurity, TechSupport, OnlineBackup**: Los clientes SIN estos servicios tienen mayor churn
- **Analogía**: Es como tener un seguro completo vs. básico; el completo te hace sentir más protegido y menos propenso a cambiar

---

### 3. **Análisis de Variables Numéricas**

#### **Tenure (Antigüedad en meses)**

- **Clientes que se van**: Promedio de ~18 meses
- **Clientes que se quedan**: Promedio de ~38 meses

**Hallazgo crítico**: Los clientes nuevos son MÁS propensos a irse.

**Analogía**: Es como una relación: los primeros meses son críticos. Si sobrevives el primer año, es más probable que dures mucho tiempo.

#### **MonthlyCharges (Cargos Mensuales)**

- **Clientes que se van**: Pagan MÁS en promedio (~$75)
- **Clientes que se quedan**: Pagan MENOS en promedio (~$61)

**Insight**: El precio alto es un factor de riesgo para el churn.

#### **TotalCharges (Cargos Totales)**

- **Clientes que se van**: Han pagado MENOS en total
- **Razón**: Tienen menos antigüedad (tenure bajo)

---

### 4. **Análisis de Correlaciones**

El bloque crea una **matriz de correlación** que muestra cómo las variables se relacionan entre sí.

**¿Qué es correlación?**

- Mide si dos variables se mueven juntas
- Valores de -1 a +1:

  - **+1**: Correlación positiva perfecta (si una sube, la otra también)
  - **0**: No hay relación
  - **-1**: Correlación negativa perfecta (si una sube, la otra baja)

**Correlaciones importantes encontradas**:

1. **TotalCharges ↔ Tenure**: +0.83 (fuerte positiva)
   - **Lógica**: Más tiempo como cliente = más has pagado en total

2. **MonthlyCharges ↔ TotalCharges**: +0.65 (moderada positiva)
   - **Lógica**: Si pagas más al mes, pagas más en total

3. **Churn ↔ Tenure**: Negativa
   - **Lógica**: Más antigüedad = menos probabilidad de irse

4. **Churn ↔ MonthlyCharges**: Positiva
   - **Lógica**: Más caro = más probabilidad de irse

---

## 📊 Visualizaciones Clave

El bloque crea varios tipos de gráficos:

### **1. Gráficos de Barras**

- Comparan churn entre diferentes categorías
- **Ejemplo**: Churn por tipo de contrato

### **2. Histogramas**

- Muestran distribuciones de variables numéricas
- **Ejemplo**: Distribución de tenure para clientes que se van vs. se quedan

### **3. Box Plots (Diagramas de Caja)**

- Muestran la distribución, mediana y valores atípicos
- **Ejemplo**: MonthlyCharges para cada grupo de churn

### **4. Heatmap de Correlación**

- Matriz de colores que muestra correlaciones
- Colores cálidos (rojo) = correlación alta
- Colores fríos (azul) = correlación baja

**Analogía**: Es como un mapa de calor que muestra qué variables están "conectadas".

---

## 🔗 Relación con el Análisis General

El EDA es **fundamental** porque:

1. **Genera hipótesis**: Descubrimos que contratos largos reducen churn
2. **Identifica variables importantes**: Tenure, MonthlyCharges, Contract son clave
3. **Detecta problemas**: Desbalanceo de clases que necesitaremos manejar
4. **Informa decisiones**: Qué variables incluir en el modelo
5. **Comunica insights**: Las visualizaciones cuentan la historia a stakeholders

---

## 💡 Puntos Clave para Recordar

1. **27% de churn** - Problema significativo de negocio
2. **Desbalanceo de clases**: 73% No, 27% Yes
3. **Factores de riesgo de churn**:

   - Contratos mes a mes
   - Clientes nuevos (tenure bajo)
   - Cargos mensuales altos
   - Sin servicios adicionales (seguridad, soporte)
   - Fibra óptica (más cara)
4. **Factores protectores**:

   - Contratos largos (1-2 años)
   - Mayor antigüedad
   - Servicios adicionales contratados
5. **Correlaciones importantes**: Tenure y MonthlyCharges son predictores clave

---

---

## 🔬 Comprobación de Hipótesis Estadísticas

### ¿Qué es?

Después del análisis exploratorio visual, realizamos **pruebas estadísticas formales** para validar las relaciones observadas.

**Analogía del juicio**: En un juicio, no basta con "creer" que alguien es culpable. Necesitas **evidencia estadística** que demuestre la culpabilidad más allá de una duda razonable.

### Pruebas Realizadas

El notebook incluye **7 pruebas de hipótesis** con nivel de significancia α = 0.05:

#### 1. **Tipo de Contrato vs Churn** (Chi-cuadrado)
- **H₀**: El contrato NO está asociado con el churn
- **H₁**: El contrato SÍ está asociado con el churn
- **Resultado**: ✅ Rechazamos H₀ (p-value < 0.05)
- **Conclusión**: El tipo de contrato SÍ está significativamente asociado con el churn

#### 2. **Método de Pago vs Churn** (Chi-cuadrado)
- **H₀**: El método de pago NO está asociado con el churn
- **H₁**: El método de pago SÍ está asociado con el churn
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: El método de pago SÍ está significativamente asociado con el churn

#### 3. **Servicio de Internet vs Churn** (Chi-cuadrado)
- **H₀**: El servicio de internet NO está asociado con el churn
- **H₁**: El servicio de internet SÍ está asociado con el churn
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: El tipo de internet SÍ está significativamente asociado con el churn

#### 4. **Antigüedad (Tenure) vs Churn** (Mann-Whitney U)
- **H₀**: La antigüedad promedio es igual entre grupos
- **H₁**: La antigüedad promedio es diferente entre grupos
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: Los clientes que NO abandonan tienen significativamente más antigüedad

#### 5. **Cargos Mensuales vs Churn** (Mann-Whitney U)
- **H₀**: Los cargos mensuales son iguales entre grupos
- **H₁**: Los cargos mensuales son diferentes entre grupos
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: Los clientes que SÍ abandonan pagan significativamente más al mes

#### 6. **Soporte Técnico vs Churn** (Chi-cuadrado)
- **H₀**: El soporte técnico NO está asociado con el churn
- **H₁**: El soporte técnico SÍ está asociado con el churn
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: Tener soporte técnico SÍ está significativamente asociado con menor churn

#### 7. **Facturación sin Papel vs Churn** (Chi-cuadrado)
- **H₀**: La facturación sin papel NO está asociada con el churn
- **H₁**: La facturación sin papel SÍ está asociada con el churn
- **Resultado**: ✅ Rechazamos H₀
- **Conclusión**: La facturación sin papel SÍ está significativamente asociada con el churn

### ¿Qué significa p-value < 0.05?

**Analogía del dado trucado**: Si lanzas un dado 100 veces y sale 6 en 90 ocasiones, ¿es casualidad o está trucado?

- **p-value < 0.05** significa que hay menos del 5% de probabilidad de que la relación sea por casualidad
- Es decir, tenemos **95% de confianza** de que la relación es real

### Implicaciones para el Modelo

Las variables que mostraron asociaciones significativas son **candidatas importantes** para el modelo de predicción:

1. ✅ **Contract** - Fuerte predictor
2. ✅ **PaymentMethod** - Fuerte predictor
3. ✅ **InternetService** - Fuerte predictor
4. ✅ **tenure** - Fuerte predictor
5. ✅ **MonthlyCharges** - Fuerte predictor
6. ✅ **TechSupport** - Predictor moderado
7. ✅ **PaperlessBilling** - Predictor moderado

Estas pruebas **validan estadísticamente** lo que observamos en el EDA visual.

---

## 🎓 Conclusión

El EDA revela la **historia detrás de los números**: los clientes se van
principalmente por precios altos y falta de compromiso (contratos cortos).
Los clientes leales tienen contratos largos, servicios adicionales y llevan más
tiempo con la empresa.

Las **pruebas de hipótesis estadísticas** confirman que estas relaciones NO son casualidad,
sino que tienen **significancia estadística** (p-value < 0.05).

Estos insights no solo nos ayudan a construir mejores modelos, sino que también
sugieren **estrategias de negocio**:

- Incentivar contratos largos
- Ofrecer descuentos en servicios adicionales
- Programas de retención para clientes nuevos
- Mejorar soporte técnico
- Revisar estrategia de facturación electrónica

**Siguiente paso**: Feature Engineering - crear nuevas variables basadas en estos insights validados estadísticamente.

