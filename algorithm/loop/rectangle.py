#직사각형의 넓이로 변 구하기 ( 약수 구하기 )

from time_check import time_check

area = int(input("직사각형의 넓이를 구하시오 >> "))
for i in range(1, area + 1): #1부터 계산
    if i * i > area: break
    if area % i: continue
    print(f'{i} x {area // i}')
time_check()