"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.
"""
import random
import time
from api import débuter_partie, jouer_coup
from quoridor import Quoridor
from quoridorx import QuoridorX
from utilitaire import analyser_commande


# Mettre ici votre secret récupéré depuis le site de PAX
SECRET = "3194de1c-2935-4909-a372-d877ec4dc4c7"

if __name__ == "__main__":
    args = analyser_commande()
    automatique_value = args.__dict__.get('automatique ')
    if args.graphique is False and automatique_value is True:
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            # Afficher la partie
            jeu = Quoridor(état['joueurs'],état['murs'])
           
            probabilité = random.randint(1,2)
            if probabilité == 1:
                try:
                    type_coup = str(jeu.jouer_le_coup(1)[1][0])
                    position = jeu.jouer_le_coup(1)[1][1]
                    id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                except:
                    try:
                        type_coup = str(jeu.jouer_le_coup(1)[2][0])
                        position = jeu.jouer_le_coup(1)[2][1]
                        id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                    except:
                        type_coup = 'D'
                        position = [jeu.jouer_le_coup(1)[0][1][0], jeu.jouer_le_coup(1)[0][1][1]]
                        id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            else:
                type_coup = 'D'
                position = [jeu.jouer_le_coup(1)[0][1][0], jeu.jouer_le_coup(1)[0][1][1]]
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
            time.sleep(1)

    if args.graphique is True and automatique_value is False:
        id_partie, état = débuter_partie(args.idul, SECRET)
        game = QuoridorX(état['joueurs'],état['murs'])
        poo=[]
        while True:
            # Afficher la partie
            # Récupérer le coup du joueur

            #move = sc.textinput("Quel type de coup voulez-vous jouer?", "(D, MH, MV)")

            #position2 = []
            #if move in ['D', 'MH' 'MV']:

            #position1 = sc.textinput("À quelle position voulez-vous jouer?", "(x, y)")

            #position2.append(int(position1[0]))
            #position2.append(int(position1[2]))
            game.afficher()
            game.demander_coup()
            if game.ok :
                if game.type!="" and game.pos!=[]:
                    poo.append(game.pos)
                    t=True

                    if game.type == 'D' and poo.count(game.pos)==1:
                        game.état = game.vérification(game.état['joueurs'], game.état['murs'])
                        id_partie, game.état = jouer_coup(id_partie, game.type, game.pos, args.idul, SECRET,)
                        game.effacer()
                    elif game.type == 'MH'and poo.count(game.pos)==1:
                        game.état = game.vérification(game.état['joueurs'], game.état['murs'])
                        id_partie, game.état = jouer_coup(id_partie, game.type, game.pos, args.idul, SECRET,)
                        game.effacer()
                    elif game.type == 'MV'and poo.count(game.pos)==1:
                        game.état = game.vérification(game.état['joueurs'], game.état['murs'])
                        id_partie, game.état = jouer_coup(id_partie, game.type, game.pos, args.idul, SECRET,)
                        game.effacer()
                        
    if args.graphique is True and automatique_value is True:
        id_partie, état = débuter_partie(args.idul, SECRET)
        while True:
            # Afficher la partie
            jeu = QuoridorX(état['joueurs'],état['murs'])
            jeu.afficher()
            probabilité = random.randint(1,2)
            if probabilité == 1:
                try:
                    type_coup = str(jeu.jouer_le_coup(1)[1][0])
                    position = jeu.jouer_le_coup(1)[1][1]
                    id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                    jeu.effacer()
                except:
                    try:
                        type_coup = str(jeu.jouer_le_coup(1)[2][0])
                        position = jeu.jouer_le_coup(1)[2][1]
                        id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                        jeu.effacer()
                    except:
                        type_coup = 'D'
                        position = [jeu.jouer_le_coup(1)[0][1][0], jeu.jouer_le_coup(1)[0][1][1]]
                        id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                        jeu.effacer()
            else:
                type_coup = 'D'
                position = [jeu.jouer_le_coup(1)[0][1][0], jeu.jouer_le_coup(1)[0][1][1]]
                id_partie, état = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)
                jeu.effacer()
            time.sleep(0)
    else:
        id_partie, état = débuter_partie(args.idul, SECRET)
        
        while True:
            # Afficher la partie
            print(Quoridor(état['joueurs'],état['murs']))
            # Demander au joueur de choisir son prochain coup
            type_coup, position = Quoridor(état['joueurs'],état['murs']).récupérer_le_coup(1)
            # Envoyez le coup au serveur
            id_partie, état = jouer_coup(
                id_partie,
                type_coup,
                position,
                args.idul,
                SECRET,
            )