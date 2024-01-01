import os


def main():
    count = 0
    print("\t\t\tFacebook")
    print("\t\t\t--------")
    print("1.Sign up\n2.Log in")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        sign_up()
    else:
        count = login(count)
        if count == 3:
            print("Your account has been blocked due to three unsuccessful attempts!!!")
            return


def sign_up():
    user = input("Email or phone number:")
    password = input("Enter your password:")

    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input("Enter your password again:")

    file = open("info.txt", "w")
    file.write(user)
    file.write(" ")
    file.write(password)
    file.close()

    print("Signed up successfully!")


def login(count):
    user = input("Email or phone number:")
    password = input("Enter your password:")

    file = open("info.txt", "r")
    if os.stat("info.txt").st_size == 0:
        print("\nThere is no account.Please sign up first.")
        return
    data = file.read()
    space_index = data.index(" ")
    correct_user = data[:space_index]
    file.seek(space_index + 1)
    correct_pass = file.read()

    file.close()

    if user == correct_user and password == correct_pass:
        print("Log in successful!")
        return count
    else:
        print("\nWrong user email or password!\nPlease try again\n")
        count += 1
        if count < 3:
            count = login(count)
        return count


if __name__ == "__main__":
    main()
