# 📚 Sistema de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python.

O projeto permite cadastrar livros, realizar empréstimos e devoluções,
armazenar o histórico das operações e consultar informações dos livros.

---

## 🚀 Funcionalidades

- [x] Cadastrar livros
- [x] Listar livros
- [x] Buscar livros
- [x] Remover livros
- [x] Emprestar livros
- [x] Devolver livros
- [x] Histórico de empréstimos
- [x] Histórico por usuário
- [x] Histórico por livro
- [x] Persistência dos dados em JSON
- [x] Validação de entradas
- [ ] Testes automatizados

---

## 🛠️ Tecnologias

- **Python**
- **JSON**
- **Dataclasses**
- **Pytest**

---

## 📁 Estrutura do projeto

```text
Biblioteca/
│
├── main.py
├── livros.json
├── historico.json
│
├── models/
│   ├── __init__.py
│   ├── livro.py
│   └── historico.py
│
├── services/
│   ├── __init__.py
│   ├── livro_services.py
│   ├── emprestimo_services.py
│   ├── historico_services.py
│   └── menu_services.py
│
├── storage/
│   ├── __init__.py
│   └── json_storage.py
│
└── tests/
    └── test_livro_services.py