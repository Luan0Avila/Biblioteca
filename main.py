def mostrar_menu():
    print("\n===== Biblioteca =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Remover livro")
    print("0 - Sair")

rodando = True

def main():
    while rodando:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")
    
        print(f"Você escolheu a opção {opcao}")

        if opcao == "1":
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            pass
        elif opcao == "0":
            rodando = False
            print("Desligando sistema...")
        else:
            print("Opção invalida!")

if __name__=="__main__":
    main()