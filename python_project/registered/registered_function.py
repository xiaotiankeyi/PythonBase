"""注册功能"""

from python_project.output_log import The_log
import json
import os
import sys
import hashlib
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

logger = The_log.logger()


def registered():
    logger.info('\t\t欢迎来到注册首页')
    username = input('>>>请输入用户名: ').strip()
    password = input('>>>请输入密码: ').strip()
    telephone = input('>>>请输入电话号码: ').strip()
    m = hashlib.md5()
    m.update(password.encode('utf8'))
    hash = m.hexdigest()
    dic = {}
    dic["username"] = username.lower()
    dic["password"] = hash
    dic["telephone"] = telephone

    def check_code():
        checkcode = ''
        for i in range(4):
            current = random.randint(0, 4)
            if current != i:
                temp = chr(random.randint(65, 90))
            else:
                temp = random.randint(0, 9)
            checkcode += str(temp)
        return checkcode

    while True:
        code = check_code()
        print("你的验证码为 --->>>", code)
        verify = input('>>>请输入验证码: ').strip()
        if verify.upper() == code:
            j = json.dumps(dic)
            file = 'user_data.dat'
            with open(file, 'a+') as f:
                f.write(j + '\n')
                # f.write(j)
            logger.info("用户%s,注册成功" % username)
            print('succeed')
            break
        else:
            print('验证码输入错误,请重新输入.....')

    # return check_code()


if __name__ == "__main__":
    logger = The_log.logger()
    # logger.info('注册模块测试输出')
    registered()
