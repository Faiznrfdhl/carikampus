from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.faculty import FacultyResponse
from app.schemas.major import MajorResponse


class CampusBase(BaseModel):
    name: str
    short_name: Optional[str] = None
    slug: str
    type: str = "PTN"
    accreditation: Optional[str] = None
    city: str
    province: str
    address: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    ranking_national: Optional[int] = None
    is_active: bool = True


class CampusCreate(CampusBase):
    pass


class CampusUpdate(BaseModel):
    name: Optional[str] = None
    short_name: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[str] = None
    accreditation: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    banner_url: Optional[str] = None
    description: Optional[str] = None
    ranking_national: Optional[int] = None
    is_active: Optional[bool] = None


class CampusListItem(BaseModel):
    id: int
    name: str
    short_name: Optional[str] = None
    slug: str
    type: str
    accreditation: Optional[str] = None
    city: str
    province: str
    logo_url: Optional[str] = None
    ranking_national: Optional[int] = None
    majors_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class CampusDetailResponse(CampusBase):
    id: int
    created_at: datetime
    updated_at: datetime
    faculties: List[FacultyResponse] = []
    majors: List[MajorResponse] = []

    model_config = ConfigDict(from_attributes=True)
