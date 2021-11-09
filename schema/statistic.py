from pydantic import BaseModel
from enum import Enum


class CreateStatisticData(BaseModel):
    username: str
    sdk: str
    platform: str
    session_id: str
    country_code: str


class FilterStatisticTypes(Enum):
    SDK = "SDK"
    USER = "USER"


class GetStatSerializer(BaseModel):
    filter_type: FilterStatisticTypes

    class Config:
        use_enum_values = True


class CreateStatisticType(Enum):
    AD = "AD"
    IMP = "IMP"
