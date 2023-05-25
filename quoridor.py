"""Module de la classe Quoridor

Classes:
    * Quoridor - Classe pour encapsuler le jeu Quoridor.
"""
from copy import deepcopy
import networkx as nx
from quoridor_error import QuoridorError
from graphe import construire_graphe


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.

    Vous ne devez pas créer d'autre attributs pour votre classe.

    Attributes:
        état (dict): état du jeu tenu à jour.
    """

    def __init__(self, joueurs, murs=None):
        """Constructeur de la classe Quoridor.

        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.

        Appel la méthode `vérification` pour valider les données et assigne
        ce qu'elle retourne à l'attribut `self.état`.

        Cette méthode ne devrait pas être modifiée.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        """
        self.état = deepcopy(self.vérification(joueurs, murs))

    def vérification(self, joueurs, murs):
        """Vérification d'initialisation d'une instance de la classe Quoridor.

        Valide les données arguments de construction de l'instance et retourne
        l'état si valide.

        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie.
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions [x, y] des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions [x, y] des murs verticaux.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de list [x, y] uniquement.
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        if not isinstance(joueurs, list):
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")
        if len(joueurs) != 2:
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")
        if joueurs[0]['murs'] > 10 or joueurs[0]['murs'] < 0 or joueurs[1]['murs'] > 10 or joueurs[1]['murs'] < 0:
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10, ou négatif.")
        if joueurs[0]['pos'][0] < 1 or joueurs[0]['pos'][0] > 9 or joueurs[0]['pos'][1] < 1 or joueurs[0]['pos'][1] > 9 or joueurs[1]['pos'][0] < 1 or joueurs[1]['pos'][0] > 9 or joueurs[1]['pos'][1] < 1 or joueurs[1]['pos'][1] > 9:
            raise QuoridorError("La position d'un joueur est invalide.")
        if murs is not None and not isinstance(murs, dict):
            raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")
        if murs is not None and len(murs['horizontaux']) + len(murs['verticaux']) + joueurs[0]['murs'] + joueurs[1]['murs'] != 20:
            raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")
        if murs is not None:
            for mur in murs['horizontaux']:
                if mur[0] < 1 or mur[0] > 8 or mur[1] < 1 or mur[1] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
            for mur in murs['verticaux']:
                if mur[0] < 1 or mur[0] > 9 or mur[1] < 1 or mur[1] > 8:
                    raise QuoridorError("La position d'un mur est invalide.")
        murs = {'horizontaux': [], 'verticaux': []} if murs is None else murs
        return {'joueurs': joueurs, 'murs': murs}

    def formater_légende(self):
        """Produire la légende à afficher avec la représentation ASCII."""
        joueur1 = self.état['joueurs'][0]['nom']
        joueur2 = self.état['joueurs'][1]['nom']
        murs1 = self.état['joueurs'][0]['murs']
        murs2 = self.état['joueurs'][1]['murs']
        légende = "Légende:\n"
        ligne1 = '   ' + '1=' + joueur1 + ',' + ' ' + 'murs=' + '|'*murs1 + '\n'
        figne1 = '   ' + '2=' + joueur2 + ',' + ' ' * (len(joueur1) - len(joueur2)) + ' ' + 'murs=' + '|'*murs2 +'\n'
        ligne2 = '   ' + '1=' + joueur1 + ',' + ' ' * (len(joueur2) - len(joueur1)) + ' ' + 'murs=' + '|'*murs1 + '\n'
        figne2 = '   ' + '2=' + joueur2 + ',' + ' ' + 'murs=' + '|'*murs2 +'\n'
        if len(joueur1) >= len(joueur2):
            return légende + ligne1 + figne1
        return légende + ligne2 + figne2
    def formater_damier(self):
        """Formater la représentation graphique du damier.

        Returns:
            str: Chaîne de caractères représentant le damier.
        """
        c=  "   -----------------------------------\n"\
            "9 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "8 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "7 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "6 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "5 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "4 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "3 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "2 | .   .   .   .   .   .   .   .   . |\n"\
            "  |                                   |\n"\
            "1 | .   .   .   .   .   .   .   .   . |\n"\
            "--|-----------------------------------\n"\
            "  | 1   2   3   4   5   6   7   8   9\n"
        for x,i in enumerate(range(2)):
            fi, ug = self.état["joueurs"][i]["pos"]
            gg = 9 - ug
            c = c.replace(c[(gg * 80) + 39 + (fi) *4:],f"{x + 1}") + c[(gg * 80) + 40 + (fi) * 4:]
        for i in self.état ["murs"]['horizontaux']:
            fi, ug = i
            gg = 9 - ug
            c = c.replace(c[(gg*80) + 78 + (fi) * 4:], "-" *7)+c[(gg * 80) + 85 + (fi) * 4:]
        for i in self.état ["murs"]['verticaux']:
            fi, ug = i
            gg = 9 - ug
            c = c.replace(c[(gg * 80) + 37 + (fi) * 4:], "|") + c[(gg * 80) + 38 + (fi) * 4:]
            c = c.replace(c[(gg * 80) - 3 + (fi) * 4:], "|") + c[(gg * 80) - 2+ (fi) * 4:]
            c = c.replace(c[(gg * 80) - 43 + (fi) * 4:], "|") + c[(gg * 80) - 42 + (fi) * 4:]
        return c
    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.

        Cette représentation est la même que celle du projet précédent.

        Returns:
            str: La chaîne de caractères de la représentation.
        """
        return self.formater_légende() + self.formater_damier()
    def état_courant(self):
        """Produire l'état actuel du jeu.

        Cette méthode ne doit pas être modifiée.

        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de liste [x, y] uniquement.
        """
        return deepcopy(self.état)
    def est_terminée(self):
        """Déterminer si la partie est terminée.
        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        if self.état['joueurs'][0]['pos'][1] == 9:
            return self.état['joueurs'][0]['nom']
        if self.état['joueurs'][1]['pos'][1] == 1:
            return self.état['joueurs'][1]['nom']
        return False
    def récupérer_le_coup(self, joueur):
        """Récupérer le coup

        Notez que seul 2 questions devrait être posée à l'utilisateur.

        Notez aussi que cette méthode ne devrait pas modifier l'état du jeu.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Le type de coup est invalide.
            QuoridorError: La position est invalide (en dehors du damier).

        Returns:
            tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
        """
        type_de_coup = input('quel type de coup désirez-vous jouer?')
        v=(input("Donnez la position où appliquer ce coup (x,y):"))
        position=[int(v[0]), int(v[2])]
        # Vérification du joueur
        if joueur not in (1, 2):
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')
        if type_de_coup not in ['D','MH','MV']:
            raise QuoridorError('Le type de coup est invalide.')
       # Vérification de la position du joueur
        if not 1 <= position[0] <= 9 or not 1 <= position[1] <= 9:
            raise QuoridorError('La position est invalide (en dehors du damier).')
        return (str(type_de_coup), list(position))
    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.

        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.

        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (List[int, int]): La liste [x, y] de la position du jeton (1<=x<=9 et 1<=y<=9).

        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        #en utilisant la fonction construire_graphe, on peut vérifier si le déplacement est valide
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if position[0] not in list(range(1, 10)) or position[1] not in list(range(1, 10)):
            raise QuoridorError("La position est invalide (en dehors du damier).")
        graphe = graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],
                                            self.état['murs']['horizontaux'],
                                            self.état['murs']['verticaux'])
        coup_disponible = list(graphe.successors((self.état['joueurs'][joueur - 1]['pos'][0],
                                                  self.état['joueurs'][joueur - 1]['pos'][1])))
        if tuple(position) not in coup_disponible:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        self.état['joueurs'][joueur-1]['pos'] = position
    def placer_un_mur(self, joueur, position, orientation):
        """Placer un mur.
        Pour le joueur spécifié, placer un mur à la position spécifiée.
        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (List[int, int]): la liste [x, y] de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        #vérifier si le joueur correspond à 1 ou 2
        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        #vérifier si le mur est déjà placé
        if orientation == 'horizontal':
            if list[position] in self.état['murs']['horizontaux']:
                raise QuoridorError("Un mur occupe déjà cette position.")
        if orientation == 'vertical':
            if list[position] in self.état['murs']['verticaux']:
                raise QuoridorError("Un mur occupe déjà cette position.")
        #vérifier si la position est valide pour cette orientation
        if orientation == 'vertical':
            if position[0] in [8, 9] or position[1] in [1]:
                raise QuoridorError("La position est invalide pour cette orientation.")
        if orientation == 'vertical':
            if position[0] in [1] or position[1] in [9]:
                raise QuoridorError("La position est invalide pour cette orientation.")
        #vérifier si le joueur a déjà placé tous ses murs
        if self.état['joueurs'][joueur-1]['murs'] == 0:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")
        graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],
                                            self.état['murs']['horizontaux'],
                                            self.état['murs']['verticaux'])
        positions = {'B1': (5, 9), 'B2': (5, 1)}
        if orientation == "horizontal":
            if joueur == 1:
                self.état['joueurs'][joueur-1]['murs'] = self.état['joueurs'][joueur-1]['murs'] - 1
            else:
                self.état['joueurs'][joueur-1]['murs'] = self.état['joueurs'][joueur-1]['murs'] - 1
            self.état['murs']['horizontaux'] = self.état['murs']['horizontaux'] + [position]
            #vérifier si le mur enferme le joueur
            graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],
                                        self.état['murs']['horizontaux'],
                                        self.état['murs']['verticaux'])
            if nx.has_path(graphe, tuple(self.état['joueurs'][0]['pos']), 'B1') is False:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu")
            if nx.has_path(graphe, tuple(self.état['joueurs'][1]['pos']), 'B2') is False:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu")
        if orientation == "vertical":
            if joueur == 1:
                self.état['joueurs'][joueur-1]['murs'] = self.état['joueurs'][joueur-1]['murs'] - 1
            else:
                self.état['joueurs'][joueur-1]['murs'] = self.état['joueurs'][joueur-1]['murs'] - 1
            #vérifier si le mur enferme le joueur
            self.état['murs']['verticaux'] = self.état['murs']['verticaux'] + [position]
            graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],
                                        self.état['murs']['horizontaux'],
                                        self.état['murs']['verticaux'])
            if nx.has_path(graphe, tuple(self.état['joueurs'][0]['pos']), 'B1') is False:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu")
            if nx.has_path(graphe, tuple(self.état['joueurs'][1]['pos']), 'B2') is False:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu")
    def jouer_le_coup(self, joueur):
        """Jouer un coup automatique pour un joueur.
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.
        Returns:
            Tuple[str, List[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        if joueur not in (1, 2):
            raise QuoridorError(" Le numéro du joueur est autre que 1 ou 2.")
        graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],self.état['murs']['horizontaux'],self.état['murs']['verticaux'])
        destinations = {'B1': (5, 9), 'B2': (5, 1)}
        chemin_bot = nx.shortest_path(graphe, tuple(self.état['joueurs'][0]['pos']), 'B1')
        murs_horizontaux= []
        murs_verticaux= []
        chemin_horizontaux = []
        chemin_verticaux = []
        for i in range(2,10):
            for j in range(1,9):
                murs_verticaux.append([i,j])
        for x in range(1,9):
            for y in range(2,10):
                murs_horizontaux.append([x,y])
        for j in range(len(murs_horizontaux)):
            try:
                graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],self.état['murs']['horizontaux'] +
                                           [murs_horizontaux[j]],self.état['murs']['verticaux'])
                chemin_horizontaux += [nx.shortest_path(graphe, tuple(self.état['joueurs'][1]['pos']), 'B2') +
                                       [murs_horizontaux[j]] + ['MH']]
            except:
                pass
        for p in range(len(murs_verticaux)):
            try:
                graphe = construire_graphe([joueur['pos'] for joueur in self.état['joueurs']],self.état['murs']['horizontaux'],self.état['murs']['verticaux'] +
                                           [murs_verticaux[p]])
                chemin_verticaux += [nx.shortest_path(graphe, tuple(self.état['joueurs'][1]['pos']), 'B2') +
                                     [murs_verticaux[p]] + ['MV']]
            except:
                pass

        tous_chemins = chemin_verticaux + chemin_horizontaux
        tous_chemins.sort(key=len, reverse=True)

        return chemin_bot, (tous_chemins[0][-1], tous_chemins[0][-2]), (tous_chemins[1][-1], tous_chemins[1][-2]), (tous_chemins[2][-1], tous_chemins[2][-2]), (tous_chemins[3][-1], tous_chemins[3][-2])
