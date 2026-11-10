import random
students = {}
def register():
    name = input("نام دانش آموز: ")
    code = random.choice([i for i in range(1000, 10000) if i not in students])
    scores = []
    for i in range(3):
        while True:
            try:
                s = float(input(f"نمره درس {i+1}: "))
                if 0 <= s <= 20: scores.append(s); break
                print("نمره باید بین 0 تا 20 باشد")
            except ValueError: print("عدد معتبر وارد کنید")
    students[code] = dict(name=name, scores=scores)
    print("ثبت نام موفق! کد:", code)
avg = lambda s: sum(s)/len(s)
def report(c, s):
    a = avg(s["scores"])
    print(f"\nنام: {s['name']}\nکد: {c}\nنمرات: {s['scores']}\nمیانگین: {a:.2f}\nوضعیت: {'قبول خرداد' if a >= 10 else 'مردود'}")
def show(code=None):
    if not students: print("دانش آموزی ثبت نام نشده است"); return
    if code is not None:
        if code in students: report(code, students[code])
        else: print("دانش آموز پیدا نشد")
    else: 
        for c, s in students.items(): report(c, s)
def main():
    while True:
        print("\n1- ثبت نام\n2- کارنامه\n3- بهترین دانش آموز\n4- نمایش همه\n5- خروج")
        try: c = int(input("انتخاب: "))
        except ValueError: print("عدد معتبر وارد کنید"); continue
        if c == 1: register()
        elif c == 2:
            try: show(int(input("کد دانش آموزی: ")))
            except ValueError: print("کد نامعتبر است")
        elif c == 3:
            if students:
                code, s = max(students.items(), key=lambda x: avg(x[1]["scores"]))
                print("بهترین دانش آموز:")
                report(code, s)
            else: print("دانش آموزی ثبت نام نشده است")
        elif c == 4: show()
        elif c == 5: print("خداحافظ!"); break
        else: print("گزینه نامعتبر است")
main()