import numpy
def make_lotto(count):
    for i in range(count):
    lotto_num = [] # 로또 번호가 담길 리스트형 변수

    for j in range(6): # 6번 반복
        lotto_num = numpy.random.choice(range(1,46),6,replace=False)
        
    lotto_num.sort() # 값 정렬
    print("{}. 로또번호: {}".format(i+1, lotto_num))


count = int(input("로또 번호를 몇개 생성할까요?> "))
make_lotto(count)

