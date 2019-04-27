from Mastermind import *

#----------------------------------------------------
def demander_couleur(position):
    couleur = ""
    index = int(input("Quelle couleur souhaitez-vous en position " +  str(position) + " ? "))
    couleur = Constante.COULEURS_ANG[index]
    return couleur


#----------------------------------------------------
def demander_proposition():
    proposition = []

    for i in range(0, len(Constante.COULEURS_ANG)):
        print(i, ' - ', Constante.COULEURS_ANG[i])

    for position in range(0, Constante.TAILLE_DE_SOLUTION):
        proposition.append(demander_couleur(position))

    return proposition

#----------------------------------------------------
def run():
    sol = creer_une_solution()
    for z in range(0,12):
        prop = demander_proposition()
        print(prop)
        resultat = evaluer(prop, sol)
        print(resultat)
        print("votre nombre de tours restant est " + str(11 - z))
        if resultat[0] == 5:

            print("vous avez gagné")
            break
        elif z == 12:
            print("Vous avez perdu")









