# 10~99사이의 난수 생성 (20이 나오면 중단)

from time_check import time_check
import random
n=int(input("난수의 개수를 입력하시오 > "))

for _ in range(n):
    r = random.randint(10,99)
    print(r,end=' ')
    if r ==20:
        print("The End")
        break
else:
    print("Error")
time_check()