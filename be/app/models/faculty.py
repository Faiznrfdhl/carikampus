from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.campus import Campus
    from app.models.major import Major


class Faculty(Base):
    __tablename__ = "faculties"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    campus_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("campuses.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    campus: Mapped["Campus"] = relationship("Campus", back_populates="faculties")
    majors: Mapped[List["Major"]] = relationship(
        "Major", back_populates="faculty"
    )

    def __repr__(self) -> str:
        return f"<Faculty id={self.id} name='{self.name}' campus_id={self.campus_id}>"
