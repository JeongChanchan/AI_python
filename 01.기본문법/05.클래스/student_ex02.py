from student import Student


students = []
while 1:
    print('-' * 22)
    print('|1.등록|2.목록|0.종료|')
    print('-' * 22)
    menu = input('메뉴선택>')
    if menu == '0':
        break
    elif menu == '1':
        no = input('번호>')
        name = input('이름>')
        dept = input('학과>')
        birthday = input('생일>')
        students.append(Student(no,name,dept,birthday))

    elif menu == '2':
        for stu in students:
            stu.info_print()
            print('-' * 22)
