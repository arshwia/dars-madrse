import random
students = {}
def register():
    name = input("نام دانش آموز: ")
    code = random.randint(1000, 9999)
    while code in students: code = random.randint(1000, 9999)
    scores = []
    for i in range(3):
        while True:
            try:
                s = float(input(f"نمره درس {i+1}: "))
                if 0 <= s <= 20: scores.append(s); break
                print("نمره باید بین 0 تا 20 باشد")
            except ValueError: print("عدد معتبر وارد کنید")
    students[code] = {"name": name, "scores": scores}
    print("ثبت نام موفقیت آمیز بود. کد:", code)
def average(s):
    return sum(s) / len(s)
def report(code, student):
    avg = average(student["scores"])
    print(f"\nنام: {student['name']}\nکد: {code}\nنمرات: {student['scores']}\nمیانگین: {round(avg, 2)}")
    if avg < 10: print("وضعیت: مردود")
    elif avg >= 10: print("وضعیت: قبول خرداد")
def show_report():
    try: code = int(input("کد دانش آموزی: "))
    except ValueError: print("کد نامعتبر است"); return
    if code in students: report(code, students[code])
    else: print("دانش آموز پیدا نشد")
def best():
    if students:
        code, s = max(students.items(), key=lambda x: average(x[1]["scores"]))
        print("\nبهترین دانش آموز:")
        report(code, s)
    else: print("دانش آموزی ثبت نام نشده است")
def show_all():
    if students:
        for c, s in students.items(): report(c, s)
    else: print("لیست دانش آموزان خالی است")
def main():
    while True:
        print("\n1- ثبت نام\n2- مشاهده کارنامه\n3- بهترین دانش آموز\n4- نمایش همه\n5- خروج")
        try: choice = int(input("انتخاب کنید: "))
        except ValueError: print("عدد معتبر وارد کنید"); continue
        if choice == 1: register()
        elif choice == 2: show_report()
        elif choice == 3: best()
        elif choice == 4: show_all()
        elif choice == 5: print("خداحافظ!"); break
        else: print("گزینه نامعتبر است")
main()