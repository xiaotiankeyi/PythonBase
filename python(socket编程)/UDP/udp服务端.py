from socket import *

ip_addr = ('127.0.0.1', 8080)
accept_size = 1024

server = socket(AF_INET, SOCK_DGRAM)
server.bind(ip_addr)

while True:
    data, addr = server.recvfrom(accept_size)
    print(data.decode("utf8"))

    server.sendto(data.upper(), addr)