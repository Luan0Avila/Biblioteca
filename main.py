def mostrar_menu():
    print("\n===== Biblioteca =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Remover livro")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o sistema...")
            break
    
        print(f"Você escolheu a opção {opcao}")

if __name__=="__main__":
    main()