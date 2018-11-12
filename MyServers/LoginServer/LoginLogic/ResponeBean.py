import json
import time


class UserBean(object):
    def __init__(self, uid, token):
        self._uid = uid
        self._token = token
        self._login_time = time.process_time()

    def __str__(self):
        return '{"uid": "%s", "code": 1000, "token": "%s"}' % (self._uid, self._token)


class ErrorBean(object):
    def __init__(self, name, msg):
        self._name = name
        self._msg = msg

    def __str__(self):
        return '{"name": "%s", "code": 1001, "msg": "%s"}' % (self._name, self._msg)


if __name__ == '__main__':
    err = ErrorBean('login', "password error")
    print(err)
    user = UserBean('123', 'hhh')
    print(user)
