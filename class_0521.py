# num1 = 10
# num2 = 20

# # print("num1(%d)" % num1, "+", "num2(%d)" % num2, "=", num1+num2)
# # print("num1({}) + num2({}) = {}".format(num1, num2, num1 + num2))

# print("num1(%d) + num2(%d) = %d" % (num1, num2, num1 + num2))
# print("num1(",num1,")+num2(",num2,")=",num1+num2) # , 사용하면 자동으로 공백 생김

# num1 = 7
# num2 = 5
# sum_ = num1 + num2
# minus = num1 - num2
# mul = num1 * num2
# div = num1 / num2

# print("%d + %d = %d" % (num1, num2, sum_))
# print("%d - %d = %d" % (num1, num2, minus))
# print("%d * %d = %d" % (num1, num2, mul))
# print("%d / %d = %.1f" % (num1, num2, div))

# python = 100
# print("파이썬 %d점" % python)
# age = 27
# print("나는 %d살이다." % age)

# python = 62
# c = 72
# java =59
# total = python + c + java
# avg = total / 3
# print("total = %d\navg = %.2f" % (total, avg))

# all_station = 11
# time = 37
# one_station = time / all_station
# print("한 역을 지나는데 걸리는 시간: %.2f분" % one_station)

# # round()는 반올림 
# flt = 12457808123.56778945643287845
# print("round(flt):", round(flt))
# print("round(flt,-8):", round(flt,-8)) # - 사용하면 정수자리 반올림
# print("round(flt,8):", round(flt,8))


# #내가한거
# each_floor = 260
# floor = 14
# all_floor = 260 * 14 / 100
# print("%.3f" % all_floor)
# #선생님꺼
# avg = 260
# one_floor = 500.23
# total = avg * (14 - 1) + one_floor
# meter = total / 100
# print("건물의 총 높이:", round(meter,3),"m")

# ride = 11.27
# one_hour = 3600 # 60*60으로 표시하기 문제 그대로 표시하는 것이 중요
# all_hour = one_hour / ride
# all_m = all_hour * 100
# all_km = all_m / 1000
# print("전동 자전거로 1시간 동안 가는 거리:", round(all_km, 2), "km")

# flt = 123.123
# print("%.3f + %.3f = %.3f" % (flt, 321.321, flt+321.321))
# print(flt, "+", 321.321, "=", flt+321.321)

# ch1,ch2,ch3 = "파","2","썬"
# print("%c + %c + %c = %s" % (ch1, ch2, ch3, ch1+ch2+ch3))
# print(ch1, "+", ch2, "+", ch3, "=", ch1+ch2+ch3)

# str_1 = "python"
# str_2 = "test"
# str_3 = str_1 + str_2
# print("%s + %s = %s" % (str_1, str_2, str_3))
# print(str_1, "+", str_2, "=", str_3)

# # 자료형 + 자료형
# 자료형: 숫자 정수 실수 단일문자 문자열 리스트 튜플
# 숫자-숫자, 문자-문자, 리스트-리스트, 튜플-튜플 만 + 연산 가능, 자료형이 서로 틀리면 연산 불가능
# print("a" + 1) 에러남

# A = 10
# B = 5
# print("type:", type(A<B))
# print("type:", (A<B))
# num = 100
# print("type: %s" % type(num))
# flt = 321.321
# print("type: %s" % type(flt))
# ch = "A"
# print("type: %s" % type(ch))
# st = "test"
# print("type: %s" % type(st))

# num = 100
# print("type: %s\tid: %s" % (type(num),id(num)))
# num = 321.321
# print("type: %s\tid: %s" % (type(num),id(num)))
# num = "A"
# print("type: %s\tid: %s" % (type(num),id(num)))
# num = "test"
# print("type: %s\tid: %s" % (type(num),id(num)))

# st1 = "python"
# st2 = "test"
# su = 100
# flt = 1.11
# num = '100'
# print(flt+su)
# print(st1 + st2)
# # print(su + num) TypeError뜸

# #강제 형변환, 1회성
# su = 100
# print("type(su): ",type(su))
# print("type(su): ",type(str(su)))
# print("type(su): ",type(float(su)))

# su = 100
# num = '100'
# flt = '1.111'

# print(su+int(num))
# print(float(num)+float(flt))
# print(str(su)+num)
# #print(int(flt)) value에러: 실수는 정수형으로 변경 불가능
# #print(int('one')) value에러: 문자열도 정수형으로 변경 불가능