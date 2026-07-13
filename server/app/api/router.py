from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import ml
from app.api.routes import repository

router = APIRouter()

router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)

router.include_router(
    ml.router,
    prefix="/ml",
    tags=["Machine Learning"],
)

router.include_router(repository.router)