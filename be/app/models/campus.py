from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Text, Integer, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Campus(Base):
    __tablename__ = "campuses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    short_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, index=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False, default="PTN")  # PTN, PTS, PTK
    accreditation: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)  # Unggul, A, Baik Sekali, B
    city: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    province: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    website: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    banner_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ranking_national: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    faculties: Mapped[List["Faculty"]] = relationship(
        "Faculty", back_populates="campus", cascade="all, delete-orphan"
    )
    majors: Mapped[List["Major"]] = relationship(
        "Major", back_populates="campus", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Campus id={self.id} name='{self.name}'>"
