from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database2:

    def __init__(self, name):
        self.__engine = create_engine('sqlite:///' + name, echo=True)

        self.__conn = self.__engine.connect()

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def conn(self):
        return self.__conn

    @property
    def session(self):
        if self.__session is None:
            session = sessionmaker(self.__engine)
            self.__session = session()
        return self.__session
