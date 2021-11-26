import time

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import Response
import time
from flask import redirect
from flask import url_for
from datetime import datetime
from datetime import timedelta

# 如果想要把客户端的文件名作为服务器上的文件名
from werkzeug.utils import secure_filename

# flask实现from表单文件上传

app = Flask(__name__)


@app.route("/index/")
def index():
    return render_template("send_file.html")


@app.route("/login/", methods=['post'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']
        print(user)
        print(pwd)
        if user == 'jack' and int(pwd) == 123456:
            res_cookies = make_response(redirect(url_for("page")))
            res_cookies.set_cookie('username', 'jack')
            res_cookies.set_cookie('password', '123456', max_age=60)
            time = datetime.now() + timedelta(days=10)
            print(time)
            res_cookies.set_cookie('token', '123456hdjahdauas&qwqwsd',expires=time)

            return res_cookies
        else:
            return render_template("send_file.html")
    else:
        return render_template("send_file.html")


@app.route("/page/")
def page():
    cookies = request.cookies
    return fr"请求头中返回的cookies是{cookies}"

if __name__ == "__main__":
    app.run(debug=True)
