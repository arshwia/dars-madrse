# numbers = []

# for i in range(10):
#     number = int(input("Enter a number: "))
#     numbers.append(number)

# zoj = []
# fard = []
# for number in numbers:
#     if number % 2 == 0:
#         zoj.append(number)
#     else:
#         fard.append(number)

# print("Smallest:", min(numbers))
# print("Largest:", max(numbers))

# print(f"zoj : {zoj}\nfard {fard}")

number=int(input("please enter number 1 :"))
even=0
odd=0
largest=number
smalest=number
if number%2==0:
    even=even+1
else:
    odd=odd+1

for i in range(2,11):
    number=int(input("please enter number "+str(i)+" :"))
    if number>largest:
        largest=number
    if number<smalest:
        smalest=number
    if number%2==0:
        even=even+1
    else:
        odd=odd+1

print("largest number is:",largest)
print("smalest number is:",smalest)
print("even number is:",even)
print("odd number is:",odd)