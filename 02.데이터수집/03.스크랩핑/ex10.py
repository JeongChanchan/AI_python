import requests
from bs4 import BeautifulSoup

city = '서울날씨'
url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={city}&oquery=%EB%82%A0%EC%94%A8&tqi=j7PMLsqVOsossLdzQ4Kssssssr4-086177&ackey=pqz0s57z'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')

summary = soup.find('p', attrs={'class':'summary'}).get_text()
print(summary)

temp = soup.find('div',attrs={'class':'temperature_text'}).strong.contents[1]
print(temp)


temperature = soup.find('span', attrs={'class':'temperature_inner'}).span.contents[1]
print(temperature)
