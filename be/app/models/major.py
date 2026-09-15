from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Text, Integer, Boolean, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.campus import Campus
    from app.models.faculty import Faculty


class Major(Base):
    __tablename__ = "majors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    campus_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("campuses.id", ondelete="CASCADE"), nullable=False, index=True
    )
    faculty_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("faculties.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    degree: Mapped[str] = mapped_column(String(20), nullable=False, default="S1")  # D3, D4, S1, S2, S3, Profesi
    accreditation: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    capacity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    tuition_min: Mapped[Optional[float]] = mapped_column(Numeric(12, 2), nullable=True)
    tuition_max: Mapped[Optional[float]] = mapped_column(Numeric(12, 2), nullable=True)
    career_prospects: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    campus: Mapped["Campus"] = relationship("Campus", back_populates="majors")
    faculty: Mapped[Optional["Faculty"]] = relationship("Faculty", back_populates="majors")

    def __repr__(self) -> str:
        return f"<Major id={self.id} name='{self.name}' degree='{self.degree}' campus_id={self.campus_id}>"
