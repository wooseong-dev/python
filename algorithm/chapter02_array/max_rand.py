#배열 원소의 최댓값을 구한 후 출력(원소값을 난수로 생성)

import random
from array_max import max_arr

num = int(input("난수의 개수를 입력하시오 >> "))
lo = int(input("난수의 최소값을 구하시오 >> "))
hi = int(input('난수의 최대값을 구하시오 >> '))

x = [None] * num #원소수가 num인 리스트 생성

for i in range(num):
    x[i] = random.randint(lo,hi) #lo 이상 hi 이하

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_arr(x)}입니다.')