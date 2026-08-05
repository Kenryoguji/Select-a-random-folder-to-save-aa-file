import csv # import csv Library
from pathlib import Path # Import Library Path for track
import tkinter as tk # Graphicd Library
from tkinter import filedialog # windows dialog file

root = tk.Tk() # Create a window named root
root.withdraw() # cash the windows
dossier = filedialog.askdirectory(title = "Sélectionner un répertoire") 

if dossier :
    track = Path(dossier)/"données.csv"

    with open (track,"w",newline ="",encoding="utf-8") as f:
        ecrire = csv.writer (f,delimiter=",")
        ecrire.writerow(["Age","Nom","Ville"])
        ecrire.writerow([22,"Axel","Nancy"])
        ecrire.writerow([22,"Axel","Nancy"])

    print (f"fichier creer ici : {track}")

else :
    print ("aucun dossier sélectionné")