#숫자입력
def inputNum(title):
    while 1:
        num = input(f'{title}')
        if num.isnumeric():
            return int(num)
        elif num == '':
            return num
        else:
            print('숫자를 입력하세요!')

num = inputNum('숫자입력> ')
print(num, type(num))