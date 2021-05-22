#visit Dhermil.github.io
#Jeu : DEVINE LE NOMBRE entre 1 et 1000

from random import *
from math import sqrt

nieme=['premier', 'deuxième', 'troisième',
       'quatrième', 'cinquième', 'sixième',
       'septième', 'huitième', 'neuvième',
       'dixième']

nb_deviner = str(randint(1,1000))
liste = list(nb_deviner)

longueur = len(nb_deviner)
plus_grand = max(liste)
plus_petit = min(liste)
racine_carree = sqrt(int(nb_deviner))
premier = liste[0]
dernier = liste[len(liste)-1]

indice = {'Nombre de chiffres dont le nombre que tu recherche est composé :' : [longueur],
          'Le plus grand chiffre de ce nombre est : '  : [plus_grand],
          'La racine carrée de ce nombre est : ' : [racine_carree],
          'Le dernier chiffre de ce nombre est : ' : [dernier],
          'Le plus petit chiffre de ce nombre est : ' : [plus_petit],
          'Le premier chiffre de ce nombre est : ' : [premier] }

print('Premier essai :')

saisie = input('Saisis un nombre : ')

if saisie != nb_deviner :
        global n_essai
        n_essai = 1
        for k, v in indice.items():
            print(k, v[0])
            saisie = input('Allez ! Deuxième tentative : ')
            n_essai +=1
            if saisie != nb_deviner :
                continue
            else :
                print('Bravo ! Réussi au bout de la', nieme[n_essai - 1], 'tentative !')
                break

else :
    print('Félicitations ! Du', nieme[0] ,'coup !')

if saisie != nb_deviner :
    print('Dommage, c\'est raté, le nombre était', nb_deviner ,'.')

