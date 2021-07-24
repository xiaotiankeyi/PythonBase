"""
........学生系统2.0版本......
"""
print(" = " * 40)
print("\t\t\t学生名片管理系统")
print("1:添加学生")
print("2:删除学生")
print("3:修改学生")
print("4:查找学生")
print("5:显示学生")
print("6:退出系统")
print("=" * 40)

student = []
while True:
    print("\t\t请输入需要进行操作的序号")
    num = input(">>>>>>> ").strip()
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
            print("添加成功！！！")

        elif num == 2:
            tar = True
            while tar:
                print("请输入要删除学生的序号: ")
                student_card = input(">>>>>>> ")
                if student_card.isdecimal():
                    student_card = int(student_card)
                    if 0 <= student_card < len(student):
                        key = True
                        while key:
                            confirm = input("确定要删除吗[n/y]: ").strip()
                            if confirm.lower() == 'y':
                                del student[student_card]
                                break
                            elif confirm.lower() == 'n':
                                key = False
                                break
                            else:
                                print("你输入的操作有误,请重新输入 ")
                    else:
                        print("没有该序号,请重新输入>>>")

                elif student_card == 'q':
                    tar = False
                    break
                else:
                    print("你输入的序号不存在,请重新输入 ")

        elif num == 4:
            sign = True
            while sign:
                print("....请输入要查找学生的名字")
                seek_name = input(">>>>> ").strip()
                for n in student:
                    if n["name"] == seek_name:
                        print("姓名\t年龄\t性别")
                        print(
                            "%s\t\t%s\t\t%s" %
                            (n["name"], n["age"], n["sex"]))
                        break
                    elif seek_name == "q":
                        sign = False
                        break
                    else:
                        print("......没有你要查找的学生,请重新输入 ")
        elif num == 5:
            print("\t表中信息如下>>>>")
            result = "姓名\t年龄\t性别"
            print(result.expandtabs(20))
            for n in student:
                result2 = "%s\t%s\t%s" % (n["name"], n["age"], n["sex"])
                print(result2.expandtabs(20))

        elif num == 3:
            pass

        elif num == 6:
            break
    else:
        print("你输入的序号有误,请重新输入...")
