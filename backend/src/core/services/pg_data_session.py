from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.interfaces.data_session import DataSessionInterface


class PgDataSession(DataSessionInterface):

    def __init__(self, url: str, name: str, user: str,
                 password: str):
        engine = create_engine(
            f'postgresql://{user}:{password}@{url}/{name}')
        self.Session = sessionmaker(bind=engine)

    def get_session(self):
        return self.Session
