#숫자함수
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

while 1:
    score = input('점수> ')
    if score == '':
        break
    elif isNumber(score):
        level = grade(int(score))
        print(f'평점:{level}')

    