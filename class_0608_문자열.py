## 문자열 함수

## .strip('지우고 싶은 문자') 문자열의 양쪽부터 문자 제거, 미 입력시 공백 제거
# st = '      파 이 썬      '
# print('st\t\t:{}{}{}'.format('*',st,'*'))
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))
# print()
# st = '    !  파 이 썬        !       ' #제거하는게 연속적이여야됨 양쪽에서 제거해오다가 다른거 있음 중단
# print('st\t\t:{}{}{}'.format('*',st,'*'))
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))

# st = '파이썬파파파파파파파'
# print('st\t\t:', st)
# print()
# print('st.strip("파")\t:', st.strip('파')) # 꼭 대칭 아니여도 됨
# print()
# st = '파이썬'
# print('st\t\t:', st)
# print()
# print('st.strip("파")\t:', st.strip('파'))

# 이건 지우고 싶은 문자가 어느 위치인지 정확히 알고 있을때 사용
## .lstrip('지우고 싶은 문자') 문자열의 왼쪽부터 제거
## .rstrip('지우고 싶은 문자') 문자열의 오른쪽부터 제거
# st = '--------------------!-파---이---썬---!------------'
# print('st\t\t:', st)
# print('st.strip("-")\t:', st.strip('-'))
# print('st.rstrip("-")\t:', st.rstrip('-'))
# print('st.lstrip("-")\t:', st.lstrip('-'))


## .replace('A', 'B') 해당 문자열의 모든 A를 B로 바꾼다
# st = "2015/04/02"
# print('st\t\t\t:', st)
# print('st.replace("/",".")\t:', st.replace('/','.'))
# print('st.replace("/","-")\t:', st.replace('/','-'))
# print('st.replace("/","....")\t:', st.replace('/','....')) #문자길이가 달라도 상관없음
# print('st.replace("0","!")\t:', st.replace('0','!'))
# print('st.replace()\t\t:', st.replace('2015','2020'))
# print('st.replace([0:4])\t:', st.replace(st[0:4],'2020')) # []로 인덱스를 지정해서 바꿀수도 있음

## 많은 문자열 처리
# ## 사이에 "" 써도됨, """는 안됨
# st = """
# "오늘 하루도 즐겁게" 
# 오늘 하루도 행복하게
# 오늘 하루도 최선을
# """
# print(st, end="") ## """는 주석처리랑 햇갈릴수 있음 쓸때 확실하게 표현하기

# st = """
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# """
# print(st.replace('-',':').replace('2017','1999').replace('2015','1999').replace('2018','1999'))
# # st에 있는 '년'의 인덱스 위치 찾기
# i = 0
# ls = []
# while True:
#     i = st.find('년', i)
#     if i != -1:
#         ls.append(i)
#         i += 1
#     else:
#         break
# # 찾은 인덱스를 이용해서 년도 바꾸기
# for j in range(len(ls)):
#     st = st.replace(st[ls[j]-4:ls[j]],"1999")
# st = st.replace('-',':')
# print(st)
# #선생님방법
# st = """
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# """
# st = st.replace('-',':')
# cnt = 0
# while True:
#     cnt = st.find('년', cnt)
#     if cnt != -1:
#         st = st.replace(st[cnt-4:cnt],'1999')
#         cnt += 1
#     else:
#         break
# print(st)


# .split("A"): 문자열을 A기준으로 끊어서 리스트에 담아줌
# st = 'Never ever give up'
# print('st\t\t:', st)
# print('st.split()\t:', st.split()) # 아무것도 안적으면 공백 기준
# print('st.split()\t:', st.split('e')) # 'e'를 기준으로 끊어서 리스트에 담아줌
# print('st.split()\t:', st.split('!')) # 없는 문자 쓰면 전체 문자열을 담아줌

# st = '하나:둘:셋'
# print('st\t\t:', st)
# print('st.split(":")\t:', st.split(":"))
# st = '일,이,삼'
# print('st\t\t:', st)
# print('st.split(",")\t:', st.split(","))

## .splitlines(): \n기준으로 끊어서 리스트로 담아줌
# st = 'Never ever give up'
# print('st\t\t:', st)
# print('st.splitlines()\t:', st.splitlines())
# ## \n을 기준으로 앞쪽을 담음
# st = """
# Never ever give up
# Never ever give up
# Never ever give up
# """
# print('st\t\t:', st)
# print('st.splitlines()\t:', st.splitlines())

# st ="하나\n둘\n셋"
# print('st.splitlines()\t:', st.splitlines())


## .join(): 앞에있는 데이터를()안에있는 문자열 사이사이에 집어넣음/앞에있는 문자열을 ()사이에 집어넣음
# Str = " 123"
# print('"%".join(Str)\t\t:', "%".join(Str)) #앞에있는 데이터를()안에있는 문자열 사이사이에 집어넣음
# print('Str.join("%a")\t\t:', Str.join("%a")) #앞에있는 문자열을 ()사이에 집어넣음
# print('Str.join("%abc")\t:', Str.join("%abc"))
# #리스트는 내용 삽입 후 문자열로 반환
# li = ['','123','456']
# print('"공백".join([123,456])\t:'," ".join(li))
# li = ['','안녕하세요','만나서 반갑습니다','행복한 하루 되세요^^']
# print('"엔터".join(li)\t:',"\n\n".join(li))


## .center(숫자): 숫자만큼 칸 확보하고 가운데 정렬
# Str = 'python'
# print("Srt\t\t\t:", Str)
# print("Srt.center(10)\t\t:", Str.center(10))
# print("Srt.center(10,'-')\t:", Str.center(10,'-')) # 나머지칸 - 로 채움
# ## .ljust(숫자): 숫자만큼 칸 확보하고 왼쪽 정렬
# print("Srt.ljust(10)\t\t:", Str.ljust(10), Str.ljust(10))
# print("Srt.ljust(10,'-')\t:", Str.ljust(10,'-'), Str.ljust(10,'-'))
# ## .rjust(숫자): 숫자만큼 칸 확보하고 오른쪽 정렬
# print("Srt.rjust(10)\t\t:", Str.rjust(10), Str.rjust(10))
# print("Srt.rjust(10,'-')\t:", Str.rjust(10,'-'), Str.rjust(10,'-'))
# ## .zfill(숫자): 오른쪽 정렬하고 나머지 0으로 채움
# print("Srt.rjust(10,'0')\t:", Str.rjust(10,'0'))
# print("Srt.zfill(10)\t\t:", Str.zfill(10))


# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# accountBook = "shoes\t03/02\t$59000\ncoffee\t03/03\t$2500\nfood\t03/04\t$7000\ndress\t03/13\t$130000"
## 1. 모든 ", " \n으로 바꾸기
## 2. 모든 공백 \t로 바꾸기
# print(accountBook.replace(",","\n"))
# print(accountBook.split())
# 선생님꺼
# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# replaceAB = accountBook.split(',') # ,기준으로 리스트 저장
# # print(replaceAB)
# k = 0
# for i in replaceAB:
#     replaceAB[k] = i.strip() # 각 문자열의 왼쪽공백 삭제 후 저장
#     k += 1
# # print(replaceAB)
# ## 목록 만들기
# print('item'.ljust(10), end="")
# print('date'.ljust(10), end="")
# print('$(price)'.ljust(10))

# kk = "$ "
# for i in range(len(replaceAB)):
#     z = replaceAB[i].split() #공백을 기준으로 리스트 저장
#     # print(z)
#     for k in range(len(z)):
#         if k == 0:
#             print(z[k].ljust(10),end="") # 10칸 확보 후 왼쪽출력
#         elif k == 1:
#             print(z[k].ljust(10),end="") # 10칸 확보 후 왼쪽출력
#         elif k == 2:
#             print("{:,}".format(int(z[k])).join(kk).ljust(10))



# Str = "python te12st 1234"
# ## .isdigit()
# print(Str.isdigit()) # 숫자로만 구성인가?
# print(Str[9:11].isdigit()) # 인덱스 사용 가능
# ## .isalpha()
# print(Str.isalpha()) # 글자로만 구성인가?
# print(Str[:6].isalpha()) # 인덱스 사용 가능
# ## .isalnum()
# print(Str.isalnum()) # 글자 + 숫자 인가? ## 중간에 공백있어서 False
# print(Str[7:13].isalnum()) # 인덱스 사용 가능
# ## .islower(), .isupper(), .isspace()
# print(Str.islower()) # 소문자로만 구성되어 있나?
# print(Str.isupper()) # 대문자로만 구성되어 있나?
# print(Str.isspace()) # 공백으로만 구성되어 있나?