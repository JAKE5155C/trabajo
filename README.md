# Lista de productos

Aplicación web pequeña para consultar una lista de productos y generar un
reporte descargable en PDF. Está construida con FastAPI y plantillas Jinja2;
el PDF se crea directamente desde HTML con xhtml2pdf.

## Funcionalidades

- Página de inicio con el acceso a la lista.
- Vista previa de los productos con categoría, precio y existencias.
- Descarga del reporte como archivo `report.pdf`.

## Ejecutar en local

Desde la raíz del repositorio:

```bash
cd pdfs-main
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt uvicorn
uvicorn main:app --reload
```

Abre <http://127.0.0.1:8000> en el navegador.

## Rutas

| Ruta | Descripción |
| --- | --- |
| `/` | Página de inicio |
| `/report` | Vista previa de la lista |
| `/report/pdf` | Descarga del reporte en PDF |

## Publicar en Vercel

1. Importa el repositorio en Vercel.
2. Puedes seleccionar `pdfs-main` como **Root Directory** para usar su configuración, o dejar la raíz del repositorio como directorio: el `vercel.json` de la raíz también apunta a esta aplicación e incluye sus plantillas.
3. Después de subir los cambios al repositorio, crea un nuevo deployment en Vercel. Para confirmar que se muestra la versión nueva, verifica que el deployment use el commit más reciente.
Enlace del proyecto: <https://trabajo-1o9e.vercel.app/>.

## Estructura

```text
pdfs-main/
├── main.py               # Aplicación FastAPI y rutas
├── requirements.txt      # Dependencias de Python
└── templates/
    ├── index.html        # Página de inicio
    └── report.html       # Vista previa y plantilla del PDF
```

Los productos de ejemplo están definidos en `pdfs-main/main.py`.
