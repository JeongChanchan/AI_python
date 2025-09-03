while 1:
    try:
        num =input('숫자> ')
        if num =='': break
        num = int(num)
    except Exception as err:
        print(err)