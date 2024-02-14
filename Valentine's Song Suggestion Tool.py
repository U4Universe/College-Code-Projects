#To create an output window where the song suggestions will be displayed, you need to define the `suggest_songs()` function correctly. In your code, the function already creates a Toplevel window (`output_window`) to display the song suggestions.
import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton, messagebox

window = tk.Tk()
window.title ("Valentine's Day Song Suggestion 2024")
window.configure(bg="#e38f9c")

label = tk.Label(window, text="Valentine's Day Song Suggestion",bg="#E38F9C",fg="#f01a3b",font="Verdana 24 bold")
label.grid(row = 0, columnspan = 5)

def suggest_songs():
    name = E1.get()
    age = E2.get()
    genre = E3.get()
    gender = gender.get()
    relationship_status = relationship_var.get()

    if not name or not age or not genre or not relationship_status:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    song_suggestions = {
        "Single": {
            "Pop": ["Shake It Off by Taylor Swift", "A Sky Full of Stars by Coldplay","7 Rings by Ariana Grande","Independent Women Pt. I by Destiny's Child"],
            "Rock": ["I Wanna Dance With Somebody (Who Loves Me) by Whitney Houston", "Livin' on a Prayer by Bon Jovi","Stronger by Kanye West","I'm Still Standing by Elton John"],
            "RnB": ["Single Ladies (Put a Ring On It) by Beyoncé", "Cupid (English Version) by Fifty Fifty","Survivor by Destiny's Child","R.E.S.P.E.C.T. by Aretha Franklin"],
        },
        "Dating": {
            "Pop": ["Can't Help Falling in Love by Elvis Presley", "Shape of You by Ed Sheeran","Lover by Taylor Swift","Just the Way You Are by Bruno Mars"],
            "Rock": ["Sweet Child o' Mine by Guns N' Roses", "Paradise City by Guns N' Roses","I Want to Hold Your Hand by The Beatles","I Will Follow You into the Dark by Death Cab for Cutie"],
            "RnB": ["Crazy in Love by Beyoncé ft. Jay-Z", "Let's Stay Together by Al Green","Thinkin Bout You by Frank Ocean","Adore You by Harry Styles"],
        },
        "Married": {
            "Pop": ["All of Me by John Legend", "Perfect by ED Sheeran","You Are the Best Thing by Ray LaMontagne","Marry Me by Train"],
            "Rock": ["Something by The Beatles", "More Than Words by Extreme","I'll Be There for You by Bon Jovi","Sweet Child o' Mine by Guns N' Roses"],
            "RnB": ["Best Part by H.E.R. ft. Daniel Caesar","If I Ain't Got You by Alicia Keys","You Are My Lady by Freddie Jackson","Always and Forever by Heatwave"],
        },
         "It's Complicated": {
            "Pop": ["Someone You Loved by Lewis Capaldi", "Happier by Marshmello ft. Bastille","Without Me by Halsey","Sorry by Justin Beiber"],
            "Rock": ["Don't Speak by No Doubt", "Zombie by The Cranberries","I Will Always Love You by Whitney Houston","November Rain by Guns N' Roses"],
            "RnB": ["Ex Factor by Lauryn Hill", "Say My Name by Destiny's Child","End of the Road by Boyz II Men","We Can't Be Friends by Deborah Cox ft. R.L."],
        },
    }

    suggestions = song_suggestions[relationship_status][genre]

    # Create output window with title and greeting
    output_window = tk.Toplevel(window)
    output_window.title("Valentine's Day Song Suggestions for " + name)
    greeting_label = tk.Label(output_window, text="Hey " + name + ", here are some song suggestions for your Valentine's Day 2024:")
    greeting_label.pack()


    # Improved song list with formatting and scrolling
    song_list = tk.Listbox(output_window, borderwidth=2, relief="ridge", highlightthickness=0,
                          font=("Courier New", 12), selectmode=tk.SINGLE)
    for song in suggestions:
        song_list.insert(tk.END, song)
    song_list.pack(expand=True, fill="both")

    # Close button with centered placement
    close_button = tk.Button(output_window, text="Close", command=output_window.destroy)
    close_button.pack(pady=10, padx=10)


#creating the label and entry fields
L1=Label(window, text="Name:", bg="#e38f9c", fg="White", font="monospace 14 bold")
L1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
E1=Entry(window, bd=5, width=30)
E1.grid(row = 1, column = 1, padx=10, pady=10, sticky="w")

L2=Label(window, text="Age:", bg="#e38f9c", fg="White", font="monospace 14 bold")
L2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
E2=Entry(window, bd=5, width=30)
E2.grid(row = 2, column = 1, padx=10, pady=10, sticky="w")

L3=Label(window, text="Genre:",bg="#e38f9c", fg="White", font="monospace 14 bold")
L3.grid(row=3, column=0, padx=10, pady=10, sticky="w")
E3=Entry(window, bd=5, width=30)
E3.grid(row = 3, column = 1, padx=10, pady=10, sticky="w")

L4=Label(window, text="Gender:",bg="#e38f9c", fg="White", font="monospace 14 bold")
L4.grid(row=4, column=0, padx=10, pady=10, sticky="w")

def gender_selection():
    selected_gender = gender.get()
    if selected_gender == 1:
        selected_text = "Male"
    elif selected_gender == 2:
        selected_text = "Female"
    else:
        selected_text = "Other"
gender = tk.IntVar()
Radiobutton(window ,text="Male",variable=gender,value = 1,bg='#e38f9c',font="Arial 11",command=gender_selection()).grid(row=5,column=1,sticky="w")
Radiobutton(window ,text="Female",variable=gender,value = 2,bg='#e38f9c',font="Arial 11",command=gender_selection()).grid(row=6,column=1,sticky="w")
Radiobutton(window ,text="Other",variable=gender,value = 3,bg='#e38f9c',font="Arial 11",command=gender_selection()).grid(row=7,column=1,sticky="w")

L5=Label(window, text="Relationship Status:",bg="#e38f9c", fg="White", font="monospace 14 bold")
L5.grid(row=8, column=0, padx=10, pady=10, sticky="w")

relationship_var = tk.StringVar(window)
relationship_var.set("Single")
relationship_dropdown = tk.OptionMenu(window,relationship_var, "Single", "Dating", "Married", "It's Complicated")
relationship_dropdown.config(bg="#f12746", fg="White")
relationship_dropdown.grid(row=8, column=1, padx=10, pady=10, sticky="w")

#suggest songs button
suggest_button = Button(window, text="Suggest Song", font="monospace 12 bold", bg="#f01a3b", fg="white",command=suggest_songs)
suggest_button.grid(row=20, columnspan=3, padx=10, pady=10)

window.mainloop()











