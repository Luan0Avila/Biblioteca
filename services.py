from models import Livro


def gerar_id(livros):

    return len(livros) + 1

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
            encontrado = True

    if not encontrado:
        print("Nenhum livro encontrado! :(")


def apagar_livro(livros):
    try:
        id_livro = int(input("Digite o ID do livro a ser apagado:"))
    except ValueError:
        print("Digite um ID válido")
        return
    for livro in livros:
        if id_livro == livro.id:
            livros.remove(livro)
            print(f'Livro "{livro.titulo}" removido com sucesso!')
            return
    
    print("ID de livro não encontrado.")