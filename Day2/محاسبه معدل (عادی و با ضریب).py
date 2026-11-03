# نمره های هر درس را از کاربر میگیرم
ryazi = int(input("nomre ryazi(input number): "))
farsi = int(input("nomre farsi(input number): "))
web = int(input("nomre web(input number): "))

# محاسبه معدل عادی
avarge = (ryazi + farsi + web) / 3
print(avarge)

# محاسبه نمره با ضریب
ryazi = ryazi * 2
web = web * 4

# محاسبه معدل با ضریب
print((web + ryazi + farsi) / 7)

