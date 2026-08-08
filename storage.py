import json
from dataclasses import asdict
from models import Livro, HistoricoEmprestimo

def salvar_livros(livros):
    livros_dict = [asdict(livro) for livro in livros]
    with open("livros.json", "w") as arquivo:
        json.dump(livros_dict, arquivo, indent=4)


def carregar_livros():
    try:
        with open("livros.json", "r") as arquivo:
            livros = json.load(arquivo)
            
        livros_objetos = [
            Livro(**dados)
            for dados in livros
        ]

        return livros_objetos
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_historico(historico):
    historico_dict = [asdict(registro) for registro in historico]
    with open("historico.json", "w") as arquivo:
        json.dump(historico_dict, arquivo, indent=4)


def carregar_historico():
    try:
        with open("historico.json", "r") as arquivo:
            historico = json.load(arquivo)
            
        historico_objetos = [
            HistoricoEmprestimo(**dados)
            for dados in historico
        ]

        return historico_objetos
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    