#importing libs
import tkinter
import random
from tkinter import messagebox


#main window
root=tkinter.Tk()
root.geometry("400x500")
root.maxsize(400,500)
root.minsize(400,500)
root.title("Password Generator")


#creating command functions
#for  Generating password
def Gen_pass():
    l=[]
    if not name.get():
        tkinter.messagebox.showerror(title="Error", message="Enter the name...")
        return
    if(length.get()<8 ):
        tkinter.messagebox.showerror(title="Error", message="Password lrngth is too short...")
        return
    #according the complexity level
    if(val.get()==3):
        for i in range(length.get()//4):
            l.append(chr(random.randint(65,90)))
        for i in range(length.get()//4):
            l.append(chr(random.randint(97,122)))
        for i in range(length.get()//3):
            l.append(chr(random.randint(33,65)))
        rem=length.get()-(length.get()//4+length.get()//4+length.get()//3)
        for i in range(rem):
            l.append(random.choice("[]\^_`{}~|"))
    elif(val.get()==2):
        for i in range(length.get()//3):
            l.append(chr(random.randint(65,90)))
        for i in range(length.get()//3):
            l.append(chr(random.randint(97,122)))
        for i in range(length.get()//3):
            l.append(chr(random.randint(33,65)))
        rem=length.get()-(length.get()//3+length.get()//3+length.get()//3)
        for i in range(rem):
            l.append(random.choice("[]\^_`{}~|"))
    else:
        for i in range(length.get()//3):
            l.append(chr(random.randint(65,90)))
        for i in range(length.get()//3):
            l.append(chr(random.randint(97,122)))
        for i in range(length.get()//4):
            l.append(chr(random.randint(33,65)))
        rem=length.get()-(length.get()//3+length.get()//3+length.get()//4)
        for i in range(rem):
            l.append(random.choice("[]\^_`{}~|"))
    random.shuffle(l)
    passwrd=''.join(l)
    Pass.set(passwrd)

#for accepting the password
def Accept(): 
    if not pass_entry.get():
        tkinter.messagebox.showerror(title="Error", message="There is no Generated Password...")
        return
    tkinter.messagebox.showinfo(title="Accept", message=f"Write or Remember the Password,But Never share it...  \n\n\t\t{Pass.get()}")
    pass_entry.delete(0,tkinter.END)

#for the reset of entries
def Reset():
    name_entry.delete(0,tkinter.END)
    leng.delete(0,tkinter.END)
    pass_entry.delete(0,tkinter.END)


#creating user friendly-GUI
tkinter.Label(text="Password Genrator",font="Serif 20 bold").grid(row=0,column=0,columnspan=3,pady=20,padx=20)

tkinter.Label(root,text="Enter the Name: ",font="Serif 10 bold").grid(row=1,column=0,padx=20,pady=5)
name=tkinter.StringVar()
name_entry=tkinter.Entry(root,textvariable=name,font="Serif 10 ",borderwidth=2)
name_entry.grid(row=1,column=1,padx=20,pady=5)

tkinter.Label(root,text="Enter Password Length: ",font="Serif 10 bold").grid(row=2,column=0,padx=20,pady=5)
length=tkinter.IntVar()
leng=tkinter.Entry(root,textvariable=length,font="Serif 10",borderwidth=2)
leng.grid(row=2,column=1,padx=20,pady=5)

tkinter.Label(root,text="Generated Password: ",font="Serif 10 bold").grid(row=3,column=0,padx=20,pady=5)
Pass=tkinter.StringVar()
pass_entry=tkinter.Entry(root,textvariable=Pass,font="Serif 10",borderwidth=2)
pass_entry.grid(row=3,column=1,padx=20,pady=5)

tkinter.Label(root,text="Complexity level: ",font="Serif 10 bold").grid(row=4,column=0,pady=5,padx=20)
val=tkinter.Scale(root,from_=1,to=3,orient="horizontal")
val.grid(row=4,column=1,pady=10,padx=20)

tkinter.Button(root,text="Generate Password",command=Gen_pass,font="Serif 15",bg="blue").grid(row=5,column=0,columnspan=3,padx=20,pady=20)
tkinter.Button(root,text="Accept",command=Accept,font="Serif 15",bg="green").grid(row=6,column=0,columnspan=3,padx=20,pady=10)
tkinter.Button(root,text="Reset",command=Reset,font="Serif 15",bg="red").grid(row=7,column=0,columnspan=3,padx=20,pady=10)

#end the mainloop
root.mainloop()