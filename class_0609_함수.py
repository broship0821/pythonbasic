## 사용자 정의 함수

# result, temp = 0, 0
# result = int(input("수 입력:"))
# while True:
#     temp = int(result%10)
#     result = int(result/10)
#     print(temp, end='')
#     if not result: #result가 0일때 종료
#         break
# print("\n프로그램 종료")

# def reverseCode():
#     result, temp = 0, 0
#     result = int(input("수 입력:"))
#     while True:
#         temp = int(result%10)
#         result = int(result/10)
#         print(temp, end='')
#         if not result:
#             break
# print("프로그램 시작")
# reverseCode() # 이렇게 바로 쓸 수 있음
# print()
# print(1)
# print(2)
# reverseCode()
# print()
# reverseCode()
# print()
# print(3)
# reverseCode()
# print("\n프로그램 종료")

# sel = 0
# sel = int(input("음료 선택\n1. 콜라\n2. 핫식스\n3. 포카리\n입력:"))
# if sel == 1:
#     print('콜라')
# elif sel == 2:
#     print("핫식스")
# elif sel == 3:
#     print("포카리")
# else:
#     print("만들어 드세요^^")
# if sel >= 1 and sel <=3:
#     print("맛있게 드세요")

# def sel_machine():
#     sel = 0
#     sel = int(input("음료 선택\n1. 콜라\n2. 핫식스\n3. 포카리\n입력:"))
#     if sel == 1:
#         print('콜라')
#     elif sel == 2:
#         print("핫식스")
#     elif sel == 3:
#         print("포카리")
#     else:
#         print("만들어 드세요^^")
#     if sel >= 1 and sel <=3:
#         print("맛있게 드세요")
# sel_machine()
# sel_machine()
# sel_machine()
# sel_machine()

# def calc():
#     result = 0
#     su1, op, su2 = int(input("숫자:")), input("부호:"), int(input("숫자:"))
#     if op == "+":
#         result = su1 + su2
#     elif op == "-":
#         result = su1 - su2
#     elif op == "/":
#         result = su1 / su2
#     elif op == "*":
#         result = su1 * su2
#     print("%d %c %d = %.1f" % (su1, op, su2, result))
# calc()

# def cal(num1, op, num2): # 매개변수는 지역변수, 호출될때 개수만 매칭되면 되고 똑같은 이름일 필요는 없음
#     result = num1+num2
#     print(num1,'+',num2,'=',result)
# su1, op, su2 = int(input("숫자:")), input("부호:"), int(input("숫자:"))
# cal(su1,op,su2)

# def cal(num1, op, num2):
#     result = num1+num2
#     print('cal 실행')
#     return result #함수 종료, 뒤에있는 값은 호출될때 되돌려줌, 변수,상수,none 다 가능
# su1, op, su2 = int(input("숫자:")), input("부호:"), int(input("숫자:"))
# result = cal(su1,op,su2)
# print(su1,'+',su2,'=',result)
# print("다음 문장 실행")

# def showAvrg(a,b,c):
#     print("{}와 {}의 평균".format(a,b))
#     print("값은 {}입니다".format(round(c,1)))
# def avrg(j,k):
#     total = j+k
#     f = total/2
#     return f
# #위에 두 함수는 순서가 뒤바껴도 상관없음
# i = 2
# j = 3
# f = avrg(i,j)
# showAvrg(i,j,f)
# # 하지만 실행될때 순서가 뒤바뀌면 안됨
# print("다음 문장 실행")

# def func2(a,b):
#     a += 5
#     b *= 10
#     print("func2: a = {}, b = {}".format(a,b))
# def func1():
#     a = 5
#     b = 10
#     func2(a,b)
#     print("func1: a = {}, b = {}".format(a,b))
# func1()

## 함수 호출 방법
# def 함수명(매개변수1~n):

# 1. 함수명()
# 2. 함수명(인수1,인수2~인수n)
# 3. 변수 = 함수명()
# 4. 변수 = 함수명(인수1,인수2~인수n)
# 되돌려 받는 값이 있을수도 있고 없을수도 있음

# def aa(a):
#     if a == 1:
#         print("1입력")
#     print('다음 문장 실행')
# a = aa(1)
# print("리턴값:",a)
# print("프로그램 종료")

# def aa(a):
#     if a == 1:
#         return # 함수 즉시 종료 밑의 코드 적용되지 않음
#         print("1입력")
#     print('다음 문장 실행')
# a = aa(1)
# print("리턴값:",a)
# print("프로그램 종료")

# def move():
#     print('이동')
# # def attack(): # 함수만 정의하고 내용이 없으면 에러남
    
# def defense():
#     pass #내용이 없을땐 pass 사용/ 임시로 함수 만들어 놀때 사용
# move()
# # attack()
# defense()



## 짝,홀수를 구분하는 함수를 만드시오
# def holjjak():
#     num = int(input("숫자 입력:"))
#     if num % 2 == 0:
#         print("{}은 짝수 입니다".format(num))
#     else:
#         print("{}은 홀수 입니다".format(num))
# holjjak()
## 매개변수 사용
# def holjjak(num):
#     if num % 2 == 0:
#         print("{}은 짝수 입니다".format(num))
#     else:
#         print("{}은 홀수 입니다".format(num))
# num = int(input("숫자 입력:"))
# holjjak(num)
## 선생님꺼
# def jjak_hol(num1):
#     if num1 % 2 == 0:
#         return True
#     else:
#         return False
# num1 = int(input("숫자 입력:"))
# ret = jjak_hol(num1)
# if ret:
#     print("{}은 짝수 입니다".format(num1))
# else:
#     print("{}은 홀수 입니다".format(num1))

## 3의 배수를 판별하는 함수를 만드시오
# def three():
#     num = int(input("숫자 입력:"))
#     if num % 3 == 0:
#         print("{}은 3의 배수 입니다".format(num))
#     else:
#         print("{}은 3의 배수가 아닙니다".format(num))
# three()
## 선생님꺼
# def Three_mul(num1):
#     ret = num1%3
#     return ret
# num1 = int(input("숫자 입력:"))
# if not(Three_mul(num1)): # ret이 3의 배수가 되서 0이되면 not으로 True로바꿔줌, 그때만 실행됨
#     print("{}은 3의 배수 입니다".format(num1))

### 계산기
# def cal_input():
#     su1, op, su2 = int(input("숫자:")), input("부호:"), int(input("숫자:"))
#     return su1, su2, op
# def calculate(su1,su2,op):
#     if op == "+":
#         result = su1 + su2
#     elif op == "-":
#         result = su1 - su2
#     elif op == "/":
#         result = su1 / su2
#     elif op == "*":
#         result = su1 * su2
#     return result
# def cal_print(su1,su2,op,result):
#     print("%d %c %d = %.1f" % (su1, op, su2, result))
# def calculater():
#     # ls = [] 하나 이상의 값이 담기면 자동으로 list가 됨 # 그런줄 알았는데 튜플로 받음
#     ls = cal_input()
#     result = calculate(ls[0],ls[1],ls[2])
#     cal_print(ls[0],ls[1],ls[2],result)
# calculater()
## 선생님 방법
# def cal_print(su1,su2,op,result):
#     print("%d %c %d = %.1f" % (su1, op, su2, result))
# def calculate(su1,su2,op):
#     if op == "+":
#         result = su1 + su2
#     elif op == "-":
#         result = su1 - su2
#     elif op == "/":
#         result = su1 / su2
#     elif op == "*":
#         result = su1 * su2
#     cal_print(su1,su2,op,result)
# def cal_input():
#     su1, op, su2 = int(input("숫자:")), input("부호:"), int(input("숫자:"))
#     calculate(su1,su2,op)
# cal_input()


## 거꾸로 수를 반환하는 함수를 만드시오
# def reverseCode():
#     result = int(input("수 입력:"))
#     i=''
#     while True:
#         temp = str(result%10)
#         result = int(result/10)
#         i += temp
#         if not result:
#             break
#     return int(i)
# print("프로그램 시작")
# reverseCode()
# print("프로그램 종료")
### 매개변수 사용해보기
# def reverseCode(result):
#     i=''
#     while True:
#         temp = str(result%10)
#         result = int(result/10)
#         i += temp
#         if not result:
#             break
#     return int(i)
# print(reverseCode(int(input("숫자 입력:"))))
