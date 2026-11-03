# list
# numbers = []

# for i in range(10):
#     number = float(input("Enter a number: "))
#     numbers.append(number)

# average = sum(numbers) / len(numbers)
# print("Average:", average)

# no list
total = 0

for i in range(10):
    grade = float(input(f"please enter grade {str(i + 1)}: "))
    total += grade

average = total / 10

print("Average:", average)
