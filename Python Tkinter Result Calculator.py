import tkinter as tk
from tkinter import Label, Entry, Button, END

#create a tkinter window
window = tk.Tk()

#setting title to the window
window.title("COMPUTER SCIENCE SEM II MARKS CALCULATOR")

def calculate_sum_and_grade():
    try:
        python_marks=float(E1.get())
        java_marks=float(E2.get())
        c_marks=float(E3.get())
        smth_marks=float(E4.get())
        linux_marks=float(E5.get())
        calculus_marks=float(E6.get())
        sma_marks=float(E7.get())
        ce_marks=float(E8.get())
        gt_marks=float(E9.get())
        cplusplus_marks=float(E10.get())

        #calculate total marks
        total_marks = python_marks + java_marks + c_marks + linux_marks + smth_marks + calculus_marks + sma_marks + ce_marks + gt_marks + cplusplus_marks

        #calculate percentage from total marks
        percentage = (total_marks / 1000) * 100
        
        #update the total_marks field
        E11.delete(0, END)
        E11.insert(0,total_marks)

        #upade the percentage field
        E12.delete(0, END)
        E12.insert(0, "{:.2f} %".format(percentage))

       
        #calculate grade
        if percentage >= 90:
            grade = "O"
            remarks = "Outstanding" 
        elif percentage >= 80:
            grade = "A+" 
            remarks = "Excellent"
        elif percentage >= 70:
            grade = "A"
            remarks = "Good" 
        elif percentage >= 60:
            grade = "B"
            remarks = "Average" 
        elif percentage >= 50:
            grade = "C"
            remarks = "Poor"
        elif percentage >= 40:
            grade = "D"
            remarks = "Very Poor"
        else:
            grade = "F"
            remarks = "Fail"

        #update the grade field
        E13.delete(0, END)
        E13.insert(0, grade)
        #update the remarks field
        E14.delete(0, END)
        E14.insert(0, remarks) 
    except ValueError:
        E11.delete(0, END)
        E11.insert(0,"Invalid input")

#creating the label and entry fields        
L1=Label(window, text="Python")
L1.place(x=10,y=10)
E1=Entry(window, bd=5)
E1.place(x=80,y=10)

L2=Label(window,text="Java")
L2.place(x=220,y=10)
E2=Entry(window, bd=5)
E2.place(x=290,y=10)

L3=Label(window,text="C")
L3.place(x=10,y=40)
E3=Entry(window, bd=5)
E3.place(x=80,y=40)

L4=Label(window,text="Linux")
L4.place(x=220,y=40)
E4=Entry(window, bd=5)
E4.place(x=290,y=40)

L5=Label(window,text="SMTH")
L5.place(x=10,y=70)
E5=Entry(window, bd=5)
E5.place(x=80,y=70)

L6=Label(window,text="Calculus")
L6.place(x=220,y=70)
E6=Entry(window, bd=5)
E6.place(x=290,y=70)

L7=Label(window,text="SMA")
L7.place(x=10,y=100)
E7=Entry(window, bd=5)
E7.place(x=80,y=100)

L8=Label(window,text="CE")
L8.place(x=220,y=100)
E8=Entry(window, bd=5)
E8.place(x=290,y=100)

L9=Label(window,text="GT")
L9.place(x=10,y=130)
E9=Entry(window, bd=5)
E9.place(x=80,y=130)

L10=Label(window,text="C++")
L10.place(x=220,y=130)
E10=Entry(window, bd=5)
E10.place(x=290,y=130)


L11=Label(window,text="Marks")
L11.place(x=10,y=190)
E11=Entry(window, bd=5)
E11.place(x=80,y=190)

L12=Label(window,text="Percentage")
L12.place(x=220,y=190)
E12=Entry(window, bd=5)
E12.place(x=290,y=190)

L13=Label(window,text="Grade")
L13.place(x=10,y=230)
E13=Entry(window, bd=5)
E13.place(x=80,y=230)

E14=Label(window, text="Remarks")
E14.place(x=220,y=230)
E14=Entry(window,text="", bd=5)
E14.place(x=290,y=230)

B=Button(window, text="SHOW RESULT",bg="blue",fg="white",command=calculate_sum_and_grade,width=20,height=2)
B.place(x=150,y=290)

window.mainloop()
