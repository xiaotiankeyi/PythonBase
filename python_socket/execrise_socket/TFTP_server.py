from socket import *
import struct

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    conn, addr = tcp_server.accept()
    print('新的客户端链接', addr)
    while True:
        # 收
        try:

            pass
        except Exception as e:
            print(e)
            break
    pass
