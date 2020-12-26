from time_check import time_check
print("1부터 n 까지의 정수의 합을 구하시오.")
n = int(input("n의 값을 입력하시오 >> "))

sum=0
i=1

while i<=n:
    sum+=i
    i+=1
print(f'{sum}')
time_check()