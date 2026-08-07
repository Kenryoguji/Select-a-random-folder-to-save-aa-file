import csv # import csv Library
from pathlib import Path # Import Library Path for track
import tkinter as tk # Graphic Library
from tkinter import filedialog # windows dialog file

root = tk.Tk() # Create a window named root
root.withdraw() # cash the windows
dossier = filedialog.askdirectory(title = "Sélectionner un répertoire") 

if dossier : # si le répertoire est sélectionnée
    track = Path(dossier)/"donnes.csv" # On recupere le chemin du dossier sélectionné

    with open (track,"w",newline ="",encoding="utf-8") as f: # Création et ouverture du fichier f encoder en string en mode écriture
        ecrire = csv.writer (f,delimiter=",") # Variable d'écriture dans le fichier f avec pour delimiter de séparation du csv la ","

        # Remplissage des lignes
        ecrire.writerow(["Age","Nom","Ville"]) 
        ecrire.writerow([22,"Axel","Nancy"]) 
        ecrire.writerow([22,"Axel","Nancy"])

    print (f"fichier creer ici : {track}") #Affichage du chemin du fichier

else :
    print ("aucun dossier sélectionné")