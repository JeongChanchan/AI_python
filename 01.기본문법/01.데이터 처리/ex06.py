age = 19
gender = '남'

result1 = (age >= 20)
print(1,result1)

result2 = (gender == '남')
print(2,result2)

result3 = (result1 and result2)
print("3(and)",result3)
result4 = (result1 or result2)
print("4(or)",result4)

result5 = not(result1 and result2)
print(5,result5)