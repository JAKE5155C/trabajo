import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def obtener_database_url() -> str:
    return os.environ.get("DATABASE_URL", "").strip().strip('"').strip("'")


def database_configured() -> bool:
    return bool(obtener_database_url())