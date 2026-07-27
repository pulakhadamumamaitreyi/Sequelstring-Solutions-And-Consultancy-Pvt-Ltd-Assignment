from app.database.database import engine
from app.database.base import Base

from app.models.document import Document


def create_tables():
    Base.metadata.create_all(bind=engine)
