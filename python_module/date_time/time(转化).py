import time

def handle():
    """时间戳要转化为格式化字符串时间"""
    a = time.time()
    print("获取当前时间戳 %s" % a)

    """把时间戳转化为结构化时间"""
    g = time.localtime()
    print("当前的结构化时间为 {}".format(g))

    """把结构化时间转化为格式化字符串时间"""
    r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("当前的格式化字符串时间为 %s" % r)

handle()

print("=" * 40)

def variable():
    """把字符串时间转化为时间戳，，第一步先转化为结构化时间，在转化为时间撮"""

    r = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("获取当前的字符串时间 %s" % r)

    """把字符串时间转化为结构化时间，，"""
    g = time.strptime(r, "%Y-%m-%d %H:%M:%S")
    print("把字符串时间转化为结构化时间 {}".format(g))

    """结构化时间转化为时间戳"""
    f = time.mktime(g)
    print("把结构化时间转化为时间戳 %s" % f)

variable()

# print(time.ctime())
# print(time.localtime())