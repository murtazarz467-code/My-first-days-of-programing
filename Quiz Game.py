while True:
    print("Welcome if you want to play Quiz game enter Start or if you don't want to play enter Quit! ")

    User_start = input("Do you want to start? ").lower()

    if User_start != "start":
        break

    scores = 0
    Correct = 0

    print("\n=============== Start ===============")
    print("\nWelcome Ok Start!")

    print("\nOk first question What is algorithm (it has 4 number )?",
          "\nOption A: An algorithm is a program",
          "\nOption B: An algorithm is a type of hardware",
          "\nOption C: An algorithm is a step by step set of instructions to solve a problem",
          "\nOption D: An algorithm is a type of problem solving")
    Answer = input("Ok which option is correct A B C or D ===> ").lower()
    if Answer == "c":
        print("correct")
        Correct += 1
        scores += 4
    else:
        print("Incorrect")


    print("\nOk first question What is compiler (it has 6 number )?",
          "\nOption A: Compiler is a program that translates source code into machine code.",
          "\nOption B: An compiler is a type of hardware.",
          "\nOption C: A compiler is used to draw graphics on the screen.",
          "\nOption D: A compiler is a program that stores data.")
    Answer = input("Ok which option is correct A B C or D ===> ").lower()
    if Answer == "a":
        print("correct")
        Correct += 1
        scores += 6
    else:
        print("Incorrect")

    print("Your score is", scores,
          "\nand correct answers are",Correct)
    
    print("\n============= Down =============","\n")