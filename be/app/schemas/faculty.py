from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from app.schemas.major import MajorResponse


class FacultyBase(BaseModel):
    name: str
    slug: str


class FacultyCreate(FacultyBase):
    campus_id: int


class FacultyResponse(FacultyBase):
    id: int
    campus_id: int
    created_at: datetime
    updated_at: datetime
    majors: List[MajorResponse] = []

    model_config = ConfigDict(from_attributes=True)
