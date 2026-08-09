import csv # library of csv file
import time # Command time
import customtkinter as ctk # Library windows
import tkinter as tk # Original window
from tkinter import filedialog # library do dialog with os file system
from pathlib import Path # Library track of file


screen = ctk.CTk() # main window
screen.title ("Mon application") # Title of window
screen.geometry ("400x400") # size of window in pixel 

entree = ctk.CTkEntry(screen,placeholder_text= "Inout a number between 1 and 100",fg_color= "white",text_color="black",width = 220 ,height= 50, corner_radius= 10)  # input section 
lab = ctk.CTkCheckBox (screen ,text= "save",bg_color= "cyan",text_color= "black",width = 5, height=5,corner_radius = 2) #checkBox section to configure save file or not

# Function to save csv file in folder that we want

def save() :
    verif = lab.get() # Take the value of checkBox lab , it's a boolean
    value = entree.get() # Take the value of the entry section , it's a string
    man = int (value) #convert the string to int type

    # if the checkbox is on
    if verif :
        screen.withdraw() #cash the main window
        track = filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("csv","*.csv")],initialfile= "result")# ask os directory fodlder and enter the name that we want to the file to save

        line = Path(track) # track of the save file

        # if the track is ok 
        if line :
            with open (line , "w", newline= "", encoding= "utf-8") as my_file: #create the csv file in writting mode 
                file = csv.writer(my_file,delimiter=",") #activate the writer function in csv
                file.writerow (["N°","chiffre"]) #write on the firts row of csv

                # write the number of row corresponding of the int value that we enter on the entry sexion
                for i in range (man) :
                    file.writerow([i,i])
            print (f"vous avez enregistré ca ici : {line}") #write the track of save file

        #Delate the dialog file name window
        screen.deiconify()
    else :
        pass

ask = ctk.CTkButton (screen,text ="Download",bg_color= "blue", text_color= "white",command = save)# create button to validate a save

entree.pack (side="right", padx=30,pady=40,anchor = "w") # organize the entry sexion
ask.pack (side = "right", padx=20 , pady=20) # organize the Button sexion
lab.pack (side = "right", padx=20 , pady=20) # organize the checkBox sexion

screen.mainloop() #Make the window run continuous