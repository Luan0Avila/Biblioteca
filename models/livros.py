from dataclasses import dataclass

@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    ano: int
    emprestado: bool = False