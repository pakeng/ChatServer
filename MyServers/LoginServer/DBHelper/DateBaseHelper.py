from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from MyServers.LoginServer.DBHelper import Config


class DBHelper(object):

    def __init__(self):
        # 创建引擎
        self._engine = create_engine(Config.uri, max_overflow=Config.max_overflow, encoding=Config.char_set)
        self._session = ''

    def get_db_engine(self):
        return self._engine

    def get_db_session(self):
        Session = sessionmaker(bind=self._engine)
        self._session = Session()
        return self._session
