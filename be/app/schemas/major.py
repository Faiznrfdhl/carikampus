from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class MajorBase(BaseModel):
    name: str
    slug: str
    degree: str = "S1"
    accreditation: Optional[str] = None
    capacity: Optional[int] = None
    tuition_min: Optional[float] = None
    tuition_max: Optional[float] = None
    career_prospects: Optional[str] = None
    is_active: bool = True


class MajorCreate(MajorBase):
    campus_id: int
    faculty_id: Optional[int] = None


class MajorResponse(MajorBase):
    id: int
    campus_id: int
    faculty_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
