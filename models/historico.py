from dataclasses import dataclass

@dataclass
class HistoricoEmprestimo:
    livro_id: int
    titulo: str
    usuario: str
    data_emprestimo: str
    data_devolucao: str | None = None