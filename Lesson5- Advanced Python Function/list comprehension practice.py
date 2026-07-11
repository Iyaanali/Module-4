# Input from the user
num = int(input("Enter a number: "))

# List of odd numbers
odd_numbers = [i for i in range(1, num) if i % 2 != 0]

# List of even numbers
even_numbers = [i for i in range(1, num) if i % 2 == 0]

# Display the lists
print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)