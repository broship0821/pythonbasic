# st = "Hello Python Fun"
# na = input("찾고자 하는 문자열 입력")
# if na in st:
#     print("st:", st, "찾는 문자열:", na, "존재 한다")
# else:
#     print("st안에는", na, "존재하지 않습니다")

# old_id = input("저장할 id 입력:")
# print("인증 프로그램 입니다")
# print("id와 pw를 입력하세요")
# new_id = input("id 입력:")
# if old_id ==  new_id:
#     print("인증 되셨습니다")
# else:
#     print("인증 실패")

##중첩된 if문
# num = int(input("수 입력:"))
# if num % 3 == 0:
#     if num % 2 == 0:
#         print("num은 3의 배수이면서 짝수 입니다")
# print("다음 문장 실행")

# num = int(input("수 입력:"))
# if num % 3 == 0 and num % 2 == 0:
#     print("num은 3의 배수이면서 짝수 입니다")
# print("다음 문장 실행")

# num = int(input("수 입력:"))
# if num > 0:
#     if num % 2 == 0:
#         print("num은 양의 짝수 입니다")
#     else:
#         print("num은 양의 홀수 입니다")
# else:
#     print("num은 음수 입니다")
# print("다음 문장 실행")


# Gbyte = int(input("Gbyte 입력:"))
# menu = int(input("1.byte 2.Kbyte 3.Mbyte: "))
# if menu == 1:
#     Gbyte = Gbyte * 2 ** 30
#     print("%dbyte" % Gbyte)
# if menu == 2:
#     Gbyte = Gbyte * 2 ** 20
#     print("%dKbyte" % Gbyte)
# if menu == 3:
#     Gbyte = Gbyte * 2 ** 10
#     print("%dMbyte" % Gbyte)

# #로그인 네이버 버전
# old_id = input("저장할 id 입력:")
# old_pw = input("저장할 pw 입력:")
# print("인증 프로그램 입니다")
# print("id와 pw를 입력하세요")
# new_id = input("id 입력:")
# new_pw = input("pw 입력:")
# if old_id == new_id:
#     if old_pw == new_pw:
#         print("인증 되셨습니다")
#     else:
#         print("비밀번호가 틀렸습니다")
# else:
#     print("등록되지 않은 id 입니다 ")

# #로그인 구글 버전
# old_id = input("저장할 id 입력:")
# old_pw = input("저장할 pw 입력:")
# print("인증 프로그램 입니다")
# print("id와 pw를 입력하세요")
# new_id = input("id 입력:")
# if old_id != new_id:
#     print("등록되지 않은 id 입니다 ")
# else:
#     new_pw = input("pw 입력:")
#     if old_pw != new_pw:
#         print("비밀번호가 틀렸습니다")
#     if old_pw == new_pw:
#         print("인증 되셨습니다")
#다른 방법
# old_id = input("저장할 id 입력:")
# old_pw = input("저장할 pw 입력:")
# print("인증 프로그램 입니다")
# print("id와 pw를 입력하세요")
# new_id = input("id 입력:")
# if old_id == new_id:   
#     new_pw = input("pw 입력:")
#     if old_pw == new_pw:
#         print("인증 되셨습니다")
#     else:
#         print("비밀번호가 틀렸습니다")
# else:
#     print("등록되지 않은 id 입니다 ")

##elif문
# num = int(input("수 입력:"))
# if num > 100:
#     print("100보다 큰 수 입력")
# elif num > 50:
#     print("50보다 큰 수 입력")
# elif num > 0:
#     print("0보다 큰 수 입력")
# else:
#     print("그 외의 값 입력")
# #가장 범위가 좁은게 상단에 있어야됨, 밑으로 갈수록 범위가 커짐
# num = int(input("수 입력:"))
# if num > 0:
#     print("0보다 큰 수 입력")
# elif num > 50:
#     print("50보다 큰 수 입력")
# elif num > 100:
#     print("100보다 큰 수 입력")
# else:
#     print("그 외의 값 입력")

# name = input("이름:")
# num = int(input("학번:"))
# kor = int(input("국어:"))
# eng = int(input("영어:"))
# math = int(input("수학:"))
# total = kor + eng + math
# avg = total / 3
# print("총점:", total)
# print("평균:", avg)
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# elif avg >= 60:
#     print("D")
# else:
#     print("F")
##다른 방법
# name = input("이름:")
# num = int(input("학번:"))
# kor = int(input("국어:"))
# eng = int(input("영어:"))
# math = int(input("수학:"))
# total = kor + eng + math
# avg = total / 3
# if avg >= 90:
#     grade = "A"
# elif avg >= 80:
#     grade = "B"
# elif avg >= 70:
#     grade = "C"
# elif avg >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print("====================학생 정보====================")
# print("이름\t학번\t국어\t영어\t수학\t합계\t평균\t학점")
# print("%s\t%d\t%d\t%d\t%d\t%d\t%.2f\t%s" % (name, num, kor, eng, math, total, avg, grade))

# coffee = 2000
# num = int(input("커피 개수:"))
# if num <= 10:
#     money = coffee * num
#     print("가격:", money)
# else:
#     money = 20000 + (num-10)*1500
#     print("가격:", money)

# num = int(input("정수 입력:"))
# if num == 0:
#     print("0은 3의 배수도 4의 배수도 아닙니다")
# elif num % 3 == 0 and num % 4 == 0:
#     print("3의 배수이면서 4의 배수 입니다")
# elif num % 3 == 0:
#     print("3의 배수입니다")
# elif num % 4 == 0:
#     print("4의 배수 입니다")
# else:
#     print("3의 배수도 4의 배수도 아닙니다")
##### elif num % 3 != 0 and num % 4 != 0:
#####     print("3의 배수도 4의 배수도 아닙니다")


#비행기를 타는데 30분 거리까지의 기본 요금은 3만원이며 10분 단위로 추가요금 5천원씩 부가된다.
#비행기 탈 시간을 입력하여 요금 계산기를 만드시오

# airplan = 30000
# time = int(input("비행기 탈 시간:"))
# if time <= 30:
#     money = airplan
#     print("요금은 %d원 입니다" % money)
# elif 40 >= time > 30:
#     plus_money = 5000
#     money = airplan + plus_money*1
#     print("요금은 %d원 입니다" % money)
# elif 50 >= time > 40:
#     plus_money = 5000
#     money = airplan + plus_money*2
#     print("요금은 %d원 입니다" % money)
# elif 60 >= time > 50:
#     plus_money = 5000
#     money = airplan + plus_money*3
#     print("요금은 %d원 입니다" % money)
# elif 70 >= time > 60:
#     plus_money = 5000
#     money = airplan + plus_money*4
#     print("요금은 %d원 입니다" % money)
# elif 80 >= time > 70:
#     plus_money = 5000
#     money = airplan + plus_money*5
#     print("요금은 %d원 입니다" % money)

#다른 방법
# money = 30000
# time = int(input("비행기 탑승 시간 입력(분단위):"))
# time -= 30
# if time > 0:
#     if time % 10 == 0:
#         money = money + time//10*5000
#     else:
#         money = money + time//10*5000 + 5000
# print("비행기 탑승 요금: %d" % money)

#또다른 방법
# money = 30000
# time = int(input("비행기 탑승 시간 입력(분단위):"))
# time -= 30
# if time > 0:
#     money = money + ((time-1)//10)*5000 + 5000
# print("비행기 탑승 요금: %d" % money)