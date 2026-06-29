from database.base import Base
from database.connection import engine
import models.student

Base.metadata.create_all(bind=engine)