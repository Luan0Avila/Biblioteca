from dataclasses import dataclass
from datetime import datetime

@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    ano: int
    emprestado: bool = False

@dataclass
class HistoricoEmprestimo:
    livro_id: int
    titulo: str
    data_emprestimo: str
    data_devolucao: str | None = None