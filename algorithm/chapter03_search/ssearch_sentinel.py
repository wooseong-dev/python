# 선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq : Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형검색함 (보초법으로)"""
    a = copy.deepcopy(seq) # seq를 깊은 복사
    a.append(key)          # 보초 key를 추가
    
    i = 0
    while True:
        if a[i] == key:
            break # 검색에 성공하면 while문 종료
        i +=1
    return -1 if i == len(seq) else i

if __name__ == '__main__' :
    num = int(input('원소 수를 입력하시오 >> ')) # num 값을 입력받는다.
    x = [None] * num                         # 원소 수가 num인 배열을 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] >> ')) 
        
    key = int(input('검색할 값을 입력 >> ')) # 검색할 key 값 입력하기
    
    idx = seq_search(x, key)              # key값과 같은 원소를 x 에서 검색
    
    if idx == -1:
        print('원소가 존재하지 않음')
    else:
        print(f'검색값은 x[{idx}]에 위치')