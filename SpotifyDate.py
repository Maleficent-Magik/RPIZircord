import time
import tkinter as tk  # Import pour la fênetre et la mise en oeuvre de l'app -> Tout prog
import pyglet as customfont  # Import pour une police customisé -> Ligne 71, 289
from datetime import date, datetime  # Import pour la date -> Ligne 77, 83

root = tk.Tk()  # Init Tkinter
root.attributes('-fullscreen', True)  # Fullscreen obligatoire
root['background'] = '#c9c9c9'  # couleur du fond

# SCREENINFO
rootheight = root.winfo_screenheight()  # taille de ton écran
rootwidth = root.winfo_screenwidth()  # taille de ton écran
print("width x height = %d x %d (in pixels)\n" % (rootwidth, rootheight))  # Print
##


# Images
photoredcross = tk.PhotoImage(file="./images/redcross.png")
smaller_imageredcross = photoredcross.subsample(10, 10)
Spotify = tk.PhotoImage(file="./images/Spotify_App_Logo.png")
smaller_imageSpotify = Spotify.subsample(20, 20)
LetterA = tk.PhotoImage(file="./images/Letter/letterA.png")
number0 = tk.PhotoImage(file="./images/number/0.png")
number1 = tk.PhotoImage(file="./images/number/1.png")
number2 = tk.PhotoImage(file="./images/number/2.png")
number3 = tk.PhotoImage(file="./images/number/3.png")
number4 = tk.PhotoImage(file="./images/number/4.png")
number5 = tk.PhotoImage(file="./images/number/5.png")
number6 = tk.PhotoImage(file="./images/number/6.png")
number7 = tk.PhotoImage(file="./images/number/7.png")
number8 = tk.PhotoImage(file="./images/number/8.png")
number9 = tk.PhotoImage(file="./images/number/9.png")
deuxpoints = tk.PhotoImage(file="./images/number/deuxpoints.png")
void = tk.PhotoImage(file="./images/number/void.png")
debughelp = tk.PhotoImage(file="./images/number/debugvoid.png")

# FONT
print("Adding CustomFont . . .")
customfont.font.add_file("./custfont/Papernotes.otf")  # Ajout de la police custom
#

# Hours
recuphours = time.strftime("%H %M")
print(recuphours)
test = ([recuphours[0], recuphours[1], recuphours[3], recuphours[4]])
hours = [int(i) for i in test]

# Day
today = date.today()
canvas_day = tk.Canvas(root, width=1000, height=1000)  # Dessine une fenetre/canvas
canvas_day.pack(anchor=tk.NW)
canvas_day.place(x=0, y=10, anchor=tk.NW)
canvas_day.create_rectangle(0, 0, 260, 50, fill='white')
canvas_day['background'] = '#c9c9c9'
dayaffiche = today.strftime("%d, %B, %Y")
print(dayaffiche)
canvas_day.create_text(0, 0, text=dayaffiche, fill="black", font=("Arial", 30), anchor=tk.NW)
#

canvas_firstletter = tk.Canvas(root, width=rootwidth, height=rootheight)
canvas_firstletter.pack(anchor=tk.CENTER)
canvas_firstletter.place(x=rootwidth // 2, y=rootheight // 2, anchor=tk.CENTER)
canvas_firstletter['background'] = '#c9c9c9'
for i in range(1):

    if hours[0] == 0:
        canvas_firstletter.create_image(150, 200, image=number0)
    elif hours[0] == 1:
        canvas_firstletter.create_image(150, 200, image=number1)
    elif hours[0] == 2:
        canvas_firstletter.create_image(150, 200, image=number2)
    elif hours[0] == 3:
        canvas_firstletter.create_image(150, 200, image=number3)
    elif hours[0] == 4:
        canvas_firstletter.create_image(150, 200, image=number4)
    elif hours[0] == 5:
        canvas_firstletter.create_image(150, 200, image=number5)
    elif hours[0] == 6:
        canvas_firstletter.create_image(150, 200, image=number6)
    elif hours[0] == 7:
        canvas_firstletter.create_image(150, 200, image=number7)
    elif hours[0] == 8:
        canvas_firstletter.create_image(150, 200, image=number8)
    elif hours[0] == 9:
        canvas_firstletter.create_image(150, 200, image=number9)

    if hours[1] == 0:
        canvas_firstletter.create_image(250, 200, image=number0)
    elif hours[1] == 1:
        canvas_firstletter.create_image(250, 200, image=number1)
    elif hours[1] == 2:
        canvas_firstletter.create_image(250, 200, image=number2)
    elif hours[1] == 3:
        canvas_firstletter.create_image(250, 200, image=number3)
    elif hours[1] == 4:
        canvas_firstletter.create_image(250, 200, image=number4)
    elif hours[1] == 5:
        canvas_firstletter.create_image(250, 200, image=number5)
    elif hours[1] == 6:
        canvas_firstletter.create_image(250, 200, image=number6)
    elif hours[1] == 7:
        canvas_firstletter.create_image(250, 200, image=number7)
    elif hours[1] == 8:
        canvas_firstletter.create_image(250, 200, image=number8)
    elif hours[1] == 9:
        canvas_firstletter.create_image(250, 200, image=number9)

    if hours[2] == 0:
        canvas_firstletter.create_image(600, 200, image=number0)
    elif hours[2] == 1:
        canvas_firstletter.create_image(600, 200, image=number1)
    elif hours[2] == 2:
        canvas_firstletter.create_image(600, 200, image=number2)
    elif hours[2] == 3:
        canvas_firstletter.create_image(600, 200, image=number3)
    elif hours[2] == 4:
        canvas_firstletter.create_image(600, 200, image=number4)
    elif hours[2] == 5:
        canvas_firstletter.create_image(600, 200, image=number5)
    elif hours[2] == 6:
        canvas_firstletter.create_image(600, 200, image=number6)
    elif hours[2] == 7:
        canvas_firstletter.create_image(600, 200, image=number7)
    elif hours[2] == 8:
        canvas_firstletter.create_image(600, 200, image=number8)
    elif hours[2] == 9:
        canvas_firstletter.create_image(600, 200, image=number9)

    if hours[3] == 0:
        canvas_firstletter.create_image(700, 200, image=number0)
    elif hours[3] == 1:
        canvas_firstletter.create_image(700, 200, image=number1)
    elif hours[3] == 2:
        canvas_firstletter.create_image(700, 200, image=number2)
    elif hours[3] == 3:
        canvas_firstletter.create_image(700, 200, image=number3)
    elif hours[3] == 4:
        canvas_firstletter.create_image(700, 200, image=number4)
    elif hours[3] == 5:
        canvas_firstletter.create_image(700, 200, image=number5)
    elif hours[3] == 6:
        canvas_firstletter.create_image(700, 200, image=number6)
    elif hours[3] == 7:
        canvas_firstletter.create_image(700, 200, image=number7)
    elif hours[3] == 8:
        canvas_firstletter.create_image(700, 200, image=number8)
    elif hours[3] == 9:
        canvas_firstletter.create_image(700, 200, image=number9)

canvas_firstletter.create_image(420, 200, image=deuxpoints)


def clock():
    recuphours = time.strftime("%H %M")
    print(recuphours)
    test = ([recuphours[0], recuphours[1], recuphours[3], recuphours[4]])
    hours = [int(i) for i in test]

    for _ in hours:
        canvas_firstletter.create_image(150, 200, image=void)
        if hours[0] == 0:
            canvas_firstletter.create_image(150, 200, image=number0)
        elif hours[0] == 1:
            canvas_firstletter.create_image(150, 200, image=number1)
        elif hours[0] == 2:
            canvas_firstletter.create_image(150, 200, image=number2)
        elif hours[0] == 3:
            canvas_firstletter.create_image(150, 200, image=number3)
        elif hours[0] == 4:
            canvas_firstletter.create_image(150, 200, image=number4)
        elif hours[0] == 5:
            canvas_firstletter.create_image(150, 200, image=number5)
        elif hours[0] == 6:
            canvas_firstletter.create_image(150, 200, image=number6)
        elif hours[0] == 7:
            canvas_firstletter.create_image(150, 200, image=number7)
        elif hours[0] == 8:
            canvas_firstletter.create_image(150, 200, image=number8)
        elif hours[0] == 9:
            canvas_firstletter.create_image(150, 200, image=number9)

    for i in hours:
        canvas_firstletter.create_image(300, 200, image=void)

        if hours[1] == 0:
            canvas_firstletter.create_image(250, 200, image=number0)
        elif hours[1] == 1:
            canvas_firstletter.create_image(250, 200, image=number1)
        elif hours[1] == 2:
            canvas_firstletter.create_image(250, 200, image=number2)
        elif hours[1] == 3:
            canvas_firstletter.create_image(250, 200, image=number3)
        elif hours[1] == 4:
            canvas_firstletter.create_image(250, 200, image=number4)
        elif hours[1] == 5:
            canvas_firstletter.create_image(250, 200, image=number5)
        elif hours[1] == 6:
            canvas_firstletter.create_image(250, 200, image=number6)
        elif hours[1] == 7:
            canvas_firstletter.create_image(250, 200, image=number7)
        elif hours[1] == 8:
            canvas_firstletter.create_image(250, 200, image=number8)
        elif hours[1] == 9:
            canvas_firstletter.create_image(250, 200, image=number9)

    canvas_firstletter.create_image(420, 200, image=deuxpoints)

    for i in hours:
        canvas_firstletter.create_image(600, 200, image=void)

        if hours[2] == 0:
            canvas_firstletter.create_image(600, 200, image=number0)
        elif hours[2] == 1:
            canvas_firstletter.create_image(600, 200, image=number1)
        elif hours[2] == 2:
            canvas_firstletter.create_image(600, 200, image=number2)
        elif hours[2] == 3:
            canvas_firstletter.create_image(600, 200, image=number3)
        elif hours[2] == 4:
            canvas_firstletter.create_image(600, 200, image=number4)
        elif hours[2] == 5:
            canvas_firstletter.create_image(600, 200, image=number5)
        elif hours[2] == 6:
            canvas_firstletter.create_image(600, 200, image=number6)
        elif hours[2] == 7:
            canvas_firstletter.create_image(600, 200, image=number7)
        elif hours[2] == 8:
            canvas_firstletter.create_image(600, 200, image=number8)
        elif hours[2] == 9:
            canvas_firstletter.create_image(600, 200, image=number9)

    for i in hours:
        canvas_firstletter.create_image(750, 200, image=void)
        if hours[3] == 0:
            canvas_firstletter.create_image(700, 200, image=number0)
        elif hours[3] == 1:
            canvas_firstletter.create_image(700, 200, image=number1)
        elif hours[3] == 2:
            canvas_firstletter.create_image(700, 200, image=number2)
        elif hours[3] == 3:
            canvas_firstletter.create_image(700, 200, image=number3)
        elif hours[3] == 4:
            canvas_firstletter.create_image(700, 200, image=number4)
        elif hours[3] == 5:
            canvas_firstletter.create_image(700, 200, image=number5)
        elif hours[3] == 6:
            canvas_firstletter.create_image(700, 200, image=number6)
        elif hours[3] == 7:
            canvas_firstletter.create_image(700, 200, image=number7)
        elif hours[3] == 8:
            canvas_firstletter.create_image(700, 200, image=number8)
        elif hours[3] == 9:
            canvas_firstletter.create_image(700, 200, image=number9)

    root.after(100, clock)


# Spotify
canvasSpotify = tk.Canvas(root, width=480, height=180)
canvasSpotify.pack(anchor=tk.SW)
canvasSpotify.place(x=-5, y=rootheight, anchor=tk.SW)
canvasSpotify.create_rectangle(96, 180, 400, 140, fill='grey')
# canvasSpotify.create_text(100, 200, text=musicprinter(), fill="black", font=('Papernotes', 30), anchor=tk.SW)
canvasSpotify.create_text(100, 180, text="test", fill="black", font=('Papernotes', 30), anchor=tk.SW)
canvasSpotify.create_image(42, 130, image=smaller_imageSpotify)
canvasSpotify['background'] = '#c9c9c9'

tk.Button(root, image=smaller_imageredcross, command=root.destroy).pack(padx=1, pady=1,
                                                                        anchor=tk.NE)  # Bouton pour quitter
clock()
root.mainloop()
