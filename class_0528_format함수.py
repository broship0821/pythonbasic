## format
#숫자를 적으면 숫자 순서대로, 생략하면 정순으로
# print("{0} + {1} = {2}".format(10, 2, 10+2))
# print("{2} + {1} = {0}".format(10, 2, 10+2))
# print("{} + {} = {}".format(10, 2, 10+2))
# #천단위마다 , 표시
# print("{:,}".format(10000000000))
# #한글은 한글자로 읽힘
# print("{:<10}, 왼쪽ㅇ정렬, {:0<10}".format("첫번째", "두번째"))
# print("{:>10}, 오른쪽정렬, {:9>10}".format("첫번째", "두번째"))
# print("{:^10}, 가운데정렬, {:5^10}".format("첫번째", "두번째"))#짝수, 홀수 칸이 안맞으면 맨 끝에 한칸 생략해서 진행
