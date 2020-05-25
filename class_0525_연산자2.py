#논리 연산자 and or not
#and는 앞이 거짓이면 무조건 거짓 뒤는 무시, or은 앞이 참이면 무조건 참 뒤는 무시

# print(0 or 0, ":", False or False)
# print(1 or 0, ":", True or False)
# print(0 or 1, ":", False or True)
# print(1 or 1, ":", True or True)
# print("not:", not(0 or 0), ":", not(False or False))
# print("not:", not(1 or 1), ":", not(True or True))

# #논리 연산자 보다 산술 연산자 우선순위가 높음
# a = 20
# b = 10
# print(0 or 0, ":", False or (a+b)) #앞이 거짓, 뒤에 봐야됨, 산술연산식 우선
# print(1 or 1, ":", True or (a+b)) #앞이 참, 뒤에 무시, 논리연산식 우선
# print(0 and 0, ":", False and (a+b)) #앞이 거짓, 뒤에 무시, 논리연산식 우선
# print(1 and 0, ":", True and (a+b)) #앞이 참, 뒤에 봐야됨, 산술연산식 우선


# #비트 연산자
#     101(5)
# |   011(3)
#     111(7)

#     101(5)
# &   011(3)
#     001(1)

#     101(5)
# ^   011(3)
#     110(6)

# ~: 양 → 음: +1 (10 → (-11))
#    음 → 양: -1 ((-10) → 9)

# a << b : 2진수로 바꾼다음 b만큼 0을 붙임
# a >> b : 2진수로 바꾼다음 b만큼 0,1을 뺌(만약 다 지워지면 0이 됨)

# num1 = 3
# num2 = 5
# or_bit = num1 | num2
# and_bit = num1 & num2
# xor_bit = num1 ^ num2
# a = ~num1
# b = ~-12
# result = 5 << 2
# result1 = 20 >> 2
# result2 = 20 >> 3

# print(or_bit)
# print(and_bit)
# print(xor_bit)
# print(a)
# print(b)
# print(result)
# print(result1)
# print(result2)


##연산자 우선순위
# 남의 코드:가장 순위가 낮은것부터 거꾸로 좌우로 쪼갬/ 내 코드:연산해야되는거 괄호로 묶기