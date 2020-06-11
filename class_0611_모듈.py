## 가위 바위 보
# import random
# while True:
#     user = int(input("1. 가위 2. 바위 3. 보 4. 게임 종료\n입력:"))
#     com = random.randrange(1,4)
#     if user == 1:
#         if com == 1:
#             print("나: 가위, 컴퓨터: 가위, 결과: 비김\n")
#         elif com == 2:
#             print("나: 가위, 컴퓨터: 바위, 결과: 짐\n")
#         elif com == 3:
#             print("나: 가위, 컴퓨터: 보, 결과: 이김\n")
#     elif user == 2:
#         if com == 2:
#             print("나: 바위, 컴퓨터: 바위, 결과: 비김\n")
#         elif com == 3:
#             print("나: 바위, 컴퓨터: 보, 결과: 짐\n")
#         elif com == 1:
#             print("나: 바위, 컴퓨터: 가위, 결과: 이김\n")
#     elif user == 3:
#         if com == 3:
#             print("나: 보, 컴퓨터: 보, 결과: 비김\n")
#         elif com == 1:
#             print("나: 보, 컴퓨터: 가위, 결과: 짐\n")
#         elif com == 2:
#             print("나: 보, 컴퓨터: 바위, 결과: 이김\n")
#     elif user == 4:
#         print("게임을 종료합니다")
#         break
#     else:
#         print("잘못 입력하셨습니다\n")
## 선생님 방법 평범한거
# import random
# print("=== 가위 바위 보 게임 ===")
# sel = int(input("0. 가위    1. 바위     2. 보\n>>>>"))
# com = random.randrange(0,3)
# menu = ['가위','바위','보']
# print("User:", menu[sel], "Computer:", menu[com])
# if sel == com:
#     print("비김")
# elif (sel==0 and com==2) or (sel==1 and com==0) or (sel==2 and com1):
#     print("승리")
# else:
#     print("패배")

# import random
# def game_start():
#     print("=== 가위 바위 보 게임 ===")
#     sel = int(input("0. 가위    1. 바위     2. 보\n>>>>"))
#     com = random.randrange(0,3)
#     menu = ['가위','바위','보']
#     print("User:", menu[sel], "Computer:", menu[com])
#     if sel == com:
#         print("비김")
#     elif com-sel == -1 or com-sel==2:
#         print("승리")
#     else:
#         print("패배")
# while True:
#     game_start()
#     Next = int(input("continue: 1 / 종료: 2\n>>>>"))
#     print()
#     if Next == 2:
#         break
#     else:
#         continue


## 로또 프로그램 만들기
# import random
# lotto_ls = []
# while True:
#     lotto = random.randrange(1,46)
#     if lotto not in lotto_ls:
#         lotto_ls.append(lotto)
#     if len(lotto_ls) == 6:
#         break
# print("로또 추천 번호:", lotto_ls)
## 선생님꺼
# import random
# def lotto_data():
#     lotto = []
#     print("=== 로또 추천 번호 ===")
#     while True:
#         num = random.randrange(1,46)
#         if lotto.count(num) == 0:
#             lotto.append(num)
#         if len(lotto) == 6:
#             break
#     print("추천번호:", end='')
#     for i in range(len(lotto)):
#         print("%d" % lotto[i], end='   ')
#     print()
# while True:
#     lotto_data()
#     Next = int(input("continue: 1 / 종료: 2\n>>>>"))
#     print()
#     if Next == 2:
#         break
#     else:
#         continue