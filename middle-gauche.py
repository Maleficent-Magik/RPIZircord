import sys  # Import pour quitter le programme avant l'appelle de Tkinter -> Ligne 14
import tkinter as tk  # Import pour la fênetre et la mise en oeuvre de l'app -> Tout prog
import pyglet as customfont  # Import pour une police customisé -> Ligne 71, 289

PDJ = "#Forever"
nbl = len(PDJ)
print(nbl)

root = tk.Tk()  # Init Tkinter
root.attributes('-fullscreen', True)  # Fullscreen obligatoire
root['background'] = '#c9c9c9'  # couleur du fond

rootheight = root.winfo_screenheight()  # taille de ton écran
rootwidth = root.winfo_screenwidth()  # taille de ton écran

# FONT
print("Adding CustomFont . . .")
customfont.font.add_file("./custfont/Papernotes.otf")  # Ajout de la police custom
#
photoredcross = tk.PhotoImage(file="./images/redcross.png")
smaller_imageredcross = photoredcross.subsample(10, 10)


# FirstLetter
canvas_firstletter = tk.Canvas(root, width=rootwidth, height=rootheight)
canvas_firstletter.pack(anchor=tk.CENTER)
canvas_firstletter.place(x=rootwidth // 2, y=rootheight // 2, anchor=tk.CENTER)
canvas_firstletter['background'] = '#c9c9c9'

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
LetterHastag = tk.PhotoImage(file="./images/Letter/hastag.png")

if nbl == 1:
    coord1 = [380, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 2:
    coord1 = [335, 250, 380, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 3:
    coord1 = [335, 250, 380, 250, 425, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 4:
    coord1 = [290, 250, 335, 250, 380, 250, 425, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 5:
    coord1 = [290, 250, 335, 250, 380, 250, 425, 250, 470, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 6:
    coord1 = [245, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 7:
    coord1 = [245, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 8:
    coord1 = [200, 250, 245, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 9:
    coord1 = [200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 10:
    coord1 = [155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 11:
    coord1 = [155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560, 250, 605, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 12:
    coord1 = [110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560, 250, 605,
              250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 12:
    coord1 = [110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560, 250, 605,
              250, 650, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 13:
    coord1 = [70, 250, 110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560,
              250, 605, 250, 650, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 14:
    coord1 = [70, 250, 110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515, 250, 560,
              250, 605, 250, 650, 250, 695, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 15:
    coord1 = [20, 250, 70, 250, 110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515,
              250, 560, 250, 605, 250, 650, 250, 695, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 16:
    coord1 = [20, 250, 70, 250, 110, 250, 155, 250, 200, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470, 250, 515,
              250, 560, 250, 605, 250, 650, 250, 695, 250, 740, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 17:
    coord1 = [20, 250, 70, 250, 110, 250, 155, 250, 200, 250, 245, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470,
              250, 515, 250, 560, 250, 605, 250, 650, 250, 695, 250, 740, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")

if nbl == 18:
    coord1 = [20, 250, 70, 250, 110, 250, 155, 250, 200, 250, 245, 250, 290, 250, 335, 250, 380, 250, 425, 250, 470,
              250, 515, 250, 560, 250, 605, 250, 650, 250, 695, 250, 740, 250, 785, 250]
    for letter in PDJ:
        print(letter)
        if letter == "A" or letter == "a":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterA)
            # canvas_firstletter['background'] = '#c9c9c9'
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "B" or letter == "b":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterB)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "C" or letter == "c":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterC)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "D" or letter == "d":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterD)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "E" or letter == "e":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterE)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "F" or letter == "f":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterF)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "G" or letter == "g":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterG)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "H" or letter == "h":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterH)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "I" or letter == "i":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterI)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "J" or letter == "j":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterJ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "K" or letter == "k":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterK)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "L" or letter == "l":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterL)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "M" or letter == "m":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterM)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "N" or letter == "n":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterN)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "O" or letter == "o":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterO)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "P" or letter == "p":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterP)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Q" or letter == "q":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterQ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "R" or letter == "r":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterR)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "S" or letter == "s":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterS)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "T" or letter == "t":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterT)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "U" or letter == "u":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterU)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "V" or letter == "v":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterV)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "W" or letter == "w":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterW)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "X" or letter == "x":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterX)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Y" or letter == "y":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterY)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == "Z" or letter == "z":
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterZ)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == str("#"):
            canvas_firstletter.create_image(coord1[0], coord1[1], image=LetterHastag)
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)
        elif letter == " ":
            del coord1[0]
            print(coord1)
            del coord1[0]
            print(coord1)

        else:
            print("Root")
tk.Button(root, image=smaller_imageredcross, command=root.destroy).pack(ipadx=1, ipady=1, anchor=tk.NE)  # Bouton pour quitter

root.mainloop()
