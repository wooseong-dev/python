#List Comprehension basic
numbers = [1,2,3,4,5]
cloth = [num * 2 for num in numbers if num % 2 == 1]
print(cloth)