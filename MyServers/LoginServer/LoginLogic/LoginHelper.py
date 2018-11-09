from MyServers.LoginServer.DataBase.Tables import User
from MyServers.LoginServer.DBHelper.DateBaseHelper import DBHelper


class Login(object):

    @staticmethod
    def valid_login(name, pwd):
        dbhelper = DBHelper()
        session = dbhelper.get_db_session()
        session.query(User).filter_by()
        ret = session.query(User).filter_by(name=name).first()
        if ret.pwd == pwd:
            return True
        else:
            return False

    @staticmethod
    def log_the_user_in(account):

        return True
