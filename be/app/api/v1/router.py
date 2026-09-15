from fastapi import APIRouter
from app.api.v1.endpoints import health, campuses

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="", tags=["Health"])
api_router.include_router(campuses.router, prefix="/campuses", tags=["Campuses"])
