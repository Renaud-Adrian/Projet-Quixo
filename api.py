import requests

def initialiser_partie(idul, secret):
    url = "https://pax.ulaval.ca/quixo/api/a24/partie/"
    response = requests.post(url, auth=(idul, secret))
    
    if response.status_code == 200:
        data = response.json()
        return data['id'], data['joueurs'], data['etat']
    elif response.status_code == 401:
        raise PermissionError(response.json()['message'])
    elif response.status_code == 406:
        raise RuntimeError(response.json()['message'])
    else:
        raise ConnectionError("Erreur inconnue lors de la requête")

def jouer_un_coup(id_partie, origine, direction, idul, secret):
    url = f"https://pax.ulaval.ca/quixo/api/a24/partie/{id_partie}/"
    data = {
        "origine": origine,
        "direction": direction
    }
    response = requests.put(url, auth=(idul, secret), json=data)
    
    if response.status_code == 200:
        data = response.json()
        return data['id'], data['joueurs'], data['etat']
    elif response.status_code == 401:
        raise PermissionError(response.json()['message'])
    elif response.status_code == 406:
        raise RuntimeError(response.json()['message'])
    else:
        raise ConnectionError("Erreur inconnue lors de la requête")