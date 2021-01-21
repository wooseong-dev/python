'''import hashlib
h = hashlib.sha256()
h.update(b'clone')
print(h.hexdigest())'''

'''
from hashlib import sha256

prev_hash = b'What is this'
for _ in range(3):
    print(prev_hash.hex())'''

'''
#선형검색 알고리즘인데 시발 이게 뭐지

def seq_search(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return 1
    return -1

n=int(input('n >> '))

a =[None]*n
for i in range(n):
    a[i] = int(input('원소의 값 >>'))
    
key=int(input('key >> '))

print(key)

val = seq_search(a,key)

if val == 1:
    print(f'Success {key}값은 {a[val]} 번째에 있습니다.')
else:
    print('False')'''

import hashlib
n = hashlib.sha256()
n.update(b'please help me')
print(n.hexdigest())


