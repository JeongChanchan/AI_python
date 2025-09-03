import requests
from bs4 import BeautifulSoup
import os

url = 'https://finance.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')



tbody = soup.find('tbody',attrs = {'id':'_topItems1'})
print(tbody)

trs = tbody.find_all('tr')
print('갯수',len(trs))

list1 =[]

for idx,tr in enumerate(trs):
    name = tr.a.get_text()
    price = tr.td.get_text()
    up_down = tr['class'][0]

    tds = tr.find_all('td')
    up_down_price = tds[1].get_text().replace('하락','').replace('상승','').strip()          
    list1.append(f'{idx+1},{name},{price},{up_down},{up_down_price}')
print(list1)
    
    
file_name = 'data/거래상위.txt'
with open(file_name, 'a', encoding='utf-8') as file:
    for line in list1:
        file.write(line + '\n')

    