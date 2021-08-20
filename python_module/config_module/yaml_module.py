import yaml

with open('config.yml', 'r') as f:
    data = yaml.load(f)
    print(data)
    f.close()

with open('config.yml', 'a+') as d:
    token = {'token': 21793621974712832831231,
             'status_code': 'ok'}
    yaml.dump(token, d)

with open('config.yml', 'r') as a:
    data2 = yaml.load(a)
    print(data2)
    print(data2['token'])
