"""
概念：文件的数据是存放于硬盘上的，因而只存在覆盖、不存在修改这么一说，我们平时看到的修改文件，都是模拟出来的效果，
实现：将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）
"""
import os
import time


def handle():
    """将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘"""
    with open('n.txt') as read_f, open('test.txt', 'w') as write_f:
        data = read_f.read()  # 全部读入内存,如果文件很大,会很卡
        data = data.replace('apple', 'SB')  # 在内存中完成修改

        write_f.write(data)  # 一次性写入新文件

    """将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件"""
    with open('g.txt') as read_f, open('test.txt', 'w') as write_f:
        for line in read_f:
            line = line.replace('SB', 'android')
            write_f.write(line)

    os.remove('g.txt')  # 删除a.txt
    time.sleep(4)
    os.rename('test.txt', 'shopping.txt')  # 重命名


# handle()

"""求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数"""


def handle_1(txt):
    with open(txt, 'r', encoding='utf8') as f:
        """表达式书写方式为"""
        # ret = max(len(e) for e in f)
        # ter = sum(len(o) for o in f)
        v = []
        for i in f:
            v.append(i)
        g = []
        for h in v:
            g.append(len(h))
        print("四行字符的长度分别为{}".format(g))

    # return ter
    return "最长的一行长度为{}".format(max(g))

# t = handle_1("b.txt")
# print(t)
