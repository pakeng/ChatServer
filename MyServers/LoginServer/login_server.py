from flask import Flask, request
from flask import render_template

from MyServers.LoginServer.DataBase import Tables
from MyServers.LoginServer.LoginLogic.LoginHelper import Login

app = Flask('MyLoginServer')


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/register')
def register():
    return 'success'


@app.route(r'/registerNew')
def registerNew():
    return 'registerNew'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if Login.valid_login(request.form['username'], request.form['password']):
            # return Login.log_the_user_in(request.form['username'])
            return render_template('login_success.html', result={'username': request.form['username']})
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == '__main__':
    print(app.name)
    Tables.create_tables()
    # app.run("0.0.0.0", "8088", True)


