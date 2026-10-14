from contextlib import asynccontextmanager

from fastapi import FastAPI

from biblioteca.nucleo.configuracion import database_configured
from biblioteca.nucleo.conexion import db
from biblioteca.presentacion.rutas.autores import router as autores_router
from biblioteca.presentacion.rutas.ejercicios import router as ejercicios_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        if db.pool is not None:
            await db.close()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def healthcheck():
    return {
        "status": "ok",
        "database": "configured" if database_configured() else "not_configured",
    }


app.include_router(autores_router)
app.include_router(ejercicios_router)