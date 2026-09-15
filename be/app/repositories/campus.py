from typing import List, Optional, Tuple
from sqlalchemy import or_
from sqlalchemy.orm import Session, selectinload

from app.models.campus import Campus
from app.models.faculty import Faculty
from app.schemas.campus import CampusCreate


class CampusRepository:
    def get_by_id(self, db: Session, campus_id: int) -> Optional[Campus]:
        return db.query(Campus).filter(Campus.id == campus_id).first()

    def get_by_slug(self, db: Session, slug: str) -> Optional[Campus]:
        return (
            db.query(Campus)
            .options(
                selectinload(Campus.faculties).selectinload(Faculty.majors),
                selectinload(Campus.majors),
            )
            .filter(Campus.slug == slug)
            .first()
        )

    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 12,
        search: Optional[str] = None,
        type: Optional[str] = None,
        accreditation: Optional[str] = None,
        city: Optional[str] = None,
        province: Optional[str] = None,
    ) -> Tuple[List[Campus], int]:
        query = db.query(Campus).filter(Campus.is_active.is_(True))

        if search:
            search_pattern = f"%{search.strip()}%"
            query = query.filter(
                or_(
                    Campus.name.ilike(search_pattern),
                    Campus.short_name.ilike(search_pattern),
                    Campus.city.ilike(search_pattern),
                )
            )

        if type:
            query = query.filter(Campus.type == type.upper())

        if accreditation:
            query = query.filter(Campus.accreditation == accreditation)

        if city:
            query = query.filter(Campus.city.ilike(f"%{city.strip()}%"))

        if province:
            query = query.filter(Campus.province.ilike(f"%{province.strip()}%"))

        total = query.count()

        items = (
            query.order_by(
                Campus.ranking_national.asc().nulls_last(),
                Campus.name.asc(),
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

        return items, total

    def create(self, db: Session, campus_in: CampusCreate) -> Campus:
        db_obj = Campus(**campus_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


campus_repository = CampusRepository()
