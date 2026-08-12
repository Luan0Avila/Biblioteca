from services import encontrar_livro_por_id, encontrar_livro_por_titulo
from datetime import datetime

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
