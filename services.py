from models import Livro


def gerar_id(livros):
    

    novo_id = len(livros) + 1

    return novo_id

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
