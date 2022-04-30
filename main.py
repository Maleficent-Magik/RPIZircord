import sys #Import pour quitter le programme avant l'appelle de Tkinter -> Ligne 14
import tkinter as tk #Import pour la fênetre et la mise en oeuvre de l'app -> Tout prog
import pyglet as customfont #Import pour une police customisé -> Ligne 71, 289
from datetime import date #Import pour la date -> Ligne 77, 83
#from MusicEcouteSpotify import musicprinter #Import pour afficher le titre en cours de diffusion sur Spotify -> Ligne 288

PDJ = input("Phrase du jour?")
if PDJ: #??
    if len(PDJ) <= 30: #calcul du nombre de caractères si ça passe sera recalculé à l'alpha
        print(PDJ)
else:
    print("ERROR. Phrase du jour invalide.")
    sys.exit() #Programme quitté avant Tkinter

root = tk.Tk() #Init Tkinter
root.attributes('-fullscreen', True) #Fullscreen obligatoire
root['background'] = '#c9c9c9' #couleur du fond

# SCREENINFO
rootheight = root.winfo_screenheight() #taille de ton écran
rootwidth = root.winfo_screenwidth() #taille de ton écran
print("width x height = %d x %d (in pixels)\n" % (rootwidth, rootheight)) #Print
##

# Coord
coord2 = [296, 100, 350, 100, 400, 100, 450, 100, 500, 100, 550, 100, 600, 100, 650, 100, 700, 100, 750, 100, 800, 100,
          850, 100, 900, 100, 950, 100, 1000, 100, 1050, 100, 1100, 100, 1150, 100, 1200, 100, 1250, 100, 1300, 100,
          1350, 100, 1400, 100, 1450, 100, 1500, 100,
          400, 300, 450, 300, 500, 300, 550, 300, 600, 300, 650, 300, 700, 300,
          750, 300, 800, 300, 850, 300, 900, 300, 950, 300, 1000, 300, 1050, 300, 1100, 300, 1150, 300, 1200, 300, 1250,
          300, 1300, 300, 1350, 300,
          500, 500, 550, 500, 600, 500, 650, 500, 700, 500, 750, 500, 800, 500, 850, 500, 900, 500, 950, 500, 1000, 500,
          1050, 500, 1100, 500, 1150, 500]
#

#Images
photoredcross = tk.PhotoImage(file="./images/redcross.png")
smaller_imageredcross = photoredcross.subsample(10, 10)
Spotify = tk.PhotoImage(file="./images/Spotify_App_Logo.png")
smaller_imageSpotify = Spotify.subsample(10, 10)
LetterA = tk.PhotoImage(file="./images/Letter/letterA.png")
LetterB = tk.PhotoImage(file="./images/Letter/letterB.png")
LetterC = tk.PhotoImage(file="./images/Letter/letterC.png")
LetterD = tk.PhotoImage(file="./images/Letter/letterD.png")
LetterE = tk.PhotoImage(file="./images/Letter/letterE.png")
LetterF = tk.PhotoImage(file="./images/Letter/letterF.png")
LetterG = tk.PhotoImage(file="./images/Letter/letterG.png")
LetterH = tk.PhotoImage(file="./images/Letter/letterH.png")
LetterI = tk.PhotoImage(file="./images/Letter/letterI.png")
LetterJ = tk.PhotoImage(file="./images/Letter/letterJ.png")
LetterK = tk.PhotoImage(file="./images/Letter/letterK.png")
LetterL = tk.PhotoImage(file="./images/Letter/letterL.png")
LetterM = tk.PhotoImage(file="./images/Letter/letterM.png")
LetterN = tk.PhotoImage(file="./images/Letter/letterN.png")
LetterO = tk.PhotoImage(file="./images/Letter/letterO.png")
LetterP = tk.PhotoImage(file="./images/Letter/letterP.png")
LetterQ = tk.PhotoImage(file="./images/Letter/letterQ.png")
LetterR = tk.PhotoImage(file="./images/Letter/letterR.png")
LetterS = tk.PhotoImage(file="./images/Letter/letterS.png")
LetterT = tk.PhotoImage(file="./images/Letter/letterT.png")
LetterU = tk.PhotoImage(file="./images/Letter/letterU.png")
LetterV = tk.PhotoImage(file="./images/Letter/letterV.png")
LetterW = tk.PhotoImage(file="./images/Letter/letterW.png")
LetterX = tk.PhotoImage(file="./images/Letter/letterX.png")
LetterY = tk.PhotoImage(file="./images/Letter/letterY.png")
LetterZ = tk.PhotoImage(file="./images/Letter/letterZ.png")

# FONT
print("Adding CustomFont . . .")
customfont.font.add_file("./custfont/Papernotes.otf") #Ajout de la police custom
#

tk.Button(root, image=smaller_imageredcross, command=root.destroy).pack(padx=1, pady=1, anchor=tk.NE) #Bouton pour quitter

# Day
today = date.today()
canvas_day = tk.Canvas(root, width=1000, height=1000) #Dessine une fenetre/canvas
canvas_day.pack(anchor=tk.NW)
canvas_day.place(x=0, y=10, anchor=tk.NW)
canvas_day.create_rectangle(0, 0, 260, 50, fill='white')
canvas_day['background'] = '#c9c9c9'
dayaffiche = today.strftime("%d, %B, %Y")
print(dayaffiche)
canvas_day.create_text(0, 0, text=dayaffiche, fill="black", font=("Arial", 30), anchor=tk.NW)
#

# FirstLetter
canvas_firstletter = tk.Canvas(root, width=rootwidth, height=rootheight - 400)
canvas_firstletter.pack(anchor=tk.CENTER)
canvas_firstletter.place(x=rootwidth // 2, y=rootheight // 2, anchor=tk.CENTER)
canvas_firstletter['background'] = '#c9c9c9'
#
'''

CECI ETAIT LORS DES TESTS. PEUT ETRE DELETE.

# CanvasCreate
canvas_firstletter.create_rectangle(200, 0, 400, 200, fill='black')
canvas_firstletter.create_rectangle(400, 0, 600, 200, fill='red')
canvas_firstletter.create_rectangle(600, 0, 800, 200, fill='yellow')
canvas_firstletter.create_rectangle(800, 0, 1000, 200, fill='green')
canvas_firstletter.create_rectangle(1000, 0, 1200, 200, fill='blue')
canvas_firstletter.create_rectangle(1200, 0, 1400, 200, fill='brown')
canvas_firstletter.create_rectangle(1400, 0, 1600, 200, fill='black')
canvas_firstletter.create_rectangle(1600, 0, 1800, 200, fill='cyan')
canvas_firstletter.create_rectangle(400, 200, 600, 400, fill='pink')
canvas_firstletter.create_rectangle(600, 200, 800, 400, fill='green')
canvas_firstletter.create_rectangle(800, 200, 1000, 400, fill='maroon')
canvas_firstletter.create_rectangle(1000, 200, 1400, 400, fill='green')
canvas_firstletter.create_rectangle(1200, 200, 1400, 400, fill='orange')
canvas_firstletter.create_rectangle(1400, 200, 1600, 400, fill='navyblue')
canvas_firstletter.create_rectangle(600, 400, 800, 600, fill='brown')
canvas_firstletter.create_rectangle(800, 400, 1000, 600, fill='orange')
canvas_firstletter.create_rectangle(1000, 400, 1200, 600, fill='red')
canvas_firstletter.create_rectangle(1200, 400, 1400, 600, fill='blue')
'''


'''
Dans la phrase, chaque lettre corresponds à un image. La phrase change et les lettres sont pas au meme emplacement...
'''
for letter in PDJ:
    print(letter)

    if letter == "A" or letter == "a":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterA)
        canvas_firstletter['background'] = '#c9c9c9'
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "B" or letter == "b":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterB)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "C" or letter == "c":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterC)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "D" or letter == "d":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterD)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "E" or letter == "e":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterE)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "F" or letter == "f":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterF)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "G" or letter == "g":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterG)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "H" or letter == "h":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterH)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "I" or letter == "i":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterI)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "J" or letter == "j":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterJ)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "K" or letter == "k":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterK)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "L" or letter == "l":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterL)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "M" or letter == "m":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterM)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "N" or letter == "n":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterN)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "O" or letter == "o":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterO)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "P" or letter == "p":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterP)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "Q" or letter == "q":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterQ)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "R" or letter == "r":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterR)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "S" or letter == "s":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterS)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "T" or letter == "t":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterT)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "U" or letter == "u":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterU)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "V" or letter == "v":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterV)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "W" or letter == "w":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterW)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "X" or letter == "x":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterX)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "Y" or letter == "y":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterY)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == "Z" or letter == "z":
        canvas_firstletter.create_image(coord2[0], coord2[1], image=LetterZ)
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    elif letter == " ":
        del coord2[0]
        print(coord2)
        del coord2[0]
        print(coord2)
    else:
        print("Root")

# Spotify
canvasSpotify = tk.Canvas(root, width=1200, height=300)
canvasSpotify.pack(anchor=tk.SW)
canvasSpotify.place(x=-2, y=rootheight + 102, anchor=tk.SW)
canvasSpotify.create_rectangle(203, 210, rootwidth - 600, 150, fill='grey')
# canvasSpotify.create_text(203, 200, text=musicprinter(), fill="black", font=('Papernotes', 30), anchor=tk.SW)
canvasSpotify.create_image(100, 100, image=smaller_imageSpotify)
canvasSpotify['background'] = '#c9c9c9'
#

root.mainloop()
