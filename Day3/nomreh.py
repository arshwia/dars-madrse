name = input("enter your name: ")
grade = float(input("enter your grade: "))

if grade < 0 or grade > 20:
    print("نمره نا معتبر است")

elif grade >= 18:
    print(f"عالی {name}")


elif grade >= 15:
    print(f"خوب {name}")


elif grade >= 12:
    print(f"ضعیف {name}")


elif grade >= 10:
    print(f"مشروط {name}")

else:
    print(f"مردود {name}")
