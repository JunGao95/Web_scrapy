import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

homepage = 'https://task.zbj.com/t-cpwgsj/page{}.html?so=2&ss=0'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}
PAGE_NUM = 10
SLEEP_TIME = 5
info = {}
df_columns = ['Title', 'Money', 'Requirement', 'Link']
for _ in df_columns:
    info[_] = []


def get_subpages(homepage_url):
    r = requests.get(homepage_url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    subpages = re.findall('href="(//task.zbj.com/[0-9]*?/)"', soup.prettify())
    time.sleep(SLEEP_TIME)

    return subpages


def get_content(subpage_url):
    r = requests.get(subpage_url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find(name='h1', attrs={'class': "title"}).string.strip()
    money = soup.find(name='p', attrs={'class': 'money'}).get_text().strip()[:-10]
    requirement = soup.find(name='div', attrs={'class': 'content-item'}).contents
    requirement_text = ''
    for _ in requirement:
        requirement_text = requirement_text + str(_)
    requirement_text = re.sub('<[\s\S]*?>', ' ', requirement_text)
    requirement_text = requirement_text.replace('\n', '')
    time.sleep(SLEEP_TIME)

    return title, money, requirement_text


for homepage_num in range(201, 203):
    subpages = get_subpages(homepage.format(homepage_num))
    print('No.{} homepage scrapied.'.format(homepage_num))
    for subpage in subpages:
        subpage_url = 'http:' + subpage
        try:
            title, money, requirement = get_content(subpage_url)
            info['Title'].append(title)
            info['Money'].append(money)
            info['Requirement'].append(requirement)
            info['Link'].append(subpage_url)
            print('Page:{} scrapied'.format(subpage_url))
        except:
            print('Page:{} error!'.format(subpage_url))
            continue



    df = pd.DataFrame(info)
    df = df[df_columns]
    curr_time = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    df.to_excel('collected_data\\'+curr_time+'.xls')
