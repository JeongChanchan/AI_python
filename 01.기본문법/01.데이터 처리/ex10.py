#문자열 슬라이싱
jumin = '990120-2155011'

#남자?
gender = jumin[7]
result = (gender == '1') or (gender =='3')
print(f'{gender} : 결과는 {result}')

yy = jumin[:2]
mm = jumin[2:4]
dd =jumin[4:6]

print(f'{yy}년 {mm}월 {dd}일')

print(jumin[-7:])