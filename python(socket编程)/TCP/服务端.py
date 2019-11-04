"""
1、内存的区分为"用户态","内核态",操作系统驱动流程为读取"内核态"的代码到内存
2、应用收发消息时就是在操作自己的"缓存区"......
"""
from socket import *
import socket

# socket.AF_INET基于网络，socket.SOCK_STREAM基于tcp/ip协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8080))  # 提供连接信息

phone.listen(3)  # 半连接池
while True:

    print("等待连接........")
    conn, addr = phone.accept()  # 三次握手,建立连接
    print(addr,"连接成功")
    while True:
        try:
            data = input(">>>：").strip()
            if data != 'q':
                conn.send(data.upper().encode('utf8'))
                massage = conn.recv(1024)
                values = massage.decode("utf8")
                if values == 'q':
                    print('接收到客户端发来的消息是：', values, "--->客户端断开连接")
                    break
                else:
                    print('接收到客户端发来的消息是：', values, )
            else:
                conn.send(data.upper().encode('utf8'))
                break
        except Exception as e:
            print(e)
            break

    conn.close()  # 四次挥手
    # print("=======")
    # phone.close()
pass