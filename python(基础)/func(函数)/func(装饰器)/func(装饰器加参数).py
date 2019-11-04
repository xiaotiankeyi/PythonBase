import time

"""装饰器的框架"""


def timmer(func):  # 第一步，目前形参是test
    def wrapper(*args, **kwargs):
        # print(func)
        start_time = time.time()  # 第五步
        ret = func(*args, **kwargs)  # 第六步，运行test
        stop_time = time.time()  # 第九步
        print("运行的时间是%s " % (stop_time - start_time))  # 第十步
        return ret  # "我是test的返回值"

    return wrapper  # 第二步，返回wrapper地址


"""@表示语法堂,@后面加上装饰器>>>>相当于test = timmer(test)"""


@timmer  # 相当于test = timmer(test)
def test(name, age):
    time.sleep(2)  # 第七步
    print("test函数运行完毕, 名字是%s, 年龄是%s" % (name, age))  # 第八步
    return "我是test的返回值"


test("jack", age=22)
