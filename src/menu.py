from src.selecoes import pesquisar_selecao


def menu():
    while True:
        print("\n" + "=" * 40)
        print("       COPA 2026 VIEWER")
        print("=" * 40)
        print("1 - Testar API")
        print("2 - Jogos da Seleção")
        print("3 - Estatísticas de Jogadores")
        print("4 - Ranking FIFA")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            pesquisar_selecao()

        elif opcao == "2":
            print("\nFunção em desenvolvimento.")

        elif opcao == "3":
            print("\nFunção em desenvolvimento.")

        elif opcao == "4":
            print("\nFunção em desenvolvimento.")

        elif opcao == "5":
            print("\nEncerrando...")
            break

        else:
            print("\nOpção inválida!")