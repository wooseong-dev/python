# a부터 b 까지의 합 구하기
from time_check import time_check 
a,b= input("a와 b의 값을 입력하시오 >> (구분:공백)").split()
          
a=int(a)
b=int(b)
if a>b:
    a,b=b,a # a와 b를 오름차순으로 정렬

sum=0
for i in range(a,b+1):
    sum+=i

print(f"{a}부터 {b} 까지의 총합은 {sum} 입니다.")
time_check()