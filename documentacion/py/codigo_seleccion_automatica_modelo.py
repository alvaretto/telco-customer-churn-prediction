"""
CÓDIGO PARA SELECCIÓN AUTOMÁTICA DEL MEJOR MODELO
==================================================

Este archivo contiene el código que debes agregar al notebook
Telco_Customer_Churn.ipynb para implementar la selección automática
del mejor modelo según ROC-AUC.

INSTRUCCIONES:
1. Abre el notebook en Google Colab
2. Busca la celda donde se muestra el resumen de resultados con SMOTE
3. Agrega una NUEVA CELDA después de esa
4. Copia y pega el CÓDIGO 1 en esa nueva celda
5. Busca la celda donde se optimiza Random Forest (línea ~3400)
6. REEMPLAZA esa celda con el CÓDIGO 2
"""

# ============================================================================
# CÓDIGO 1: SELECCIÓN AUTOMÁTICA DEL MEJOR MODELO
# ============================================================================
# Agregar DESPUÉS de mostrar el resumen de resultados con SMOTE

# Seleccionar automáticamente el mejor modelo según ROC-AUC
best_model_name = results_balanced_df.iloc[0]['Modelo']
best_model_roc_auc = results_balanced_df.iloc[0]['ROC-AUC']

print("\n" + "="*80)
print("\n🏆 MEJOR MODELO SEGÚN COMPARATIVA:")
print(f"   • Modelo: {best_model_name}")
print(f"   • ROC-AUC: {best_model_roc_auc:.4f}")
print("\n" + "="*80)


# ============================================================================
# CÓDIGO 2: OPTIMIZACIÓN DINÁMICA SEGÚN EL MODELO GANADOR
# ============================================================================
# REEMPLAZAR la celda de optimización de Random Forest con este código

import numpy as np
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb

# Definir espacios de hiperparámetros para cada modelo
param_distributions = {
    'Random Forest': {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'max_features': ['sqrt', 'log2'],
        'bootstrap': [True, False]
    },
    'Logistic Regression': {
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'penalty': ['l1', 'l2'],
        'solver': ['liblinear', 'saga'],
        'max_iter': [1000, 2000]
    },
    'Gradient Boosting': {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 7],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'subsample': [0.8, 0.9, 1.0]
    },
    'XGBoost': {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 7],
        'min_child_weight': [1, 3, 5],
        'subsample': [0.8, 0.9, 1.0],
        'colsample_bytree': [0.8, 0.9, 1.0]
    }
}

# Crear instancia del modelo ganador
models_dict = {
    'Random Forest': RandomForestClassifier(random_state=RANDOM_STATE),
    'Logistic Regression': LogisticRegression(random_state=RANDOM_STATE),
    'Gradient Boosting': GradientBoostingClassifier(random_state=RANDOM_STATE),
    'XGBoost': xgb.XGBClassifier(random_state=RANDOM_STATE, eval_metric='logloss')
}

print(f"\n🔧 Optimizando {best_model_name}...")
print("="*80)

# Seleccionar el modelo y sus parámetros
best_model_instance = models_dict[best_model_name]
param_dist = param_distributions[best_model_name]

# Usar GridSearchCV para Logistic Regression, RandomizedSearchCV para los demás
if best_model_name == 'Logistic Regression':
    search = GridSearchCV(
        best_model_instance,
        param_dist,
        cv=3,
        scoring='roc_auc',
        n_jobs=-1,
        verbose=1
    )
else:
    search = RandomizedSearchCV(
        best_model_instance,
        param_dist,
        n_iter=20,
        cv=3,
        scoring='roc_auc',
        random_state=RANDOM_STATE,
        n_jobs=-1,
        verbose=1
    )

# Entrenar con búsqueda de hiperparámetros
search.fit(X_train_balanced, y_train_balanced)

# Mejor modelo optimizado
best_model_optimized = search.best_estimator_

print(f"\n✅ Mejores hiperparámetros para {best_model_name}:")
for param, value in search.best_params_.items():
    print(f"   • {param}: {value}")

print(f"\n📊 ROC-AUC en validación cruzada: {search.best_score_:.4f}")

# Predicciones
y_pred_best = best_model_optimized.predict(X_test)
y_pred_proba_best = best_model_optimized.predict_proba(X_test)[:, 1]

# Guardar métricas del mejor modelo para conclusiones dinámicas
best_model_metrics = {
    'name': f'{best_model_name} Optimizado',  # ✅ DINÁMICO
    'accuracy': accuracy_score(y_test, y_pred_best),
    'precision': precision_score(y_test, y_pred_best),
    'recall': recall_score(y_test, y_pred_best),
    'f1': f1_score(y_test, y_pred_best),
    'roc_auc': roc_auc_score(y_test, y_pred_proba_best),
    'cv_score': search.best_score_,
    'best_params': search.best_params_
}

print("\n" + "="*80)
print(f"\n📈 MÉTRICAS FINALES - {best_model_metrics['name']}:")
print(f"   • Accuracy:  {best_model_metrics['accuracy']:.4f}")
print(f"   • Precision: {best_model_metrics['precision']:.4f}")
print(f"   • Recall:    {best_model_metrics['recall']:.4f}")
print(f"   • F1-Score:  {best_model_metrics['f1']:.4f}")
print(f"   • ROC-AUC:   {best_model_metrics['roc_auc']:.4f}")
print("\n" + "="*80)

