# برنامه ای بنویسید که ده عدد صحیح را از ورودی بگیره و کوچیک ترین و بزرگ ترین رو در خروجی نمایش بده 
numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Smallest:", min(numbers))
print("Largest:", max(numbers))

# برنامه ای بنویسید که ده عدد صحیح یا اعشاری را از ورودی دریافت کند و معدل رو حساب کنه 
numbers = [12, 15.5, 18, 10, 17.25, 14, 19, 16.5, 11, 20]

average = sum(numbers) / len(numbers)

print("Average:", average)