# Import all SQLAlchemy models here for Alembic detection and metadata reflection
# Example: from app.models.user import User
from app.db.base import Base

__all__ = ["Base"]
