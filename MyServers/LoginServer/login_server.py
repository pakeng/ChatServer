from flask import Flask, request
from flask import render_template

from MyServers.LoginServer.DataBase import Tables
from MyServers.LoginServer.LoginLogic.LoginHelper import Login

app = Flask('MyLoginServer')


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        if username and pwd :
            if Login.register(username, pwd):
                return 'Register Success'
            else:
                error = "Register ERROR"
    return render_template('login.html', error=error)


@app.route(r'/registerNew')
def registerNew():
    return 'registerNew'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if Login.valid_login(request.form['username'], request.form['password']):
            return render_template('login_success.html', result={'username': request.form['username']})
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == '__main__':
    print(app.name)
    app.run("0.0.0.0", "8088", True)


