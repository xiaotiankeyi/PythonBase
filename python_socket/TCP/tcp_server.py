from socket import *
import subprocess
import struct

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)     # 设置最大链接数

while True:
    conn, addr = tcp_server.accept()    # 等待接收socket连接，conn新的套节字用于数据的收发
    print('新的客户端链接', addr)
    while True:
        # 收
        try:
            cmd = conn.recv(buffer_size)
            if not cmd:
                break
            print('收到客户端的命令', cmd)

            # 执行命令，得到命令的运行结果cmd_res
            res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()

            # 发
            if not cmd_res:
                cmd_res = '执行成功'.encode('utf-8')

            length = len(cmd_res)
            # print('输出:', length)
            data_length = struct.pack('i', length)
            conn.send(data_length)
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            conn.close()
            break
    pass
