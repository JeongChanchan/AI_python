#list 타입
names = ['홍길동', '심청이', '강감찬',True]
print(names, type(names))

names.append('박명수')
print(names)

names.pop(3)
print(names)

names.insert(1,'유재석')
names.append('유재석')
print(names)

print(names.count('유재석'))
print(names[0],names[-1],names[-2:])
