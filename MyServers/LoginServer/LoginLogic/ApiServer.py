import hashlib

from flask_restful import  reqparse, abort, Resource
from MyServers.LoginServer.DataBase.Tables import User
from MyServers.LoginServer.DBHelper.DateBaseHelper import DBHelper
from MyServers.LoginServer.LoginLogic.LoginHelper import Login
from MyServers.LoginServer.LoginLogic.ResponeBean import UserBean, ErrorBean

APIS = {
    'Login': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="APIS {} doesn't exist".format(api_id))


class LoginApi(Resource):

    def get(self, todo_id):
        return APIS[todo_id]

    def post(self):
        args = parser.parse_args()
        name = args['username']
        pwd = args['password']
        pwd = hashlib.sha256(str(pwd).encode('utf-8')).hexdigest()
        user, err = Login.valid_login_get_user(name, pwd)
        if user:
            return UserBean(user.uid, 'test token').__str__()
        else:
            return ErrorBean('login', err).__str__()

