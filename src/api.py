import requests

API_KEY = "94922ad863484c1ca58891dda9d1f7f7"


def buscar_competicoes():
    url = "https://api.football-data.org/v4/competitions"

    headers = {
        "X-Auth-Token": API_KEY
    }

    try:
        resposta = requests.get(url, headers=headers)

        if resposta.status_code == 200:
            return resposta.json()

        print(f"\nErro na API: {resposta.status_code}")
        return None

    except Exception as erro:
        print(f"\nErro: {erro}")
        return None