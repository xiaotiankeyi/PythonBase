from socket import *
import hmac,os

secret_key=b'linhaifeng bang bang bang'
def conn_auth(conn):
    '''
    验证客户端到服务器的链接
    :param conn:
    :return:
    '''
    msg=conn.recv(32)
    h=hmac.new(secret_key,msg)
    digest=h.digest()
    conn.sendall(digest)
def client_handler(ip_port,bufsize=1024):
    tcp_socket_client=socket(AF_INET,SOCK_STREAM)
    tcp_socket_client.connect(ip_port)

    conn_auth(tcp_socket_client)

    through = tcp_socket_client.recv(1024)
    if through.decode("utf8") == 'through':
        while True:
                data=input('>>: ').strip()
                if not data:continue
                if data == 'quit':break
                tcp_socket_client.sendall(data.encode('utf-8'))
                respone=tcp_socket_client.recv(bufsize)
                print(respone.decode('utf-8'))
    else:print('你的链接不合法,,,')

    tcp_socket_client.close()

if __name__ == '__main__':
    ip_port=('127.0.0.1',8000)
    bufsize=1024
    client_handler(ip_port,bufsize)

"""合法客户端,,,,,"""