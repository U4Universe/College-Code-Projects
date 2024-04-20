from tkinter import*
from tkinter import messagebox
root=Tk()
var1=StringVar()
var2=StringVar()

itv1=Label(root,text="Username").grid(row=1,column=0)
e1=Entry(root,textvariable = var1,bd=10,fg="Black",bg="White",font='Helvetica').grid(row=1,column=1)

itv2=Label(root,text="Password").grid(row=2,column=0)
e2=Entry(root,textvariable = var2,bd=10,fg="Black",bg="White",font='Helvetica').grid(row=2,column=1)

def submit():
    username = var1.get()
    password = var2.get()
    if not username:
        messagebox.showerror("Error","Please Enter Username")
    elif not password:
        messagebox.showerror("Error","Please Enter Password")
    else:
        messagebox.showinfo("Welcome","Username: "+var1.get()+" Password: "+var2.get())


b=Button(root,text="Submit",command=submit).grid(row=7,column=1)


