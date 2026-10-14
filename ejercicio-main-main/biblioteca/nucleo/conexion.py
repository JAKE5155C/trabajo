import asyncio
from typing import Annotated

import asyncpg
from fastapi import Depends, HTTPException

from biblioteca.nucleo.configuracion import obtener_database_url


class Db:
    """Envoltorio mínimo sobre el pool de conexiones de asyncpg."""

    pool: asyncpg.Pool | None = None
    _connect_lock = asyncio.Lock()

    async def connect(self, db_url: str):
        self.pool = await asyncpg.create_pool(
            dsn=db_url,
            min_size=1,
            max_size=1,
            timeout=15,
        )

    async def connect_from_environment(self):
        db_url = obtener_database_url()
        if not db_url:
            raise HTTPException(
                status_code=503,
                detail="DATABASE_URL no está configurada en Vercel",
            )
        async with self._connect_lock:
            if self.pool is None:
                try:
                    await self.connect(db_url)
                except Exception as error:
                    raise HTTPException(
                        status_code=503,
                        detail="No se pudo conectar a PostgreSQL. Revisa DATABASE_URL en Vercel.",
                    ) from error

    async def close(self):
        if self.pool is not None:
            await self.pool.close()
            self.pool = None


db = Db()


async def get_connection():
    """Dependencia de FastAPI: cede una conexión del pool a cada petición."""
    if db.pool is None:
        await db.connect_from_environment()
    async with db.pool.acquire() as conn:
        yield conn


ConnectionDep = Annotated[asyncpg.Connection, Depends(get_connection)]