from models import Livro
from services.livro_services import gerar_id


def test_gerar_id():
    livros = [
        Livro(
            id=1,
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano=1899
        ),
        Livro(
            id=2,
            titulo="O Hobbit",
            autor="J. R. R. Tolkien",
            ano=1937
        )
    ]

    assert gerar_id(livros) == 3

def test_gerar_id_lista_vazia():
    livros = []

    assert gerar_id(livros) == 1


def test_gerar_id_com_ids_nao_sequenciais():
    livros = [
        Livro(
            id=1,
            titulo="Livro A",
            autor="Autor A",
            ano=2000
        ),
        Livro(
            id=2,
            titulo="Livro B",
            autor="Autor B",
            ano=2001
        ),
        Livro(
            id=5,
            titulo="Livro C",
            autor="Autor C",
            ano=2002
        )
    ]

    assert gerar_id(livros) == 6