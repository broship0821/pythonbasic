# 바뀌지 않거나 적은 규모의 것들은 튜플로 만드는게 좋음

# tp = (10,20,30) # tp = 10,20,30 괄호 생략 가능
# print("tp:", tp)
# print("tp type:", type(tp))
# print("tp len:", len(tp))

# tp1 = 10,20,30
# print("tp1:", tp1)
# print("tp1 type:", type(tp1))
# print("tp[0] type:", type(tp1[0]))
# # tp1[0] = 1000000 # 에러발생

# tpType = "문자열",100,1.111
# print("tpType:",tpType)
# print("tpType type:", type(tpType))
# print("tpType[0] type:", type(tpType[0]))
# print("tpType[1] type:", type(tpType[1]))
# print("tpType[2] type:", type(tpType[2]))


#튜플은 괄호 생략 가능, 단, 하나의 항목만 가진 튜플을 만들때는 주의
# tpInt = (10)
# print("ptInt:", type(tpInt))
# print(tpInt)
# tpTuple1 = (10,) #하나의 항목만 가지고 있는 튜플은 , 표시를 해줘야 튜플이 됨, 안해주면 int
# print(tpTuple1)
# print("tpTuple1:", type(tpTuple1))
# tpTuple2 = 10,
# print("tpTuple2", type(tpTuple2))

#이런건 리스트랑 똑같음
# tt1 = 10,20,30,40
# tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3]
# print("튜플 합:", tt2)
# print("tt1[1:3]:", tt1[1:3])
# print("tt1[1:]:", tt1[1:])
# print("tt1[:3]:", tt1[:3])

# a = 1,2,3
# b = 4,5,6
# c = a + b
# d = a * 3
# print(a)
# print(b)
# print(c)
# print(d)
# a = a + b # a에 담는거 되는데..?
# print(a)


##### 튜틀에서 가장 중요 #####
# ## packing & unpacking
# pack = 1,2,"패킹"
# print("packing\npack:", pack)
# #언패킹을 통해 튜플을 변경할 수 있음
# a,b,c = pack #언패킹할때는 변수랑 튜플의 수랑 정확히 맞아야됨
# a = 100000000
# print("unpacking\na:", a, "b:", b, "c:", c)
# 패킹을 통해서만 변경이 되고 언패킹할때 변수를 튜플수 만큼 생성해야되니
# 항목이 적고 변경 가능성이 적은 것들만 튜플로 만듬, 나머지는 리스트나 딕셔너리


# 튜플 함수 index, count
# tp = 100, 200, '함수', 100, '개수'
# print("tp안의 200 위치:", tp.index(200), "번째 인덱스")
# print("tp안의 100 개수:", tp.count(100), "개")

# tp = "회사정보", "제품명", "가격정보", "출시일"
# ls = ["삼성전자", "겔럭시", "100원", "미정"]
# print(tp[0], "    :", ls[0])
# print(tp[1], "      :", ls[1])
# print(tp[2], "    :", ls[2])
# print(tp[3], "      :", ls[3])
# for i in range(len(tp)):
#     print("%5s\t"%tp[i], ":", ls[i])
# for i in range(len(tp)):
#     print("{}\t:{:<5}".format(tp[i],ls[i]))
# for i in range(len(tp)):
#     print("{1}\t:{0:<5}".format(tp[i],ls[i]))
# for i in range(len(tp)):
#     print("{}\t:{:=^10}".format(tp[i],ls[i]))