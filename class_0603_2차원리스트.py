# aa = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(aa[0])
# print(aa[1])
# print(aa[2])

# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# for i in range(len(aa)):
#     for j in range(len(aa[i])):
#         print("[%d][%d]"%(i,j), aa[i][j])
#다른방법
# for i in aa: #한꺼풀씩 벗겨낸다고 생각, aa->aa[i]->j 2차원배열->1차원배열->변수
    # for j in i:
    #     print(j)

#얕은복사
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# a = aa[0]
# a[1] = 20000
# print("[0]:", aa[0])
# print(a)
# print(aa[0])
#깊은복사
# import copy
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# # a = aa[0][:]
# a = copy.deepcopy(aa[0])
# a[1] = 20000
# print("[0]:", aa[0])
# print(a)
# print(aa)



### 이 부분 반복 보기
# ls_1 = []
# ls_2 = []
# value = 1
# for a in range(3):
#     for i in range(4):
#         ls_1.append(value)
#         value += 1
#     ls_2.append(ls_1)
#     ls_1=[]
# print(ls_2)
# for m in ls_2:
#     for n in m:
#         print(n, end="\t")
#     print()




# be = ['2019','12','31']
# print(be)
# af = list(map(int,be)) # be라는 리스트에 차례대로 진행함
# print(af)

# be = [
#     ['100'],
#     ['200'],
#     ['300']
# ]
# print('수정:', be)
# for i in range(len(be)):
#     be[i] = list(map(int,be[i]))
# print(be)
# for i in range(len(be)):
#     be[i][0] = str(be[i][0]*100)
# print('수정후:', be)