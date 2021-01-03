#리스트로 원소 스캔 
#enumerate 

x = ['john','George','Paul','ringo']

for i,name in enumerate(x,1):
    print(f'{i}번째 = {name}')