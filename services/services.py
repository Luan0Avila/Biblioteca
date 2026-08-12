from models import Livro, HistoricoEmprestimo

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





