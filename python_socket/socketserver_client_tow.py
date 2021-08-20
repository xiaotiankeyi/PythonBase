
from socket import *

ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input('>>: ').strip()
    if not cmd:
        continue
    if cmd == 'quit':
        break

    tcp_client.send(cmd.encode('utf-8'))

    data = tcp_client.recv(buffer_size)

    print('服务端返回的的执行结果是: ', data.decode('gbk'))
tcp_client.close()
pass
