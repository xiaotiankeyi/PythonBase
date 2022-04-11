import time

# print(time.localtime(time.time()))

current = time.time()
print("当前时间的时间戳为{}".format(current))

localtime = time.localtime()
print("当前结构化的本地时间为:{}".format(localtime))

"""把结构化时间转化为格式化的字符串时间,,,,"""
response = time.asctime(time.localtime(time.time()))
print("第一种------获取格式化字符串的时间为:{}".format(response))

"""自定义格式化的字符串时间成2019-07-23 11:45:39形式"""
print("第二种----自定义格式化的字符串时间", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 将格式化的时间字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 将字符串时间转化为结构化时间
print(time.strptime("2019-07-31 19:45:17", "%Y-%m-%d %H:%M:%S"))

# 将结构化时间转化为时间撮
print(time.mktime(time.localtime()))

