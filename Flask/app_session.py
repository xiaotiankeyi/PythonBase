from flask import session, request, render_template, redirect, url_for
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    if session.get('username'):
        cookies = request.headers['Cookie']
        name = session.get('username')
        print(cookies)
        print(name)
        return """
                <p>当前是首页,用户已经登录<p>
                <p>cookies:'%s'<p>
                """ % cookies
    else:
        return """
                <p>当前是首页,用户没登录<p>
                <a href="/login/">点击跳转登录<a>
                """


@app.route("/login/", methods=['get', 'post'])
def login():
    if request.method == "POST":
        session['username'] = request.form['name']
        session['password'] = request.form['pwd']
        return redirect(url_for('index'))
    else:
        return """
                <p>登录界面<p>
                <form action='/login/' method='post'>
                    <p>用户名:<input type='text' name='name' value=''><p>
                    <p>密码:<input type='password' name='pwd' value=''><p>
                    <p><input type='submit' value='提交'><p>
                <form>
                """


if __name__ == "__main__":
    app.run(debug=True)
