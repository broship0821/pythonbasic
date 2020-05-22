##산술 연산자
# num1 = 9
# num2 = 2
# print(num1, "+", num2, "=", num1 + num2)
# print(num1, "-", num2, "=", num1 - num2)
# print(num1, "*", num2, "=", num1 * num2)
# print(num1, "/", num2, "=", num1 / num2)
# print(num1, "//", num2, "=", num1 // num2)
# print(num1, "%", num2, "=", num1 % num2)
# print(num1, "**", num2, "=", num1 ** num2)

#관계 연산자 0은 거짓
# su1 = 3.1
# su2 = 3
# print("su1 >= su2: %d" % (su1 >= su2))
# print("su1 <= su2: %s" % (su1 <= su2))
# print("su1 == su2: %d" % (su1 == su2))
# print("su1 != su2: %s" % (su1 != su2))

# #복합 대입 연산자 좌측에는 변수만 올수있음
# su1 = su2 = 5
# su1 += 1
# print("su1 + 1 =", su1) #6
# su1 -= 1
# print("su1 - 1 =", su1) #5 똑같은 변수기 때문에 su1은 6이었음
# su1 *= su2
# print("su1 * su2 =", su1) #25
# su1 //= su2
# print("su1 // su2 =", su1) # 5
# su1 %= su2
# print("su1 % su2 =", su1) # 0

su1 = 5
su2 = 3
su1 **= su2 #125
su1-=2 # 123
print("su1 / 4:", su1/4)
print("su1 // 4:", su1//4)
print("su1 % 4:", su1%4)