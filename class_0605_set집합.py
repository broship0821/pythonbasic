# set 집합 {}
# list-index/dic-key로 첨자가 있었는데 set은 첨자가 없음 - 중복불가
# 저장속도는 빠르나 검색은 반복하여 찾아야됨 / 자료 수집에 몰빵
# 집합은 여러 값들의 모임, 저장순서 보장안되고 중복값을 허용하지않음
# 딕셔너리처럼 {}로 쓰나 key,value값이 지정되어있지 않음

#print할때마다 순서가 바뀜
# names = {'허준', '신사임당', '권율', '홍길동', '허준                 ', 212, 'ㅅㅅㅅ'}
# print(type(names)) #class 'set'
# print(len(names)) #집합의 개수 (7, 중복제거, 공백만 있어도 다른 문자로 표시)
# print(names) #중복되어 있는 값은 있어도 오류는 나지 않지만 하나만 표시

# s = {}
# print(type(s)) #그냥 {}면 dic으로 인지함
# s = set({}) #set 자료형 초기화 방법
# print(type(s))
# #순서없이 중복제거하여 출력됨
# print(set('progr               ammmmmming')) #공백도 하나의 문자로 인지
# print(set('asdfdasf''qwerqwer')) # 이렇게 하나의 문자열이면 가능
# print(set('asdfdasf','qwerqwer')) # ,로 2개로 구분지으면 에러남
# print(set([12,14,16,25,11,15, 12]))
# dic = {'a':1, 'b':2, 'c':3}
# print(set(dic)) # key값만 set으로 가져옴
# print(set({'a':1, 'b':2, 'c':3}))

# 순서 전혀 없음 매 출력마다 결과 바뀜
# for i in {'가','나','다','라'}:
#     print(i)

### set 조작함수
## .add(추가할 값): 순서없이 추가되기 때문에 .append랑 다름
# asia = {'korea', 'china', 'japan'}
# print(asia)
# asia.add('north_korea')
# print(asia)
# asia.add('china') #이미 있는 값은 추가 안됨, 공백이나 _를 써서 다른값을 만들어줘야됨
# print(asia)
# ## .remove(삭제할 값): 인덱스가 없기 때문에 .del()은 사용할수없음
# ## .del(삭제할 인덱스 위치), .remove(삭제할 값)
# asia.remove('japan')
# print(asia)

## .update(추가할 집합)
# asia = {'korea', 'china', 'japan'}
# print(asia)
# asia2 = {'iraq', 'singapore', 'korea'}
# asia.update(asia2)
# print(asia)
# print("-"*40)
# asia = {'korea', 'china', 'japan'}
# asia2 = {'iraq', 'singapore', 'korea'}
# #asia3 = asia + asia2 # +연산 사용 불가능
# #print(asia3)

# set 집합의 연산
# 1. 합집합(|): 두 집합의 전체 요소들의 모음
# 2. 교집합(&): 두 집합의 공통 요소들의 모음
# 3. 차집합(-): 왼쪽 집합의 요소에서 오른쪽 집합의 요소를 제거
# 4. 배타적 차집합(^): 합집합 - 교집합
# 5. 부분집합(<=): 왼쪽 집합이 오른쪽 집합의 부분집합인지의 여부를 확인
# 6. 진성 부분집합(<): 부분집합이면서 추가로 요소가 더 존재하는지 확인
# 부분집합과 진성부분집합의 차이는:
#     부분집합(<=) 경우는 좌우 집합이 같아도 부분집합이다
#     진성부분집합(<)은 좌우 집합이 모두 같을 경우 성립되지 않는다
# asia = {'korea', 'china', 'japan'}
# asia2 = {'iraq', 'singapore', 'korea'}
# print(asia|asia2)
# print(asia&asia2)
# print(asia-asia2)
# print(asia^asia2)
# asia3 = {'korea', 'china', 'japan', 'north_korea'}
# print(asia<=asia3)
# print(asia<asia3)
# asia4 = {'korea', 'china', 'japan', 'north_korea'}
# print(asia4<=asia3)
# print(asia4<asia3)

# two = {2,4,6,8,10,12}
# three = {3,6,9,12,15}
# print("교집합:", two & three) #6 12
# print("합집합:", two | three) #2,3,4,6,8,9,10,12,15
# print("차집합:", two - three) #2,4,8,10
# print("배타적 차집합:", two ^ three) #2,3,4,8,9,10,15

# animal = {'호랑이','사자','강아지','치타','햄스터','고양이'}
# pet = {'강아지','고양이','햄스터'}
# print(pet<=animal)
# print(pet<=pet)
# print(pet<animal)
# print(pet<pet)