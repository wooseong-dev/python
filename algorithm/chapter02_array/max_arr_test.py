#각 배열 원소의 최댓값 구해서 출력
# tuple, str, str list

from array_max import max_arr

t = (4,7,5.6,2,3.14,1)
s = 'string'
a=['DTS','AAC','FLAG']

print(f'{t}의 최대값은 {max_arr(t)}입니다.')
print(f'{s}의 최대값은 {max_arr(s)}입니다.')
print(f'{a}의 최대값은 {max_arr(a)}입니다.')