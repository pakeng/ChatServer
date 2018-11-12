from MyServers.LoginServer.DataBase.Tables import User
from MyServers.LoginServer.DBHelper.DateBaseHelper import DBHelper
import time
import hashlib

dbHelper = DBHelper()
session = dbHelper.get_db_session()


class Login(object):

    @staticmethod
    def valid_login(name, pwd):
        user = session.query(User).filter_by(name=name).first()
        if user and user.pwd == pwd:
            return True
        else:
            return False

    @staticmethod
    def valid_login_get_user(name, pwd):
        err = None
        user = session.query(User).filter_by(name=name).first()
        if user:
            if user.pwd == pwd:
                return user, err
            err = "password error"
        else:
            err = "user not exist"
        return None, err

    @staticmethod
    def log_the_user_in(account):

        return True

    @staticmethod
    def register(username, pwd):
        ret = session.query(User).filter_by(name=username).all()
        if len(ret) > 0:
            return False
        else:
            uid = Login.create_uid()
            pwd_hash = hashlib.sha256(str(pwd).encode('utf-8')).hexdigest()
            user = User(name=username, uid=uid, pwd=pwd_hash)
            session.add(user)
            session.commit()
            return True

    @staticmethod
    def create_uid():
        m = hashlib.md5(str(time.clock()).encode('utf-8'))
        return m.hexdigest()
