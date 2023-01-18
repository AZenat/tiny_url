from sqlalchemy import Integer, Column, String

from .database import Model


class User(Model):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
