import struct
from socket import *


def UDP_server():
    global f
    global filename
    ip_port = ('', 69)
    buffer_size = 1024

    udp_server = socket(AF_INET, SOCK_DGRAM)
    udp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    udp_server.bind(ip_port)

    recvdata, clientInfo = udp_server.recvfrom(buffer_size)  # 第一次接收首次连接信息

    server_send = socket(AF_INET, SOCK_DGRAM)

    try:
        if struct.unpack("!b5sb", recvdata[-7:]) == (0, b"octet", 0):
            handle_card = struct.unpack("!H", recvdata[:2])  # 读取操作码
            filename = recvdata[2:-7].decode()  # 文件名
            print("操作码{}\t文件名:{}".format(handle_card, filename))
            f = open(filename, 'rb')
    except Exception as e:
        val = str(e)
        errorInfo = struct.pack("!HH5sb", 5, 5, "文件不存在".encode(), 0)

        # 发送错误操作信息
        udp_server.sendto(errorInfo, clientInfo)
        exit()
    else:
        file_card = 0
        while True:
            # 发送文件
            readFileData = f.read(512)  # 读取文件
            file_card += 1  # 生成块变编号
            print("块编号", file_card)

            send_data = struct.pack("!HH", 3, file_card) + readFileData  # 数据打包
            server_send.sendto(send_data, clientInfo)  # 数据发送

            # 判断是否发送完成
            if len(send_data) < 516:
                print("用户" + str(clientInfo), end="")
                print(":下载" + filename + "完成")
                break

            # 接收客户端返回的确认包数据
            recvdata, clientInfo = server_send.recvfrom(buffer_size)
            response_card, flieNum_card = struct.unpack(
                "!HH", recvdata[:4])  # 获取确认包的操作码和块编号
            if response_card != 4 or flieNum_card != file_card:
                print("文件传输错误。。。。")
                break

    f.close()
    server_send.close()
    udp_server.close()
    exit()


if __name__ == "__main__":
    UDP_server()
