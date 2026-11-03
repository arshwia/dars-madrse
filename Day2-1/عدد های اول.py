# برنامه ای بنویسید که یک عدد صحیح از ورودی دریافت کند و اعداد اول تا ان عدد را چاپ کند
number = int(input("enter a number(int): "))

for j in range(1, number + 1):
    cont = 0
    for i in range(1, number + 1):
        if (j % i) == 0:
            cont = cont + 1

    if cont == 2:
        print(j)
