import requests
from bs4 import BeautifulSoup
import lxml
import re
from .model import GameInformation


def get_inf():
    url = "https://www.xctf.org.cn/ctfs/recently/"
    param = {"page": 1}
    try:
        res = requests.get(url=url, params=param, timeout=3)
    except:
        return False  # 请求失败返回False
    soup = BeautifulSoup(res.text, "lxml")
    game_list = soup.find(class_="nearest pad10T").find_all("li")
    for i in game_list:
        date = i.find(class_="x2_timeInterval").string
        if ("2020" not in date):  # 只爬取2020年之后的数据
            break
        pattern = re.compile(r'[(](.*?)[)]', re.S)
        jpg_addr = i.find("a")["style"]
        jpg_addr = "https://www.xctf.org.cn" + re.findall(pattern, jpg_addr)[0]
        apply_addr = "https://www.xctf.org.cn" + \
                     i.find(class_="x2_hotTitle")["href"]
        game_name = i.find(class_="x2_hotTitle").find("span").string
        game_type = i.find(class_="x2_nearType").string
        addr = i.find(class_="x2_nearplace mrg5T").string

        try:
            # 判断是否存在记录
            GameInformation.objects.get(name=game_name)
        except:
            # 不存在就添加
            new_game_record = GameInformation(name=game_name, type=game_type, hyperlink=apply_addr, date=date,
                                              pic_addr=jpg_addr, location=addr)
            new_game_record.save()
        #
        # print("jpg addr is :" + jpg_addr)
        # print("apply addr is: " + apply_addr)
        # print("game name is: " + game_name)
        # print("game type is: " + game_type)
        # print("addr is: " + addr)
        # print("date is: " + date)
