from socket import *
from threading import Thread

ip_addr = ('127.0.0.1', 8080)  # 服务器IP地址
accept_size = 1024  # 接收最大的字节数

client = socket(AF_INET, SOCK_DGRAM)
client.bind(("", 5050))  # 如果只是接收方一定要绑定ip


def accept():
    """接收信息"""

    while True:
        data, addr = client.recvfrom(accept_size)
        print("\n接收到服务器信息是:", data.decode("utf8"))
        # print(addr)

        # client.close()


def send():
    """发送信息"""
    # print('线程二:', t2.ident)

    while True:
        # sendto发送数据,发送数据需要转变为字节流encode
        val = str(input("请客户端输入发送字母:")).strip()
        client.sendto(val.encode('utf-8'), ip_addr)


if __name__ == "__main__":
    t1 = Thread(target=accept, args="")
    t2 = Thread(target=send, args="")

    # t1.setDaemon(True)
    # t2.setDaemon(True)

    t1.start()
    t2.start()
