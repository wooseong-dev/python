# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색 """
    fir=0          # 검색 범위 맨 앞 원소의 인덱스
    las = len(a) - 1# 검색 범위 맨 끝 원소의 인덱스
    
    while True:
        mid_idx = (fir + las)//2 # 중앙 인덱스를 구하기 위해 
        
        if a[mid_idx] == key:
            return mid_idx
        elif a[mid_idx] < key:
            fir = las + 1 # 검색 범위를 뒤쪽 절반으로
        else:
            las = mid_idx -1 # 검색 범위를 앞쪽 절반으로
        if fir > las:
            break
        return -1 # 검색 실패
    
    
if __name__ == "__main__":
    num = int(input('원소 수를 입력하시오 >> '))
    x = [None] * num
    print('오름차순으로 배열값 입력 ')
    x[0] = int(input('x[0] >> '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] >> '))
            if x[i] >= x[i-1]:
                break
    ky = int(input('검색할 값을 입력 >> '))
    
    idx = bin_search(x, ky)
    
    if idx == -1:
        print('검색값이 존재하지 않음')
        
    else:
        print(f'검색값은 x[{idx}]에 위치')