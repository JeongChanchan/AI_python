def search (list,code):
    for index, item in enumerate(list):
        if item['code'] == code:
            return index


sale =[
    {'code': 1, 'name': '냉장고', 'price' : 250, 'qnt': 5},
    {'code': 2, 'name': '세탁기', 'price' : 150, 'qnt': 3}
]

code = int(input('코드> '))
index = search(sale,code)
if index == None:
    ('해당 데이터가 없습니다.')
print(sale[index])