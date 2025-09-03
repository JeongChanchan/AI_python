from function import *

kor = inputNum('국어')
eng = inputNum('영어')
math = inputNum('수학')
avg = (kor + eng + math)/3

print(f'평균:{avg:.2f} 평점{grade(avg)}')