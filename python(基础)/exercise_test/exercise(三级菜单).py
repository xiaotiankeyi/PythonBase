"""
要求：
    1、打印省、市、县三级菜单
    2、可返回上一级
    3、可随时退出程序
"""
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

tar = True


def handle():
    while tar:
        # 显示第一级
        def handle_2():
            for key in menu:
                print(key)
            province = input("请输入省>>>>>>> ").strip()
            if province in menu:
                for key_province in menu[province]:
                    print(key_province)

                def handle_3():
                    city = input("请输入市区或者...[q]...返回省城>>>>>>>")
                    if city in menu[province]:
                        while True:
                            for key_city in menu[province][city]:
                                print(key_city)

                            # -----------------------------------------------------------------
                            def handle_4():
                                county = input("请输入县区或...[a]...返回市区或者输入...[c]...返回省城>>>>>>>")
                                if county in menu[province][city]:
                                    while True:
                                        for key_county in menu[province][city][county]:
                                            print(key_county)
                                        break

                                    """返回省城"""
                                elif county == 'c':
                                    print("\t\t\t", "....你选择了%s返回,请再次你选择需要查看的省城....." % county)
                                    handle_2()

                                    """返回市区"""
                                elif county == "a":
                                    print("\t\t\t", "....你选择了%s返回,请再次你选择需要查看的市区........." % county)
                                    handle_3()
                                    """退出"""
                                elif county != "c" and county != "a":
                                    pass

                            return handle_4()

                        """返回省城"""
                    elif city == "q":
                        print("\t\t\t", ".........你选择了%s返回,请再次选择需要查看的省城............." % city)
                        handle_2()
                        """退出"""
                    elif city != "q" and city in menu[province]:
                        pass

                return handle_3()
                """退出"""
            elif province in menu:
                pass

        return handle_2()


handle()
"""第二种写法"""
# tar = True
# while tar:
#     for key in menu:
#         print(key)
#
#     province = input("请选择省城>>>>> ").strip()
#     if province in menu:
#         for key_province in menu[province]:
#             print(key_province)
#
#         city = input("请选择市区>>>>>> ").strip()
#         if city in menu[province]:
#             while True:
#                 for key_city in menu[province][city]:
#                     print(key_city)
#
#                 county = input("请选择县城>>>> ").strip()
#                 if county in menu[province][city]:
#                     while True:
#                         for key_county in menu[province][city][county]:
#                             print(key_county)
#                         choice = input("再次输入>>>> ").strip()
#                         # print("已在最底层")
#                         if choice == 'b':
#                             tar = False
#                             break
#                         else:
#                             print("已在最底层")
