# *을 n개 출력 l마다 줄바꿈

from time_check import time_check

n=int(input("출력 횟수를 입력하시오 >> "))
l=int(input("줄 바꿈 제한을 입력하시오 >> "))

for i in range(n): # 반복 시마다 조건 판별
    print("*", end='')
    if i % l == l-1:
        print()
        
if n%l:
    print()