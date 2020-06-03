## 순위구하기
# rank = [1, 1, 1, 1, 1]
# num = [82, 85, 76, 79, 96]
# for i in range(len(num)):
#     for j in range(len(num)):
#         if num[i] < num[j]:
#             rank[i] += 1
#     print(num)
#     print(rank)
#다른방법
# rank = []
# num = [82, 85, 76, 79, 96, 64, 99]
# for i in range(len(num)):
#     rank.append(1)
#     for j in range(len(num)):
#         if num[i] < num[j]:
#             rank[i] += 1
# for i in range(len(num)):
#     print("점수: %d\t등수: %d" % (num[i], rank[i]))

## 리스트 조작 함수
#.append
# ls = [10, 20, 30]
# ls.append(100)
# ls.append(200)
# ls.append(100)
# ls.append(200)
# for i in range(len(ls)):
#     print("ls[{}]: {}".format(i, ls[i]))
# print("리스트의 총 개수:", len(ls))
# print("ls:", ls)
# ls=[] #리스트초기화
# print("ls초기화 후:", ls)
# print(type(ls))

# ls=[]
# for i in range(4):
#     ls.append(0)
# print(ls)
# Sum = 0
# for i in range(len(ls)):
#     ls[i] = int(input(str(i+1)+"번째 숫자: "))
#     Sum += ls[i]
# for i in range(len(ls)):
#     print("입력 받은 값ls[{}]: {}".format(i, ls[i]))
# print("합계: %d" % Sum)

# num = int(input("몇개의 공간을 만들겠습니까?:"))
# ls = []
# Sum = 0
# for i in range(num):
#     ls.append(int(input(str(i+1)+"번째 숫자: ")))
#     Sum += ls[i]
# for i in range(0,len(ls)):
#     print("입력 받은 값ls[{}]: {}".format(i, ls[i]))
# print("합계: %d" % Sum)

## pop(빼내고 제거) sort(오름차순 정렬) reverse(역순) del(삭제)
# List = [15, 40, 30, 20, 10, 35, 25, 65, 15]
# print("현재 리스트:", List)
# List.append(50)
# print("append(50) 후 리스트:", List)

# test = List.pop(1)
# print(test)
# List.pop(0)
# print("pop(0) 후 리스트:", List)
# List.sort()
# print("sort() 후 리스트:", List)
# List.reverse()
# print("reverse() 후 리스트:", List)
# del(List[3])
# print("del(List[3]) 후 리스트:", List)

## index insert remove extend count
# List = [15, 40, 30, 20, 10, 35, 25, 65, 45]
# print("현재 리스트:", List)

# print("10값의 위치:", List.index(10))
# List.insert(3, 60)
# print("insert(3, 60) 후 리스트:", List)
# List.remove(60)
# print("remove(60) 후 리스트:", List)
# List.extend([75, 80, 85, 15, 15]) # +연산이랑 동일
# print("extend([75, 80, 85]) 후 리스트:", List)
# print("15값의 개수:", List.count(15))

# # print("15값의 위치:", List.index(150)) #여러개면 첫번째만 찾아줌/ 값이 없으면 에러
# List.insert(30, 60) 
# print("insert(30, 60) 후 리스트:", List) # 범위 넘어서면 그냥 맨 뒤에 추가됨
# # List.remove(600)
# # print("remove(600) 후 리스트:", List) #없는 값은 에러
# List.remove(15)
# print("remove(15) 후 리스트:", List) # 중복되면 첫번째만 삭제
# print("15값의 개수:", List.count(15120912)) # 없으면 0





###숙제
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]
#리스트 2개를 만들어서 홀수번째의 값, 짝수번째의 값을 따로 넣고 짝수번째와 홀수번째의 차를
#또다른 리스트에 넣어놓고 출력하시오 답:[5, 13, -22, 1, -13]
# hol = []
# zzak = []
# result = []
# for i in range(len(ls)):
#     if i % 2 == 0:
#         hol.append(ls[i])
#     else:
#         zzak.append(ls[i])
# for i in range(len(hol)):
#     result.append(hol[i] - zzak[i])
# print(result)

#ls의 값중 인덱스 홀수번째와 짝수 번째의 합과 차를 구하시오(짝수[0,2,4,8]-홀수[1,3,5,7,9])
#답: -16
# zzak_sum = 0
# hol_sum = 0
# for i in range(len(ls)):
#     if i % 2 == 0:
#         zzak_sum += ls[i]
#     else:
#         hol_sum += ls[i]
# print(zzak_sum-hol_sum)

# ls의 저장된 값을 invertLs에 거꾸로 저장하시오
#첫번째방법
# invertLs = ls
# for i in range(len(invertLs)//2):
#     j = -1-i
#     invertLs[j],invertLs[i] = invertLs[i],invertLs[j]
# print(invertLs)
#두번째 ls가 삭제됨
# invertLs = []
# for i in range(len(ls)):
#     invertLs.append(ls.pop())
# print(ls)
# print(invertLs)
#세번째
# invertLs = []
# for i in range(1,len(ls)+1):
#     invertLs.append(ls[-i])
# print(invertLs)

# ls의 값을 오름차순으로 sortLs에 저장 후 출력
# sortLs = ls[:]
# print(sortLs)
# for j in range(len(ls)-1):
#     for i in range(j+1, len(ls)):
#         if sortLs[j] > sortLs[i]:
#             sortLs[j], sortLs[i] = sortLs[i], sortLs[j]
# print(sortLs)
# ls의 값을 내림차순으로 reverseLs에 저장 후 출력
# reverseLs = ls[:]
# print(reverseLs)
# for j in range(len(ls)-1):
#     for i in range(j+1, len(ls)):
#         if reverseLs[j] < reverseLs[i]:
#             reverseLs[j], reverseLs[i] = reverseLs[i], reverseLs[j]
# print(reverseLs)