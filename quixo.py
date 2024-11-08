def formater_entête(joueurs):
    """Formate la légende du jeu avec les noms des joueurs"""
    return f"Légende:\n   X={joueurs[0]}\n   O={joueurs[1]}"

def formater_le_damier(etat):
    """Formate le plateau de jeu en art ASCII"""
    plateau = etat['plateau']
    lignes = []
    for i, ligne in enumerate(plateau, 1):
        ligne_str = f"{i} | " + " | ".join(ligne) + " |"
        lignes.append(ligne_str)
        if i < 5:
            lignes.append("  |---|---|---|---|---|")
    return "\n".join(lignes) + "\n--|---|---|---|---|---|\n  | 1   2   3   4   5 |"