def listar_historico(historico):
    print("Este é o histórico")
    for registro in historico:
        print(f'Livro: {registro.titulo}\n'
        f'Usuário: {registro.usuario}\n'
        f'Empréstimo: {registro.data_emprestimo}'
        )

        if registro.data_devolucao is None:
            print('Devolução: Ainda está emprestado')
        else:
            print(f'Devolução: {registro.data_devolucao}')
        
        print("-" * 40)

def listar_historico_de_usuario(historico):
    usuario = input("Digite o nome do usuário: ")
    encontrado = False

    for registro in historico:
        if usuario.lower() == registro.usuario.lower():
            print(f'Livro: {registro.titulo}\n'
            f'Usuário: {registro.usuario}\n'
            f'Empréstimo: {registro.data_emprestimo}'
            )
            if registro.data_devolucao is None:
                print("Devolução: Ainda está emprestado")
            else:
                print(f"Devolução: {registro.data_devolucao}")

            print("-" * 40)
            encontrado = True
    
    if not encontrado:
        print("Usuário não encontrado! :(")

def listar_historico_de_livro(historico):
    livro = input("Digite o titulo do livro: ")
    encontrado = False

    for registro in historico:
        if livro.lower() == registro.titulo.lower():
            print(f'Livro: {registro.titulo}\n'
            f'Usuário: {registro.usuario}\n'
            f'Empréstimo: {registro.data_emprestimo}'
            )
            if registro.data_devolucao is None:
                print("Devolução: Ainda está emprestado")
            else:
                print(f"Devolução: {registro.data_devolucao}")

            print("-" * 40)
            encontrado = True
    
    if not encontrado:
        print("Livro não encontrado! :(")