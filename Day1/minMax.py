numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Smallest:", min(numbers))
print("Largest:", max(numbers))
