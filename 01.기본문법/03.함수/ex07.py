from function import *
sale =[
    {'code': 1, 'name': '냉장고', 'price' : 250, 'qnt': 5},
    {'code': 2, 'name': '세탁기', 'price' : 150, 'qnt': 3}
]
#검색
def search(code):
    isFind = False
    for index, s in enumerate(sale):
        if s['code'] == code or (code == 0):
            isFind = True
            sum = s['price'] * s['qnt']
            print(index, s['code'], s['name'], s['price'], s['qnt'], sum)
            if code != 0: return index
    if isFind == False:
        print('상품이 존재하지 않습니다.')
    

#삭제
def delete(code):
    isFind = True
    print('삭제된 상품')
    index = search(code)
    if isFind == True:
        sale.pop(index-1)
    else: print('삭제할 수 없습니다.')
    

while 1:
    menuPrint('매출 관리', 21)
    menu = input('메뉴 선택> ')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1':
        pass
    elif menu == '2':
        code = inputNum('검색코드')
        search(code)
    elif menu == '3':
        if len(sale) == 0: 
            print('상품이 존재하지 않습니다')
            continue
        search(0)
    elif menu == '4':
        print('삭제할 상품')
        search(0)
        code = inputNum('삭제코드')
        delete(code)
    elif menu == '5':
        pass
