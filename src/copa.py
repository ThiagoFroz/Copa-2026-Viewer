from src.api import obter_copa


def mostrar_copa():
    dados = obter_copa()

    if not dados:
        print("Erro ao acessar API.")
        return

    print("\n=== COPA DO MUNDO 2026 ===\n")

    print("Competição:", dados["name"])
    print("Início:", dados["currentSeason"]["startDate"])
    print("Fim:", dados["currentSeason"]["endDate"])

    print("\nÚltimos campeões:\n")

    for temporada in dados["seasons"][:10]:

        vencedor = temporada.get("winner")

        if vencedor:
            print(
                f"{temporada['startDate'][:4]} - {vencedor['name']}"
            )