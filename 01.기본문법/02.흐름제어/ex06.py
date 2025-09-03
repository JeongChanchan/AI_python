names = []
num = int(input('학생수>\n'))
for i in range(num):
    name = input('이름>')
    names.append(name)

for index in range(len(names)):
    print(f'{index+1}: {names[index]}')
print()
for name in names:
    print(name,end= ',')
print()
for i, name in enumerate(names):
    print(i,name,end= ',')