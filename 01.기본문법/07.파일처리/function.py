def isNumber(str):
    if str.isnumeric():
        return 1
    else:
        print('숫자로 입력하세요')
        return 0
    
def grade(score):
    grade=''
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def inputNum(title):
    while True:
        str = input(f'{title}')
        if str.isnumeric():
            return int(str)
        elif str == '':
            return str
        else:
            print('숫자로 입력하세요.')

def menuPrint(title,num):
    print('-'*43)
    print(f'{title:>{num}}')
    print('-'*43)
    print('|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|')
    print('-'*43)
