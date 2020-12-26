import time
from input import inputvalue3
start = time.time() # 시작 시간 저장 (start)

def median(a,b,c):
    if (b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif(a>b and c<b) or (a<b and c>b):
        return b
    return c

a,b,c = inputvalue3()
print('median : {}'.format(median(a,b,c)))
print("time :", time.time() - start) # 현재시간 - 시작시간 = 즉 실행시간