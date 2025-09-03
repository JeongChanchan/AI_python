def newCode(list):
    if len(list) == 0:
        return 1
    
    codes = []
    for s in list:
        codes.append(s['code'])
    return max(codes)+1

def inputNum(title):
    while 1:
        num = input(f'{title}')
        if num.isnumeric():
            return int(num)
        elif num == '':
            return num
        else:
            print('숫자를 입력하세요!')


def search (list,code):
    for index, item in enumerate(list):
        if item['code'] == code:
            return index
        

def menuPrint(title,num):
    print('-'*43)
    print(f'{title:>{num}}')
    print('-'*43)
    print('|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|')
    print('-'*43)
