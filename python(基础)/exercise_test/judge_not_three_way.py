"""判断是否为空的三种方法"""
string = None

# print(string is None)
#
# if string is None:
#     print("is ok")
# else:
#     print("is not")
#
# print(not string)
# if not string:
#     print("is ok")
# else:
#     print("is not")


print(not string is None)

if not string is None:
    print("is ok")
else:
    print("is not")
