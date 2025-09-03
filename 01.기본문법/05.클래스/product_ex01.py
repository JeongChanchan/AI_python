from function import *
from product import Product

products = [{'code': '001', 'name': 'LG 냉장고' , 'price' : 250},
            {'code': '002', 'name': 'LG 세탁기' , 'price' : 300}
 ]

def search(code):
    for idx, p in enumerate(products):
        if code == p['code']:
            return idx

while 1:
    menuPrint('상품관리', 22)
    menu = input('메뉴> ')
    if menu == '0':
        break
    elif menu == '1':
        code = len(products) +1
        code = f'{code:03d}'
        
        print(f'상품코드> {code}')
        name = input('상품이름> ')
        if name == '':continue
        
        price = inputNum('상품가격> ')
        if price == '': price = 0

        p = Product(code,name,price)
        products.append(p.dict())
        print('상품등록 완료!')

    elif menu == '2':
        name = input('검색이름> ')
        for p in products:        
            if p['name'].upper().find(name.upper()) != -1:
                print(p['code'],p['name'],p['price'])

    elif menu == '3':
        for p in products:
            print(p['code'], p['name'], p['price'])
        print(f'{len(products)}개 상품이 존재합니다.')

    elif menu == '4':
        code = input('삭제코드> ')
        if code == '':continue
        idx = search(code)
        if idx == None:
            print(f'{code}번 상품이 없습니다.')
        else: 
            products.pop(idx)
            print('상품삭제 완료!')

    elif menu == '5':
        code = input('수정코드> ')
        if code == '': continue
        idx = search(code)
        if idx == None:
            print(f'{code}번 상품이 없습니다.')
            continue

        p = products[idx]
        name = input(f'상품이름: {p['name']}> ')
        if name != '': p['name'] = name
        price = inputNum(f'상품가격: {p['price']}> ')
        if price != '': p['price'] = price
        print('상품수정 완료!')
            