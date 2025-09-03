#샘플데이터
info = [{'no':1, 'name':'홍길동', 'addre':'인천 서구 경서동'},
        {'no':2, 'name':'심청이', 'addre':'경기도 광명시 철산동'}]
while 1:
    print('-' * 43)
    print('\t     주소관리 프로그램')
    print('-' * 43)

    print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-' * 43)

    menu = input('메뉴선택> ')
    print()
    if menu == '0':     #종료
        print('프로그램을 종료합니다.')
        break
    
    elif menu == '1':   #입력
        no = []
        for a in info:
            no.append(a['no'])
        new_no = max(no)+1
        print(f'번호> {new_no}')
        name = input('이름>')
        addre =input('주소> ')
        info.append({'no': new_no, 'name': name, 'addre': addre})
        ['새로운 주소가 등록되었습니다. ']

    elif menu == '2':   #목록
        for i in info:
                print(i['no'], i['name'], i['addre'])
        continue
    
    elif menu == '3':   #검색
        name = input('검색이름> ')
        for a in info:
             if   a['name'].find(name) != -1:
                  print(a['no'], a['name'], a['addre'])
    
    elif menu == '4':   #삭제
        no = input('삭제번호> ')
        if no == '':
            continue
        for index, a in enumerate(info):
            if int(no) == a['no']:
                info.pop(index)
                print(no,'번 삭제되었습니다.')
        
    elif menu == '5':   #수정
        no = input('수정번호> ')
        for a in info:
            
            if no == '': 
                  continue
        
            elif int(no) == a['no']:
                name = input(f'{a['name']}> ')
                if name !='':
                    a['name'] = name
                
                addre = input(f'{a['addre']}> ')
                if addre != '':
                    a['addre'] = addre   
            
            else:
                print('올바른 값이 아닙니다.')
                break

    else:
        print('0 ~ 5번을 다시 선택하세요!')