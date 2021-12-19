import json

import flask
from flask import render_template
from flask import request

# import os
# base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# html_dir = os.path.join(base_dir + '/python_web/')
# print(html_dir)

server = flask.Flask(__name__)  # 把当前这个python文件，当做一个服务，定义Server(启动服务)


@server.route('/index/', methods=['get'])  # 接口装饰器，get请求
def index():
    return render_template("ajax.html")


@server.route('/index2/', methods=['get'])  # 接口装饰器，get请求
def index2():
    return render_template("ajax_two.html")


@server.route('/index3/', methods=['get'])  # 接口装饰器，get请求
def index3():
    return render_template("ajax_three.html")


@server.route('/string/', methods=['get', 'post'])
def string():
    if request.method == 'GET':
        name = request.args.get('name')
        pwd = request.args.get('pwd')
        print(f'获取url上的参数—>用户:{name},密码:{pwd}')

        res = {'msg': '请求成功！', 'msg_code': 200}
        return json.dumps(res, ensure_ascii=False)

    elif request.method == 'POST':
        print(type(request.data))

        print(request.form)
        print('获取通过x-www-form-urlencoded方式传过来的参数:', request.form['name'])

        res = {'msg': '请求成功！', 'msg_code': 200}
        return json.dumps(res, ensure_ascii=False)


@server.route('/string2/', methods=['post'])
def string2():
    if request.method == 'POST':
        print('如果返回的是json就取值,否侧就None', request.json)
        print(request.data)

        # 把传过来的JSON数据转化为字典
        data = json.loads(request.data)
        print(type(data))
        print('获取通过application/json方式传过来的参数:', data['name'])

        res = {"msg": "请求成功!", "msg_code": "200"}
        print('转化前:', type(res))
        res = json.dumps(res, ensure_ascii=False)

        print('转化后:',type(res))
        return res


if __name__ == "__main__":
    server.run(debug=True)
    pass
