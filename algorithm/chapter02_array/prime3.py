# 1000이하의 소수 나열 ( 개선된 알고리즘 )

counter =0 # 나눗셈 횟수 카운트
ptr =0 # 이미 찾은 소수의 개수
prime =[None]*500 #소수 저장배열

prime[ptr] = 2 # 2는 소수이므로 초기값 지정
ptr+=1 

prime[ptr] =3
ptr += 1

for n in range(5, 1001, 2): #홀수만을 대상으로 설정
    i=1
    while prime[i] * prime[i] <= n:
        counter+=2
        if n % prime[i] ==0:
            break
        i+=1
    else:
        prime[ptr]=n
        ptr+=1
        counter +=1
        
for i in range(ptr): #ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수 >> {counter}')