n = int(input("Enter the size of the square: "))

square = []  # List to store each row

for i in range(n):
    row = []
    for j in range(n):
        row.append("*")
    square.append(row)

# Print the square
for row in square:
    print(" ".join(row))