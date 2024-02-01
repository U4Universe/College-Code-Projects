from tkinter import*
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

        #calculate total marks
        total_marks = python_marks + java_marks + c_marks + linux_marks + smth_marks + calculus_marks + sma_marks + ce_marks + gt_marks

        #calculate percentage from total marks
        percentage = (total_marks / 900) * 100
        
        #update the total_marks field
        E10.delete(0, END)
        E10.insert(0,total_marks)

        #upade the percentage field
        E11.delete(0, END)
        E11.insert(0, "{:.2f} %".format(percentage))

       
        #calculate grade
        if percentage >= 90:
            grade = "O"
            remarks = "Outstanding" 
        elif percentage >= 80:
            grade = "A+" #
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
        E12.delete(0, END)
        E12.insert(0, grade)
        #update the remarks field
        E13.delete(0, END)
        E13.insert(0, remarks) 
    except ValueError:
        E10.delete(0, END)
        E10.insert(0,"Invalid input")

#creating the label and entry fields        
top=Tk()
L1=Label(top, text="Python")
L1.place(x=10,y=10)
E1=Entry(top, bd=5)
E1.place(x=80,y=10)

L2=Label(top,text="Java")
L2.place(x=10,y=40)
E2=Entry(top, bd=5)
E2.place(x=80,y=40)

L3=Label(top,text="C")
L3.place(x=10,y=70)
E3=Entry(top, bd=5)
E3.place(x=80,y=70)

L4=Label(top,text="Linux")
L4.place(x=10,y=100)
E4=Entry(top, bd=5)
E4.place(x=80,y=100)

L5=Label(top,text="SMTH")
L5.place(x=10,y=130)
E5=Entry(top, bd=5)
E5.place(x=80,y=130)

L6=Label(top,text="Calculus")
L6.place(x=10,y=160)
E6=Entry(top, bd=5)
E6.place(x=80,y=160)

L7=Label(top,text="SMA")
L7.place(x=10,y=190)
E7=Entry(top, bd=5)
E7.place(x=80,y=190)

L8=Label(top,text="CE")
L8.place(x=10,y=220)
E8=Entry(top, bd=5)
E8.place(x=80,y=220)

L9=Label(top,text="GT")
L9.place(x=10,y=250)
E9=Entry(top, bd=5)
E9.place(x=80,y=250)

L10=Label(top,text="Marks")
L10.place(x=10,y=280)
E10=Entry(top, bd=5)
E10.place(x=80,y=280)

L11=Label(top,text="Percentage")
L11.place(x=10,y=310)
E11=Entry(top, bd=5)
E11.place(x=80,y=310)

L12=Label(top,text="Grade")
L12.place(x=10,y=340)
E12=Entry(top, bd=5)
E12.place(x=80,y=340)

E13=Label(top, text="Remarks")
E13.place(x=10,y=370)
E13=Entry(top, bd=5)
E13.place(x=80,y=370)

B=Button(top, text="Sum",bg="blue",fg="white",command=calculate_sum_and_grade)
B.place(x=370,y=370)

top.mainloop()
