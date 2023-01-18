from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config


class SQLiteDatabase:
    def __init__(self):
        self.engine = create_engine(config.db_url, connect_args={"check_same_thread": False})
        session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = session()
        self.session.commit()


Model = declarative_base()
