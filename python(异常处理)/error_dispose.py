"""异常处理即错误捕获框架"""

try:
    pass

except ValueError as a:
    pass

except Exception as e:      #万能异常捕获
    pass

else:       #没异常就运行else
    pass

finally:    #有没有异常都会运行
    pass

"""主动触发异常"""
try:
    raise TypeError("")

except Exception as s:
    pass

"""断言"""
i = 1
assert i != 1
#类似于
# if i == 1:
#     raise AssertionError