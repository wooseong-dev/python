# +와 -를 번갈아가며 n 회 출력
from time_check import time_check
n = int(input("몇 개를 출력할지 입력 >> "))

for i in range(n):
    if i%2:
        print('-',end='')
    else:
        print('+',end='')
        


print()
time_check()

# 문제점1 : for 반복시마다 if문 수행
# 문제점2 : 상황에 따른 유연한 수정 불가능