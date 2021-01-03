# 각 배열 원소의 최대값 구하기 (튜플,문자열,list)

from array_max import max_arr

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAS','FLAG']


print(f'{t}의 최대값은 {max_arr(t)}.')
print(f'{s}의 최대값은 {max_arr(s)}.')
print(f'{a}의 최대값은 {max_arr(a)}.')