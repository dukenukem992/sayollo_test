from fastapi import APIRouter
from schema.health import Health


health_router = APIRouter(
    prefix="/v1/health",
    tags=["health"]
)


@health_router.get("")
async def get():
    return Health()
