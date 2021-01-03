#mutable(변환가능자료형) 원소를 역순 정렬
 
from typing import Any, MutableSequence
def reverse_arr(a: MutableSequence) -> None:
    #mutable 시퀀스 a의 원소 역순 정렬
    n = len(a)
    for i in range(n//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        
if __name__ == '__main__':
    nx = int(input('원소의 개수를 입력하시오 >> '))
    x = [None]*nx #원소수 nx개의 list 생성
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]의 값을 입력하시오 >> '))
    
    reverse_arr(x)
    
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')