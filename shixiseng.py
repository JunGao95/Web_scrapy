import requests
from bs4 import BeautifulSoup

f = open('test.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

soup = BeautifulSoup(text, 'html.parser')
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.a
len(soup.find_all('a'))
count = 0
for link in soup.find_all('a'):
    print(link.get('href'))
    count += 1
soup_list = soup.find_all('div')
type(soup_list)
soup.find_all(class="position-name fl")