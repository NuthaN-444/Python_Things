from tkinter import*
from tkinter import messagebox


def submit():
    Label(root,text="Successfully submitted.",fg='green',font=("#1b263b",20),bg='#e0e1dd').place(x=840,y=620)   #Text
    UserName = inputUserName.get()    #getting data
    UserPassword = inputUserPassword.get()    #getting data
    PlatformName = inputPlatformName.get()     #getting data

    print("User Name: ",UserName)
    print("password : ",UserPassword)
    print("platform  : ",PlatformName)

    try:
        #Note : Here Below Give Your file Name
        with open("datauser.txt","a") as file:    # storing data in the file
            file.write(f"UserName : {UserName}\n")
            file.write(f"PassWord : {UserPassword}\n")
            file.write(f"Platform : {PlatformName}\n\n")
    except Exception as e:    # incase file couldn't open
        messagebox.showinfo("Sorry ! We can't Store Your Data due To Some Reason.")

    
    messagebox.showinfo('Submitted', "Your data is submitted successfully!")    # popup



# reset the data in entry field
def reset():
    Label(root,text="Successfully Reset.     ",fg='red',font=("#1b263b",20),bg='#e0e1dd').place(x=840,y=620)#Text
    inputUserName.delete(0, END)
    inputUserPassword.delete(0, END)
    inputPlatformName.delete(0, END)

    messagebox.showinfo("Caution ", "Your Data has been Reset")   # popup


        # step 1 basics things
root = Tk()
root.title("Login Page")
root.configure(background='#e0e1dd')
root.minsize(800,800)
root.geometry('1924x1924')



        # step 2 
text = Label(root,text="LOGIN PAGE",fg='#415a77',font=('white',50,'bold'),bg='#e0e1dd')#Text
text.pack(pady=70)



    #username input
textUserName = Label(root,text="Username : ",fg='#1b263b',font=('#1b263b',20),bg='#e0e1dd')#Text
textUserName.place(x=650,y=300)
inputUserName = Entry(root,text="",fg='#415a77',font=('#415a77',20),bg='white',highlightcolor='white',highlightthickness=1)
inputUserName.place(x=840,y=300)

    #passward input
textUserPassword = Label(root,text="Password : ",fg='#1b263b',font=('#1b263b',20),bg='#e0e1dd')#Text
textUserPassword.place(x=650,y=400)
inputUserPassword = Entry(root,show="*",fg='#415a77',font=('#415a77',20),bg='white',highlightcolor='white',highlightthickness=1)
inputUserPassword.place(x=840,y=400)

    #Address input
textPlatform = Label(root,text="Platform : ",fg='#1b263b',font=('#1b263b',20),bg='#e0e1dd')#Text
textPlatform.place(x=665,y=500)
inputPlatformName = Entry(root,text='',fg='#415a77',font=('#415a77',20),bg='white',highlightcolor='white',highlightthickness=1)
inputPlatformName.place(x=840,y=500)

# submit and reset button
subm = Button(root,text="Submit",fg='white',font=('white',20),bg='#415a77',command=submit)#button
subm.place(x=850,y=680)   

resetbt = Button(root,text="Reset",fg='white',font=('white',20),bg='red',command=reset)#button
resetbt.place(x=980,y=680)

root.mainloop()


