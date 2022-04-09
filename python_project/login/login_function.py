"""实现其登录功能"""

from python_project.output_log import The_log
import json
import os
import sys
import hashlib

BASE_BIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_BIR)

logger = The_log.logger()


def login():
    filename = BASE_BIR + "/registered" + "/user_data.dat"
    with open(filename, 'r') as w:
        user = []
        while True:
            lien_data = w.readline()
            if lien_data == "":
                break
            data = json.loads(lien_data)
            user.append(data)
        # print(user)

    print("\t\t欢迎登录")
    logger.info('欢迎登录')
    tag = True
    while tag:
        username = input(">>>请输入用户名:").strip()
        password = input(">>>请输入密码:").strip()
        m = hashlib.md5()
        m.update(password.encode("utf8"))
        hash = m.hexdigest()
        for users in user:
            if username == users['username'] and hash == users['password']:
                print('\t\t登录成功!!!!')
                logger.info("用户%s,登录成功" % username)
                tag = False
                break
        else:
            print('用户名不存在或密码错误')
            logger.info("用户名不存在或是密码错误")


if __name__ == "__main__":
    logger = The_log.logger()
    # logger.info('登录模块测试日志')
    login()
