from services import cadastrar_livro, listar_livros, buscar_livro,apagar_livro, emprestar_livro, devolver_livro, listar_historico, listar_historico_de_usuario, listar_historico_de_livro

from storage import carregar_livros, salvar_livros, carregar_historico,salvar_historico

def mostrar_menu():
    print("=" * 20 + " Biblioteca " + "=" * 20)
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Remover livro")
    print("7 - Listar histórico")
    print("8 - Listar histórico de usuário")
    print("9 - Listar histórico de livro")
    print("0 - Sair")
    print("=" * 53)

def main():

    livros = carregar_livros()
    historico = carregar_historico()
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")
    
        print(f"Você escolheu a opção {opcao}")

        if opcao == "1":
            livro = cadastrar_livro(livros)
            if livro:
                livros.append(livro)
                salvar_livros(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            buscar_livro(livros)
        elif opcao == "4":
            emprestar_livro(livros, historico)
            salvar_livros(livros)
            salvar_historico(historico)
        elif opcao == "5":
            devolver_livro(livros, historico)
            salvar_livros(livros)
            salvar_historico(historico)
        elif opcao == "6":
            apagar_livro(livros)
            salvar_livros(livros)
        elif opcao == "7":
            listar_historico(historico)
        elif opcao == "8":
            listar_historico_de_usuario(historico)
        elif opcao == "9":
            listar_historico_de_livro(historico)
        elif opcao == "0":

            print("Desligando sistema...")
            break
        else:
            print("Opção invalida!")

if __name__=="__main__":
    main()