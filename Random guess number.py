import random

player_Name = []
scores = {}

print("Welcome if you want to play play game enter Start or if you don't want to play enter Quit! ")

User_start = input("Do you want to start? ").lower()

if User_start != "start":
    quit()

print("\n============== Start ===============")
#Asking about how many player is there
players = int(input("How many player is there ===> "))

for i in range(players):
    print("\n----- New player -----")

    #Asking Player Name
    Name = input("What is player Name ===> ")

    # Adding player Name in list
    player_Name.append(Name)

    # Times player could not
    Could_Not = 1

    #Computer random Number
    Computer_Number = random.randint(1,100)
    print("Guess number between 1 to 100")

    #Starting the game

    #Asking player Number
    while True:
        try:
            Player_Number = int(input("Try your Number (Enter your Number)===> "))
            break
        except ValueError:
            print("please enter a valid Number!")

    #Process of game
    while Computer_Number != Player_Number:
        if Player_Number > Computer_Number:
            print("your number is bigger")
        elif Player_Number < Computer_Number:
            print("your number is smaller")

        while True:
            try:
                Player_Number = int(input("enter your number(you can try agen)===> "))
                break
            except ValueError:
                print("Enter a valid Number!")
                                
        Could_Not += 1

    else:
        print("the number was ===>", Computer_Number, "you found it in", Could_Not,"tries")

    scores[Name] = Could_Not

#Making a little space
for i in range(1,5):
    print("")

print("\n========== Results ==========")

winner = min(scores, key=scores.get)

print("\n Winner is:", winner)
print("with", scores[winner], "tries!")