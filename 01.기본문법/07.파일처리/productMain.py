from function import *
from productFile import *

def newCode():
    list = fileRead()
    result = sorted(list,key = lambda p:p.code, reverse=True)
    if len(list) == 0:
        return 1
    else:
        p = result[0]
        return p.code +1
    
while True:
    menuPrint('상품관리',22)
    menu = input('메뉴선택> ')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1': #입력
        p = Product()
        p.code = newCode()
        p.name = input('상품이름> ')
        p.price = input('상품가격> ')
        fileAppend(p)
        print('등록성공!')
       
    elif menu == '2': #검색
         while True:
            value = input('검색어>')
            if value=='': break
            list = fileRead()
            result=[p for p in list if p.name.find(value)!=-1]
            if len(result)==0:
                print('검색내용이 없습니다.')
                continue
            for p in result:
                p.print()

    elif menu == '3': #목록
         while True:
            sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
            if sort == '':break
            list = fileRead()
            result = []
            if sort==1:result = sorted(list, key=lambda p:p.code)
            if sort==2:result = sorted(list, key=lambda p:p.name)
            if sort==3:result = sorted(list, key=lambda p:p.price)
            if sort==4:result = sorted(list, key=lambda p:p.price, reverse=True)
            print()
            for p in result:
                p.print()

    elif menu == '4': #삭제
        plist = fileRead()
        code = input('상품코드> ')
        result = [p for p in list if p.code!=code]
        fileWrite(result)

    elif menu == '5': #수정
        code= input('상품코드> ')
        list = fileRead()
        result = [p for p in list if p.code==code]
        p = result[0]
        p.name= input(f'{p.name}>  ')
        p.price= input(f'{p.price}> ')
        fileWrite(list)
        
    
    else:
        print('0~5 숫자를 입력하세요')