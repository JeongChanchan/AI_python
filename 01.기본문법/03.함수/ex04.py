from function import *

while 1:
   kor = input('국어> ')
   if isNumber(kor):
        break

while 1:
    eng = input('영어> ')
    if isNumber(eng):
        break

while 1:
    math = input('수학> ')
    if isNumber(math):
        break

avg= (int(kor) + int(eng)+ int(math))/3
level = grade(avg)
print(f'평균: {avg:.2f} 평점:{level}')