# ------- Rock Paper Scissor Game -------


import random   # To make computer’s choice randomly between ( r , p , s )


# To display emojis for better user experience
emojis = {'r':'🪨' , 'p':'📃' , 's':'✂️'}       


# Here in Tuple stores characters for Rock(R) paper(P) scissors(S) 
choices = ('r','p','s')       # Computer Picks random choice from this tuple  


#  To track scores during the game.
userPoints = computerPoints = 0        
name = input("Enter Your Name -->  ")  #Taking User Name


a=0     # Iteration Variable

# to play the game for 10 rounds
while a<10:        
    
    # Taking user Choice for each round
    userChoice = input("Enter Choice --> ('r','p','s') -->  ").lower()
    print()

    #  If the user enters something other than 'r', 'p', 's'. Prints invalid and ends the game
    if userChoice != 'r' and userChoice !='p' and userChoice != 's':
        print(" -------------Invalid Choice --------------- ")
        exit(1)
    print("----------------------------------------")


    # random choice for computer/bot 
    computer_choice = random.choice(choices)


    # printing Both users Choice & Computer Choice
    print("User Choice      -->   ",emojis[userChoice])
    print()
    print("Computer Choice  -->   ",emojis[computer_choice])
    print()


    # Both user and computer choose the same prints tie
    if userChoice == computer_choice: 
        print("------------Tie -------------")
        print()
        print()
    

    # all loosing possiblities conditions if the condition true prints You loose
    elif ((userChoice == 'r' and computer_choice == 'p') or (userChoice == 'p' and computer_choice == 's') or (userChoice == 's' and computer_choice == 'r')) :
        print("------------You Loose ------------")
        computerPoints+=1
        print()
        print()


    # all winning possiblities conditions if the condition true prints You won
    elif ((userChoice == 'p' and computer_choice == 'r') or (userChoice == 's' and computer_choice == 'p') or (userChoice == 'r' and computer_choice == 's')) :
        print("---------- You Won----------")
        userPoints+=1
        print()
        print()

    a+=1       # updating 'a' with 1 each round so that it runs 10 times

# Printing the points of both player and computer
print(f"{name} Your Points Is {userPoints}")
print(f"Computer points Is {computerPoints}")


# Deciding the winner 
if userPoints == computerPoints:    
    print("------------------Tie--------------------")
    exit(1)

elif userPoints > computerPoints:
        print()
        print()
        print(f"------ Congratulations {name} You Won The Match , You Played Well ------")
        print()
        print("---------------------------- End -----------------------------")
        print()
        print()
        exit(1)

else :
        print()
        print()
        print(f"---------------------- Computer Wins The Game ------------------------")
        print()
        print("---------------------------- End -----------------------------")
        print()
        print()
        exit(1)
        



