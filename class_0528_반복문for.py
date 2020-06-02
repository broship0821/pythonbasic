## 이중 for문 / 중첩 for문
#총 반복 횟수 = 바깥 반복수 * 안쪽 반복수

# for i in range(0, 3,):
#     for k in range(0, 5):
#         print("이중 for문 (i: %d\tk:%d)" % (i, k))

##구구단
# for i in range(2, 10,):
#     for j in range(1, 10):
#         print("{} * {} = {}".format(i, j, i*j))
#     print()

# print("{:=^60}".format(" 구 구 단 "))
# print("{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}".format("2단", "3단", "4단", "5단", "6단", "7단", "8단", "9단"))
# print("{:=^63}".format("="))
# for i in range(1, 10,):
#     for j in range(2, 10):
#         print("{}*{}={:<3}".format(j, i, i*j), end=" ")
#     print()

# print("{:=^124}".format(" 구 구 단 "))
# print("{:^14}{:^14}{:^14}{:^14}{:^14}{:^14}{:^14}{:^14}".format("2단", "3단", "4단", "5단", "6단", "7단", "8단", "9단"))
# print("{:=^127}".format("="))
# for i in range(1, 10,):
#     for j in range(2, 10):
#         print("{} * {} = {}".format(j, i, i*j), end="\t")
#     print()
# ##선생님꺼
# print("{:=^61}".format(" 구 구 단 "))
# for i in range(2, 10):
#     print("{:^5}".format("{}단".format(i)), end="\t")
# print()
# print("="*64)
# for i in range(1, 10,):
#     for j in range(2, 10):
#         print("{}*{}={:<3}".format(j, i, i*j), end=" ")
#     print()

# #예시 실패작
# for i in range(0, 5):
#     for j in range(0, 5):
#         print("상위포문 {} 일때 하위 포문:{}{}{}{}{}".format(i,i*j,i*j,i*j,i*j,i*j))

# for j in range(0, 5):
#     print("{}".format(j), end=" ")
# for i in range(0, 5):
#     print("상위포문 {} 일때".format(i))
#선생님이 한거
# for i in range(5):
#     print("상위포문 %d 일때 하위포문: " % i, end=" ")
#     for j in range(5):
#         print(i * j, end=" ")
#     print()



# for i in range(1,26):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i, end="\t")
## 이거를 2중 포문으로 작성
# for i in range(1,6):
#     print(i, end="\t")
#     for j in range(5):
#         print(i+j, end="\t")
#     print()

# for i in range(1,6):
#     print(i, end="\t")
# print()
# for i in range(6,11):
#     print(i, end="\t")



# #선생님
# for i in range(1, 22, 5):
#     print(i, end="\t")
#     for j in range(1,5):
#         print(i+j, end="\t")
#     print()
#다른 방법
# for j in range(5):
#     for k in range(1,6):
#         print(j*5+k, end="\t")
#     print()
