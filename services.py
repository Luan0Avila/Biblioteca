from models import Livro, HistoricoEmprestimo
from datetime import datetime

def gerar_id(livros):
    if not livros:
        return 1

    ids = [livro.id for livro in livros]
    return max(ids) + 1

def encontrar_livro_por_titulo(livros, titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            return livro

    return None

def encontrar_livro_por_id(livros, id_livro):
    for livro in livros:
        if livro.id == id_livro:
            return livro

    return None

def cadastrar_livro(livros):
    titulo = input("Digite o titulo: ")
    autor = input("Digite o nome do autor: ")
    try:
        ano = int(input("Digite o ano de publicação: "))
    except ValueError:
        print("Digite um ano válido.")
        return

    print("Livro cadastrado com sucesso!")
    livro = Livro(
        id = gerar_id(livros),
        titulo = titulo,
        autor = autor,
        ano = ano
    )

    return livro

def listar_livros(livros):
    if not livros:
        print("No momento não nenhum livro para listar")
    else:
        print("====Livros Listados====")

        for livro in livros:
            print(f"ID: {livro.id}\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}")
            print("______________________________________")

def buscar_livro(livros):
    busca = input("Digite o titulo: ").lower()
    encontrado = False

    for livro in livros:
        if busca in livro.titulo.lower():
            print("Livro encontrado!")
            print(f"ID: {livro.id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")
            print("-" * 40)

            encontrado = True

    if not encontrado:
        print("Nenhum livro encontrado! :(")

def apagar_livro(livros):
    try:
        id_livro = int(input("Digite o ID do livro a ser apagado:"))
    except ValueError:
        print("Digite um ID válido")
        return
        livro = encontrar_livro_por_id(livros, id_livro)

        if livro is None:
            print("ID de livro não encontrado.")
            return

        livros.remove(livro)
        print(f'Livro "{livro.titulo}" removido com sucesso!')

def emprestar_livro(livros, historico):
    try:
        livro_emprestado = int(input("Digite o ID do livro que deseja pegar emprestado: "))
    except ValueError:
        print("Digite um ID válido")
        return

    livro = encontrar_livro_por_id(livros, livro_emprestado)

    if livro is None:
        print("Livro não encontrado")
        return

    usuario = input("Digite o nome do usuário: ")

    if livro.emprestado:
        print("Este livro já foi pego emrestado! :(")
        return
    print(f'Livro "{livro.titulo}" emprestado com sucesso"')
    livro.emprestado = True
    registro = HistoricoEmprestimo(
    livro_id=livro.id,
    titulo=livro.titulo,
    usuario=usuario,
    data_emprestimo=datetime.now().isoformat()
    )
    historico.append(registro)
    return

def devolver_livro(livros,historico):
    try:
        livro_devolvido = int(input("Digite o ID do livro que deseja devolver: "))
    except ValueError:
        print("Digite um ID válido")
        return

    livro = encontrar_livro_por_id(livros, livro_devolvido)

    if livro is None:
        print("Livro não encontrado")
        return

    if not livro.emprestado:
        print("Este livro não está emprestado!")
        return

    livro.emprestado = False

    for registro in historico:
        if registro.livro_id == livro.id and registro.data_devolucao is None:
            registro.data_devolucao = datetime.now().isoformat()
            break

    print(f'Livro "{livro.titulo}" foi devolvido com sucesso')

def listar_historico(historico):
    print("Este é o histórico")
    for registro in historico:
        print(f'Livro: {registro.titulo}\n'
        f'Usuário: {registro.usuario}\n'
        f'Empréstimo: {registro.data_emprestimo}'
        )

        if registro.data_devolucao is None:
            print('Devolução: Ainda está emprestado')
        else:
            print(f'Devolução: {registro.data_devolucao}')
        
        print("-" * 40)

def listar_historico_de_usuario(historico):
    usuario = input("Digite o nome do usuário: ")
    encontrado = False

    for registro in historico:
        if usuario.lower() == registro.usuario.lower():
            print(f'Livro: {registro.titulo}\n'
            f'Usuário: {registro.usuario}\n'
            f'Empréstimo: {registro.data_emprestimo}'
            )
            if registro.data_devolucao is None:
                print("Devolução: Ainda está emprestado")
            else:
                print(f"Devolução: {registro.data_devolucao}")

            print("-" * 40)
            encontrado = True
    
    if not encontrado:
        print("Usuário não encontrado! :(")

def listar_historico_de_livro(historico):
    livro = input("Digite o titulo do livro: ")
    encontrado = False

    for registro in historico:
        if livro.lower() == registro.titulo.lower():
            print(f'Livro: {registro.titulo}\n'
            f'Usuário: {registro.usuario}\n'
            f'Empréstimo: {registro.data_emprestimo}'
            )
            if registro.data_devolucao is None:
                print("Devolução: Ainda está emprestado")
            else:
                print(f"Devolução: {registro.data_devolucao}")

            print("-" * 40)
            encontrado = True
    
    if not encontrado:
        print("Livro não encontrado! :(")


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



