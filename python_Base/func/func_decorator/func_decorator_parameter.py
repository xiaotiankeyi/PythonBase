# 装饰器加参数
import time

"""装饰器的框架,创建一个统计函数运行时间的功能"""


def timmer(func):  # 第一步，目前形参是orange
    print('函数名称1:', func.__name__)

    def wrapper(*args, **kwargs):

        start_time = time.time()  # 第五步
        ret = func(*args, **kwargs)  # 第六步，运行orange
        stop_time = time.time()  # 第九步

        # print("运行的时间是%s " % (stop_time - start_time))  # 第十步
        # return ret  # "ret接收orange运行后的返回值"

        return "运行的时间是%s " % (stop_time - start_time)

    return wrapper  # 第二步，返回wrapper地址


"""@表示语法堂,@后面加上装饰器>>>>相当于orange = timmer(orange)"""


@timmer  # 相当于orange = timmer(test)
def orange(name, age):
    time.sleep(2)  # 第七步
    print("orange函数运行完毕, 名字是%s, 年龄是%s" % (name, age))  # 第八步
    return "我是orange的返回值"


if __name__ == "__main__":
    result = orange("jack", age=22)
    print(result)
    pass
