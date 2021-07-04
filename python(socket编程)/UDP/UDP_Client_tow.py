
from socket import *

ip_addr = ('127.0.0.1', 8080)
accept_size = 1024

client = socket(AF_INET, SOCK_DGRAM)

# 输入一个"string"，发送给服务端

while True:
    msg = input(">>>:").strip()
    client.sendto(msg.encode('utf8'), ip_addr)

    data, addr = client.recvfrom(accept_size)
    print(data.decode("utf8"))
