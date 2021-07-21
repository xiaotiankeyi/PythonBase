from socket import *

ip_addr = ('127.0.0.1', 8080)
accept_size = 1024

# SOCK_DGRAM表示UDP协议
server = socket(AF_INET, SOCK_DGRAM)
server.bind(ip_addr)    # 绑定IP地址

# 接收客户端发来的"string"，然后转化为大写在发送回客户端

while True:
    # 接收客户端发送过的数据
    data, addr = server.recvfrom(accept_size)
    print(data.decode("utf8"))
    print(addr)

    server.sendto(data.upper(), addr)
