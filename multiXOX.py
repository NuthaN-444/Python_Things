# Multiplier XOX GAME

import random


name = input("Enter Your Name >>> ")
blocks = [['.','.','.'],['.','.','.'],['.','.','.']]       # Multi List To Store The Data Of both Players
print("__________________________________________")
choice = input("Enter 1 for play with friend or Enter 2 for play with Bot >>> ")
print("__________________________________________")
user_1_Symbol = input("Enter The Symbol (X or O) >>> ").upper()   #Taking (X or O ) Symbol From User 


if (user_1_Symbol == 'X' or user_1_Symbol == 'O'):                # Checking If User1 Entered Character is X or O
     pass
else :
     print("___________________________________________________________________")
     print("You have Entered InCorrect Symbol , So Please Restart The Game ...")
     print()
     print()
     print()
     exit(1)


user_2_symbol = 's'
def User_2_symbol():
     if user_1_Symbol =='X':               # This function Stores Left Out of The Symbol To user 2 Symbol 
          user_2_symbol = 'O'
     else :
          user_2_symbol = 'X'
     print("__________________________________________")         
     print("Caution !!! Remember Your Symbol")
     print("__________________________________________")
     print("User 1 Symbol is :: ",user_1_Symbol)
     print("__________________________________________")
     print("User 2 Symbol is :: ",user_2_symbol)
     return user_2_symbol


computerSymbol = 's'      
def Computer_symbol():                   # This function Stores Left Out of The Symbol To computer's Symbol 
     if user_1_Symbol =='X':             
          computerSymbol = 'O'
     else :
          computerSymbol = 'X'
          print("__________________________________________")         
     print("Caution !!! Remember Your Symbol")
     print("__________________________________________")
     print("Your Symbol is :: ",user_1_Symbol)
     print("__________________________________________")
     print("Computer Symbol is :: ",computerSymbol)
     return computerSymbol


# This Function Stores Data To Random position  to the List
def computerChoiceFunc() :
    computerPosiRow = random.randint(0,2)   #Random row b/w [0,2]
    computerPosiCol = random.randint(0,2)    #Random col b/w [0,2]

    if  blocks[computerPosiRow][computerPosiCol] == '.':                   # this condition check if that particular position is already any symbol is there Or not
        blocks[computerPosiRow][computerPosiCol] = computerSymbol          # stroing the computer's symbol
        for i in range(3):                                                  # prints the entire list After Storing The Computer's symbol 
            for j in range(3):
               print(blocks[i][j],end=' ')
            print()
        print("__________________________________________")
    else :                                                                 # for another Chance if if block is not execute
        computerChoiceFunc()


def user_1_ChoiceFunc() :
        print("__________________________________________")
        print("Now User 1 Turn : ")
        print("__________________________________________")
        usersPosiRow = int(input("User 1 Enter The Position Of Row >>> "))             # taking Row position from user
        print("__________________________________________")
        usersPosiCol = int(input("User 1 Enter The Position Of Column >>> "))          # taking Col position from user

        if ((usersPosiRow >= 0 and usersPosiRow <3) and (usersPosiCol >= 0 and usersPosiCol <3)):         # Chceking if user entered out of the range positon
            if blocks[usersPosiRow][usersPosiCol] == '.' :                      # this condition check if that particular position is already any symbol is there Or not
                blocks[usersPosiRow][usersPosiCol] = user_1_Symbol                 # stroing the user's symbol
                for i in range(3):                                              # prints the entire list After Storing The user's symbol 
                     for j in range(3):
                         print(blocks[i][j],end=' ')
                     print()
                print("__________________________________________")
               
            else:
               print("__________________________________________")
               print("Your Position Is Not Empty ! ")
               user_1_ChoiceFunc()                                                  # for another Chance if if block is not execute
        else :
          print("__________________________________________")
          print("Opps! You Entered Invalid Range Or Symbol ... ")
          user_1_ChoiceFunc() 


def user_2_ChoiceFunc() :
        print("__________________________________________")
        print("Now User 2 Turn : ")
        print("__________________________________________")
        usersPosiRow = int(input("User 2 Enter The Position Of Row >>> "))             # taking Row position from user
        print("__________________________________________")
        usersPosiCol = int(input("User 2 Enter The Position Of Column >>> "))          # taking Col position from user      # taking Col position from user

        if ((usersPosiRow >= 0 and usersPosiRow <3) and (usersPosiCol >= 0 and usersPosiCol <3)):         # Chceking if user entered out of the range positon
            if blocks[usersPosiRow][usersPosiCol] == '.' :                      # this condition check if that particular position is already any symbol is there Or not
                blocks[usersPosiRow][usersPosiCol] = user_2_symbol                 # stroing the user's symbol
                for i in range(3):                                              # prints the entire list After Storing The user's symbol 
                     for j in range(3):
                         print(blocks[i][j],end=' ')
                     print()
                print("__________________________________________")
               
            else:
               print("__________________________________________")
               print("Your Position Is Not Empty ! ")
               user_2_ChoiceFunc()                                                  # for another Chance if if block is not execute
        else :
          print("__________________________________________")
          print("Opps! You Entered Invalid Range Or Symbol ... ")
          user_2_ChoiceFunc()


               # This Function Return if user1 can be win or not



def isUser_1_Winner() :                                                             
     if blocks[0][0] == user_1_Symbol and blocks[1][1] == user_1_Symbol and blocks[2][2] == user_1_Symbol :                       
          return True
     
     elif blocks[0][2] == user_1_Symbol and blocks[1][1] == user_1_Symbol and blocks[2][0] == user_1_Symbol:
          return True
     
     elif blocks[0][0] == user_1_Symbol and blocks[0][1] == user_1_Symbol and blocks[0][2] == user_1_Symbol:
          return True
     
     elif blocks[1][0] == user_1_Symbol and blocks[1][1] == user_1_Symbol and blocks[1][2] == user_1_Symbol:
          return True
     
     elif blocks[2][0] == user_1_Symbol and blocks[2][1] == user_1_Symbol and blocks[2][2] == user_1_Symbol:
          return True
     
     elif blocks[0][0] == user_1_Symbol and blocks[1][0] == user_1_Symbol and blocks[2][0] == user_1_Symbol:
          return True
     
     elif blocks[0][1] == user_1_Symbol and blocks[1][1] == user_1_Symbol and blocks[2][1] == user_1_Symbol:
          return True
     
     elif blocks[0][2] == user_1_Symbol and blocks[1][2] == user_1_Symbol and blocks[2][2] == user_1_Symbol:
          return True
     
     return False


               # This Function Return if user2 is win or not

def isUser_2_Winner() :                                                             
     if blocks[0][0] == user_2_symbol and blocks[1][1] == user_2_symbol and blocks[2][2] == user_2_symbol :                       
          return True
     
     elif blocks[0][2] == user_2_symbol and blocks[1][1] == user_2_symbol and blocks[2][0] == user_2_symbol:
          return True
     
     elif blocks[0][0] == user_2_symbol and blocks[0][1] == user_2_symbol and blocks[0][2] == user_2_symbol:
          return True
     
     elif blocks[1][0] == user_2_symbol and blocks[1][1] == user_2_symbol and blocks[1][2] == user_2_symbol:
          return True
     
     elif blocks[2][0] == user_2_symbol and blocks[2][1] == user_2_symbol and blocks[2][2] == user_2_symbol:
          return True
     
     elif blocks[0][0] == user_2_symbol and blocks[1][0] == user_2_symbol and blocks[2][0] == user_2_symbol:
          return True
     
     elif blocks[0][1] == user_2_symbol and blocks[1][1] == user_2_symbol and blocks[2][1] == user_2_symbol:
          return True
     
     elif blocks[0][2] == user_2_symbol and blocks[1][2] == user_2_symbol and blocks[2][2] == user_2_symbol:
          return True
     
     return False


               # This Function Return if computer can be win ot not 

def isComputerWinner():
     if blocks[0][0] == computerSymbol and blocks[1][1] == computerSymbol and blocks[2][2] == computerSymbol :
          return True
     
     elif blocks[0][2] == computerSymbol and blocks[1][1] == computerSymbol and blocks[2][0] == computerSymbol:
          return True
     
     elif blocks[0][0] == computerSymbol and blocks[0][1] == computerSymbol and blocks[0][2] == computerSymbol:
          return True
     
     elif blocks[1][0] == computerSymbol and blocks[1][1] == computerSymbol and blocks[1][2] == computerSymbol:
          return True
     
     elif blocks[2][0] == computerSymbol and blocks[2][1] == computerSymbol and blocks[2][2] == computerSymbol:
          return True
     
     elif blocks[0][0] == computerSymbol and blocks[1][0] == computerSymbol and blocks[2][0] == computerSymbol:
          return True
     
     elif blocks[0][1] == computerSymbol and blocks[1][1] == computerSymbol and blocks[2][1] == computerSymbol:
          return True
     
     elif blocks[0][2] == computerSymbol and blocks[1][2] == computerSymbol and blocks[2][2] == computerSymbol:
          return True
     
     return False


a=1
if (choice == '1'):         # with friend
     user_2_symbol = User_2_symbol()
     while (a<10) :                                 # It Runs 9 Times Because There are 9 blocks
          user_1_ChoiceFunc()                                  
          user_2_ChoiceFunc()
          if isUser_1_Winner() == True:
              print("__________________________________________")
              print("-------------- User 1 Win --------------")
              print("____________________________________________________________")
              print(" User 1 , Do You Like To Play Again ! ...")
              break
          if isUser_2_Winner() == True:
               print("__________________________________________")
               print("-------------- User 2 Win --------------")
               print("____________________________________________________________")
               print(" User 2 , Do You Like To Play Again ! ...")
               break
          a+=1
else :              # with Computer 
     computerSymbol = Computer_symbol()
     while (a<10) :                                         # It Runs 9 Times Because There are 9 blocks
          user_1_ChoiceFunc()                         
          computerChoiceFunc()
          if isUser_1_Winner() == True:
              print("__________________________________________")
              print("-------------- You Win --------------")
              break
          if isComputerWinner() == True:
               print("__________________________________________")
               print("-------------- You LOSE --------------")
               break
          a+=1



print()
print()
print()
print()
print()
print()
