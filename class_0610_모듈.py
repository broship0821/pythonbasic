# import math
# ## math. 으로 출처를 밝혀야됨
# print(math.pi) # 파이
# print(math.factorial(5)) # 5*4*3*2*1
# print(math.sqrt(5)) # 루트
# print(math.log10(2)) # 로그

# from math import factorial, sqrt, pi
# # 이렇게 가져오면 math. 안 붙여도 됨
# print(pi)
# print(factorial(5))
# print(sqrt(5))
# # print(log10(2)) 로그는 import 안했기 때문에 에러남

# 이렇게 사용하면 어떤건 .math 안붙여서 사용 가능하고 나머진 .math로 사용 가능
# from math import factorial, sqrt, pi
# import math
# print(pi)
# print(factorial(5))
# print(sqrt(5))
# print(math.log10(2))
# print(math.log10(3))
# print(math.gcd(12,18)) # 최대공약수

# import statistics
# points = [65,75,55]
# print("평균:", statistics.mean(points))
# print("분산:", statistics.variance(points))
# print("표준편차:", statistics.stdev(points))
## as 를 사용해서 줄여서 사용 가능
# import statistics as st
# points = [65,75,55]
# print("평균:", st.mean(points))
# print("분산:", st.variance(points))
# print("표준편차:", st.stdev(points))
## 이렇게도 가능, 단 한번에 하나씩만 가능
# from statistics import mean as m
# # from statistics import mean, variance as m,v 이건 안됨
# points = [65,75,55]
# print("평균:", m(points))

## 이렇게 내 폴더 중 다른 파일에 있는 내용도 import 할수 있음
## 단 파일명 앞에 숫자가 있으면 안됨
# import calculator as cal
# from calculator import info
# print("1인치: %.2fcm" % cal.inch)
# print("1~10까지의 누적 합:", cal.calc_sum(10))
# info()
# info()
# info()

# import random

# for i in range(10):
    # print("%d번째:"%(i+1), random.random())
    # print("%d번째:"%(i+1), int(random.random()*10))
    # print("%d번째:"%(i+1), random.randrange(1,11))
