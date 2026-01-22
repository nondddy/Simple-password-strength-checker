def check_password():
    password = input("Enter password: ")
    length = len(password)

    if length < 6:
        strength = "Weak"
    elif length < 10:
        strength = "Medium"
    else:
        strength = "Strong"

    print("Password strength:", strength)

def main():
    while True:
        print("1. Check Password Strength")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_password()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
