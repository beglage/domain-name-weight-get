import requests
from bs4 import BeautifulSoup
import time
import random

# 读取文件内容
with open('domain.txt', 'r') as f:
  content = f.read()

# 提取域名列表
domains = content.split('\n')

# 常用浏览器的请求头
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}

# 遍历域名列表
for domain in domains:
  # 发送请求
    url = f'https://www.aizhan.com/cha/{domain}/'
    res = requests.get(url, headers=headers)

  # 解析响应
    soup = BeautifulSoup(res.text, 'html.parser')

    baidu_rank_img = soup.find(id='baidurank_br').find('img')
    baidu_rank = baidu_rank_img['alt']
    if   baidu_rank != "n":
        baidu_rank = int(baidu_rank)
    else:
        baidu_rank = int("0")

# 找到移动权重信息
    mobile_rank_img = soup.find(id='baidurank_mbr').find('img')
    mobile_rank = mobile_rank_img['alt']
    if mobile_rank != "n":
        mobile_rank = int(mobile_rank)
    else:
        mobile_rank = int("0")

# 找到谷歌权重信息
    google_rank_img = soup.find(id='google_pr').find('img')
    if google_rank_img:
        google_rank = int(google_rank_img['alt'])
    
    if baidu_rank >= 1 or mobile_rank >= 1 or google_rank >= 3:
        print(f"{domain}")

  # 暂停 1 到 2 秒之间的随机时间
    time.sleep(random.randint(1, 2))
