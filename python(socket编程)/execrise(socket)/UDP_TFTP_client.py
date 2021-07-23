
# struct模块可以按照指定格式将python数据转换为字符串，该字符串为字节流
# pack()包装字节流, unpack()解析字节流, calcsize()计算给定的格式占用多少字节
# TFTP是一个传输文件的简单协议，它基于UDP协议而实现。
# 2、特点简单、占用资源少、基于UDP实现、端口号为69、适合在局域网内传输小文件。

from socket import *
import struct


def UDP_client():
    server_ip_port = ('127.0.0.1', 69)        # 服务端IP地址
    buffer_size = 1024

    udp_client = socket(AF_INET, SOCK_DGRAM)
    # udp_client.bind(("", 5050))
    filename = "../picture.jpeg"     # 服务器文件地址
    pull_room = "picture.jpeg"
    # udp_client.sendto('hello world'.encode(), server_ip_port)
    request_data = struct.pack(
        "!H%dsb5sb" %
        len(filename),
        1,
        filename.encode(),
        0,
        "octet".encode(),
        0)
    udp_client.sendto(request_data, server_ip_port)     # 第一步发送下载信息

    f = open(pull_room, 'ab')
    while True:
        try:
            dataInfo, serverInfo = udp_client.recvfrom(buffer_size)

            handle_card, ack_num = struct.unpack(
                "!HH", dataInfo[:4])       # 获取操作码和块编号

            print("操作码{}\t块编号{}\t服务器端口{}\t数据长度{}".format(
                handle_card, ack_num, serverInfo[1], len(dataInfo[4:])))
            # break
            if int(handle_card) != 5:
                f.write(dataInfo[4:])
                if len(dataInfo) < 516:
                    break
                right_data = struct.pack("!HH", 4, ack_num)
                udp_client.sendto(right_data, serverInfo)
            else:
                print('接收出错')

        except Exception as e:
            print(e)

    udp_client.close()


if __name__ == "__main__":
    UDP_client()
