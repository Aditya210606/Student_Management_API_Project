
from sqlalchemy import create_engine
from core.config import settings

DATABASE_URL = (
    f"postgresql://postgres:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)

print("Database Connected Successfully")