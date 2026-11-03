import random
import statistics

students = {}


def register_student():
    name = str(input("نام دانش اموز:\t"))
    id_code = random.randint(1000, 9999)

    scores = []
    for i in range(3):
        score = float(input(f"نمره درس {i + 1} را وارد کنید\t"))
        if score < 0 or score > 20:
            print("نمره بین 0 تا 20 نیست")
            return
        scores.append(score)

    students[id_code] = {"id_code": id_code, "name": name, "scores": scores}

    print("ثبت نام با موفقیت انجام شد")
    print(f"کد دانش اموز {id_code}")


def calculate_average(scores):
    return statistics.mean(scores)


def show_report():
    code = int(input("کد دانش اموزی رو وارد کنید\n"))

    if not code in students["id_code"]:
        print("id code not defind")
        return

    student = students[code]
    average = calculate_average(scores)

    print("\n-------کار نامه دانش اموز-------")
    print(
        f"name {student['name']}\nنمرات: {student['scores']}\nمیانگین نمرات:{round(average, 2)}"
    )

    if average >= 10:
        print("قبول خرداد")
    else:
        print("مردود")


def show_best_student():
    if not students:
        print("هنوز دانش اموز ثبت نام نشده است")
        return

    best_code = None
    best_average = -1

    for code, student in students.items():
        average = calculate_average(student["scores"])

        if average > best_average:
            best_average = average
            best_code = code

        best = students[best_code]

        print("\n-------بهترین دانش اموز-------")
        print(
            f"name {best['name']}\nنمرات: {best['scores']}\nمیانگین نمرات:{round(average, 2)}"
        )


def show_all_students():
    if not students:
        print("لیست دانش اموزان خالی است")
        return

    for code, student in students.items():
        average = calculate_average(student["scores"])

        print("\n-------کار نامه دانش اموز-------")
        print(f"نام : {student['name']} نمرات: {code} میانگین {round(average)}")


def main():
    print("\n-------سیستم مدریت نمرات-------")
    print("1- ثبت نام دانش اموز")
    print("2- مشاهده کار نامه")
    print("3- بهترین دانش اموز")
    print("4- نمایش تمام دانش اموزان")
    print("exit\n\n\n")

    choice = int(input("یکی رو انتخاب کن "))

    if choice == 1:
        register_student()

    elif choice == 2:
        show_report()

    elif choice == 3:
        show_best_student()

    elif choice == 4:
        show_all_students()

    elif choice == 5:
        print("seeU")

    else:
        print("گزینه وارد شده نامعتبر است")


main()
