import requests

def initialiser_partie(idul, secret):
    url = "https://pax.ulaval.ca/quixo/api/a24/partie/"
    response = requests.post(url, auth=(idul, secret))
    
    try:
        response.raise_for_status()  # Vérifie les erreurs HTTP (non 2xx)
        data = response.json()
        if 'id' in data and 'joueurs' in data and 'etat' in data:
            return data['id'], data['joueurs'], data['etat']
        else:
            raise ValueError("Réponse invalide: les clés attendues ne sont pas présentes.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            raise PermissionError(response.json().get('message', 'Erreur d\'authentification'))
        elif response.status_code == 406:
            raise RuntimeError(response.json().get('message', 'Erreur lors de la requête'))
        else:
            raise ConnectionError(f"Erreur HTTP: {http_err}")
    except Exception as err:
        raise RuntimeError(f"Erreur inconnue: {err}")

def jouer_un_coup(id_partie, origine, direction, idul, secret):
    url = f"https://pax.ulaval.ca/quixo/api/a24/partie/{id_partie}/"
    data = {
        "origine": origine,
        "direction": direction
    }
    response = requests.put(url, auth=(idul, secret), json=data)
    
    try:
        response.raise_for_status()  # Vérifie les erreurs HTTP (non 2xx)
        data = response.json()
        if 'id' in data and 'joueurs' in data and 'etat' in data:
            return data['id'], data['joueurs'], data['etat']
        else:
            raise ValueError("Réponse invalide: les clés attendues ne sont pas présentes.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            raise PermissionError(response.json().get('message', 'Erreur d\'authentification'))
        elif response.status_code == 406:
            raise RuntimeError(response.json().get('message', 'Erreur lors de la requête'))
        else:
            raise ConnectionError(f"Erreur HTTP: {http_err}")
    except Exception as err:
        raise RuntimeError(f"Erreur inconnue: {err}")