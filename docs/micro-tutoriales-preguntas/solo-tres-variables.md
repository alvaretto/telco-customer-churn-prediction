## ¿Por qué se analizan solo tres variables numéricas?

Excelente pregunta. Te explico por qué solo aparecen **tres variables numéricas** en las estadísticas descriptivas iniciales:

## 🔍 Razón Principal: Problema con TotalCharges

En el momento de ejecutar `df.describe()` (exploración inicial), el dataset tiene **4 variables que deberían ser numéricas**:

1. ✅ **SeniorCitizen** (int64)
2. ✅ **tenure** (int64) 
3. ✅ **MonthlyCharges** (float64)
4. ❌ **TotalCharges** (object) ← **¡Este es el problema!**

### ¿Por qué TotalCharges no aparece?

**Archivo:** `Telco_Customer_Churn.ipynb`

```python
# TotalCharges aparece como 'object' (texto) en lugar de numérico
TotalCharges         object
```

**TotalCharges está almacenado como texto (`object`)** porque contiene **espacios en blanco** en 11 registros:

**Archivo:** `Telco_Customer_Churn.ipynb`

```python
# Registros con TotalCharges vacío: 11
# Características de registros con TotalCharges vacío:
      customerID  tenure  MonthlyCharges TotalCharges
488   4472-LVYGI       0           52.55
753   3115-CZMZD       0           20.25
```

Cuando pandas encuentra valores no numéricos (espacios en blanco), **interpreta toda la columna como texto**, por lo que `df.describe()` la excluye de las estadísticas.

## ✅ Solución Aplicada

Más adelante en el notebook, se **limpia y convierte TotalCharges a numérico**:

**Archivo:** `Telco_Customer_Churn.ipynb`

```python
# Limpieza de TotalCharges
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
# Imputar valores faltantes con MonthlyCharges (para clientes nuevos)
df.loc[df['TotalCharges'].isna(), 'TotalCharges'] = df.loc[df['TotalCharges'].isna(), 'MonthlyCharges']
```

Después de esta limpieza, **TotalCharges ya aparece en los análisis posteriores** como variable numérica.

## 📊 Resumen

| Variable | Tipo Inicial | ¿Aparece en describe()? | Razón |
|----------|--------------|-------------------------|-------|
| SeniorCitizen | int64 | ✅ Sí | Numérica válida |
| tenure | int64 | ✅ Sí | Numérica válida |
| MonthlyCharges | float64 | ✅ Sí | Numérica válida |
| TotalCharges | **object** | ❌ No | Contiene espacios en blanco |

Esta es una **situación común en análisis de datos reales**: los datos vienen "sucios" y requieren limpieza antes de poder analizarlos correctamente. 🧹
