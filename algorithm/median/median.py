import time
from input import inputvalue3
start = time.time() # 시작 시간 저장 (start)

def median(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

a,b,c = inputvalue3()
print('median : {}'.format(median(a,b,c)))
print("time :", time.time() - start) # 현재시간 - 시작시간 = 즉 실행시간