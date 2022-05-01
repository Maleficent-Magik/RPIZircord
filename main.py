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
Dans la phrase, chaque lettre corresponds à un image. La phrase change et les lettres sont pas au meme emplacement...
'''


def trucChelou (letter):


    pathName = "./images/Letter/letter"+ letter +".png"
    canvas_firstletter.create_image(coord2[0], coord2[1], image=tk.PhotoImage(file=pathName))

    del coord2[0]
    print(coord2)
    del coord2[0]
    print(coord2)


for letter in PDJ:
    if letter.isupper() :
        trucChelou(letter)

    elif letter.islower() :
        x = letter.upper()
        trucChelou(x)

    elif letter.isspace() :
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
