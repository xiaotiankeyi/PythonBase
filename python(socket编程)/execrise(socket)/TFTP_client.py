# struct模块可以按照指定格式将python数据转换为字符串，该字符串为字节流
# pack()包装字节流, unpack()解析字节流, calcsize()计算给定的格式占用多少字节

from socket import *
import struct
from functools import partial

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    filename = input()
    file = {
        'filename': filename,
        'filesize': 1024
    }
    pass

tcp_client.close()
