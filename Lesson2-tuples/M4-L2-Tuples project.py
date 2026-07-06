# Two tuples
tuple1 = (2, 4, 6)
tuple2 = (3, 5, 7)

# Calculate the product of each tuple
product1 = 1
product2 = 1

for num in tuple1:
    product1 *= num

for num in tuple2:
    product2 *= num

# Display the results
print("Tuple 1:", tuple1)
print("Product of Tuple 1:", product1)

print("Tuple 2:", tuple2)
print("Product of Tuple 2:", product2)