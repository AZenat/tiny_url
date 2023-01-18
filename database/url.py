import datetime
from sqlalchemy import Column, Integer, String, DateTime

from .database import Model


class URL(Model):

    __tablename__ = "url"

    id = Column(Integer, primary_key=True, autoincrement=True)
    long_url = Column(String, index=True)
    short_url = Column(String, unique=True, index=True)
    clicks = Column(Integer, default=0)
    created = Column(DateTime, default=datetime.datetime.now)
