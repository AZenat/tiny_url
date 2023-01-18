from .database import Model, SQLiteDatabase
from .user import User
from .url import URL


class DatabaseFactory:

    @staticmethod
    def create():
        database = SQLiteDatabase()
        Model.metadata.create_all(bind=database.engine)
        return database
