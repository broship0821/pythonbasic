#조건문, 조건분기문
#if문
# num1 = 10
# num2 = 5
# if num1 > num2:
#     print("num1 이 num2 보다 크다")
# if num2 - num1: #0을 제외한 모든 숫자는 참
#     print("num1 이 num2 보다 크다")
# if "나는 실행될까?": #문자열도됨, 0을 빼고 모든게 다 참
#     print("num1 이 num2 보다 크다")

# num1 = int(input("숫자 입력:"))
# if num1 % 2 == 0:
#     print("입력하신 숫자는:", num1, ", 짝수입니다.")
# print("나는 다음 문장")

# num1 = int(input("숫자 입력:"))
# if num1 % 2 == 0:
#     print("입력하신 숫자는:", num1, ", 짝수입니다.")
#     print("입력하신 숫자는:", num1, ", 2의 배수입니다.")
# print("나는 다음 문장")

# print("1. easy mode")
# print("2. hard mode")
# print("3. exit")
# num1 = int(input("선택:"))
# if num1 == 1:
#     print("easy mode start")
# if num1 == 2:
#     print("hard mode start")
# if num1 == 3:
#     print("game exitd")

# num1 = int(input("숫자 입력:"))
# if num1 > 10:
#     print("10보다 큽니다.")
# if num1 > 50:
#     print("50보다 큽니다.")
# if num1 > 100:
#     print("100보다 큽니다.")
# #결과: 중복실행됨
# 숫자 입력:123
# 10보다 큽니다.
# 50보다 큽니다.
# 100보다 큽니다.

# date = int(input("날짜 입력:"))
# if date % 7 == 0:
#     print("일요일")
# if date % 7 == 1:
#     print("월요일")
# if date % 7 == 2:
#     print("화요일")
# if date % 7 == 3:
#     print("수요일")
# if date % 7 == 4:
#     print("목요일")
# if date % 7 == 5:
#     print("금요일")
# if date % 7 == 6:
#     print("토요일")

#입력한 데이터가 3의 배수인 경우 출력하시오
# num1 = int(input("숫자 입력:"))
# if num1 % 3 == 0:
#     print(num1, ", 3의 배수")
#절대값을 구하는 프로그램을 작성하시오
# num1 = int(input("숫자 입력:"))
# if num1 >= 0:
#     print(num1)
# if num1 < 0:
#     print(-(num1))
#다른 방법
# num1 = int(input("숫자 입력:"))
# if num1 < 0:
#     num1 *= -1
# print(num1)
#수를 입력받아 짝, 홀수를 구분하여 출력하시오
# num1 = int(input("숫자 입력:"))
# if num1 % 2 == 0:
#     print("짝수입니다.")
# if num1 % 2 == 1:
#     print("홀수입니다.")
#두 수를 입력받아 큰 수를 출력하시오
# num1 = int(input("숫자 입력1:"))
# num2 = int(input("숫자 입력2:"))
# if num1 > num2:
#     print(num1)
# if num1 < num2:
#     print(num2)
#다른 방법
# if num1 < num2:
#     num1 = num2
# print(num1)
#세 수를 입력받아 큰 수를 출력하시오
# num1 = int(input("숫자 입력1:"))
# num2 = int(input("숫자 입력2:"))
# num3 = int(input("숫자 입력3:"))
# if num1 > num2 and num1 > num3:
#     print(num1)
# if num2 > num1 and num2 > num3:
#     print(num2)
# if num3 > num1 and num3 > num2:
#     print(num3)
#다른 방법
# if num1 < num2:
#     num1 = num2
# if num1 < num3:
#     num1 = num3
# print(num1)
#두 수를 입력 받아 큰 수가 짝수이면 출력하시오
# num1 = int(input("숫자 입력1:"))
# num2 = int(input("숫자 입력2:"))
# if num1 > num2 and num1 % 2 == 0:
#     print(num1)
# if num1 < num2 and num2 % 2 == 0:
#     print(num2)
#두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오
# num1 = int(input("숫자 입력1:"))
# num2 = int(input("숫자 입력2:"))
# num3 = num1 + num2
# if num3 % 2 == 0 and num3 % 3 == 0:
#     print(num3)


#if else문
# num = int(input("숫자 입력:"))
# if num == 1:
#     print("값은 1")
# else:
#     print("1이 아닌 값")

# arr = [1,2,3,4,5]
# na = int(input("찾을 숫자 입력:"))
# if na in arr:
#     print("arr:", arr, "찾는 숫자가 존재합니다:", na)
# else:
#     print("arr:", arr, "찾는 숫자가 없습니다:", na)
# print("결과:", na in arr)