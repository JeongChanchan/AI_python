address = [
    {'no': 1, 'name': '홍길동', 'addre' : '서울 강서구'},
    {'no': 2, 'name': '강감찬', 'addre' : '인천 서구'},
]
while 1:
    print('-'*36)
    print('\t 주소관리 프로그램')
    print('-'*36)
    print('|1.입력|2.검색|3.수정|4.삭제|0.종료|')
    print('-'*36)

    menu = input('번호입력> ')
    
    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':
        no = input('번호> ')
        name = input('이름> ')
        addre = input('주소> ')
        address.append({'no': no, 'name': name, 'addre': addre})        
    elif menu == '2':
        for addre in address:
            print(f'{addre['no']}, {addre['name']}, {addre['addre']}')
        print()
        print(len(address),'명이 존재 합니다.')
    elif menu == '3':
        print('프로그램을 종료합니다.')
    elif menu == '4':
        print('프로그램을 종료합니다.')

    else: print('올바른 번호를 입력하세요.(0 ~ 4)')
