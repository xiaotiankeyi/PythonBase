'''
列表:
        定义:[]内可以有多个任意类型的值,逗号分隔
        概念:
            1、列表里每个元素都是可变的
            2、列表中的元素是有序的,也就是说每个元素都有一个位置
            3、列表可以容纳任何对象
常用操作:
            >索引
            >切片
            >追加
            >删除
            >长度
            >循环
            >包含
'''


def list_collection():
    # ___创建列表___
    name_list = ['jack', 'Tom', 'alex', 'eric']
    # 或
    lists = list(['jack', 'Tom', 'alex', 'eric'])

    # ___[0]___查看下标为(0-1)的字符串.....
    print(name_list[0:2])

    # ___count___统计字符串(jack)在列表里出现几次....
    print(name_list.count('Tom'))

    # ___len___查看列表的长度
    print(len(name_list))

    # ___copy___拷贝列表
    paste = name_list.copy()

    # ___clear___清空列表
    name_list.clear()

    # ___extend___扩展....内部进行了for循环追加
    lists.extend(['and', 'sex', 'add', 32, 34, 544])

    # ___index___查找索引,,,可以指定索引范围
    lists.index('Tom', 1, 4)

    # ___insert___指定索引插入值,(0)为索引
    lists.insert(0, 'i')
    print(lists)

    # ___pop___依据索引来删除指定的值....并返回删除的值
    lists.pop(2)

    # ___remove___依据指定值来进行删除
    lists.remove("jack")

    # ___del___删除
    del lists[2]

    # ___reverse___将列表进行反转
    lists.reverse()

    # ___sort___将列表进行排序
    number = [1, 4, 5, 7, 12, 53, 32, 12, 67]
    number.sort(reverse=True)  # 从大到小
    # lists.sort(reverse=False)   #从小到大
    number.sort()
    # number.insert(0,2)
    print(number)

    # ____列表重复,,,,
    quest = ["hi"] * 5
    # print(quest)


"""进行倒序排列和冒泡排序"""
def sort():
    # 冒泡排序
    list = [5, 8, 6, 9, 3, 4, 8, 9, 5, 1, 4]
    list_len = len(list)
    for i in range(list_len - 1):
        for j in range(i, list_len):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(list)

    password_list = ['*#*#', '12345']
    print('===', password_list[-1])


# sort()

def testFunc():
    f = [1,4,5,7,]
    f.remove(4)
    print(f)
    print(f[1])
    for i in f:
        print(i, type(i))

    print(dir(list))

    list = [5, 8, 6, 9, 3, 4, 8, 9, 5, 1, 4]
    list.sort(reverse=False)
    print(list)

def sort_list(number):
    # 冒泡排序
    # 思路, 每相邻的两个数进行比较,如果前边的比后边的数大,则交换这两个数,重复操作,这样的话每一趟会确定一个最大值
    for j in range(len(number) - 1):
        for i in range(j, len(number)):
            if number[j] > number[i]:
                number[j], number[i] = number[i], number[j]
    return number


def select_sort(number):
    # 选择排序
    for j in range(len(number) - 1):
        min_loc = j
        for i in range(j + 1, len(number)):
            if number[i] > number[min_loc]:
                number[i], number[min_loc] = number[min_loc], number[i]
    return number

a = [10, 20, 30, 40]
print(id(a))
print(id(a[0]))
print(id(a[1]))

if __name__ == "__main__":
    sotr_number = sort_list([5, 8, 6, 9, 3, 4, 8, 9, 5, 1, 4])
    # print('==', sotr_number)

    select_number = select_sort([7, 5, 4, 6, 2, 8, 3, 1])
    # print(select_number)