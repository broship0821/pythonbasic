# 변수[스코핑 룰]
# 지역변수와 전역변수
# 지역변수는 한정된 지역(Local) 에서만 사용되는 변수,
# 전역변수는 프로그램 전체(Global)에서 사용되는 변수
## 지역변수는 해당 함수가 종료되면 소멸되기 때문에 프로그램이 가벼워 질수 있음, 전역보다는 지역변수 사용

# def func1():
#     a = 100 # 이 함수가 끝나면 a는 소멸됨, 지역변수
#     print("func1의 a: %d" % a)
# def func2():
#     a = 200
#     print("func2의 a: %d" % a)
# func1()
# func2()

# def func1():
#     print("func1의 a: %d" % a) # 변수명이 같아야됨
# def func2():
#     print("func2의 a: %d" % a)
# a = 200 # 전역변수 프로그램 종료와 동시에 종료됨
# func1()
# func2()

# def func1():
#     a = 123 # 지역변수가 높은 우선순위를 가짐
#     print("func1의 a: %d" % a)
# def func2():
#     print("func2의 a: %d" % a)
# a = 200 # 전역변수
# func1()
# func2()

# def func1():
#     global a # a를 전역변수로 선언
#     a = 12223 # 밖에있는 전역변수를 12223으로 바꿈
#     print("func1의 a: %d" % a)
# def func2():
#     print("func2의 a: %d" % a)
# a = 55555 # 전역변수
# func1() # 이때 전역변수가 바뀜
# func2() # 이때 55555가 아닌 12223을 사용

# def display():
#     num = 10
#     print("10까지의 합:", sumFunc(num))
# def sumFunc(num):
#     sum = 0
#     for i in range(num+1):
#         sum += i
#     return sum
# display()


## 기본 매개변수값
# def sum_func(x1,x2,x3 = 100): # x3의 기본값, 함수 호출할때 매개변수 지정해주지 않으면 기본값 나옴
#     result = 0
#     result = x1 + x2 + x3
#     return result
# def display():
#     Sum = 0
#     a,b,c = 10,20,30
#     Sum = sum_func(a,b) # 개수 매칭이 안될때 기본값을 사용해 연산
#     print("매개변수 2개 함수 호출:", Sum) # 10 + 20 + 100
#     Sum = sum_func(a,b,c)
#     print("매개변수 3개 함수 호출:", Sum) # 10 + 20 + 30
# display()

# def alba(day=30,time=8,won=8500):
#     result = day * time * won
#     return result
# def display():
#     num = int(input("1.기본급\n2.일한 날짜 입력\n"))
#     if num == 1:
#         result = alba()
#     elif num == 2:
#         day = int(input("일한 날짜 수 입력:"))
#         result = alba(day) # alba()의 첫번째 매개변수로 삽입됨
#     print("당신의 급여는 {:,}원 입니다.".format(result))
# display()

### 가변 매개변수*: 입력되는 값을 튜플로 받음
# def sum_func(*par):
#     result = 0
#     print(type(par))
#     print(par)
#     for num in par:
#         result = result + num
#         print("num:%d" % num)
#     return result
# Sum = 0
# Sum = sum_func(10,20)
# print("매개변수 2개 함수:", Sum)
# Sum = sum_func(10,20,30,40)
# print("매개변수 4개 함수:", Sum)

## 가변 매개변수**: 입력되는 값을 딕셔너리로 받음
# def dic_func(**par):
#     print("type(par):", type(par))
#     for k in par.keys():
#         print("{}:{}명 입니다.".format(k,par[k]))
# dic_func(똭뚝뽹=123,꿔익꿔익=8,test="테스뚜")

# def change(a,b,c):
#     return a+10,b+20,c+30 # 여러개의 값을 return받을땐 튜플로 받음
# a,b,c=change(10,20,30) # 언패킹처리
# d = change(10,20,30)
# print("a,b,c:",a,b,c)
# print(a+b+c)
# print("d:{}, type:{}".format(d,type(d)))

# def swap(x,y):
#     return y,x
# a=10
# b=20
# print("바꾸기 전:",a,b)
# a,b=swap(a,b)
# print("바꾼 후:",a,b)


## lambda 함수: 1회성, 단발성으로 위치 바꿔줌
# swap = lambda a,b:[b,a]
# a = swap(20,10)
# print("swap 결과:", a) #데이터 위치도 바뀌고 리스트로 바뀜
# swap = lambda a,b:(b,a)
# a = swap(20,10)
# print("swap 결과:", a) # 튜플로 바뀜
# swap = lambda a,b:{b,a}
# a = swap(20,10)
# print("swap 결과:", a) # 딕셔너리로 바뀜, 뭘로든 묶어줘야됨, 안묶으면 에러

# lam = lambda a:a*10
# hap = lambda a,b:a+b
# noData = lambda : print("인자값 없는 람다")
# print(lam(10))
# print(hap(5,10))
# noData()

# def startGame(): # 게임 시작은 여러번 할 수 있으니 함수로 만들어서 자주 사용
#     print("Game start!")
# def test():
#     print("1. 게임 시작")
#     print("2. 게임 종료")
#     num = int(input("선택:"))
#     if num == 1:
#         startGame()
#     elif num == 2:
#         end()
# end = lambda : print("게임 종료") # 게임 종료는 한번만 하면 되니 람다 함수 사용
# test()