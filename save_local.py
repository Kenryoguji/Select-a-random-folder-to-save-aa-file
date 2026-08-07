import csv
import time
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

screen = ctk.CTk()
screen.title ("Mon application")
screen.geometry ("400x400")

def save() :
    screen.withdraw()

    track = filedialog.askdirectory()

    line = Path(track)/"result"

    if line :
        with open (line , "w", newline= "", encoding= "utf-8") as my_file:
            file = csv.writer(my_file,delimiter=",")
            file.writerow (["N°","chiffre"])
            for i in range (10) :
                file.writerow([i,i])
        print (f"vous avez enregistré ca ici : {line}")
        
    screen.deiconify()

ask = ctk.CTkButton (screen,text ="Download",bg_color= "blue", text_color= "white",command = save)
ask.pack (side = "rigth", padx = 20 , pady = 20)
screen.mainloop()