import argparse
from api import initialiser_partie, jouer_un_coup
from quixo import formater_entête, formater_le_damier

def main():
    # Argument de la ligne de commande pour l'idul du joueur
    parser = argparse.ArgumentParser(description="Jeu Quixo")
    parser.add_argument("idul", type=str, help="IDUL du joueur")
    args = parser.parse_args()
    
    # Récupère les informations d'authentification
    idul = args.idul
    secret = "ton-jeton-personnel"  # Remplace par ton jeton

    # Initialiser la partie
    id_partie, joueurs, etat = initialiser_partie(idul, secret)
    
    # Afficher l'état du jeu
    print(formater_entête(joueurs))
    print(formater_le_damier(etat))
    
    # Boucle de jeu
    while True:
        # Demander un coup à l'utilisateur (on suppose que la fonction choisir_un_coup existe)
        origine, direction = choisir_un_coup()
        
        # Jouer le coup
        id_partie, joueurs, etat = jouer_un_coup(id_partie, origine, direction, idul, secret)
        
        # Afficher le nouvel état du jeu
        print(formater_entête(joueurs))
        print(formater_le_damier(etat))

if __name__ == "__main__":
    main()