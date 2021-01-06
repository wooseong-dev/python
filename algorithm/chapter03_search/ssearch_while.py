# while문으로 작성된 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a:Sequence, key: Any) -> int:
        """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
        i=0
        
        while True:
            if i ==len(a):
                return -1 # 끝에 도달하면(검색 실패) -1 리턴
            if a[i] == key:
                return i # 검색에 성공하면 index 반환
            i+=1
if __name__ == "__main__":
    num = int(input('원소의 개수를 입력하시오 >> '))
    x = [None]*num # 개수가 num인 list x 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] >> ')) # 배열에 원소 집어넣기
    
    key = int(input('검색할 값을 입력하시오 >> ')) # 검색할 값 입력하기
    
    idx = seq_search(x, key) # 배열 x에서 key값 검색
    
    if idx == -1:
        print('검색한 값이 배열 x 에 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 위치')
    