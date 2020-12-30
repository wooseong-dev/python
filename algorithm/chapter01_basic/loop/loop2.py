
import sys
#sys.path.append('/workspace/python/algorithm/module')
from time_check import time_check

n=int(input("n의 값을 입력하시오 >> "))
i=1
sum=0


for i in range(1,n+1):
    sum+=i
    

print(f'1부터 n 까지의 합은 {sum}입니다.')
time_check()