# 동일한 반복/ 단계적인 방법/ 규칙 없는 반복
# for 변수 in range(초기값, 끝값, 증감값):
#     print("종속문장")
# 초기값: 시작점, 끝값: 반복 끝나는 조건, 증감값:반복 간격
# 무엇을 반복실킬 것인가, 규칙을 찾는것

# for i in range(0, 10, 1):
#     print(i+1)
# print("다음 문장")
# #i를 꼭 사용해야하는건 아님
# for i in range(0, 10, 1):
#     print("ㅍㅍㅍ")
# print("다음 문장")

# for i in range(0, 3, 1):
#     print("i:", i, "for문 이해하기")
# print("다음 문장 실행")

# #반복 10회 진행
# for i in range(1, 11, 1):
#     if i % 2 == 0:
#         print("i:", i, ": 값 확인")
# print("다음 문장 실행")
# #반복 6회 진행
# for i in range(0, 11, 2):
#     print("i:", i, ": 값 확인")

# for i in range(10, -1, -1):
#     print(i, ": 10 ~ 0 까지 출력")

# num = 0
# for i in range(1, 11, 1):
#     num = num + i
# print(num)

# num = 0
# for i in range(0, 10, 1):
#     num = num + (i+1)
# print(num)

# num = 0
# for i in range(10, 0, -1):
#     num = num + i
# print(num)

# num = 0
# for i in range(1, 11, 1):
#     num += i
#     print(num, i) #검산 가능

# #end는 공백 or 문자열 or 이스케이프 문자 or 서식제어문 가능 / 숫자 불가능
# for i in range(1, 11, 1):
#     print(i, end=" ")
# for i in range(1, 11, 1):
#     print(i, end="\t")
# for i in range(1, 11, 1):
#     print(i, end="%d" % 1)

# for i in range(1, 31, 1):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i, end="\t")
# #다른 방법
# for i in range(1, 31, 1):
#     print(i, end="\t")
#     if i % 5 == 0:
#         print()

# i, sum_ = 0, 0
# num = 0

# num = int(input("값 입력: "))

# for i in range(1, num+1, 1):
#     sum_ = sum_ + i
# print("1에서 %d까지 합: %d" % (num, sum_))

# i, Sum = 0, 0
# start, end, grow = 0, 0, 0

# start = int(input("시작값 입력: "))
# end = int(input("끝값 입력: "))
# grow = int(input("증가값 입력: "))

# for i in range(start, end+1, grow):
#     Sum += i
# print("%d에서 %d까지 %d씩 증가한 값의 합: %d" % (start, end, grow, Sum))

# for i in range(0,10): #증감값 기본값인 1인 생략 가능
#     print(i)
# for i in range(10): #시작값도 기본값 0, 생략가능
#     print(i)
# for i in range(10,2): #매게변수가 2개 있으면 생략되는건 무조건 증감값
#     print(i)
# for i in range(0,10,2): #기본
#     print(i)
# #파이썬에서 무조건 끝값은 남아 있어야됨, C는 무한 반복
# for i in range():
#     print(i)



# start = int(input("시작값 입력: "))
# end = int(input("끝값 입력: "))
# grow = int(input("증가값 입력: "))
# for i in range(start, end+1, grow):
#     if i % 7 == 0:
#         print(i)

# Sum = 0
# for n in range(1, 101, 1):
#     if n % 3 == 0 and n % 5 == 0:
#         Sum += n
# print(Sum)

#내가한거, 틀림
# num1 = int(input("숫자 입력:"))
# num2 = int(input("숫자 입력:"))
# if num1 < num2:
#     for i in range(num1, num2+1, 1):
#         num1 += i
#     print(num1)
# elif num1 > num2:
#     for i in range(num2, num1+1, 1):
#         num2 += i
#     print(num2)
# else:
#     print(0)
#선생님
# Sum = 0
# num1 = int(input("첫번째 숫자 입력:"))
# num2 = int(input("두번째 숫자 입력:"))
# if num1 < num2:
#     for i in range(num1, num2+1, 1):
#         Sum += i
#         print(Sum)
# elif num1 > num2:
#     for i in range(num2, num1+1, 1):
#         Sum += i
#         print(Sum)
# else:
#     print(0)

# #첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로
# #한달(30일) 동안 저축한 금액 중 마지막 저금액을 구하시오.
# n = 10
# Sum = 10
# for i in range (1, 30, 1):
#     n *= 2
#     Sum += n
# print(n)
# print(Sum)

# #선생님
# money = 10
# save = 10
# for i in range(2, 31): #문제 그대로 써야됨
#     money *= 2
#     save += money
# print("마지막 입금액: %d원, 총 저축 금액: %d원" % (money, save))



#리스트는 순서대로 대입
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print("i:", i)

# ls = [1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     print("i:", i)
# for i in ls:
#     print(i, end=" ")    

# ls = [10, "test", 123.123]
# print("list:", ls)
# print()
# for i in ls:
#     print("i에", i, "대입한 후 print() 실행")
#     print(type(i))

# st = "Hello Python"
# for i in st:
#     print("i:", i)
# for i in st:
#     print(i, end=" ")

a_sum=0
st = "It is a fun Python class"
#총개수, a개수, s개수를 구하시오
for i in st:
    print("총 개수")
    s_sum = 
    if i == "a":
        print("a 개수")
    if i == "s":
        print("s 개수")