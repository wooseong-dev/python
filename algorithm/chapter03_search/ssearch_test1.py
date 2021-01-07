# seq_search() 함수를 사용하여 실수 검색하기

from ssearch_while import seq_search

print('End 입력 시 종료')

number = 0
x = [] # 빈 리스트 x 생성

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s)) # 배열 맨 끝에 원소를 추가
    number += 1
key = float(input('검색할 값을 입력하시오 >> ')) # 검색할 key 입력

idx = seq_search(x, key) # key와 값이 같은 원소를 list x 에서 검색
if idx == -1:
    print('원소가 존재하지 않는다.')
else:
    print(f'검색값은 x[{idx}]에 존재.')