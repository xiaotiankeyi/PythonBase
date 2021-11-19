"""os模块是与操作系统交互的一个接口"""

import os
import time

"""获取当前模块执行的目录"""
print(os.getcwd())

"""可生成多层递归目录"""
# os.makedirs("dirname1/dirname2")

"""可递归删除空目录,上级目录也为空也就删除，以此类推"""
time.sleep(2)
# os.removedirs(r"C:/Users/admin/PycharmProjects/python/python_module/os/dirname1/dirname2")


def handle():
    """生成单级目录,相当于创建一个目录相当于mkdir dirname"""
    os.mkdir(" ")
    """删除单级空目录,如果有内容就没法删除"""
    os.rmdir(" ")
    """删除一个文件"""
    os.remove(" ")
    """重命名文件及目录"""
    os.rename(" ", " ")


"""运行shell命令,直接显示"""
# os.system("bash command")

"""获取系统环境变量"""
v = os.environ

"""获取目录下的所有文件及目录"""
print(os.listdir(r"C:\Users\admin\PycharmProjects\python_study\python_module"))

"""获取文件目录信息"""
print(os.stat(r"C:\Users\admin\PycharmProjects\python_study\python_module"))

"""返回path目录,可以返回上一级"""
vv = os.path.dirname(os.path.dirname(__file__))
print(vv)

"""返回path最后的文件名"""
g = os.path.basename("C:/Users/admin/PycharmProjects/python/python_Base")
print(g)

"""目录路径拼接,将多个路径组合后返回"""
f = r"C:Users\admin\PycharmProjects\python_study"
h = r"python_module\os(路径模块)\python(os模块).py"
y = os.path.join(f, h)
print(y)

"""获取文件或目录最后一次的存取时间"""
t = os.path.getatime("os_base.py")
print(t)

"""获取文件或目录最后一次的修改时间"""
r = os.path.getmtime("os_base.py")
print(r)

"""返回文件或目录的大小"""
c = os.path.getsize("os_base.py")
print(c)

"""判断路径下的文件是否存在"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(BASE_DIR, 'test.txt')
# print(BASE_DIR)
print(os.path.exists(base_path))

"""判断是否为一个目录"""
print(os.path.isdir(BASE_DIR))

"""判断是否是文件"""
print(os.path.isfile(BASE_DIR))

"""返回文件的信息"""
print(os.stat(base_path).st_size)
