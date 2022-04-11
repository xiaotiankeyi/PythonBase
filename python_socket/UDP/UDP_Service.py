from socket import *
from threading import Thread

ip_addr = ('127.0.0.1', 8080)
accept_size = 1024

# SOCK_DGRAM表示UDP协议
server = socket(AF_INET, SOCK_DGRAM)
server.bind(ip_addr)  # 绑定IP地址


# 接收客户端发来的"string",然后转化为大写在发送回客户端
addr = ""


def accept():
    """接收客户端发送来的信息"""
    while True:
        # 接收客户端发送过的数据
        global addr
        data, addr = server.recvfrom(accept_size)
        print("\n接收到客户端信息是:", data.decode("utf8"))
        # print(addr)


def send():
    """发送信息给客户端"""
    while True:
        val = str(input("请输入发送给客户端的字母:"))
        server.sendto(val.encode('utf-8'), addr)


if __name__ == "__main__":

    t1 = Thread(target=accept, args="")
    t2 = Thread(target=send, args="")

    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
