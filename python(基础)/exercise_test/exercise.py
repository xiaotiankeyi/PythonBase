"""
要求：
    1、打印省、市、县三级菜单
    2、可返回上一级
    3、可随时退出程序
"""

# def handle():
#     paras = {"response": "request", 12: ["lower", "upper"]}
#     for reception in paras.items():
#         """字典循环迭代出来的键值对为元组"""
#         print(reception, type(reception))
#
#     paras = {"response": "request", 12: ["lower", "upper"]}
#     for reception in paras.values():
#         """字典迭代出来的values值为原数据类型"""
#         print(reception, type(reception))

# handle()

# info_list = [
#     {'name': 'jack', 'tel': '18172745976', 'qq': '45456154465'},
#     {'name': 'tom', 'tel': '13122225555', 'qq': '45612254895'}
# ]

# print(info_list)

def modify_info(info_list):
    """修改学生信息"""
    tag = True
    while tag:
        modify_num = input("请输入你要修改的学生的序号： ")
        if modify_num.isdecimal():
            modify_num = int(modify_num)
            if 0 <= modify_num < len(info_list):
                v = info_list[modify_num]
                print(v)
                for k, y in enumerate(v.keys(), ):
                    print(k, y)
                # tag = True
                while tag:
                    altar = input("请输入你所要修改信息的序号： ").strip()  # 要修改所选信息的序号
                    if altar.isdecimal():
                        altar = int(altar)
                        if altar == 0:
                            def new_user():
                                global tag
                                new_name = input("请输入新的名字： ").strip()
                                for temp_info in info_list:
                                    if new_name == temp_info['name']:
                                        print("此用户名已经被占用,请重新输入----------------")
                                        return new_user()
                                else:
                                    info_list[modify_num]['name'] = new_name
                                    print("修改成功>>>",info_list[modify_num])
                                    tag = False

                            return new_user()

                        elif altar == 1:
                            info_list[modify_num]['tel'] = input("请输入新的手机号： ")
                            print("修改成功>>>",info_list[modify_num])
                            tag = False

                        elif altar == 2:
                            info_list[modify_num]['qq'] = input("请输入新QQ： ")
                            print("修改成功>>>",info_list[modify_num])
                            tag = False

                        else:
                            print("你所选择要修改的序号不存在,请重新输入")
                            continue
                    else:
                        print("你输入信息错误,请再次输入")

        else:
            print("输入序号有误,请重新输入")


if __name__ == "__main__":
    modify_info()
    # print(info_list)
