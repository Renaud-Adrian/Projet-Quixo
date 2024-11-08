def formater_entête(joueurs):
    """Formate la légende du jeu avec les noms des joueurs"""
    return f"Légende:\n   X={joueurs[0]}\n   O={joueurs[1]}"

def choisir_un_coup():
    # Demande la position d'origine du cube et la convertit en liste d'entiers
    while True:
        origine_str = input("Donnez la position d'origine du cube (x,y) : ")
        try:
            origine = [int(coord) for coord in origine_str.split(",")]
            if len(origine) != 2:
                raise ValueError("Il faut deux coordonnées.")
            break
        except ValueError:
            print("Entrée invalide. Assurez-vous que vous saisissez deux nombres séparés par une virgule.")
    
    # Demande la direction de déplacement
    directions_valides = ['haut', 'bas', 'gauche', 'droite']
    while True:
        direction = input("Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') : ")
        if direction in directions_valides:
            break
        print("Direction invalide. Veuillez choisir parmi 'haut', 'bas', 'gauche', 'droite'.")
    
    # Retourne un tuple contenant la position d'origine et la direction
    return origine, direction

def formater_le_damier(etat):
    """Formate le plateau de jeu en art ASCII"""
    plateau = etat['plateau']
    lignes = []
    for i, ligne in enumerate(plateau, 1):
        ligne_str = f"{i} | " + " | ".join(ligne) + " |"
        lignes.append(ligne_str)
        if i < len(plateau):  # Ne pas ajouter la ligne de séparation après la dernière ligne
            lignes.append("  |---|---|---|---|---|")
    return "\n".join(lignes) + "\n--|---|---|---|---|---|\n  | 1   2   3   4   5 |"