import requests
import json

data = {
    'name': 'java'
}

obj = requests.get(
    url="https://www.v2ex.com/api/nodes/show.json?",
    params=data,
    headers=None,
    cookies=None,
    timeout=None)
# print(obj.text, type(obj.text))

'''把相应结果转化为dictionary'''
formatJson = json.loads(obj.text)
print(formatJson, type(formatJson))

'''转化为二进制数据'''
a = obj.content
print('获取二进制数据:', a, type(a))

'''响应的属性'''
print('响应状态:', obj.status_code, type(obj.status_code))
print('响应头:', obj.headers, type(obj.headers))
print('响应cookies:', obj.cookies, type(obj.cookies))
print('重定项与请求历史:', obj.history, type(obj.history))
