"""
Utilidades para el proyecto de predicción de Customer Churn.

Este módulo contiene funciones auxiliares para:
- Configuración y gestión de rutas
- Validación de datos
- Logging estructurado
- Cálculo de métricas de negocio
- Reproducibilidad
"""

import os
import json
import logging
import random
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Any, Optional
from sklearn.metrics import confusion_matrix


class ConfigManager:
    """Gestor de configuración del proyecto."""
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Inicializa el gestor de configuración.
        
        Args:
            config_path: Ruta al archivo de configuración JSON
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.is_colab = self._check_colab()
    
    def _load_config(self) -> Dict:
        """Carga la configuración desde el archivo JSON."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"❌ Archivo de configuración no encontrado: {self.config_path}\n"
                "   Asegúrate de que config.json existe en el directorio del proyecto."
            )
        except json.JSONDecodeError as e:
            raise ValueError(f"❌ Error al parsear config.json: {str(e)}")
    
    def _check_colab(self) -> bool:
        """Verifica si se está ejecutando en Google Colab."""
        try:
            import google.colab
            return True
        except ImportError:
            return False
    
    def get_base_path(self) -> str:
        """Retorna la ruta base según el entorno (Colab o local)."""
        if self.is_colab:
            return self.config['paths']['colab_base']
        return self.config['paths']['local_base']
    
    def get_models_path(self) -> str:
        """Retorna la ruta para guardar modelos."""
        if self.is_colab:
            return self.config['paths']['colab_models']
        return self.config['paths']['local_models']
    
    def get_reports_path(self) -> str:
        """Retorna la ruta para guardar informes."""
        if self.is_colab:
            return self.config['paths']['colab_reports']
        return self.config['paths']['local_reports']
    
    def get(self, *keys):
        """
        Obtiene un valor de la configuración usando notación de puntos.
        
        Ejemplo:
            config.get('random_state', 'seed')  # Retorna 42
        """
        value = self.config
        for key in keys:
            value = value[key]
        return value


def setup_google_drive(force_remount: bool = False) -> bool:
    """
    Monta Google Drive si está en Colab y no está montado.
    
    Args:
        force_remount: Si True, fuerza el remontaje incluso si ya está montado
    
    Returns:
        True si Drive está montado o se montó exitosamente, False en caso contrario
    """
    try:
        from google.colab import drive
        
        if not os.path.exists('/content/drive') or force_remount:
            print("📁 Montando Google Drive...")
            drive.mount('/content/drive', force_remount=force_remount)
            print("✅ Google Drive montado exitosamente")
        else:
            print("✅ Google Drive ya está montado")
        return True
    except ImportError:
        print("ℹ️  No se está ejecutando en Google Colab")
        return False
    except Exception as e:
        print(f"❌ Error al montar Google Drive: {str(e)}")
        return False


def set_all_seeds(seed: int = 42) -> None:
    """
    Fija todas las semillas aleatorias para reproducibilidad total.
    
    Args:
        seed: Valor de la semilla (default: 42)
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    
    # Si se usa TensorFlow/Keras (descomentar si es necesario)
    # try:
    #     import tensorflow as tf
    #     tf.random.set_seed(seed)
    # except ImportError:
    #     pass
    
    print(f"✅ Todas las semillas aleatorias fijadas a: {seed}")
    print(f"   📌 Reproducibilidad garantizada")


def setup_logging(config: ConfigManager, notebook_name: str = "churn_model") -> logging.Logger:
    """
    Configura el sistema de logging.

    Args:
        config: Instancia de ConfigManager
        notebook_name: Nombre base para el archivo de log

    Returns:
        Logger configurado
    """
    log_config = config.get('logging')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    handlers = [logging.StreamHandler()]

    if log_config.get('log_to_file', True):
        log_filename = f"{notebook_name}_{timestamp}.log"
        handlers.append(logging.FileHandler(log_filename))

    logging.basicConfig(
        level=getattr(logging, log_config['level']),
        format=log_config['format'],
        handlers=handlers
    )

    logger = logging.getLogger(notebook_name)
    logger.info(f"Sistema de logging inicializado - {timestamp}")

    return logger


def validate_dataset(df: pd.DataFrame, config: ConfigManager, logger: Optional[logging.Logger] = None) -> bool:
    """
    Valida la integridad y calidad del dataset.

    Args:
        df: DataFrame a validar
        config: Instancia de ConfigManager
        logger: Logger opcional para registrar mensajes

    Returns:
        True si todas las validaciones pasan

    Raises:
        ValueError: Si alguna validación falla
    """
    validation_config = config.get('validation')
    errors = []
    warnings = []

    # 1. Verificar que el DataFrame no esté vacío
    if df.empty:
        errors.append("Dataset está vacío")

    # 2. Verificar columnas requeridas
    required_cols = set(validation_config['required_columns'])
    actual_cols = set(df.columns)
    missing_cols = required_cols - actual_cols

    if missing_cols:
        errors.append(f"Columnas faltantes: {missing_cols}")

    # 3. Verificar columnas críticas sin valores nulos
    critical_cols = validation_config['critical_columns']
    for col in critical_cols:
        if col in df.columns and df[col].isnull().any():
            errors.append(f"Columna crítica '{col}' tiene valores nulos")

    # 4. Verificar porcentaje de valores nulos
    max_null_pct = validation_config['max_null_percentage']
    null_percentages = (df.isnull().sum() / len(df)) * 100
    high_null_cols = null_percentages[null_percentages > max_null_pct]

    if not high_null_cols.empty:
        warnings.append(
            f"Columnas con >{max_null_pct}% nulos: {dict(high_null_cols)}"
        )

    # 5. Verificar duplicados
    max_duplicates = validation_config['max_duplicates']
    n_duplicates = df.duplicated().sum()

    if n_duplicates > max_duplicates:
        warnings.append(f"Se encontraron {n_duplicates} registros duplicados")

    # 6. Verificar tipos de datos básicos
    if 'Churn' in df.columns:
        unique_churn = df['Churn'].unique()
        if not set(unique_churn).issubset({'Yes', 'No'}):
            errors.append(f"Valores inesperados en 'Churn': {unique_churn}")

    # Reportar resultados
    if errors:
        error_msg = "❌ Validación del dataset FALLIDA:\n" + "\n".join(f"   - {e}" for e in errors)
        if logger:
            logger.error(error_msg)
        raise ValueError(error_msg)

    if warnings:
        warning_msg = "⚠️  Advertencias de validación:\n" + "\n".join(f"   - {w}" for w in warnings)
        if logger:
            logger.warning(warning_msg)
        print(warning_msg)

    success_msg = f"✅ Dataset validado correctamente ({len(df):,} registros, {len(df.columns)} columnas)"
    if logger:
        logger.info(success_msg)
    print(success_msg)

    return True


def calculate_business_cost(y_true: np.ndarray, y_pred: np.ndarray,
                           fn_cost: float = 500, fp_cost: float = 50) -> Dict[str, float]:
    """
    Calcula el costo de negocio basado en la matriz de confusión.

    Args:
        y_true: Etiquetas verdaderas
        y_pred: Predicciones del modelo
        fn_cost: Costo de un falso negativo (cliente perdido)
        fp_cost: Costo de un falso positivo (campaña innecesaria)

    Returns:
        Diccionario con métricas de costo de negocio
    """
    cm = confusion_matrix(y_true, y_pred)
    true_negatives, false_positives, false_negatives, true_positives = cm.ravel()

    total_cost = (false_negatives * fn_cost) + (false_positives * fp_cost)
    cost_per_customer = total_cost / len(y_true)

    # Calcular ahorro potencial (si detectamos todos los churns)
    total_churns = false_negatives + true_positives
    potential_savings = total_churns * fn_cost
    actual_savings = true_positives * fn_cost
    savings_rate = (actual_savings / potential_savings * 100) if potential_savings > 0 else 0

    return {
        'total_cost': total_cost,
        'cost_per_customer': cost_per_customer,
        'false_negative_cost': false_negatives * fn_cost,
        'false_positive_cost': false_positives * fp_cost,
        'potential_savings': potential_savings,
        'actual_savings': actual_savings,
        'savings_rate': savings_rate,
        'true_negatives': true_negatives,
        'false_positives': false_positives,
        'false_negatives': false_negatives,
        'true_positives': true_positives
    }


def print_business_metrics(business_metrics: Dict[str, float]) -> None:
    """
    Imprime las métricas de negocio de forma formateada.

    Args:
        business_metrics: Diccionario retornado por calculate_business_cost
    """
    print("\n" + "="*80)
    print("💰 MÉTRICAS DE NEGOCIO")
    print("="*80)
    print(f"\n📊 Matriz de Confusión:")
    print(f"   • Verdaderos Negativos (TN): {business_metrics['true_negatives']:,}")
    print(f"   • Falsos Positivos (FP):     {business_metrics['false_positives']:,}")
    print(f"   • Falsos Negativos (FN):     {business_metrics['false_negatives']:,} ⚠️ CRÍTICO")
    print(f"   • Verdaderos Positivos (TP): {business_metrics['true_positives']:,}")

    print(f"\n💵 Costos:")
    print(f"   • Costo por FN (cliente perdido):      ${business_metrics['false_negative_cost']:,.2f}")
    print(f"   • Costo por FP (campaña innecesaria):  ${business_metrics['false_positive_cost']:,.2f}")
    print(f"   • Costo Total:                         ${business_metrics['total_cost']:,.2f}")
    print(f"   • Costo por Cliente:                   ${business_metrics['cost_per_customer']:.2f}")

    print(f"\n💰 Ahorro Potencial:")
    print(f"   • Ahorro Máximo Posible:  ${business_metrics['potential_savings']:,.2f}")
    print(f"   • Ahorro Actual:          ${business_metrics['actual_savings']:,.2f}")
    print(f"   • Tasa de Ahorro:         {business_metrics['savings_rate']:.1f}%")
    print("="*80 + "\n")

