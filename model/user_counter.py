from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from database import Base


class UserCounter(Base):
    __tablename__ = "usercounter"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    ad_counter = Column(Integer, nullable=False, default=1)
    imp_counter = Column(Integer, nullable=False, default=1)

    @classmethod
    def add_user_ad_or_imp_counter(
            cls,
            db: Session,
            user,
            type_counter: str
    ):
        if type_counter.value == 'AD':
            user.ad_counter = UserCounter.ad_counter + 1
        if type_counter.value == 'IMP':
            user.imp_counter = UserCounter.imp_counter + 1
        db.add(user)
        db.commit()

    @classmethod
    def get_all_user(cls, db: Session):
        return db.query(UserCounter).all()

    @classmethod
    def create_user(cls, username: str, db: Session):
        new_user = UserCounter(username=username)
        db.add(new_user)
        db.commit()

    @classmethod
    def get_or_create_user_by_username(
            cls,
            username: str,
            db: Session
    ):
        user = db.query(UserCounter)\
            .filter(UserCounter.username == username)\
            .first()
        if user:
            return user, False
        else:
            return cls.create_user(username, db), True
