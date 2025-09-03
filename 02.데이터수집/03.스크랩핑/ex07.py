import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.hanbit.co.kr/store/store_submain.html'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')

path = os.getcwd() + '/data/books'
if not os.path.exists(path):
    os.mkdir(path)

ul = soup.find('ul', attrs={'id': 'new_books_slider'})
best_div= soup.find('div', attrs={'div': 'best-books-container'})

imgs = ul.find_all('img')

for idx,img in enumerate(imgs):
    print(f'book{idx+1:02d}.jpg',img['src'])
    url = img['src']
    res_img = requests.get(url)
    file_name = path + f'/book{idx+1:02d}.jpg'
    with open(file_name,'wb') as file:
        file.write(res_img.content)