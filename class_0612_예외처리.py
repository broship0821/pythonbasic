## try ~ except

# n1 = 10
# n2 = 0
# try: # try 없으면 에러남
#     result = n1/n2
#     print("%d / %d = %d" % (n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다")
# print("프로그램 정상 종료")

## 사용자가 입력할때 에러가 많이 남
# try: 
#     n1 = 10
#     n2 = int(input("정수 입력:")) # 0을 치면 에러남, 문자를 입력해도 똑같이 나옴
#     result = n1/n2
#     print("%d / %d = %d" % (n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다")
# print("프로그램 정상 종료")

# 반복문 사용해서 try 2번쓰기
# while True:
#     try:
#         n1 = int(input("정수1: "))
#         n2 = int(input("정수2: "))
#         break
#     except:
#         print("숫자만 입력하세요")
# try:
#     result = n1/n2
#     print("%d / %d = %d" % (n1,n2,result))
# except:
#     print("0으로 나눌 수 없습니다")
# print("프로그램 정상 종료")

# s = input('정수: ')
# try:
#     point = int(s)
#     print(150/point)
# except ValueError:
#     print("숫자만 입력하세요")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다")
# except NameError:
#     print("프로그램 내부 문제가 발생했습니다")
# except:
#     print("알수없는 오류 발생, 점검 후 조치하겠습니다") # 지정하지 않은 변수 사용하면 에러남 그때 또 추가
# print("프로그램 정상 종료")

# pet = ['거북이','타란튤라','전갈']
# for i in range(4):
#     try:
#         print(pet[i],'키울레용')
#     except:
#         print("애완동물의 정보가 없습니다.")
#     finally: # 예외처리(에러)와 상관없이 꼭 실행되야 하는경우
#         print("애완동물 좋아")
# print("프로그램 정상 종료")

