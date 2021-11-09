from fastapi import Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base, get_db


class SdkCounter(Base):
    __tablename__ = "sdkcounter"
    id = Column(Integer, primary_key=True, index=True)
    sdk = Column(String, index=True)
    ad_counter = Column(Integer, nullable=False, default=1)
    imp_counter = Column(Integer, nullable=False, default=1)

    @classmethod
    def get_all_sdk(cls, db: Session):
        return db.query(SdkCounter).all()

    @classmethod
    def add_sdk_ad_or_imp_counter(
            cls,
            sdk,
            type_counter: str,
            db: Session = Depends(get_db)
    ):
        if type_counter.value == 'AD':
            sdk.ad_counter = SdkCounter.ad_counter + 1
        if type_counter.value == 'IMP':
            sdk.imp_counter = SdkCounter.imp_counter + 1
        db.add(sdk)
        db.commit()
