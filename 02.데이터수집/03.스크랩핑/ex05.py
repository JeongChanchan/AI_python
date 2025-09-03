import requests
from bs4 import BeautifulSoup
import csv

with open('data/hollys_seoul.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['No', 'City', 'Name', 'Address', 'Phone'])

    store_no = 1  # Start numbering from 1
    for page in range(1, 11):
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=서울&gugun=&store='
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        table = soup.find('table', attrs={'class': 'tb_store'})
        rows = table.find_all('tr')
        for idx, row in enumerate(rows):
            if idx == 0:
                continue 
            cols = row.find_all('td')
            city = cols[0].getText().strip()
            name = cols[1].getText().strip()
            address = cols[3].getText().replace(',', ' ').replace('.', '').strip()
            phone = cols[5].getText().strip().replace('.', '')
            data = [store_no, city, name, address, phone]
            writer.writerow(data)
            store_no += 1 