import turtle
import time
import random

WIDTH , HEIGTH = 500,500  # setting width and heigth for the screen
COLORS = ['red','orange','yellow','blue','green','black','brown','cyan','purple','pink'] #storing colors to give colors for each racers

def get_number_of_racers():  # taking number of racers from the user
    racers = 0
    while True:
        racers = input('Enter the number of racers (2-10) : ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric try again !")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else :
            print("Number Is Not In Range ..")

    

    #This Function is To Move the Turtles forward
def race(colors):                             
    turtles = create_turtle(colors)           #calling create turtle function
    while True:                               # when any one turtles/racer hits the finish line while loop will stop
        for racer in turtles:
            distance = random.randint(1,20)  # it give random number between 1 to 20 pixels
            racer.forward(distance)          # it moves between 1 to 20 pixels

            x,y = racer.pos()                # this stores x and y values repectively
            if y>=HEIGTH//2-10:              # checking if any turtle win or not
                time.sleep(3)                # if any one turle touches the win line screen stop for 3 second
                return colors[turtles.index(racer)] # it return the index value of the winner 



    # This function creates number of turtle given by the user
def create_turtle(colors):
    turtles = []                # creating empty "list" to store the racers
    scapingx = WIDTH // (len(colors)+1)  # gap b/w the turtles/racer/objects
    
    # creating 
    for i , color in enumerate(colors):
        racer = turtle.Turtle() # creating turtles/objects
        racer.color(color)      # setting random color to racer/turtles
        racer.shape("turtle")   #giving turtle shape to the racer
        racer.left(90)          #setting left 90 deg because normally it is placed right side in the middle screen
        racer.penup()           # removing line/path of the racer/turtles
        racer.setpos(-WIDTH//2 + (i+1)*scapingx,-HEIGTH//2+20)          # setting the position of the racer/turtles
        racer.pendown()         # agian adding path/line to the turtles/racer/objects
        turtles.append(racer)   # inserting the racer new object/new turtles/new racer to "turtles List"
    return turtles  #returning turtles list to turtles list in line 27

    # creating screen
def init_turtle():
    screen = turtle.Screen()    # Creation of White Screen
    screen.setup(WIDTH,HEIGTH)  #Giving Width and Height of Screen
    screen.title("Turtle Race") #Giving Title For The Screen




racers = get_number_of_racers() # it stores number of turtles
init_turtle()                   #calling the creating screen function
random.shuffle(COLORS)          # shuffling The colors list
colors = COLORS[:racers]        #taking colors based on number of racers

winner = race(colors)           # storing winner color to winner variable
print("WIINER IS : ",winner)    # printing winner
