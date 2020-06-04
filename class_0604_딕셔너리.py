#딕셔너리
# 인덱스 없음, 키 값으로 대체
# impo = {}
# impo["파이썬"] = "www.python.org" #impo[0]이 아니라 impo['key']로 구분
# impo["네이버"] = "www.naver.com"
# impo["구글"] = "www.google.com"
# print("파이썬:", impo["파이썬"])
# print("네이버:", impo["네이버"])
# print("구글:", impo["구글"])
# print(impo)

# impo = {}
# name = input("키값 입력:")
# val = input("값 입력:")
# impo[name] = val
# print(name, ":", impo[name])
# print(impo)

# impo = {}
# for i in range(5):
#     name = input("이름 입력:")
#     val = input("값 입력:")
#     impo[name] = val # name=q, val=w면 impo[q] = w 라고 저장됨 만약 키값을 똑같은거 입력하면 수정만됨
# print(impo)
#참조 (파이썬 이전 버전에선 딕셔너리 순서가 없었음, 순서대로 할려면 밑에내용으로 해야했었음)
# import collections
# #순서있는 사전
# overWatch = collections.OrderedDict()
# # i=0
# # name=""
# # val=""
# for i in range(5):
#     name = input("이름(key) 입력:")
#     val = input("값(value) 입력:")
#     overWatch[name] = val
# print(overWatch)

#딕셔너리 함수

# .keys(),.values(): 키랑 값을 리스트로 추출해줌
# num = {1:'일', 2:'이', 3:'삼', 4:'사'}
# print('keys()키:', num.keys())
# print()
# print('values()값:', num.values())
#하지만 정확한 리스트형이 아님, 형 변환을 해줘야됨
# num = {1:'일', 2:'이', 3:'삼', 4:'사'}
# print('num.keys()키:', num.keys())
# print('list(num)', list(num)) # 그냥 list()는 키값만 추출하는것이 기본값, value는 추출 안함
# print('list(num.keys())', list(num.keys()))
# print()
# print('num.values()값:', num.values())
# print('list(num.values())', list(num.values()))

# singer = {}
# singer['이름'] = input("가수 이름 입력:")
# singer['구성원'] = input("인원수 입력:")
# singer['대표곡'] = input("대표곡 입력:")
# print(singer)
# for i in singer.keys(): #딕셔너리를 순서대로 출력하는 방법
#     print("%s : %s" % (i,singer[i]))

#1,3번 메뉴가 기능이 똑같음, 둘다 추가, 갱신 가능한 버그
# menu = {}
# bl = True
# num = 0
# while bl:
#     print("1.메뉴 등록")
#     print("2.메뉴 가격 보기")
#     print("3.가격 수정")
#     print("4.종료")
#     num = int(input(">>> "))
#     if num == 1:
#         name = input("메뉴 입력:")
#         menu[name] = input("가격 입력:")
#     elif num == 2:
#         if menu == {}:
#             print("메뉴없음")
#         for i in menu.keys():
#             print(i, ":", menu[i])
#     elif num == 3:
#         name = input("수정할 메뉴 입력:")
#         menu[name] = input("수정 가격:")
#     elif num == 4:
#         print("프로그램 종료")
#         bl = False
#     else:
#         print("잘못 입력, 1~4 입력")

# num = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오'}
# print(num)
# print("num.get(3):", num.get(3))
# print("num.get(9):", num.get(9))
# print("num.get(0):", num.get(0, '없음')) # key가 없으면 None으로 출력, 그때 ,"없음" 이라고 치면 반환값 바꿈(문자열, 숫자, 불형 등 다 됨)
# su = int(input("찾고자하는 키 입력:"))
# if num.get(su) == None:
#     print("값이 없습니다")
# else:
#     print(num.get(su))

# menu = {}
# bl = True
# while bl:
#     print("1.메뉴 등록")
#     print("2.메뉴 가격 보기")
#     print("3.가격 수정")
#     print("4.종료")
#     num = int(input(">>> "))
#     if num == 1:
#         name = input("메뉴 입력:")
#         if menu.get(name) == None:
#             menu[name] = input("가격 입력:")
#         else:
#             print("이미 존재하는 메뉴입니다")
#     elif num == 2:
#         if menu == {}:
#             print("메뉴없음")
#         for i in menu.keys():
#             print(i, ":", menu[i], "원")
#     elif num == 3:
#         name = input("수정할 메뉴 입력:")
#         if menu.get(name) == None:
#             print("존재하지 않는 메뉴입니다")
#         else:
#             menu[name] = input("수정 가격:")
#     elif num == 4:
#         print("프로그램 종료")
#         bl = False
#     else:
#         print("잘못 입력, 1~4 입력")
#     print()


## .items() 딕셔너리의 key, value를 리스트로 반환
# student = {'학번':1234, '이름':'홍길동', '학과':'it학과'}
# print(student['학번'])
# print(student['이름'])
# print(student['학과'])
# print()
# print(student.items())
# print(list(student.items()))
# print()
# print(list(student)) # 이거는 key 값만 반환

# name = {'이순신':'거북선', '세종대왕':'훈민정음', '파이썬':'프로그래밍언어'}
# print(name.items()) #각각 튜플로 담아서 리스트에 담음
# for key, value in name.items(): #언패킹을 통해 key, value에 각각 담음
#     print(key, ":", value)
#     print(type(key), type(value))
### .clear() 삭제
# print("삭제:", name.clear())
# print("삭제 후 값:", name)


### .setdefault() 없으면 추가, 있으면 무시(수정안됨)
# num = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오'}
# print("변경 전 값:", num)
# print()
# print("num.setdefault(5):", num.setdefault(5, "구~우")) # 있으면 수정되지 않고 무시됨, 없으면 추가
# print("num.setdefault(9):", num.setdefault(9, "구~우"))
# print()
# print("변경 후:", num)
# print()
# print("num의 9번째 value:", num.get(9))



### .update(dic) 딕셔너리 합치기/ +연산이 안되서 update만 합치기 가능
# num = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오'}
# aaa = {6:'육', 7:'칠', 8:'팔'}
# print("update 전 num:", num)
# num.update(aaa)
# print("update 후 num:", num)
# bbb = {}
# # bbb = num + aaa # 딕셔너리는 + 연산 안됨
# print(bbb)


### .fromkeys(ls) ls리스트(튜플)의 있는 값을 받아서 딕셔너리의 키값으로 대입
## 리스트
# dic = {}
# ls = []
# ls.append(input("등록할 키값 입력:"))
# ls.append(input("등록할 키값 입력:"))
# ls.append(input("등록할 키값 입력:"))
# print(ls)
# dic = dic.fromkeys(ls)
# print("dic키 설정:", dic)
# dic = dic.fromkeys(ls,0)
# print("dic키&값 설정:", dic)
## 튜플
# dic = {}
# tp = ('날짜', '재고', '출고')
# print(tp)
# dic = dic.fromkeys(tp)
# print("dic키 설정:", dic)
# dic = dic.fromkeys(tp,0)
# print("dic키&값 설정:", dic)

### .pop() ()안에 쓴 키를 찾아서 빼내고 원래 딕셔너리에서 삭제
# num = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오'}
# print("pop 전 num:", num)
# print("pop(3) 실행:", num.pop(3))
# #print("pop(3) 실행:", num.pop()) #리스트는 이러면 맨 마지막께 삭제, 딕셔너리는 순서가 없으므로 에러
# #print("pop(3) 실행:", num.pop(6)) #없으면 에러
# print("pop(3) 실행 후:", num)

info = {}
pe = []
bl = True
while bl:
    # pe.clear() 이런 방식 혹은
    print("1. 인적사항 등록\n2. 검색\n3. 종료")
    num = int(input(">>> "))
    if num == 1:
        pe.append(input("이름 입력:"))
        pe.append(input("점수 입력:"))
        info[pe[0]] = pe[1]
        # pe = [] 이런 방식으로 계속 초기화를 해줘야됨
    elif num == 2:
        name = input("찾고자 하는 학생이름 입력:")
        if info.get(name) == None:
            print("해당 학생의 데이터가 존재하지 않습니다")
        else:
            print(name, "의 점수:", info.get(name))
    elif num == 3:
        print("프로그램 종료")
        bl = False
    else:
        print("1~3사이 숫자 입력")