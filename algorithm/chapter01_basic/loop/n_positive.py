# 1부터 n 까지의 합 구하기 (n은 양수여야 함)

from time_check import time_check

while True:
    n=int(input("n의 값을 입력하시오 >> "))
    if n>0:
        break # n이 음수일 때 break
sum=0
i=1

for i in range(1, n+1):
    sum+=i
    i+=1

print(f'1부터 {n}까지 정수의 합은 {sum}이다.')
time_check()