# for은 반복 횟수가 정해져 있고 while은 반복 정지 타이밍을 내가 정할 수 있음

# i = 0
# while i < 5:
#     print(i, "종속문장")
#     i += 1
# print("다음 문장")

# for i in range(5):
#     print(i, "종속문장")
# print("다음 문장")

# i = 1
# odd, even = 0, 0
# while i<=10:
#     if i%2 == 0:
#         even += i
#     else:
#         odd += i
#     i += 1
# print("1~10 짝수의 합:", even)
# print("1~10 홀수의 합:", odd)

# odd, even = 0, 0
# for i in range(1,11,1):
#     if i%2 == 0:
#         even += i
#     else:
#         odd += i
# print("1~10 짝수의 합:", even)
# print("1~10 홀수의 합:", odd)

# i=0
# while i < 5:
#     print(i, "종속문장")
#     i += 1
# else:
#     print("조건식이 거짓일 경우:", i)
# print("다음 문장")

# ##무한반복
# i = 0
# while True:
#     print(i, "종속문장", end=" ")
#     i += 1