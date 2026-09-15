from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.campus import CampusDetailResponse, CampusListItem
from app.schemas.common import PaginatedResponse
from app.services.campus import campus_service

router = APIRouter()


@router.get("", response_model=PaginatedResponse[CampusListItem], summary="Daftar Kampus")
def get_campuses(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Nomor halaman"),
    limit: int = Query(12, ge=1, le=100, description="Jumlah data per halaman"),
    search: Optional[str] = Query(None, description="Cari nama kampus atau kota"),
    type: Optional[str] = Query(None, description="Filter jenis: PTN, PTS, PTK"),
    accreditation: Optional[str] = Query(None, description="Filter akreditasi: Unggul, A, Baik Sekali, B"),
    city: Optional[str] = Query(None, description="Filter kota"),
    province: Optional[str] = Query(None, description="Filter provinsi"),
):
    """Mengambil daftar kampus dengan dukungan pagination, pencarian, dan filter."""
    return campus_service.list_campuses(
        db=db,
        page=page,
        limit=limit,
        search=search,
        type=type,
        accreditation=accreditation,
        city=city,
        province=province,
    )


@router.get("/{slug}", response_model=CampusDetailResponse, summary="Detail Kampus")
def get_campus_by_slug(
    slug: str,
    db: Session = Depends(get_db),
):
    """Mengambil informasi detail satu kampus beserta daftar fakultas dan jurusannya."""
    return campus_service.get_by_slug(db=db, slug=slug)
