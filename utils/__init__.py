def formatarListagem(lista):
    print('-' * 60)
    print(f'{"LISTA DE CONTATOS":^40}')
    print('-' * 60)
    print('ID    NOME          NUMERO          ENDERECO       EMAIL')
    print('-' * 60)
    if type(lista) == list:
        for c in lista:
            print(f'[{c[0]}]   {c[1]}         {c[3]}      {c[2]}          {c[4]}')
    elif type(lista) == tuple:
        print(f'[{lista[0]}]   {lista[1]}         {lista[3]}      {lista[2]}          {lista[4]}')
