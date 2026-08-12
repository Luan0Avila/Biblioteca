from services import gerar_id, encontrar_livro_por_id, encontrar_livro_por_titulo
from models import Livro

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