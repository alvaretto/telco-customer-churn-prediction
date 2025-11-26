#!/usr/bin/env python3
"""
Script para convertir el notebook a PDF en tamaño oficio (legal: 8.5" x 14")
"""
import subprocess
import sys
import os
from pathlib import Path

def convert_notebook_to_legal_pdf(notebook_path, output_pdf):
    """
    Convierte un notebook Jupyter a PDF en tamaño oficio.
    """
    # Paso 1: Convertir a HTML
    html_output = notebook_path.replace('.ipynb', '_temp.html')
    
    print("📄 Paso 1: Convirtiendo notebook a HTML...")
    cmd_html = [
        'jupyter', 'nbconvert',
        '--to', 'html',
        # NO usar --no-input para incluir TODO el código
        notebook_path,
        '--output', html_output
    ]
    
    try:
        subprocess.run(cmd_html, check=True)
        print(f"✅ HTML generado: {html_output}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al generar HTML: {e}")
        return False
    
    # Paso 2: Inyectar CSS para tamaño oficio
    print("\n📐 Paso 2: Ajustando CSS para tamaño oficio...")
    
    with open(html_output, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # CSS para tamaño oficio - OPTIMIZADO para aprovechar el espacio vertical
    legal_css = """
    <style>
    @page {
        size: legal; /* 8.5in x 14in */
        margin: 0.5in 0.5in 0.75in 0.5in; /* Top, Right, Bottom (espacio para footer), Left */

        @bottom-center {
            content: counter(page) " de " counter(pages);
            font-size: 9pt;
            color: #666;
            font-family: Arial, sans-serif;
        }
    }

    @media print {
        body {
            width: 7.5in;
            margin: 0 auto;
            padding: 0;
        }

        .jp-Notebook {
            max-width: 7.5in !important;
            padding: 0 !important;
        }

        .container {
            max-width: 7.5in !important;
            padding: 0 !important;
        }

        /* Reducir espaciado entre celdas */
        .jp-Cell {
            margin-bottom: 0.3em !important;
            padding: 0.2em 0 !important;
        }

        /* Reducir espaciado de outputs */
        .jp-OutputArea {
            padding: 0.2em 0 !important;
        }
    }

    body {
        max-width: 7.5in;
        margin: 0 auto;
        padding: 0;
        font-size: 10pt; /* Reducido de 11pt */
        line-height: 1.3; /* Reducido para aprovechar espacio */
    }

    .jp-Notebook {
        max-width: 7.5in !important;
        padding: 0 !important;
    }

    .container {
        max-width: 7.5in !important;
        padding: 0 !important;
    }

    /* Reducir espaciado entre celdas */
    .jp-Cell {
        margin-bottom: 0.5em !important;
        padding: 0.3em 0 !important;
    }

    /* Reducir espaciado de outputs */
    .jp-OutputArea {
        padding: 0.3em 0 !important;
        margin: 0.2em 0 !important;
    }

    /* Reducir espaciado de código */
    .jp-InputArea {
        padding: 0.2em !important;
    }

    pre {
        margin: 0.2em 0 !important;
        padding: 0.3em !important;
        line-height: 1.2;
        font-size: 9pt;
    }

    /* Reducir espaciado de headers */
    h1 {
        margin: 0.5em 0 0.3em 0 !important;
        font-size: 1.8em;
        line-height: 1.2;
    }

    h2 {
        margin: 0.4em 0 0.25em 0 !important;
        font-size: 1.5em;
        line-height: 1.2;
    }

    h3 {
        margin: 0.3em 0 0.2em 0 !important;
        font-size: 1.3em;
        line-height: 1.2;
    }

    h4, h5, h6 {
        margin: 0.2em 0 0.15em 0 !important;
        line-height: 1.2;
    }

    /* Reducir espaciado de párrafos */
    p {
        margin: 0.3em 0 !important;
        line-height: 1.3;
    }

    /* Reducir espaciado de listas */
    ul, ol {
        margin: 0.3em 0 !important;
        padding-left: 1.5em !important;
    }

    li {
        margin: 0.1em 0 !important;
        line-height: 1.3;
    }

    /* Ajustar imágenes para que aprovechen el espacio */
    img {
        max-width: 100% !important;
        height: auto !important;
        margin: 0.3em 0 !important;
    }

    /* Optimizar tablas */
    table {
        max-width: 100% !important;
        font-size: 9pt;
        margin: 0.3em 0 !important;
        border-collapse: collapse !important;
    }

    td, th {
        padding: 0.2em 0.3em !important;
        line-height: 1.2;
    }

    /* Reducir espaciado de dataframes */
    .dataframe {
        font-size: 8pt !important;
        margin: 0.3em 0 !important;
    }

    .dataframe td, .dataframe th {
        padding: 0.15em 0.25em !important;
    }

    /* Optimizar outputs de texto */
    .output_text {
        font-size: 9pt;
        line-height: 1.2;
        margin: 0.2em 0 !important;
    }

    /* Reducir espaciado de divs generales */
    div {
        margin: 0 !important;
    }

    /* Evitar saltos de página innecesarios */
    .jp-Cell {
        page-break-inside: avoid;
    }

    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
    }
    </style>
    """
    
    # Insertar CSS antes de </head>
    html_content = html_content.replace('</head>', legal_css + '\n</head>')
    
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ CSS para tamaño oficio aplicado")
    
    # Paso 3: Convertir HTML a PDF usando playwright
    print("\n🖨️  Paso 3: Convirtiendo HTML a PDF (tamaño oficio)...")
    
    # Usar nbconvert webpdf pero desde el HTML modificado
    # Primero convertir el HTML de vuelta a notebook temporalmente no es eficiente
    # Mejor usar playwright directamente
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Cargar el HTML
            html_file_path = f"file://{os.path.abspath(html_output)}"
            page.goto(html_file_path)
            
            # Generar PDF con tamaño oficio y numeración de páginas
            page.pdf(
                path=output_pdf,
                format='Legal',  # 8.5" x 14"
                margin={
                    'top': '0.5in',
                    'bottom': '0.75in',  # Espacio para el footer con numeración
                    'left': '0.5in',
                    'right': '0.5in'
                },
                print_background=True,
                display_header_footer=True,
                header_template='<div></div>',  # Header vacío
                footer_template='''
                    <div style="font-size: 9pt; color: #666; text-align: center; width: 100%; margin: 0 auto;">
                        <span class="pageNumber"></span> de <span class="totalPages"></span>
                    </div>
                '''
            )
            
            browser.close()
        
        print(f"✅ PDF generado: {output_pdf}")
        
        # Limpiar archivo temporal
        os.remove(html_output)
        print(f"🧹 Archivo temporal eliminado: {html_output}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        return False

if __name__ == '__main__':
    notebook = 'Telco_Customer_Churn.ipynb'
    output = 'Telco_Customer_Churn_Oficio.pdf'
    
    print("=" * 60)
    print("🔄 Conversión de Notebook a PDF Tamaño Oficio")
    print("=" * 60)
    print(f"📓 Notebook: {notebook}")
    print(f"📄 Output: {output}")
    print("=" * 60)
    print()
    
    success = convert_notebook_to_legal_pdf(notebook, output)
    
    if success:
        # Obtener tamaño del archivo
        size_mb = os.path.getsize(output) / (1024 * 1024)
        print()
        print("=" * 60)
        print("✅ CONVERSIÓN EXITOSA")
        print("=" * 60)
        print(f"📄 Archivo: {output}")
        print(f"📏 Tamaño: {size_mb:.2f} MB")
        print(f"📐 Formato: Legal (8.5\" x 14\" - Oficio)")
        print("=" * 60)
        sys.exit(0)
    else:
        print()
        print("=" * 60)
        print("❌ ERROR EN LA CONVERSIÓN")
        print("=" * 60)
        sys.exit(1)

