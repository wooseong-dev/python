#최댓값 구하는 알고리즘
import time
start = time.time() # 시작 시간 저장 (start)
print('세 정수의 최대값을 구한다')

a=int(input('정수 a의 값을 입력하세요 : '))
b=int(input('정수 b의 값을 입력하세요 : '))
c=int(input('정수 c의 값을 입력하세요 : '))

maximum=a
if b > maximum: maximum = b
if c > maximum: maximum = c
    
print('최댓값은 {}입니다.'.format(maximum))
print("time :", time.time() - start) # 현재시간 - 시작시간 = 즉 실행시간
#선택구조

