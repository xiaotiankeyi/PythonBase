# 如果条件成立，那么将 “值1” 赋值给result变量，否则，将“值2”赋值给result变量

"""解释：当判断2>=2时，返回(request),当不等于时返回(response)"""
result = "request" if 2 >= 2 else "response"
print(result)
