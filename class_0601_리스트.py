# ###리스트
# 리스트는 데이터의 목록을 다루는 자료형
# []대괄호로 명명한다
# 리스트 안에는 어떠한 자료형도 포함시킬수 있음 C는 같은 자료형만 가능

# 변수가 많아지면 관리해야할 사항이 많아지고 실수할 확률이 높아짐
# 리스트는 연속적으로 되있어서 데이터 가져오기 편함

# 리스트를 가져올때는 인덱스를 사용 0번부터

# ls = [500, 200, 300, 400]
# Sum = 0
# print("ls:", ls)
# print("ls[0]:", ls[0])
# print("ls[1]:", ls[1])
# print("ls[2]:", ls[2])
# print("ls[3]:", ls[3])
# #맨 오른쪽이 -1 맨 왼쪽은 -n임
# ls = [500, 200, 300, 400]
# Sum = 0
# print("ls:", ls)
# print("ls[0]:", ls[-4])
# print("ls[1]:", ls[-3])
# print("ls[2]:", ls[-2])
# print("ls[3]:", ls[-1])

# ls = [0, 0, 0, 0] #박스를 생성해주는 일, 0이 아닌 다른게 들어가도 상관없음
# Sum = 0
# ls[0] = int(input("1번째 숫자 입력:"))
# ls[1] = int(input("2번째 숫자 입력:"))
# ls[2] = int(input("3번째 숫자 입력:"))
# ls[3] = int(input("4번째 숫자 입력:"))
# Sum = ls[0] + ls[1] + ls[2] + ls[3]
# print("ls[0]:", ls[0])
# print("ls[1]:", ls[1])
# print("ls[2]:", ls[2])
# print("ls[3]:", ls[3])
# print("리스트의 합: %d" % Sum)


# ls = [0, 0, 0, 0]
# Sum = 0
# print("len(ls):", len(ls))
# for i in range (len(ls)):
#     ls[i] = int(input(str(i+1)+"번째 숫자 입력:"))
#     Sum += ls[i]
# for i in range(len(ls)):
#     print("ls[%d]:" % i, ls[i])
# print("리스트의 합:", Sum)

# ls = [10, 20, 30, 40]
# print("ls:", ls)
# print()
# print("ls[1:3] => ls[1]~[2]:", ls[1:3])
# print("ls[0:3] => ls[0]~[2]:", ls[0:3])
# print("ls[2:] => ls[2] ~ [끝까지]", ls[2:]) #비워두나 전체길이보다 큰 숫자를 적으면 끝까지
# print("ls[:2] => ls[0] ~ [1]", ls[:2])
#[:]우측은 그 전까지, 좌측은 그 숫자 포함


#### 중요 ####
# ## 리스트[얕은 복사] 데이터 하나를 공유
# ls = [10, 20, 30, 40]
# arr = ls
# print("ls: {}ls, id: {}".format(ls,id(ls)))
# print("arr: {}arr, id: {}".format(arr,id(arr)))
# #arr = ls = [10,20,30,40] 불리는 이름만 다르지 이 둘은 같은 개체임
# ls = [10, 20, 30, 40]
# arr = ls
# arr[2] = 20000
# print("ls: {}ls, id: {}".format(ls,id(ls)))
# print("arr: {}arr, id: {}".format(arr,id(arr)))
# ## ls arr 이 둘은 서로 동기화됨

# ## 리스트[깊은 복사] 똑같은 데이터 2개
# ls = [10, 20, 30, 40]
# arr = ls[:] # arr = [10, 20, 30, 40] 이거랑 똑같은 개념임
# arr[2] = 20000
# print("ls: {}ls, id: {}".format(ls,id(ls)))
# print("arr: {}arr, id: {}".format(arr,id(arr)))

#입고, 재고, 출고
#출고랑 재고는 동기화가 되야되서 얕은 복사
#입고랑 재고는 동기화가 되면 안됨(재고=입고+재고 라고 해서 입고까지 바뀌면 안됨) 깊은 복사

# import copy # copy 라는 묘듈을 가져와라 (묘듈: 함수의 모임)
# ls = [10, 20, 30, 40]
# #arr = ls[:]
# arr = copy.deepcopy(ls)
# arr[2] = "deepcopy"
# print("ls: {}ls, id: {}".format(ls,id(ls)))
# print("arr: {}arr, id: {}".format(arr,id(arr)))


##업데이트 연산
# ls = [10, 20, 30]
# arr = [40, 50, 60]
# print("ls:", ls)
# print("arr:", arr)
# Str = ls + arr
# print("ls + arr => Str", Str)
# string = ls * 3
# print("ls * 3 => string", string)

##숫자 연산
# ls = [10, 20, 30]
# arr = [40, 50, 60]
# for i in range(len(ls)):
#     ls[i] = ls[i] + arr[i]
# print(ls)
# for i in range(len(ls)):
#     ls[i] = ls[i] * 3
# print(ls)
#선생님 방법
# ls = [10, 20, 30]
# arr = [40, 50, 60]
# Str = [0, 0, 0]
# string = [0, 0, 0]
# for i in range(len(ls)):
#     Str[i] = ls[i] + arr[i]
# for i in range(len(ls)):
#     string[i] = ls[i] * 3
# print(Str)
# print(string)