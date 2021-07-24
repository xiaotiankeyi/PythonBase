
import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))  # 发送连接

while True:
    data = phone.recv(1024)
    value = data.decode("utf8")
    if value == 'Q':
        print('收到服务端发来的消息是：', value, "--->服务端断开连接")
        break
    else:
        print('收到服务端发来的消息是：', value)
    msg = input(">>>：").strip()
    if msg != 'q':
        phone.send(msg.encode('utf8'))
    else:
        phone.send(msg.encode('utf8'))
        break

phone.close()
