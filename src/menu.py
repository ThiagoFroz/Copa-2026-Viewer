from src.copa import mostrar_copa


def menu():

    while True:

        print("\n" + "=" * 40)
        print("       COPA 2026 VIEWER")
        print("=" * 40)

        print("1 - Informações da Copa")
        print("2 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            mostrar_copa()

        elif opcao == "2":
            print("\nEncerrando...")
            break

        else:
            print("\nOpção inválida!")