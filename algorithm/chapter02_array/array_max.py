#배열 원소들 중 최댓값 구하는 함수 구현

from typing import Any,Sequence

def max_arr(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum=a[i]
    return maximum

if __name__ == "__main__":
    num = int(input("원소 수를 입력하시오 >> "))
    x = [None] * num # 원소 수가 num 인 list 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] 값을 입력하시오 >> '))
    print(f'최대값은 {max_arr(x)} 이다.')