fruits = ["banana", "apple", "orange", "banana", "apple", "banana"]

frequency = {}

for fruit in fruits:
    if fruit in frequency:
        frequency[fruit] += 1
    else:
        frequency[fruit] = 1

print(frequency)