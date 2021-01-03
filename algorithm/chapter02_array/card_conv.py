# 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기

def card_conv(x:int, r:int) -> str:
    #정수값 x를 r진수로 변환 후 그 수의 문자열을 반환
    
    d='' # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while x>0:
        d+=dchar[x%r] # 해당 문자 꺼내서 결합
        x //=r
        
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

'''
x = 5
r = 10
#x//=r
print(f'{x}')'''