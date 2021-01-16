import hashlib # hashlib은 SHA 함수들이 들어있는 라이브러리다.

data = 'test'.encode()
hash_object = hashlib.sha1() # sha1은 해쉬값의 크기를 160으로 고정하는 알고리즘
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
#SHA, Secure Hash Algorithm 은 어떤 데이터도 고정된 크기의 유일한 값으로 리턴해주기 떄문에 보안에서 많이 사용된다.
data2 = 'hello world'.encode()
hash_object2 = hashlib.sha256()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)

#sha1, sha256