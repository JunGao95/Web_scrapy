import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

search_word = '数据'
page_num = 5
root_path = 'https://www.shixiseng.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8"}

for homepage_num in range(1, page_num+1):
    print('Homepage No.{} scraping started.'.format(homepage_num))
    info = {}
    for _ in ['Title', 'Address', 'Description']:
        info[_] = []
    homepage_path = 'https://www.shixiseng.com/interns/c-110100_?k={}&p={}'.format(search_word, homepage_num)
    r = requests.get(homepage_path, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    subpage_paths = []
    for _ in soup.find_all(name='a', attrs={'class': 'position-name fl'}):
        subpage_paths.append(_.get('href'))
    print('Subpage paths collected')
    time.sleep(5)
    for subpage_path in subpage_paths:
        r = requests.get(root_path+subpage_path, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        info['Title'].append(soup.find(name='div', attrs={'class': 'new_job_name'}).string.strip())
        info['Address'].append(soup.find(name='span', attrs={'class':'com_position'}).string.strip())
        job_des = str(soup.find(name='div', attrs={'class':'job_detail'}))
        job_des = re.sub('<[\s\S]*?>', '', job_des)
        job_des = job_des.replace('\n', '')
        info['Description'].append(job_des)
        print('Page No.{} Path {} Scraping finished'.format(homepage_num, subpage_path))
        time.sleep(5)
    print('Homepage No.{} scraping finished.'.format(homepage_num))

output_df = pd.DataFrame(info)
column_order = ['Title', 'Description', 'Address']
output_df = output_df[column_order]
date_str = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
output_df.to_excel('collected_data\\'+date_str+'.xls')