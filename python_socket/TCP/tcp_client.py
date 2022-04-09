from socket import *
import struct
from functools import partial
ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)     # 连接,拨打服务器

while True:
    cmd = input('>>: ').strip()
    if not cmd:
        continue
    if cmd == 'quit':
        break

    tcp_client.send(cmd.encode('utf-8'))

    # 解决粘包
    length_data = tcp_client.recv(4)
    # print('输出:', length_data)

    length = struct.unpack('i', length_data)[0]
    # print('输出二:', length)

    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        recv_msg += tcp_client.recv(buffer_size)
        recv_size = len(recv_msg)

    print('命令的执行结果是 ', recv_msg.decode('utf-8'))
tcp_client.close()
