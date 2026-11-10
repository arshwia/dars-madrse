import random
import statistics

students = {}


def register_student():
    name = input("نام دانش آموز:")
    code = random.randint(1000, 9999)
    scores = []

    for i in range(3):
        score = float(input("نمره درس:"))
        if score < 0 or score > 20:
            print("نمره باید بین 0 تا 20 باشد")
            return
        scores.append(score)

    students[code] = {"name": name, "scores": scores}

    print("ثبت نام با موفقیت انجام شد")
    print("کد دانش آموز", code)


def calculate_average(scores):
    return statistics.mean(scores)


def show_report():
    code = int(input("لطفا کد دانش آموزی را وارد نمایید:"))

    if code not in students:
        print("دانش آموز یافت نشد")
        return

    student = students[code]
    average = calculate_average(student["scores"])

    print("")
    print("نام:", student["name"])
    print("نمرات", student["scores"])
    print("میانگین", round(average, 2))

    print(
        f"\n\n ----------کارنامه دانش آموز----------\nنام: {student['name']}\nنمرات: {student['scores']}\nمیانگین: {round(average,)}"
    )

    if average >= 10:
        print("وضعیت:قبول")
    else:
        print("وضعیت:مردود")


def show_best_student():
    if not students:
        print("هنوز دانش آموز ثبت نام نشده است")
        return
    best_code = None
    best_average = -1

    for code, student in students.items():
        average = calculate_average(student["scores"])

        if average > best_average:
            best_average = average
            best_code = code

    best = students[best_code]

    print("\n --------بهترین دانش آموز کلاس--------")
    print("نام:", best["name"])
    print("نمرات", best_code)
    print("میانگین", round(best_average, 2))


def show_all_students():
    if not students:
        print("لیست دانش آموزان خالی است")
        return
    for code, student in students.items():
        average = calculate_average(student["scores"])

        print("\n ----------------")
        print("نام:", student["name"])
        print("کد دانش آموز", code)
        print("میانگین", round(average, 2))


def main():
    while True:
        print("\n-------سیستم مدیریت نمرات-------")
        print("1- ثبت نام دانش آموز")
        print("2- مشاهده کارنامه")
        print("3- بهترین دانش آموز")
        print("4- نمایش همه دانش آموزان")
        print("5- خروج")

        choice = input("لطفا از منوی بالا یک گزینه را انتخاب فرمایید")

        if choice == "1":
            register_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            show_best_student()
        elif choice == "4":
            show_all_students()
        elif choice == "5":
            print("برنامه پایان یافت.")
            break
        else:
            print("گزینه وارد شده نامعتبر است")


main()
