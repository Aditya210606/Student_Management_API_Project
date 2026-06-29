from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from core.config import settings

DATABASE_URL = URL.create(
    drivername="postgresql",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)

engine = create_engine(DATABASE_URL, echo=True)

print("Database Connected Successfully")