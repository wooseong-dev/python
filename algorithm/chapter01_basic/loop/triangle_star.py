#*로 이등변 삼각형 출력하기

n=int(input("짧은 변의 길이를 입력하시오 >> "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()