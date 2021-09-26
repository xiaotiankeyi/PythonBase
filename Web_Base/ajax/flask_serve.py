import json
import flask
from flask import render_template
from flask import request

server = flask.Flask(__name__)  # 把当前这个python文件，当做一个服务，定义Server(启动服务)


@server.route('/index/', methods=['get'])  # 接口装饰器，get请求
def index():
    # return render_template("ajax.html")
    return render_template("ajax_two.html")


@server.route('/string/', methods=['get', 'post'])
def string():
    if request.method == 'GET':
        # return '请求成功'
        res = {'msg': '请求成功！', 'msg_code': 0}
        return json.dumps(res, ensure_ascii=False)

    elif request.method == 'POST':
        # 把传过来的数据转化为字典
        # print(type(json.loads(request.data)))
        print(request.data)

        res = {'msg': '请求成功！', 'msg_code': 0}
        return json.dumps(res, ensure_ascii=False)


if __name__ == "__main__":
    server.run(debug=True)
    pass
