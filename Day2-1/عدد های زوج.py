# برنامه ای بنویسید که یک عدد صحیح از ورودی دریافت کند و اعداد زوج تا ان عدد را چاپ کند 
number = int(input("enter a number(int): "))

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)