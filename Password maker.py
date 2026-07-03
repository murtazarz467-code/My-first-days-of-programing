import random
import string
import json
import os


def English_word(User_letter):

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&"

    if User_letter == "1":
        return random.choice(letters)

    elif User_letter == "2":
        return random.choice(digits)

    elif User_letter == "3":
        return random.choice(letters + digits + symbols)


def save_password(password_name, password, password_type):

    data = {
        "name": password_name,
        "password": password,
        "type": password_type
    }

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)

    except:
        passwords = []

    passwords.append(data)

    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)


def password_name_exists(password_name):

    if not os.path.exists("passwords.json"):
        return False

    with open("passwords.json", "r") as file:
        passwords = json.load(file)

    for item in passwords:

        if item.get("name", "").lower() == password_name.lower():
            return True

    return False


while True:

    print("\n<================================================= New password ==============================================>\n")

    print(
        "\nWelcome Let's make a password",
        "\n1.Creat a new password",
        "\n2.Load password list",
        "\n3.Quit"
    )

    User_wants = input("Please chooce an option: ")

    if User_wants == "3":
        break


    elif User_wants == "1":

        print("\n<==================================== Ok next step ============================================>\n")

        print(
            "Chooce an option",
            "\n1.Letters only",
            "\n2.Numbers only",
            "\n3.Strong (letters + numbers + symbols)"
        )

        User_letter = input("enter here: ")

        while True:

            try:

                User_input = int(
                    input("How many password characters do you need? ")
                )

                if User_input <= 0:
                    print("enter a number greater than 0")
                    continue

                break

            except ValueError:
                print("please enter number")

        print(
            "<========================================= Your password is ready ============================================>\n"
        )

        print("your password is: ", end="")

        password = ""

        i = 1

        while i <= User_input:

            char = English_word(User_letter)

            print(char, end="")

            password += char

            i += 1


        # نوع پسورد
        if User_letter == "1":
            password_type = "Letters only"

        elif User_letter == "2":
            password_type = "Numbers only"

        else:
            password_type = "Strong"


        # پرسیدن برای ذخیره
        save_option = input("\n\nDo you want to save this password? (y/n): ")

        if save_option.lower() == "y":

            while True:

                password_name = input("Enter a name for this password: ")

                if password_name_exists(password_name):

                    print("This name already exists! Choose another name.")

                else:
                    break


            save_password(password_name, password, password_type)

            print("\nPassword saved successfully 🔥")

        else:
            print("\nPassword not saved.")


    elif User_wants == "2":

        print("\n<==================================== Saved Passwords ============================================>\n")

        try:

            with open("passwords.json", "r") as file:

                passwords = json.load(file)

                if len(passwords) == 0:
                    print("No saved passwords.")

                else:

                    for item in passwords:

                        print(f"Name     : {item.get('name', 'Unknown')}")
                        print(f"Password : {item.get('password', 'None')}")
                        print(f"Type     : {item.get('type', 'Unknown')}")
                        print("-" * 50)

        except:
            print("No password file found.")


    else:
        print("Invalid option!")


    input("\n\npress enter to return to menu ...")