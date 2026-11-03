saved_username = "arka"
saved_passworld = "arshia"
saved_role = "admin"

username = str(input("please enter username: "))
password = str(input("please enter password: "))
role = str(input("please enter your role: "))

if username == saved_username and password == saved_passworld:
    if role == "admin":
        print("welcome admin!")
    else:
        print(f"welcome {role}!")
else:
    print("try again...")
