## 문자열
# Str = 'Have a nice day'
# for i in range(len(Str)): # i가 인덱스가 됨
#     print(Str[i], end="") 
# print()
# for i in Str: #한꺼풀 벗겨내기 ,i 자체가 하나의 문자가 됨
#     print(i, end="")
# print()
# print("문자열의 총 길이:", len(Str))
# print("Str:", Str)


# Str = 'Have a nice day'
##print(Str[15]) # 인덱스 벗어나면 에러남
# arr = Str[7:11]
# print(Str)
# print(arr)

# Str = "즐거운 파이썬"
# print(Str)
# print(Str[0])
# print(Str[1:5])
# print(Str[3:])
# print(Str[:3])

# Str = "Have a"
# print(Str)
# print("_"*64)
# Str += " nice day"
# print(Str)
# print(Str*3)

#### 문자열 함수
## .upper():소문자를 대문자로 변경/ .lower():대문자를 소문자로 변경
## .swapcase(): 대소문자 상호 변경/ .title():각 단어의 첫번째 문자 대문자로 변경
# Str = 'Python is Easy. 그리고 programming 할만하다 ^^123'
# print(Str)
# print(Str.upper())
# print()
# print(Str.lower())
# print()
# print(Str.swapcase())
# print()
# print(Str.title()) # 각 단어의 첫번째 문자 대문자로 변경
# print()

#.title()은 첫글자를 대문자로 만들어줄뿐 아니라 나머지 글자는 소문자로 만들어줌
# 첫글자가 숫자나 특수기호, 한글일 경우 무시하고 영어 부분만 바꿔줌
# st = 'NevEr -eVer 110gIVe 업up'
# st=st.title()
# print(st)


# ## .count('찾는 문자or문자열')
# st = "Have a nice day"
# print(st)
# print()
# print("'a'개수:", st.count('a'))
# print("' '개수:", st.count(' '))
# print(st.count('')) #아무것도 안적으면 총 문자열 개수 알려줌/문자열은 끝을 알려주는null문자가 있기때문에 문자열개수+1된 값이 나옴
# print("'da'개수:", st.count('da'))
# print("'dad'개수:", st.count('dad'))

# st = "It is a fun Python class"
# a, s, All = 0, 0, 0
# for i in st:
#     All += 1
#     if i == 'a':
#         a += 1
#     elif i == 's':
#         s += 1
# print("총개수:", All)
# print("a 개수:", a)
# print("s 개수:", s)
# ## 이렇게 바로 변환할 수 있음
# print("총개수:", st.count("")-1)
# print("총개수:", len(st))
# print("a 개수:", st.count("a"))
# print("s 개수:", st.count("s"))


# ## .find('찾을 문자or문자열'): 첫글자의 위치 인덱스 반환/못찾으면 -1반환 .index()도 똑같으나 못찾으면 에러남
# st = "Have a nice day"
# print(st)
# print("find: 'day'위치:", st.find('day')) # 시작 인덱스의 위치값 출력
# print("index: 'day'위치:", st.index('day'))
# print("find: 'kkk'위치:", st.find('kkk'))
# # print("index: 'kkk'위치:", st.index('kkk'))

# st = "Have a nice day"
# print(st)
# print("find: 'a'위치:", st.find('a')) #첫번째께 찾아짐
# print("find: 'a'위치:", st.find('a',2)) # 2번 인덱스 이후부터 찾아줘
# print("find: 'a'위치:", st.find('a',6)) # 6번 인덱스 이후부터 찾아줘
# print("find: 'a'위치:", st.find('a',20)) # 에러는 안남

# # a의 총 개수와 첨자의 위치를 출력 하시오
st = "Have a nice day Have a nice day Have a nice day"
# 결과: [1,5,13,17,21,29,33,37,45]
# while .find()로 -1 이 될때까지
Set = set({})
flag = True
i = 0
while flag:
    num_a = st.find('a', i)
    if num_a != -1:
        Set.add(num_a)
    elif num_a == -1:
        break
    i += 1
ls = list(Set)
ls.sort()
print("a 위치:", ls)
print("a 개수:", len(Set))