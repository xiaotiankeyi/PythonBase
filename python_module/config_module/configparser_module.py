import configparser


def handle():
    """创建配置文件"""
    config = configparser.ConfigParser()  # 实例化一个对象config
    """["DEFAULT"]特殊配置信息公用的"""
    config["DEFAULT"] = {'ServerAliveInterval': '45',
                         'Compression': 'yes',
                         'CompressionLevel': '9'}

    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'

    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Host Port'] = '50022'  # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here

    config['DEFAULT']['ForwardX11'] = 'yes'

    """写入文件操作不同"""
    with open('example.ini', 'w') as configfile:
        config.write(configfile)


def show_ini():
    """查看配置数据"""
    config = configparser.ConfigParser()  # 获取对象实例化对象
    config.read('example.ini')  # 通过对象读取example.ini

    """查看标题"""
    res = config.sections()  # 不显示默认的块
    print(res)

    """查看bitbucket.org所有键值对的key(默认信息也被显示出来了)"""
    res_1 = config.options('bitbucket.org')
    res_2 = config['bitbucket.org']['user']  # 取bitbucket.org块下user的值
    res_3 = config['DEFAULT']['serveraliveinterval']  # 取默认块[DEFAULT]下的serveraliveinterval的值
    # for i in config["DEFAULT"]:
    #     print(i)
    print(res_1, '\t', res_2, '\t', res_3)

    """查看['DEFAULT']所有键值对的格式"""
    res_4 = config.items('DEFAULT')
    res_5 = config.get("DEFAULT", 'compressionlevel')
    print(res_4, '\t', res_5)



def alter():
    config = configparser.ConfigParser()
    config.read('example.ini')

    """增加key及values"""
    # config['bitbucket.org']['password'] = '123456'
    config['bitbucket.org']['path'] = 'C:/Users/admin/PycharmProjects/python/python_module/config_module'
    config['bitbucket.org']['ip'] = '127.0.0.1'
    config.add_section('response')

    """删除操作"""
    # config.remove_section()     #删除标题
    config.remove_option('bitbucket.org', 'password')  # 删除一个键值对

    """修改好后重新写进一个文件,可重名覆盖"""
    config.write(open('config_test.ini', 'w'))

# alter()
