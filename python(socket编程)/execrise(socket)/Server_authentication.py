# _*_coding:utf-8_*_
from socketserver import *
import hmac, os

secret_key = b'linhaifeng bang bang bang'


class Handler(BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        # self.setup()
        try:
            if not self.setup():
                print("链接不合法,,,,")
                self.request.close()
                return
            self.request.sendall('through'.encode("utf8"))
            print("链接合法,,,,")
            self.handle()
        finally:
            self.finish()

    def setup(self):
        """验证客户端的合法性"""
        print("开始验证链接合法性,,,,")

        msg = os.urandom(32)
        self.request.sendall(msg)
        h = hmac.new(secret_key, msg)
        digest = h.digest()
        response = self.request.recv(len(digest))
        return hmac.compare_digest(digest, response)

    def handle(self):
        print('{}认证完成,开始通讯循环操作....'.format(self.client_address))
        while True:
            try:
                data = self.request.recv(1024)
                if not data: break
                print('接收到客户端发来的消息是：', data.decode("utf8"))

                self.request.sendall(data.upper())
            except Exception as e:
                print('{}客服端断开链接'.format(self.client_address))
                break
            pass


if __name__ == '__main__':
    s = ThreadingTCPServer(('127.0.0.1', 8000), Handler)  # 多线程
    # s.allow_reuse_address = True
    s.serve_forever()
    pass

"""合法服务端"""
