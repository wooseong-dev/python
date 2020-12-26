def pibo(n):
    result, num=0,1
    for i in range(n):
        result,num=num,result+num
    return result

i=0
for i in range(i,10):
    print(pibo(i))

