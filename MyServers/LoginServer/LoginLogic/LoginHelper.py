from MyServers.LoginServer.DataBase.Tables import User
from MyServers.LoginServer.DBHelper.DateBaseHelper import DBHelper


class Login(object):

    @staticmethod
    def valid_login(name, pwd):
        dbhelper = DBHelper()
        session = dbhelper.get_db_session()
        ret = session.query(User).filter_by(name=name).first()
        if ret.pwd == pwd:
            return True
        else:
            return False

    @staticmethod
    def log_the_user_in(account):

        return True

    @staticmethod
    def register(username, pwd):
        dbhelper = DBHelper()
        session = dbhelper.get_db_session()
        ret = session.query(User).filter_by(name=username).all()
        if len(ret) > 0:
            return False
        else:
            user = User(name=username, uid=username, pwd=pwd)
            session.add(user)
            session.commit()
            return True
