mablagh = int(input("مبلغ خرید را وارد کنید: "))

if mablagh < 0:
    print("مبلغ وارد شده نامعتبر است")

elif mablagh > 2_000_000:
    hazine = 0
    print("هزینه ارسال: رایگان")
    print("مبلغ نهایی:", mablagh + hazine)

elif mablagh >= 1_000_000:
    hazine = 50_000
    print("هزینه ارسال:", hazine, "تومان")
    print("مبلغ نهایی:", mablagh + hazine)

else:
    hazine = 100_000
    print("هزینه ارسال:", hazine, "تومان")
    print("مبلغ نهایی:", mablagh + hazine)
