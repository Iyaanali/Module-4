numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(result)
print(list(result))

nums = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, nums)
print(result)
print(list(result))

def add(n):
    return n*n
squares = map(add, nums)
print(list(squares))