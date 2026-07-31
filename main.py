from services import cadastrar_livro, listar_livros

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

    livros = []
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")
    
        print(f"Você escolheu a opção {opcao}")

        if opcao == "1":
            livro = cadastrar_livro(livros)
            livros.append(livro)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            pass
        elif opcao == "0":

            print("Desligando sistema...")
            break
        else:
            print("Opção invalida!")

if __name__=="__main__":
    main()