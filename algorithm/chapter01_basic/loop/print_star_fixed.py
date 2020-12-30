# *을 n회 출력 l마다 줄바꿈
# print_star는 반복마다 if문 수행 비효율

from time_check import time_check
n=int(input("*을 몇회 출력 >> "))
l=int(input("몇 마다 줄바꿈 >> "))

for _ in range(n//l): # 반복수행
    print('*' * l)
    
rest = n% l

if rest: # 조건 판단 1회
    print('*'*rest)
time_check()