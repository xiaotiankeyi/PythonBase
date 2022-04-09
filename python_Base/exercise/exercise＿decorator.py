# 实现装饰器功能

"""
一:编写函数,（函数执行的时间是随机的）
"""
import os
import time
import random
"""装饰器"""


def handle(func):
    def carry():
        start = time.time()
        time.sleep(random.randint(1, 5))
        func()
        stop = time.time()
        print("执行时间是{}".format(stop - start))

    return carry


@handle
def test():
    print("实现一个随机执行函数的功能")

# test()


"""编写装饰器,为多个函数加上认证的功能（用户的账号密码来源于文件）,要求登录成功一次,后续的函数都无需再输入用户名和密码
注意:从文件中读出字符串形式的字典,可以用eval('{"name":"egon","password":"123"}')转成字典格式"""

current_dic = {'username': None, 'login': False}


def welcome(func):  # func现在是index
    def login(*args, **kwargs):
        if current_dic['username'] and current_dic['login']:
            test = func(*args, **kwargs)  # 运行index并返回值给res
            return test
        tag = True
        while tag:
            username = input("用户名>>>>>> ").strip()
            password = input("密码>>>>>>> ").strip()
            filepath = "C:/Users/admin/PycharmProjects/python/python_Base/func/func_decorator/ID.dat"
            with open(filepath, 'r', encoding='utf8') as file_c:
                for paras in file_c:
                    paras = eval(paras)
                    if username == paras['name'] and password == paras['passwd']:
                        current_dic['username'] = username
                        current_dic['login'] = True
                        res = func(*args, **kwargs)  # 运行index并返回值给res
                        return res
                        # tag = False
                    else:
                        print('用户名或密码错误')
                        continue
    return login


@welcome
def index():
    print("欢迎来到京东主页...")


@welcome
def stopping(name):
    print("这个%s的购物车,,,," % name)
    v = input('请进行操作')


@welcome
def oneself(name):
    print("这是%s的个人中心,,," % name)

# index()
# stopping("产品经理")
# oneself("产品经理")


"""编写装饰器,为多个函数加上认证功能,要求登录成功一次,在超时时间内无需重复登录,超过了超时时间,则必须重新登录"""

user = {'user': None, 'login_time': None, 'timeout': 0.000003, }


def timmer(func):
    def wrapper(*args, **kwargs):
        s1 = time.time()
        res = func(*args, **kwargs)
        s2 = time.time()
        print('%s' % (s2 - s1))
        return res
    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        if user['user']:
            timeout = time.time() - user['login_time']
            if timeout < user['timeout']:
                return func(*args, **kwargs)
        name = input('name>>: ').strip()
        password = input('password>>: ').strip()
        if name == 'egon' and password == '123':
            user['user'] = name
            user['login_time'] = time.time()
            res = func(*args, **kwargs)
            return res
    return wrapper


@auth
def index():
    time.sleep(random.randrange(3))
    print('welcome to index')


@auth
def home(name):
    time.sleep(random.randrange(3))
    print('welcome %s to home ' % name)

# index()
# home('egon')


"""九 编写日志装饰器,实现功能如:一旦函数f1执行,则将消息2017-07-21 11:12:11 f1 run写入到日志文件中,日志文件路径可以指定"""


def logger(logfile):
    def deco(func):
        if not os.path.exists(logfile):
            with open(logfile, 'w'):
                pass

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(logfile, 'a', encoding='utf-8') as f:
                f.write(
                    '%s %s run\n' %
                    (time.strftime('%Y-%m-%d %X'), func.__name__))
            return res
        return wrapper
    return deco


@logger(logfile='log.txt')
def index():
    print('index')


index()
