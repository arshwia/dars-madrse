accounts = {}
transactions = []


def create_account():
    print("\n-----------eftetah hesab-----------")

    name = input("name saheb hesab: ")
    account_number = input("shomar hesab")

    if account_number in accounts:
        print("in shomareh hesab ghablan sabt shode")
        return

    try:
        balance = float(input("mojodi avaleh "))

        if balance < 0:
            print("mojodi nmitavanad manfi bashad")
            return

    except ValueError:
        print("megdar avaleh motabar nist")
        return

    accounts[account_number] = {"name": name, "balance": balance}

    print("status 200 | hesab ba movafgiat ejad shod")


def deposit():
    # shomare hesab
    number = input("shomare hesab: integer")

    if number not in accounts:
        print("hsab peda nashod")
        return

    try:
        amount = float(input("mablag varizi: "))

        if amount <= 0:
            print("mablag bayad bishtar az 0 bashad")
            return

    except ValueError:
        print("mablag na motabar astttttttttt")
        return

    accounts[number]["balance"] += amount

    transactions.append(f"variz {amount} be hesab {number}")

    print("variz ba movafgit angam shod")


def withdraw():
    number = input("shomare hesab: integer")

    if number not in accounts:
        print("hsab peda nashod")
        return

    try:
        amount = float(input("mablag bardasht: "))

        if amount <= 0:
            print("mablag bayad bishtar az 0 bashad")
            return
        
        if accounts[number]["balance"] < amount:
            print("mojodi na kafi")
            return

    except ValueError:
        print("mablag na motabar ast")
        return

    accounts[number]["balance"] -= amount

    transactions.append(f"bardasht {amount} be hesab {number}")

    print("bardasht ba movafgit angam shod")


def transfer():
    source = input("shomare hesab mabda")
    destination = input("shomare hesab magsad")

    if source not in accounts or destination not in accounts:
        print("yke az hesab ha vojod ndarad")
        return

    if source == destination:
        print("mabda ba bagsad nmishe eki bashe")
        return

    try:
        amount = float(input("mablag bardasht: "))

        if amount <= 0:
            print("mablag bayad bishtar az 0 bashad")
            return
    except ValueError:
        print("mablag na motabar ast")
        return

    if accounts[source]["balance"] < amount:
        print("mojodi na kafi")
        return

    accounts[source]["balance"] -= amount
    accounts[destination]["balance"] += amount

    transactions.append(f"variz {amount} az {source} be {destination}")

    print("antgal vage anjam shod")


def show_balanc():
    number = input("shomare hesab: ")

    if number not in accounts:
        print("hesab peyda nashod")
        return

    print("name:", accounts[number]["name"])
    print("mojodi:", accounts[number]["balance"])


def show_all_acc():
    if not accounts:
        print("hich hsabi sabt nshode ast")
        return

    print("\n-------fehrst hsab ha-------")

    for number, info in accounts.items():
        print("\n-------")

        print("shomre hesab", number)
        print("name", info["name"])
        print("mojodi", info["balance"])


def show_transactions():
    if not transactions:
        print("hech trakonshe anjam nashede")

    print("--------gozarsh takonsh ha--------")

    for i, transaction in enumerate(transactions, start=1):
        print(i, "_", transaction)


def main():
    while True:
        print(
            "\n---------- SYSTEM MODIRIAT BANK ----------\n"
            "1. افتتاح حساب\n"
            "2. واریز وجه\n"
            "3. برداشت وجه\n"
            "4. انتقال وجه\n"
            "5. مشاهده موجودی\n"
            "6. نمایش حساب ها\n"
            "7. گزارش تراکنش ها\n"
            "8. خروج از برنامه"
        )

        try:
            num = int(input("لطفا گزینه مورد نظر را انتخاب کنید: "))
        except ValueError:
            print("لطفا فقط عدد وارد کنید!")
            continue

        if num == 1:
            create_account()

        elif num == 2:
            deposit()

        elif num == 3:
            withdraw()

        elif num == 4:
            transfer()

        elif num == 5:
            show_balanc()

        elif num == 6:
            show_all_acc()

        elif num == 7:
            show_transactions()

        elif num == 8:
            print("از برنامه خارج شدید.")
            break

        else:
            print("گزینه وارد شده معتبر نیست!")
            

main()
