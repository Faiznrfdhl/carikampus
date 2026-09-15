import math
from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.campus import campus_repository
from app.schemas.campus import CampusDetailResponse, CampusListItem
from app.schemas.common import PaginatedResponse


class CampusService:
    def list_campuses(
        self,
        db: Session,
        page: int = 1,
        limit: int = 12,
        search: Optional[str] = None,
        type: Optional[str] = None,
        accreditation: Optional[str] = None,
        city: Optional[str] = None,
        province: Optional[str] = None,
    ) -> PaginatedResponse[CampusListItem]:
        if page < 1:
            page = 1
        if limit < 1 or limit > 100:
            limit = 12

        skip = (page - 1) * limit
        campuses, total = campus_repository.get_all(
            db=db,
            skip=skip,
            limit=limit,
            search=search,
            type=type,
            accreditation=accreditation,
            city=city,
            province=province,
        )

        items = []
        for c in campuses:
            items.append(
                CampusListItem(
                    id=c.id,
                    name=c.name,
                    short_name=c.short_name,
                    slug=c.slug,
                    type=c.type,
                    accreditation=c.accreditation,
                    city=c.city,
                    province=c.province,
                    logo_url=c.logo_url,
                    ranking_national=c.ranking_national,
                    majors_count=len(c.majors) if c.majors else 0,
                )
            )

        total_pages = math.ceil(total / limit) if total > 0 else 0

        return PaginatedResponse[CampusListItem](
            items=items,
            total=total,
            page=page,
            limit=limit,
            total_pages=total_pages,
        )

    def get_by_slug(self, db: Session, slug: str) -> CampusDetailResponse:
        campus = campus_repository.get_by_slug(db, slug)
        if not campus:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Kampus dengan slug '{slug}' tidak ditemukan.",
            )
        return CampusDetailResponse.model_validate(campus)


campus_service = CampusService()
