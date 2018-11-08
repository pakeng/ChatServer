from sqlalchemy import create_engine

from MyServers.LoginServer.DBHelper import Config


class DBHelper(object):

    def __init__(self):
        # 创建引擎
        self.engine = create_engine(Config.uri, max_overflow=Config.max_overflow)

    def get_db_engine(self):
        return self.engine
