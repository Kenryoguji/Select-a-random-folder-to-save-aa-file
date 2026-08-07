import csv
import time
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

screen = ctk.CTk()
screen.title ("Mon application")
screen.geometry ("400x400")

entree = ctk.CTkEntry(screen,placeholder_text= "Inout a number between 1 and 100",fg_color= "white",text_color="black",width = 220 ,height= 50, corner_radius= 10)

def save() :
    value = entree.get()
    man = int (value)
    screen.withdraw()
    track = filedialog.askdirectory()

    line = Path(track)/"result.csv"
    if line :
        with open (line , "w", newline= "", encoding= "utf-8") as my_file:
            file = csv.writer(my_file,delimiter=",")
            file.writerow (["N°","chiffre"])
            for i in range (man) :
                file.writerow([i,i])
        print (f"vous avez enregistré ca ici : {line}")
        
    screen.deiconify()

ask = ctk.CTkButton (screen,text ="Download",bg_color= "blue", text_color= "white",command = save)

entree.pack (side="right", padx=30,pady=40)
ask.pack (side = "right", padx=20 , pady=20)

screen.mainloop()