#!/usr/bin/python3

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

headers = {
    'Cookie': 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593050498; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=172e9358325c8-0f6d2fb401f1b7-31607402-7e9000-172e9358325c8; uuid_n_v=v1; iuuid=6C7D9B90B79611EA9A87292804CC68F3A2238CB82A244E6190B92062D7CF683E; webp=true; ci=93%2C%E6%A1%82%E6%9E%97; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172f0230ec9942-0efd2f57eeb4b9-63181e33-230400-172f0230eca538%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172f0230ec9942-0efd2f57eeb4b9-63181e33-230400-172f0230eca538%22%7D; _last_page=c_dmLad; __mta=174373405.1593050498009.1593167310363.1593167340883.10; _lxsdk=6C7D9B90B79611EA9A87292804CC68F3A2238CB82A244E6190B92062D7CF683E; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593167391; __mta=174373405.1593050498009.1593167340883.1593167392361.11; latlng=52.3666969%2C4.8945398%2C1593167392983; _lxsdk_s=172efd824a0-76f-9e5-82b%7C%7C40',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
}

myurl = 'https://m.maoyan.com/?showType=3#movie/classic'

response = requests.get(myurl, headers=headers)

# print(response.text)
# print(f'返回码是：{response.status_code}')

# 保存网页到本地
file_obj = open('maoyan.html', 'w')  # 以写模式打开名叫 maoyan.htm 的文件
file_obj.write(response.text)  # 把请求到的html内容写入
file_obj.close()  # 关闭文件

file_obj = open('maoyan.html', 'r')  # 以读方式打开文件
html = file_obj.read()  # 把文件内容读取出来并赋值给html变量
file_obj.close()  # 关闭文件

bs_info = bs(html, 'lxml')

all_movies = bs_info.find('div', attrs={'class': 'classic-movie-list'})

for tags in bs_info.find_all('div', attrs={'class': 'movie-info'}):
    for title in tags.find_all('div', attrs={'class': 'title'}):
        for actors in tags.find_all('div', attrs={'class': 'actors'}):
            for showtime in tags.find_all('div', attrs={'class': 'show-info'}):

                print('电影名称：{}｜电影类型：{}｜上映日期：{}'.format(
                    title.text, actors.text, showtime.text))

                mylist = [(title.text, actors.text, showtime.text)]
                movie1 = pd.DataFrame(data=mylist)
                movie1.to_csv('./movie1.csv', mode='a', encoding='utf8',
                              index=False, header=False)
