#flag 변수는 상반된 걸로 전환시키는 용도로 쓰임/True-False, +- 등
# i = 0
# flag = True
# while flag:
#     print(i, "종속 문장", end=" ")
#     if i == 10:
#         flag = False
#     i+=1

## break, continue
# while 조건식:
#     while 조건식:
#         break #전체가 아닌 종속 조건문에서만 빠져나옴

# i = 0
# while True:
#     if i == 3:
#         break
#         print("3 출력") #break 하위는 생략됨
#     print(i, "출력")
#     i+=1
# print("다음 문장")

# i = 0
# while i < 5:
#     i+=1
#     if i == 3:
#         continue
#         print("3 출력") #continue 하위는 생략됨
#     print(i, "촐력")
# print("다음 문장")

# for i in range(1,6,1):
#     if i == 3:
#         continue
#         print("3 출력")
#     print(i, "출력")
# print("다음 문장")

# else 버그 고치기
# num, result, i = 0, 0, 1
# while True:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     break
# # else:
# print("next..")
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)
#flag로 고치기
# num, result, i = 0, 0, 1
# flag = True
# while flag:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     else:
#         flag = False
# else:
#     print("next..")
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)
#break 위에 넣어주는 방법
# num, result, i = 0, 0, 1
# while True:
#     num = int(input("1~10 사이의 숫자 입력:"))
#     if num < 1 or num > 10:
#         print("잘못 입력, 다시입력")
#         continue
#     print("next..")
#     break
# while i <= num:
#     result += i
#     i += 1
# else:
#     print("1~", num, "까지의 합:", result)

# result = 0
# while True:
#     num = int(input("10~20사이의 숫자 입력:"))
#     if num < 10 or num > 20:
#         print("잘못된 숫자 입력, 다시 입력")
#         continue
#     break
# print("next..")
# for i in range(num+1):
#     result += i
# print("1~", num, "까지의 합:", result)

# for i in range(0,3,1):
#     for k in range(0,5,1):
#         if k == 3:
#             break
#         print("(i: %d\tk: %d)" % (i, k))
# print()
# #위에꺼 while문으로 바꾸기
# i = 0
# while i < 3:
#     k = 0
#     while k < 5:
#         if k == 3:
#             break
#         print("(i: %d\tk: %d)" % (i, k))
#         k += 1
#     i+=1

#####첫번째 시도######
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한마리가 하루에
# 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 며칠만에
# 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
# (쌀 한통 = 1kg, 쌀을 먹은 후 2배 증가하는 조건)
# 총 10만그람 쌀
# rice = 100000
# eat_oneday = 20
# mouse = 2
# day = 1

# eat_sum = rice - (mouse * eat_oneday) * day
# while eat_sum >= 0:
#     if day % 10 == 0:
#         mouse = mouse * 2
#     eat_sum = rice - (mouse * eat_oneday) * day
#     day += 1
# print("{}번째날 남은 쌀: {:,}".format(day-1, eat_sum))
# print("%d번째 모두 쥐의 먹이가 됨" % (day-1))
# print("총 쥐 마리: %d" % mouse)

# eat_sum = rice - (mouse * eat_oneday) * day
# print("총 쌀: {:,}".format(eat_sum))
# # print("남은 쌀: {:,}".format(eat_sum))
# while eat_sum >= 0:
#     if day % 10 == 0:
#         mouse = mouse * 2
#     eat_sum = rice - (mouse * eat_oneday) * day
#     day += 1
# print("{}번째날 남은 쌀: {:,}".format(day, eat_sum))
# print("%d번째 모두 쥐의 먹이가 됨" % day)
# print("총 쥐 마리: %d" % mouse)


#####두번째 시도######
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한마리가 하루에
# 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 며칠만에
# 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
# (쌀 한통 = 1kg, 쌀을 먹은 후 2배 증가하는 조건)
# 총 10만그람 쌀

# print("1번째", rice - (2 * eat_oneday) * 1)
# print("9번째", rice - (2 * eat_oneday) * 9)
# print("10번째", rice - (2 * eat_oneday) * 9 - (4 * eat_oneday) * 1)
# print("19번째", rice - (2 * eat_oneday) * 9 - (4 * eat_oneday) * 9)
# print("20번째", rice - (2 * eat_oneday) * 9 - (4 * eat_oneday) * 9 - (8 * eat_oneday) * 1)
# print()
# rice = 100000
# eat_oneday = 20
# mouse = 2
# day = 1
# eat_today = (mouse * eat_oneday)
# eat_total = 0
# left_rice = rice - eat_total
# # while left_rice >= 0:

# #0~9번째날
# for j in range(0, 10):
#     eat_total = 2 * eat_oneday * j
#     print(eat_total)

# # 10~ 11번째날
# for i in range(1, 11)
# eat_total = eat_total + 4 * eat_oneday * i
# left_rice = rice - eat_total
# print("남은쌀:", left_rice)
# print()


# #0~9번째날
# day_nine = 2 * 20 * 9
# print(day_nine)
# # 10~ 19번째날
# eat = day_nine + 4 * 20 * 10
# print(eat)
# # 20~ 29번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10
# print(eat)
# # 30~ 39번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10 + 16 * 20 * 10
# print(eat)
# # 40~ 49번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10 + 16 * 20 * 10 + 32 * 20 * 10
# print(eat)
# # 50~ 59번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10 + 16 * 20 * 10 + 32 * 20 * 10 + 64 * 20 * 10
# print(eat)
# # 60~ 69번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10 + 16 * 20 * 10 + 32 * 20 * 10 + 64 * 20 * 10 + 128 * 20 * 10
# print(eat)
# # 70~ 79번째날
# eat = day_nine + 4 * 20 * 10 + 8 * 20 * 10 + 16 * 20 * 10 + 32 * 20 * 10 + 64 * 20 * 10 + 128 * 20 * 10 + 256 * 20 * 10
# print(eat)

    

#####세번째 시도######
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 쥐 한마리가 하루에
# 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 며칠만에
# 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇마리 인가?
# (쌀 한통 = 1kg, 쌀을 먹은 후 2배 증가하는 조건)
# eat_all = - 2 * 20
# day = 0
# mouse = 2
# every_tenday = 1
# flag = True
# while flag:
#     while day < 10 * every_tenday:
#         eat_all = eat_all + mouse * 20 
#         # print("{}번째날 먹은양: {:,}".format(day, eat_all))
#         rice = 100000 - eat_all
#         if rice <= 0:
#             flag = False
#             break
#         day += 1
#     mouse = mouse * 2
#     every_tenday += 1
# print("다 먹는데 걸리는 시간: %d일, 총 쥐 마리수: %d마리" % (day, mouse/2))
# #답은 맞는데 너무 복잡함, 아래가 정답
# mouse = 2 
# rice = 100000          # 단위 : 그램(gram) 
# day = 1 
# while True: 
#     rice = rice - (mouse * 20) 
#     if rice <= 0: 
#         break 
#     day = day + 1
#     if (day % 10) == 0: 
#         mouse = mouse * 2 
# print(day, "일", mouse, "마리") 


######숙제2
# print("------------------------")
# money = int(input("요금을 투입하세요\n>"))
# while True:
#     print("------------------------")
#     print("========커피 자판기========")
#     print("1. 커피(200)\t2. 코코아(150)\t3. 반환\t4. 종료")
#     menu = int(input("메뉴를 선택하세요\n>"))
#     if menu == 1:
#         if money >= 200:
#             money = money - 200
#             print("커피 나왔습니다. 잔돈은 %d원 입니다." % (money))
#         else:
#             print("돈이 부족합니다.")
#             extra_money = int(input("요금을 더투입하세요\n>"))
#             money = money + extra_money
#     elif menu == 2:
#         if money >= 150:
#             money = money - 150
#             print("코코아 나왔습니다. 잔돈은 %d원 입니다." % (money))
#         else:
#             print("돈이 부족합니다.")
#             extra_money = int(input("요금을 더투입하세요\n>"))
#             money = money + extra_money
#     elif menu == 3:
#         money = money
#         print("잔돈을 반환합니다. 잔돈은 %d원 입니다." % money)
#         break
#     elif menu == 4:
#         break
#     else:
#         print("메뉴는 1~4 사이의 번호를 입력해야 합니다.")