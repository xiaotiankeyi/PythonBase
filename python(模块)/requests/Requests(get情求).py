import requests
import json

data = {
    'name':'java'
}

obj = requests.get("https://www.v2ex.com/api/nodes/show.json?", params=data)
# print(obj.text, type(obj.text))

'''把相应结果转化为dictionary'''
formatJson = json.loads(obj.text)
print(formatJson, type(formatJson))

'''转化为二进制数据'''
print('获取二进制数据:', obj.content)

'''响应的属性'''
print(obj.status_code, type(obj.status_code))
print(obj.headers, type(obj.headers))
print(obj.cookies, type(obj.cookies))
print(obj.history, type(obj.history))