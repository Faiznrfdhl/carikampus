from app.schemas.common import PaginatedResponse
from app.schemas.major import MajorBase, MajorCreate, MajorResponse
from app.schemas.faculty import FacultyBase, FacultyCreate, FacultyResponse
from app.schemas.campus import (
    CampusBase,
    CampusCreate,
    CampusUpdate,
    CampusListItem,
    CampusDetailResponse,
)

__all__ = [
    "PaginatedResponse",
    "MajorBase",
    "MajorCreate",
    "MajorResponse",
    "FacultyBase",
    "FacultyCreate",
    "FacultyResponse",
    "CampusBase",
    "CampusCreate",
    "CampusUpdate",
    "CampusListItem",
    "CampusDetailResponse",
]
