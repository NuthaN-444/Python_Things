# ------- Rock Paper Scissor Game -------

import random

# --- Here Dictionary Stores The Emojis Respective Characters ---
emojis = {'r':'🪨' , 'p':'📃' , 's':'✂️'}

# ---Here in Tuple stores characters for Rock paper scissors ---
choices = ('r','p','s')
name = input("Enter Your Name -->  ").upper()

while True:
    
    # --- Taking user Choice ---
    userChoice = input("Enter Choice --> ('r','p','s') -->  ").lower()
    print()

    # --- if User Choice is other than this --> (r , p , s) . prints "invalid choice" ---
    if userChoice != 'r' and userChoice !='p' and userChoice != 's':
        print(" -------------Invalid Choice --------------- ")
        break
    print("----------------------------------------")


    # --- random choice for computer/bot ---
    computer_choice = random.choice(choices)


    # --- printing Both users Choice & Computer Choice ---
    print("User Chose      -->   ",emojis[userChoice])
    print()
    print("Computer Chose  -->   ",emojis[computer_choice])
    print()



    if userChoice == computer_choice:
        print("------------Tie -------------")
        print()
    
    elif ((userChoice == 'r' and computer_choice == 'p') or (userChoice == 'p' and computer_choice == 's') or (userChoice == 's' and computer_choice == 'r')) :
        print("------------You Loose ------------")
        print()

    elif ((userChoice == 'p' and computer_choice == 'r') or (userChoice == 's' and computer_choice == 'p') or (userChoice == 'r' and computer_choice == 's')) :
        print("---------- You Won----------")
        print()

    # --- Asking to User Wants to Play again Or Not ---
    PlayAgain = input("Want To Play Again --> (yes / no)   -->  ").lower()
    print()


    print("--------------------------------------------------------------")
    print()

    # --- if user is yes then Game will continue other game will end ---
    if(PlayAgain == 'no'):
        print(f"------ THANKYOU {name} FOR PLAYING , YOU PLAYED WELL ------")
        print()
        print("---------------------------- End -----------------------------")
        print()
        print()
        break






