import os

file_name = 'C:/python/01.기본문법/data/juso.txt'

with open(file_name,'a',encoding='utf-8') as file:
    name = '홍길동'
    phone = '010-1111-1111'
    address = '서울 강서구 화곡동'
    file.write(f'{name},{phone},{address}\n')


