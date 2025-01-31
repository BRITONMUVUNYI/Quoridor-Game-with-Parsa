"""Module d'API du jeu Quoridor

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""

import requests

URL = "https://pax.ulaval.ca/quoridor/api/v2/"


def lister_parties(idul, SECRET):
    """Lister les parties
    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX
    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406
    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le json de sa réponse.
    """
    rep = requests.get(URL +'parties', auth=(idul, SECRET))
    per = rep.json()
    if rep.status_code == 200:
        return per['parties']
    if rep.status_code == 401:
        raise PermissionError(per['message'])
    if rep.status_code == 406:
        raise RuntimeError(per['message'])
    raise ConnectionError

def débuter_partie(idul, SECRET):
    """Débuter une partie
    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX
    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.post(URL +'partie', auth=(idul, SECRET))
    per = rep.json()
    if rep.status_code == 200:
        return (per['id'], per['état'])
    if rep.status_code == 401:
        raise PermissionError(per['message'])
    if rep.status_code == 406:
        raise RuntimeError(per['message'])
    raise ConnectionError

def récupérer_partie(id_partie, idul, SECRET):
    """Récupérer une partie
    Args:
        id_partie (str): identifiant de la partie à récupérer
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX
    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.get(URL+'partie/'+id_partie, auth=(idul, SECRET))
    per = rep.json()

    if rep.status_code == 200:
        return (per['id'], per['état'], per['gagnant'])
    if rep.status_code == 401:
        raise PermissionError(per['message'])
    if rep.status_code == 406:
        raise RuntimeError(per['message'])

    raise ConnectionError

def jouer_coup(id_partie, type_coup, position, idul, SECRET):
    """Jouer un coup
    Args:
        id_partie (str): Identifiant de la partie.
        type_coup (str): Type de coup du joueur :
                            'D' pour déplacer le jeton,
                            'MH' pour placer un mur horizontal,
                            'MV' pour placer un mur vertical;
        position (list): La position [x, y] du coup.
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX
    Raises:
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406
    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours
            et de l'état courant du jeu, après avoir décodé
            le JSON de sa réponse.
    """
    rep = requests.put(URL+'jouer', auth=(idul, SECRET),
                       json={"id": id_partie,"type": type_coup,"pos": position,})
    per = rep.json()

    if rep.status_code == 200:
        if per['gagnant'] is not None:
            raise StopIteration(per['gagnant'])
        return (per['id'], per['état'])
    if rep.status_code == 401:
        raise PermissionError(per['message'])
    if rep.status_code == 406:
        raise RuntimeError(per['message'])
    raise ConnectionError
