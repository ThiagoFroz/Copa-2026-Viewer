import requests

API_KEY = "94922ad863484c1ca58891dda9d1f7f7"

HEADERS = {
    "X-Auth-Token": API_KEY
}


def obter_copa():
    url = "https://api.football-data.org/v4/competitions/WC"

    resposta = requests.get(url, headers=HEADERS)

    if resposta.status_code != 200:
        return None

    return resposta.json()