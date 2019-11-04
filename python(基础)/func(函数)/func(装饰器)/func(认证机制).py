user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]
current_dic={'username':None,'login':False}

def welcome(func):      #func现在是index
    def login(*args, **kwargs):
        if current_dic['username'] and current_dic['login']:
            test = func(*args, **kwargs)  # 运行index并返回值给res
            return test

        username = input("用户名>>>>>> ").strip()
        password = input("密码>>>>>>> ").strip()
        for paras in user_list:
            if username == paras['name'] and password == paras['passwd']:
                current_dic['username'] = username
                current_dic['login'] = True
                res = func(*args, **kwargs)     #运行index并返回值给res
                return res
            else:
                print('用户名或密码错误')
    return login

@welcome
def index():
    print("欢迎来到京东主页...")

"""不使用语法堂的表现形式"""
# ret = welcome(index)    #运行结束，获取login地址在赋值给ret
# ret()       #运行login

@welcome
def stopping(name):
    print("这个%s的购物车。。。。" % name)

"""不使用语法堂的表达形式"""
# ret = welcome(stopping)
# ret("产品经理")

@welcome
def oneself(name):
    print("这是%s的个人中心。。。" % name)

index()
stopping("产品经理")
oneself("产品经理")