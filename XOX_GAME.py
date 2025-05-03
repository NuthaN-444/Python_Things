# XOX GAME
import random


name = input("Enter Your Name >>> ").upper()
blocks = [['.','.','.'],['.','.','.'],['.','.','.']]           # Multi List To Store The Data Of both Players
print("__________________________________________")
userSymbol = input("Enter The Symbol (X or O) >>> ").upper()   #Taking (X or O ) Symbol From User 

if (userSymbol == 'X' or userSymbol == 'O'):                   
     pass
else :
     print("___________________________________________________________________")
     print("You have Entered InCorrect Symbol , So Please Restart The Game ...")
     print()
     print()
     print()
     exit(1)

computerSymbol = "S"     # For Simplicity

if userSymbol =='X':               # This Condition Stores Left Out of The Symbol To Computer's Symbol 
     computerSymbol = 'O'
else :
     computerSymbol = 'X'

print("__________________________________________")         
print("Caution !!! Remember Your Symbol")
print("__________________________________________")
print("Your Symbol is :: ",userSymbol)
print("__________________________________________")
print("Computer Symbol is :: ",computerSymbol)
     


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


def userChoiceFunc() :
        print("__________________________________________")
        usersPosiRow = int(input("Enter The Position Of Row >>> "))             # taking Row position from user
        print("__________________________________________")
        usersPosiCol = int(input("Enter The Position Of Column >>> "))          # taking Col position from user

        if ((userSymbol == 'X' or userSymbol =='O') and (usersPosiRow >= 0 and usersPosiRow <3) and (usersPosiRow >= 0 and usersPosiRow <3)):         # Chceking if user entered out of the range positon
            if blocks[usersPosiRow][usersPosiCol] == '.' :                      # this condition check if that particular position is already any symbol is there Or not
                blocks[usersPosiRow][usersPosiCol] = userSymbol                 # stroing the user's symbol
                for i in range(3):                                              # prints the entire list After Storing The user's symbol 
                     for j in range(3):
                         print(blocks[i][j],end=' ')
                     print()
                print("__________________________________________")
               
            else:
               print("__________________________________________")
               print("Your Position Is Not Empty ! ")
               userChoiceFunc()                                                  # for another Chance if if block is not execute
        else :
          print("__________________________________________")
          print("Opps! You Entered Invalid Range Or Symbol ... ")



               # This Function Return if user can be win or not

def isUserWinner() :                                                             
     if blocks[0][0] == userSymbol and blocks[1][1] == userSymbol and blocks[2][2] == userSymbol :                       
          return True
     
     elif blocks[0][2] == userSymbol and blocks[1][1] == userSymbol and blocks[2][0] == userSymbol:
          return True
     
     elif blocks[0][0] == userSymbol and blocks[0][1] == userSymbol and blocks[0][2] == userSymbol:
          return True
     
     elif blocks[1][0] == userSymbol and blocks[1][1] == userSymbol and blocks[1][2] == userSymbol:
          return True
     
     elif blocks[2][0] == userSymbol and blocks[2][1] == userSymbol and blocks[2][2] == userSymbol:
          return True
     
     elif blocks[0][0] == userSymbol and blocks[1][0] == userSymbol and blocks[2][0] == userSymbol:
          return True
     
     elif blocks[0][1] == userSymbol and blocks[1][1] == userSymbol and blocks[2][1] == userSymbol:
          return True
     
     elif blocks[0][2] == userSymbol and blocks[1][2] == userSymbol and blocks[2][2] == userSymbol:
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
while (a<10) :                                         # It Runs 9 Times Because There are 9 blocks
     userChoiceFunc()                                  
     computerChoiceFunc()
     if isUserWinner() == True:
         print("__________________________________________")
         print("-------------- You Win --------------")
         break
     if isComputerWinner() == True:
          print("__________________________________________")
          print("-------------- You LOSE --------------")
          break
     a+=1



print("____________________________________________________________")
print(f"Congratulations {name} , Do You Like To Play Again ! ...")
print()
print()
print()
print()
print()
print()

