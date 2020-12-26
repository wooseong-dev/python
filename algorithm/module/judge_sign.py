def judge_sign(n):
    n=int(input('판정할 수를 입력하시오 >>'))

    if n<0: print('n은 음수')
    elif n>0: print('n은 양수')
    else: print('n은 0')
    
    