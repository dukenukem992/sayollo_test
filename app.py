from fastapi import FastAPI
from router.health import health_router
from router.statistic import static_router
from database import engine
from model.sdk_counter import SdkCounter
from model.user_counter import UserCounter
SdkCounter.metadata.create_all(bind=engine)
UserCounter.metadata.create_all(bind=engine)
api = FastAPI(title="Sayollo API")
api.include_router(health_router)
api.include_router(static_router)