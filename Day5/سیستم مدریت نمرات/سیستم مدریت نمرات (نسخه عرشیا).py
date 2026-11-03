import random
import statistics

students = {}


def register_student():
    name = input("نام دانش آموز: ")

    id_code = random.randint(1000, 9999)

    while id_code in students:
        id_code = random.randint(1000, 9999)

    scores = []

    for i in range(3):
        while True:
            try:
                score = float(input(f"نمره درس {i + 1} را وارد کنید: "))

                if 0 <= score <= 20:
                    scores.append(score)
                    break
                else:
                    print("نمره باید بین 0 تا 20 باشد")

            except ValueError:
                print("لطفاً یک عدد معتبر وارد کنید")

    students[id_code] = {"id_code": id_code, "name": name, "scores": scores}

    print("\nثبت نام با موفقیت انجام شد")
    print(f"کد دانش آموز: {id_code}")


def calculate_average(scores):
    return statistics.mean(scores)


def show_report():
    try:
        code = int(input("کد دانش آموزی را وارد کنید: "))
    except ValueError:
        print("کد دانش آموزی نامعتبر است")
        return

    if code not in students:
        print("دانش آموزی با این کد پیدا نشد")
        return

    student = students[code]

    average = calculate_average(student["scores"])

    print("\n------- کارنامه دانش آموز -------")
    print(f"نام: {student['name']}")
    print(f"نمرات: {student['scores']}")
    print(f"میانگین نمرات: {round(average, 2)}")

    if average >= 10:
        print("وضعیت: قبول خرداد")
    else:
        print("وضعیت: مردود")


def show_best_student():
    if not students:
        print("هنوز دانش آموزی ثبت نام نشده است")
        return

    best_code = None
    best_average = -1

    for code, student in students.items():
        average = calculate_average(student["scores"])

        if average > best_average:
            best_average = average
            best_code = code

    best = students[best_code]

    print("\n------- بهترین دانش آموز -------")
    print(f"نام: {best['name']}")
    print(f"کد دانش آموزی: {best_code}")
    print(f"نمرات: {best['scores']}")
    print(f"میانگین: {round(best_average, 2)}")


def show_all_students():
    if not students:
        print("لیست دانش آموزان خالی است")
        return

    for code, student in students.items():
        average = calculate_average(student["scores"])

        print("\n------- کارنامه دانش آموز -------")
        print(f"نام: {student['name']}")
        print(f"کد دانش آموزی: {code}")
        print(f"نمرات: {student['scores']}")
        print(f"میانگین: {round(average, 2)}")


def main():

    while True:
        print("\n\n\n------- سیستم مدیریت نمرات -------")
        print("1- ثبت نام دانش آموز")
        print("2- مشاهده کارنامه")
        print("3- بهترین دانش آموز")
        print("4- نمایش تمام دانش آموزان")
        print("5- خروج")

        try:
            choice = int(input("\nیکی را انتخاب کن: "))
        except ValueError:
            print("لطفاً یک عدد معتبر وارد کنید")
            continue

        if choice == 1:
            register_student()

        elif choice == 2:
            show_report()

        elif choice == 3:
            show_best_student()

        elif choice == 4:
            show_all_students()

        elif choice == 5:
            print("خروج از برنامه. خداحافظ!")
            break

        else:
            print("گزینه وارد شده نامعتبر است")


main()
