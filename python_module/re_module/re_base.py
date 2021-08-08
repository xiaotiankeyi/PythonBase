"""
    概念：
        1、进行模糊匹配操作
        2、只对字符串进行处理
        3、元字符
        4、普通字符串是一对一的匹配
"""
import re

r"""元字符 . ^ $ * + ? {} [] | () \ 匹配出来的数据可通过for循环取值"""

h = re.findall(
    r'formhash=(.*)>',
    "[<a href='member.php?mod=logging&amp;action=logout&amp;formhash=dc66d9c9'>退出</a>]")
# print(h, type(h))

# for i in h:
#     print(str(i), type(i))


def letter():
    '''cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951'''

    w = re.findall(
        r'\W',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # \w数字字母下划线  \W非数字母下划线
    print(w)

    d = re.findall(
        r'\d+',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # \d匹配任意数字   \D匹配数字之外的值
    print(d)

    s = re.findall(
        r'\s',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # \s匹配任何空白字符    \S匹配任意非空白字符
    print(s)

    end = re.findall(
        '1$',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # 1$匹配字符串结尾
    print(end)

    start = re.findall(
        '^c',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # ^c匹配字符串开头
    print(start)

    all = re.findall(
        '.+',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # .通配符,匹配任意字符
    print(all)

    v = re.findall(
        '%*',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # * 匹配0个或无限个 %
    print(v)

    e = re.findall(
        'D2?',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    q = re.findall(
        r'\d+\.?\d*',
        'cnzz_eid%3D214.5852493-15651\n44951-https%2.53A%\t252F%25.2Fwww.baidu.com%252F%26ntime%3D1565144951')
    # D2? 匹配0个或1个D2。。。。。非贪婪模式   q = 为匹配所有包含小写在内的数字
    print('=========', q)

    k = re.findall(
        '14{2}',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # z{2}精确匹配两个合在一起的 z
    T = re.findall(
        '2{1,5}',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # {1, 5}匹配1次到5次之间。。。。。。贪婪模式
    print(T)

    w = re.findall(
        'ht|b2',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    q = re.findall(
        r'\n|\t',
        'cnzz_eid%3D2145852493-15651\n44951-https%253A%\t252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # | 匹配ht或b2，当两个都存在时都显示出来。。。。
    print(w)

    q = re.findall('www.(?:baidu|51zxw).com',  # 匹配为结果的全部内容
                   'cnzz_eid%3D2145852www.51zxw.com5144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    z = re.findall(
        '(.*)',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # print('z-------', z)
    x = re.findall(
        '(52)+F',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%262ntime%3D1565144951')
    # ()分组，(.*)为贪婪匹配
    print('---------', x)

    p = re.findall(
        '25[0-5]',
        'cnzz_eid%3D214582552493-15651\n44951-https%253A%\t250F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # [ - ]表示之间，如上面匹配25，就是把25后面[0至5之间也匹配出来]、如250,251,252,253,254,255
    print(p)

    x = re.findall(
        '2[^5,1]',
        'cnzz_eid%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%252F%262ntime%3D1565144951')
    x = re.findall(
        r'\([^()]+\)',
        'cnzz_eid%3D2145852493-15(651)44951-https%253A%252F%252Fwww.baidu.com%252F%262ntime%3D1565144951')
    # [^]表示非，上面的表达就是匹配非25,21
    g = re.findall(
        '51[\\n]',
        'cnzz_eid%3D2145852493-15651\n44951-https%253A%\t252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # [ \ ]转义
    q = re.findall(
        '5[2|1]]',
        'cnzz_eid%3D2145852493-15651\n44951-https%253A%\t252F%252Fwww.baidu.com%252F%26ntime%3D1565144951')
    # [ | ]表示或， 上面的表达式就是匹配52或51
    print(x)

    return None


# letter()

def method():
    re.findall('', '')
    # 有名函数
    c = re.search(
        r'(?P<name>[A-Z]+)(?P<age>\d+)',
        'id%23TOM21&45852493-1565144951-https%253A%252F%252Fwww.baidu.com%')
    print(c.group('name'), c.group('age'))  # 只匹配第一个。。成功就返回，没找到就返回None

    v = re.finditer(
        '[A-Z]',
        'id%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%')  # 定义迭代器
    print(next(v).group(), next(v).group(), next(v).group())

    # ['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割
    b = re.split('[ab]', 'abcdafbe')
    print(b)

    f = re.sub(
        'baidu',
        '51zxw',
        'id%3D2145852493-1565144951-https%253A%252F%252Fwww.baidu.com%')  # 替换
    print(f)
# method()
