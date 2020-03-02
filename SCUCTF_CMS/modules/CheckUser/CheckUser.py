import requests
from bs4 import BeautifulSoup
import re
'''
    注释：
        1.输入用户名和密码并传入Login
        2.参数condition中的handleLoginSuccessed是登陆成功的响应头，如果用户账户密码错误则响应头中出现handleLoginFailure
        3.由于学校网站有点神奇，本来输入错误就需要输入验证码的，但是如果刷新下网页验证码就消失了，所以就不用那么麻烦将验证码返
        回前端了
        4.成功验证以后返回用户名字
        5.学校网站太水了就不增加try容错了
'''


class Login:
    def __init__(self, username, passpord):
        self.u_name = username
        self.u_pass = passpord
        self.session = requests.session()

    def operate(self):
        postdata = {'Login.Token1': self.u_name, 'Login.Token2': self.u_pass,
                    'goto': 'http://my.scu.edu.cn/loginSuccess.portal',
                    'gotoOnFail': 'http://my.scu.edu.cn/loginFailure.portal'}
        headers = {
            'Referer': 'http://my.scu.edu.cn/',  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
            # 伪装成浏览器
            'Connection': 'keep-alive',
            'Accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Host': 'my.scu.edu.cn'
        }
        response = self.session.post('http://my.scu.edu.cn/userPasswordValidate.portal', data=postdata, headers=headers,
                                     timeout=3)
        text1 = response.text
        condition = 'handleLoginSuccessed'
        if condition in text1:
            return True
        else:
            return False

    def get_name(self):
        url = 'http://my.scu.edu.cn/'
        headers = {
            'Referer': 'http://my.scu.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
            'Connection': 'keep-alive',
            'Accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Host': 'my.scu.edu.cn'
        }
        response = self.session.get(url, headers=headers, timeout=3)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        get_name = re.split(r'：', soup.li.text)
        result = get_name[1]
        return result
        # if response3.status_code == 200:
        #     with open('douban3.html', 'w') as file:
        #         file.write(response3.text)


if __name__ == '__main__':
    username = input('username:')
    password = input('password:')
    while True:
        generator = Login(username, password)
        status = generator.operate()
        if status:
            print(generator.get_name())
            print('登录验证成功')
            break
        else:
            print('用户不存在或密码错误,请重新输入')
            username = input('username:')
            password = input('password:')
