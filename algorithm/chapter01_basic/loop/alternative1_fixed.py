# alternative1.py 보완
# +와 -를 번갈아 n 회 출력
from time_check import time_check
n=int(input("출력할 횟수 n 을 입력하시오 >> "))

for _ in range(n//2):
    print('+-',end='')
if n%2:
    print('+',end='')
print()    
time_check()

# 무시하고 싶은 값은 _(언더스코어) 로 처리 후 인덱스를 사용하지 않을 수 있음.