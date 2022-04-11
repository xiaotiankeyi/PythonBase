from bs4 import BeautifulSoup
import requests


def test_login():
    url = "http://192.168.117.9:8080/jforum/jforum.page"
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    data = {
        'module': 'user',
        'action': 'validateLogin',
        'username': 'admin',
        'password': 'admin',
        'login': '登入'
    }

    response = requests.request('post', url, params=data, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    print(soup)
    print('获取文本值:', soup.find('a', id='logout').get_text())
    print('通过ID属性搜索a标签:', soup.find_all('a', id='logout'))
    print('通过class属性来搜索span标签:', soup.find_all(
        'span', class_='gensmall')[0].string)

    # for item in soup.find_all('a'):
    #     print(item.get_text())


test_login()
