from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.orm import Session
from config import EXTERNAL_API
from database import get_db

from schema.statistic import (
    GetStatSerializer,
    CreateStatisticData,
    CreateStatisticType
)
from service.statistic_service import (
    get_all_statistic_by_filter_type,
    get_external_responce,
    create_user_or_update_statistic
)


static_router = APIRouter(
    prefix="/v1/stat",
    tags=["statistic"]
)


@static_router.post("/GetAd", status_code=status.HTTP_200_OK)
async def create_ad_stat(
        new_statistic: CreateStatisticData,
        db: Session = Depends(get_db)
):
    external_response = get_external_responce(EXTERNAL_API)
    create_user_or_update_statistic(new_statistic, CreateStatisticType.AD, db)
    return external_response.text


@static_router.post("/Impression", status_code=status.HTTP_204_NO_CONTENT)
async def update_imp_stat(
        new_statistic: CreateStatisticData,
        db: Session = Depends(get_db)
):
    create_user_or_update_statistic(new_statistic, CreateStatisticType.IMP, db)


@static_router.get("/GetStats", status_code=status.HTTP_200_OK)
async def get_stats(filter_type: str, db: Session = Depends(get_db)):
    try:
        GetStatSerializer(filter_type=filter_type)
    except ValidationError:
        raise HTTPException(
            detail="Filter type is not defined",
            status_code=status.HTTP_400_BAD_REQUEST)
    data = get_all_statistic_by_filter_type(filter_type, db)
    return data
