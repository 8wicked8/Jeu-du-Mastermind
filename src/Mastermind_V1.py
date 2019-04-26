from random import *
import Constante

def creer_une_solution():
    liste_couleurs_reponses=[]

    for x in range(0, Constante.TAILLE_DE_SOLUTION):
        num_coul_de_la_soluce=randint(0,len(Constante.COULEURS)-1)
        coul_de_la_soluce=Constante.COULEURS[num_coul_de_la_soluce]
        liste_couleurs_reponses.append(coul_de_la_soluce)
    
    return liste_couleurs_reponses

def evaluer(proposition, solution):

    local_proposition = proposition.copy()
    local_solution = solution.copy()

    resultat = [0, 0]
    Nbs_noir = 0
    for i in range(0, len(local_solution)):
        if local_proposition[i] == local_solution[i]:
            Nbs_noir = Nbs_noir+1
            local_proposition[i] = ""
            local_solution[i] = ""

    Nbs_blanc = 0
    for i in range(0, len(local_solution)):
        for j in range(0, len(local_proposition)):
            if len(local_proposition[j]) > 0 or len(local_solution[i]) > 0:
                if local_proposition[j] == local_solution[i]:
                    Nbs_blanc = Nbs_blanc+1
                    local_proposition[j] = ""
                    local_solution[i] = ""

    resultat[0] = Nbs_noir
    resultat[1] = Nbs_blanc

    return resultat

def demander_couleur(position):
    couleur = ""
    index = int(input("Quelle couleur souhaitez-vous en position " +  str(position) + " ? "))
    couleur = Constante.COULEURS[index]
    return couleur


def demander_proposition():
    proposition = []

    for i in range(0, len(Constante.COULEURS)):
        print(i, ' - ', Constante.COULEURS[i])

    for position in range(0, Constante.TAILLE_DE_SOLUTION):
        proposition.append(demander_couleur(position))

    return proposition

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



     

evalu = evaluer(prop, sol)








