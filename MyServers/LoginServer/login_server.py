import hashlib
from flask import Flask, request, make_response, url_for
from flask import render_template
from werkzeug.utils import redirect

from MyServers.LoginServer.LoginLogic.ApiServer import LoginApi
from MyServers.LoginServer.LoginLogic.LoginHelper import Login
from flask_restful import Api


loginWebApp = Flask('MyLoginWebServer')
# loginApiApp = Flask('MyLoginApiServer')
api = Api(loginWebApp)


@loginWebApp.route('/')
def root():
    return render_template('index.html')


@loginWebApp.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        try:
            error = " username error"
            username = request.form['username']
            error = " password error"
            pwd = request.form['password']
        except KeyError:
            # return render_template('register.html', error=error)
            login_url = url_for('login')
            return redirect(login_url)

        if username and pwd:
            if Login.register(username, pwd):
                return render_template('login.html')
            else:
                error = "username has registered"
    return render_template('register.html', error=error)


@loginWebApp.route(r'/registerNew')
def registerNew():
    return 'registerNew'


@loginWebApp.route(r'/about')
def about():
    return render_template('about.html')


@loginWebApp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        try:
            error = "username error"
            username = request.form['username']
            error = 'password error'
            pwd = request.form['password']
            pwd_hash = hashlib.sha256(str(pwd).encode('utf-8')).hexdigest()
        except KeyError:
            return render_template("login.html", error=error)

        if Login.valid_login(username, pwd_hash):
            response = make_response(render_template("login_success.html", result={"username": username}))
            response.set_cookie('username', username)
            return response
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


def init_api():
    api.add_resource(LoginApi, "/api/login")


if __name__ == '__main__':
    print(loginWebApp.name)
    # loginWebApp.run("0.0.0.0", "8088", True)
    init_api()
    # print(loginApiApp.name)
    loginWebApp.run("0.0.0.0", "8088", True)


