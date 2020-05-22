# print("숫자 입력")
# num1 = input()
# print("입력 받은 값:", num1)

# print("이름 입력:")
# name = input()
# print("나이 입력:")
# age = input()
# #print("%s 님의 나이는 %d 살 입니다." % (name, age)) type에러 
# print("%s 님의 나이는 %s 살 입니다." % (name, age))
# print("{} 님의 나이는 {} 살 입니다.".format(name, age))

# #input()은 자동으로 문자열을 받음
# print("두 수의 합을 구해 줍니다")
# print("두 수 입력")
# num1 = input()
# num2 = input()
# #num3 = num1 + num2
# num3 = int(num1) + int(num2)
# print("두 수의 합:", num1, "+", num2, "=", num3)
# print("num1 type:", type(num1))
# print("num2 type:", type(num2))
# print("num3 type:", type(num3))
## 이렇게 하면 후에 출력할때 마다 형변환을 해줘야됨

# num1 = int(input())
# num2 = int(input())
# result = num1 + num2
# print(num1, "+", num2, "=", result)
# result = num1 - num2
# print(num1, "-", num2, "=", result)
# result = num1 * num2
# print(num1, "*", num2, "=", result)
# result = num1 / num2
# print(num1, "/", num2, "=", result)

# #올바른 입력을 하도록 설명을 해줘야 되고 입력값에 맞는 형 변환을 해줘야됨
# print("문자열 입력")
# name = input()
# print("정수 입력")
# age = int(input())
# print("실수 입력")
# flt = float(input())
# print("name 값:", name,"\t type:", type(name))
# print("age 값:", age,"\t type:", type(age))
# print("flt 값:", flt,"\t type:", type(flt))

# #input(이곳에 출력할 문구 넣기)
# name = input("이름을 입력 하세요:")
# age = int(input("나이를 입력 하세요:"))
# addr = input("주소를 입력 하세요:")
# print("이름:", name, "\n나이:", age, "\n주소:", addr)

# test = input(10)
# test = input("숫자를 %d번 입력하세요" % 10)
# #test = input("숫자를" ,10,"번 입력하세요") type에러, input(이 안에는 ,로 구분할 수 없음)

# #올해 년도와 태어난 년도를 구하여 나이를 계산하는 프로그램을 코딩하시오
# year = int(input("올해의 년도를 4자리로 입력하시오:"))
# birth = int(input("당신이 태어난 년도를 4자리로 입력하시오:"))
# age = year - birth + 1
# print("당신의 나이는 %d살 입니다" % age)
# print("당신의 나이는 %d살 입니다" % (year - birth + 1)) #연산자도 ()로 묶어줘야됨

# #600kg 제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입력받아 현재
# #엘리베이터에 더 적재할 수 있는 무게를 구하시오
# first = float(input("첫 번째 물건의 무게를 입력하시오:"))
# second = float(input("두 번째 물건의 무게를 입력하시오:"))
# print("현재 엘리베이터의 허용 무게는 %.2fkg 입니다." % (600 - first - second))
# result = 600 - first - second
# print("현재 엘리베이터의 허용 무게는 %.2fkg 입니다." % result)

# tall = float(input("키를 입력하시오:"))
# fat = (tall - 100) * 0.9
# print("표준 체중은 %.1f 입니다." % fat)

# tall = float(input("키를 입력하시오:"))
# weight = float(input("현재 체중을 입력하시오:"))
# pyojun = (tall - 100) * 0.9
# fat = (weight/pyojun) * 100
# print("표준 체중은 %.1f이고 비만도는 %.2f입니다." % (pyojun, fat))

# name = input("학생 이름:")
# kor = int(input("국어 점수:"))
# eng = int(input("영어 점수:"))
# math = int(input("수학 점수:"))
# total = kor + eng + math
# avg = total / 3
# print("====================학생 정보====================")
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("%s\t%d\t%d\t%d\t%d\t%.2f\t" % (name, kor, eng, math, total, avg))