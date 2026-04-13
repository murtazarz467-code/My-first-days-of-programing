while True:
    User_wanting = input("If you want to start program enter start ===> ").lower()
    if User_wanting != "start":
        print("Good bye")
        break
    while True:
        try:
            User_Number = int(input("enter you number ===> "))
            break
        except ValueError:
            print("Please enter a number ")


    if User_Number % 3 == 0 and User_Number % 5 == 0:
        print("Python Data Science")
    elif User_Number % 3 == 0:
        print("python")
    elif User_Number % 5 == 0:
        print("Data Science")
    else:
        print(User_Number)

