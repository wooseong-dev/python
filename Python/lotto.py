'''
#random 함수 이용
import random

cnt=int(input("원하는 로또 생성 횟수를 입력하시오 >> "))

for i in range(0,cnt):
    lotto_rand=[]
    for j in range(0,6):
        a=random.randint(0,46)
        lotto_rand.append(a)
    print(lotto_rand)
'''


#numpy사용

import numpy #numpy 임포트

cnt = int(input("원하는 로또 생성 횟수를 입력하시오 >> ")) #cnt 로또 생성횟수

for i in range(0,cnt):
    lotto_number=[] #로또 번호를 담을 빈 리스트 생성
    lotto_number=numpy.random.choice(range(0,46),6,replace=False) #(0~46)까지의 숫자중 랜덤으로 6자리 난수 생성 중복미허용
    lotto_number.sort() # 정렬
    print(lotto_number) # 출력





