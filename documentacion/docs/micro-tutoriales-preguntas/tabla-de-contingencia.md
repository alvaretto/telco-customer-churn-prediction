En el contexto de tu notebook `Telco_Customer_Churn.ipynb`, una **tabla de contingencia** es una herramienta estadística que muestra la frecuencia de observaciones para dos variables categóricas simultáneamente.

## ¿Cómo se usa en tu proyecto?

En tu análisis, las tablas de contingencia se crean con `pd.crosstab()` para analizar la relación entre variables categóricas y el **Churn** (abandono de clientes). Por ejemplo:

```python
# Crear tabla de contingencia
ct = pd.crosstab(df[col], df['Churn'], normalize='index') * 100
```

## Ejemplo concreto del notebook:

Para la variable **Contract** (tipo de contrato), la tabla de contingencia muestra:

```python
# Tabla de contingencia
contingency_table = pd.crosstab(df['Contract'], df['Churn'])
print("\nTabla de Contingencia:")
print(contingency_table)
```

Esto genera una tabla como:

```
Churn              No   Yes
Contract                    
Month-to-month   2220  1655
One year          1307   166
Two year          1647    48
```

## ¿Para qué sirve?

1. **Visualizar relaciones**: Permite ver cómo se distribuyen los clientes que abandonan (Churn=Yes) vs los que se quedan (Churn=No) según diferentes categorías

2. **Pruebas estadísticas**: Se usa como entrada para la **prueba Chi-cuadrado** (`chi2_contingency`), que determina si existe una asociación estadísticamente significativa entre las variables

3. **Análisis de tasas**: Cuando se normaliza (`normalize='index'`), muestra el porcentaje de churn dentro de cada categoría

En resumen, las tablas de contingencia son fundamentales en tu análisis para identificar qué factores (tipo de contrato, método de pago, servicio de internet, etc.) están asociados con el abandono de clientes.
