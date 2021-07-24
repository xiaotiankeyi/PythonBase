"""解决并发问题........."""

from socketserver import *


class Handler(BaseRequestHandler):

    def handle(self):
        # print('conn is:', self.request)
        # print('poet is:', self.client_address)

        while True:
            try:
                # 收消息
                data = self.request.recv(1024)
                if not data:
                    break
                print('收到客户端{}的消息是'.format(self.client_address), data, )

                # 发消息
                self.request.sendall(data.upper())

            except Exception as e:
                print(self.client_address, '连接断开......')
                break

    def setup(self):
        print(self.client_address, '建立连接.....')

    pass


if __name__ == "__main__":
    s = ThreadingTCPServer(('127.0.0.1', 8080), Handler)  # 多线程
    s.serve_forever()
