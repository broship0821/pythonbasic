# #반복문for0528
# for i in range(5):
#     print("상위포문 %d 일때 하위포문:" % i, end="  ")
#     for j in range(5):
#         print(j*i, end=" ")
#     print()

# #반복문for0528
# for i in range(1, 22, 5):
#     print(i, end="\t")
#     for j in range(1, 5):
#         print(i+j, end="\t")
#     print()

class Player: # 부모 클래스
    def __init__(self,user_id):
        self.user_id = user_id
        self.level = 1
        self.hp = 50
        self.atk = 3
        self.exp = 0
    def info(self):
        print('\n========캐릭터 정보========')
        print("아이디:", self.user_id)
        print("레벨:", self.level)
        print("공격력:", self.atk)
        print("경험치:", self.exp)
        print("체력:", self.hp)
        print("===========================")