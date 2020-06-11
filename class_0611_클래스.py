# result1 = 0
# def add1(n):
#     global result1
#     result1 += n
# def sub1(n):
#     global result1
#     result1 -= n
# result2 = 0
# def add2(n):
#     global result2
#     result2 += n
# def sub2(n):
#     global result2
#     result2 -= n
# add1(8)
# add1(19)
# sub2(15)
# print("1번 계산기 계산 결과: %d" % result1)
# print("2번 계산기 계산 결과: %d" % result2)

## 클래스명은 일반적으로 앞글자 대문자 표시
# class Claculator:
#     result = 0 # 클래스 내부 초기화
#     def add(self,n): # self:클래스 내부에서 자체적으로 쓰이는 형식
#         self.result += n
#     def sub(self,n):
#         self.result -= n
# cal1 = Claculator() # cal1 이라는 개체 생성
# cal2 = Claculator()
# cal3 = Claculator()
# cal1.add(19)
# cal1.sub(5)
# cal3.add(56)
# cal3.sub(26)
# print("1번 계산기 계산 결과: %d" % cal1.result)
# print("2번 계산기 계산 결과: %d" % cal2.result)
# print("3번 계산기 계산 결과: %d" % cal3.result)
# ## 각자의 계산기가 서로 영향 없이 실행됨
# print(type(cal1), type(cal2), type(cal3)) # __main__ 면 현재 디렉토리에서 실행시킨거임
# ls = []
# print(type(ls)) # 리스트, 튜플, 딕셔너리도 다 클래스로 저장됨

# class Person:
#     name = "Hong Kil Dong"
#     gender = "male"
#     address = "seoul"
#     def set_name(self,name):
#         self.name = name
#     def print(self):
#         print("My name is {0}".format(self.name))
# p1 = Person()
# p2 = Person()
# p1.name = "홍길동"
# print("p1's name is", p1.name)
# print("p2's name is", p2.name)
# p1.set_name('peter')
# print(p1.print())
# print(p2.print())
# print("p1's name is", p1.name)

### 생성자
# class Account:
#     def __init__(self,bank): # Account의 생성자
#         self.balance = 0
#         self.bank = bank
#     def get_balance(self):
#         return self.balance
#     def deposit(self,money):
#         self.balance += money
#     def withdraw(self,money):
#         self.balance -= money
# if __name__ == '__main__': # 지금 사용하는게 현재 모듈에 있는지 확인
#     woori = Account('우리은행')
#     woori.deposit(15000)
#     print("%s 잔액: %d원"%(woori.bank,woori.get_balance()))

## 상속
# class Player: # 부모 클래스
#     def __init__(self,user_id):
#         self.user_id = user_id
#         self.level = 1
#         self.hp = 50
#         self.atk = 3
#         self.exp = 0
#     def info(self):
#         print('\n========캐릭터 정보========')
#         print("아이디:", self.user_id)
#         print("레벨:", self.level)
#         print("공격력:", self.atk)
#         print("경험치:", self.exp)
#         print("체력:", self.hp)
#         print("===========================")
# if __name__ == "__main__":
#     class Healer(Player): # 자식 클래스 힐러에다가 부모클래스 Player를 상속
#         def heal(self):
#             pass
#     class Tanker(Player):
#         def tank(self):
#             pass
#     P1 = Healer('아처')
#     P2 = Tanker('워리어')
#     P1.info()
#     P2.info()
# else:
#     class Healer(Player):
#         def heal(self):
#             pass
#     class Tanker(Player):
#         def tank(self):
#             pass
#     P1 = Healer('archer')
#     P2 = Tanker('worrior')
#     P1.info()
#     P2.info()