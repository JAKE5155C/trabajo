# Lista de productos

## Ejecutar en local

```bash
cd pdfs-main
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt uvicorn
uvicorn main:app --reload
```

Abre `https://trabajo-ovkn.vercel.app/`.

## Publicar en Vercel

1. Importa el repositorio en Vercel.
2. En la configuracion del proyecto, selecciona `pdfs-main` como **Root Directory**.
3. Despliega el proyecto. Vercel detecta FastAPI desde `main.py` e instala las dependencias de `requirements.txt`.

`vercel.json` incluye las plantillas que usa la aplicacion para mostrar la pagina y generar el PDF.
