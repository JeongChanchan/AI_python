from score import Score
from function import *

def insert(list):
    score = Score()
    score.no = input('학번>')
    score.name = input('이름>')
    

    score.kor = int(input('국어>'))
    score.eng = int(input('영어>'))
    score.mat = int(input('수학>'))

    print(score.info())
    list.append(score)

scores = []
while True:
    menuPrint('성적관리',20)
    menu = input('메뉴선택> ')
    if menu == '0':
        break
    if menu == '1':
        insert(scores)
    elif menu == '3': 
        for s in scores:
            print(s.info())