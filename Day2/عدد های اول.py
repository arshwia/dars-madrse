number = int(input("enter a number(int): "))

cont = 0
for i in range(1, number + 1):
    if (number % i) == 0:
        cont = cont + 1

if cont == 2:
    print("this number prime")
else:
    print("this number not prime")
