#두 자리의 양수 입력받기

while True:
    n = int(input('값을 입력하시오 >> '))
    if n >=10 and n <=99: # 비교 연산자 연속 사용
        break

print(f'입력받은 양수는 {n}입니다.')