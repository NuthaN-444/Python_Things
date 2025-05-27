# ------- Rock Paper Scissor Game -------

from tkinter import*
from tkinter import messagebox
import random   # To make computer’s choice randomly between ( r , p , s )


global userChoice
global computerChoice
global result
#  To track scores during the game.

userPoints=computerPoints=0

def rockfunc():
    global userPoints,computerPoints

    userChoice='r'
    userChoiceText = Label(root,text="Your Choice :         🪨",fg="black",font=('roboto',40),bg='white').place(x=700,y=300)
    computerChoice = random.choice(choices)
    computerLabel = Label(root,text=f"Computer Choice : {emojis[computerChoice]}",fg="black",font=('roboto',40),bg='white').place(x=700,y=360)
    if userChoice == computerChoice:
        Label(root,text="Tie",fg="black",width=10,font=('roboto',40),bg='white').place(x=800,y=480)

        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)


      # all loosing possiblities conditions if the condition true prints You loose
    elif ((userChoice == 'r' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 's') or (userChoice == 's' and computerChoice == 'r')) :
        Label(root,text="Lose",fg="red",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
        computerPoints+=1
        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)

       
      # all winning possiblities conditions if the condition true prints You won
    elif ((userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p') or (userChoice == 'r' and computerChoice == 's')) :
          Label(root,text="Win",fg="green",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
          userPoints+=1
          Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
          Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)

    if(userPoints == 10 ):
        messagebox.showinfo("Result","You Win")
        exit(1)
    elif(computerPoints == 10):
        messagebox.showinfo("Result","Computer Wins")
        exit(1)





def paperfunc():
    global userPoints,computerPoints


    userChoice='p'
    userChoiceText = Label(root,text="Your Choice :         📃",fg="black",font=('roboto',40),bg='white').place(x=700,y=300)
    computerChoice = random.choice(choices)
    computerLabel = Label(root,text=f"Computer Choice : {emojis[computerChoice]}",fg="black",font=('roboto',40),bg='white').place(x=700,y=360) 
    if userChoice == computerChoice:
        Label(root,text="Tie",fg="black",width=10,font=('roboto',40),bg='white').place(x=800,y=480)


        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)


      # all loosing possiblities conditions if the condition true prints You loose
    elif ((userChoice == 'r' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 's') or (userChoice == 's' and computerChoice == 'r')) :
        Label(root,text="Lose",fg="red",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
        computerPoints+=1
        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)



      # all winning possiblities conditions if the condition true prints You won
    elif ((userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p') or (userChoice == 'r' and computerChoice == 's')) :
          Label(root,text="Win",fg="green",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
          userPoints+=1
          Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
          Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)

          
    if(userPoints == 10 ):
        messagebox.showinfo("Result","You Win")
        exit(1)
    elif(computerPoints == 10):
        messagebox.showinfo("Result","Computer Wins")
        exit(1)




def scissorfunc():
    global userPoints,computerPoints
    
    userChoice='s'
    userChoiceText = Label(root,text="Your Choice :         ✂️",fg="black",font=('roboto',40),bg='white').place(x=700,y=300)
    computerChoice = random.choice(choices) 
    computerLabel = Label(root,text=f"Computer Choice : {emojis[computerChoice]}",fg="black",font=('roboto',40),bg='white').place(x=700,y=360)
    if userChoice == computerChoice:
        Label(root,text="Tie",fg="black",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)
       


      # all loosing possiblities conditions if the condition true prints You loose
    elif ((userChoice == 'r' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 's') or (userChoice == 's' and computerChoice == 'r')) :
        Label(root,text="Lose",fg="red",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
        computerPoints+=1
        Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
        Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)



      # all winning possiblities conditions if the condition true prints You won
    elif ((userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p') or (userChoice == 'r' and computerChoice == 's')) :
          Label(root,text="Win",fg="green",width=10,font=('roboto',40),bg='white').place(x=800,y=480)
          userPoints+=1
          Label(root,text=f"Your Points : {userPoints}",fg="black",width=15,font=('roboto',30),bg='white').place(x=400,y=600)
          Label(root,text=f"Computer Points : {computerPoints}",fg="black",width=17,font=('roboto',30),bg='white').place(x=1200,y=600)

    if(userPoints == 10 ):
        messagebox.showinfo("Result","You Win")
        exit(1)
    elif(computerPoints == 10):
        messagebox.showinfo("Result","Computer Wins")
        exit(1)



root = Tk()
root.title("RockPaperScissors")
root.configure(background='white')
root.geometry('1800x1800')

Label(root,text='RocK PapeR ScissorR',fg='red',font=("roboto",50,'bold'),bg='white').place(x=630,y=60)

rockbtn = Button(root,text='🪨Rock',width=8,font=("roboto",20),command=rockfunc).place(x=700,y=800)
paperbtn = Button(root,text='📃Paper',width=8,font=("roboto",20),command=paperfunc).place(x=900,y=800)
scissorbtn = Button(root,text='✂️Scissor',font=("roboto",20),command=scissorfunc).place(x=1100,y=800)

  
# To display emojis for better user experience
emojis = {'r':'🪨' , 'p':'📃' , 's':'✂️'}   


# Here in Tuple stores characters for Rock(R) paper(P) scissors(S) 
choices = ('r','p','s')       # Computer Picks random choice from this tuple  





root.mainloop()
print(userPoints,computerPoints)