"""
Configuración de colores y estilos para el dashboard
"""

# Paleta de colores principal
COLORS = {
    'primary': '#1f77b4',      # Azul principal
    'secondary': '#ff7f0e',    # Naranja secundario
    'success': '#2ca02c',      # Verde éxito
    'warning': '#ff9800',      # Naranja advertencia
    'danger': '#d62728',       # Rojo peligro
    'info': '#17a2b8',         # Azul info
    'light': '#f8f9fa',        # Gris claro
    'dark': '#343a40',         # Gris oscuro
}

# CSS personalizado para el dashboard
CUSTOM_CSS = """
<style>
    /* Estilos generales */
    .main {
        padding: 2rem;
    }
    
    /* Tarjetas de contenido */
    .content-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    
    /* Métricas destacadas */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Botones personalizados */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Formularios */
    .stSelectbox, .stNumberInput, .stSlider {
        margin-bottom: 0.5rem;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Alertas personalizadas */
    .alert-success {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-warning {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-danger {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .alert-info {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .hero h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .hero p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Secciones de características */
    .feature-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }
    
    /* Tooltips personalizados */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    
    /* Separadores */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 2px solid #e9ecef;
    }
</style>
"""

def get_risk_color(probability):
    """Retorna el color según el nivel de riesgo"""
    if probability < 0.3:
        return COLORS['success']
    elif probability < 0.5:
        return COLORS['warning']
    elif probability < 0.7:
        return COLORS['secondary']
    else:
        return COLORS['danger']

def get_risk_level(probability):
    """Retorna el nivel de riesgo según la probabilidad"""
    if probability < 0.3:
        return "🟢 Bajo"
    elif probability < 0.5:
        return "🟡 Medio"
    elif probability < 0.7:
        return "🟠 Alto"
    else:
        return "🔴 Crítico"

