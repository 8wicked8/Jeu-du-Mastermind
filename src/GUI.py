from tkinter import *
import Constante
import Mastermind

solution = []
propositionsEvaluees = []

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()

#----------------------------------------------------
def traduireCouleurFrVersAng(couleur):
        return Constante.traductionCouleursFrVersAng[couleur]

#----------------------------------------------------
def traduireCouleurAngVersFr(couleur):
        return Constante.traductionCouleursAngVersFr[couleur]

#----------------------------------------------------
def afficherProposition(canvas, proposition, positionX, positionY, diametre, intervalle):
    for i in range(0, len(proposition)):
        x = positionX + i * (diametre + intervalle)
        canvas.create_oval(x, positionY, x+diametre, positionY+diametre, fill=proposition[i])

#----------------------------------------------------
def afficherEvaluation(canvas, evaluation, positionX, positionY, diametre, intervalle):
    x = positionX

    for i in range(0, evaluation[0]):
        canvas.create_oval(x, positionY, x+diametre, positionY+diametre, fill='black')
        x = x + diametre + intervalle
 
    for i in range(0, evaluation[1]):
        canvas.create_oval(x, positionY, x+diametre, positionY+diametre, fill='white')
        x = x + diametre + intervalle
       
#----------------------------------------------------
def afficherLigne(canvas, proposition, evaluation, positionX, positionY):
    afficherProposition(canvas, proposition, positionX, positionY, 20, 10)
    afficherEvaluation(canvas, evaluation, positionX + len(proposition) * 30 + 20, positionY+5, 10, 5)

#----------------------------------------------------
def afficherHistorique(canvas, propositionsEvaluees):
    y = 100
    for i in range(0, len(propositionsEvaluees)):
        proposition = propositionsEvaluees[i][0]
        evaluation = propositionsEvaluees[i][1]
        afficherLigne(canvas, proposition, evaluation, 100, y)
        y = y + 30

#----------------------------------------------------
def afficherCapture(canvas, positionX, positionY, taille, diametre, intervalle):
    for i in range(0, taille):
        x = positionX + i * (diametre + intervalle)
        canvas.create_oval(x, positionY, x+diametre, positionY+diametre, fill='grey', tags='pion_' + str(i))

    boutonOk = Button(root, text="OK", command = boutonOkClique)
    canvas.create_window(positionX + (taille + 1) * (diametre + intervalle), positionY - 2, anchor=NW, window=boutonOk)

#----------------------------------------------------
def boutonOkClique():
    proposition = []

    for i in range(0, 6):
        items = canvas.find_withtag("pion_" + str(i))
        if len(items) > 0:    
            couleur = canvas.itemcget(items[0], "fill")
            proposition.append(couleur)

    evaluation = Mastermind.evaluer(proposition, solution)

    propositionsEvaluees.append([proposition, evaluation])

    canvas.delete("all")
    afficherHistorique(canvas, propositionsEvaluees)
    afficherCapture(canvas, 100, 410, 5, 20, 10)

#----------------------------------------------------
def prochaineCouleur(couleur):
    prochaine = Constante.COULEURS_ANG[0]

    for i in range(0, len(Constante.COULEURS_ANG)):
        if (couleur == Constante.COULEURS_ANG[i]):
            if (i < len(Constante.COULEURS_ANG) - 1):
                prochaine = Constante.COULEURS_ANG[i+1]
                break

    return prochaine

#----------------------------------------------------
def onClick(event):
    items = canvas.find_withtag(CURRENT)
    if len(items) > 0:    
        couleur = canvas.itemcget(items[0], "fill")
        canvas.itemconfig(CURRENT, fill=prochaineCouleur(couleur))

#----------------------------------------------------
def run():
    global solution

    canvas.bind('<Button-1>', onClick)

    solution = Mastermind.creer_une_solution()

    afficherCapture(canvas, 100, 410, 5, 20, 10)

    root.mainloop()

#----------------------------------------------------
def tester():
    canvas.bind('<Button-1>', onClick)

    propositionTest1=["black", "black", "yellow", "black", "blue"]
    propositionTest2=["yellow", "green", "yellow", "black", "brown"]
    propositionTest3=["green", "green", "yellow", "red", "white"]

    afficherProposition(canvas, propositionTest1, 100, 100, 20, 10)
    afficherProposition(canvas, propositionTest2, 100, 130, 20, 10)
    afficherProposition(canvas, propositionTest3, 100, 160, 20, 10)

    afficherEvaluation(canvas, [3, 1], 100, 190, 10, 5)
    afficherEvaluation(canvas, [2, 3], 100, 220, 10, 5)
    afficherEvaluation(canvas, [4, 0], 100, 250, 10, 5)

    afficherLigne(canvas, propositionTest1, [3, 1], 100, 280)

    afficherCapture(canvas, 100, 410, 5, 20, 10)

    root.mainloop()
