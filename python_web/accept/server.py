from flask import Flask
from flask import request
from flask import render_template
import json


server = Flask(__name__)

@server.route("/index/", methods=['get'])
def index():

    return render_template("home.html")


@server.route('/string/', methods=['get', 'post'])
def string():
    if request.method == 'GET':
        # return '请求成功'
        res = {'msg': '请求成功！', 'msg_code': 200}
        return json.dumps(res, ensure_ascii=False)

    elif request.method == 'POST':

        print(type(request.data))

        # 把传过来的数据转化为字典
        # print(type(json.loads(request.data)))

        print(request.data)

        res = {'msg': '请求成功！', 'msg_code': 200}
        return json.dumps(res, ensure_ascii=False)

if __name__ == "__main__":
    server.run(debug=True)
    pass
