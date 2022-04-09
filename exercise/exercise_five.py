# 遍历文件
import os

# 如何遍历查找出某个文件夹内所有的子文件呢?并且找出某个后缀的所有文件

listdir = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '\\mysql')
print(listdir)

file = []
for i in listdir:
    if i.endswith('.py'):
        file.append(i)
print(file)