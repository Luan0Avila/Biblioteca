from models import Livro


def gerar_id(livros):

    return len(livros) + 1

def cadastrar_livro(livros):
    titulo = input("Digite o titulo: ")
    autor = input("Digite o nome do autor: ")
    ano = int(input("Digite o ano de publicação: "))

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