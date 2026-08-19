from models import Livro
from pytest import MonkeyPatch, CaptureFixture
from services.livro_services import gerar_id, encontrar_livro_por_id, encontrar_livro_por_titulo,cadastrar_livro


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

def test_encontrar_livro_por_id():
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

    livro = encontrar_livro_por_id(livros, 2)

    assert livro is not None
    assert livro.titulo == "O Hobbit"

def test_encontrar_livro_por_id_nao_encontrado():
    livros = [
        Livro(
            id=1,
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano=1899
        )
    ]

    livro = encontrar_livro_por_id(livros, 99)

    assert livro is None

def test_encontrar_livro_por_titulo():
    livros = [
        Livro(
            id=1,
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano=1899
        )
    ]

    livro = encontrar_livro_por_titulo(livros, "Dom Casmurro")

    assert livro is not None
    assert livro.id == 1

def test_encontrar_livro_por_titulo_ignora_maiusculas():
    livros = [
        Livro(
            id=1,
            titulo="Dom Casmurro",
            autor="Machado de Assis",
            ano=1899
        )
    ]

    livro = encontrar_livro_por_titulo(livros, "dOm CaSmUrRo")

    assert livro is not None
    assert livro.id == 1

def test_cadastrar_livro(monkeypatch):
    entradas = iter([
        "Dom Casmurro",
        "Machado de Assis",
        "1899"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    livros = []
    livro = cadastrar_livro(livros)

    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.ano == 1899
    assert livro.id == 1

def test_cadastrar_livro_ano_invalido(monkeypatch, capsys):
    entradas = iter([
        "Dom Casmurro",
        "Machado de Assis",
        "abc",
        "1899"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    livros = []
    livro = cadastrar_livro(livros)

    captura = capsys.readouterr()

    assert "Digite um número válido." in captura.out
    assert livro.ano == 1899
