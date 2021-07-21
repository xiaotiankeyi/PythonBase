
from socket import *

ip_addr = ('127.0.0.1', 8080)
accept_size = 1024      # 接收最大的字节数

client = socket(AF_INET, SOCK_DGRAM)
client.bind(("", 5050))     # 如果只是接收方一定要绑定ip

while True:
    msg = input(">>>:").strip()

    # sendto发送数据，发送数据需要转变为字节流encode
    client.sendto(msg.encode('utf8'), ip_addr)

    data, addr = client.recvfrom(accept_size)
    print(data.decode("utf8"))
    print(addr)

    # client.close()
