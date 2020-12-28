#1부터 100까지의 id값 차이 보기

for i in range(1,101):
    print(f'i={i:3} id(i)={id(i)}')
    
    # 32씩 차이남
    #int 형 = 4bytes 즉 32bit