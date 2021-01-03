def card_conv(x:int, r:int) -> str:
    #정수값 x를 r진수로 변환 후 그 수의 문자열을 반환
    
    d='' # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n=len(str(x))
    
    print(f'{r:2} | {x:{n}d}')
    while x>0:
        print('    +' + (n+2)*'-')
        if x//r:
            print(f'{r:2} | {x // r:{n}d}  {x%r}')
        else:
            print(f'     {x // r:{n}d}   {x%r}')
        d += dchar[x%r]
        x//=r

        
    return d[::-1] # 역순으로 변환


if __name__ == "__main__":
    while True:
        while True: # 음이 아닌 정수를 입력받음
            no = int(input("변환할 값으로 음이 아닌 정수를 입력하시오 >> "))
            if no>0:
                break
        while True: # 2~36진수의 정숫값을 입력받음
            cd = int(input('어떤 진수로 변환할까요 >> '))
            if 2<= cd <= 36:
                break
        print(f'{cd}진수로 {card_conv(no, cd)}이다.')
        
        retry = input("한 번 더 변환 여부(y/n) >> ")
        if retry in {'N','n'}:
            break