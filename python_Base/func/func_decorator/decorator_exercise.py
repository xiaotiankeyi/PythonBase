"""自制装饰器"""

"""实现判断执行的函数是否有返回值,并且获取其返回值...."""


def create(function):
    def add():
        v = function()
        if v is None:  # 这个函数就是use在运行
            print('use没有返回值')
        else:
            return '有返回值,且返回的值为:%s' % v

    return add


@create  # 处理逻辑为:use = create(use)
def use():  # use()
    def output():
        # print("最后输出结果为,,,")
        return '哈哈'

    return output()


print(use())  # 通过return add我获取了函数add的地址,现在运行add

"""实现判断传入的参数有哪些类型"""


def judge(func):
    def realize(name, age):
        print("perform传入得参数有 %s %s" % (type(name), type(age)))

        d = func(name, age)

        return d

    return realize


@judge
def perform(name, age):
    return '自制需要传入参数的装饰器%s, %s' % (name, age)

# v = perform('Tom', 23)
# print(v)
