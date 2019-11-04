"""
........学生系统2.0版本......
"""
import time
import logging
# import logging_test
import realize_logging

logger = logging.getLogger("测试")


def handle():
    print("=" * 40)
    print("\t\t\t学生名片管理系统")
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查找学生")
    print("5:显示学生")
    print("6:退出系统")
    print("=" * 40)

    dic = {
        '1': '添加学生',
        '2': '删除学生',
        '3': '修改学生',
        '4': '查找学生',
        '5': '显示学生',
        '6': '退出系统'
    }
    student = []
    while True:
        print("\t\t请输入需要进行操作的序号")
        num = input(">>>>>>> ").strip()
        logger.info("用户选择的操作是·{}>>>>{}".format(num, dic[num]))
        if num.isdecimal():
            num = int(num)
            if num == 1:
                collect = {}

                name = input("请输入要添加学生的名字：").strip()
                age = input("请输入要添加的学生年龄：").strip()
                sex = input("请输入要添加的学生性别: ").strip()

                collect["name"] = name
                collect["age"] = age
                collect["sex"] = sex
                student.append(collect)
                # print("添加成功！！！")
                logger.info("successfully added")

            elif num == 2:
                tag = True
                while tag:
                    print("请输入要删除学生的序号或[q]退出: ")
                    student_card = input(">>>>>>> ")
                    logger.info("用户输入的信息为·{}".format(student_card))
                    if student_card.isdecimal():
                        student_card = int(student_card)
                        if 0 <= student_card < len(student):
                            while tag:
                                confirm = input("确定要删除吗[n/y]: ").strip()
                                logger.info("用户选择是·{}".format(confirm))
                                if confirm.lower() == 'y':
                                    del student[student_card]
                                    logger.info("successfully delete")
                                    tag = False
                                elif confirm.lower() == 'n':
                                    tag = False
                                else:
                                    print("你输入的操作有误,请重新输入 ")
                        else:
                            print("没有该序号,请重新输入>>>")

                    elif student_card == 'q':
                        tag = False
                    else:
                        print("你输入的序号不存在,请重新输入>>> ")

            elif num == 4:
                tag = True
                while tag:
                    print("请输入要查找学生的名字或[q]退出")
                    seek_name = input(">>>>> ").strip()
                    logger.info("用户输入信息为·{}".format(seek_name))
                    for n in student:
                        if n["name"] == seek_name:
                            print("姓名\t年龄\t性别")
                            print("%s\t\t%s\t\t%s" % (n["name"], n["age"], n["sex"]))
                            tag = False
                            break
                        elif seek_name == "q":
                            tag = False
                            break
                    else:
                        print("...没有你要查找的学生,请重新输入 ")

            elif num == 5:
                print("\t表中信息如下>>>>")
                result = "姓名\t年龄\t性别"
                print(result.expandtabs(20))
                for n in student:
                    result2 = "%s\t%s\t%s" % (n["name"], n["age"], n["sex"])
                    print(result2.expandtabs(20))

            elif num == 3:
                logger.info("操作3的功能正在开发中........")
                continue

            elif num == 6:
                break

        else:
            print("你输入的序号有误,请重新输入...")


if __name__ == "__main__":
    # logging_test.load_my_logging_cfg()    #第一种日志格式
    logger = realize_logging.handle()  # 第二种日志格式
    handle()
