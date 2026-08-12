from .historico_services import listar_historico,listar_historico_de_usuario,listar_historico_de_livro



def mostrar_menu_historico():
    print("1 - Listar histórico")
    print("2 - Listar histórico de usuário")
    print("3 - Listar histórico de livro")
    print("0 - Voltar")

def menu_historico(historico):
        while True:
            mostrar_menu_historico()

            opcao_historico = input("Escolha uma opção: ")
            if opcao_historico == "1":
                listar_historico(historico)

            elif opcao_historico == "2":
                listar_historico_de_usuario(historico)

            elif opcao_historico == "3":
                listar_historico_de_livro(historico)

            elif opcao_historico == "0":
                print("Voltando ao menu principal")
                break
            else:
                print("Opção invalida!")