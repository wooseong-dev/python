# 객체 식별번호 출력
#함수 내부, 외부

n=1
def put_id():
    x=1
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()