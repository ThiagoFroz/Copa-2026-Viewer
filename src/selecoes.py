from src.api import buscar_competicoes


def pesquisar_selecao():
    dados = buscar_competicoes()

    if not dados:
        return

    print("\nCompetições encontradas:\n")

    for competicao in dados["competitions"][:10]:
        print(f"- {competicao['name']}")