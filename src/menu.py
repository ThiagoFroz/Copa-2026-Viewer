def menu():
    while True:
        print("\n" + "=" * 40)
        print("       COPA 2026 VIEWER")
        print("=" * 40)
        print("1 - Pesquisar Seleção")
        print("2 - Jogos da Seleção")
        print("3 - Estatísticas de Jogadores")
        print("4 - Ranking FIFA")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nPesquisar Seleção")
            nome = input("Digite o nome da seleção: ")
            buscar_selecao(nome)
        elif opcao == "2":
            print("\nJogos da Seleção")
        elif opcao == "3":
            print("\nEstatísticas de Jogadores")
        elif opcao == "4":
            print("\nRanking FIFA")
        elif opcao == "5":
            print("\nEncerrando...")
            break
        else:
            print("\nOpção inválida!")

from src.api import buscar_selecao